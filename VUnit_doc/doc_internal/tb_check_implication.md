# Entity: tb_check_implication
## Diagram
![Diagram](tb_check_implication.svg "Diagram")
## Description
This test suite verifies the check_implication checker.
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
| Name                        | Type                     | Description |
| --------------------------- | ------------------------ | ----------- |
| clk                         | std_logic                |             |
| check_implication_in_1      | std_logic_vector(1 to 2) |             |
| 
    check_implication_in_2 | std_logic_vector(1 to 2) |             |
| 
    check_implication_in_3 | std_logic_vector(1 to 2) |             |
| 
    check_implication_in_4 | std_logic_vector(1 to 2) |             |
| check_implication_en_1      | std_logic                |             |
|  check_implication_en_2     | std_logic                |             |
|  check_implication_en_3     | std_logic                |             |
|  check_implication_en_4     | std_logic                |             |
## Constants
| Name        | Type      | Value                                                  | Description |
| ----------- | --------- | ------------------------------------------------------ | ----------- |
| my_checker  | checker_t |  new_checker("my_checker1")                            |             |
| my_checker2 | checker_t |  new_checker("my_checker2")                            |             |
| my_checker3 | checker_t |  new_checker("my_checker3", default_log_level => info) |             |
| my_checker4 | checker_t |  new_checker("my_checker4")                            |             |
## Processes
- clock: _(  )_

- check_implication_runner: _(  )_

