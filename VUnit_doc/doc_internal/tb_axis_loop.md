# Entity: tb_axis_loop
## Diagram
![Diagram](tb_axis_loop.svg "Diagram")
## Generics
| Generic name | Type   | Value          | Description |
| ------------ | ------ | -------------- | ----------- |
| runner_cfg   | string |                |             |
| tb_path      | string |                |             |
| csv_i        | string | "data/in.csv"  |             |
| csv_o        | string | "data/out.csv" |             |
## Signals
| Name   | Type      | Description |
| ------ | --------- | ----------- |
| clk    | std_logic |             |
|  rst   | std_logic |             |
|  rstn  | std_logic |             |
| start  | boolean   |             |
|  done  | boolean   |             |
|  saved | boolean   |             |
## Constants
| Name              | Type                | Value                                                                                                        | Description |
| ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| clk_period        | time                |  20 ns                                                                                                       |             |
| data_width        | natural             |  32                                                                                                          |             |
| master_axi_stream | axi_stream_master_t |  new_axi_stream_master(     data_length => data_width,     stall_config => new_stall_config(0.05, 1, 10)   ) |             |
| slave_axi_stream  | axi_stream_slave_t  |  new_axi_stream_slave(     data_length => data_width,     stall_config => new_stall_config(0.05, 1, 10)   )  |             |
| m_I               | integer_array_t     |  load_csv(tb_path & csv_i)                                                                                   |             |
| m_O               | integer_array_t     |  new_2d(width(m_I), height(m_I), data_width, true)                                                           |             |
## Processes
- main: _(  )_

- stimuli: _(  )_

- save: _(  )_

## Instantiations
- uut_vc: work.vc_axis
