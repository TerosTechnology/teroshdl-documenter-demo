# Package: stream_slave_pkg
## Constants
| Name           | Type       | Value                       | Description |
| -------------- | ---------- | --------------------------- | ----------- |
| stream_pop_msg | msg_type_t |  new_msg_type("stream pop") |             |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| stream_slave_t |      |             |
## Functions
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable data : out std_logic_vector;
                       variable last : out boolean)</font> <font id="function_return">return ()</font>
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable data : out std_logic_vector)</font> <font id="function_return">return ()</font>
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable reference : inout stream_reference_t)</font> <font id="function_return">return ()</font>
- await_pop_stream_reply <font id="function_arguments">(signal net : inout network_t;                                   variable reference : inout stream_reference_t;
                                   variable data : out std_logic_vector;
                                   variable last : out boolean)</font> <font id="function_return">return ()</font>
- await_pop_stream_reply <font id="function_arguments">(signal net : inout network_t;                                   variable reference : inout stream_reference_t;
                                   variable data : out std_logic_vector)</font> <font id="function_return">return ()</font>
- check_stream <font id="function_arguments">(signal net : inout network_t;                         stream : stream_slave_t;
                         expected : std_logic_vector;
                         last : boolean := false;
                         msg : string := "")</font> <font id="function_return">return ()</font>
