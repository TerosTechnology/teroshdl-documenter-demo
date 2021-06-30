# Entity: tb_sobel_x

## Diagram

![Diagram](tb_sobel_x.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
| tb_path      | string |       |             |
## Signals

| Name             | Type                                | Description |
| ---------------- | ----------------------------------- | ----------- |
| clk              | std_logic                           |             |
| input_tvalid     | std_logic                           |             |
| input_tlast      | std_logic                           |             |
| input_tdata      | unsigned(13 downto 0)               |             |
| output_tvalid    | std_logic                           |             |
| output_tlast     | std_logic                           |             |
| output_tdata     | signed(input_tdata'length downto 0) |             |
| start            | boolean                             |             |
|  data_check_done | boolean                             |             |
|  stimuli_done    | boolean                             |             |
## Processes
- main: (  )
- stimuli_process: (  )
- data_check_process: (  )
## Instantiations

- dut: work.sobel_x
