# Entity: neorv32_pwm
## Diagram
![Diagram](neorv32_pwm.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| NUM_CHANNELS | natural | 4     |             |
## Ports
| Port name   | Direction | Type                                       | Description |
| ----------- | --------- | ------------------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                                 |             |
| addr_i      | in        | std_ulogic_vector(31 downto 0)             |             |
| rden_i      | in        | std_ulogic                                 |             |
| wren_i      | in        | std_ulogic                                 |             |
| data_i      | in        | std_ulogic_vector(31 downto 0)             |             |
| data_o      | out       | std_ulogic_vector(31 downto 0)             |             |
| ack_o       | out       | std_ulogic                                 |             |
| clkgen_en_o | out       | std_ulogic                                 |             |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0)             |             |
| pwm_o       | out       | std_ulogic_vector(NUM_CHANNELS-1 downto 0) |             |
## Signals
| Name      | Type                           | Description |
| --------- | ------------------------------ | ----------- |
| acc_en    | std_ulogic                     |             |
| addr      | std_ulogic_vector(31 downto 0) |             |
| wren      | std_ulogic                     |             |
| rden      | std_ulogic                     |             |
| pwm_ch    | pwm_ch_t                       |             |
| enable    | std_ulogic                     |             |
| prsc      | std_ulogic_vector(2 downto 0)  |             |
| pwm_ch_rd | pwm_ch_rd_t                    |             |
| prsc_tick | std_ulogic                     |             |
| pwm_cnt   | std_ulogic_vector(7 downto 0)  |             |
## Constants
| Name             | Type    | Value                      | Description |
| ---------------- | ------- | -------------------------- | ----------- |
| hi_abb_c         | natural |  index_size_f(io_size_c)-1 |             |
| lo_abb_c         | natural |  index_size_f(pwm_size_c)  |             |
| ctrl_enable_c    | natural |  0                         |             |
| ctrl_prsc0_bit_c | natural |  1                         |             |
| ctrl_prsc1_bit_c | natural |  2                         |             |
| ctrl_prsc2_bit_c | natural |  3                         |             |
## Types
| Name        | Type | Description |
| ----------- | ---- | ----------- |
| pwm_ch_t    |      |             |
| pwm_ch_rd_t |      |             |
## Processes
- wr_access: _( clk_i )_

- pwm_dc_rd_gen: _( pwm_ch )_

- pwm_core: _( clk_i )_

