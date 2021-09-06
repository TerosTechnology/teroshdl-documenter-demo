# Entity: keymgr_ctrl

- **File**: keymgr_ctrl.sv
## Diagram

![Diagram](keymgr_ctrl.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Key manager top level


## Generics

| Generic name  | Type | Value | Description |
| ------------- | ---- | ----- | ----------- |
| KmacEnMasking | bit  | 1'b1  |             |
## Ports

| Port name              | Direction | Type                        | Description                                       |
| ---------------------- | --------- | --------------------------- | ------------------------------------------------- |
| clk_i                  | input     |                             |                                                   |
| rst_ni                 | input     |                             |                                                   |
| en_i                   | input     |                             |  lifecycle enforcement                            |
| regfile_intg_err_i     | input     |                             |  faults that can occur outside of operations      |
| shadowed_update_err_i  | input     |                             |                                                   |
| shadowed_storage_err_i | input     |                             |                                                   |
| op_start_i             | input     |                             |  Software interface                               |
| op_i                   | input     | keymgr_ops_e                |                                                   |
| op_cdi_sel_i           | input     | [CdiWidth-1:0]              |                                                   |
| op_done_o              | output    |                             |                                                   |
| status_o               | output    | keymgr_op_status_e          |                                                   |
| error_o                | output    | [ErrLastPos-1:0]            |                                                   |
| fault_o                | output    | [FaultLastPos-1:0]          |                                                   |
| data_en_o              | output    |                             |                                                   |
| data_valid_o           | output    |                             |                                                   |
| wipe_key_o             | output    |                             |                                                   |
| working_state_o        | output    | keymgr_working_state_e      |                                                   |
| sw_binding_unlock_o    | output    |                             |                                                   |
| init_o                 | output    |                             |                                                   |
| root_key_i             | input     |                             |  Data input                                       |
| hw_sel_o               | output    | keymgr_gen_out_e            |                                                   |
| stage_sel_o            | output    | keymgr_stage_e              |                                                   |
| cdi_sel_o              | output    | [CdiWidth-1:0]              |                                                   |
| adv_en_o               | output    |                             |  KMAC ctrl interface                              |
| id_en_o                | output    |                             |                                                   |
| gen_en_o               | output    |                             |                                                   |
| key_o                  | output    | hw_key_req_t                |                                                   |
| kmac_done_i            | input     |                             |                                                   |
| kmac_input_invalid_i   | input     |                             | asserted when selected data fails criteria check  |
| kmac_fsm_err_i         | input     |                             | asserted when kmac fsm reaches unexpected state   |
| kmac_op_err_i          | input     |                             | asserted when kmac itself reports an error        |
| kmac_cmd_err_i         | input     |                             | asserted when more than one command given to kmac |
| kmac_data_i            | input     | [Shares-1:0][KeyWidth-1:0]  |                                                   |
| entropy_i              | input     | [Shares-1:0][RandWidth-1:0] |  prng control interface                           |
| prng_reseed_ack_i      | input     |                             |                                                   |
| prng_reseed_req_o      | output    |                             |                                                   |
| prng_en_o              | output    |                             |                                                   |
## Signals

| Name             | Type                                                              | Description                                                                                                                                                                                                               |
| ---------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| state_q          | keymgr_ctrl_state_e                                               |                                                                                                                                                                                                                           |
| state_d          | keymgr_ctrl_state_e                                               |                                                                                                                                                                                                                           |
| op_state_q       | keymgr_op_state_e                                                 |                                                                                                                                                                                                                           |
| op_state_d       | keymgr_op_state_e                                                 |                                                                                                                                                                                                                           |
| key_state_q      | logic [CDIs-1:0][Shares-1:0][EntropyRounds-1:0][EntropyWidth-1:0] |  There are two versions of the key state, one for sealing one for attestation  Among each version, there are multiple shares  Each share is a fixed multiple of the entropy width                                         |
| key_state_d      | logic [CDIs-1:0][Shares-1:0][EntropyRounds-1:0][EntropyWidth-1:0] |  There are two versions of the key state, one for sealing one for attestation  Among each version, there are multiple shares  Each share is a fixed multiple of the entropy width                                         |
| cnt              | logic [CntWidth-1:0]                                              |                                                                                                                                                                                                                           |
| cdi_cnt          | logic [CdiWidth-1:0]                                              |                                                                                                                                                                                                                           |
| invalid_kmac_out | logic                                                             |  error conditions                                                                                                                                                                                                         |
| invalid_op       | logic                                                             |                                                                                                                                                                                                                           |
| cnt_err          | logic                                                             |                                                                                                                                                                                                                           |
| state_intg_err_q | logic                                                             |  states fall out of sparsely encoded range                                                                                                                                                                                |
| state_intg_err_d | logic                                                             |  states fall out of sparsely encoded range                                                                                                                                                                                |
| adv_op           | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| dis_op           | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| gen_id_op        | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| gen_sw_op        | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| gen_hw_op        | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| gen_op           | logic                                                             | /////////////////////////   General operation decode /////////////////////////                                                                                                                                            |
| advance_sel      | logic                                                             | /////////////////////////   interaction between software and main fsm /////////////////////////  disable is treated like an advanced call                                                                                 |
| disable_sel      | logic                                                             |                                                                                                                                                                                                                           |
| gen_out_hw_sel   | logic                                                             |                                                                                                                                                                                                                           |
| op_req           | logic                                                             | /////////////////////////   interaction between main control fsm and operation fsm /////////////////////////  req/ack interface with op handling fsm                                                                      |
| op_ack           | logic                                                             |                                                                                                                                                                                                                           |
| op_update        | logic                                                             |                                                                                                                                                                                                                           |
| op_busy          | logic                                                             |                                                                                                                                                                                                                           |
| disabled         | logic                                                             |                                                                                                                                                                                                                           |
| adv_req          | logic                                                             |                                                                                                                                                                                                                           |
| dis_req          | logic                                                             |                                                                                                                                                                                                                           |
| id_req           | logic                                                             |                                                                                                                                                                                                                           |
| gen_req          | logic                                                             |                                                                                                                                                                                                                           |
| sync_err         | logic [SyncErrLastIdx-1:0]                                        | /////////////////////////   interaction between operation fsm and software /////////////////////////  categories of keymgr errors                                                                                         |
| async_err        | logic [AsyncErrLastIdx-1:0]                                       |                                                                                                                                                                                                                           |
| sync_fault       | logic [SyncFaultLastIdx-1:0]                                      |                                                                                                                                                                                                                           |
| async_fault      | logic [AsyncFaultLastIdx-1:0]                                     |                                                                                                                                                                                                                           |
| op_err           | logic                                                             |                                                                                                                                                                                                                           |
| op_fault_err     | logic                                                             |                                                                                                                                                                                                                           |
| update_sel       | keymgr_key_update_e                                               |                                                                                                                                                                                                                           |
| op_update_sel    | keymgr_key_update_e                                               |                                                                                                                                                                                                                           |
| wipe_req         | logic                                                             |  req from main control fsm to key update controls                                                                                                                                                                         |
| random_req       | logic                                                             |                                                                                                                                                                                                                           |
| random_ack       | logic                                                             |                                                                                                                                                                                                                           |
| prng_en          | logic                                                             | /////////////////////////   interaction between main fsm and prng /////////////////////////                                                                                                                               |
| state_raw_q      | logic [StateWidth-1:0]                                            | ////////////////////////  Main Control FSM ////////////////////////                                                                                                                                                       |
| root_key_valid_q | logic                                                             |  root key valid sync                                                                                                                                                                                                      |
| adv_state        | logic                                                             |  There are 3 possibilities  advance to next state (software command)  advance to disabled state (software command)  advance to invalid state (detected fault)                                                             |
| dis_state        | logic                                                             |                                                                                                                                                                                                                           |
| inv_state        | logic                                                             |                                                                                                                                                                                                                           |
| last_working_st  | keymgr_working_state_e                                            |  always_comb  Current working state provided for software read  Certain states are collapsed for simplicity                                                                                                               |
| state_update     | logic                                                             |                                                                                                                                                                                                                           |
| sync_err_q       | logic[SyncErrLastIdx-1:0]                                         |  Advance calls are made up of multiple rounds of kmac operations.  Any sync error that occurs is treated as an error of the entire call.  Therefore sync errors that happen before the end of the call must be  latched.  |
| sync_err_d       | logic[SyncErrLastIdx-1:0]                                         |  Advance calls are made up of multiple rounds of kmac operations.  Any sync error that occurs is treated as an error of the entire call.  Therefore sync errors that happen before the end of the call must be  latched.  |
| sync_fault_q     | logic[SyncFaultLastIdx-1:0]                                       |                                                                                                                                                                                                                           |
| sync_fault_d     | logic[SyncFaultLastIdx-1:0]                                       |                                                                                                                                                                                                                           |
| err_vld          | logic                                                             |                                                                                                                                                                                                                           |
| data_st_d        | keymgr_ctrl_data_state_e                                          |                                                                                                                                                                                                                           |
| data_st_q        | keymgr_ctrl_data_state_e                                          |                                                                                                                                                                                                                           |
## Constants

| Name            | Type | Value                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | ---- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EntropyWidth    | int  | LfsrWidth / 2                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| EntropyRounds   | int  | KeyWidth / EntropyWidth                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| EntropyRndWidth | int  | prim_util_pkg::vbits(EntropyRounds)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CntWidth        | int  | EntropyRounds > CDIs ? EntropyRndWidth : CdiWidth |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| StateWidth      | int  | 10                                                |  Enumeration for working state  Encoding generated with:  $ ./util/design/sparse-fsm-encode.py -d 5 -m 11 -n 10 \       -s 4101887575 --language=sv<br>  Hamming distance histogram:<br>   0: --   1: --   2: --   3: --   4: --   5: |||||||||||||||||||| (54.55%)   6: |||||||||||||||| (45.45%)   7: --   8: --   9: --  10: --<br>  Minimum Hamming distance: 5  Maximum Hamming distance: 6  Minimum Hamming weight: 2  Maximum Hamming weight: 8<br>  |
## Types

| Name                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description                                                                                                                                                             |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| keymgr_ctrl_state_e      | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     StCtrlReset          = 10'b1101100001,<br><span style="padding-left:20px">     StCtrlEntropyReseed  = 10'b1110010010,<br><span style="padding-left:20px">     StCtrlRandom         = 10'b0011110100,<br><span style="padding-left:20px">     StCtrlRootKey        = 10'b0110101111,<br><span style="padding-left:20px">     StCtrlInit           = 10'b0100000100,<br><span style="padding-left:20px">     StCtrlCreatorRootKey = 10'b1000011101,<br><span style="padding-left:20px">     StCtrlOwnerIntKey    = 10'b0001001010,<br><span style="padding-left:20px">     StCtrlOwnerKey       = 10'b1101111110,<br><span style="padding-left:20px">     StCtrlDisabled       = 10'b1010101000,<br><span style="padding-left:20px">     StCtrlWipe           = 10'b0000110011,<br><span style="padding-left:20px">     StCtrlInvalid        = 10'b1011000111   } |                                                                                                                                                                         |
| keymgr_op_state_e        | enum logic [1:0] {<br><span style="padding-left:20px">     StIdle,<br><span style="padding-left:20px">     StAdv,<br><span style="padding-left:20px">     StAdvAck,<br><span style="padding-left:20px">     StWait   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  Enumeration for operation handling                                                                                                                                     |
| keymgr_ctrl_data_state_e | enum logic [1:0] {<br><span style="padding-left:20px">     StCtrlDataIdle,<br><span style="padding-left:20px">     StCtrlDataEn,<br><span style="padding-left:20px">     StCtrlDataDis,<br><span style="padding-left:20px">     StCtrlDataWait   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | /////////////////////////////  Suppress kmac return data /////////////////////////////  This is a separate data path from the FSM used to control the data_en_o output  |
## Functions
- valid_data_chk <font id="function_arguments">(logic [KeyWidth-1:0])</font> <font id="function_return">return (logic)</font>
</br>**Description**
/////////////////////////////
 Functions
/////////////////////////////
 unclear what this is supposed to be yet
 right now just check to see if it not all 0's and not all 1's

## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_i) )
  - **Type:** always_ff
</br>**Description**
 key state is intentionally not reset 
- unnamed: (  )
  - **Type:** always_comb
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
</br>**Description**
///////////////////////  Operateion state, handle advance and generate /////////////////////// 
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
</br>**Description**
 The below control path is used for modulating the datapath to sideload and sw keys.  This path is separate from the data_valid_o path, thus creating two separate attack points.  The data is only enabled when a non-advance operation is invoked.  When an advance operation is called, the data is disabled. It will stay disabled until an  entire completion sequence is seen (op_done_o assert -> start_i de-assertion).  When a generate operation is called, the data is enabled.  However, any indication of this  supposedly being an advance call will force the path to disable again. 
## Instantiations

- u_state_regs: prim_flop
- u_key_valid_sync: prim_flop_2sync
- u_cnt: keymgr_cnt
