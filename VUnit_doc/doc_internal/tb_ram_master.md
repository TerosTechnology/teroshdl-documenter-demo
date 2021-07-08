# Entity: tb_ram_master

## Diagram

![Diagram](tb_ram_master.svg "Diagram")
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

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| clk   | std_logic                     |             |
| en    | std_logic                     |             |
| we    | std_logic_vector(3 downto 0)  |             |
| addr  | std_logic_vector(7 downto 0)  |             |
| wdata | std_logic_vector(31 downto 0) |             |
| rdata | std_logic_vector(31 downto 0) |             |
| start | boolean                       |             |
|  done | boolean                       |             |
## Constants

| Name                   | Type         | Value                                                                                                    | Description |
| ---------------------- | ------------ | -------------------------------------------------------------------------------------------------------- | ----------- |
| latency                | integer      |  2                                                                                                       |             |
| num_back_to_back_reads | integer      |  64                                                                                                      |             |
| bus_handle             | bus_master_t |  new_bus(data_length => wdata'length,<br><span style="padding-left:20px"> address_length => addr'length) |             |
## Processes
- main: (  )
- support: (  )
## Instantiations

- dut: work.ram_master
