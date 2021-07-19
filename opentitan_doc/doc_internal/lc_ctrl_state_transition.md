# Entity: lc_ctrl_state_transition

- **File**: lc_ctrl_state_transition.sv
## Diagram

![Diagram](lc_ctrl_state_transition.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Life cycle state transition function. Checks whether a transition is valid
 and computes the target state. This module is purely combinational.
 
## Ports

| Port name              | Direction | Type           | Description                            |
| ---------------------- | --------- | -------------- | -------------------------------------- |
| lc_state_i             | input     | lc_state_e     | Life cycle state vector.               |
| lc_cnt_i               | input     | lc_cnt_e       |                                        |
| fsm_state_i            | input     | fsm_state_e    | Main FSM state.                        |
| dec_lc_state_i         | input     | dec_lc_state_e | Decoded lc state input                 |
| trans_target_i         | input     | dec_lc_state_e | Transition target.                     |
| next_lc_state_o        | output    | lc_state_e     | Updated state vector.                  |
| next_lc_cnt_o          | output    | lc_cnt_e       |                                        |
| trans_cnt_oflw_error_o | output    |                | If the transition counter is maxed out |
| trans_invalid_error_o  | output    |                |                                        |
## Processes
- p_lc_state_transition: (  )
**Description**
The decoder logic below checks whether a given transition edge
is valid and computes the next lc counter ans state vectors.

