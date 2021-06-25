# Entity: main_bram
## Diagram
![Diagram](main_bram.svg "Diagram")
## Generics
| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| WIDTH         | natural | 64    |             |
| HEIGHT_BITS   | natural | 1024  |             |
| MEMORY_SIZE   | natural | 65536 |             |
| RAM_INIT_FILE | string  |       |             |
## Ports
| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk       | in        | std_logic                                  |             |
| addr      | in        | std_logic_vector(HEIGHT_BITS - 1 downto 0) |             |
| di        | in        | std_logic_vector(WIDTH-1 downto 0)         |             |
| do        | out       | std_logic_vector(WIDTH-1 downto 0)         |             |
| sel       | in        | std_logic_vector((WIDTH/8)-1 downto 0)     |             |
| re        | in        | std_ulogic                                 |             |
| we        | in        | std_ulogic                                 |             |
## Signals
| Name   | Type                               | Description |
| ------ | ---------------------------------- | ----------- |
| memory | ram_t                              |             |
| obuf   | std_logic_vector(WIDTH-1 downto 0) |             |
## Constants
| Name        | Type    | Value      | Description |
| ----------- | ------- | ---------- | ----------- |
| WIDTH_BYTES | natural |  WIDTH / 8 |             |
## Types
| Name  | Type | Description |
| ----- | ---- | ----------- |
| ram_t |      |             |
## Functions
## Processes
- memory_0: _( clk )_

