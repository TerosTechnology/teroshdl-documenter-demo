# Entity: sdram_ctrl_fsm
## Diagram
![Diagram](sdram_ctrl_fsm.svg "Diagram")
## Generics
| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| SDRAM_TYPE   | natural  |       |             |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| R_BITS       | positive |       |             |
| C_BITS       | positive |       |             |
| B_BITS       | positive |       |             |
| CL           | positive |       |             |
| BL           | positive |       |             |
| T_MRD        | integer  |       |             |
| T_RAS        | integer  |       |             |
| T_RCD        | integer  |       |             |
| T_RFC        | integer  |       |             |
| T_RP         | integer  |       |             |
| T_WR         | integer  |       |             |
| T_WTR        | integer  |       |             |
| T_REFI       | integer  |       |             |
| INIT_WAIT    | integer  |       |             |
## Ports
| Port name        | Direction | Type                                               | Description |
| ---------------- | --------- | -------------------------------------------------- | ----------- |
| clk              | in        | std_logic                                          |             |
| rst              | in        | std_logic                                          |             |
| user_cmd_valid   | in        | std_logic                                          |             |
| user_wdata_valid | in        | std_logic                                          |             |
| user_write       | in        | std_logic                                          |             |
| user_addr        | in        | std_logic_vector(A_BITS-1 downto 0)                |             |
| user_got_cmd     | out       | std_logic                                          |             |
| user_got_wdata   | out       | std_logic                                          |             |
| sd_cke_nxt       | out       | std_logic                                          |             |
| sd_cs_nxt        | out       | std_logic                                          |             |
| sd_ras_nxt       | out       | std_logic                                          |             |
| sd_cas_nxt       | out       | std_logic                                          |             |
| sd_we_nxt        | out       | std_logic                                          |             |
| sd_a_nxt         | out       | std_logic_vector(imax(R_BITS,C_BITS+1)-1 downto 0) |             |
| sd_ba_nxt        | out       | std_logic_vector(B_BITS-1 downto 0)                |             |
| rden_nxt         | out       | std_logic                                          |             |
| wren_nxt         | out       | std_logic                                          |             |
## Signals
| Name               | Type                                   | Description |
| ------------------ | -------------------------------------- | ----------- |
| fsm_cs             | FSM_TYPE                               |             |
| fsm_ns             | FSM_TYPE                               |             |
| sd_cmd_nxt         | SD_CMD_TYPE                            |             |
| bank_addr          | std_logic_vector(B_BITS-1 downto 0)    |             |
| row_addr           | std_logic_vector(R_BITS-1 downto 0)    |             |
| col_addr           | std_logic_vector(C_BITS-1 downto 0)    |             |
| precharge_all      | std_logic                              |             |
| reset_dll          | std_logic                              |             |
| sd_a_sel           | SD_A_SEL_TYPE                          |             |
| sd_ba_sel          | SD_BA_SEL_TYPE                         |             |
| timer_tREFI        | signed(log2ceil(T_REFI-2) downto 0)    |             |
| timer_tREFI_start  | std_logic                              |             |
| timer_tREFI_done   | std_logic                              |             |
| timer_cmd          | signed(5 downto 0)                     |             |
| timer_cmd_init     | signed(5 downto 0)                     |             |
| timer_cmd_start    | std_logic                              |             |
| timer_cmd_done     | std_logic                              |             |
| timer_tRAS         | signed(log2ceil(T_RAS-2) downto 0)     |             |
| timer_tRAS_start   | std_logic                              |             |
| timer_tRAS_done    | std_logic                              |             |
| downcnt            | signed(log2ceil(INIT_WAIT-2) downto 0) |             |
| downcnt_init       | signed(downcnt'range)                  |             |
| downcnt_set        | std_logic                              |             |
| downcnt_dec        | std_logic                              |             |
| downcnt_done       | std_logic                              |             |
| last_bank_addr_r   | std_logic_vector(bank_addr'range)      |             |
| last_bank_addr_nxt | std_logic_vector(bank_addr'range)      |             |
| last_row_addr_r    | std_logic_vector(row_addr'range)       |             |
| last_row_addr_nxt  | std_logic_vector(row_addr'range)       |             |
| last_write_r       | std_logic                              |             |
| last_write_nxt     | std_logic                              |             |
| save_cmd_addr      | std_logic                              |             |
| same_bank_row      | std_logic                              |             |
## Constants
| Name                   | Type                                | Value                                                                                                | Description |
| ---------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| BCC                    | natural                             |  burst_clock_cycles                                                                                  |             |
| SD_CMD_DESELECT        | SD_CMD_TYPE                         |  "1---"                                                                                              |             |
| SD_CMD_NOP             | SD_CMD_TYPE                         |  "0111"                                                                                              |             |
| SD_CMD_ACTIVE          | SD_CMD_TYPE                         |  "0011"                                                                                              |             |
| SD_CMD_READ            | SD_CMD_TYPE                         |  "0101"                                                                                              |             |
| SD_CMD_WRITE           | SD_CMD_TYPE                         |  "0100"                                                                                              |             |
| SD_CMD_BURST_TERMINATE | SD_CMD_TYPE                         |  "0110"                                                                                              |             |
| SD_CMD_PRECHARGE       | SD_CMD_TYPE                         |  "0010"                                                                                              |             |
| SD_CMD_AUTO_REFRESH    | SD_CMD_TYPE                         |  "0001"                                                                                              |             |
| SD_CMD_LOAD_MODE_REG   | SD_CMD_TYPE                         |  "0000"                                                                                              |             |
| EXT_MODE_REG           | std_logic_vector(1 downto 0)        |      (others => '0')                                                                                 |             |
| MODE_REG               | std_logic_vector(8 downto 0)        |      "00" & std_logic_vector(to_unsigned(CL, 3)) &     "0"  & std_logic_vector(to_unsigned(BL-1, 3)) |             |
| TIMER_TREFI_INIT       | signed(log2ceil(T_REFI-2) downto 0) |  to_signed(T_REFI-2, timer_tREFI'length)                                                             |             |
| TIMER_TRAS_INIT        | signed(log2ceil(T_RAS-2) downto 0)  |  to_signed(T_RAS-1 -2, timer_tRAS'length)                                                            |             |
## Types
| Name           | Type                                                                                                                                                                                                                                                                                                    | Description |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| FSM_TYPE       | (INIT1, INIT2, INIT3, INIT4, INIT5, INIT6, INIT7, INIT8,                     INIT9, INIT10, INIT11,                     DO_ACTIVATE,                     DO_READ1, DO_READ2,                     DO_WRITE1, DO_WRITE2,                     CHECKNXT,                     DO_PRECHARGE, DO_AUTO_REFRESH) |             |
| SD_A_SEL_TYPE  | (SD_A_SEL_EXT_MODE_REG,                          SD_A_SEL_MODE_REG,                          SD_A_SEL_ROW_ADDR,                          SD_A_SEL_COL_ADDR)                                                                                                                                             |             |
| SD_BA_SEL_TYPE | (SD_BA_SEL_EXT_MODE_REG,                          SD_BA_SEL_MODE_REG,                          SD_BA_SEL_ADDR)                                                                                                                                                                                          |             |
## Functions
- burst_clock_cycles <font id="function_arguments">()</font> <font id="function_return">return positive</font>
## Processes
- unnamed: _( fsm_cs,
           timer_tREFI_done, timer_cmd_done, timer_tRAS_done,
           downcnt_done,
           same_bank_row, last_write_r,
           user_cmd_valid, user_write, user_wdata_valid )_

- unnamed: _( sd_a_sel, reset_dll, row_addr, col_addr, precharge_all )_

- unnamed: _( clk )_

