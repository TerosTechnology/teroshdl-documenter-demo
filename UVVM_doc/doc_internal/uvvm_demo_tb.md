# Entity: uvvm_demo_tb
## Diagram
![Diagram](uvvm_demo_tb.svg "Diagram")
## Signals
| Name                    | Type            | Description |
| ----------------------- | --------------- | ----------- |
| watchdog_ctrl_terminate | t_watchdog_ctrl |             |
| watchdog_ctrl_init      | t_watchdog_ctrl |             |
| watchdog_ctrl_extend    | t_watchdog_ctrl |             |
| watchdog_ctrl_reinit    | t_watchdog_ctrl |             |
## Constants
| Name                        | Type                 | Value               | Description |
| --------------------------- | -------------------- | ------------------- | ----------- |
| C_SCOPE                     | string               |  C_TB_SCOPE_DEFAULT |             |
| C_MONITOR_SCOPE             | string               |  "UART Monitor"     |             |
| C_CLK_PERIOD                | time                 |  10 ns              |             |
| C_BIT_PERIOD                | time                 |  16 * C_CLK_PERIOD  |             |
| C_ADDR_RX_DATA              | unsigned(2 downto 0) |  "000"              |             |
| C_ADDR_RX_DATA_VALID        | unsigned(2 downto 0) |  "001"              |             |
| C_ADDR_TX_DATA              | unsigned(2 downto 0) |  "010"              |             |
| C_ADDR_TX_READY             | unsigned(2 downto 0) |  "011"              |             |
| C_ACTIVITY_WATCHDOG_TIMEOUT | time                 |  50 * C_BIT_PERIOD  |             |
| C_GENERAL_WATCHDOG_TIMEOUT  | time                 |  1 sec              |             |
## Processes
- p_main: _(  )_

## Instantiations
- i_test_harness: work.uvvm_demo_th
