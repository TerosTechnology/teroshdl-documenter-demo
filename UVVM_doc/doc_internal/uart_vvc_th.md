# Entity: uart_vvc_th
## Diagram
![Diagram](uart_vvc_th.svg "Diagram")
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
| Name         | Type | Value  | Description |
| ------------ | ---- | ------ | ----------- |
| C_CLK_PERIOD | time |  10 ns |             |
## Processes
- p_clk: _(  )_

## Instantiations
- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_uart: bitvis_uart.uart
- i1_sbi_vvc: bitvis_vip_sbi.sbi_vvc
- i1_uart_vvc: bitvis_vip_uart.uart_vvc
