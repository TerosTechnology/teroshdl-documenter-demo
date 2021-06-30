# Package: axi_slave_pkg

## Constants

| Name                                               | Type       | Value                                                            | Description       |
| -------------------------------------------------- | ---------- | ---------------------------------------------------------------- | ----------------- |
| axi_slave_logger                                   | logger_t   |  get_logger("vunit_lib:axi_slave_pkg")                           |                   |
| axi_slave_set_address_fifo_depth_msg               | msg_type_t |  new_msg_type("axi slave set address channel fifo depth")        | Private constants |
| axi_slave_set_write_response_fifo_depth_msg        | msg_type_t |  new_msg_type("set write response fifo depth")                   |                   |
| axi_slave_set_address_stall_probability_msg        | msg_type_t |  new_msg_type("axi slave set address channel stall probability") |                   |
| axi_slave_set_data_stall_probability_msg           | msg_type_t |  new_msg_type("axi slave set data stall probability")            |                   |
| axi_slave_set_write_response_stall_probability_msg | msg_type_t |  new_msg_type("axi slave set write response stall probability")  |                   |
| axi_slave_set_response_latency_msg                 | msg_type_t |  new_msg_type("axi slave response latency probability")          |                   |
| axi_slave_configure_4kbyte_boundary_check_msg      | msg_type_t |  new_msg_type("axi slave configure 4kbyte boundary check")       |                   |
| axi_slave_get_statistics_msg                       | msg_type_t |  new_msg_type("axi slave get statistics")                        |                   |
| axi_slave_enable_well_behaved_check_msg            | msg_type_t |  new_msg_type("axi slave enable well behaved check")             |                   |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| axi_slave_t |      |             |
## Functions
- get_logger <font id="function_arguments">(axi_slave : axi_slave_t) </font> <font id="function_return">return logger_t </font>
**Description**
Get the logger used by the axi_slave
- set_address_fifo_depth <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; depth : positive) </font> <font id="function_return">return ()</font>
**Description**
Set the maximum number address channel tokens that can be queued
- set_write_response_fifo_depth <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; depth : positive) </font> <font id="function_return">return ()</font>
**Description**
Set the maximum number write responses that can be queued
- set_address_stall_probability <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; probability : probability_t) </font> <font id="function_return">return ()</font>
**Description**
Set the address channel stall probability
- set_data_stall_probability <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; probability : probability_t) </font> <font id="function_return">return ()</font>
**Description**
Set the data channel stall probability
- set_write_response_stall_probability <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; probability : probability_t) </font> <font id="function_return">return ()</font>
**Description**
Set the write response stall probability
- set_response_latency <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; min_latency, max_latency : delay_length) </font> <font id="function_return">return ()</font>
**Description**
The response latency is randomly choosen in the uniform interval:[min_latency, max_latency]
- set_response_latency <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; latency : delay_length) </font> <font id="function_return">return ()</font>
**Description**
Short hand for set_response_latency when min and max are the same
- enable_4kbyte_boundary_check <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t) </font> <font id="function_return">return ()</font>
- disable_4kbyte_boundary_check <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t) </font> <font id="function_return">return ()</font>
- get_statistics <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t; variable stat  : inout axi_statistics_t; clear : boolean := false) </font> <font id="function_return">return ()</font>
**Description**
Get statistics object from axi slaveDynamically allocates new statistics object which must he deallocated whenusedThis procedure will automatically deallocate the input statistics objectif it is not null
- enable_well_behaved_check <font id="function_arguments">(signal net : inout network_t; axi_slave : axi_slave_t) </font> <font id="function_return">return ()</font>
**Description**
Check that bursts are well behaved, that is that data channel traffic isas compact as possibleFor write:1. awvalid never high without wvalid2. wvalid never goes low during active burst3. uses max awsize supported by data width4. bready never low during active burstFor read:1. rready never low during active burst2. uses max arsize supported by data width
