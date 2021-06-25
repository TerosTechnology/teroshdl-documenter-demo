# Entity: tb_check_sequence
## Diagram
![Diagram](tb_check_sequence.svg "Diagram")
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
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| slv_vector |      |             |
## Processes
- clock: _(  )_

- check_sequence_4: _(  )_

- check_sequence_runner: _(  )_

