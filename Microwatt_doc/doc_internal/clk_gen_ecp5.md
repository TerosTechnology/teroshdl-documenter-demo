# Entity: clock_generator

- **File**: clk_gen_ecp5.vhd
## Diagram

![Diagram](clk_gen_ecp5.svg "Diagram")
## Generics

| Generic name  | Type     | Value    | Description |
| ------------- | -------- | -------- | ----------- |
| CLK_INPUT_HZ  | positive | 12000000 |             |
| CLK_OUTPUT_HZ | positive | 50000000 |             |
## Ports

| Port name      | Direction | Type      | Description |
| -------------- | --------- | --------- | ----------- |
| ext_clk        | in        | std_logic |             |
| pll_rst_in     | in        | std_logic |             |
| pll_clk_out    | out       | std_logic |             |
| pll_locked_out | out       | std_logic |             |
## Signals

| Name  | Type      | Description |
| ----- | --------- | ----------- |
| clkop | std_logic |             |
| lock  | std_logic |             |
## Constants

| Name          | Type    | Value                  | Description                               |
| ------------- | ------- | ---------------------- | ----------------------------------------- |
| PLL_IN        | natural |     2000000            | PLL constants based on prjtrellis example |
| PLL_OUT       | natural |  600000000             |                                           |
| PLL_CLKOP_DIV | natural |  PLL_OUT/CLK_OUTPUT_HZ | Configration for ECP5 PLL                 |
| PLL_CLKFB_DIV | natural |  CLK_OUTPUT_HZ/PLL_IN  |                                           |
| PLL_CLKI_DIV  | natural |  CLK_INPUT_HZ/PLL_IN   |                                           |
## Instantiations

- clkgen: EHXPLLL
**Description**
FIXME: EHXPLLL lock signal active low?!?

