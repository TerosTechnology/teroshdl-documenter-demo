# Entity: uvvm_demo_th
## Diagram
![Diagram](uvvm_demo_th.svg "Diagram")
## Generics
| Generic name                 | Type                 | Value              | Description |
| ---------------------------- | -------------------- | ------------------ | ----------- |
| GC_CLK_PERIOD                | time                 | 10 ns              |             |
| GC_BIT_PERIOD                | time                 | 16 * GC_CLK_PERIOD |             |
| GC_ADDR_RX_DATA              | unsigned(2 downto 0) | "000"              |             |
| GC_ADDR_RX_DATA_VALID        | unsigned(2 downto 0) | "001"              |             |
| GC_ADDR_TX_DATA              | unsigned(2 downto 0) | "010"              |             |
| GC_ADDR_TX_READY             | unsigned(2 downto 0) | "011"              |             |
| GC_ACTIVITY_WATCHDOG_TIMEOUT | time                 | 50 * GC_BIT_PERIOD |             |
## Signals
| Name        | Type                         | Description |
| ----------- | ---------------------------- | ----------- |
| clk         | std_logic                    |             |
| arst        | std_logic                    |             |
| cs          | std_logic                    |             |
| addr        | unsigned(2 downto 0)         |             |
| wr          | std_logic                    |             |
| rd          | std_logic                    |             |
| wdata       | std_logic_vector(7 downto 0) |             |
| rdata       | std_logic_vector(7 downto 0) |             |
| ready       | std_logic                    |             |
| uart_vvc_rx | std_logic                    |             |
| uart_vvc_tx | std_logic                    |             |
## Constants
| Name                            | Type                    | Value                                                                                                                                                                                                                                                           | Description |
| ------------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| C_SBI_VVC                       | natural                 |  1                                                                                                                                                                                                                                                              |             |
| C_UART_TX_VVC                   | natural                 |  1                                                                                                                                                                                                                                                              |             |
| C_UART_RX_VVC                   | natural                 |  1                                                                                                                                                                                                                                                              |             |
| C_CLOCK_GEN_VVC                 | natural                 |  1                                                                                                                                                                                                                                                              |             |
| C_DATA_WIDTH                    | natural                 |  8                                                                                                                                                                                                                                                              |             |
| C_ADDR_WIDTH                    | natural                 |  3                                                                                                                                                                                                                                                              |             |
| C_UART_MONITOR_INTERFACE_CONFIG | t_uart_interface_config |  (     bit_time         => GC_BIT_PERIOD,     num_data_bits    => 8,     parity           => PARITY_ODD,     num_stop_bits    => STOP_BITS_ONE     )                                                                                                            |             |
| C_UART_MONITOR_CONFIG           | t_uart_monitor_config   |  (     scope_name               => (1 to 12 => "UART Monitor", others => NUL),     msg_id_panel             => C_UART_MONITOR_MSG_ID_PANEL_DEFAULT,     interface_config         => C_UART_MONITOR_INTERFACE_CONFIG,     transaction_display_time => 0 ns     ) |             |
## Processes
- p_model: _(  )_

## Instantiations
- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_uart: bitvis_uart.uart
- i1_sbi_vvc: bitvis_vip_sbi.sbi_vvc
- i1_uart_vvc: bitvis_vip_uart.uart_vvc
- i1_uart_monitor: bitvis_vip_uart.uart_monitor
- i_clock_generator_vvc: bitvis_vip_clock_generator.clock_generator_vvc
