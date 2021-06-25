# Entity: axi_write_slave
## Diagram
![Diagram](axi_write_slave.svg "Diagram")
## Generics
| Generic name | Type        | Value | Description |
| ------------ | ----------- | ----- | ----------- |
| axi_slave    | axi_slave_t |       |             |
## Ports
| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| aclk      | in        | std_logic        |             |
| awvalid   | in        | std_logic        |             |
| awready   | out       | std_logic        |             |
| awid      | in        | std_logic_vector |             |
| awaddr    | in        | std_logic_vector |             |
| awlen     | in        | std_logic_vector |             |
| awsize    | in        | std_logic_vector |             |
| awburst   | in        | axi_burst_type_t |             |
| wvalid    | in        | std_logic        |             |
| wready    | out       | std_logic        |             |
| wdata     | in        | std_logic_vector |             |
| wstrb     | in        | std_logic_vector |             |
| wlast     | in        | std_logic        |             |
| bvalid    | out       | std_logic        |             |
| bready    | in        | std_logic        |             |
| bid       | out       | std_logic_vector |             |
| bresp     | out       | axi_resp_t       |             |
## Signals
| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| initialized | boolean |             |
## Constants
| Name               | Type                      | Value                                 | Description |
| ------------------ | ------------------------- | ------------------------------------- | ----------- |
| data_vector_length | natural                   |  max_axi4_burst_length * wdata'length |             |
| data_pool          | integer_vector_ptr_pool_t |  new_integer_vector_ptr_pool          |             |
## Types
| Name         | Type | Description |
| ------------ | ---- | ----------- |
| burst_data_t |      |             |
## Functions
- push_burst_data <font id="function_arguments">(queue : queue_t; variable burst_data : inout burst_data_t)</font> <font id="function_return">return ()</font>
- recycle <font id="function_arguments">(variable burst_data : inout burst_data_t)</font> <font id="function_return">return ()</font>
## Processes
- control_process: _(  )_

- axi_process: _(  )_

- well_behaved_check: _(  )_

