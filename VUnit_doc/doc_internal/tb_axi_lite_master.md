# Entity: tb_axi_lite_master

- **File**: tb_axi_lite_master.vhd
## Diagram

![Diagram](tb_axi_lite_master.svg "Diagram")
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

| Name    | Type                          | Description |
| ------- | ----------------------------- | ----------- |
| clk     | std_logic                     |             |
| arready | std_logic                     |             |
| arvalid | std_logic                     |             |
| araddr  | std_logic_vector(31 downto 0) |             |
| rready  | std_logic                     |             |
| rvalid  | std_logic                     |             |
| rdata   | std_logic_vector(15 downto 0) |             |
| rresp   | std_logic_vector(1 downto 0)  |             |
| awready | std_logic                     |             |
| awvalid | std_logic                     |             |
| awaddr  | std_logic_vector(31 downto 0) |             |
| wready  | std_logic                     |             |
| wvalid  | std_logic                     |             |
| wdata   | std_logic_vector(15 downto 0) |             |
| wstrb   | std_logic_vector(1 downto 0)  |             |
| bvalid  | std_logic                     |             |
| bready  | std_logic                     |             |
| bresp   | std_logic_vector(1 downto 0)  |             |
| start   | boolean                       |             |
|  done   | boolean                       |             |
## Constants

| Name             | Type         | Value                                                                                                                                                      | Description |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| num_random_tests | integer      |  128                                                                                                                                                       |             |
| bus_handle       | bus_master_t |  new_bus(data_length => wdata'length,<br><span style="padding-left:20px">                                                 address_length => awaddr'length) |             |
## Processes
- main: (  )
- support: (  )
## Instantiations

- dut: work.axi_lite_master
