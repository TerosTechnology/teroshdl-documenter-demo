# Entity: tb_check_false
## Diagram
![Diagram](tb_check_false.svg "Diagram")
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
| Name                 | Type        | Value                                               | Description |
| -------------------- | ----------- | --------------------------------------------------- | ----------- |
| check_false_checker  | checker_t   |  new_checker("checker1")                            |             |
| check_false_checker2 | checker_t   |  new_checker("checker2")                            |             |
| check_false_checker3 | checker_t   |  new_checker("checker3", default_log_level => info) |             |
| check_false_checker4 | checker_t   |  new_checker("checker4")                            |             |
| default_level        | log_level_t |  error                                              |             |
## Processes
- clock: _(  )_

- check_false_runner: _(  )_

