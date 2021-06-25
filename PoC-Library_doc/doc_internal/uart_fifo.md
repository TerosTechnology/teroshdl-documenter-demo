# Entity: uart_fifo
## Diagram
![Diagram](uart_fifo.svg "Diagram")
## Generics
| Generic name            | Type                         | Value                 | Description |
| ----------------------- | ---------------------------- | --------------------- | ----------- |
| CLOCK_FREQ              | FREQ                         |                       |             |
| BAUDRATE                | BAUD                         |                       |             |
| ADD_INPUT_SYNCHRONIZERS | boolean                      | TRUE                  |             |
| TX_MIN_DEPTH            | positive                     | 16                    |             |
| TX_ESTATE_BITS          | natural                      | 0                     |             |
| RX_MIN_DEPTH            | positive                     | 16                    |             |
| RX_FSTATE_BITS          | natural                      | 0                     |             |
| FLOWCONTROL             | T_IO_UART_FLOWCONTROL_KIND   | UART_FLOWCONTROL_NONE |             |
| SWFC_XON_CHAR           | std_logic_vector(7 downto 0) | x"11"                 |             |
| SWFC_XON_TRIGGER        | real                         | 0.0625                |             |
| SWFC_XOFF_CHAR          | std_logic_vector(7 downto 0) | x"13"                 |             |
| SWFC_XOFF_TRIGGER       | real                         | 0.75                  |             |
## Ports
| Port name     | Direction | Type                                                 | Description |
| ------------- | --------- | ---------------------------------------------------- | ----------- |
| Clock         | in        | std_logic                                            |             |
| Reset         | in        | std_logic                                            |             |
| TX_put        | in        | std_logic                                            |             |
| TX_Data       | in        | std_logic_vector(7 downto 0)                         |             |
| TX_Full       | out       | std_logic                                            |             |
| TX_EmptyState | out       | std_logic_vector(imax(0, TX_ESTATE_BITS-1) downto 0) |             |
| RX_Valid      | out       | std_logic                                            |             |
| RX_Data       | out       | std_logic_vector(7 downto 0)                         |             |
| RX_got        | in        | std_logic                                            |             |
| RX_FullState  | out       | std_logic_vector(imax(0, RX_FSTATE_BITS-1) downto 0) |             |
| RX_Overflow   | out       | std_logic                                            |             |
| UART_TX       | out       | std_logic                                            |             |
| UART_RX       | in        | std_logic                                            |             |
| UART_RTS      | out       | std_logic                                            |             |
| UART_CTS      | in        | std_logic                                            |             |
## Signals
| Name          | Type      | Description |
| ------------- | --------- | ----------- |
| FC_TX_Strobe  | std_logic |             |
| FC_TX_Data    | T_SLV_8   |             |
| FC_TX_got     | std_logic |             |
| FC_RX_put     | std_logic |             |
| FC_RX_Data    | T_SLV_8   |             |
| TXFIFO_Valid  | std_logic |             |
| TXFIFO_Data   | T_SLV_8   |             |
| RXFIFO_Full   | std_logic |             |
| TXUART_Full   | std_logic |             |
| RXUART_Strobe | std_logic |             |
| RXUART_Data   | T_SLV_8   |             |
| BitClock      | std_logic |             |
| BitClock_x8   | std_logic |             |
| UART_RX_sync  | std_logic |             |
## Instantiations
- TXFIFO: PoC.fifo_cc_got
- RXFIFO: PoC.fifo_cc_got
- bclk: PoC.uart_bclk
- TX: PoC.uart_tx
- RX: PoC.uart_rx
