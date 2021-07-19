# Entity: tb_check_false

- **File**: tb_check_false.vhd
## Diagram

![Diagram](tb_check_false.svg "Diagram")
## Description

This test suite verifies the check_false checker.
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
vunit: run_all_in_same_sim
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name              | Type      | Description |
| ----------------- | --------- | ----------- |
| clk               | std_logic |             |
| check_false_in_1  | std_logic |             |
|  check_false_in_2 | std_logic |             |
|  check_false_in_3 | std_logic |             |
|  check_false_in_4 | std_logic |             |
| check_false_en_1  | std_logic |             |
|  check_false_en_2 | std_logic |             |
|  check_false_en_3 | std_logic |             |
|  check_false_en_4 | std_logic |             |
## Constants

| Name                 | Type        | Value                                                                                   | Description |
| -------------------- | ----------- | --------------------------------------------------------------------------------------- | ----------- |
| check_false_checker  | checker_t   |  new_checker("checker1")                                                                |             |
| check_false_checker2 | checker_t   |  new_checker("checker2")                                                                |             |
| check_false_checker3 | checker_t   |  new_checker("checker3",<br><span style="padding-left:20px"> default_log_level => info) |             |
| check_false_checker4 | checker_t   |  new_checker("checker4")                                                                |             |
| default_level        | log_level_t |  error                                                                                  |             |
## Processes
- clock: (  )
- check_false_runner: (  )
