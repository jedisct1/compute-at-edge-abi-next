#!/usr/bin/env python3
"""
Generate witx-next files from root WITX files.

This script transforms the legacy WITX format into the witx-codegen compatible format.
"""

import re
import os
import textwrap
from pathlib import Path


def find_balanced_expr(text, start_pos):
    """
    Find the end position of a balanced S-expression starting at start_pos.
    start_pos should point to the opening '('.
    Returns the position after the closing ')'.
    """
    if text[start_pos] != '(':
        raise ValueError("start_pos must point to an opening parenthesis")

    depth = 0
    in_string = False
    in_comment = False
    i = start_pos

    while i < len(text):
        char = text[i]

        # Handle line comments
        if not in_string and char == ';':
            # Check if it's a comment (;;; or ;;)
            if i + 1 < len(text) and text[i + 1] == ';':
                in_comment = True
                i += 1
                continue

        if in_comment:
            if char == '\n':
                in_comment = False
            i += 1
            continue

        # Handle strings
        if char == '"' and (i == 0 or text[i - 1] != '\\'):
            in_string = not in_string
            i += 1
            continue

        if in_string:
            i += 1
            continue

        # Track parentheses
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
            if depth == 0:
                return i + 1

        i += 1

    raise ValueError("Unbalanced parentheses")


def extract_modules(text):
    """
    Extract all top-level (module ...) blocks from text.
    Returns a list of tuples: (module_name, module_content, full_text_including_module_wrapper)
    """
    modules = []
    pos = 0

    while pos < len(text):
        # Find next module declaration
        match = re.search(r'\(module\s+\$(\w+)', text[pos:])
        if not match:
            break

        module_name = match.group(1)
        module_start = pos + match.start()

        # Find the end of this module
        try:
            module_end = find_balanced_expr(text, module_start)
            full_module_text = text[module_start:module_end]

            # Extract just the content inside the module (without the wrapping (module ...) part)
            # Find where the actual content starts (after "module $name")
            content_start = text.find('\n', module_start) + 1
            if content_start <= module_start:
                content_start = module_start + len(match.group(0)) + 1

            # Content is everything except the last closing paren and the opening
            inner_content = text[content_start:module_end - 1].strip()

            modules.append((module_name, inner_content, full_module_text))
            pos = module_end
        except ValueError:
            break

    return modules


def extract_types_before_module(text):
    """
    Extract type definitions that appear before the first (module ...) declaration.
    Returns (types_text, remaining_text)
    """
    match = re.search(r'\(module\s+\$\w+', text)
    if not match:
        return text.strip(), ""

    split_pos = match.start()
    types_text = text[:split_pos].strip()
    remaining_text = text[split_pos:]

    return types_text, remaining_text


def transform_handle_types(content, module_name):
    """
    Transform (typename $*_handle (handle)) declarations.

    For cache module: use $cache_handle_res
    Otherwise: use $http_handle from typenames
    """
    if module_name == "fastly_cache":
        # The cache module defines its own resource
        # Only transform the $cache_handle itself
        content = re.sub(
            r'\(typename \$cache_handle \(handle\)\)',
            r'(typename $cache_handle (handle $cache_handle_res))',
            content
        )
        return content

    # For all other modules, transform all handles to use $http_handle
    content = re.sub(
        r'\(typename \$(\w+_handle) \(handle\)\)',
        r'(typename $\1 (handle $http_handle))',
        content
    )

    return content


def transform_typenames(content):
    """
    Transform typenames.witx:
    - Wrap in (module $typenames ...)
    - Add (resource $http_handle) after opening
    - Transform handle types to use $http_handle
    """
    lines = content.strip().split('\n')

    # Add module wrapper
    result = "(module $typenames\n"

    # Find first typename or comment
    first_content_idx = 0
    for i, line in enumerate(lines):
        if line.strip() and not line.strip().startswith(';;;'):
            first_content_idx = i
            break

    # Add any leading comments
    for i in range(first_content_idx):
        result += "    " + lines[i] + "\n"

    # Transform handle definitions
    content_to_transform = '\n'.join(lines)

    # Transform all handle types to use $http_handle, but first we need to find
    # where to insert the resource declaration

    # Find the position after $body_write_end enum (before handle declarations)
    match = re.search(r'(\(typename \$body_write_end.*?\n.*?\$front\)\))', content_to_transform, re.DOTALL)

    if match:
        before_handles = content_to_transform[:match.end()]
        after_handles = content_to_transform[match.end():]

        # Add resource declaration
        result_content = before_handles + "\n\n    (resource $http_handle)\n" + after_handles
    else:
        result_content = content_to_transform

    # Transform all handle types
    result_content = re.sub(
        r'\(typename \$(\w+_handle) \(handle\)\)',
        r'(typename $\1 (handle $http_handle))',
        result_content
    )

    # Indent all lines
    indented_lines = []
    for line in result_content.split('\n'):
        if line.strip():
            indented_lines.append("    " + line)
        else:
            indented_lines.append("")

    result = "(module $typenames\n" + '\n'.join(indented_lines) + "\n)\n"

    return result


