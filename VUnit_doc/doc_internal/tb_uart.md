# Entity: tb_uart
## Diagram
![Diagram](tb_uart.svg "Diagram")
## Generics
| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals
| Name | Type      | Description |
| ---- | --------- | ----------- |
| chan | std_logic |             |
## Constants
| Name          | Type            | Value                             | Description |
| ------------- | --------------- | --------------------------------- | ----------- |
| master_uart   | uart_master_t   |  new_uart_master                  |             |
| master_stream | stream_master_t |  as_stream(master_uart)           |             |
| slave_uart    | uart_slave_t    |  new_uart_slave(data_length => 8) |             |
| slave_stream  | stream_slave_t  |  as_stream(slave_uart)            |             |
## Processes
- main: _(  )_

## Instantiations
- uart_master_inst: work.uart_master
- uart_slave_inst: work.uart_slave
