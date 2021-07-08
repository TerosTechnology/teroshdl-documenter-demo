# Entity: tb_check

## Diagram

![Diagram](tb_check.svg "Diagram")
## Description

This test suite verifies the check checker.
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
vunit: run_all_in_same_sim
## Generics

| Generic name             | Type    | Value | Description |
| ------------------------ | ------- | ----- | ----------- |
| use_check_not_check_true | boolean | true  |             |
| runner_cfg               | string  |       |             |
## Signals

| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| clk         | std_logic |             |
| check_in_1  | std_logic |             |
|  check_in_2 | std_logic |             |
|  check_in_3 | std_logic |             |
|  check_in_4 | std_logic |             |
| check_en_1  | std_logic |             |
|  check_en_2 | std_logic |             |
|  check_en_3 | std_logic |             |
|  check_en_4 | std_logic |             |
## Constants

| Name           | Type      | Value                                                                                   | Description |
| -------------- | --------- | --------------------------------------------------------------------------------------- | ----------- |
| check_checker  | checker_t |  new_checker("checker")                                                                 |             |
| check_checker2 | checker_t |  new_checker("checker2")                                                                |             |
| check_checker3 | checker_t |  new_checker("checker3",<br><span style="padding-left:20px"> default_log_level => info) |             |
| check_checker4 | checker_t |  new_checker("checker4")                                                                |             |
## Processes
- clock: (  )
- check_runner: (  )
