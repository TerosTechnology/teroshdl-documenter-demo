# Entity: sysrst_ctrl_comboact

## Diagram

![Diagram](sysrst_ctrl_comboact.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: sysrst_ctrl combo action Module
 
## Ports

| Port name          | Direction | Type                                | Description |
| ------------------ | --------- | ----------------------------------- | ----------- |
| clk_aon_i          | input     |                                     |             |
| rst_aon_ni         | input     |                                     |             |
| clk_i              | input     |                                     |             |
| rst_ni             | input     |                                     |             |
| cfg_intr_en        | input     |                                     |             |
| cfg_bat_disable_en | input     |                                     |             |
| cfg_ec_rst_en      | input     |                                     |             |
| cfg_gsc_rst_en     | input     |                                     |             |
| combo_det          | input     |                                     |             |
| ec_rst_l_i         | input     |                                     |             |
| ec_rst_ctl_i       | input     | sysrst_ctrl_reg2hw_ec_rst_ctl_reg_t |             |
| combo_intr_pulse   | output    |                                     |             |
| bat_disable_o      | output    |                                     |             |
| gsc_rst_o          | output    |                                     |             |
| ec_rst_l_o         | output    |                                     |             |
## Signals

| Name                    | Type         | Description |
| ----------------------- | ------------ | ----------- |
| cfg_ec_rst_timer        | logic [15:0] |             |
| load_ec_rst_timer       | logic        |             |
| cfg_ec_rst_timer_d      | logic [15:0] |             |
| combo_det_q             | logic        |             |
| combo_gsc_pulse         | logic        |             |
| combo_bat_disable_pulse | logic        |             |
| bat_disable_q           | logic        |             |
| bat_disable_d           | logic        |             |
| gsc_rst_q               | logic        |             |
| gsc_rst_d               | logic        |             |
| combo_ec_rst_pulse      | logic        |             |
| ec_rst_l_q              | logic        |             |
| ec_rst_l_d              | logic        |             |
| timer_cnt_d             | logic [15:0] |             |
| timer_cnt_q             | logic [15:0] |             |
| timer_cnt_clr           | logic        |             |
| timer_cnt_en            | logic        |             |
| ec_rst_l_int            | logic        |             |
| ec_rst_l_det            | logic        |             |
## Processes
- i_combo_det: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_combo_bat_disable: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_cfg_ec_rst_timer_reg: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_ec_rst_l_int: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_combo_ec_rst_l: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- timer_cnt_regs: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
- i_combo_gsc_rst: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
## Instantiations

- i_cfg_ec_rst_pulse: prim_fifo_async
