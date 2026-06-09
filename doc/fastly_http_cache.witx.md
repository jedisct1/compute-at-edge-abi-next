
# Module: fastly_http_cache

## Table of contents

### Types list:

[**[All](#types)**] - [_[`fastly_status`](#fastly_status)_] - [_[`http_version`](#http_version)_] - [_[`http_status`](#http_status)_] - [_[`body_write_end`](#body_write_end)_] - [_[`body_handle`](#body_handle)_] - [_[`request_handle`](#request_handle)_] - [_[`response_handle`](#response_handle)_] - [_[`pending_request_handle`](#pending_request_handle)_] - [_[`endpoint_handle`](#endpoint_handle)_] - [_[`dictionary_handle`](#dictionary_handle)_] - [_[`object_store_handle`](#object_store_handle)_] - [_[`pending_kv_lookup_handle`](#pending_kv_lookup_handle)_] - [_[`pending_kv_insert_handle`](#pending_kv_insert_handle)_] - [_[`pending_kv_delete_handle`](#pending_kv_delete_handle)_] - [_[`pending_kv_list_handle`](#pending_kv_list_handle)_] - [_[`kv_store_handle`](#kv_store_handle)_] - [_[`kv_store_lookup_handle`](#kv_store_lookup_handle)_] - [_[`kv_store_insert_handle`](#kv_store_insert_handle)_] - [_[`kv_store_delete_handle`](#kv_store_delete_handle)_] - [_[`kv_store_list_handle`](#kv_store_list_handle)_] - [_[`secret_store_handle`](#secret_store_handle)_] - [_[`secret_handle`](#secret_handle)_] - [_[`acl_handle`](#acl_handle)_] - [_[`request_promise_handle`](#request_promise_handle)_] - [_[`async_item_handle`](#async_item_handle)_] - [_[`multi_value_cursor`](#multi_value_cursor)_] - [_[`multi_value_cursor_result`](#multi_value_cursor_result)_] - [_[`cache_override_tag`](#cache_override_tag)_] - [_[`num_bytes`](#num_bytes)_] - [_[`header_count`](#header_count)_] - [_[`is_done`](#is_done)_] - [_[`done_idx`](#done_idx)_] - [_[`is_valid`](#is_valid)_] - [_[`inserted`](#inserted)_] - [_[`ready_idx`](#ready_idx)_] - [_[`ddos_detected`](#ddos_detected)_] - [_[`port`](#port)_] - [_[`timeout_ms`](#timeout_ms)_] - [_[`timeout_secs`](#timeout_secs)_] - [_[`probe_count`](#probe_count)_] - [_[`backend_exists`](#backend_exists)_] - [_[`is_dynamic`](#is_dynamic)_] - [_[`is_keepalive`](#is_keepalive)_] - [_[`is_ssl`](#is_ssl)_] - [_[`backend_health`](#backend_health)_] - [_[`bot_analyzed`](#bot_analyzed)_] - [_[`bot_detected`](#bot_detected)_] - [_[`bot_category_kind`](#bot_category_kind)_] - [_[`bot_verified`](#bot_verified)_] - [_[`resvpnproxy_is_anonymous`](#resvpnproxy_is_anonymous)_] - [_[`resvpnproxy_is_anonymous_vpn`](#resvpnproxy_is_anonymous_vpn)_] - [_[`resvpnproxy_is_hosting_provider`](#resvpnproxy_is_hosting_provider)_] - [_[`resvpnproxy_is_proxy_over_vpn`](#resvpnproxy_is_proxy_over_vpn)_] - [_[`resvpnproxy_is_public_proxy`](#resvpnproxy_is_public_proxy)_] - [_[`resvpnproxy_is_relay_proxy`](#resvpnproxy_is_relay_proxy)_] - [_[`resvpnproxy_is_residential_proxy`](#resvpnproxy_is_residential_proxy)_] - [_[`resvpnproxy_is_smart_dns_proxy`](#resvpnproxy_is_smart_dns_proxy)_] - [_[`resvpnproxy_is_tor_exit_node`](#resvpnproxy_is_tor_exit_node)_] - [_[`resvpnproxy_is_vpn_datacenter`](#resvpnproxy_is_vpn_datacenter)_] - [_[`content_encodings`](#content_encodings)_] - [_[`framing_headers_mode`](#framing_headers_mode)_] - [_[`http_keepalive_mode`](#http_keepalive_mode)_] - [_[`tls_version`](#tls_version)_] - [_[`kv_lookup_config_options`](#kv_lookup_config_options)_] - [_[`kv_lookup_config`](#kv_lookup_config)_] - [_[`kv_delete_config_options`](#kv_delete_config_options)_] - [_[`kv_delete_config`](#kv_delete_config)_] - [_[`kv_insert_config_options`](#kv_insert_config_options)_] - [_[`kv_insert_mode`](#kv_insert_mode)_] - [_[`kv_insert_config`](#kv_insert_config)_] - [_[`kv_list_config_options`](#kv_list_config_options)_] - [_[`kv_list_mode`](#kv_list_mode)_] - [_[`kv_list_config`](#kv_list_config)_] - [_[`kv_error`](#kv_error)_] - [_[`backend_config_options`](#backend_config_options)_] - [_[`dynamic_backend_config`](#dynamic_backend_config)_] - [_[`client_cert_verify_result`](#client_cert_verify_result)_] - [_[`purge_options_mask`](#purge_options_mask)_] - [_[`purge_options`](#purge_options)_] - [_[`send_error_detail_tag`](#send_error_detail_tag)_] - [_[`send_error_detail_mask`](#send_error_detail_mask)_] - [_[`send_error_detail`](#send_error_detail)_] - [_[`blocked`](#blocked)_] - [_[`rate`](#rate)_] - [_[`count`](#count)_] - [_[`has`](#has)_] - [_[`body_length`](#body_length)_] - [_[`vcpu_ms`](#vcpu_ms)_] - [_[`memory_mib`](#memory_mib)_] - [_[`inspect_info_mask`](#inspect_info_mask)_] - [_[`inspect_info`](#inspect_info)_] - [_[`acl_error`](#acl_error)_] - [_[`image_optimizer_transform_config_options`](#image_optimizer_transform_config_options)_] - [_[`image_optimizer_transform_config`](#image_optimizer_transform_config)_] - [_[`image_optimizer_error_tag`](#image_optimizer_error_tag)_] - [_[`image_optimizer_error_detail`](#image_optimizer_error_detail)_] - [_[`next_request_options_mask`](#next_request_options_mask)_] - [_[`next_request_options`](#next_request_options)_] - [_[`pending_response_kind`](#pending_response_kind)_] - [_[`cache_duration_ns`](#cache_duration_ns)_] - [_[`cache_object_length`](#cache_object_length)_] - [_[`cache_hit_count`](#cache_hit_count)_] - [_[`cache_lookup_state`](#cache_lookup_state)_] - [_[`http_cache_handle`](#http_cache_handle)_] - [_[`is_cacheable`](#is_cacheable)_] - [_[`is_sensitive`](#is_sensitive)_] - [_[`http_storage_action`](#http_storage_action)_] - [_[`http_cache_lookup_options`](#http_cache_lookup_options)_] - [_[`http_cache_lookup_options_mask`](#http_cache_lookup_options_mask)_] - [_[`http_cache_write_options`](#http_cache_write_options)_] - [_[`http_cache_write_options_mask`](#http_cache_write_options_mask)_]

### Functions list:

[**[All](#functions)**] - [[`is_request_cacheable()`](#is_request_cacheable)] - [[`get_suggested_cache_key()`](#get_suggested_cache_key)] - [[`lookup()`](#lookup)] - [[`transaction_lookup()`](#transaction_lookup)] - [[`transaction_insert()`](#transaction_insert)] - [[`transaction_insert_and_stream_back()`](#transaction_insert_and_stream_back)] - [[`transaction_update()`](#transaction_update)] - [[`transaction_update_and_return_fresh()`](#transaction_update_and_return_fresh)] - [[`transaction_choose_stale()`](#transaction_choose_stale)] - [[`transaction_record_not_cacheable()`](#transaction_record_not_cacheable)] - [[`transaction_abandon()`](#transaction_abandon)] - [[`close()`](#close)] - [[`get_suggested_backend_request()`](#get_suggested_backend_request)] - [[`get_suggested_cache_options()`](#get_suggested_cache_options)] - [[`prepare_response_for_storage()`](#prepare_response_for_storage)] - [[`get_found_response()`](#get_found_response)] - [[`get_state()`](#get_state)] - [[`get_length()`](#get_length)] - [[`get_max_age_ns()`](#get_max_age_ns)] - [[`get_stale_while_revalidate_ns()`](#get_stale_while_revalidate_ns)] - [[`get_stale_if_error_ns()`](#get_stale_if_error_ns)] - [[`get_age_ns()`](#get_age_ns)] - [[`get_hits()`](#get_hits)] - [[`get_sensitive_data()`](#get_sensitive_data)] - [[`get_surrogate_keys()`](#get_surrogate_keys)] - [[`get_vary_rule()`](#get_vary_rule)]

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

### _[`cache_duration_ns`](#cache_duration_ns)_
Alias for `u64`.


---

### _[`cache_object_length`](#cache_object_length)_
Alias for `u64`.


---

### _[`cache_hit_count`](#cache_hit_count)_
Alias for `u64`.


---

### _[`cache_lookup_state`](#cache_lookup_state)_

Set of constants, of type `u32`

Predefined constants for _[`cache_lookup_state`](#cache_lookup_state)_:

* **`found`** = `0x1`
* **`usable`** = `0x2`
* **`stale`** = `0x4`
* **`must_insert_or_update`** = `0x8`
* **`usable_if_error`** = `0x10`

> The status of this lookup (and potential transaction)


---

### _[`http_cache_handle`](#http_cache_handle)_
Alias for `handle`.


> Overall, this should look very familiar to users of the Core Cache API. The primary differences
> are:
> 
> - HTTP `request_handle`s and `response_handle`s are used rather than relying on the user to
> encode headers, status codes, etc in `user_metadata`.
> 
> - Convenience functions specific to HTTP semantics are provided, such as `is_request_cacheable`,
> `get_suggested_backend_request`, `get_suggested_cache_options`, and
> `transaction_record_not_cacheable`.
> 
> The HTTP-specific behavior of these functions is intended to support applications that match the
> normative guidance in RFC 9111. For example, `is_request_cacheable` returns `false` for `POST`
> requests. However, this answer along with those of many of these functions explicitly provide
> _suggestions_; they do not necessarily need to be followed if custom behavior is required, such
> as caching `POST` responses when the application author knows that to be safe.
> 
> The starting points for this API are `lookup` (no request collapsing) and `transaction_lookup`
> (request collapsing).
> A handle to an HTTP Cache transaction.


---

### _[`is_cacheable`](#is_cacheable)_
Alias for `u32`.


> Boolean: 1 == true, 0 == false.


---

### _[`is_sensitive`](#is_sensitive)_
Alias for `u32`.


> Boolean: 1 == true, 0 == false.


---

### _[`http_storage_action`](#http_storage_action)_

Enumeration with tag type: `u32`, and the following members:

* **`insert`**: _[`http_storage_action`](#http_storage_action)_
* **`update`**: _[`http_storage_action`](#http_storage_action)_
* **`do_not_store`**: _[`http_storage_action`](#http_storage_action)_
* **`record_uncacheable`**: _[`http_storage_action`](#http_storage_action)_

> The suggested action to take for spec-recommended behavior following
> `prepare_response_for_storage`.


---

### _[`http_cache_lookup_options`](#http_cache_lookup_options)_
Structure, with the following members:

* **`override_key_ptr`**: `char8` mutable pointer
* **`override_key_len`**: `usize`
* **`backend_name_ptr`**: `char8` mutable pointer
* **`backend_name_len`**: `usize`

> Non-required options for cache lookups.
> 
> This record is always provided along with an `http_cache_lookup_options_mask` value that
> indicates which of the fields in this record are valid.


---

### _[`http_cache_lookup_options_mask`](#http_cache_lookup_options_mask)_

Set of constants, of type `u32`

Predefined constants for _[`http_cache_lookup_options_mask`](#http_cache_lookup_options_mask)_:

* **`reserved`** = `0x1`
* **`override_key`** = `0x2`
* **`backend_name`** = `0x4`

> Options mask for `http_cache_lookup_options`.


---

### _[`http_cache_write_options`](#http_cache_write_options)_
Structure, with the following members:

* **`max_age_ns`**: _[`cache_duration_ns`](#cache_duration_ns)_
* **`vary_rule_ptr`**: `char8` mutable pointer
* **`vary_rule_len`**: `usize`
* **`initial_age_ns`**: _[`cache_duration_ns`](#cache_duration_ns)_
* **`stale_while_revalidate_ns`**: _[`cache_duration_ns`](#cache_duration_ns)_
* **`surrogate_keys_ptr`**: `char8` mutable pointer
* **`surrogate_keys_len`**: `usize`
* **`length`**: _[`cache_object_length`](#cache_object_length)_
* **`stale_if_error_ns`**: _[`cache_duration_ns`](#cache_duration_ns)_

> Options for cache insertions and updates.
> 
> This record is always provided along with an `http_cache_write_options_mask` value that
> indicates which of the fields in this record are valid.


---

### _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_

Set of constants, of type `u32`

Predefined constants for _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_:

* **`reserved`** = `0x1`
* **`vary_rule`** = `0x2`
* **`initial_age_ns`** = `0x4`
* **`stale_while_revalidate_ns`** = `0x8`
* **`surrogate_keys`** = `0x10`
* **`length`** = `0x20`
* **`sensitive_data`** = `0x40`
* **`stale_if_error_ns`** = `0x80`

> Options mask for `http_cache_write_options`.


---

## Functions

### [`is_request_cacheable()`](#is_request_cacheable)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req_handle`**: _[`request_handle`](#request_handle)_

#### Output:

* _[`is_cacheable`](#is_cacheable)_ mutable pointer

> Determine whether a request is cacheable per conservative RFC 9111 semantics.
> 
> In particular, this function checks whether the request method is `GET` or `HEAD`, and
> considers requests with other methods uncacheable. Applications where it is safe to cache
> responses to other methods should consider using their own cacheability check instead of
> this function.


---

### [`get_suggested_cache_key()`](#get_suggested_cache_key)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req_handle`**: _[`request_handle`](#request_handle)_
* **`key_out_ptr`**: `char8` mutable pointer
* **`key_out_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

> Retrieves the default cache key for the request.
> 
> The `$key_out` parameter must point to an array of size `key_out_len`.
> 
> If the guest-provided output parameter is not long enough to contain the full key,
> the required size is written by the host to `nwritten_out` and the `$buflen`
> error is returned.
> 
> At the moment, HTTP cache keys must always be 32 bytes.


---

### [`lookup()`](#lookup)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req_handle`**: _[`request_handle`](#request_handle)_
* **`options_mask`**: _[`http_cache_lookup_options_mask`](#http_cache_lookup_options_mask)_
* **`options`**: _[`http_cache_lookup_options`](#http_cache_lookup_options)_ mutable pointer

#### Output:

* _[`http_cache_handle`](#http_cache_handle)_ mutable pointer

> DEPRECATED: use transaction_lookup


---

### [`transaction_lookup()`](#transaction_lookup)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`req_handle`**: _[`request_handle`](#request_handle)_
* **`options_mask`**: _[`http_cache_lookup_options_mask`](#http_cache_lookup_options_mask)_
* **`options`**: _[`http_cache_lookup_options`](#http_cache_lookup_options)_ mutable pointer

#### Output:

* _[`http_cache_handle`](#http_cache_handle)_ mutable pointer

> Perform a cache lookup based on the given request.
> 
> This operation always participates in request collapsing and may return an obligation to
> insert or update responses, and/or stale responses. To bypass request collapsing, use
> `lookup` instead.
> 
> The request is not consumed.


---

### [`transaction_insert()`](#transaction_insert)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`resp_handle`**: _[`response_handle`](#response_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

#### Output:

* _[`body_handle`](#body_handle)_ mutable pointer

> Insert a response into the cache with the given options, returning a streaming body handle
> that is ready for writing or appending.
> 
> Can only be used if the cache handle state includes the `$must_insert_or_update` flag.
> 
> The response is consumed.


---

### [`transaction_insert_and_stream_back()`](#transaction_insert_and_stream_back)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`resp_handle`**: _[`response_handle`](#response_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

#### Output:

* _[`body_handle`](#body_handle)_ mutable pointer
* _[`http_cache_handle`](#http_cache_handle)_ mutable pointer

> Insert a response into the cache with the given options, and return a fresh cache handle
> that can be used to retrieve and stream the response while it's being inserted.
> 
> This helps avoid the "slow reader" problem on a teed stream, for example when a program wishes
> to store a backend request in the cache while simultaneously streaming to a client in an HTTP
> response.
> 
> The response is consumed.


---

### [`transaction_update()`](#transaction_update)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`resp_handle`**: _[`response_handle`](#response_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

This function has no output.

> Update freshness lifetime, response headers, and caching settings without updating the
> response body.
> 
> Can only be used in if the cache handle state includes both of the flags:
> - `$found`
> - `$must_insert_or_update`
> 
> The response is consumed.


---

### [`transaction_update_and_return_fresh()`](#transaction_update_and_return_fresh)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`resp_handle`**: _[`response_handle`](#response_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

#### Output:

* _[`http_cache_handle`](#http_cache_handle)_ mutable pointer

> Update freshness lifetime, response headers, and caching settings without updating the
> response body, and return a fresh cache handle that can be used to retrieve and stream the
> stored response.
> 
> Can only be used in if the cache handle state includes both of the flags:
> - `$found`
> - `$must_insert_or_update`
> 
> The response is consumed.


---

### [`transaction_choose_stale()`](#transaction_choose_stale)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

This function has no output.

> Fulfill an obligation to provide a response to the cache by selecting a stale-if-error response.
> 
> A guest that is obligated to insert/update the cache may not be able to produce an acceptable
> response (e.g. unreachable backend, 5xx response). If the cache contains a response in the
> stale-if-error period, the guest may prefer to use that response rather than returning an error.
> 
> `transaction_choose_stale` is an alternative to `transaction_update_and_return_fresh` or
> `transaction_insert_and_stream_back`. Like those methods, it completes a request collapse,
> providing the stale response to all collapsed transactions; and, after calling
> `transaction_choose_stale`, the cache handle provides the (stale) response to send to the client.
> 
> However, `transaction_choose_stale` does not change the cached state. The next lookup will again
> collapse and/or get an obligation to revalidate.


---

### [`transaction_record_not_cacheable()`](#transaction_record_not_cacheable)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

This function has no output.

> Fulfill an obligation to provide a response to the cache by disabling request collapsing and
> response caching for this cache entry.
> 
> In Varnish terms, this function stores a hit-for-pass object.
> 
> Only the max age and, optionally, the vary rule are read from the options mask and struct
> for this function.


---

### [`transaction_abandon()`](#transaction_abandon)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

This function has no output.

> Abandon an obligation to provide a response to the cache.
> 
> Useful if there is an error before streaming is possible, e.g. if a backend is unreachable.
> 
> If there are other requests collapsed on this transaction, one of those other requests will
> be awoken and given the obligation to provide a response. Note that if subsequent requests
> are unlikely to yield cacheable responses, this may lead to undesired serialization of
> requests. Consider using `transaction_record_not_cacheable` to make lookups for this request
> bypass the cache.


---

### [`close()`](#close)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

This function has no output.

> Close an ongoing interaction with the cache.
> 
> If the cache handle state includes `$must_insert_or_update` (and hence no insert or update
> has been performed), closing the handle cancels any request collapsing, potentially choosing
> a new waiter to perform the insertion/update.


---

### [`get_suggested_backend_request()`](#get_suggested_backend_request)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`request_handle`](#request_handle)_ mutable pointer

> Prepare a suggested request to make to a backend to satisfy the looked-up request.
> 
> If there is a stored, stale response, this suggested request may be for revalidation. If the
> looked-up request is ranged, the suggested request will be unranged in order to try caching
> the entire response.


---

### [`get_suggested_cache_options()`](#get_suggested_cache_options)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`response`**: _[`response_handle`](#response_handle)_
* **`options_mask`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_
* **`options`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer
* **`options_mask_out`**: _[`http_cache_write_options_mask`](#http_cache_write_options_mask)_ mutable pointer
* **`options_out`**: _[`http_cache_write_options`](#http_cache_write_options)_ mutable pointer

This function has no output.

> Prepare a suggested set of cache write options for a given request and response pair.
> 
> The ABI of this function includes several unusual types of input and output parameters.
> 
> The bits set in the `options_mask` input parameter describe which cache options the guest is
> requesting that the host provide.
> 
> The `options` input parameter allows the guest to provide output parameters for
> pointer/length options. When the corresponding bit is set in `options_mask`, the pointer and
> length should be set in this record to be used by the host to provide the output.
> 
> The `options_mask_out` output parameter is only used by the host to indicate the status of
> pointer/length data in the `options_out` record. The flag for a given pointer/length
> parameter is set by the host if the corresponding flag was set in `options_mask`, and the
> value is present in the suggested options. If the host returns a status of `$buflen`, the
> same set of flags will be set, but the length value of the corresponding fields in
> `options_out` are set to the lengths that would be required to read the full value from the
> host on a subsequent call.
> 
> The `options_out` output parameter is where the host writes the suggested options that were
> requested by the guest in `options_mask`. For pointer/length data, if there was enough room
> to write the suggested option, the length field will contain the length of the data actually
> written, while the pointer field will match the input pointer.
> 
> The response is not consumed.


---

### [`prepare_response_for_storage()`](#prepare_response_for_storage)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`response`**: _[`response_handle`](#response_handle)_

#### Output:

* _[`http_storage_action`](#http_storage_action)_ mutable pointer
* _[`response_handle`](#response_handle)_ mutable pointer

> Adjust a response into the appropriate form for storage and provides a storage action recommendation.
> 
> For example, if the looked-up request contains conditional headers, this function will
> interpret a `304 Not Modified` response for revalidation by updating headers.
> 
> In addition to the updated response, this function returns the recommended storage action.


---

### [`get_found_response()`](#get_found_response)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`transform_for_client`**: `u32`

#### Output:

* _[`response_handle`](#response_handle)_ mutable pointer
* _[`body_handle`](#body_handle)_ mutable pointer

> Retrieve a stored response from the cache, returning the `$none` error if there was no
> response found.
> 
> If `transform_for_client` is set, the response will be adjusted according to the looked-up
> request. For example, a response retrieved for a range request may be transformed into a
> `206 Partial Content` response with an appropriate `content-range` header.


---

### [`get_state()`](#get_state)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_lookup_state`](#cache_lookup_state)_ mutable pointer

> Get the state of a cache transaction.
> 
> Primarily useful after performing the lookup to determine what subsequent operations are
> possible and whether any insertion or update obligations exist.


---

### [`get_length()`](#get_length)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_object_length`](#cache_object_length)_ mutable pointer

> Get the length of the found response, returning the `$none` error if there was no response
> found or no length was provided.


---

### [`get_max_age_ns()`](#get_max_age_ns)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_duration_ns`](#cache_duration_ns)_ mutable pointer

> Get the configured max age of the found response in nanoseconds, returning the `$none` error
> if there was no response found.


---

### [`get_stale_while_revalidate_ns()`](#get_stale_while_revalidate_ns)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_duration_ns`](#cache_duration_ns)_ mutable pointer

> Get the configured stale-while-revalidate period of the found response in nanoseconds,
> returning the `$none` error if there was no response found.


---

### [`get_stale_if_error_ns()`](#get_stale_if_error_ns)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_duration_ns`](#cache_duration_ns)_ mutable pointer

> Get the configured stale-if-error period of the found response in nanoseconds,
> returning the `$none` error if there was no response found.


---

### [`get_age_ns()`](#get_age_ns)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_duration_ns`](#cache_duration_ns)_ mutable pointer

> Get the age of the found response in nanoseconds, returning the `$none` error if there was
> no response found.


---

### [`get_hits()`](#get_hits)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`cache_hit_count`](#cache_hit_count)_ mutable pointer

> Get the number of cache hits for the found response, returning the `$none` error if there
> was no response found.
> 
> Note that this figure only reflects hits for a stored response in a particular cache server
> or cluster, not the entire Fastly network.


---

### [`get_sensitive_data()`](#get_sensitive_data)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_

#### Output:

* _[`is_sensitive`](#is_sensitive)_ mutable pointer

> Get whether a found response is marked as containing sensitive data, returning the `$none`
> error if there was no response found.


---

### [`get_surrogate_keys()`](#get_surrogate_keys)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`surrogate_keys_out_ptr`**: `u8` mutable pointer
* **`surrogate_keys_out_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

> Get the surrogate keys of the found response, returning the `$none` error if there was no
> found response.
> 
> The output is a list of surrogate keys separated by spaces.
> 
> If the guest-provided output parameter is not long enough to contain the full list of
> surrogate keys, the required size is written by the host to `nwritten_out` and the `$buflen`
> error is returned.


---

### [`get_vary_rule()`](#get_vary_rule)
Returned error type: _[`fastly_status`](#fastly_status)_

#### Input:

* **`handle`**: _[`http_cache_handle`](#http_cache_handle)_
* **`vary_rule_out_ptr`**: `u8` mutable pointer
* **`vary_rule_out_len`**: `usize`
* **`nwritten_out`**: `usize` mutable pointer

This function has no output.

> Get the vary rule of the found response, returning the `$none` error if there was no
> response found.
> 
> The output is a list of header names separated by spaces.
> 
> If the guest-provided output parameter is not long enough to contain the full list of
> surrogate keys, the required size is written by the host to `nwritten_out` and the `$buflen`
> error is returned.


---

