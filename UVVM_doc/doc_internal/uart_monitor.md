# Entity: uart_monitor
## Diagram
![Diagram](uart_monitor.svg "Diagram")
## Generics
| Generic name      | Type                  | Value | Description |
| ----------------- | --------------------- | ----- | ----------- |
| GC_INSTANCE_IDX   | natural               | 1     |             |
| GC_MONITOR_CONFIG | t_uart_monitor_config |       |             |
## Ports
| Port name   | Direction | Type      | Description |
| ----------- | --------- | --------- | ----------- |
| uart_dut_rx | in        | std_logic |             |
| uart_dut_tx | in        | std_logic |             |
## Signals
| Name | Type      | Description |
| ---- | --------- | ----------- |
| tx_i | std_logic |             |
| rx_i | std_logic |             |
## Functions
- monitor_uart_line <font id="function_arguments">(    constant  operation           : in    t_operation;
    constant  C_LOG_PREFIX        : in    string;
    signal    transaction_trigger : inout std_logic;
    variable  transaction_info    : inout t_base_transaction;
    signal    uart_line           : in    std_logic;
    variable  monitor_config      : in    t_uart_monitor_config
  )</font> <font id="function_return">return ()</font>
