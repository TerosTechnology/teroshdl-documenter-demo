# Entity: uart_rx
## Diagram
![Diagram](uart_rx.svg "Diagram")
## Generics
| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| cycles_per_bit | natural | 434   |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| rx        | in        | std_logic                    |             |
| overflow  | out       | std_logic                    |             |
| tready    | in        | std_logic                    |             |
| tvalid    | out       | std_Logic                    |             |
| tdata     | out       | std_logic_vector(7 downto 0) |             |
## Signals
| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| tvalid_int | std_logic |             |
## Processes
- main: _( clk )_

## State machines
![Diagram_state_machine_0]( stm_uart_rx_00.svg "Diagram")