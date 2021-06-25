# Package: axi_lite_master_pkg
## Constants
| Name               | Type       | Value                           | Description |
| ------------------ | ---------- | ------------------------------- | ----------- |
| axi_lite_read_msg  | msg_type_t |  new_msg_type("read axi lite")  |             |
| axi_lite_write_msg | msg_type_t |  new_msg_type("write axi lite") |             |
## Functions
- write_axi_lite <font id="function_arguments">(signal net : inout network_t;                           constant bus_handle : bus_master_t;
                           constant address : std_logic_vector;
                           constant data : std_logic_vector;
                           constant expected_bresp : axi_resp_t := axi_resp_okay;
                            default byte enable is all bytes
                           constant byte_enable : std_logic_vector := "")</font> <font id="function_return">return ()</font>
- read_axi_lite <font id="function_arguments">(signal net : inout network_t;                          constant bus_handle : bus_master_t;
                          constant address : std_logic_vector;
                          constant expected_rresp : axi_resp_t := axi_resp_okay;
                          variable reference : inout bus_reference_t)</font> <font id="function_return">return ()</font>
- read_axi_lite <font id="function_arguments">(signal net : inout network_t;                          constant bus_handle : bus_master_t;
                          constant address : std_logic_vector;
                          constant expected_rresp : axi_resp_t := axi_resp_okay;
                          variable data : inout std_logic_vector)</font> <font id="function_return">return ()</font>
- check_axi_lite <font id="function_arguments">(signal net : inout network_t;                           constant bus_handle : bus_master_t;
                           constant address : std_logic_vector;
                           constant expected_rresp : axi_resp_t := axi_resp_okay;
                           constant expected : std_logic_vector;
                           constant msg : string := "")</font> <font id="function_return">return ()</font>
- is_read <font id="function_arguments">(msg_type : msg_type_t)</font> <font id="function_return">return boolean</font>
- is_write <font id="function_arguments">(msg_type : msg_type_t)</font> <font id="function_return">return boolean</font>
- is_axi_lite_msg <font id="function_arguments">(msg_type : msg_type_t)</font> <font id="function_return">return boolean</font>
