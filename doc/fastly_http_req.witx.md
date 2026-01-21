
# Module: fastly_http_req

## Table of contents

### Types list:

[**[All](#types)**] - [_[`fastly_status`](#fastly_status)_] - [_[`http_version`](#http_version)_] - [_[`http_status`](#http_status)_] - [_[`body_write_end`](#body_write_end)_] - [_[`body_handle`](#body_handle)_] - [_[`request_handle`](#request_handle)_] - [_[`response_handle`](#response_handle)_] - [_[`pending_request_handle`](#pending_request_handle)_] - [_[`endpoint_handle`](#endpoint_handle)_] - [_[`dictionary_handle`](#dictionary_handle)_] - [_[`object_store_handle`](#object_store_handle)_] - [_[`pending_kv_lookup_handle`](#pending_kv_lookup_handle)_] - [_[`pending_kv_insert_handle`](#pending_kv_insert_handle)_] - [_[`pending_kv_delete_handle`](#pending_kv_delete_handle)_] - [_[`pending_kv_list_handle`](#pending_kv_list_handle)_] - [_[`kv_store_handle`](#kv_store_handle)_] - [_[`kv_store_lookup_handle`](#kv_store_lookup_handle)_] - [_[`kv_store_insert_handle`](#kv_store_insert_handle)_] - [_[`kv_store_delete_handle`](#kv_store_delete_handle)_] - [_[`kv_store_list_handle`](#kv_store_list_handle)_] - [_[`secret_store_handle`](#secret_store_handle)_] - [_[`secret_handle`](#secret_handle)_] - [_[`acl_handle`](#acl_handle)_] - [_[`request_promise_handle`](#request_promise_handle)_] - [_[`async_item_handle`](#async_item_handle)_] - [_[`multi_value_cursor`](#multi_value_cursor)_] - [_[`multi_value_cursor_result`](#multi_value_cursor_result)_] - [_[`cache_override_tag`](#cache_override_tag)_] - [_[`num_bytes`](#num_bytes)_] - [_[`header_count`](#header_count)_] - [_[`is_done`](#is_done)_] - [_[`done_idx`](#done_idx)_] - [_[`is_valid`](#is_valid)_] - [_[`inserted`](#inserted)_] - [_[`ready_idx`](#ready_idx)_] - [_[`ddos_detected`](#ddos_detected)_] - [_[`port`](#port)_] - [_[`timeout_ms`](#timeout_ms)_] - [_[`timeout_secs`](#timeout_secs)_] - [_[`probe_count`](#probe_count)_] - [_[`backend_exists`](#backend_exists)_] - [_[`is_dynamic`](#is_dynamic)_] - [_[`is_keepalive`](#is_keepalive)_] - [_[`is_ssl`](#is_ssl)_] - [_[`backend_health`](#backend_health)_] - [_[`content_encodings`](#content_encodings)_] - [_[`framing_headers_mode`](#framing_headers_mode)_] - [_[`http_keepalive_mode`](#http_keepalive_mode)_] - [_[`tls_version`](#tls_version)_] - [_[`kv_lookup_config_options`](#kv_lookup_config_options)_] - [_[`kv_lookup_config`](#kv_lookup_config)_] - [_[`kv_delete_config_options`](#kv_delete_config_options)_] - [_[`kv_delete_config`](#kv_delete_config)_] - [_[`kv_insert_config_options`](#kv_insert_config_options)_] - [_[`kv_insert_mode`](#kv_insert_mode)_] - [_[`kv_insert_config`](#kv_insert_config)_] - [_[`kv_list_config_options`](#kv_list_config_options)_] - [_[`kv_list_mode`](#kv_list_mode)_] - [_[`kv_list_config`](#kv_list_config)_] - [_[`kv_error`](#kv_error)_] - [_[`backend_config_options`](#backend_config_options)_] - [_[`dynamic_backend_config`](#dynamic_backend_config)_] - [_[`client_cert_verify_result`](#client_cert_verify_result)_] - [_[`purge_options_mask`](#purge_options_mask)_] - [_[`purge_options`](#purge_options)_] - [_[`send_error_detail_tag`](#send_error_detail_tag)_] - [_[`send_error_detail_mask`](#send_error_detail_mask)_] - [_[`send_error_detail`](#send_error_detail)_] - [_[`blocked`](#blocked)_] - [_[`rate`](#rate)_] - [_[`count`](#count)_] - [_[`has`](#has)_] - [_[`body_length`](#body_length)_] - [_[`vcpu_ms`](#vcpu_ms)_] - [_[`memory_mib`](#memory_mib)_] - [_[`inspect_info_mask`](#inspect_info_mask)_] - [_[`inspect_info`](#inspect_info)_] - [_[`acl_error`](#acl_error)_] - [_[`image_optimizer_transform_config_options`](#image_optimizer_transform_config_options)_] - [_[`image_optimizer_transform_config`](#image_optimizer_transform_config)_] - [_[`image_optimizer_error_tag`](#image_optimizer_error_tag)_] - [_[`image_optimizer_error_detail`](#image_optimizer_error_detail)_] - [_[`next_request_options_mask`](#next_request_options_mask)_] - [_[`next_request_options`](#next_request_options)_]

### Functions list:

[**[All](#functions)**] - [[`body_downstream_get()`](#body_downstream_get)] - [[`cache_override_set()`](#cache_override_set)] - [[`cache_override_v2_set()`](#cache_override_v2_set)] - [[`downstream_client_ip_addr()`](#downstream_client_ip_addr)] - [[`downstream_server_ip_addr()`](#downstream_server_ip_addr)] - [[`downstream_client_h2_fingerprint()`](#downstream_client_h2_fingerprint)] - [[`downstream_client_request_id()`](#downstream_client_request_id)] - [[`downstream_client_oh_fingerprint()`](#downstream_client_oh_fingerprint)] - [[`downstream_client_ddos_detected()`](#downstream_client_ddos_detected)] - [[`downstream_tls_cipher_openssl_name()`](#downstream_tls_cipher_openssl_name)] - [[`downstream_tls_protocol()`](#downstream_tls_protocol)] - [[`downstream_tls_client_hello()`](#downstream_tls_client_hello)] - [[`downstream_tls_raw_client_certificate()`](#downstream_tls_raw_client_certificate)] - [[`downstream_tls_client_cert_verify_result()`](#downstream_tls_client_cert_verify_result)] - [[`downstream_tls_ja3_md5()`](#downstream_tls_ja3_md5)] - [[`downstream_tls_ja4()`](#downstream_tls_ja4)] - [[`downstream_compliance_region()`](#downstream_compliance_region)] - [[`new()`](#new)] - [[`header_names_get()`](#header_names_get)] - [[`original_header_names_get()`](#original_header_names_get)] - [[`original_header_count()`](#original_header_count)] - [[`header_value_get()`](#header_value_get)] - [[`header_values_get()`](#header_values_get)] - [[`header_values_set()`](#header_values_set)] - [[`header_insert()`](#header_insert)] - [[`header_append()`](#header_append)] - [[`header_remove()`](#header_remove)] - [[`method_get()`](#method_get)] - [[`method_set()`](#method_set)] - [[`uri_get()`](#uri_get)] - [[`uri_set()`](#uri_set)] - [[`version_get()`](#version_get)] - [[`version_set()`](#version_set)] - [[`send()`](#send)] - [[`send_v2()`](#send_v2)] - [[`send_v3()`](#send_v3)] - [[`send_async()`](#send_async)] - [[`send_async_v2()`](#send_async_v2)] - [[`send_async_streaming()`](#send_async_streaming)] - [[`pending_req_poll()`](#pending_req_poll)] - [[`pending_req_poll_v2()`](#pending_req_poll_v2)] - [[`pending_req_wait()`](#pending_req_wait)] - [[`pending_req_wait_v2()`](#pending_req_wait_v2)] - [[`pending_req_select()`](#pending_req_select)] - [[`pending_req_select_v2()`](#pending_req_select_v2)] - [[`fastly_key_is_valid()`](#fastly_key_is_valid)] - [[`close()`](#close)] - [[`auto_decompress_response_set()`](#auto_decompress_response_set)] - [[`upgrade_websocket()`](#upgrade_websocket)] - [[`redirect_to_websocket_proxy()`](#redirect_to_websocket_proxy)] - [[`redirect_to_grip_proxy()`](#redirect_to_grip_proxy)] - [[`redirect_to_websocket_proxy_v2()`](#redirect_to_websocket_proxy_v2)] - [[`redirect_to_grip_proxy_v2()`](#redirect_to_grip_proxy_v2)] - [[`framing_headers_mode_set()`](#framing_headers_mode_set)] - [[`register_dynamic_backend()`](#register_dynamic_backend)] - [[`inspect()`](#inspect)] - [[`on_behalf_of()`](#on_behalf_of)]

## Types

### _[`fastly_status`](#fastly_status)_

Enumeration with tag type: `u32`, and the following members:

* **`ok`**: _[`fastly_status`](#fastly_status)_
* **`error`**: _[`fastly_status`](#fastly_status)_
* **`inval`**: _[`fastly_status`](#fastly_status)_
* **`badf`**: _[`fastly_status`](#fastly_status)_
* **`buflen`**: _[`fastly_status`](#fastly_status)_
* **`unsupported`**: _[`fastly_status`](#fastly_status)_
* **`badalign`**: _[`fastly_status`](#fastly_status)_
* **`httpinvalid`**: _[`fastly_status`](#fastly_status)_
* **`httpuser`**: _[`fastly_status`](#fastly_status)_
* **`httpincomplete`**: _[`fastly_status`](#fastly_status)_
* **`none`**: _[`fastly_status`](#fastly_status)_
* **`httpheadtoolarge`**: _[`fastly_status`](#fastly_status)_
* **`httpinvalidstatus`**: _[`fastly_status`](#fastly_status)_
* **`limitexceeded`**: _[`fastly_status`](#fastly_status)_
* **`again`**: _[`fastly_status`](#fastly_status)_

> Status codes returned from hostcalls.


---

### _[`http_version`](#http_version)_

Enumeration with tag type: `u32`, and the following members:

* **`http_09`**: _[`http_version`](#http_version)_
* **`http_10`**: _[`http_version`](#http_version)_
* **`http_11`**: _[`http_version`](#http_version)_
* **`h2`**: _[`http_version`](#http_version)_
* **`h3`**: _[`http_version`](#http_version)_

> A tag indicating HTTP protocol versions.


---

### _[`http_status`](#http_status)_
Alias for `u16`.


> HTTP status codes.


---

### _[`body_write_end`](#body_write_end)_

Enumeration with tag type: `u32`, and the following members:

* **`back`**: _[`body_write_end`](#body_write_end)_
* **`front`**: _[`body_write_end`](#body_write_end)_

---

### _[`body_handle`](#body_handle)_
Alias for `handle`.


> A handle to an HTTP request or response body.


---

### _[`request_handle`](#request_handle)_
Alias for `handle`.


> A handle to an HTTP request.


---

### _[`response_handle`](#response_handle)_
Alias for `handle`.


> A handle to an HTTP response.


---

### _[`pending_request_handle`](#pending_request_handle)_
Alias for `handle`.


> A handle to a currently-pending asynchronous HTTP request.


---

### _[`endpoint_handle`](#endpoint_handle)_
Alias for `handle`.


> A handle to a logging endpoint.


---

### _[`dictionary_handle`](#dictionary_handle)_
Alias for `handle`.


> A handle to an Edge Dictionary.


---

### _[`object_store_handle`](#object_store_handle)_
Alias for `handle`.


> (DEPRECATED) A handle to an Object Store.


---

### _[`pending_kv_lookup_handle`](#pending_kv_lookup_handle)_
Alias for `handle`.


> (DEPRECATED) A handle to a pending KV lookup.


---

### _[`pending_kv_insert_handle`](#pending_kv_insert_handle)_
Alias for `handle`.


> (DEPRECATED) A handle to a pending KV insert.


---

### _[`pending_kv_delete_handle`](#pending_kv_delete_handle)_
Alias for `handle`.


> (DEPRECATED) A handle to a pending KV delete.


---

### _[`pending_kv_list_handle`](#pending_kv_list_handle)_
Alias for `handle`.


> (DEPRECATED) A handle to a pending KV list.


---

### _[`kv_store_handle`](#kv_store_handle)_
Alias for `handle`.


> A handle to an KV Store.


---

### _[`kv_store_lookup_handle`](#kv_store_lookup_handle)_
Alias for `handle`.


> A handle to a KV Store lookup.


---

### _[`kv_store_insert_handle`](#kv_store_insert_handle)_
Alias for `handle`.


> A handle to a KV Store insert.


---

### _[`kv_store_delete_handle`](#kv_store_delete_handle)_
Alias for `handle`.


> A handle to a KV Store delete.


---

### _[`kv_store_list_handle`](#kv_store_list_handle)_
Alias for `handle`.


> A handle to a KV Store list.


---

### _[`secret_store_handle`](#secret_store_handle)_
Alias for `handle`.


> A handle to a Secret Store.


---

### _[`secret_handle`](#secret_handle)_
Alias for `handle`.


> A handle to an individual secret.


---

### _[`acl_handle`](#acl_handle)_
Alias for `handle`.


> A handle to an ACL.


---

### _[`request_promise_handle`](#request_promise_handle)_
Alias for `handle`.


> A handle to a request promise.


---

### _[`async_item_handle`](#async_item_handle)_
Alias for `handle`.


> A handle to an object supporting generic async operations.
> Can be a `body_handle`, `pending_request_handle`,
> `cache_handle`, `cache_busy_handle`, `cache_replace_handle` (see cache.witx),
> `request_promise_handle`, or other handles.
>
> Each async item has an associated I/O action:
>
> * Pending requests: awaiting the response headers / `Response` object
> * Normal bodies: reading bytes from the body
> * Streaming bodies: writing bytes to the body
> * Cache handles: the caller has been selected to perform a fetch, or there is data ready
> * Request promise: a new request is ready, or there will be no request provided via this handle
>
> For writing bytes, note that there is a large host-side buffer that bytes can eagerly be written
> into, even before the origin itself consumes that data.


---

### _[`multi_value_cursor`](#multi_value_cursor)_
Alias for `u32`.


> A "multi-value" cursor.


---

### _[`multi_value_cursor_result`](#multi_value_cursor_result)_
Alias for `i64`.


> -1 represents "finished", non-negative represents a $multi_value_cursor:


---

### _[`cache_override_tag`](#cache_override_tag)_

Set of constants, of type `u32`

Predefined constants for _[`cache_override_tag`](#cache_override_tag)_:

* **`pass`** = `0x1`
* **`ttl`** = `0x2`
* **`stale_while_revalidate`** = `0x4`
* **`pci`** = `0x8`

> An override for response caching behavior.
> A zero value indicates that the origin response's cache control headers should be used.


---

### _[`num_bytes`](#num_bytes)_
Alias for `usize`.


---

### _[`header_count`](#header_count)_
Alias for `u32`.


---

### _[`is_done`](#is_done)_
Alias for `u32`.


---

### _[`done_idx`](#done_idx)_
Alias for `u32`.


---

### _[`is_valid`](#is_valid)_
Alias for `u32`.


---

### _[`inserted`](#inserted)_
Alias for `u32`.


---

### _[`ready_idx`](#ready_idx)_
Alias for `u32`.


---

### _[`ddos_detected`](#ddos_detected)_
Alias for `u32`.


---

### _[`port`](#port)_
Alias for `u16`.


---

### _[`timeout_ms`](#timeout_ms)_
Alias for `u32`.


---

### _[`timeout_secs`](#timeout_secs)_
Alias for `u32`.


---

### _[`probe_count`](#probe_count)_
Alias for `u32`.


---

### _[`backend_exists`](#backend_exists)_
Alias for `u32`.


---

### _[`is_dynamic`](#is_dynamic)_
Alias for `u32`.


---

### _[`is_keepalive`](#is_keepalive)_
Alias for `u32`.


---

### _[`is_ssl`](#is_ssl)_
Alias for `u32`.


---

### _[`backend_health`](#backend_health)_

Enumeration with tag type: `u32`, and the following members:

* **`unknown`**: _[`backend_health`](#backend_health)_
* **`healthy`**: _[`backend_health`](#backend_health)_
* **`unhealthy`**: _[`backend_health`](#backend_health)_

---

### _[`content_encodings`](#content_encodings)_

Set of constants, of type `u32`

Predefined constants for _[`content_encodings`](#content_encodings)_:

* **`gzip`** = `1`

---

### _[`framing_headers_mode`](#framing_headers_mode)_

Enumeration with tag type: `u32`, and the following members:

* **`automatic`**: _[`framing_headers_mode`](#framing_headers_mode)_
* **`manually_from_headers`**: _[`framing_headers_mode`](#framing_headers_mode)_

---

### _[`http_keepalive_mode`](#http_keepalive_mode)_

Enumeration with tag type: `u32`, and the following members:

* **`automatic`**: _[`http_keepalive_mode`](#http_keepalive_mode)_
* **`no_keepalive`**: _[`http_keepalive_mode`](#http_keepalive_mode)_

---

### _[`tls_version`](#tls_version)_

Enumeration with tag type: `u32`, and the following members:

* **`tls_1`**: _[`tls_version`](#tls_version)_
* **`tls_1_1`**: _[`tls_version`](#tls_version)_
* **`tls_1_2`**: _[`tls_version`](#tls_version)_
* **`tls_1_3`**: _[`tls_version`](#tls_version)_

---

### _[`kv_lookup_config_options`](#kv_lookup_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`kv_lookup_config_options`](#kv_lookup_config_options)_:

* **`reserved`** = `1`

---

### _[`kv_lookup_config`](#kv_lookup_config)_
Structure, with the following members:

* **`reserved`**: `u32`

---

### _[`kv_delete_config_options`](#kv_delete_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`kv_delete_config_options`](#kv_delete_config_options)_:

* **`reserved`** = `1`

---

### _[`kv_delete_config`](#kv_delete_config)_
Structure, with the following members:

* **`reserved`**: `u32`

---

### _[`kv_insert_config_options`](#kv_insert_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`kv_insert_config_options`](#kv_insert_config_options)_:

* **`reserved`** = `0x1`
* **`background_fetch`** = `0x2`
* **`reserved_2`** = `0x4`
* **`metadata`** = `0x8`
* **`time_to_live_sec`** = `0x10`
* **`if_generation_match`** = `0x20`

---

### _[`kv_insert_mode`](#kv_insert_mode)_

Enumeration with tag type: `u32`, and the following members:

* **`overwrite`**: _[`kv_insert_mode`](#kv_insert_mode)_
* **`add`**: _[`kv_insert_mode`](#kv_insert_mode)_
* **`append`**: _[`kv_insert_mode`](#kv_insert_mode)_
* **`prepend`**: _[`kv_insert_mode`](#kv_insert_mode)_

---

### _[`kv_insert_config`](#kv_insert_config)_
Structure, with the following members:

* **`mode`**: _[`kv_insert_mode`](#kv_insert_mode)_
* **`unused`**: `u32`
* **`metadata`**: `char8` mutable pointer
* **`metadata_len`**: `u32`
* **`time_to_live_sec`**: `u32`
* **`if_generation_match`**: `u64`

---

### _[`kv_list_config_options`](#kv_list_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`kv_list_config_options`](#kv_list_config_options)_:

* **`reserved`** = `0x1`
* **`cursor`** = `0x2`
* **`limit`** = `0x4`
* **`prefix`** = `0x8`

---

### _[`kv_list_mode`](#kv_list_mode)_

Enumeration with tag type: `u32`, and the following members:

* **`strong`**: _[`kv_list_mode`](#kv_list_mode)_
* **`eventual`**: _[`kv_list_mode`](#kv_list_mode)_

---

### _[`kv_list_config`](#kv_list_config)_
Structure, with the following members:

* **`mode`**: _[`kv_list_mode`](#kv_list_mode)_
* **`cursor`**: `char8` mutable pointer
* **`cursor_len`**: `u32`
* **`limit`**: `u32`
* **`prefix`**: `char8` mutable pointer
* **`prefix_len`**: `u32`

---

### _[`kv_error`](#kv_error)_

Enumeration with tag type: `u32`, and the following members:

* **`uninitialized`**: _[`kv_error`](#kv_error)_
* **`ok`**: _[`kv_error`](#kv_error)_
* **`bad_request`**: _[`kv_error`](#kv_error)_
* **`not_found`**: _[`kv_error`](#kv_error)_
* **`precondition_failed`**: _[`kv_error`](#kv_error)_
* **`payload_too_large`**: _[`kv_error`](#kv_error)_
* **`internal_error`**: _[`kv_error`](#kv_error)_
* **`too_many_requests`**: _[`kv_error`](#kv_error)_

---

### _[`backend_config_options`](#backend_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`backend_config_options`](#backend_config_options)_:

* **`reserved`** = `0x1`
* **`host_override`** = `0x2`
* **`connect_timeout`** = `0x4`
* **`first_byte_timeout`** = `0x8`
* **`between_bytes_timeout`** = `0x10`
* **`use_ssl`** = `0x20`
* **`ssl_min_version`** = `0x40`
* **`ssl_max_version`** = `0x80`
* **`cert_hostname`** = `0x100`
* **`ca_cert`** = `0x200`
* **`ciphers`** = `0x400`
* **`sni_hostname`** = `0x800`
* **`dont_pool`** = `0x1000`
* **`client_cert`** = `0x2000`
* **`grpc`** = `0x4000`
* **`keepalive`** = `0x8000`
* **`pooling_limits`** = `0x10000`
* **`prefer_ipv4`** = `0x20000`

---

### _[`dynamic_backend_config`](#dynamic_backend_config)_
Structure, with the following members:

* **`host_override`**: `char8` mutable pointer
* **`host_override_len`**: `u32`
* **`connect_timeout_ms`**: `u32`
* **`first_byte_timeout_ms`**: `u32`
* **`between_bytes_timeout_ms`**: `u32`
* **`ssl_min_version`**: _[`tls_version`](#tls_version)_
* **`ssl_max_version`**: _[`tls_version`](#tls_version)_
* **`cert_hostname`**: `char8` mutable pointer
* **`cert_hostname_len`**: `u32`
* **`ca_cert`**: `char8` mutable pointer
* **`ca_cert_len`**: `u32`
* **`ciphers`**: `char8` mutable pointer
* **`ciphers_len`**: `u32`
* **`sni_hostname`**: `char8` mutable pointer
* **`sni_hostname_len`**: `u32`
* **`client_certificate`**: `char8` mutable pointer
* **`client_certificate_len`**: `u32`
* **`client_key`**: _[`secret_handle`](#secret_handle)_
* **`http_keepalive_time_ms`**: _[`timeout_ms`](#timeout_ms)_
* **`tcp_keepalive_enable`**: `u32`
* **`tcp_keepalive_interval_secs`**: _[`timeout_secs`](#timeout_secs)_
* **`tcp_keepalive_probes`**: _[`probe_count`](#probe_count)_
* **`tcp_keepalive_time_secs`**: _[`timeout_secs`](#timeout_secs)_
* **`max_connections`**: `u32`
* **`max_use`**: `u32`
* **`max_lifetime_ms`**: _[`timeout_ms`](#timeout_ms)_

---

### _[`client_cert_verify_result`](#client_cert_verify_result)_

Enumeration with tag type: `u32`, and the following members:

* **`ok`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`bad_certificate`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`certificate_revoked`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`certificate_expired`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`unknown_ca`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`certificate_missing`**: _[`client_cert_verify_result`](#client_cert_verify_result)_
* **`certificate_unknown`**: _[`client_cert_verify_result`](#client_cert_verify_result)_

> TLS client certificate verified result from downstream.


---

### _[`purge_options_mask`](#purge_options_mask)_

Set of constants, of type `u32`

Predefined constants for _[`purge_options_mask`](#purge_options_mask)_:

* **`soft_purge`** = `1`
* **`ret_buf`** = `2`

---

### _[`purge_options`](#purge_options)_
Structure, with the following members:

* **`ret_buf_ptr`**: `u8` mutable pointer
* **`ret_buf_len`**: `usize`
* **`ret_buf_nwritten_out`**: `usize` mutable pointer

---

### _[`send_error_detail_tag`](#send_error_detail_tag)_

Enumeration with tag type: `u32`, and the following members:

* **`uninitialized`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`ok`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`dns_timeout`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`dns_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`destination_not_found`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`destination_unavailable`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`destination_ip_unroutable`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`connection_refused`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`connection_terminated`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`connection_timeout`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`connection_limit_reached`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`tls_certificate_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`tls_configuration_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_incomplete_response`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_response_header_section_too_large`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_response_body_too_large`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_response_timeout`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_response_status_invalid`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_upgrade_failed`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_protocol_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_request_cache_key_invalid`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`http_request_uri_invalid`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`internal_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`tls_alert_received`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`tls_protocol_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_

---

### _[`send_error_detail_mask`](#send_error_detail_mask)_

Set of constants, of type `u32`

Predefined constants for _[`send_error_detail_mask`](#send_error_detail_mask)_:

* **`reserved`** = `0x1`
* **`dns_error_rcode`** = `0x2`
* **`dns_error_info_code`** = `0x4`
* **`tls_alert_id`** = `0x8`

> Mask representing which fields are understood by the guest, and which have been set by the host.
>
> When the guest calls hostcalls with a mask, it should set every bit in the mask that corresponds
> to a defined flag. This signals the host to write only to fields with a set bit, allowing
> forward compatibility for existing guest programs even after new fields are added to the struct.


---

### _[`send_error_detail`](#send_error_detail)_
Structure, with the following members:

* **`tag`**: _[`send_error_detail_tag`](#send_error_detail_tag)_
* **`mask`**: _[`send_error_detail_mask`](#send_error_detail_mask)_
* **`dns_error_rcode`**: `u16`
* **`dns_error_info_code`**: `u16`
* **`tls_alert_id`**: `u8`

---

### _[`blocked`](#blocked)_
Alias for `u32`.


---

### _[`rate`](#rate)_
Alias for `u32`.


---

### _[`count`](#count)_
Alias for `u32`.


---

### _[`has`](#has)_
Alias for `u32`.


---

### _[`body_length`](#body_length)_
Alias for `u64`.


---

### _[`vcpu_ms`](#vcpu_ms)_
Alias for `u64`.


---

### _[`memory_mib`](#memory_mib)_
Alias for `u32`.


---

### _[`inspect_info_mask`](#inspect_info_mask)_

Set of constants, of type `u32`

Predefined constants for _[`inspect_info_mask`](#inspect_info_mask)_:

* **`reserved`** = `0x1`
* **`corp`** = `0x2`
* **`workspace`** = `0x4`
* **`override_client_ip`** = `0x8`

---

### _[`inspect_info`](#inspect_info)_
Structure, with the following members:

* **`corp`**: `char8` mutable pointer
* **`corp_len`**: `u32`
* **`workspace`**: `char8` mutable pointer
* **`workspace_len`**: `u32`
* **`override_client_ip_ptr`**: `u8` mutable pointer
* **`override_client_ip_len`**: `u32`

---

### _[`acl_error`](#acl_error)_

Enumeration with tag type: `u32`, and the following members:

* **`uninitialized`**: _[`acl_error`](#acl_error)_
* **`ok`**: _[`acl_error`](#acl_error)_
* **`no_content`**: _[`acl_error`](#acl_error)_
* **`too_many_requests`**: _[`acl_error`](#acl_error)_

---

### _[`image_optimizer_transform_config_options`](#image_optimizer_transform_config_options)_

Set of constants, of type `u32`

Predefined constants for _[`image_optimizer_transform_config_options`](#image_optimizer_transform_config_options)_:

* **`reserved`** = `1`
* **`sdk_claims_opts`** = `2`

---

### _[`image_optimizer_transform_config`](#image_optimizer_transform_config)_
Structure, with the following members:

* **`sdk_claims_opts`**: `char8` mutable pointer
* **`sdk_claims_opts_len`**: `u32`

---

### _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_

Enumeration with tag type: `u32`, and the following members:

* **`uninitialized`**: _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_
* **`ok`**: _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_
* **`error`**: _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_
* **`warning`**: _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_

---

### _[`image_optimizer_error_detail`](#image_optimizer_error_detail)_
Structure, with the following members:

* **`tag`**: _[`image_optimizer_error_tag`](#image_optimizer_error_tag)_
* **`message`**: `char8` mutable pointer
* **`message_len`**: `u32`

---

### _[`next_request_options_mask`](#next_request_options_mask)_

Set of constants, of type `u32`

Predefined constants for _[`next_request_options_mask`](#next_request_options_mask)_:

* **`reserved`** = `1`
* **`timeout`** = `2`

---

### _[`next_request_options`](#next_request_options)_
Structure, with the following members:

* **`timeout_ms`**: `u64`

---

## Functions

### [`body_downstream_get()`](#body_downstream_get)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`request_handle`](#request_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`cache_override_set()`](#cache_override_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`tag`**: _[`cache_override_tag`](#cache_override_tag)_
* **`ttl`**: `u32`
* **`stale_while_revalidate`**: `u32`

This function has no output.

---

### [`cache_override_v2_set()`](#cache_override_v2_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`tag`**: _[`cache_override_tag`](#cache_override_tag)_
* **`ttl`**: `u32`
* **`stale_while_revalidate`**: `u32`
* **`sk`**: `u8` mutable slice

This function has no output.

---

### [`downstream_client_ip_addr()`](#downstream_client_ip_addr)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`addr_octets_out`**: `char8` mutable pointer

#### Output:

* _[`num_bytes`](#num_bytes)_ mutable pointer

---

### [`downstream_server_ip_addr()`](#downstream_server_ip_addr)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`addr_octets_out`**: `char8` mutable pointer

#### Output:

* _[`num_bytes`](#num_bytes)_ mutable pointer

---

### [`downstream_client_h2_fingerprint()`](#downstream_client_h2_fingerprint)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h2fp_out`**: `char8` mutable pointer
* **`h2fp_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_client_request_id()`](#downstream_client_request_id)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`reqid_out`**: `char8` mutable pointer
* **`reqid_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_client_oh_fingerprint()`](#downstream_client_oh_fingerprint)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`ohfp_out`**: `char8` mutable pointer
* **`ohfp_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_client_ddos_detected()`](#downstream_client_ddos_detected)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`ddos_detected`](#ddos_detected)_ mutable pointer

---

### [`downstream_tls_cipher_openssl_name()`](#downstream_tls_cipher_openssl_name)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`cipher_out`**: `char8` mutable pointer
* **`cipher_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_tls_protocol()`](#downstream_tls_protocol)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`protocol_out`**: `char8` mutable pointer
* **`protocol_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_tls_client_hello()`](#downstream_tls_client_hello)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`chello_out`**: `char8` mutable pointer
* **`chello_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_tls_raw_client_certificate()`](#downstream_tls_raw_client_certificate)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`raw_client_cert_out`**: `char8` mutable pointer
* **`raw_client_cert_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_tls_client_cert_verify_result()`](#downstream_tls_client_cert_verify_result)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`client_cert_verify_result`](#client_cert_verify_result)_ mutable pointer

---

### [`downstream_tls_ja3_md5()`](#downstream_tls_ja3_md5)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`cja3_md5_out`**: `char8` mutable pointer

#### Output:

* _[`num_bytes`](#num_bytes)_ mutable pointer

---

### [`downstream_tls_ja4()`](#downstream_tls_ja4)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`ja4_out`**: `char8` mutable pointer
* **`ja4_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`downstream_compliance_region()`](#downstream_compliance_region)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`region_out`**: `char8` mutable pointer
* **`region_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`new()`](#new)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`request_handle`](#request_handle)_ mutable pointer

---

### [`header_names_get()`](#header_names_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`cursor`**: _[`multi_value_cursor`](#multi_value_cursor)_
* **`ending_cursor_out`**: _[`multi_value_cursor_result`](#multi_value_cursor_result)_ mutable pointer
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`original_header_names_get()`](#original_header_names_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`cursor`**: _[`multi_value_cursor`](#multi_value_cursor)_
* **`ending_cursor_out`**: _[`multi_value_cursor_result`](#multi_value_cursor_result)_ mutable pointer
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`original_header_count()`](#original_header_count)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`header_count`](#header_count)_ mutable pointer

---

### [`header_value_get()`](#header_value_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `char8` mutable pointer
* **`value_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`header_values_get()`](#header_values_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`cursor`**: _[`multi_value_cursor`](#multi_value_cursor)_
* **`ending_cursor_out`**: _[`multi_value_cursor_result`](#multi_value_cursor_result)_ mutable pointer
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`header_values_set()`](#header_values_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice
* **`values`**: `string`

This function has no output.

---

### [`header_insert()`](#header_insert)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `u8` mutable slice

This function has no output.

---

### [`header_append()`](#header_append)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `u8` mutable slice

This function has no output.

---

### [`header_remove()`](#header_remove)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`name`**: `u8` mutable slice

This function has no output.

---

### [`method_get()`](#method_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`method_set()`](#method_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`method`**: `string`

This function has no output.

---

### [`uri_get()`](#uri_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`uri_set()`](#uri_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`uri`**: `string`

This function has no output.

---

### [`version_get()`](#version_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_

#### Output:

* _[`http_version`](#http_version)_ mutable pointer

---

### [`version_set()`](#version_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`version`**: _[`http_version`](#http_version)_

This function has no output.

---

### [`send()`](#send)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`send_v2()`](#send_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`
* **`error_detail`**: _[`send_error_detail`](#send_error_detail)_ mutable pointer

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`send_v3()`](#send_v3)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`
* **`error_detail`**: _[`send_error_detail`](#send_error_detail)_ mutable pointer

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`send_async()`](#send_async)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`

#### Output:

* _[`pending_request_handle`](#pending_request_handle)_ mutable pointer

---

### [`send_async_v2()`](#send_async_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`
* **`streaming`**: `u32`

#### Output:

* _[`pending_request_handle`](#pending_request_handle)_ mutable pointer

---

### [`send_async_streaming()`](#send_async_streaming)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`backend`**: `string`

#### Output:

* _[`pending_request_handle`](#pending_request_handle)_ mutable pointer

---

### [`pending_req_poll()`](#pending_req_poll)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`pending_request_handle`](#pending_request_handle)_

#### Output:

* _[`is_done`](#is_done)_ mutable pointer
* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`pending_req_poll_v2()`](#pending_req_poll_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`pending_request_handle`](#pending_request_handle)_
* **`error_detail`**: _[`send_error_detail`](#send_error_detail)_ mutable pointer

#### Output:

* _[`is_done`](#is_done)_ mutable pointer
* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`pending_req_wait()`](#pending_req_wait)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`pending_request_handle`](#pending_request_handle)_

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`pending_req_wait_v2()`](#pending_req_wait_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`pending_request_handle`](#pending_request_handle)_
* **`error_detail`**: _[`send_error_detail`](#send_error_detail)_ mutable pointer

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`pending_req_select()`](#pending_req_select)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`hs`**: _[`pending_request_handle`](#pending_request_handle)_ mutable slice

#### Output:

* _[`done_idx`](#done_idx)_ mutable pointer
* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`pending_req_select_v2()`](#pending_req_select_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`hs`**: _[`pending_request_handle`](#pending_request_handle)_ mutable slice
* **`error_detail`**: _[`send_error_detail`](#send_error_detail)_ mutable pointer

#### Output:

* _[`done_idx`](#done_idx)_ mutable pointer
* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

---

### [`fastly_key_is_valid()`](#fastly_key_is_valid)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`is_valid`](#is_valid)_ mutable pointer

> DEPRECATED: use fastly_http_downstream::fastly_key_is_valid
>
> Returns whether or not the original client request arrived with a
> Fastly-Key belonging to a user with the rights to purge content on this
> service.


---

### [`close()`](#close)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_

This function has no output.

---

### [`auto_decompress_response_set()`](#auto_decompress_response_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`encodings`**: _[`content_encodings`](#content_encodings)_

This function has no output.

---

### [`upgrade_websocket()`](#upgrade_websocket)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`backend_name`**: `string`

This function has no output.

---

### [`redirect_to_websocket_proxy()`](#redirect_to_websocket_proxy)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`backend_name`**: `string`

This function has no output.

---

### [`redirect_to_grip_proxy()`](#redirect_to_grip_proxy)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`backend_name`**: `string`

This function has no output.

---

### [`redirect_to_websocket_proxy_v2()`](#redirect_to_websocket_proxy_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`backend_name`**: `string`

This function has no output.

---

### [`redirect_to_grip_proxy_v2()`](#redirect_to_grip_proxy_v2)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`backend_name`**: `string`

This function has no output.

---

### [`framing_headers_mode_set()`](#framing_headers_mode_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`request_handle`](#request_handle)_
* **`mode`**: _[`framing_headers_mode`](#framing_headers_mode)_

This function has no output.

> Adjust how this requests's framing headers are determined.


---

### [`register_dynamic_backend()`](#register_dynamic_backend)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`name_prefix`**: `string`
* **`target`**: `string`
* **`backend_config_mask`**: _[`backend_config_options`](#backend_config_options)_
* **`backend_configuration`**: _[`dynamic_backend_config`](#dynamic_backend_config)_ mutable pointer

This function has no output.

> Create a backend for later use


---

### [`inspect()`](#inspect)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req`**: _[`request_handle`](#request_handle)_
* **`body`**: _[`body_handle`](#body_handle)_
* **`insp_info_mask`**: _[`inspect_info_mask`](#inspect_info_mask)_
* **`insp_info`**: _[`inspect_info`](#inspect_info)_ mutable pointer
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`

#### Output:

* _[`num_bytes`](#num_bytes)_ mutable pointer

> Hostcall for Fastly Compute guests to inspect request HTTP traffic
> using the NGWAF lookaside service.


---

### [`on_behalf_of()`](#on_behalf_of)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req`**: _[`request_handle`](#request_handle)_
* **`service`**: `string`

This function has no output.

> Instead of having this request cache in this service's space, use the
> cache of the named service


---

