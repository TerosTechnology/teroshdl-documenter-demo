# Entity: neorv32_wdt
## Diagram
![Diagram](neorv32_wdt.svg "Diagram")
## Ports
| Port name   | Direction | Type                           | Description |
| ----------- | --------- | ------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                     |             |
| rstn_i      | in        | std_ulogic                     |             |
| addr_i      | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i      | in        | std_ulogic                     |             |
| wren_i      | in        | std_ulogic                     |             |
| data_i      | in        | std_ulogic_vector(31 downto 0) |             |
| data_o      | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o       | out       | std_ulogic                     |             |
| clkgen_en_o | out       | std_ulogic                     |             |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |             |
| irq_o       | out       | std_ulogic                     |             |
| rstn_o      | out       | std_ulogic                     |             |
## Signals
| Name      | Type                           | Description |
| --------- | ------------------------------ | ----------- |
| acc_en    | std_ulogic                     |             |
| wren      | std_ulogic                     |             |
| rden      | std_ulogic                     |             |
| ctrl_reg  | ctrl_reg_t                     |             |
| prsc_tick | std_ulogic                     |             |
| wdt_cnt   | std_ulogic_vector(20 downto 0) |             |
| hw_rst    | std_ulogic                     |             |
| rst_gen   | std_ulogic_vector(03 downto 0) |             |
| rstn_sync | std_ulogic                     |             |
## Constants
| Name           | Type    | Value                      | Description |
| -------------- | ------- | -------------------------- | ----------- |
| hi_abb_c       | natural |  index_size_f(io_size_c)-1 |             |
| lo_abb_c       | natural |  index_size_f(wdt_size_c)  |             |
| ctrl_enable_c  | natural |  0                         |             |
| ctrl_clksel0_c | natural |  1                         |             |
| ctrl_clksel1_c | natural |  2                         |             |
| ctrl_clksel2_c | natural |  3                         |             |
| ctrl_mode_c    | natural |  4                         |             |
| ctrl_rcause_c  | natural |  5                         |             |
| ctrl_reset_c   | natural |  6                         |             |
| ctrl_force_c   | natural |  7                         |             |
| ctrl_lock_c    | natural |  8                         |             |
## Types
| Name       | Type | Description |
| ---------- | ---- | ----------- |
| ctrl_reg_t |      |             |
## Processes
- write_access: _( rstn_i, clk_i )_

- wdt_counter: _( clk_i )_

- reset_generator: _( rstn_i, clk_i )_

- read_access: _( clk_i )_

