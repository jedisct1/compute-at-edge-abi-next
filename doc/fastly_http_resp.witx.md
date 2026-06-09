
# Module: fastly_http_resp

## Table of contents

### Types list:

[**[All](#types)**] - [_[`fastly_status`](#fastly_status)_] - [_[`http_version`](#http_version)_] - [_[`http_status`](#http_status)_] - [_[`body_write_end`](#body_write_end)_] - [_[`body_handle`](#body_handle)_] - [_[`request_handle`](#request_handle)_] - [_[`response_handle`](#response_handle)_] - [_[`pending_request_handle`](#pending_request_handle)_] - [_[`endpoint_handle`](#endpoint_handle)_] - [_[`dictionary_handle`](#dictionary_handle)_] - [_[`object_store_handle`](#object_store_handle)_] - [_[`pending_kv_lookup_handle`](#pending_kv_lookup_handle)_] - [_[`pending_kv_insert_handle`](#pending_kv_insert_handle)_] - [_[`pending_kv_delete_handle`](#pending_kv_delete_handle)_] - [_[`pending_kv_list_handle`](#pending_kv_list_handle)_] - [_[`kv_store_handle`](#kv_store_handle)_] - [_[`kv_store_lookup_handle`](#kv_store_lookup_handle)_] - [_[`kv_store_insert_handle`](#kv_store_insert_handle)_] - [_[`kv_store_delete_handle`](#kv_store_delete_handle)_] - [_[`kv_store_list_handle`](#kv_store_list_handle)_] - [_[`secret_store_handle`](#secret_store_handle)_] - [_[`secret_handle`](#secret_handle)_] - [_[`acl_handle`](#acl_handle)_] - [_[`request_promise_handle`](#request_promise_handle)_] - [_[`async_item_handle`](#async_item_handle)_] - [_[`multi_value_cursor`](#multi_value_cursor)_] - [_[`multi_value_cursor_result`](#multi_value_cursor_result)_] - [_[`cache_override_tag`](#cache_override_tag)_] - [_[`num_bytes`](#num_bytes)_] - [_[`header_count`](#header_count)_] - [_[`is_done`](#is_done)_] - [_[`done_idx`](#done_idx)_] - [_[`is_valid`](#is_valid)_] - [_[`inserted`](#inserted)_] - [_[`ready_idx`](#ready_idx)_] - [_[`ddos_detected`](#ddos_detected)_] - [_[`port`](#port)_] - [_[`timeout_ms`](#timeout_ms)_] - [_[`timeout_secs`](#timeout_secs)_] - [_[`probe_count`](#probe_count)_] - [_[`backend_exists`](#backend_exists)_] - [_[`is_dynamic`](#is_dynamic)_] - [_[`is_keepalive`](#is_keepalive)_] - [_[`is_ssl`](#is_ssl)_] - [_[`backend_health`](#backend_health)_] - [_[`bot_analyzed`](#bot_analyzed)_] - [_[`bot_detected`](#bot_detected)_] - [_[`bot_category_kind`](#bot_category_kind)_] - [_[`bot_verified`](#bot_verified)_] - [_[`resvpnproxy_is_anonymous`](#resvpnproxy_is_anonymous)_] - [_[`resvpnproxy_is_anonymous_vpn`](#resvpnproxy_is_anonymous_vpn)_] - [_[`resvpnproxy_is_hosting_provider`](#resvpnproxy_is_hosting_provider)_] - [_[`resvpnproxy_is_proxy_over_vpn`](#resvpnproxy_is_proxy_over_vpn)_] - [_[`resvpnproxy_is_public_proxy`](#resvpnproxy_is_public_proxy)_] - [_[`resvpnproxy_is_relay_proxy`](#resvpnproxy_is_relay_proxy)_] - [_[`resvpnproxy_is_residential_proxy`](#resvpnproxy_is_residential_proxy)_] - [_[`resvpnproxy_is_smart_dns_proxy`](#resvpnproxy_is_smart_dns_proxy)_] - [_[`resvpnproxy_is_tor_exit_node`](#resvpnproxy_is_tor_exit_node)_] - [_[`resvpnproxy_is_vpn_datacenter`](#resvpnproxy_is_vpn_datacenter)_] - [_[`content_encodings`](#content_encodings)_] - [_[`framing_headers_mode`](#framing_headers_mode)_] - [_[`http_keepalive_mode`](#http_keepalive_mode)_] - [_[`tls_version`](#tls_version)_] - [_[`kv_lookup_config_options`](#kv_lookup_config_options)_] - [_[`kv_lookup_config`](#kv_lookup_config)_] - [_[`kv_delete_config_options`](#kv_delete_config_options)_] - [_[`kv_delete_config`](#kv_delete_config)_] - [_[`kv_insert_config_options`](#kv_insert_config_options)_] - [_[`kv_insert_mode`](#kv_insert_mode)_] - [_[`kv_insert_config`](#kv_insert_config)_] - [_[`kv_list_config_options`](#kv_list_config_options)_] - [_[`kv_list_mode`](#kv_list_mode)_] - [_[`kv_list_config`](#kv_list_config)_] - [_[`kv_error`](#kv_error)_] - [_[`backend_config_options`](#backend_config_options)_] - [_[`dynamic_backend_config`](#dynamic_backend_config)_] - [_[`client_cert_verify_result`](#client_cert_verify_result)_] - [_[`purge_options_mask`](#purge_options_mask)_] - [_[`purge_options`](#purge_options)_] - [_[`send_error_detail_tag`](#send_error_detail_tag)_] - [_[`send_error_detail_mask`](#send_error_detail_mask)_] - [_[`send_error_detail`](#send_error_detail)_] - [_[`blocked`](#blocked)_] - [_[`rate`](#rate)_] - [_[`count`](#count)_] - [_[`has`](#has)_] - [_[`body_length`](#body_length)_] - [_[`vcpu_ms`](#vcpu_ms)_] - [_[`memory_mib`](#memory_mib)_] - [_[`inspect_info_mask`](#inspect_info_mask)_] - [_[`inspect_info`](#inspect_info)_] - [_[`acl_error`](#acl_error)_] - [_[`image_optimizer_transform_config_options`](#image_optimizer_transform_config_options)_] - [_[`image_optimizer_transform_config`](#image_optimizer_transform_config)_] - [_[`image_optimizer_error_tag`](#image_optimizer_error_tag)_] - [_[`image_optimizer_error_detail`](#image_optimizer_error_detail)_] - [_[`next_request_options_mask`](#next_request_options_mask)_] - [_[`next_request_options`](#next_request_options)_] - [_[`pending_response_kind`](#pending_response_kind)_]

### Functions list:

[**[All](#functions)**] - [[`new()`](#new)] - [[`header_names_get()`](#header_names_get)] - [[`header_value_get()`](#header_value_get)] - [[`header_values_get()`](#header_values_get)] - [[`header_values_set()`](#header_values_set)] - [[`header_insert()`](#header_insert)] - [[`header_append()`](#header_append)] - [[`header_remove()`](#header_remove)] - [[`version_get()`](#version_get)] - [[`version_set()`](#version_set)] - [[`send_downstream()`](#send_downstream)] - [[`send_downstream_pending()`](#send_downstream_pending)] - [[`status_get()`](#status_get)] - [[`status_set()`](#status_set)] - [[`close()`](#close)] - [[`framing_headers_mode_set()`](#framing_headers_mode_set)] - [[`http_keepalive_mode_set()`](#http_keepalive_mode_set)] - [[`get_addr_dest_ip()`](#get_addr_dest_ip)] - [[`get_addr_dest_port()`](#get_addr_dest_port)]

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

### _[`bot_analyzed`](#bot_analyzed)_
Alias for `u32`.


---

### _[`bot_detected`](#bot_detected)_
Alias for `u32`.


---

### _[`bot_category_kind`](#bot_category_kind)_
Alias for `u32`.


---

### _[`bot_verified`](#bot_verified)_
Alias for `u32`.


---

### _[`resvpnproxy_is_anonymous`](#resvpnproxy_is_anonymous)_
Alias for `u32`.


---

### _[`resvpnproxy_is_anonymous_vpn`](#resvpnproxy_is_anonymous_vpn)_
Alias for `u32`.


---

### _[`resvpnproxy_is_hosting_provider`](#resvpnproxy_is_hosting_provider)_
Alias for `u32`.


---

### _[`resvpnproxy_is_proxy_over_vpn`](#resvpnproxy_is_proxy_over_vpn)_
Alias for `u32`.


---

### _[`resvpnproxy_is_public_proxy`](#resvpnproxy_is_public_proxy)_
Alias for `u32`.


---

### _[`resvpnproxy_is_relay_proxy`](#resvpnproxy_is_relay_proxy)_
Alias for `u32`.


---

### _[`resvpnproxy_is_residential_proxy`](#resvpnproxy_is_residential_proxy)_
Alias for `u32`.


---

### _[`resvpnproxy_is_smart_dns_proxy`](#resvpnproxy_is_smart_dns_proxy)_
Alias for `u32`.


---

### _[`resvpnproxy_is_tor_exit_node`](#resvpnproxy_is_tor_exit_node)_
Alias for `u32`.


---

### _[`resvpnproxy_is_vpn_datacenter`](#resvpnproxy_is_vpn_datacenter)_
Alias for `u32`.


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
* **`h2_error`**: _[`send_error_detail_tag`](#send_error_detail_tag)_

---

### _[`send_error_detail_mask`](#send_error_detail_mask)_

Set of constants, of type `u32`

Predefined constants for _[`send_error_detail_mask`](#send_error_detail_mask)_:

* **`reserved`** = `0x1`
* **`dns_error_rcode`** = `0x2`
* **`dns_error_info_code`** = `0x4`
* **`tls_alert_id`** = `0x8`
* **`h2_error`** = `0x10`

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
* **`h2_error_frame`**: `u8`
* **`h2_error_code`**: `u32`

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

### _[`pending_response_kind`](#pending_response_kind)_

Enumeration with tag type: `u32`, and the following members:

* **`any`**: _[`pending_response_kind`](#pending_response_kind)_
* **`response`**: _[`pending_response_kind`](#pending_response_kind)_
* **`error`**: _[`pending_response_kind`](#pending_response_kind)_

> Kinds of responses to pending request handles.


---

## Functions

### [`new()`](#new)
Returned error type: _[`fastly_status`](#fastly_status)_


#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer

---

### [`header_names_get()`](#header_names_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`buf`**: `char8` mutable pointer
* **`buf_len`**: `usize`
* **`cursor`**: _[`multi_value_cursor`](#multi_value_cursor)_
* **`ending_cursor_out`**: _[`multi_value_cursor_result`](#multi_value_cursor_result)_ mutable pointer
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`header_value_get()`](#header_value_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `char8` mutable pointer
* **`value_max_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

---

### [`header_values_get()`](#header_values_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
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

* **`h`**: _[`response_handle`](#response_handle)_
* **`name`**: `u8` mutable slice
* **`values`**: `string`

This function has no output.

---

### [`header_insert()`](#header_insert)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `u8` mutable slice

This function has no output.

---

### [`header_append()`](#header_append)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`name`**: `u8` mutable slice
* **`value`**: `u8` mutable slice

This function has no output.

---

### [`header_remove()`](#header_remove)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`name`**: `u8` mutable slice

This function has no output.

---

### [`version_get()`](#version_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_

#### Output:

* _[`http_version`](#http_version)_ mutable pointer

---

### [`version_set()`](#version_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`version`**: _[`http_version`](#http_version)_

This function has no output.

---

### [`send_downstream()`](#send_downstream)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`b`**: _[`body_handle`](#body_handle)_
* **`streaming`**: `u32`

This function has no output.

---

### [`send_downstream_pending()`](#send_downstream_pending)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`pending_request_handle`](#pending_request_handle)_

This function has no output.

> Use a pending request handle to send a downstream response.
> 
> This will cause Compute to wait in the background for the pending request handle to
> resolve into its response headers and body, and then forward them back downstream.
> 
> If the pending request fails while sending and a response never materializes, Compute
> will generate a 5XX response to send in its stead.


---

### [`status_get()`](#status_get)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_

#### Output:

* _[`http_status`](#http_status)_ mutable pointer

---

### [`status_set()`](#status_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`status`**: _[`http_status`](#http_status)_

This function has no output.

---

### [`close()`](#close)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_

This function has no output.

---

### [`framing_headers_mode_set()`](#framing_headers_mode_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`mode`**: _[`framing_headers_mode`](#framing_headers_mode)_

This function has no output.

> Adjust how this response's framing headers are determined.


---

### [`http_keepalive_mode_set()`](#http_keepalive_mode_set)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`mode`**: _[`http_keepalive_mode`](#http_keepalive_mode)_

This function has no output.

> Adjust the response's connection reuse mode.


---

### [`get_addr_dest_ip()`](#get_addr_dest_ip)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_
* **`addr_octets_out`**: `char8` mutable pointer

#### Output:

* _[`num_bytes`](#num_bytes)_ mutable pointer

> Hostcall for getting the destination IP used for this request.
> 
> The buffer for the IP address must be 16 bytes. `addr_octets_out`
> will be set to 4 for IPv4 addresses, and 16 for IPv6.


---

### [`get_addr_dest_port()`](#get_addr_dest_port)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`h`**: _[`response_handle`](#response_handle)_

#### Output:

* _[`port`](#port)_ mutable pointer

> Hostcall for getting the destination port used for this request.


---

