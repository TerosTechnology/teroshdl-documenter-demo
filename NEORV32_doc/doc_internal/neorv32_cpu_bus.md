# Entity: neorv32_cpu_bus
## Diagram
![Diagram](neorv32_cpu_bus.svg "Diagram")
## Generics
| Generic name          | Type    | Value   | Description |
| --------------------- | ------- | ------- | ----------- |
| CPU_EXTENSION_RISCV_A | boolean | false   |             |
| CPU_EXTENSION_RISCV_C | boolean | true    |             |
| PMP_NUM_REGIONS       | natural | 0       |             |
| PMP_MIN_GRANULARITY   | natural | 64*1024 |             |
## Ports
| Port name     | Direction | Type                                       | Description |
| ------------- | --------- | ------------------------------------------ | ----------- |
| clk_i         | in        | std_ulogic                                 |             |
| rstn_i        | in        | std_ulogic                                 |             |
| ctrl_i        | in        | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| fetch_pc_i    | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| instr_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| i_wait_o      | out       | std_ulogic                                 |             |
| ma_instr_o    | out       | std_ulogic                                 |             |
| be_instr_o    | out       | std_ulogic                                 |             |
| addr_i        | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| wdata_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rdata_o       | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| mar_o         | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_wait_o      | out       | std_ulogic                                 |             |
| excl_state_o  | out       | std_ulogic                                 |             |
| ma_load_o     | out       | std_ulogic                                 |             |
| ma_store_o    | out       | std_ulogic                                 |             |
| be_load_o     | out       | std_ulogic                                 |             |
| be_store_o    | out       | std_ulogic                                 |             |
| pmp_addr_i    | in        | pmp_addr_if_t                              |             |
| pmp_ctrl_i    | in        | pmp_ctrl_if_t                              |             |
| i_bus_addr_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| i_bus_rdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| i_bus_wdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| i_bus_ben_o   | out       | std_ulogic_vector(03 downto 0)             |             |
| i_bus_we_o    | out       | std_ulogic                                 |             |
| i_bus_re_o    | out       | std_ulogic                                 |             |
| i_bus_lock_o  | out       | std_ulogic                                 |             |
| i_bus_ack_i   | in        | std_ulogic                                 |             |
| i_bus_err_i   | in        | std_ulogic                                 |             |
| i_bus_fence_o | out       | std_ulogic                                 |             |
| d_bus_addr_o  | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_rdata_i | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_wdata_o | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_ben_o   | out       | std_ulogic_vector(03 downto 0)             |             |
| d_bus_we_o    | out       | std_ulogic                                 |             |
| d_bus_re_o    | out       | std_ulogic                                 |             |
| d_bus_lock_o  | out       | std_ulogic                                 |             |
| d_bus_ack_i   | in        | std_ulogic                                 |             |
| d_bus_err_i   | in        | std_ulogic                                 |             |
| d_bus_fence_o | out       | std_ulogic                                 |             |
## Signals
| Name                  | Type                                       | Description |
| --------------------- | ------------------------------------------ | ----------- |
| mar                   | std_ulogic_vector(data_width_c-1 downto 0) |             |
|  mdo                  | std_ulogic_vector(data_width_c-1 downto 0) |             |
|  mdi                  | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_wdata           | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_rdata           | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rdata_align           | std_ulogic_vector(data_width_c-1 downto 0) |             |
| d_bus_ben             | std_ulogic_vector(3 downto 0)              |             |
| d_misaligned          | std_ulogic                                 |             |
|  i_misaligned         | std_ulogic                                 |             |
| i_arbiter             | bus_arbiter_t                              |             |
|  d_arbiter            | bus_arbiter_t                              |             |
| exclusive_lock        | std_ulogic                                 |             |
| exclusive_lock_status | std_ulogic_vector(data_width_c-1 downto 0) |             |
| pmp                   | pmp_t                                      |             |
| d_bus_we              | std_ulogic                                 |             |
|  d_bus_we_buf         | std_ulogic                                 |             |
| d_bus_re              | std_ulogic                                 |             |
|  d_bus_re_buf         | std_ulogic                                 |             |
| i_bus_re              | std_ulogic                                 |             |
|  i_bus_re_buf         | std_ulogic                                 |             |
| if_pmp_fault          | std_ulogic                                 |             |
| ld_pmp_fault          | std_ulogic                                 |             |
| st_pmp_fault          | std_ulogic                                 |             |
## Constants
| Name             | Type                          | Value                              | Description |
| ---------------- | ----------------------------- | ---------------------------------- | ----------- |
| pmp_off_mode_c   | std_ulogic_vector(1 downto 0) |  "00"                              |             |
| pmp_napot_mode_c | std_ulogic_vector(1 downto 0) |  "11"                              |             |
| pmp_g_c          | natural                       |  index_size_f(PMP_MIN_GRANULARITY) |             |
| pmp_cfg_r_c      | natural                       |  0                                 |             |
| pmp_cfg_w_c      | natural                       |  1                                 |             |
| pmp_cfg_x_c      | natural                       |  2                                 |             |
| pmp_cfg_al_c     | natural                       |  3                                 |             |
| pmp_cfg_ah_c     | natural                       |  4                                 |             |
| pmp_cfg_l_c      | natural                       |  7                                 |             |
## Types
| Name          | Type | Description |
| ------------- | ---- | ----------- |
| bus_arbiter_t |      |             |
| pmp_addr_t    |      |             |
| pmp_t         |      |             |
## Processes
- mem_adr_reg: _( rstn_i, clk_i )_

- misaligned_d_check: _( mar, ctrl_i )_

- mem_do_reg: _( rstn_i, clk_i )_

- byte_enable: _( mar, mdo, ctrl_i )_

- mem_di_reg: _( rstn_i, clk_i )_

- read_align: _( mdi, mar, ctrl_i )_

- data_access_arbiter: _( rstn_i, clk_i )_

- pmp_dbus_buffer: _( rstn_i, clk_i )_

- exclusive_access_controller: _( rstn_i, clk_i )_

- ifetch_arbiter: _( rstn_i, clk_i )_

- pmp_ibus_buffer: _( rstn_i, clk_i )_

- pmp_masks: _( rstn_i, clk_i )_

- pmp_check_permission: _( pmp, pmp_ctrl_i, ctrl_i )_

