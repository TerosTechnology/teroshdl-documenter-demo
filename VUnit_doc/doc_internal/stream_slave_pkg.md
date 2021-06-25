# Package: stream_slave_pkg
## Constants
| Name           | Type       | Value                       | Description                                                       |
| -------------- | ---------- | --------------------------- | ----------------------------------------------------------------- |
| stream_pop_msg | msg_type_t |  new_msg_type("stream pop") | Message type definitions used by VC implementing stream slave VCI |
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| stream_slave_t |      |             |
## Functions
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable data : out std_logic_vector;
                       variable last : out boolean)</font> <font id="function_return">return ()</font>
**Description**
Blocking: pop a value from the stream
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable data : out std_logic_vector)</font> <font id="function_return">return ()</font>
- pop_stream <font id="function_arguments">(signal net : inout network_t;                       stream : stream_slave_t;
                       variable reference : inout stream_reference_t)</font> <font id="function_return">return ()</font>
**Description**
Non-blocking: pop a value from the stream to be read in the future
- await_pop_stream_reply <font id="function_arguments">(signal net : inout network_t;                                   variable reference : inout stream_reference_t;
                                   variable data : out std_logic_vector;
                                   variable last : out boolean)</font> <font id="function_return">return ()</font>
**Description**
Blocking: Wait for reply to non-blocking pop
- await_pop_stream_reply <font id="function_arguments">(signal net : inout network_t;                                   variable reference : inout stream_reference_t;
                                   variable data : out std_logic_vector)</font> <font id="function_return">return ()</font>
- check_stream <font id="function_arguments">(signal net : inout network_t;                         stream : stream_slave_t;
                         expected : std_logic_vector;
                         last : boolean := false;
                         msg : string := "")</font> <font id="function_return">return ()</font>
**Description**
Blocking: read stream and check result against expected value
