# Package: stream_master_pkg
## Constants
| Name            | Type       | Value                        | Description |
| --------------- | ---------- | ---------------------------- | ----------- |
| stream_push_msg | msg_type_t |  new_msg_type("stream push") |             |
## Types
| Name            | Type | Description |
| --------------- | ---- | ----------- |
| stream_master_t |      |             |
## Functions
- push_stream <font id="function_arguments">(signal net : inout network_t;                        stream : stream_master_t;
                        data : std_logic_vector;
                        last : boolean := false)</font> <font id="function_return">return ()</font>
