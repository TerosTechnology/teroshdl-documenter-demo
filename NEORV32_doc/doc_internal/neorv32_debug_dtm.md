# Entity: neorv32_debug_dtm
## Diagram
![Diagram](neorv32_debug_dtm.svg "Diagram")
## Generics
| Generic name   | Type                           | Value         | Description |
| -------------- | ------------------------------ | ------------- | ----------- |
| IDCODE_VERSION | std_ulogic_vector(03 downto 0) | x"0"          |             |
| IDCODE_PARTID  | std_ulogic_vector(15 downto 0) | x"cafe"       |             |
| IDCODE_MANID   | std_ulogic_vector(10 downto 0) | "00000000000" |             |
## Ports
| Port name        | Direction | Type                           | Description |
| ---------------- | --------- | ------------------------------ | ----------- |
| clk_i            | in        | std_ulogic                     |             |
| rstn_i           | in        | std_ulogic                     |             |
| jtag_trst_i      | in        | std_ulogic                     |             |
| jtag_tck_i       | in        | std_ulogic                     |             |
| jtag_tdi_i       | in        | std_ulogic                     |             |
| jtag_tdo_o       | out       | std_ulogic                     |             |
| jtag_tms_i       | in        | std_ulogic                     |             |
| dmi_rstn_o       | out       | std_ulogic                     |             |
| dmi_req_valid_o  | out       | std_ulogic                     |             |
| dmi_req_ready_i  | in        | std_ulogic                     |             |
| dmi_req_addr_o   | out       | std_ulogic_vector(06 downto 0) |             |
| dmi_req_op_o     | out       | std_ulogic                     |             |
| dmi_req_data_o   | out       | std_ulogic_vector(31 downto 0) |             |
| dmi_resp_valid_i | in        | std_ulogic                     |             |
| dmi_resp_ready_o | out       | std_ulogic                     |             |
| dmi_resp_data_i  | in        | std_ulogic_vector(31 downto 0) |             |
| dmi_resp_err_i   | in        | std_ulogic                     |             |
## Signals
| Name     | Type       | Description |
| -------- | ---------- | ----------- |
| tap_ctrl | tap_ctrl_t |             |
| tap_reg  | tap_reg_t  |             |
| dmi_ctrl | dmi_ctrl_t |             |
## Constants
| Name          | Type                           | Value     | Description |
| ------------- | ------------------------------ | --------- | ----------- |
| dmi_idle_c    | std_ulogic_vector(02 downto 0) |  "010"    |             |
| dmi_version_c | std_ulogic_vector(03 downto 0) |  "0001"   |             |
| dmi_abits_c   | std_ulogic_vector(05 downto 0) |  "000111" |             |
## Types
| Name             | Type                                                                                                                                                                                                   | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| tap_ctrl_state_t | (LOGIC_RESET, DR_SCAN, DR_CAPTURE, DR_SHIFT, DR_EXIT1, DR_PAUSE, DR_EXIT2, DR_UPDATE,                                RUN_IDLE, IR_SCAN, IR_CAPTURE, IR_SHIFT, IR_EXIT1, IR_PAUSE, IR_EXIT2, IR_UPDATE) |             |
| tap_ctrl_t       |                                                                                                                                                                                                        |             |
| tap_reg_t        |                                                                                                                                                                                                        |             |
| dmi_ctrl_state_t | (DMI_IDLE, DMI_READ_WAIT, DMI_READ, DMI_READ_BUSY,                             DMI_WRITE_WAIT, DMI_WRITE, DMI_WRITE_BUSY)                                                                              |             |
| dmi_ctrl_t       |                                                                                                                                                                                                        |             |
## Processes
- tap_control: _( rstn_i, clk_i )_

- reg_access: _( clk_i )_

- dmi_controller: _( rstn_i, clk_i )_

