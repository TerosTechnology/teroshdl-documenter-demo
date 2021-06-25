# Entity: neorv32_busswitch
## Diagram
![Diagram](neorv32_busswitch.svg "Diagram")
## Generics
| Generic name      | Type    | Value | Description |
| ----------------- | ------- | ----- | ----------- |
| PORT_CA_READ_ONLY | boolean | false |             |
| PORT_CB_READ_ONLY | boolean | false |             |
## Ports
| Port name      | Direction | Type                                       | Description |
| -------------- | --------- | ------------------------------------------ | ----------- |
| clk_i          | in        | std_ulogic                                 |             |
| rstn_i         | in        | std_ulogic                                 |             |
| ca_bus_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| ca_bus_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| ca_bus_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| ca_bus_ben_i   | in        | std_ulogic_vector(03 downto 0)             |             |
| ca_bus_we_i    | in        | std_ulogic                                 |             |
| ca_bus_re_i    | in        | std_ulogic                                 |             |
| ca_bus_lock_i  | in        | std_ulogic                                 |             |
| ca_bus_ack_o   | out       | std_ulogic                                 |             |
| ca_bus_err_o   | out       | std_ulogic                                 |             |
| cb_bus_addr_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cb_bus_rdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cb_bus_wdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cb_bus_ben_i   | in        | std_ulogic_vector(03 downto 0)             |             |
| cb_bus_we_i    | in        | std_ulogic                                 |             |
| cb_bus_re_i    | in        | std_ulogic                                 |             |
| cb_bus_lock_i  | in        | std_ulogic                                 |             |
| cb_bus_ack_o   | out       | std_ulogic                                 |             |
| cb_bus_err_o   | out       | std_ulogic                                 |             |
| p_bus_src_o    | out       | std_ulogic                                 |             |
| p_bus_addr_o   | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| p_bus_rdata_i  | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| p_bus_wdata_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| p_bus_ben_o    | out       | std_ulogic_vector(03 downto 0)             |             |
| p_bus_we_o     | out       | std_ulogic                                 |             |
| p_bus_re_o     | out       | std_ulogic                                 |             |
| p_bus_lock_o   | out       | std_ulogic                                 |             |
| p_bus_ack_i    | in        | std_ulogic                                 |             |
| p_bus_err_i    | in        | std_ulogic                                 |             |
## Signals
| Name             | Type       | Description |
| ---------------- | ---------- | ----------- |
| ca_rd_req_buf    | std_ulogic |             |
|   ca_wr_req_buf  | std_ulogic |             |
| cb_rd_req_buf    | std_ulogic |             |
|   cb_wr_req_buf  | std_ulogic |             |
| ca_req_current   | std_ulogic |             |
|  ca_req_buffered | std_ulogic |             |
| cb_req_current   | std_ulogic |             |
|  cb_req_buffered | std_ulogic |             |
| ca_bus_ack       | std_ulogic |             |
|  cb_bus_ack      | std_ulogic |             |
| ca_bus_err       | std_ulogic |             |
|  cb_bus_err      | std_ulogic |             |
| p_bus_we         | std_ulogic |             |
|    p_bus_re      | std_ulogic |             |
| arbiter          | arbiter_t  |             |
## Types
| Name            | Type                                                 | Description |
| --------------- | ---------------------------------------------------- | ----------- |
| arbiter_state_t | (IDLE, BUSY, RETIRE, BUSY_SWITCHED, RETIRE_SWITCHED) |             |
| arbiter_t       |                                                      |             |
## Processes
- access_buffer: _( rstn_i, clk_i )_

- arbiter_sync: _( rstn_i, clk_i )_

- arbiter_comb: _( arbiter, ca_req_current, cb_req_current, ca_req_buffered, cb_req_buffered,
                        ca_rd_req_buf, ca_wr_req_buf, cb_rd_req_buf, cb_wr_req_buf, p_bus_ack_i, p_bus_err_i )_

