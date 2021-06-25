# Entity: sdram_ctrl_phy_de0
## Diagram
![Diagram](sdram_ctrl_phy_de0.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| CL           | positive |       |             |
## Ports
| Port name  | Direction | Type                          | Description |
| ---------- | --------- | ----------------------------- | ----------- |
| clk        | in        | std_logic                     |             |
| clkout     | in        | std_logic                     |             |
| rst        | in        | std_logic                     |             |
| sd_cke_nxt | in        | std_logic                     |             |
| sd_cs_nxt  | in        | std_logic                     |             |
| sd_ras_nxt | in        | std_logic                     |             |
| sd_cas_nxt | in        | std_logic                     |             |
| sd_we_nxt  | in        | std_logic                     |             |
| sd_ba_nxt  | in        | std_logic_vector(1 downto 0)  |             |
| sd_a_nxt   | in        | std_logic_vector(11 downto 0) |             |
| wren_nxt   | in        | std_logic                     |             |
| wdata_nxt  | in        | std_logic_vector(15 downto 0) |             |
| rden_nxt   | in        | std_logic                     |             |
| rdata      | out       | std_logic_vector(15 downto 0) |             |
| rstb       | out       | std_logic                     |             |
| sd_ck      | out       | std_logic                     |             |
| sd_cke     | out       | std_logic                     |             |
| sd_cs      | out       | std_logic                     |             |
| sd_ras     | out       | std_logic                     |             |
| sd_cas     | out       | std_logic                     |             |
| sd_we      | out       | std_logic                     |             |
| sd_ba      | out       | std_logic_vector(1 downto 0)  |             |
| sd_a       | out       | std_logic_vector(11 downto 0) |             |
| sd_dq      | inout     | std_logic_vector(15 downto 0) |             |
## Signals
| Name     | Type                          | Description |
| -------- | ----------------------------- | ----------- |
| sd_cke_r | std_logic                     |             |
| sd_cs_r  | std_logic                     |             |
| sd_ras_r | std_logic                     |             |
| sd_cas_r | std_logic                     |             |
| sd_we_r  | std_logic                     |             |
| sd_ba_r  | std_logic_vector(1 downto 0)  |             |
| sd_a_r   | std_logic_vector(11 downto 0) |             |
| dq_en_r  | std_logic_vector(15 downto 0) |             |
| dq_o_r   | std_logic_vector(15 downto 0) |             |
| dq_i     | std_logic_vector(15 downto 0) |             |
| rden_r   | std_logic_vector(CL downto 0) |             |
| rstb_r   | std_logic                     |             |
| rdata_r  | std_logic_vector(15 downto 0) |             |
## Processes
- unnamed: _( clk )_

- unnamed: _( clk )_

- unnamed: _( clk )_

## Instantiations
- sd_ck_obuf: altiobuf_out
- dq_obuf: altiobuf_out
- dq_ibuf: altiobuf_in
