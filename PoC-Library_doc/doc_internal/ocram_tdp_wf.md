# Entity: ocram_tdp_wf
## Diagram
![Diagram](ocram_tdp_wf.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| FILENAME     | string   | ""    |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| ce        | in        | std_logic                           |             |
| we1       | in        | std_logic                           |             |
| we2       | in        | std_logic                           |             |
| a1        | in        | unsigned(A_BITS-1 downto 0)         |             |
| a2        | in        | unsigned(A_BITS-1 downto 0)         |             |
| d1        | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| d2        | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Signals
| Name   | Type                       | Description |
| ------ | -------------------------- | ----------- |
| wd1_r  | std_logic_vector(d1'range) |             |
| wd2_r  | std_logic_vector(d2'range) |             |
| fwd1_r | std_logic                  |             |
| fwd2_r | std_logic                  |             |
| ram_q1 | std_logic_vector(q1'range) |             |
| ram_q2 | std_logic_vector(q2'range) |             |
## Functions
- addr_equal <font id="function_arguments">(a1 : unsigned; a2 : unsigned)</font> <font id="function_return">return X01</font>
## Processes
- unnamed: _( clk )_

## Instantiations
- ram_tdp: work.ocram_tdp
