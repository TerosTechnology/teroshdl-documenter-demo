# Entity: ram_master
## Diagram
![Diagram](ram_master.svg "Diagram")
## Description
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics
| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| bus_handle   | bus_master_t |       |             |
| latency      | positive     |       |             |
## Ports
| Port name | Direction | Type                                                        | Description |
| --------- | --------- | ----------------------------------------------------------- | ----------- |
| clk       | in        | std_logic                                                   |             |
| en        | out       | std_logic                                                   |             |
| we        | out       | std_logic_vector(byte_enable_length(bus_handle)-1 downto 0) |             |
| addr      | out       | std_logic_vector(address_length(bus_handle)-1 downto 0)     |             |
| wdata     | out       | std_logic_vector(data_length(bus_handle)-1 downto 0)        |             |
| rdata     | in        | std_logic_vector(data_length(bus_handle)-1 downto 0)        |             |
## Signals
| Name    | Type                             | Description |
| ------- | -------------------------------- | ----------- |
| rd      | std_logic                        |             |
| rd_pipe | std_logic_vector(0 to latency-1) |             |
## Constants
| Name          | Type    | Value      | Description |
| ------------- | ------- | ---------- | ----------- |
| request_queue | queue_t |  new_queue |             |
## Processes
- main: _(  )_

- read_return: _(  )_

