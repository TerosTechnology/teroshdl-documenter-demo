# Entity: sysrst_ctrl_ulp

- **File**: sysrst_ctrl_ulp.sv
## Diagram

![Diagram](sysrst_ctrl_ulp.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description sysrst_ctrl ULP module

## Ports

| Port name               | Direction | Type                                           | Description                                       |
| ----------------------- | --------- | ---------------------------------------------- | ------------------------------------------------- |
| clk_i                   | input     |                                                |                                                   |
| rst_ni                  | input     |                                                |                                                   |
| lid_open_int_i          | input     |                                                |  (Optionally) inverted input signals on AON clock |
| ac_present_int_i        | input     |                                                |                                                   |
| pwrb_int_i              | input     |                                                |                                                   |
| ulp_ac_debounce_ctl_i   | input     | sysrst_ctrl_reg2hw_ulp_ac_debounce_ctl_reg_t   |  CSRs synced to AON clock                         |
| ulp_lid_debounce_ctl_i  | input     | sysrst_ctrl_reg2hw_ulp_lid_debounce_ctl_reg_t  |                                                   |
| ulp_pwrb_debounce_ctl_i | input     | sysrst_ctrl_reg2hw_ulp_pwrb_debounce_ctl_reg_t |                                                   |
| ulp_ctl_i               | input     | sysrst_ctrl_reg2hw_ulp_ctl_reg_t               |                                                   |
| ulp_status_o            | output    | sysrst_ctrl_hw2reg_ulp_status_reg_t            |                                                   |
| ulp_wakeup_pulse_o      | output    |                                                |  Wakeup pulses on AON clock                       |
| z3_wakeup_hw_o          | output    |                                                |                                                   |
## Signals

| Name                  | Type  | Description |
| --------------------- | ----- | ----------- |
| pwrb_cond_met_d       | logic |             |
| pwrb_cond_met_q       | logic |             |
| lid_open_cond_met_d   | logic |             |
| lid_open_cond_met_q   | logic |             |
| ac_present_cond_met_d | logic |             |
| ac_present_cond_met_q | logic |             |
| pwrb_det_pulse        | logic |             |
| lid_open_det_pulse    | logic |             |
| ac_present_det_pulse  | logic |             |
## Processes
- p_ulp_cond_met: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
</br>**Description**
 delay the level signal to generate a pulse 
## Instantiations

- u_pwrb_ulpfsm: sysrst_ctrl_ulpfsm
- u_lid_open_ulpfsm: sysrst_ctrl_ulpfsm
- u_ac_present_ulpfsm: sysrst_ctrl_ulpfsm
