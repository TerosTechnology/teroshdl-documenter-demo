# Package: avalon_stream_pkg

- **File**: avalon_stream_pkg.vhd
## Constants

| Name                          | Type       | Value                                      | Description |
| ----------------------------- | ---------- | ------------------------------------------ | ----------- |
| avalon_stream_logger          | logger_t   |  get_logger("vunit_lib:avalon_stream_pkg") |             |
| push_avalon_stream_msg        | msg_type_t |  new_msg_type("push avalon stream")        |             |
| pop_avalon_stream_msg         | msg_type_t |  new_msg_type("pop avalon stream")         |             |
| avalon_stream_transaction_msg | msg_type_t |  new_msg_type("avalon stream transaction") |             |
## Types

| Name                        | Type | Description |
| --------------------------- | ---- | ----------- |
| avalon_source_t             |      |             |
| avalon_sink_t               |      |             |
| avalon_stream_transaction_t |      |             |
## Functions
- push_avalon_stream <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> avalon_source : avalon_source_t;<br><span style="padding-left:20px"> data : std_logic_vector;<br><span style="padding-left:20px"> sop : std_logic := '0';<br><span style="padding-left:20px"> eop : std_logic := '0') </font> <font id="function_return">return ()</font>
- pop_avalon_stream <font id="function_arguments">(signal net : inout network_t;<br><span style="padding-left:20px"> avalon_sink : avalon_sink_t;<br><span style="padding-left:20px"> variable data : inout std_logic_vector;<br><span style="padding-left:20px"> variable sop  : inout std_logic;<br><span style="padding-left:20px"> variable eop  : inout std_logic) </font> <font id="function_return">return ()</font>
- push_avalon_stream_transaction <font id="function_arguments">(msg : msg_t;<br><span style="padding-left:20px"> avalon_stream_transaction : avalon_stream_transaction_t) </font> <font id="function_return">return ()</font>
- pop_avalon_stream_transaction <font id="function_arguments">( constant msg : in msg_t;<br><span style="padding-left:20px"> variable avalon_stream_transaction : out avalon_stream_transaction_t ) </font> <font id="function_return">return ()</font>
- handle_avalon_stream_transaction <font id="function_arguments">( variable msg_type : inout msg_type_t;<br><span style="padding-left:20px"> variable msg : inout msg_t;<br><span style="padding-left:20px"> variable avalon_transaction : out avalon_stream_transaction_t ) </font> <font id="function_return">return ()</font>
