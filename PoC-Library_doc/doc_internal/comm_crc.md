# Entity: comm_crc
## Diagram
![Diagram](comm_crc.svg "Diagram")
## Generics
| Generic name | Type             | Value | Description |
| ------------ | ---------------- | ----- | ----------- |
| GEN          | bit_vector       |       |             |
| BITS         | positive         |       |             |
| STARTUP_RMD  | std_logic_vector | "0"   |             |
| OUTPUT_REGS  | boolean          | true  |             |
## Ports
| Port name | Direction | Type                                                      | Description |
| --------- | --------- | --------------------------------------------------------- | ----------- |
| clk       | in        | std_logic                                                 |             |
| set       | in        | std_logic                                                 |             |
| init      | in        | std_logic_vector(abs(mssb_idx(GEN)-GEN'right)-1 downto 0) |             |
| step      | in        | std_logic                                                 |             |
| din       | in        | std_logic_vector(BITS-1 downto 0)                         |             |
| rmd       | out       | std_logic_vector(abs(mssb_idx(GEN)-GEN'right)-1 downto 0) |             |
| zero      | out       | std_logic                                                 |             |
## Signals
| Name | Type                       | Description |
| ---- | -------------------------- | ----------- |
| lfsr | std_logic_vector(GN'range) |             |
| lfsn | std_logic_vector(GN'range) |             |
| lfso | std_logic_vector(GN'range) |             |
## Constants
| Name | Type             | Value                              | Description |
| ---- | ---------------- | ---------------------------------- | ----------- |
| GN   | std_logic_vector |  to_stdlogicvector(normalize(GEN)) |             |
## Functions
- normalize <font id="function_arguments">(G : bit_vector)</font> <font id="function_return">return bit_vector</font>
## Processes
- unnamed: _( lfsr, din )_

- unnamed: _( clk )_

