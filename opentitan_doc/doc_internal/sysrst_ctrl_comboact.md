# Entity: sysrst_ctrl_comboact

- **File**: sysrst_ctrl_comboact.sv
## Diagram

![Diagram](sysrst_ctrl_comboact.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: sysrst_ctrl combo action Module


## Ports

| Port name            | Direction | Type                                | Description |
| -------------------- | --------- | ----------------------------------- | ----------- |
| clk_i                | input     |                                     |             |
| rst_ni               | input     |                                     |             |
| combo_det_i          | input     |                                     |             |
| ec_rst_l_i           | input     |                                     |             |
| cfg_bat_disable_en_i | input     |                                     |             |
| cfg_ec_rst_en_i      | input     |                                     |             |
| cfg_rst_req_en_i     | input     |                                     |             |
| cfg_intr_en_i        | input     |                                     |             |
| ec_rst_ctl_i         | input     | sysrst_ctrl_reg2hw_ec_rst_ctl_reg_t |             |
| combo_intr_pulse_o   | output    |                                     |             |
| bat_disable_o        | output    |                                     |             |
| rst_req_o            | output    |                                     |             |
| ec_rst_l_o           | output    |                                     |             |
## Signals

| Name                    | Type                   | Description                                                                                                                                        |
| ----------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| combo_det_pulse         | logic                  | /////////////////////////////////////  Combo / EC reset detection Pulses // /////////////////////////////////////  generate combo detection pulse  |
| combo_det_q             | logic                  | /////////////////////////////////////  Combo / EC reset detection Pulses // /////////////////////////////////////  generate combo detection pulse  |
| combo_bat_disable_pulse | logic                  |  mask combo detection pulse with config bits                                                                                                       |
| combo_gsc_pulse         | logic                  |  mask combo detection pulse with config bits                                                                                                       |
| combo_ec_rst_pulse      | logic                  |  mask combo detection pulse with config bits                                                                                                       |
| ec_rst_l_det_pulse      | logic                  | ec_rst_l_i high->low detection                                                                                                                     |
| ec_rst_l_det_q          | logic                  | ec_rst_l_i high->low detection                                                                                                                     |
| bat_disable_q           | logic                  | //////////////////////////////////  Bat / GSC reset pulse latching // //////////////////////////////////                                           |
| bat_disable_d           | logic                  | //////////////////////////////////  Bat / GSC reset pulse latching // //////////////////////////////////                                           |
| rst_req_q               | logic                  |                                                                                                                                                    |
| rst_req_d               | logic                  |                                                                                                                                                    |
| timer_expired           | logic                  | //////////////////  EC reset logic // //////////////////  GSC reset will also reset EC                                                             |
| ec_rst_l_q              | logic                  |                                                                                                                                                    |
| ec_rst_l_d              | logic                  |                                                                                                                                                    |
| timer_cnt_d             | logic [TimerWidth-1:0] |  Reset stretching counter                                                                                                                          |
| timer_cnt_q             | logic [TimerWidth-1:0] |  Reset stretching counter                                                                                                                          |
## Processes
- p_regs: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
</br>**Description**
/////////////  Registers // ///////////// 
