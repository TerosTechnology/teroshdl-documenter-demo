# Entity: run_tests
## Diagram
![Diagram](run_tests.svg "Diagram")
## Description
This test suite verifies the VHDL test runner functionality
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| output_path  | string |       |             |
## Signals
| Name                            | Type    | Description |
| ------------------------------- | ------- | ----------- |
| start_test_process              | boolean |             |
|  start_test_process2            | boolean |             |
| test_process_completed          | boolean |             |
| start_locking_process           | boolean |             |
| start_test_runner_watchdog      | boolean |             |
|  test_runner_watchdog_completed | boolean |             |
## Constants
| Name                 | Type     | Value                               | Description |
| -------------------- | -------- | ----------------------------------- | ----------- |
| locking_proc1_logger | logger_t |  get_logger("locking_proc1_logger") |             |
| locking_proc2_logger | logger_t |  get_logger("locking_proc2")        |             |
## Functions
## Processes
- test_process: _(  )_

- test_process2: _(  )_

- locking_proc1: _(  )_

- locking_proc2: _(  )_

- watchdog: _(  )_

- test_runner: _(  )_

