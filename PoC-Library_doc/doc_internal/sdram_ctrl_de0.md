# Entity: sdram_ctrl_de0
## Diagram
![Diagram](sdram_ctrl_de0.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| CLK_PERIOD   | real     |       |             |
| CL           | positive |       |             |
| BL           | positive |       |             |
## Ports
| Port name        | Direction | Type                          | Description |
| ---------------- | --------- | ----------------------------- | ----------- |
| clk              | in        | std_logic                     |             |
| clkout           | in        | std_logic                     |             |
| rst              | in        | std_logic                     |             |
| user_cmd_valid   | in        | std_logic                     |             |
| user_wdata_valid | in        | std_logic                     |             |
| user_write       | in        | std_logic                     |             |
| user_addr        | in        | std_logic_vector(21 downto 0) |             |
| user_wdata       | in        | std_logic_vector(15 downto 0) |             |
| user_got_cmd     | out       | std_logic                     |             |
| user_got_wdata   | out       | std_logic                     |             |
| user_rdata       | out       | std_logic_vector(15 downto 0) |             |
| user_rstb        | out       | std_logic                     |             |
| sd_ck            | out       | std_logic                     |             |
| sd_cke           | out       | std_logic                     |             |
| sd_cs            | out       | std_logic                     |             |
| sd_ras           | out       | std_logic                     |             |
| sd_cas           | out       | std_logic                     |             |
| sd_we            | out       | std_logic                     |             |
| sd_ba            | out       | std_logic_vector(1 downto 0)  |             |
| sd_a             | out       | std_logic_vector(11 downto 0) |             |
| sd_dq            | inout     | std_logic_vector(15 downto 0) |             |
## Signals
| Name       | Type                          | Description |
| ---------- | ----------------------------- | ----------- |
| sd_cke_nxt | std_logic                     |             |
| sd_cs_nxt  | std_logic                     |             |
| sd_ras_nxt | std_logic                     |             |
| sd_cas_nxt | std_logic                     |             |
| sd_we_nxt  | std_logic                     |             |
| sd_a_nxt   | std_logic_vector(11 downto 0) |             |
| sd_ba_nxt  | std_logic_vector(1 downto 0)  |             |
| rden_nxt   | std_logic                     |             |
| wren_nxt   | std_logic                     |             |
## Constants
| Name      | Type     | Value                                                                                                         | Description |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------- | ----------- |
| A_BITS    | positive |  22                                                                                                           |             |
| D_BITS    | positive |  16                                                                                                           |             |
| R_BITS    | positive |  12                                                                                                           |             |
| C_BITS    | positive |   8                                                                                                           |             |
| B_BITS    | positive |   2                                                                                                           |             |
| T_MRD     | integer  |  2                                                                                                            |             |
| T_RAS     | integer  |  integer(ceil(42.0/CLK_PERIOD))                                                                               |             |
| T_RCD     | integer  |  integer(ceil(18.0/CLK_PERIOD))                                                                               |             |
| T_RFC     | integer  |  integer(ceil(60.0/CLK_PERIOD))                                                                               |             |
| T_RP      | integer  |  integer(ceil(18.0/CLK_PERIOD))                                                                               |             |
| T_WR      | integer  |  2                                                                                                            |             |
| T_WTR     | integer  |  1                                                                                                            |             |
| T_REFI    | integer  |  integer(ceil(15625.0/  -- 64 ms / 4096 rows                                                CLK_PERIOD))-50   |             |
| INIT_WAIT | integer  |  integer(ceil(100000.0/  -- 100 us                                                (real(T_REFI)*CLK_PERIOD))) |             |
## Instantiations
- fsm: poc.sdram_ctrl_fsm
- phy: poc.sdram_ctrl_phy_de0
