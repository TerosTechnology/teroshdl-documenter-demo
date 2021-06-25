# Entity: soc_reset
## Diagram
![Diagram](soc_reset.svg "Diagram")
## Generics
| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| PLL_RESET_BITS | integer | 5     |             |
| SOC_RESET_BITS | integer | 5     |             |
| RESET_LOW      | boolean | true  |             |
## Ports
| Port name     | Direction | Type       | Description |
| ------------- | --------- | ---------- | ----------- |
| ext_clk       | in        | std_ulogic |             |
| pll_clk       | in        | std_ulogic |             |
| pll_locked_in | in        | std_ulogic |             |
| ext_rst_in    | in        | std_ulogic |             |
| pll_rst_out   | out       | std_ulogic |             |
| rst_out       | out       | std_ulogic |             |
## Signals
| Name        | Type                                       | Description |
| ----------- | ------------------------------------------ | ----------- |
| ext_rst0_n  | std_ulogic                                 |             |
| ext_rst1_n  | std_ulogic                                 |             |
| ext_rst2_n  | std_ulogic                                 |             |
| rst0_n      | std_ulogic                                 |             |
| rst1_n      | std_ulogic                                 |             |
| rst2_n      | std_ulogic                                 |             |
| pll_rst_cnt | std_ulogic_vector(PLL_RESET_BITS downto 0) |             |
| soc_rst_cnt | std_ulogic_vector(SOC_RESET_BITS downto 0) |             |
## Processes
- pll_reset_0: _( ext_clk )_

- soc_reset_0: _( pll_clk )_

