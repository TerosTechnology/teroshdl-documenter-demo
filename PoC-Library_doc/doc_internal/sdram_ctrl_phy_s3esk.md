# Entity: sdram_ctrl_phy_s3esk
## Diagram
![Diagram](sdram_ctrl_phy_s3esk.svg "Diagram")
## Ports
| Port name  | Direction | Type                          | Description |
| ---------- | --------- | ----------------------------- | ----------- |
| clk        | in        | std_logic                     |             |
| clk_n      | in        | std_logic                     |             |
| clk90      | in        | std_logic                     |             |
| clk90_n    | in        | std_logic                     |             |
| rst        | in        | std_logic                     |             |
| rst90      | in        | std_logic                     |             |
| rst180     | in        | std_logic                     |             |
| rst270     | in        | std_logic                     |             |
| clk_fb90   | in        | std_logic                     |             |
| clk_fb90_n | in        | std_logic                     |             |
| rst_fb90   | in        | std_logic                     |             |
| rst_fb270  | in        | std_logic                     |             |
| sd_cke_nxt | in        | std_logic                     |             |
| sd_cs_nxt  | in        | std_logic                     |             |
| sd_ras_nxt | in        | std_logic                     |             |
| sd_cas_nxt | in        | std_logic                     |             |
| sd_we_nxt  | in        | std_logic                     |             |
| sd_ba_nxt  | in        | std_logic_vector(1 downto 0)  |             |
| sd_a_nxt   | in        | std_logic_vector(12 downto 0) |             |
| wren_nxt   | in        | std_logic                     |             |
| wdata_nxt  | in        | std_logic_vector(31 downto 0) |             |
| rden_nxt   | in        | std_logic                     |             |
| rdata      | out       | std_logic_vector(31 downto 0) |             |
| rstb       | out       | std_logic                     |             |
| sd_ck_p    | out       | std_logic                     |             |
| sd_ck_n    | out       | std_logic                     |             |
| sd_cke     | out       | std_logic                     |             |
| sd_cs      | out       | std_logic                     |             |
| sd_ras     | out       | std_logic                     |             |
| sd_cas     | out       | std_logic                     |             |
| sd_we      | out       | std_logic                     |             |
| sd_ba      | out       | std_logic_vector(1 downto 0)  |             |
| sd_a       | out       | std_logic_vector(12 downto 0) |             |
| sd_ldqs    | out       | std_logic                     |             |
| sd_udqs    | out       | std_logic                     |             |
| sd_dq      | inout     | std_logic_vector(15 downto 0) |             |
## Signals
| Name          | Type                          | Description |
| ------------- | ----------------------------- | ----------- |
| sd_cke_r      | std_logic                     |             |
| sd_cs_r       | std_logic                     |             |
| sd_ras_r      | std_logic                     |             |
| sd_cas_r      | std_logic                     |             |
| sd_we_r       | std_logic                     |             |
| sd_ba_r       | std_logic_vector(1 downto 0)  |             |
| sd_a_r        | std_logic_vector(12 downto 0) |             |
| wren_r_n      | std_logic                     |             |
| dqs_en0_nxt_n | std_logic                     |             |
| dqs_en0_r_n   | std_logic_vector(1 downto 0)  |             |
| dqs_en1_r_n   | std_logic_vector(1 downto 0)  |             |
| dqs_o_r       | std_logic_vector(1 downto 0)  |             |
| dq_en0_n      | std_logic                     |             |
| dq_en1_r_n    | std_logic_vector(15 downto 0) |             |
| dq_o_r        | std_logic_vector(15 downto 0) |             |
| dq_i          | std_logic_vector(15 downto 0) |             |
| wdata_r       | std_logic_vector(31 downto 0) |             |
| wdata_fal_r   | std_logic_vector(15 downto 0) |             |
| rden_r        | std_logic                     |             |
| rden1_r       | std_logic                     |             |
| rden2_r       | std_logic                     |             |
| rden3_r       | std_logic                     |             |
| rstb_r        | std_logic                     |             |
| rdata_ris_r   | std_logic_vector(15 downto 0) |             |
| rdata_r       | std_logic_vector(31 downto 0) |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( clk_n )_

- unnamed: _( clk )_

- unnamed: _( clk_fb90_n )_

- unnamed: _( clk_fb90_n )_

- unnamed: _( clk_fb90_n )_

## Instantiations
- sd_ck_p_off: ODDR2
- sd_ck_n_off: ODDR2
- ldqs_obuf: OBUFT
- udqs_obuf: OBUFT
