# Entity: csrng_main_sm

- **File**: csrng_main_sm.sv
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
| clr_adata_packer_o     | output    |       |             |
| cmd_complete_i         | input     |       |             |
| main_sm_err_o          | output    |       |             |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| state_d     | state_e                |             |
| state_q     | state_e                |             |
| state_raw_q | logic [StateWidth-1:0] |             |
## Constants

| Name       | Type | Value | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------- | ---- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| StateWidth | int  | 8     |  Encoding generated with:  $ ./util/design/sparse-fsm-encode.py -d 3 -m 15 -n 8 \       -s 1300573258 --language=sv<br>  Hamming distance histogram:<br>   0: --   1: --   2: --   3: |||||||||||||||||| (32.38%)   4: |||||||||||||||||||| (35.24%)   5: |||||||| (15.24%)   6: |||||| (11.43%)   7: ||| (5.71%)   8: --<br>  Minimum Hamming distance: 3  Maximum Hamming distance: 7  Minimum Hamming weight: 1  Maximum Hamming weight: 7<br>  |
## Types

| Name    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| state_e | enum logic [StateWidth-1:0] {<br><span style="padding-left:20px">     Idle          = 8'b01001110,<br><span style="padding-left:20px">      ParseCmd      = 8'b10111011,<br><span style="padding-left:20px">      InstantPrep   = 8'b11000001,<br><span style="padding-left:20px">      InstantReq    = 8'b01010100,<br><span style="padding-left:20px">      ReseedPrep    = 8'b11011101,<br><span style="padding-left:20px">      ReseedReq     = 8'b01011011,<br><span style="padding-left:20px">      GeneratePrep  = 8'b11101111,<br><span style="padding-left:20px">      GenerateReq   = 8'b00100100,<br><span style="padding-left:20px">      UpdatePrep    = 8'b00110001,<br><span style="padding-left:20px">      UpdateReq     = 8'b10010000,<br><span style="padding-left:20px">      UninstantPrep = 8'b11110110,<br><span style="padding-left:20px">      UninstantReq  = 8'b01100011,<br><span style="padding-left:20px">      ClrAData      = 8'b00000010,<br><span style="padding-left:20px">      CmdCompWait   = 8'b10111100,<br><span style="padding-left:20px">      Error         = 8'b01111000     } |             |
## Processes
- unnamed: (  )
  - **Type:** always_comb
## Instantiations

- u_state_regs: prim_flop
</br>**Description**
 This primitive is used to place a size-only constraint on the
 flops in order to prevent FSM state encoding optimizations.

