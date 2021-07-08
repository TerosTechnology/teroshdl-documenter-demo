# Entity: tb_check_sequence

## Diagram

![Diagram](tb_check_sequence.svg "Diagram")
## Description

This test suite verifies the check_sequence checker.
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

| Name                   | Type                           | Description |
| ---------------------- | ------------------------------ | ----------- |
| clk                    | std_logic                      |             |
| inp                    | slv_vector(1 to n_checks)      |             |
| en                     | std_logic                      |             |
| event_sequence         | std_logic_vector(23 downto 20) |             |
| start_check_sequence_4 | boolean                        |             |
## Constants

| Name         | Type      | Value                       | Description |
| ------------ | --------- | --------------------------- | ----------- |
| n_checks     | positive  |  5                          |             |
| my_checker_2 | checker_t |  new_checker("my_checker2") |             |
| my_checker_3 | checker_t |  new_checker("my_checker3") |             |
| my_checker_4 | checker_t |  new_checker("my_checker4") |             |
| my_checker_5 | checker_t |  new_checker("my_checker5") |             |
## Types

| Name       | Type                                                  | Description |
| ---------- | ----------------------------------------------------- | ----------- |
| slv_vector | array (natural range <>) of std_logic_vector(1 to 5)  |             |
## Processes
- clock: (  )
- check_sequence_4: (  )
- check_sequence_runner: (  )
