# Entity: reconfig_icap_fsm
## Diagram
![Diagram](reconfig_icap_fsm.svg "Diagram")
## Ports
| Port name      | Direction | Type                          | Description |
| -------------- | --------- | ----------------------------- | ----------- |
| clk            | in        | std_logic                     |             |
| reset          | in        | std_logic                     |             |
| icap_in        | out       | std_logic_vector(31 downto 0) |             |
| icap_out       | in        | std_logic_vector(31 downto 0) |             |
| icap_csb       | out       | std_logic                     |             |
| icap_rw        | out       | std_logic                     |             |
| in_data        | in        | std_logic_vector(31 downto 0) |             |
| in_data_valid  | in        | std_logic                     |             |
| in_data_rden   | out       | std_logic                     |             |
| out_data       | out       | std_logic_vector(31 downto 0) |             |
| out_data_valid | out       | std_logic                     |             |
| out_data_full  | in        | std_logic                     |             |
| status         | out       | std_logic_vector(31 downto 0) |             |
## Signals
| Name              | Type                          | Description |
| ----------------- | ----------------------------- | ----------- |
| cur_state         | t_state                       |             |
| nxt_state         | t_state                       |             |
| sync_state        | t_sync_state                  |             |
| sync_state_flag   | boolean                       |             |
| icap_enable       | boolean                       |             |
| icap_read         | boolean                       |             |
| icap_in_r         | std_logic_vector(31 downto 0) |             |
| in_data_swap      | std_logic_vector(31 downto 0) |             |
| icap_out_swap     | std_logic_vector(31 downto 0) |             |
| icap_error        | std_logic                     |             |
| icap_sync         | std_logic                     |             |
| icap_abort        | std_logic                     |             |
| icap_status_valid | std_logic                     |             |
| readback_cnt      | unsigned(26 downto 0)         |             |
| readback_cnt_en   | boolean                       |             |
| readback_cnt_rst  | boolean                       |             |
| in_data_valid_d   | std_logic                     |             |
| in_data_valid_re  | std_logic                     |             |
| pr_reset          | boolean                       |             |
| status_error      | boolean                       |             |
## Constants
| Name           | Type                          | Value        | Description |
| -------------- | ----------------------------- | ------------ | ----------- |
| sync_s_dummy   | std_logic_vector(31 downto 0) |  x"FFFFFFFF" |             |
| sync_s_bus_p_0 | std_logic_vector(31 downto 0) |  x"000000BB" |             |
| sync_s_bus_p_1 | std_logic_vector(31 downto 0) |  x"11220044" |             |
| sync_s_sync    | std_logic_vector(31 downto 0) |  x"AA995566" |             |
| sync_s_regW    | std_logic_vector(31 downto 0) |  x"30008001" |             |
| sync_s_dsync   | std_logic_vector(31 downto 0) |  x"0000000D" |             |
| cmd_nop        | std_logic_vector(31 downto 0) |  x"20000000" |             |
| cmd_reg_wcfg   | std_logic_vector(4 downto 0)  |  "00001"     |             |
| reg_fdro       | std_logic_vector(4 downto 0)  |  "00011"     |             |
## Types
| Name         | Type                                                                                                                              | Description |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| t_state      | (ready, abort0, abort1, abort2, abort3, write, writing, pre_reg_read0, pre_reg_read1, pre_stream_read0, read, reading, post_read) |             |
| t_sync_state | (none, dummy0, bus_width0, bus_width1, dummy1, synced, cmdWrite, dsynced)                                                         |             |
## Processes
- combi: _( reset, nxt_state, cur_state, in_data, in_data_valid, in_data_valid_re,
						sync_state, sync_state_flag, out_data_full, readback_cnt, pr_reset )_

- readback_cnt_p: _( clk )_

- sync_p: _( clk )_

## State machines
![Diagram_state_machine_0]( stm_reconfig_icap_fsm_00.svg "Diagram")