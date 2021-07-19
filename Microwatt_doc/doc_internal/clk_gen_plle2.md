# Entity: clock_generator

- **File**: clk_gen_plle2.vhd
## Diagram

![Diagram](clk_gen_plle2.svg "Diagram")
## Generics

| Generic name  | Type     | Value     | Description |
| ------------- | -------- | --------- | ----------- |
| CLK_INPUT_HZ  | positive | 100000000 |             |
| CLK_OUTPUT_HZ | positive | 100000000 |             |
## Ports

| Port name      | Direction | Type      | Description |
| -------------- | --------- | --------- | ----------- |
| ext_clk        | in        | std_logic |             |
| pll_rst_in     | in        | std_logic |             |
| pll_clk_out    | out       | std_logic |             |
| pll_locked_out | out       | std_logic |             |
## Signals

| Name  | Type       | Description |
| ----- | ---------- | ----------- |
| clkfb | std_ulogic |             |
## Constants

| Name         | Type           | Value                                                                                            | Description |
| ------------ | -------------- | ------------------------------------------------------------------------------------------------ | ----------- |
| pll_settings | pll_settings_t |  gen_pll_settings(clk_input_hz,<br><span style="padding-left:20px"> 							       clk_output_hz) |             |
## Types

| Name           | Type | Description |
| -------------- | ---- | ----------- |
| pll_settings_t |      |             |
## Functions
- gen_pll_settings <font id="function_arguments">( constant input_hz : positive;<br><span style="padding-left:20px"> constant output_hz : positive) </font> <font id="function_return">return pll_settings_t </font>
## Instantiations

- pll: PLLE2_BASE
