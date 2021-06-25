# Package: axi_slave_pkg
## Constants
| Name                                               | Type       | Value                                                            | Description |
| -------------------------------------------------- | ---------- | ---------------------------------------------------------------- | ----------- |
| axi_slave_logger                                   | logger_t   |  get_logger("vunit_lib:axi_slave_pkg")                           |             |
| axi_slave_set_address_fifo_depth_msg               | msg_type_t |  new_msg_type("axi slave set address channel fifo depth")        |             |
| axi_slave_set_write_response_fifo_depth_msg        | msg_type_t |  new_msg_type("set write response fifo depth")                   |             |
| axi_slave_set_address_stall_probability_msg        | msg_type_t |  new_msg_type("axi slave set address channel stall probability") |             |
| axi_slave_set_data_stall_probability_msg           | msg_type_t |  new_msg_type("axi slave set data stall probability")            |             |
| axi_slave_set_write_response_stall_probability_msg | msg_type_t |  new_msg_type("axi slave set write response stall probability")  |             |
| axi_slave_set_response_latency_msg                 | msg_type_t |  new_msg_type("axi slave response latency probability")          |             |
| axi_slave_configure_4kbyte_boundary_check_msg      | msg_type_t |  new_msg_type("axi slave configure 4kbyte boundary check")       |             |
| axi_slave_get_statistics_msg                       | msg_type_t |  new_msg_type("axi slave get statistics")                        |             |
| axi_slave_enable_well_behaved_check_msg            | msg_type_t |  new_msg_type("axi slave enable well behaved check")             |             |
## Types
| Name        | Type | Description |
| ----------- | ---- | ----------- |
| axi_slave_t |      |             |
## Functions
- get_logger <font id="function_arguments">(axi_slave : axi_slave_t)</font> <font id="function_return">return logger_t</font>
- set_address_fifo_depth <font id="function_arguments">(signal net : inout network_t;                                   axi_slave : axi_slave_t;
                                   depth : positive)</font> <font id="function_return">return ()</font>
- set_write_response_fifo_depth <font id="function_arguments">(signal net : inout network_t;                                          axi_slave : axi_slave_t;
                                          depth : positive)</font> <font id="function_return">return ()</font>
- set_address_stall_probability <font id="function_arguments">(signal net : inout network_t;                                          axi_slave : axi_slave_t;
                                          probability : probability_t)</font> <font id="function_return">return ()</font>
- set_data_stall_probability <font id="function_arguments">(signal net : inout network_t;                                       axi_slave : axi_slave_t;
                                       probability : probability_t)</font> <font id="function_return">return ()</font>
- set_write_response_stall_probability <font id="function_arguments">(signal net : inout network_t;                                                 axi_slave : axi_slave_t;
                                                 probability : probability_t)</font> <font id="function_return">return ()</font>
- set_response_latency <font id="function_arguments">(signal net : inout network_t;                                 axi_slave : axi_slave_t;
                                 min_latency, max_latency : delay_length)</font> <font id="function_return">return ()</font>
- set_response_latency <font id="function_arguments">(signal net : inout network_t;                                 axi_slave : axi_slave_t;
                                 latency : delay_length)</font> <font id="function_return">return ()</font>
- enable_4kbyte_boundary_check <font id="function_arguments">(signal net : inout network_t;                                         axi_slave : axi_slave_t)</font> <font id="function_return">return ()</font>
- disable_4kbyte_boundary_check <font id="function_arguments">(signal net : inout network_t;                                          axi_slave : axi_slave_t)</font> <font id="function_return">return ()</font>
- get_statistics <font id="function_arguments">(signal net : inout network_t;                           axi_slave : axi_slave_t;
                           variable stat  : inout axi_statistics_t;
                           clear : boolean := false)</font> <font id="function_return">return ()</font>
- enable_well_behaved_check <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t)</font> <font id="function_return">return ()</font>
