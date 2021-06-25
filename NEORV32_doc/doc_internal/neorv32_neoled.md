# Entity: neorv32_neoled
## Diagram
![Diagram](neorv32_neoled.svg "Diagram")
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
| irq_o       | out       | std_ulogic                     |             |
| neoled_o    | out       | std_ulogic                     |             |
## Signals
| Name      | Type                           | Description |
| --------- | ------------------------------ | ----------- |
| acc_en    | std_ulogic                     |             |
| addr      | std_ulogic_vector(31 downto 0) |             |
| wren      | std_ulogic                     |             |
| rden      | std_ulogic                     |             |
| ctrl      | ctrl_t                         |             |
| tx_buffer | tx_buffer_t                    |             |
| serial    | serial_t                       |             |
## Constants
| Name                | Type    | Value                        | Description |
| ------------------- | ------- | ---------------------------- | ----------- |
| tx_buffer_entries_c | natural |  4                           |             |
| hi_abb_c            | natural |  index_size_f(io_size_c)-1   |             |
| lo_abb_c            | natural |  index_size_f(neoled_size_c) |             |
| ctrl_enable_c       | natural |   0                          |             |
| ctrl_mode_c         | natural |   1                          |             |
| ctrl_bscon_c        | natural |   2                          |             |
| ctrl_clksel0_c      | natural |   3                          |             |
| ctrl_clksel1_c      | natural |   4                          |             |
| ctrl_clksel2_c      | natural |   5                          |             |
| ctrl_bufs_0_c       | natural |   6                          |             |
| ctrl_bufs_1_c       | natural |   7                          |             |
| ctrl_bufs_2_c       | natural |   8                          |             |
| ctrl_bufs_3_c       | natural |   9                          |             |
| ctrl_t_tot_0_c      | natural |  10                          |             |
| ctrl_t_tot_1_c      | natural |  11                          |             |
| ctrl_t_tot_2_c      | natural |  12                          |             |
| ctrl_t_tot_3_c      | natural |  13                          |             |
| ctrl_t_tot_4_c      | natural |  14                          |             |
| ctrl_t_0h_0_c       | natural |  15                          |             |
| ctrl_t_0h_1_c       | natural |  16                          |             |
| ctrl_t_0h_2_c       | natural |  17                          |             |
| ctrl_t_0h_3_c       | natural |  18                          |             |
| ctrl_t_0h_4_c       | natural |  19                          |             |
| ctrl_t_1h_0_c       | natural |  20                          |             |
| ctrl_t_1h_1_c       | natural |  21                          |             |
| ctrl_t_1h_2_c       | natural |  22                          |             |
| ctrl_t_1h_3_c       | natural |  23                          |             |
| ctrl_t_1h_4_c       | natural |  24                          |             |
| ctrl_tx_status_c    | natural |  30                          |             |
| ctrl_busy_c         | natural |  31                          |             |
## Types
| Name           | Type                                | Description |
| -------------- | ----------------------------------- | ----------- |
| ctrl_t         |                                     |             |
| tx_fifo_t      |                                     |             |
| tx_buffer_t    |                                     |             |
| serial_state_t | (S_IDLE, S_INIT, S_GETBIT, S_PULSE) |             |
| serial_t       |                                     |             |
## Processes
- rw_access: _( clk_i )_

- instr_prefetch_buffer: _( clk_i )_

- irq_generator: _( clk_i )_

- serial_engine: _( clk_i )_

