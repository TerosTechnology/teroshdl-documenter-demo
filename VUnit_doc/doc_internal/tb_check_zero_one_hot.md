# Entity: tb_check_zero_one_hot
## Diagram
![Diagram](tb_check_zero_one_hot.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name                     | Type                         | Description |
| ------------------------ | ---------------------------- | ----------- |
| clk                      | std_logic                    |             |
| check_zero_one_hot_in_1  | std_logic_vector(3 downto 0) |             |
|  check_zero_one_hot_in_2 | std_logic_vector(3 downto 0) |             |
|  check_zero_one_hot_in_3 | std_logic_vector(3 downto 0) |             |
| check_zero_one_hot_en_1  | std_logic                    |             |
|  check_zero_one_hot_en_2 | std_logic                    |             |
|  check_zero_one_hot_en_3 | std_logic                    |             |
## Constants
| Name        | Type      | Value                                                  | Description |
| ----------- | --------- | ------------------------------------------------------ | ----------- |
| my_checker2 | checker_t |  new_checker("my_checker2")                            |             |
| my_checker3 | checker_t |  new_checker("my_checker3", default_log_level => info) |             |
## Processes
- clock: _(  )_

- check_zero_one_hot_runner: _(  )_

