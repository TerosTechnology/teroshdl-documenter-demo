# Entity: comm_scramble
## Diagram
![Diagram](comm_scramble.svg "Diagram")
## Generics
| Generic name | Type       | Value | Description |
| ------------ | ---------- | ----- | ----------- |
| GEN          | bit_vector |       |             |
| BITS         | positive   |       |             |
## Ports
| Port name | Direction | Type                                    | Description |
| --------- | --------- | --------------------------------------- | ----------- |
| clk       | in        | std_logic                               |             |
| set       | in        | std_logic                               |             |
| din       | in        | std_logic_vector(GEN'length-2 downto 0) |             |
| step      | in        | std_logic                               |             |
| mask      | out       | std_logic_vector(BITS-1 downto 0)       |             |
## Signals
| Name | Type                       | Description |
| ---- | -------------------------- | ----------- |
| lfsr | std_logic_vector(GN'range) |             |
## Constants
| Name | Type       | Value           | Description |
| ---- | ---------- | --------------- | ----------- |
| GN   | bit_vector |  normalize(GEN) |             |
## Functions
- normalize <font id="function_arguments">(G : bit_vector)</font> <font id="function_return">return bit_vector</font>
## Processes
- unnamed: _( clk )_

