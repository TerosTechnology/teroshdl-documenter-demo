# Entity: tb_check_next
## Diagram
![Diagram](tb_check_next.svg "Diagram")
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
- clock: _(  )_

- check_next_runner: _(  )_

