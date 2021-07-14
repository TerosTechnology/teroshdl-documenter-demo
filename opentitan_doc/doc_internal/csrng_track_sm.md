# Entity: csrng_track_sm

## Diagram

![Diagram](csrng_track_sm.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: csrng command tracking state machine module
   provides debugging of command flow through csrng
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Cmd          | int  | 3     |             |
| StateId      | int  | 4     |             |
## Ports

| Port name               | Direction | Type          | Description       |
| ----------------------- | --------- | ------------- | ----------------- |
| clk_i                   | input     |               |                   |
| rst_ni                  | input     |               |                   |
| inst_id_i               | input     | [StateId-1:0] | ins req interface |
| acmd_hdr_capt_i         | input     |               |                   |
| acmd_i                  | input     | [Cmd-1:0]     |                   |
| shid_i                  | input     | [StateId-1:0] |                   |
| ctr_drbg_cmd_req_i      | input     |               |                   |
| ctr_drbg_cmd_req_rdy_i  | input     |               |                   |
| ctr_drbg_cmd_ccmd_i     | input     | [Cmd-1:0]     |                   |
| ctr_drbg_cmd_inst_id_i  | input     | [StateId-1:0] |                   |
| updblk_arb_vld_i        | input     |               |                   |
| updblk_arb_rdy_i        | input     |               |                   |
| updblk_arb_ccmd_i       | input     | [Cmd-1:0]     |                   |
| updblk_arb_inst_id_i    | input     | [StateId-1:0] |                   |
| benblk_arb_vld_i        | input     |               |                   |
| benblk_arb_rdy_i        | input     |               |                   |
| benblk_arb_ccmd_i       | input     | [Cmd-1:0]     |                   |
| benblk_arb_inst_id_i    | input     | [StateId-1:0] |                   |
| benblk_updblk_ack_i     | input     |               |                   |
| updblk_benblk_ack_rdy_i | input     |               |                   |
| benblk_cmd_i            | input     | [Cmd-1:0]     |                   |
| benblk_inst_id_i        | input     | [StateId-1:0] |                   |
| updblk_cmdblk_ack_i     | input     |               |                   |
| cmdblk_updblk_ack_rdy_i | input     |               |                   |
| updblk_cmdblk_ccmd_i    | input     | [Cmd-1:0]     |                   |
| updblk_cmdblk_inst_id_i | input     | [StateId-1:0] |                   |
| ctr_drbg_gen_req_i      | input     |               |                   |
| ctr_drbg_gen_req_rdy_i  | input     |               |                   |
| ctr_drbg_gen_ccmd_i     | input     | [Cmd-1:0]     |                   |
| ctr_drbg_gen_inst_id_i  | input     | [StateId-1:0] |                   |
| benblk_genblk_ack_i     | input     |               |                   |
| genblk_benblk_ack_rdy_i | input     |               |                   |
| updblk_genblk_ack_i     | input     |               |                   |
| genblk_updblk_ack_rdy_i | input     |               |                   |
| updblk_ccmd_i           | input     | [Cmd-1:0]     |                   |
| updblk_inst_id_i        | input     | [StateId-1:0] |                   |
| state_db_wr_req_i       | input     |               |                   |
| state_db_wr_req_rdy_i   | input     |               |                   |
| genbits_stage_vld_i     | input     |               |                   |
| genbits_stage_rdy_i     | input     |               |                   |
| state_db_wr_ccmd_i      | input     | [Cmd-1:0]     |                   |
| state_db_wr_inst_id_i   | input     | [StateId-1:0] |                   |
| cmd_core_ack_i          | input     |               |                   |
| cmd_stage_ack_i         | input     |               |                   |
| track_sm_o              | output    | [7:0]         |                   |
## Signals

| Name             | Type                   | Description |
| ---------------- | ---------------------- | ----------- |
| ben_ack_cntr_inc | logic                  | signals     |
| ben_ack_cntr_clr | logic                  |             |
| ben_ack_cntr_q   | logic [1:0]            | flops       |
| ben_ack_cntr_d   | logic [1:0]            | flops       |
| state_d          | state_e                |             |
| state_q          | state_e                |             |
| state_raw_q      | logic [StateWidth-1:0] |             |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| StateWidth | int  | 8     |             |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| state_e | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     Idle           = 8'h00,<br><span style="padding-left:20px">     InsCmdCap      = 8'h11,<br><span style="padding-left:20px">     InsDrbgCmdIn   = 8'h12,<br><span style="padding-left:20px">     InsDrbgUpdIn   = 8'h13,<br><span style="padding-left:20px">     InsBlkEncIn    = 8'h14,<br><span style="padding-left:20px">     InsDrbgCmdRtn  = 8'h15,<br><span style="padding-left:20px">     InsStateDBIn   = 8'h16,<br><span style="padding-left:20px">     InsCmdStageRtn = 8'h17,<br><span style="padding-left:20px">     InsAppCmdBus   = 8'h18,<br><span style="padding-left:20px">      ResCmdCap      = 8'h21,<br><span style="padding-left:20px">     ResDrbgCmdIn   = 8'h22,<br><span style="padding-left:20px">     ResDrbgUpdIn   = 8'h23,<br><span style="padding-left:20px">     ResBlkEncIn    = 8'h24,<br><span style="padding-left:20px">     ResDrbgCmdRtn  = 8'h25,<br><span style="padding-left:20px">     ResStateDBIn   = 8'h26,<br><span style="padding-left:20px">     ResCmdStageRtn = 8'h27,<br><span style="padding-left:20px">     ResAppCmdBus   = 8'h28,<br><span style="padding-left:20px">      GenCmdCap      = 8'h31,<br><span style="padding-left:20px">     GenDrbgCmdIn   = 8'h32,<br><span style="padding-left:20px">     GenDrbgUpd1In  = 8'h33,<br><span style="padding-left:20px">     GenBlkEnc1In   = 8'h34,<br><span style="padding-left:20px">     GenDrbgUpd1Rtn = 8'h35,<br><span style="padding-left:20px">     GenDrbgCmd1Rtn = 8'h36,<br><span style="padding-left:20px">     GenDrbgGenIn   = 8'h37,<br><span style="padding-left:20px">     GenDrbgUpd2In  = 8'h38,<br><span style="padding-left:20px">     GenBlkEnc2In   = 8'h39,<br><span style="padding-left:20px">     GenDrbgUpd2Rtn = 8'h3a,<br><span style="padding-left:20px">     GenDrbgGen1Rtn = 8'h3b,<br><span style="padding-left:20px">     GenBlkEnc3In   = 8'h3c,<br><span style="padding-left:20px">     GenDrbgGen2Rtn = 8'h3d,<br><span style="padding-left:20px">     GenStateDBIn   = 8'h3e,<br><span style="padding-left:20px">     GenAppCmdBus   = 8'h3f,<br><span style="padding-left:20px">      UpdCmdCap      = 8'h41,<br><span style="padding-left:20px">     UpdDrbgCmdIn   = 8'h42,<br><span style="padding-left:20px">     UpdDrbgUpdIn   = 8'h43,<br><span style="padding-left:20px">     UpdBlkEncIn    = 8'h44,<br><span style="padding-left:20px">     UpdDrbgCmdRtn  = 8'h45,<br><span style="padding-left:20px">     UpdStateDBIn   = 8'h46,<br><span style="padding-left:20px">     UpdCmdStageRtn = 8'h47,<br><span style="padding-left:20px">     UpdAppCmdBus   = 8'h48,<br><span style="padding-left:20px">      UniCmdCap      = 8'h51,<br><span style="padding-left:20px">     UniDrbgCmdIn   = 8'h52,<br><span style="padding-left:20px">     UniDrbgUpdIn   = 8'h53,<br><span style="padding-left:20px">     UniBlkEncIn    = 8'h54,<br><span style="padding-left:20px">     UniDrbgCmdRtn  = 8'h55,<br><span style="padding-left:20px">     UniStateDBIn   = 8'h56,<br><span style="padding-left:20px">     UniCmdStageRtn = 8'h57,<br><span style="padding-left:20px">     UniAppCmdBus   = 8'h58   } |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
## Instantiations

- u_state_regs: prim_flop
**Description**
This primitive is used to place a size-only constraint on the
flops in order to prevent FSM state encoding optimizations.

