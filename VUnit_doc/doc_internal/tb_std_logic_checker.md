# Entity: tb_std_logic_checker
## Diagram
![Diagram](tb_std_logic_checker.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name  | Type                         | Description |
| ----- | ---------------------------- | ----------- |
| value | std_logic_vector(1 downto 0) |             |
## Constants
| Name           | Type             | Value                                 | Description |
| -------------- | ---------------- | ------------------------------------- | ----------- |
| logger         | logger_t         |  get_logger("signal_checker")         |             |
| signal_checker | signal_checker_t |  new_signal_checker(logger => logger) |             |
## Processes
- main: _(  )_

## Instantiations
- dut: work.std_logic_checker
