# Entity: sb_uart_sbi_demo_tb
## Diagram
![Diagram](sb_uart_sbi_demo_tb.svg "Diagram")
## Signals
| Name           | Type                                                                                                                                                          | Description |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| clk            | std_logic                                                                                                                                                     |             |
| clk_ena        | boolean                                                                                                                                                       |             |
| arst           | std_logic                                                                                                                                                     |             |
| sbi_if         | t_sbi_if(addr(C_ADDR_WIDTH-1 downto 0),                            wdata(C_DATA_WIDTH-1 downto 0),                            rdata(C_DATA_WIDTH-1 downto 0)) |             |
| terminate_loop | std_logic                                                                                                                                                     |             |
| uart_rx        | std_logic                                                                                                                                                     |             |
| uart_tx        | std_logic                                                                                                                                                     |             |
## Constants
| Name         | Type    | Value  | Description |
| ------------ | ------- | ------ | ----------- |
| C_SCOPE      | string  |  "TB"  |             |
| C_ADDR_WIDTH | integer |  3     |             |
| C_DATA_WIDTH | integer |  8     |             |
| C_CLK_PERIOD | time    |  10 ns |             |
## Processes
- p_sequencer: _(  )_

## Instantiations
- i_uart: bitvis_uart.uart
