# Entity: uart_slave
## Diagram
![Diagram](uart_slave.svg "Diagram")
## Generics
| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| uart         | uart_slave_t |       |             |
## Ports
| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| rx        | in        | std_logic |             |
## Signals
| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| baud_rate   | natural   |             |
| local_event | std_logic |             |
## Constants
| Name       | Type    | Value      | Description |
| ---------- | ------- | ---------- | ----------- |
| data_queue | queue_t |  new_queue |             |
## Processes
- main: _(  )_

- recv: _(  )_

