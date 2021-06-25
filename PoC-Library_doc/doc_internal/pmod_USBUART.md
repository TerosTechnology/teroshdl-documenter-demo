# Entity: pmod_USBUART
## Diagram
![Diagram](pmod_USBUART.svg "Diagram")
## Generics
| Generic name | Type | Value     | Description |
| ------------ | ---- | --------- | ----------- |
| CLOCK_FREQ   | FREQ | 100 MHz   |             |
| BAUDRATE     | BAUD | 115200 Bd |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| Clock     | in        | std_logic                    |             |
| Reset     | in        | std_logic                    |             |
| TX_put    | in        | std_logic                    |             |
| TX_Data   | in        | std_logic_vector(7 downto 0) |             |
| TX_Full   | out       | std_logic                    |             |
| RX_Valid  | out       | std_logic                    |             |
| RX_Data   | out       | std_logic_vector(7 downto 0) |             |
| RX_got    | in        | std_logic                    |             |
| UART_TX   | out       | std_logic                    |             |
| UART_RX   | in        | std_logic                    |             |
| UART_RTS  | out       | std_logic                    |             |
| UART_CTS  | in        | std_logic                    |             |
## Instantiations
- UART: PoC.uart_fifo