def transform_cache_module(types_content, module_content):
    """
    Transform cache.witx:
    - Add (use * from $typenames)
    - Add (resource $cache_handle_res)
    - Transform $cache_handle to use $cache_handle_res
    """
    result = "(module $fastly_cache\n"
    result += "    (use * from $typenames)\n"
    result += "    (resource $cache_handle_res)\n\n"

    # Combine types and module content
    combined = types_content + "\n\n" + module_content

    # Dedent to remove any existing indentation
    combined = textwrap.dedent(combined).strip()

    # Transform the cache_handle specifically
    combined = re.sub(
        r'\(typename \$cache_handle \(handle\)\)',
        r'(typename $cache_handle (handle $cache_handle_res))',
        combined
    )

    # Indent all lines
    for line in combined.split('\n'):
        if line.strip():
            result += "    " + line + "\n"
        else:
            result += "\n"

    result += ")\n"
    return result


def transform_config_store_module(types_content, module_content):
    """
    Transform config-store.witx:
    - Add (use * from $typenames)
    - Transform handles to use $http_handle
    """
    result = "(module $fastly_config_store\n"
    result += "    (use * from $typenames)\n\n"

    # Combine types and module content
    combined = types_content + "\n\n" + module_content

    # Dedent to remove any existing indentation
    combined = textwrap.dedent(combined).strip()

    # Transform handles to use $http_handle
    combined = re.sub(
        r'\(typename \$(\w+_handle) \(handle\)\)',
        r'(typename $\1 (handle $http_handle))',
        combined
    )

    # Indent all lines
    for line in combined.split('\n'):
        if line.strip():
            result += "    " + line + "\n"
        else:
            result += "\n"

    result += ")\n"
    return result


def transform_http_cache_module(types_content, module_content):
    """
    Transform http-cache.witx:
    - Add (use * from $typenames)
    - Add (resource $http_cache_handle_res)
    - Transform $http_cache_handle to use $http_cache_handle_res
    """
    result = "(module $fastly_http_cache\n"
    result += "    (use * from $typenames)\n"
    result += "    (resource $http_cache_handle_res)\n\n"

    # Combine types and module content
    combined = types_content + "\n\n" + module_content

    # Dedent to remove any existing indentation
    combined = textwrap.dedent(combined).strip()

    # Transform the http_cache_handle specifically
    combined = re.sub(
        r'\(typename \$http_cache_handle \(handle\)\)',
        r'(typename $http_cache_handle (handle $http_cache_handle_res))',
        combined
    )

    # Indent all lines
    for line in combined.split('\n'):
        if line.strip():
            result += "    " + line + "\n"
        else:
            result += "\n"

    result += ")\n"
    return result


def transform_shielding_module(types_content, module_content):
    """
    Transform shielding.witx:
    - Add (use * from $typenames)
    """
    result = "(module $fastly_shielding\n"
    result += "    (use * from $typenames)\n\n"

    # Combine types and module content
    combined = types_content + "\n\n" + module_content

    # Dedent to remove any existing indentation
    combined = textwrap.dedent(combined).strip()

    # Indent all lines
    for line in combined.split('\n'):
        if line.strip():
            result += "    " + line + "\n"
        else:
            result += "\n"

    result += ")\n"
    return result


