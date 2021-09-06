# Entity: tb_check_stable

- **File**: tb_check_stable.vhd
## Diagram

![Diagram](tb_check_stable.svg "Diagram")
## Description

 This test suite verifies the check_stable checker.

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

| Name                       | Type                     | Description |
| -------------------------- | ------------------------ | ----------- |
| clk                        | std_logic                |             |
| check_stable_in_1          | std_logic_vector(1 to 5) |             |
|  check_stable_in_2         | std_logic_vector(1 to 5) |             |
|  check_stable_in_3         | std_logic_vector(1 to 5) |             |
| 
    check_stable_in_8     | std_logic_vector(1 to 5) |             |
|  check_stable_in_10        | std_logic_vector(1 to 5) |             |
| check_stable_start_event_4 | std_logic                |             |
| check_stable_end_event_4   | std_logic                |             |
| check_stable_expr_4        | std_logic_vector(7 to 9) |             |
| check_stable_in_5          | std_logic_vector(1 to 3) |             |
|  check_stable_in_6         | std_logic_vector(1 to 3) |             |
|  check_stable_in_7         | std_logic_vector(1 to 3) |             |
|  check_stable_in_9         | std_logic_vector(1 to 3) |             |
| 
    check_stable_in_11    | std_logic_vector(1 to 3) |             |
| check_stable_en_1          | std_logic                |             |
|  check_stable_en_2         | std_logic                |             |
|  check_stable_en_3         | std_logic                |             |
|  check_stable_en_4         | std_logic                |             |
| check_stable_en_5          | std_logic                |             |
|  check_stable_en_6         | std_logic                |             |
|  check_stable_en_7         | std_logic                |             |
|  check_stable_en_8         | std_logic                |             |
| check_stable_en_9          | std_logic                |             |
|  check_stable_en_10        | std_logic                |             |
|  check_stable_en_11        | std_logic                |             |
| en                         | std_logic                |             |
|  start_event               | std_logic                |             |
|  end_event                 | std_logic                |             |
|  expr                      | std_logic                |             |
## Constants

| Name         | Type      | Value                                                                                      | Description |
| ------------ | --------- | ------------------------------------------------------------------------------------------ | ----------- |
| my_checker2  | checker_t |  new_checker("my_checker2")                                                                |             |
| my_checker3  | checker_t |  new_checker("my_checker3",<br><span style="padding-left:20px"> default_log_level => info) |             |
| my_checker6  | checker_t |  new_checker("my_checker6")                                                                |             |
| my_checker7  | checker_t |  new_checker("my_checker7",<br><span style="padding-left:20px"> default_log_level => info) |             |
| my_checker10 | checker_t |  new_checker("my_checker10")                                                               |             |
| my_checker11 | checker_t |  new_checker("my_checker11")                                                               |             |
## Processes
- clock: (  )
- check_stable_runner: (  )
