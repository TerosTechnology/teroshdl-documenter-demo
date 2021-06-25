# Entity: tb_composite_generics
## Diagram
![Diagram](tb_composite_generics.svg "Diagram")
## Generics
| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| encoded_tb_cfg | string |       |             |
| runner_cfg     | string |       |             |
## Signals
| Name         | Type      | Description |
| ------------ | --------- | ----------- |
| dumping_done | boolean   |             |
| data_valid   | std_logic |             |
| clk          | std_logic |             |
## Constants
| Name       | Type     | Value                   | Description |
| ---------- | -------- | ----------------------- | ----------- |
| tb_cfg     | tb_cfg_t |  decode(encoded_tb_cfg) |             |
| clk_period | time     |  2 ns                   |             |
## Types
| Name     | Type | Description |
| -------- | ---- | ----------- |
| tb_cfg_t |      |             |
## Functions
## Processes
- test_runner: _(  )_

