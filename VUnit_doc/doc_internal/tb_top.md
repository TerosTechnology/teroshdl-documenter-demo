# Entity: tb_top
## Diagram
![Diagram](tb_top.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name      | Type                         | Description |
| --------- | ---------------------------- | ----------- |
| clk       | std_logic                    |             |
| rstn      | std_logic                    |             |
| in_valid  | std_logic                    |             |
| in_ready  | std_logic                    |             |
| in_data   | std_logic_vector(7 downto 0) |             |
| out_valid | std_logic                    |             |
| out_ready | std_logic                    |             |
| out_data  | std_logic_vector(7 downto 0) |             |
| start     | boolean                      |             |
|  done     | boolean                      |             |
## Constants
| Name     | Type    | Value | Description |
| -------- | ------- | ----- | ----------- |
| num_data | integer |  128  |             |
## Processes
- main: _(  )_

- stimuli: _(  )_

- data_check: _(  )_

## Instantiations
- dut: lib.top
