# Entity: neorv32_cpu_control
## Diagram
![Diagram](neorv32_cpu_control.svg "Diagram")
## Generics
| Generic name                 | Type                           | Value       | Description |
| ---------------------------- | ------------------------------ | ----------- | ----------- |
| HW_THREAD_ID                 | natural                        | 0           |             |
| CPU_BOOT_ADDR                | std_ulogic_vector(31 downto 0) | x"00000000" |             |
| CPU_DEBUG_ADDR               | std_ulogic_vector(31 downto 0) | x"00000000" |             |
| CPU_EXTENSION_RISCV_A        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_C        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_E        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_M        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_U        | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zfinx    | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zicsr    | boolean                        | true        |             |
| CPU_EXTENSION_RISCV_Zifencei | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_Zmmul    | boolean                        | false       |             |
| CPU_EXTENSION_RISCV_DEBUG    | boolean                        | false       |             |
| CPU_CNT_WIDTH                | natural                        | 64          |             |
| PMP_NUM_REGIONS              | natural                        | 0           |             |
| PMP_MIN_GRANULARITY          | natural                        | 64*1024     |             |
| HPM_NUM_CNTS                 | natural                        | 0           |             |
| HPM_CNT_WIDTH                | natural                        | 40          |             |
## Ports
| Port name     | Direction | Type                                       | Description |
| ------------- | --------- | ------------------------------------------ | ----------- |
| clk_i         | in        | std_ulogic                                 |             |
| rstn_i        | in        | std_ulogic                                 |             |
| ctrl_o        | out       | std_ulogic_vector(ctrl_width_c-1 downto 0) |             |
| alu_idone_i   | in        | std_ulogic                                 |             |
| bus_i_wait_i  | in        | std_ulogic                                 |             |
| bus_d_wait_i  | in        | std_ulogic                                 |             |
| excl_state_i  | in        | std_ulogic                                 |             |
| instr_i       | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| cmp_i         | in        | std_ulogic_vector(1 downto 0)              |             |
| alu_add_i     | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| rs1_i         | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| imm_o         | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| fetch_pc_o    | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| curr_pc_o     | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| csr_rdata_o   | out       | std_ulogic_vector(data_width_c-1 downto 0) |             |
| fpu_flags_i   | in        | std_ulogic_vector(04 downto 0)             |             |
| db_halt_req_i | in        | std_ulogic                                 |             |
| nm_irq_i      | in        | std_ulogic                                 |             |
| msw_irq_i     | in        | std_ulogic                                 |             |
| mext_irq_i    | in        | std_ulogic                                 |             |
| mtime_irq_i   | in        | std_ulogic                                 |             |
| firq_i        | in        | std_ulogic_vector(15 downto 0)             |             |
| firq_ack_o    | out       | std_ulogic_vector(15 downto 0)             |             |
| time_i        | in        | std_ulogic_vector(63 downto 0)             |             |
| pmp_addr_o    | out       | pmp_addr_if_t                              |             |
| pmp_ctrl_o    | out       | pmp_ctrl_if_t                              |             |
| mar_i         | in        | std_ulogic_vector(data_width_c-1 downto 0) |             |
| ma_instr_i    | in        | std_ulogic                                 |             |
| ma_load_i     | in        | std_ulogic                                 |             |
| ma_store_i    | in        | std_ulogic                                 |             |
| be_instr_i    | in        | std_ulogic                                 |             |
| be_load_i     | in        | std_ulogic                                 |             |
| be_store_i    | in        | std_ulogic                                 |             |
## Signals
| Name                | Type                                              | Description |
| ------------------- | ------------------------------------------------- | ----------- |
| fetch_engine        | fetch_engine_t                                    |             |
| ipb                 | ipb_t                                             |             |
| ci_instr16          | std_ulogic_vector(15 downto 0)                    |             |
| ci_instr32          | std_ulogic_vector(31 downto 0)                    |             |
| ci_illegal          | std_ulogic                                        |             |
| issue_engine        | issue_engine_t                                    |             |
| cmd_issue           | cmd_issue_t                                       |             |
| decode_aux          | decode_aux_t                                      |             |
| execute_engine      | execute_engine_t                                  |             |
| trap_ctrl           | trap_ctrl_t                                       |             |
| ctrl_nxt            | std_ulogic_vector(ctrl_width_c-1 downto 0)        |             |
|  ctrl               | std_ulogic_vector(ctrl_width_c-1 downto 0)        |             |
| bus_fast_ir         | std_ulogic                                        |             |
| csr                 | csr_t                                             |             |
| debug_ctrl          | debug_ctrl_t                                      |             |
| cnt_event           | std_ulogic_vector(hpmcnt_event_size_c-1 downto 0) |             |
|  cnt_event_nxt      | std_ulogic_vector(hpmcnt_event_size_c-1 downto 0) |             |
| hpmcnt_trigger      | std_ulogic_vector(HPM_NUM_CNTS-1 downto 0)        |             |
| illegal_opcode_lsbs | std_ulogic                                        |             |
| illegal_instruction | std_ulogic                                        |             |
| illegal_register    | std_ulogic                                        |             |
| illegal_compressed  | std_ulogic                                        |             |
| csr_acc_valid       | std_ulogic                                        |             |
## Constants
| Name               | Type    | Value                                                                      | Description |
| ------------------ | ------- | -------------------------------------------------------------------------- | ----------- |
| cpu_cnt_lo_width_c | natural |  natural(cond_sel_int_f(boolean(CPU_CNT_WIDTH < 32), CPU_CNT_WIDTH, 32))   |             |
| cpu_cnt_hi_width_c | natural |  natural(cond_sel_int_f(boolean(CPU_CNT_WIDTH > 32), CPU_CNT_WIDTH-32, 0)) |             |
| hpm_cnt_lo_width_c | natural |  natural(cond_sel_int_f(boolean(HPM_CNT_WIDTH < 32), HPM_CNT_WIDTH, 32))   |             |
| hpm_cnt_hi_width_c | natural |  natural(cond_sel_int_f(boolean(HPM_CNT_WIDTH > 32), HPM_CNT_WIDTH-32, 0)) |             |
## Types
| Name                   | Type                                                                                                                                                                                        | Description |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| fetch_engine_state_t   | (IFETCH_REQUEST, IFETCH_ISSUE)                                                                                                                                                              |             |
| fetch_engine_t         |                                                                                                                                                                                             |             |
| ipb_data_fifo_t        |                                                                                                                                                                                             |             |
| ipb_t                  |                                                                                                                                                                                             |             |
| issue_engine_state_t   | (ISSUE_ACTIVE, ISSUE_REALIGN)                                                                                                                                                               |             |
| issue_engine_t         |                                                                                                                                                                                             |             |
| cmd_issue_t            |                                                                                                                                                                                             |             |
| decode_aux_t           |                                                                                                                                                                                             |             |
| execute_engine_state_t | (SYS_WAIT, DISPATCH, TRAP_ENTER, TRAP_EXIT, TRAP_EXECUTE, EXECUTE, ALU_WAIT, BRANCH,                                   FENCE_OP,LOADSTORE_0, LOADSTORE_1, LOADSTORE_2, SYS_ENV, CSR_ACCESS) |             |
| execute_engine_t       |                                                                                                                                                                                             |             |
| trap_ctrl_t            |                                                                                                                                                                                             |             |
| pmp_ctrl_t             |                                                                                                                                                                                             |             |
| pmp_addr_t             |                                                                                                                                                                                             |             |
| pmp_ctrl_rd_t          |                                                                                                                                                                                             |             |
| mhpmevent_t            |                                                                                                                                                                                             |             |
| mhpmcnt_t              |                                                                                                                                                                                             |             |
| mhpmcnt_nxt_t          |                                                                                                                                                                                             |             |
| mhpmcnt_ovfl_t         |                                                                                                                                                                                             |             |
| mhpmcnt_rd_t           |                                                                                                                                                                                             |             |
| csr_t                  |                                                                                                                                                                                             |             |
| debug_ctrl_state_t     | (DEBUG_OFFLINE, DEBUG_PENDING, DEBUG_ONLINE, DEBUG_EXIT)                                                                                                                                    |             |
| debug_ctrl_t           |                                                                                                                                                                                             |             |
## Processes
- fetch_engine_fsm_sync: _( rstn_i, clk_i )_

