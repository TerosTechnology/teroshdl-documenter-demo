# Entity: tb_axi_read_slave
## Diagram
![Diagram](tb_axi_read_slave.svg "Diagram")
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
| arvalid | std_logic                                |             |
| arready | std_logic                                |             |
| arid    | std_logic_vector(3 downto 0)             |             |
| araddr  | std_logic_vector(31 downto 0)            |             |
| arlen   | axi4_len_t                               |             |
| arsize  | axi4_size_t                              |             |
| arburst | axi_burst_type_t                         |             |
| rvalid  | std_logic                                |             |
| rready  | std_logic                                |             |
| rid     | std_logic_vector(arid'range)             |             |
| rdata   | std_logic_vector(8*data_size-1 downto 0) |             |
| rresp   | axi_resp_t                               |             |
| rlast   | std_logic                                |             |
## Constants
| Name          | Type        | Value                                                                                                         | Description |
| ------------- | ----------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| log_data_size | integer     |  4                                                                                                            |             |
| data_size     | integer     |  2**log_data_size                                                                                             |             |
| memory        | memory_t    |  new_memory                                                                                                   |             |
| axi_slave     | axi_slave_t |  new_axi_slave(address_fifo_depth => 1,                                                     memory => memory) |             |
## Processes
- main: _(  )_

## Instantiations
- dut: work.axi_read_slave
