# Entity: tb_sobel_x
## Diagram
![Diagram](tb_sobel_x.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
| tb_path      | string |       |             |
## Signals
| Name             | Type                                | Description |
| ---------------- | ----------------------------------- | ----------- |
| clk              | std_logic                           |             |
| input_tvalid     | std_logic                           |             |
| input_tlast      | std_logic                           |             |
| input_tdata      | unsigned(13 downto 0)               |             |
| output_tvalid    | std_logic                           |             |
| output_tlast     | std_logic                           |             |
| output_tdata     | signed(input_tdata'length downto 0) |             |
| start            | boolean                             |             |
|  data_check_done | boolean                             |             |
|  stimuli_done    | boolean                             |             |
## Processes
- main: _(  )_

- stimuli_process: _(  )_

- data_check_process: _(  )_

## Instantiations
- dut: work.sobel_x
