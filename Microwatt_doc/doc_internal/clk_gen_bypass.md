# Entity: clock_generator

## Diagram

![Diagram](clk_gen_bypass.svg "Diagram")
## Generics

| Generic name  | Type     | Value    | Description |
| ------------- | -------- | -------- | ----------- |
| CLK_INPUT_HZ  | positive | 50000000 |             |
| CLK_OUTPUT_HZ | positive | 50000000 |             |
## Ports

| Port name      | Direction | Type      | Description |
| -------------- | --------- | --------- | ----------- |
| ext_clk        | in        | std_logic |             |
| pll_rst_in     | in        | std_logic |             |
| pll_clk_out    | out       | std_logic |             |
| pll_locked_out | out       | std_logic |             |
