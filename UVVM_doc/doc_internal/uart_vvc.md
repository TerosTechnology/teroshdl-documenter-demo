# Entity: uart_vvc
## Diagram
![Diagram](uart_vvc.svg "Diagram")
## Generics
| Generic name                          | Type              | Value                     | Description |
| ------------------------------------- | ----------------- | ------------------------- | ----------- |
| GC_DATA_WIDTH                         | natural           | 8                         |             |
| GC_INSTANCE_IDX                       | natural           | 1                         |             |
| GC_UART_CONFIG                        | t_uart_bfm_config | C_UART_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                | natural           | 1000                      |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD          | natural           | 950                       |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level     | WARNING                   |             |
## Ports
| Port name   | Direction | Type      | Description |
| ----------- | --------- | --------- | ----------- |
| uart_vvc_rx | in        | std_logic |             |
| uart_vvc_tx | inout     | std_logic |             |
## Instantiations
- i1_uart_rx: work.uart_rx_vvc
- i1_uart_tx: work.uart_tx_vvc