def transform_standalone_module(module_name, module_content):
    """
    Transform a module from compute-at-edge.witx into a standalone file.
    - Add (use * from $typenames)
    - Keep module content as-is
    """
    result = f"(module ${module_name}\n"
    result += "    (use * from $typenames)\n\n"

    # Dedent to remove any existing indentation
    module_content = textwrap.dedent(module_content).strip()

    # Add module content with indentation
    for line in module_content.split('\n'):
        if line.strip():
            result += "    " + line + "\n"
        else:
            result += "\n"

    result += ")\n"
    return result


def main():
    """Main transformation function."""
    root_dir = Path(__file__).parent
    output_dir = root_dir / "tmp" / "witx-next-generated"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating witx-next files to: {output_dir}")

    # 1. Transform typenames.witx
    print("\n1. Transforming typenames.witx...")
    typenames_path = root_dir / "typenames.witx"
    with open(typenames_path, 'r') as f:
        typenames_content = f.read()

    transformed_typenames = transform_typenames(typenames_content)
    output_path = output_dir / "typenames.witx"
    with open(output_path, 'w') as f:
        f.write(transformed_typenames)
    print(f"   ✓ Generated {output_path}")

    # 2. Transform cache.witx
    print("\n2. Transforming cache.witx...")
    cache_path = root_dir / "cache.witx"
    with open(cache_path, 'r') as f:
        cache_content = f.read()

    types, remaining = extract_types_before_module(cache_content)
    modules = extract_modules(remaining)
    if modules:
        _, module_content, _ = modules[0]
        transformed_cache = transform_cache_module(types, module_content)
        output_path = output_dir / "fastly_cache.witx"
        with open(output_path, 'w') as f:
            f.write(transformed_cache)
        print(f"   ✓ Generated {output_path}")

    # 3. Transform config-store.witx
    print("\n3. Transforming config-store.witx...")
    config_path = root_dir / "config-store.witx"
    with open(config_path, 'r') as f:
        config_content = f.read()

    types, remaining = extract_types_before_module(config_content)
    modules = extract_modules(remaining)
    if modules:
        _, module_content, _ = modules[0]
        transformed_config = transform_config_store_module(types, module_content)
        output_path = output_dir / "fastly_config_store.witx"
        with open(output_path, 'w') as f:
            f.write(transformed_config)
        print(f"   ✓ Generated {output_path}")

    # 4. Transform http-cache.witx (if it has a module)
    print("\n4. Transforming http-cache.witx...")
    http_cache_path = root_dir / "http-cache.witx"
    with open(http_cache_path, 'r') as f:
        http_cache_content = f.read()

    types, remaining = extract_types_before_module(http_cache_content)
    modules = extract_modules(remaining)
    if modules:
        _, module_content, _ = modules[0]
        transformed_http_cache = transform_http_cache_module(types, module_content)
        output_path = output_dir / "fastly_http_cache.witx"
        with open(output_path, 'w') as f:
            f.write(transformed_http_cache)
        print(f"   ✓ Generated {output_path}")

    # 5. Transform shielding.witx
    print("\n5. Transforming shielding.witx...")
    shielding_path = root_dir / "shielding.witx"
    with open(shielding_path, 'r') as f:
        shielding_content = f.read()

    types, remaining = extract_types_before_module(shielding_content)
    modules = extract_modules(remaining)
    if modules:
        _, module_content, _ = modules[0]
        transformed_shielding = transform_shielding_module(types, module_content)
        output_path = output_dir / "fastly_shielding.witx"
        with open(output_path, 'w') as f:
            f.write(transformed_shielding)
        print(f"   ✓ Generated {output_path}")

    # 6. Transform compute-at-edge.witx - extract all modules
    print("\n6. Transforming compute-at-edge.witx...")
    compute_path = root_dir / "compute-at-edge.witx"
    with open(compute_path, 'r') as f:
        compute_content = f.read()

    # Skip the (use ...) statements at the beginning
    _, module_section = extract_types_before_module(compute_content)
    modules = extract_modules(module_section)

    print(f"   Found {len(modules)} modules:")
    for module_name, module_content, _ in modules:
        print(f"   - {module_name}")
        transformed = transform_standalone_module(module_name, module_content)
        output_path = output_dir / f"{module_name}.witx"
        with open(output_path, 'w') as f:
            f.write(transformed)
        print(f"     ✓ Generated {output_path}")

    print(f"\n✓ All files generated successfully to {output_dir}")
    print(f"\nGenerated {len(list(output_dir.glob('*.witx')))} files total")


if __name__ == "__main__":
    main()
