# Entity: neorv32_wishbone
## Diagram
![Diagram](neorv32_wishbone.svg "Diagram")
## Generics
| Generic name      | Type    | Value  | Description |
| ----------------- | ------- | ------ | ----------- |
| MEM_INT_IMEM_EN   | boolean | true   |             |
| MEM_INT_IMEM_SIZE | natural | 8*1024 |             |
| MEM_INT_DMEM_EN   | boolean | true   |             |
| MEM_INT_DMEM_SIZE | natural | 4*1024 |             |
| BUS_TIMEOUT       | natural | 63     |             |
## Ports
| Port name | Direction | Type                           | Description |
| --------- | --------- | ------------------------------ | ----------- |
| clk_i     | in        | std_ulogic                     |             |
| rstn_i    | in        | std_ulogic                     |             |
| src_i     | in        | std_ulogic                     |             |
| addr_i    | in        | std_ulogic_vector(31 downto 0) |             |
| rden_i    | in        | std_ulogic                     |             |
| wren_i    | in        | std_ulogic                     |             |
| ben_i     | in        | std_ulogic_vector(03 downto 0) |             |
| data_i    | in        | std_ulogic_vector(31 downto 0) |             |
| data_o    | out       | std_ulogic_vector(31 downto 0) |             |
| lock_i    | in        | std_ulogic                     |             |
| ack_o     | out       | std_ulogic                     |             |
| err_o     | out       | std_ulogic                     |             |
| priv_i    | in        | std_ulogic_vector(01 downto 0) |             |
| wb_tag_o  | out       | std_ulogic_vector(02 downto 0) |             |
| wb_adr_o  | out       | std_ulogic_vector(31 downto 0) |             |
| wb_dat_i  | in        | std_ulogic_vector(31 downto 0) |             |
| wb_dat_o  | out       | std_ulogic_vector(31 downto 0) |             |
| wb_we_o   | out       | std_ulogic                     |             |
| wb_sel_o  | out       | std_ulogic_vector(03 downto 0) |             |
| wb_stb_o  | out       | std_ulogic                     |             |
| wb_cyc_o  | out       | std_ulogic                     |             |
| wb_lock_o | out       | std_ulogic                     |             |
| wb_ack_i  | in        | std_ulogic                     |             |
| wb_err_i  | in        | std_ulogic                     |             |
## Signals
| Name         | Type                           | Description |
| ------------ | ------------------------------ | ----------- |
| int_imem_acc | std_ulogic                     |             |
| int_dmem_acc | std_ulogic                     |             |
| int_boot_acc | std_ulogic                     |             |
| xbus_access  | std_ulogic                     |             |
| ctrl         | ctrl_t                         |             |
| stb_int      | std_ulogic                     |             |
| cyc_int      | std_ulogic                     |             |
| rdata        | std_ulogic_vector(31 downto 0) |             |
| ack_gated    | std_ulogic                     |             |
| rdata_gated  | std_ulogic_vector(31 downto 0) |             |
## Constants
| Name         | Type    | Value                      | Description |
| ------------ | ------- | -------------------------- | ----------- |
| timeout_en_c | boolean |  boolean(BUS_TIMEOUT /= 0) |             |
## Types
| Name         | Type         | Description |
| ------------ | ------------ | ----------- |
| ctrl_state_t | (IDLE, BUSY) |             |
| ctrl_t       |              |             |
## Processes
- bus_arbiter: _( rstn_i, clk_i )_

