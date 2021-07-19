# Entity: top

- **File**: top.vhd
## Diagram

![Diagram](top.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
A simple entity just for example
## Ports

| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| rstn      | in        | std_logic                    |             |
| in_valid  | in        | std_logic                    |             |
| in_ready  | out       | std_logic                    |             |
| in_data   | in        | std_logic_vector(7 downto 0) |             |
| out_valid | out       | std_logic                    |             |
| out_ready | in        | std_logic                    |             |
| out_data  | out       | std_logic_vector(7 downto 0) |             |
## Instantiations

- fifo_8b_32w_inst: component fifo_8b_32w
