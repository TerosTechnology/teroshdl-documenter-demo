# Entity: fifo_ic_assembly
## Diagram
![Diagram](fifo_ic_assembly.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| D_BITS       | positive |       |             |
| A_BITS       | positive |       |             |
| G_BITS       | positive |       |             |
## Ports
| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk_wr    | in        | std_logic                           |             |
| rst_wr    | in        | std_logic                           |             |
| base      | out       | std_logic_vector(A_BITS-1 downto 0) |             |
| failed    | out       | std_logic                           |             |
| addr      | in        | std_logic_vector(A_BITS-1 downto 0) |             |
| din       | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| put       | in        | std_logic                           |             |
| clk_rd    | in        | std_logic                           |             |
| rst_rd    | in        | std_logic                           |             |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0) |             |
| vld       | out       | std_logic                           |             |
| got       | in        | std_logic                           |             |
## Signals
| Name   | Type                                | Description |
| ------ | ----------------------------------- | ----------- |
| wa     | unsigned(AN-1 downto 0)             |             |
| we     | std_logic                           |             |
| di     | std_logic_vector(DN-1 downto 0)     |             |
| ra     | unsigned(AN-1 downto 0)             |             |
| do     | std_logic_vector(DN-1 downto 0)     |             |
| OPgray | std_logic_vector(A_BITS-1 downto 0) |             |
## Constants
| Name | Type     | Value            | Description |
| ---- | -------- | ---------------- | ----------- |
| AN   | positive |  A_BITS - G_BITS |             |
| DN   | positive |  G_BITS + D_BITS |             |
## Instantiations
- ram: ocram_sdp
