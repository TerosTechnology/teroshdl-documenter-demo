# Entity: tb_check_implication
## Diagram
![Diagram](tb_check_implication.svg "Diagram")
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

