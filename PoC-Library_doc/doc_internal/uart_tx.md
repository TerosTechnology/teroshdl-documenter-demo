# Entity: uart_tx
## Diagram
![Diagram](uart_tx.svg "Diagram")
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| rst       | in        | std_logic                    |             |
| bclk      | in        | std_logic                    |             |
| tx        | out       | std_logic                    |             |
| di        | in        | std_logic_vector(7 downto 0) |             |
| put       | in        | std_logic                    |             |
| ful       | out       | std_logic                    |             |
## Signals
| Name | Type                         | Description |
| ---- | ---------------------------- | ----------- |
| Buf  | std_logic_vector(9 downto 0) |             |
| Cnt  | signed(4 downto 0)           |             |
## Processes
- unnamed: _( clk )_

