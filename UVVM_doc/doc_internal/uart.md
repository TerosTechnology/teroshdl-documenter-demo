# Entity: uart
## Diagram
![Diagram](uart.svg "Diagram")
## Generics
| Generic name                 | Type      | Value | Description |
| ---------------------------- | --------- | ----- | ----------- |
| GC_START_BIT                 | std_logic | '0'   |             |
| GC_STOP_BIT                  | std_logic | '1'   |             |
| GC_CLOCKS_PER_BIT            | integer   | 16    |             |
| GC_MIN_EQUAL_SAMPLES_PER_BIT | integer   | 15    |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| arst      | in        | std_logic                    |             |
| cs        | in        | std_logic                    |             |
| addr      | in        | unsigned(2 downto 0)         |             |
| wr        | in        | std_logic                    |             |
| rd        | in        | std_logic                    |             |
| wdata     | in        | std_logic_vector(7 downto 0) |             |
| rdata     | out       | std_logic_vector(7 downto 0) |             |
| rx_a      | in        | std_logic                    |             |
| tx        | out       | std_logic                    |             |
## Signals
| Name | Type  | Description |
| ---- | ----- | ----------- |
| p2c  | t_p2c |             |
| c2p  | t_c2p |             |
## Instantiations
- i_uart_pif: work.uart_pif
- i_uart_core: work.uart_core
