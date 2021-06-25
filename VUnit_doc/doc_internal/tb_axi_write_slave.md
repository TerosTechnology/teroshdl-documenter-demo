# Entity: tb_axi_write_slave
## Diagram
![Diagram](tb_axi_write_slave.svg "Diagram")
## Description
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name    | Type                                     | Description |
| ------- | ---------------------------------------- | ----------- |
| clk     | std_logic                                |             |
| awvalid | std_logic                                |             |
| awready | std_logic                                |             |
| awid    | std_logic_vector(3 downto 0)             |             |
| awaddr  | std_logic_vector(31 downto 0)            |             |
| awlen   | axi4_len_t                               |             |
| awsize  | axi4_size_t                              |             |
| awburst | axi_burst_type_t                         |             |
| wvalid  | std_logic                                |             |
| wready  | std_logic                                |             |
| wdata   | std_logic_vector(8*data_size-1 downto 0) |             |
| wstrb   | std_logic_vector(data_size downto 0)     |             |
| wlast   | std_logic                                |             |
| bvalid  | std_logic                                |             |
| bready  | std_logic                                |             |
| bid     | std_logic_vector(awid'range)             |             |
| bresp   | axi_resp_t                               |             |
## Constants
| Name          | Type        | Value                            | Description |
| ------------- | ----------- | -------------------------------- | ----------- |
| log_data_size | integer     |  4                               |             |
| data_size     | integer     |  2**log_data_size                |             |
| memory        | memory_t    |  new_memory                      |             |
| axi_slave     | axi_slave_t |  new_axi_slave(memory => memory) |             |
## Processes
- main: _(  )_

## Instantiations
- dut: work.axi_write_slave
