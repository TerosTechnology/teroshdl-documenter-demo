# Entity: reconfig_icap_wrapper
## Diagram
![Diagram](reconfig_icap_wrapper.svg "Diagram")
## Generics
| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| MIN_DEPTH_OUT | positive | 256   |             |
| MIN_DEPTH_IN  | positive | 256   |             |
## Ports
| Port name        | Direction | Type                          | Description |
| ---------------- | --------- | ----------------------------- | ----------- |
| clk              | in        | std_logic                     |             |
| reset            | in        | std_logic                     |             |
| clk_icap         | in        | std_logic                     |             |
| icap_busy        | out       | std_logic                     |             |
| icap_readback    | out       | std_logic                     |             |
| icap_partial_res | out       | std_logic                     |             |
| write_put        | in        | std_logic                     |             |
| write_full       | out       | std_logic                     |             |
| write_data       | in        | std_logic_vector(31 downto 0) |             |
| write_done       | in        | std_logic                     |             |
| read_got         | in        | std_logic                     |             |
| read_valid       | out       | std_logic                     |             |
| read_data        | out       | std_logic_vector(31 downto 0) |             |
## Signals
| Name                 | Type                                     | Description |
| -------------------- | ---------------------------------------- | ----------- |
| reset_icap           | std_logic                                |             |
| write_done_d         | std_logic                                |             |
| write_done_edge      | std_logic                                |             |
| write_done_icapclk   | std_logic                                |             |
| in_data_valid        | std_logic                                |             |
| in_data_fill_state   | std_logic_vector(STATE_BITS -1 downto 0) |             |
| in_data_rden         | std_logic                                |             |
| in_data_start        | std_logic                                |             |
| icap_rden            | std_logic                                |             |
| in_data              | std_logic_vector(31 downto 0)            |             |
| out_data_full        | std_logic                                |             |
| out_data_put         | std_logic                                |             |
| out_data             | std_logic_vector(31 downto 0)            |             |
| icap_data_config     | std_logic_vector(31 downto 0)            |             |
| icap_data_readback   | std_logic_vector(31 downto 0)            |             |
| icap_csb             | std_logic                                |             |
| icap_rw              | std_logic                                |             |
| icap_data_config_r   | std_logic_vector(31 downto 0)            |             |
| icap_data_readback_r | std_logic_vector(31 downto 0)            |             |
| icap_csb_r           | std_logic                                |             |
| icap_rw_r            | std_logic                                |             |
| fsm_status           | std_logic_vector(31 downto 0)            |             |
| fsm_status_clk       | std_logic_vector(31 downto 0)            |             |
| fsm_ready            | std_logic                                |             |
| fsm_ready_d          | std_logic                                |             |
## Constants
| Name              | Type                                     | Value                      | Description |
| ----------------- | ---------------------------------------- | -------------------------- | ----------- |
| STATE_BITS        | positive                                 |  2                         |             |
| state_almost_full | std_logic_vector(STATE_BITS -1 downto 0) |  (0 => '0', others => '1') |             |
## Processes
- in_data_buffer_p: _( clk_icap )_

- icap_reg_p: _( clk_icap )_

## Instantiations
- fifo_in: poc.fifo_ic_got
- fifo_out: poc.fifo_ic_got
- icap_fsm_inst: poc.reconfig_icap_fsm
- icap_inst: poc.xil_ICAP
- strobe_sync: poc.sync_Strobe
- reset_sync: poc.sync_Bits
- fsm_status_sync: poc.sync_vector
