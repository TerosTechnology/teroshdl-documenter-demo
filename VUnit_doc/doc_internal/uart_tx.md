# Entity: uart_tx
## Diagram
![Diagram](uart_tx.svg "Diagram")
## Generics
| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| cycles_per_bit | natural | 434   |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| tx        | out       | std_logic                    |             |
| tready    | out       | std_logic                    |             |
| tvalid    | in        | std_Logic                    |             |
| tdata     | in        | std_logic_vector(7 downto 0) |             |
## Signals
| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| tready_int | std_logic |             |
## Processes
- main: _( clk )_

## State machines
![Diagram_state_machine_0]( stm_uart_tx_00.svg "Diagram")