- fetch_engine_fsm_comb: _( fetch_engine, execute_engine, ipb, instr_i, bus_i_wait_i, be_instr_i, ma_instr_i )_

- instr_prefetch_buffer_ctrl: _( rstn_i, clk_i )_

- instr_prefetch_buffer_data: _( clk_i )_

- issue_engine_fsm_sync: _( rstn_i, clk_i )_

- issue_engine_fsm_comb: _( issue_engine, ipb, execute_engine, ci_illegal, ci_instr32 )_

- imm_gen: _( execute_engine.i_reg, rstn_i, clk_i )_

- branch_check: _( execute_engine.i_reg, cmp_i )_

- execute_engine_fsm_sync: _( rstn_i, clk_i )_

- ctrl_output: _( ctrl, fetch_engine, trap_ctrl, bus_fast_ir, execute_engine, csr, debug_ctrl )_

- decode_helper: _( execute_engine )_

- execute_engine_fsm_comb: _( execute_engine, debug_ctrl, trap_ctrl, decode_aux, fetch_engine, cmd_issue,
                                   csr, ctrl, csr_acc_valid, alu_idone_i, bus_d_wait_i, excl_state_i )_

- csr_access_check: _( execute_engine.i_reg, csr, debug_ctrl )_

- illegal_instruction_check: _( execute_engine, decode_aux, csr_acc_valid, debug_ctrl )_

- trap_controller: _( rstn_i, clk_i )_

- trap_priority: _( trap_ctrl )_

- csr_write_data: _( execute_engine.i_reg, csr.rdata, rs1_i )_

- csr_write_access: _( rstn_i, clk_i )_

- pmp_output: _( csr )_

- pmp_rd_dummy: _( csr )_

- csr_counters: _( rstn_i, clk_i )_

- hpm_rd_dummy: _( csr )_

- hpmcnt_ctrl: _( rstn_i, clk_i )_

- csr_read_access: _( rstn_i, clk_i )_

- debug_control: _( rstn_i, clk_i )_

