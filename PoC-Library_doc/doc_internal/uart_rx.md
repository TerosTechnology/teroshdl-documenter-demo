# Entity: uart_rx
## Diagram
![Diagram](uart_rx.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| SYNC_DEPTH   | natural | 2     |             |
## Ports
| Port name | Direction | Type                         | Description |
| --------- | --------- | ---------------------------- | ----------- |
| clk       | in        | std_logic                    |             |
| rst       | in        | std_logic                    |             |
| bclk_x8   | in        | std_logic                    |             |
| rx        | in        | std_logic                    |             |
| do        | out       | std_logic_vector(7 downto 0) |             |
| stb       | out       | std_logic                    |             |
## Signals
| Name | Type                         | Description |
| ---- | ---------------------------- | ----------- |
| rxs  | std_logic                    |             |
| Buf  | std_logic_vector(9 downto 0) |             |
| Cnt  | unsigned(4 downto 0)         |             |
| Vld  | std_logic                    |             |
## Processes
- unnamed: _( clk )_

## Instantiations
- sync: PoC.sync_Bits
