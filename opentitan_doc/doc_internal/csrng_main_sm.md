# Entity: csrng_main_sm

## Diagram

![Diagram](csrng_main_sm.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: csrng app cmd request state machine module
  - handles all app cmd requests from all requesting interfaces
 
## Ports

| Port name              | Direction | Type  | Description |
| ---------------------- | --------- | ----- | ----------- |
| clk_i                  | input     |       |             |
| rst_ni                 | input     |       |             |
| enable_i               | input     |       |             |
| acmd_avail_i           | input     |       |             |
| acmd_accept_o          | output    |       |             |
| acmd_hdr_capt_o        | output    |       |             |
| acmd_i                 | input     | [2:0] |             |
| acmd_eop_i             | input     |       |             |
| ctr_drbg_cmd_req_rdy_i | input     |       |             |
| flag0_i                | input     |       |             |
| cmd_entropy_req_o      | output    |       |             |
| cmd_entropy_avail_i    | input     |       |             |
| instant_req_o          | output    |       |             |
| reseed_req_o           | output    |       |             |
| generate_req_o         | output    |       |             |
| update_req_o           | output    |       |             |
| uninstant_req_o        | output    |       |             |
| cmd_complete_i         | input     |       |             |
| halt_main_sm_i         | input     |       |             |
| main_sm_halted_o       | output    |       |             |
| main_sm_err_o          | output    |       |             |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| state_d     | state_e                |             |
| state_q     | state_e                |             |
| state_raw_q | logic [StateWidth-1:0] |             |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| StateWidth | int  | 8     |             |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_e | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     Idle    =      8'b00111111,<br><span style="padding-left:20px">      InstantPrep  = 8'b11101010,<br><span style="padding-left:20px">      InstantReq   = 8'b10011100,<br><span style="padding-left:20px">      ReseedPrep   = 8'b00100100,<br><span style="padding-left:20px">      ReseedReq    = 8'b11110101,<br><span style="padding-left:20px">      GenerateReq  = 8'b10000011,<br><span style="padding-left:20px">      UpdatePrep   = 8'b10111001,<br><span style="padding-left:20px">      UpdateReq    = 8'b00001101,<br><span style="padding-left:20px">      UninstantReq = 8'b11011111,<br><span style="padding-left:20px">      CmdCompWait  = 8'b00010000,<br><span style="padding-left:20px">      SMHalted     = 8'b01010011,<br><span style="padding-left:20px">      Error        = 8'b01111000     } |             |
## Processes
- unnamed: (  )
## Instantiations

- u_state_regs: prim_flop
**Description**
This primitive is used to place a size-only constraint on the
flops in order to prevent FSM state encoding optimizations.

