# Entity: run_tests
## Diagram
![Diagram](run_tests.svg "Diagram")
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

