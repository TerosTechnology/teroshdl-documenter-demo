# Entity: uart_vvc_demo_tb
## Diagram
![Diagram](uart_vvc_demo_tb.svg "Diagram")
## Constants
| Name                  | Type                 | Value               | Description |
| --------------------- | -------------------- | ------------------- | ----------- |
| C_SCOPE               | string               |  C_TB_SCOPE_DEFAULT |             |
| C_CLK_PERIOD          | time                 |  10 ns              |             |
| C_BIT_PERIOD          | time                 |  16 * C_CLK_PERIOD  |             |
| C_TIME_OF_ONE_UART_TX | time                 |  11*C_BIT_PERIOD    |             |
| C_ADDR_RX_DATA        | unsigned(2 downto 0) |  "000"              |             |
| C_ADDR_RX_DATA_VALID  | unsigned(2 downto 0) |  "001"              |             |
| C_ADDR_TX_DATA        | unsigned(2 downto 0) |  "010"              |             |
| C_ADDR_TX_READY       | unsigned(2 downto 0) |  "011"              |             |
## Processes
- p_main: _(  )_

## Instantiations
- i_test_harness: work.uart_vvc_demo_th
