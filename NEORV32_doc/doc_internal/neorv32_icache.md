# Entity: neorv32_icache
## Diagram
![Diagram](neorv32_icache.svg "Diagram")
## Generics
| Generic name      | Type    | Value | Description |
| ----------------- | ------- | ----- | ----------- |
| ICACHE_NUM_BLOCKS | natural | 4     |             |
| ICACHE_BLOCK_SIZE | natural | 16    |             |
| ICACHE_NUM_SETS   | natural | 1     |             |
## Ports
| Port name    | Direction | Type                                       | Description |
| ------------ | --------- | ------------------------------------------ | ----------- |
| clk_i        | in        | std_ulogic                                 |             |
| rstn_i       | in        | std_ulogic                                 |             |
| clear_i      | in        | std_ulogic                                 |             |
| host_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| host_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| host_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| host_ben_i   | in        | std_ulogic_vector(03 downto 0)             |             |
| host_we_i    | in        | std_ulogic                                 |             |
| host_re_i    | in        | std_ulogic                                 |             |
| host_ack_o   | out       | std_ulogic                                 |             |
| host_err_o   | out       | std_ulogic                                 |             |
| bus_addr_o   | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| bus_rdata_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| bus_wdata_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| bus_ben_o    | out       | std_ulogic_vector(03 downto 0)             |             |
| bus_we_o     | out       | std_ulogic                                 |             |
| bus_re_o     | out       | std_ulogic                                 |             |
| bus_ack_i    | in        | std_ulogic                                 |             |
| bus_err_i    | in        | std_ulogic                                 |             |
## Signals
| Name  | Type       | Description |
| ----- | ---------- | ----------- |
| cache | cache_if_t |             |
| ctrl  | ctrl_t     |             |
## Constants
| Name                | Type    | Value                                                | Description |
| ------------------- | ------- | ---------------------------------------------------- | ----------- |
| cache_offset_size_c | natural |  index_size_f(ICACHE_BLOCK_SIZE/4)                   |             |
| cache_index_size_c  | natural |  index_size_f(ICACHE_NUM_BLOCKS)                     |             |
| cache_tag_size_c    | natural |  32 - (cache_offset_size_c + cache_index_size_c + 2) |             |
## Types
| Name                | Type                                                                                                                                                                         | Description |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| cache_if_t          |                                                                                                                                                                              |             |
| ctrl_engine_state_t | (S_IDLE, S_CACHE_CLEAR, S_CACHE_CHECK, S_CACHE_MISS, S_BUS_DOWNLOAD_REQ, S_BUS_DOWNLOAD_GET,                                S_CACHE_RESYNC_0, S_CACHE_RESYNC_1, S_BUS_ERROR) |             |
| ctrl_t              |                                                                                                                                                                              |             |
## Processes
- ctrl_engine_fsm_sync_rst: _( rstn_i, clk_i )_

- ctrl_engine_fsm_sync: _( clk_i )_

- ctrl_engine_fsm_comb: _( ctrl, cache, clear_i, host_addr_i, host_re_i, bus_rdata_i, bus_ack_i, bus_err_i )_

## Instantiations
- neorv32_icache_memory_inst: neorv32_icache_memory
