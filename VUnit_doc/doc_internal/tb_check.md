# Entity: tb_check
## Diagram
![Diagram](tb_check.svg "Diagram")
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
| Name           | Type      | Value                                               | Description |
| -------------- | --------- | --------------------------------------------------- | ----------- |
| check_checker  | checker_t |  new_checker("checker")                             |             |
| check_checker2 | checker_t |  new_checker("checker2")                            |             |
| check_checker3 | checker_t |  new_checker("checker3", default_log_level => info) |             |
| check_checker4 | checker_t |  new_checker("checker4")                            |             |
## Processes
- clock: _(  )_

- check_runner: _(  )_

