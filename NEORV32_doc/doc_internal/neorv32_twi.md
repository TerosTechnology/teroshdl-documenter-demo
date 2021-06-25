# Entity: neorv32_twi
## Diagram
![Diagram](neorv32_twi.svg "Diagram")
## Ports
| Port name   | Direction | Type                           | Description |
| ----------- | --------- | ------------------------------ | ----------- |
| clk_i       | in        | std_ulogic                     |             |
| addr_i      | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i      | in        | std_ulogic                     |             |
| wren_i      | in        | std_ulogic                     |             |
| data_i      | in        | std_ulogic_vector(31 downto 0) |             |
| data_o      | out       | std_ulogic_vector(31 downto 0) |             |
| ack_o       | out       | std_ulogic                     |             |
| clkgen_en_o | out       | std_ulogic                     |             |
| clkgen_i    | in        | std_ulogic_vector(07 downto 0) |             |
| twi_sda_io  | inout     | std_logic                      |             |
| twi_scl_io  | inout     | std_logic                      |             |
| irq_o       | out       | std_ulogic                     |             |
## Signals
| Name           | Type                           | Description |
| -------------- | ------------------------------ | ----------- |
| acc_en         | std_ulogic                     |             |
| addr           | std_ulogic_vector(31 downto 0) |             |
| wr_en          | std_ulogic                     |             |
| rd_en          | std_ulogic                     |             |
| twi_clk        | std_ulogic                     |             |
| twi_phase_gen  | std_ulogic_vector(3 downto 0)  |             |
| twi_clk_phase  | std_ulogic_vector(3 downto 0)  |             |
| twi_clk_halt   | std_ulogic                     |             |
| ctrl           | std_ulogic_vector(7 downto 0)  |             |
| arbiter        | std_ulogic_vector(2 downto 0)  |             |
| twi_bitcnt     | std_ulogic_vector(3 downto 0)  |             |
| twi_rtx_sreg   | std_ulogic_vector(8 downto 0)  |             |
| twi_sda_i_ff0  | std_ulogic                     |             |
|  twi_sda_i_ff1 | std_ulogic                     |             |
| twi_scl_i_ff0  | std_ulogic                     |             |
|  twi_scl_i_ff1 | std_ulogic                     |             |
| twi_sda_i      | std_ulogic                     |             |
|      twi_sda_o | std_ulogic                     |             |
| twi_scl_i      | std_ulogic                     |             |
|      twi_scl_o | std_ulogic                     |             |
## Constants
| Name              | Type    | Value                      | Description |
| ----------------- | ------- | -------------------------- | ----------- |
| hi_abb_c          | natural |  index_size_f(io_size_c)-1 |             |
| lo_abb_c          | natural |  index_size_f(twi_size_c)  |             |
| ctrl_twi_en_c     | natural |  0                         |             |
| ctrl_twi_start_c  | natural |  1                         |             |
| ctrl_twi_stop_c   | natural |  2                         |             |
| ctrl_twi_prsc0_c  | natural |  3                         |             |
| ctrl_twi_prsc1_c  | natural |  4                         |             |
| ctrl_twi_prsc2_c  | natural |  5                         |             |
| ctrl_twi_mack_c   | natural |  6                         |             |
| ctrl_twi_cksten_c | natural |  7                         |             |
| ctrl_twi_ack_c    | natural |  30                        |             |
| ctrl_twi_busy_c   | natural |  31                        |             |
## Processes
- rw_access: _( clk_i )_

- clock_phase_gen: _( clk_i )_

- twi_rtx_unit: _( clk_i )_

- clock_stretching: _( ctrl, arbiter, twi_scl_o, twi_scl_i_ff1 )_

