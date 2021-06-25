# Entity: tb_check_not_unknown
## Diagram
![Diagram](tb_check_not_unknown.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name                    | Type                         | Description |
| ----------------------- | ---------------------------- | ----------- |
| clk                     | std_logic                    |             |
| check_not_unknown_in_1  | std_logic_vector(8 downto 0) |             |
|  check_not_unknown_in_2 | std_logic_vector(8 downto 0) |             |
|  check_not_unknown_in_3 | std_logic_vector(8 downto 0) |             |
| check_not_unknown_in_4  | std_logic_vector(1 downto 0) |             |
|  check_not_unknown_in_5 | std_logic_vector(1 downto 0) |             |
|  check_not_unknown_in_6 | std_logic_vector(1 downto 0) |             |
## Constants
| Name        | Type      | Value                                                  | Description |
| ----------- | --------- | ------------------------------------------------------ | ----------- |
| my_checker  | checker_t |  new_checker("my_checker1")                            |             |
| my_checker2 | checker_t |  new_checker("my_checker2")                            |             |
| my_checker3 | checker_t |  new_checker("my_checker3", default_log_level => info) |             |
| my_checker4 | checker_t |  new_checker("my_checker4")                            |             |
| my_checker5 | checker_t |  new_checker("my_checker5")                            |             |
| my_checker6 | checker_t |  new_checker("my_checker6", default_log_level => info) |             |
## Processes
- clock: _(  )_

- check_not_unknown_runner: _(  )_

