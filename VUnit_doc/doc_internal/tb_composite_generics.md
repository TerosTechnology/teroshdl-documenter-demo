# Entity: tb_composite_generics
## Diagram
![Diagram](tb_composite_generics.svg "Diagram")
## Description
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics
| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| encoded_tb_cfg | string |       |             |
| runner_cfg     | string |       |             |
## Signals
| Name         | Type      | Description |
| ------------ | --------- | ----------- |
| dumping_done | boolean   |             |
| data_valid   | std_logic |             |
| clk          | std_logic |             |
## Constants
| Name       | Type     | Value                   | Description |
| ---------- | -------- | ----------------------- | ----------- |
| tb_cfg     | tb_cfg_t |  decode(encoded_tb_cfg) |             |
| clk_period | time     |  2 ns                   |             |
## Types
| Name     | Type | Description |
| -------- | ---- | ----------- |
| tb_cfg_t |      |             |
## Functions
## Processes
- test_runner: _(  )_

