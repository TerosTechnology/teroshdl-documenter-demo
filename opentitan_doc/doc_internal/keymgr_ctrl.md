# Entity: keymgr_ctrl

- **File**: keymgr_ctrl.sv
## Diagram

![Diagram](keymgr_ctrl.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Key manager top level
 
## Ports

| Port name            | Direction | Type                        | Description                                       |
| -------------------- | --------- | --------------------------- | ------------------------------------------------- |
| clk_i                | input     |                             |                                                   |
| rst_ni               | input     |                             |                                                   |
| en_i                 | input     |                             | lifecycle enforcement                             |
| op_start_i           | input     |                             | Software interface                                |
| op_i                 | input     | keymgr_ops_e                |                                                   |
| op_cdi_sel_i         | input     | [CdiWidth-1:0]              |                                                   |
| op_done_o            | output    |                             |                                                   |
| status_o             | output    | keymgr_op_status_e          |                                                   |
| error_o              | output    | [ErrLastPos-1:0]            |                                                   |
| data_en_o            | output    |                             |                                                   |
| data_valid_o         | output    |                             |                                                   |
| wipe_key_o           | output    |                             |                                                   |
| working_state_o      | output    | keymgr_working_state_e      |                                                   |
| sw_binding_unlock_o  | output    |                             |                                                   |
| init_o               | output    |                             |                                                   |
| root_key_i           | input     |                             | Data input                                        |
| hw_sel_o             | output    | keymgr_gen_out_e            |                                                   |
| stage_sel_o          | output    | keymgr_stage_e              |                                                   |
| cdi_sel_o            | output    | [CdiWidth-1:0]              |                                                   |
| adv_en_o             | output    |                             | KMAC ctrl interface                               |
| id_en_o              | output    |                             |                                                   |
| gen_en_o             | output    |                             |                                                   |
| key_o                | output    | hw_key_req_t                |                                                   |
| kmac_done_i          | input     |                             |                                                   |
| kmac_input_invalid_i | input     |                             | asserted when selected data fails criteria check  |
| kmac_fsm_err_i       | input     |                             | asserted when kmac fsm reaches unexpected state   |
| kmac_op_err_i        | input     |                             | asserted when kmac itself reports an error        |
| kmac_cmd_err_i       | input     |                             | asserted when more than one command given to kmac |
| kmac_data_i          | input     | [Shares-1:0][KeyWidth-1:0]  |                                                   |
| entropy_i            | input     | [Shares-1:0][RandWidth-1:0] | prng control interface                            |
| prng_reseed_ack_i    | input     |                             |                                                   |
| prng_reseed_req_o    | output    |                             |                                                   |
| prng_en_o            | output    |                             |                                                   |
## Signals

| Name             | Type                                                              | Description                                                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| state_q          | keymgr_ctrl_state_e                                               |                                                                                                                                                                                 |
| state_d          | keymgr_ctrl_state_e                                               |                                                                                                                                                                                 |
| op_state_q       | keymgr_op_state_e                                                 |                                                                                                                                                                                 |
| op_state_d       | keymgr_op_state_e                                                 |                                                                                                                                                                                 |
| key_state_q      | logic [CDIs-1:0][Shares-1:0][EntropyRounds-1:0][EntropyWidth-1:0] | There are two versions of the key state, one for sealing one for attestation Among each version, there are multiple shares Each share is a fixed multiple of the entropy width  |
| key_state_d      | logic [CDIs-1:0][Shares-1:0][EntropyRounds-1:0][EntropyWidth-1:0] | There are two versions of the key state, one for sealing one for attestation Among each version, there are multiple shares Each share is a fixed multiple of the entropy width  |
| cnt              | logic [CntWidth-1:0]                                              |                                                                                                                                                                                 |
| cdi_cnt          | logic [CdiWidth-1:0]                                              |                                                                                                                                                                                 |
| key_update       | logic                                                             |                                                                                                                                                                                 |
| data_update      | logic                                                             |                                                                                                                                                                                 |
| kmac_out_valid   | logic                                                             |                                                                                                                                                                                 |
| invalid_op       | logic                                                             |                                                                                                                                                                                 |
| disabled         | logic                                                             |                                                                                                                                                                                 |
| advance_sel      | logic                                                             | disable is treated like an advanced call                                                                                                                                        |
| disable_sel      | logic                                                             |                                                                                                                                                                                 |
| gen_id_sel       | logic                                                             |                                                                                                                                                                                 |
| gen_out_sw_sel   | logic                                                             |                                                                                                                                                                                 |
| gen_out_hw_sel   | logic                                                             |                                                                                                                                                                                 |
| gen_out_sel      | logic                                                             |                                                                                                                                                                                 |
| gen_sel          | logic                                                             |                                                                                                                                                                                 |
| op_err           | logic                                                             | error types                                                                                                                                                                     |
| fault_err        | logic                                                             |                                                                                                                                                                                 |
| fault_err_q      | logic                                                             |                                                                                                                                                                                 |
| fault_err_d      | logic                                                             |                                                                                                                                                                                 |
| op_req           | logic                                                             | req/ack interface with op handling fsm                                                                                                                                          |
| op_ack           | logic                                                             |                                                                                                                                                                                 |
| op_update        | logic                                                             |                                                                                                                                                                                 |
| random_req       | logic                                                             |                                                                                                                                                                                 |
| random_ack       | logic                                                             |                                                                                                                                                                                 |
| wipe_req         | logic                                                             | req from main control fsm to key update controls                                                                                                                                |
| adv_req          | logic                                                             | requestion from working state to operation handling FSM                                                                                                                         |
| id_req           | logic                                                             | requestion from working state to operation handling FSM                                                                                                                         |
| gen_req          | logic                                                             | requestion from working state to operation handling FSM                                                                                                                         |
| root_key_valid_q | logic                                                             | root key valid sync                                                                                                                                                             |
| update_sel       | keymgr_key_update_e                                               |                                                                                                                                                                                 |
| op_update_sel    | keymgr_key_update_e                                               |                                                                                                                                                                                 |
| key_update_vld   | logic                                                             |                                                                                                                                                                                 |
| next_state       | logic                                                             |                                                                                                                                                                                 |
| invalid_state    | logic                                                             |                                                                                                                                                                                 |
| clr_err          | logic                                                             | if working over multiple CDIs, a fault of any is considered an overall fault                                                                                                    |
| data_st_d        | keymgr_ctrl_data_state_e                                          |                                                                                                                                                                                 |
| data_st_q        | keymgr_ctrl_data_state_e                                          |                                                                                                                                                                                 |
## Constants

| Name            | Type | Value                                             | Description |
| --------------- | ---- | ------------------------------------------------- | ----------- |
| EntropyWidth    | int  | LfsrWidth / 2                                     |             |
| EntropyRounds   | int  | KeyWidth / EntropyWidth                           |             |
| EntropyRndWidth | int  | prim_util_pkg::vbits(EntropyRounds)               |             |
| CntWidth        | int  | EntropyRounds > CDIs ? EntropyRndWidth : CdiWidth |             |
## Types

| Name                     | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| keymgr_ctrl_state_e      | enum logic [3:0] {<br><span style="padding-left:20px">     StCtrlReset,<br><span style="padding-left:20px">     StCtrlEntropyReseed,<br><span style="padding-left:20px">     StCtrlRandom,<br><span style="padding-left:20px">     StCtrlRootKey,<br><span style="padding-left:20px">     StCtrlInit,<br><span style="padding-left:20px">     StCtrlCreatorRootKey,<br><span style="padding-left:20px">     StCtrlOwnerIntKey,<br><span style="padding-left:20px">     StCtrlOwnerKey,<br><span style="padding-left:20px">     StCtrlDisabled,<br><span style="padding-left:20px">     StCtrlWipe,<br><span style="padding-left:20px">     StCtrlInvalid   } | Enumeration for working state                                                   |
| keymgr_op_state_e        | enum logic [2:0] {<br><span style="padding-left:20px">     StIdle,<br><span style="padding-left:20px">     StRandomize,<br><span style="padding-left:20px">     StAdv,<br><span style="padding-left:20px">     StAdvAck,<br><span style="padding-left:20px">     StWait   }                                                                                                                                                                                                                                                                                                                                                                                  | Enumeration for operation handling                                              |
| keymgr_ctrl_data_state_e | enum logic [1:0] {<br><span style="padding-left:20px">     StCtrlDataIdle,<br><span style="padding-left:20px">     StCtrlDataEn,<br><span style="padding-left:20px">     StCtrlDataDis,<br><span style="padding-left:20px">     StCtrlDataWait   }                                                                                                                                                                                                                                                                                                                                                                                                           | This is a separate data path from the FSM used to control the data_en_o output  |
## Functions
- valid_data_chk <font id="function_arguments">(logic [KeyWidth-1:0])</font> <font id="function_return">return (logic)</font>
**Description**
unclear what this is supposed to be yet
right now just check to see if it not all 0's and not all 1's

## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
**Description**
Unlike the key state, the working state can be safely reset.

- unnamed: ( @(posedge clk_i) )
**Description**
key state is intentionally not reset

- unnamed: (  )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
- unnamed: (  )
**Description**
always_comb
Current working state provided for software read
Certain states are collapsed for simplicity

- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
- unnamed: (  )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
**Description**
The below control path is used for modulating the datapath to sideload and sw keys.
This path is separate from the data_valid_o path, thus creating two separate attack points.
The data is only enabled when a non-advance operation is invoked.
When an advance operation is called, the data is disabled. It will stay disabled until an
entire completion sequence is seen (op_done_o assert -> start_i de-assertion).
When a generate operation is called, the data is enabled.  However, any indication of this
supposedly being an advance call will force the path to disable again.

## Instantiations

- u_key_valid_sync: prim_flop_2sync
