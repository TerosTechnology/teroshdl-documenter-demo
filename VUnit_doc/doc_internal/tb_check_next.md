# Entity: tb_check_next

## Diagram

![Diagram](tb_check_next.svg "Diagram")
## Description

This test suite verifies the check_next checker.
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

| Name                 | Type                     | Description |
| -------------------- | ------------------------ | ----------- |
| clk                  | std_logic                |             |
| check_next_in_1      | std_logic_vector(1 to 3) |             |
|  check_next_in_2     | std_logic_vector(1 to 3) |             |
|  check_next_in_3     | std_logic_vector(1 to 3) |             |
|  check_next_in_4     | std_logic_vector(1 to 3) |             |
| 
    check_next_in_5 | std_logic_vector(1 to 3) |             |
|  check_next_in_6     | std_logic_vector(1 to 3) |             |
|  check_next_in_7     | std_logic_vector(1 to 3) |             |
|  check_next_in_8     | std_logic_vector(1 to 3) |             |
## Constants

| Name        | Type      | Value                                                  | Description |
| ----------- | --------- | ------------------------------------------------------ | ----------- |
| my_checker2 | checker_t |  new_checker("my_checker2")                            |             |
| my_checker3 | checker_t |  new_checker("my_checker3", default_log_level => info) |             |
| my_checker4 | checker_t |  new_checker("my_checker4")                            |             |
| my_checker5 | checker_t |  new_checker("my_checker5")                            |             |
## Processes
- clock: (  )
- check_next_runner: (  )
