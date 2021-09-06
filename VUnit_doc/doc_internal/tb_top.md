# Entity: tb_top

- **File**: tb_top.vhd
## Diagram

![Diagram](tb_top.svg "Diagram")
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

| Name      | Type                         | Description |
| --------- | ---------------------------- | ----------- |
| clk       | std_logic                    |             |
| rstn      | std_logic                    |             |
| in_valid  | std_logic                    |             |
| in_ready  | std_logic                    |             |
| in_data   | std_logic_vector(7 downto 0) |             |
| out_valid | std_logic                    |             |
| out_ready | std_logic                    |             |
| out_data  | std_logic_vector(7 downto 0) |             |
| start     | boolean                      |             |
|  done     | boolean                      |             |
## Constants

| Name     | Type    | Value | Description |
| -------- | ------- | ----- | ----------- |
| num_data | integer |  128  |             |
## Processes
- main: (  )
- stimuli: (  )
- data_check: (  )
## Instantiations

- dut: lib.top
