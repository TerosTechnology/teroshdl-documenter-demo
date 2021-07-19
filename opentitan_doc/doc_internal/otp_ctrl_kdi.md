# Entity: otp_ctrl_kdi

- **File**: otp_ctrl_kdi.sv
## Diagram

![Diagram](otp_ctrl_kdi.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Scrambling key derivation module for OTP.
 
## Ports

| Port name               | Direction | Type                     | Description                                                             |
| ----------------------- | --------- | ------------------------ | ----------------------------------------------------------------------- |
| clk_i                   | input     |                          |                                                                         |
| rst_ni                  | input     |                          |                                                                         |
| kdi_en_i                | input     |                          | Pulse to enable this module after OTP partitions havebeen initialized.  |
| escalate_en_i           | input     |                          | Escalation input. This moves the FSM into a terminal state.             |
| fsm_err_o               | output    |                          | FSM is in error state                                                   |
| scrmbl_key_seed_valid_i | input     |                          | Key seed inputs from OTP                                                |
| flash_data_key_seed_i   | input     | [FlashKeySeedWidth-1:0]  |                                                                         |
| flash_addr_key_seed_i   | input     | [FlashKeySeedWidth-1:0]  |                                                                         |
| sram_data_key_seed_i    | input     | [SramKeySeedWidth-1:0]   |                                                                         |
| edn_req_o               | output    |                          | EDN interface for requesting entropy                                    |
| edn_ack_i               | input     |                          |                                                                         |
| edn_data_i              | input     | [EdnDataWidth-1:0]       |                                                                         |
| flash_otp_key_i         | input     | flash_otp_key_req_t      | Scrambling key requests                                                 |
| flash_otp_key_o         | output    | flash_otp_key_rsp_t      |                                                                         |
| sram_otp_key_i          | input     | [NumSramKeyReqSlots-1:0] |                                                                         |
| sram_otp_key_o          | output    | [NumSramKeyReqSlots-1:0] |                                                                         |
| otbn_otp_key_i          | input     | otbn_otp_key_req_t       |                                                                         |
| otbn_otp_key_o          | output    | otbn_otp_key_rsp_t       |                                                                         |
| scrmbl_mtx_req_o        | output    |                          | Scrambling mutex request                                                |
| scrmbl_mtx_gnt_i        | input     |                          |                                                                         |
| scrmbl_cmd_o            | output    | otp_scrmbl_cmd_e         | Scrambling datapath interface                                           |
| scrmbl_mode_o           | output    | digest_mode_e            |                                                                         |
| scrmbl_sel_o            | output    | [ConstSelWidth-1:0]      |                                                                         |
| scrmbl_data_o           | output    | [ScrmblBlockWidth-1:0]   |                                                                         |
| scrmbl_valid_o          | output    |                          |                                                                         |
| scrmbl_ready_i          | input     |                          |                                                                         |
| scrmbl_valid_i          | input     |                          |                                                                         |
| scrmbl_data_i           | input     | [ScrmblBlockWidth-1:0]   |                                                                         |
## Signals

| Name              | Type                                                              | Description                                                                                                                |
| ----------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| req               | logic [NumReq-1:0]                                                |                                                                                                                            |
| gnt               | logic [NumReq-1:0]                                                |                                                                                                                            |
| req_bundles       | req_bundle_t                                                      |                                                                                                                            |
| req_valid         | logic                                                             | This arbitrates among incoming key derivation requests on a round robin basis to prevent deadlock.                         |
| req_ready         | logic                                                             | This arbitrates among incoming key derivation requests on a round robin basis to prevent deadlock.                         |
| req_bundle        | req_bundle_t                                                      |                                                                                                                            |
| seed_cnt_clr      | logic                                                             |                                                                                                                            |
| seed_cnt_en       | logic                                                             |                                                                                                                            |
| entropy_cnt_clr   | logic                                                             |                                                                                                                            |
| entropy_cnt_en    | logic                                                             |                                                                                                                            |
| seed_cnt_d        | logic [1:0]                                                       |                                                                                                                            |
| seed_cnt_q        | logic [1:0]                                                       |                                                                                                                            |
| entropy_cnt_d     | logic [1:0]                                                       |                                                                                                                            |
| entropy_cnt_q     | logic [1:0]                                                       |                                                                                                                            |
| seed_valid_reg_en | logic                                                             |                                                                                                                            |
| key_reg_en        | logic                                                             |                                                                                                                            |
| nonce_reg_en      | logic                                                             |                                                                                                                            |
| seed_valid_d      | logic                                                             |                                                                                                                            |
| seed_valid_q      | logic                                                             |                                                                                                                            |
| key_out_d         | logic [ScrmblKeyWidth/ScrmblBlockWidth-1:0][ScrmblBlockWidth-1:0] |                                                                                                                            |
| key_out_q         | logic [ScrmblKeyWidth/ScrmblBlockWidth-1:0][ScrmblBlockWidth-1:0] |                                                                                                                            |
| nonce_out_d       | logic [NumNonceChunks-1:0][ScrmblBlockWidth-1:0]                  |                                                                                                                            |
| nonce_out_q       | logic [NumNonceChunks-1:0][ScrmblBlockWidth-1:0]                  |                                                                                                                            |
| data_sel          | data_sel_e                                                        | Select correct 64bit block.                                                                                                |
| state_d           | state_e                                                           |                                                                                                                            |
| state_q           | state_e                                                           |                                                                                                                            |
| edn_req_d         | logic                                                             |                                                                                                                            |
| edn_req_q         | logic                                                             |                                                                                                                            |
| state_raw_q       | logic [StateWidth-1:0]                                            | This primitive is used to place a size-only constraint on the flops in order to prevent FSM state encoding optimizations.  |
## Constants

| Name          | Type | Value                             | Description                 |
| ------------- | ---- | --------------------------------- | --------------------------- |
| NumReq        | int  | 3 + NumSramKeyReqSlots            | 2xFlash, OTBN + SRAM slots  |
| OtbnNonceSel  | int  | OtbnNonceWidth / ScrmblBlockWidth |                             |
| FlashNonceSel | int  | FlashKeyWidth / ScrmblBlockWidth  |                             |
| SramNonceSel  | int  | SramNonceWidth / ScrmblBlockWidth |                             |
| StateWidth    | int  | 10                                |                             |
## Types

| Name         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| req_bundle_t | struct packed {<br><span style="padding-left:20px">     logic                             ingest_entropy;<br><span style="padding-left:20px">      logic                             chained_digest;<br><span style="padding-left:20px">      digest_sel_e                      digest_sel;<br><span style="padding-left:20px">          logic                             fetch_nonce;<br><span style="padding-left:20px">         logic [1:0]                       nonce_size;<br><span style="padding-left:20px">          logic                             seed_valid;<br><span style="padding-left:20px">          logic [3:0][ScrmblBlockWidth-1:0] seed;<br><span style="padding-left:20px">              }                                                                                                                                                | The configuration options are set further below, depending on the request type.  |
| data_sel_e   | enum logic {<br><span style="padding-left:20px">     SeedData,<br><span style="padding-left:20px">     EntropyData   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                  |
| state_e      | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     ResetSt        = 10'b0111100000,<br><span style="padding-left:20px">     IdleSt         = 10'b0001111101,<br><span style="padding-left:20px">     DigClrSt       = 10'b1101101011,<br><span style="padding-left:20px">     DigLoadSt      = 10'b0100011010,<br><span style="padding-left:20px">     FetchEntropySt = 10'b0010001001,<br><span style="padding-left:20px">     DigEntropySt   = 10'b0110110111,<br><span style="padding-left:20px">     DigFinSt       = 10'b0001000110,<br><span style="padding-left:20px">     DigWaitSt      = 10'b1100000101,<br><span style="padding-left:20px">     FetchNonceSt   = 10'b1010101110,<br><span style="padding-left:20px">     FinishSt       = 10'b1111011100,<br><span style="padding-left:20px">     ErrorSt        = 10'b1011010011   } |                                                                                  |
## Processes
- p_outregs: (  )
- p_fsm: (  )
- p_regs: ( @(posedge clk_i or negedge rst_ni) )
## Instantiations

- u_state_regs: prim_flop
