# Entity: neorv32_uart
## Diagram
![Diagram](neorv32_uart.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| UART_PRIMARY | boolean | true  |             |
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
| uart_txd_o  | out       | std_ulogic                     |             |
| uart_rxd_i  | in        | std_ulogic                     |             |
| uart_rts_o  | out       | std_ulogic                     |             |
| uart_cts_i  | in        | std_ulogic                     |             |
| irq_rxd_o   | out       | std_ulogic                     |             |
| irq_txd_o   | out       | std_ulogic                     |             |
## Signals
| Name        | Type                           | Description |
| ----------- | ------------------------------ | ----------- |
| ctrl        | std_ulogic_vector(31 downto 0) |             |
| acc_en      | std_ulogic                     |             |
| addr        | std_ulogic_vector(31 downto 0) |             |
| wr_en       | std_ulogic                     |             |
| rd_en       | std_ulogic                     |             |
| uart_clk    | std_ulogic                     |             |
| num_bits    | std_ulogic_vector(03 downto 0) |             |
| uart_cts_ff | std_ulogic_vector(1 downto 0)  |             |
| uart_rts    | std_ulogic                     |             |
| uart_tx     | uart_tx_t                      |             |
| uart_rx     | uart_rx_t                      |             |
## Constants
| Name                   | Type                                       | Value                                                                                                  | Description |
| ---------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ----------- |
| uart_id_base_c         | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY, uart0_base_c,      uart1_base_c)                             |             |
| uart_id_size_c         | natural                                    |  cond_sel_natural_f(        UART_PRIMARY, uart0_size_c,      uart1_size_c)                             |             |
| uart_id_ctrl_addr_c    | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY, uart0_ctrl_addr_c, uart1_ctrl_addr_c)                        |             |
| uart_id_rtx_addr_c     | std_ulogic_vector(data_width_c-1 downto 0) |  cond_sel_stdulogicvector_f(UART_PRIMARY, uart0_rtx_addr_c,  uart1_rtx_addr_c)                         |             |
| hi_abb_c               | natural                                    |  index_size_f(io_size_c)-1                                                                             |             |
| lo_abb_c               | natural                                    |  index_size_f(uart_id_size_c)                                                                          |             |
| sim_screen_output_en_c | boolean                                    |  true                                                                                                  |             |
| sim_text_output_en_c   | boolean                                    |  true                                                                                                  |             |
| sim_data_output_en_c   | boolean                                    |  true                                                                                                  |             |
| sim_uart_text_file_c   | string                                     |  cond_sel_string_f(UART_PRIMARY, "neorv32.uart0.sim_mode.text.out", "neorv32.uart1.sim_mode.text.out") |             |
| sim_uart_data_file_c   | string                                     |  cond_sel_string_f(UART_PRIMARY, "neorv32.uart0.sim_mode.data.out", "neorv32.uart1.sim_mode.data.out") |             |
| ctrl_uart_baud00_c     | natural                                    |   0                                                                                                    |             |
| ctrl_uart_baud01_c     | natural                                    |   1                                                                                                    |             |
| ctrl_uart_baud02_c     | natural                                    |   2                                                                                                    |             |
| ctrl_uart_baud03_c     | natural                                    |   3                                                                                                    |             |
| ctrl_uart_baud04_c     | natural                                    |   4                                                                                                    |             |
| ctrl_uart_baud05_c     | natural                                    |   5                                                                                                    |             |
| ctrl_uart_baud06_c     | natural                                    |   6                                                                                                    |             |
| ctrl_uart_baud07_c     | natural                                    |   7                                                                                                    |             |
| ctrl_uart_baud08_c     | natural                                    |   8                                                                                                    |             |
| ctrl_uart_baud09_c     | natural                                    |   9                                                                                                    |             |
| ctrl_uart_baud10_c     | natural                                    |  10                                                                                                    |             |
| ctrl_uart_baud11_c     | natural                                    |  11                                                                                                    |             |
| ctrl_uart_sim_en_c     | natural                                    |  12                                                                                                    |             |
| ctrl_uart_rts_en_c     | natural                                    |  20                                                                                                    |             |
| ctrl_uart_cts_en_c     | natural                                    |  21                                                                                                    |             |
| ctrl_uart_pmode0_c     | natural                                    |  22                                                                                                    |             |
| ctrl_uart_pmode1_c     | natural                                    |  23                                                                                                    |             |
| ctrl_uart_prsc0_c      | natural                                    |  24                                                                                                    |             |
| ctrl_uart_prsc1_c      | natural                                    |  25                                                                                                    |             |
| ctrl_uart_prsc2_c      | natural                                    |  26                                                                                                    |             |
| ctrl_uart_cts_c        | natural                                    |  27                                                                                                    |             |
| ctrl_uart_en_c         | natural                                    |  28                                                                                                    |             |
| ctrl_uart_tx_busy_c    | natural                                    |  31                                                                                                    |             |
| data_rx_perr_c         | natural                                    |  28                                                                                                    |             |
| data_rx_ferr_c         | natural                                    |  29                                                                                                    |             |
| data_rx_overr_c        | natural                                    |  30                                                                                                    |             |
| data_rx_avail_c        | natural                                    |  31                                                                                                    |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| uart_tx_t     |      |             |
| ry_data_buf_t |      |             |
| uart_rx_t     |      |             |
## Processes
- rw_access: _( clk_i )_

- uart_tx_unit: _( clk_i )_

- uart_rx_unit: _( clk_i )_

- flow_control_buffer: _( clk_i )_

- sim_output: _( clk_i )_

