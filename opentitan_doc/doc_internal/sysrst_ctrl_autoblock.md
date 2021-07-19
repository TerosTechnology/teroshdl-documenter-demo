# Entity: sysrst_ctrl_autoblock

- **File**: sysrst_ctrl_autoblock.sv
## Diagram

![Diagram](sysrst_ctrl_autoblock.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description sysrst_ctrl PWRB autoblock module
 
## Ports

| Port name                 | Direction | Type                                             | Description |
| ------------------------- | --------- | ------------------------------------------------ | ----------- |
| clk_aon_i                 | input     |                                                  |             |
| rst_aon_ni                | input     |                                                  |             |
| clk_i                     | input     |                                                  |             |
| rst_ni                    | input     |                                                  |             |
| pwrb_int                  | input     |                                                  |             |
| key0_int                  | input     |                                                  |             |
| key1_int                  | input     |                                                  |             |
| key2_int                  | input     |                                                  |             |
| auto_block_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_auto_block_debounce_ctl_reg_t |             |
| auto_block_out_ctl_i      | input     | sysrst_ctrl_reg2hw_auto_block_out_ctl_reg_t      |             |
| pwrb_out_hw               | output    |                                                  |             |
| key0_out_hw               | output    |                                                  |             |
| key1_out_hw               | output    |                                                  |             |
| key2_out_hw               | output    |                                                  |             |
## Signals

| Name                     | Type         | Description |
| ------------------------ | ------------ | ----------- |
| cfg_auto_block_en        | logic        |             |
| load_auto_block_timer    | logic        |             |
| cfg_auto_block_timer     | logic [15:0] |             |
| cfg_auto_block_timer_d   | logic [15:0] |             |
| cfg_key0_o_sel           | logic        |             |
| cfg_key1_o_sel           | logic        |             |
| cfg_key2_o_sel           | logic        |             |
| cfg_key0_o_q             | logic        |             |
| cfg_key1_o_q             | logic        |             |
| cfg_key2_o_q             | logic        |             |
| ab_cond_met              | logic        |             |
| pwrb_int_i               | logic        |             |
| unused_auto_block_enable | logic        |             |
## Processes
- i_cfg_auto_block_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
## Instantiations

- i_cfg_auto_block_en: prim_flop_2sync
- i_cfg_auto_block_timer: prim_fifo_async
- i_cfg_key0_o_sel: prim_flop_2sync
- i_cfg_key1_o_sel: prim_flop_2sync
- i_cfg_key2_o_sel: prim_flop_2sync
- i_cfg_key0_o_q: prim_flop_2sync
- i_cfg_key1_o_q: prim_flop_2sync
- i_cfg_key2_o_q: prim_flop_2sync
- i_pwrb_in_i: prim_flop_2sync
- i_ab_fsm: sysrst_ctrl_timerfsm
