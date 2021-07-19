# Entity: tb_avalon

- **File**: tb_avalon.vhd
## Diagram

![Diagram](tb_avalon.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
This test bench is to reproduce issue with pop form empty queue in modelsim.
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name          | Type                          | Description |
| ------------- | ----------------------------- | ----------- |
| av_address    | std_logic_vector(31 downto 0) |             |
| av_write      | std_logic                     |             |
| av_writedata  | std_logic_vector(31 downto 0) |             |
| av_read       | std_logic                     |             |
| av_readdata   | std_logic_vector(31 downto 0) |             |
| av_byteenable | std_logic_vector(3 downto 0)  |             |
| av_burstcount | std_logic_vector(3 downto 0)  |             |
| clk           | std_logic                     |             |
## Constants

| Name       | Type         | Value                                                                                                | Description |
| ---------- | ------------ | ---------------------------------------------------------------------------------------------------- | ----------- |
| avalon_bus | bus_master_t |  new_bus(data_length => 32,<br><span style="padding-left:20px"> address_length => av_address'length) |             |
| CLK_period | time         |  20 ns                                                                                               |             |
## Processes
- tests: (  )
## Instantiations

- avalon_master: vunit_lib.avalon_master
