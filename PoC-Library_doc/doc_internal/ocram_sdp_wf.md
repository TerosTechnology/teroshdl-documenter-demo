# Entity: ocram_sdp_wf
## Diagram
![Diagram](ocram_sdp_wf.svg "Diagram")
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
| we        | in        | std_logic                           |             |
| ra        | in        | unsigned(A_BITS-1 downto 0)         |             |
| wa        | in        | unsigned(A_BITS-1 downto 0)         |             |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Signals
| Name  | Type                      | Description |
| ----- | ------------------------- | ----------- |
| wd_r  | std_logic_vector(d'range) |             |
| fwd_r | std_logic                 |             |
| ram_q | std_logic_vector(q'range) |             |
## Functions
- addr_equal <font id="function_arguments">(a1 : unsigned; a2 : unsigned)</font> <font id="function_return">return X01</font>
## Processes
- unnamed: _( clk )_

## Instantiations
- ram_sdp: work.ocram_sdp
