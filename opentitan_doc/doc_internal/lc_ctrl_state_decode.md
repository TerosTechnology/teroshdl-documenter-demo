# Entity: lc_ctrl_state_decode

- **File**: lc_ctrl_state_decode.sv
## Diagram

![Diagram](lc_ctrl_state_decode.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Life cycle state decoder. This is a purely combinational module.

## Ports

| Port name             | Direction | Type              | Description               |
| --------------------- | --------- | ----------------- | ------------------------- |
| lc_state_valid_i      | input     |                   |  Life cycle state vector. |
| lc_state_i            | input     | lc_state_e        |                           |
| lc_cnt_i              | input     | lc_cnt_e          |                           |
| secrets_valid_i       | input     | lc_tx_t           |                           |
| fsm_state_i           | input     | fsm_state_e       |  Main FSM state.          |
| dec_lc_state_o        | output    | dec_lc_state_e    |  Decoded state vector.    |
| dec_lc_id_state_o     | output    | dec_lc_id_state_e |                           |
| dec_lc_cnt_o          | output    | dec_lc_cnt_t      |                           |
| state_invalid_error_o | output    | [5:0]             |                           |
## Processes
- p_lc_state_decode: (  )
  - **Type:** always_comb
**Description**
////////////////////////  Signal Decoder Logic // ////////////////////////  The decoder logic below decodes the life cycle state vector and counter  into a format that can be exposed in the CSRs. If the state is invalid,  this will be flagged as well. 
