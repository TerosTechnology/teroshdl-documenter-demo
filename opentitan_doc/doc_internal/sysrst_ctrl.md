# Entity: sysrst_ctrl

- **File**: sysrst_ctrl.sv
## Diagram

![Diagram](sysrst_ctrl.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 sysrst_ctrl module

## Generics

| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports

| Port name                  | Direction | Type            | Description                                                          |
| -------------------------- | --------- | --------------- | -------------------------------------------------------------------- |
| clk_i                      | input     |                 | Always-on 24MHz clock(config)                                        |
| clk_aon_i                  | input     |                 | Always-on 200KHz clock(logic)                                        |
| rst_ni                     | input     |                 | power-on reset for the 24MHz clock(config)                           |
| rst_aon_ni                 | input     |                 | power-on reset for the 200KHz clock(logic)                           |
| tl_i                       | input     |                 |  Register interface                                                  |
| tl_o                       | output    |                 |                                                                      |
| alert_rx_i                 | input     | [NumAlerts-1:0] |  Alerts                                                              |
| alert_tx_o                 | output    | [NumAlerts-1:0] |                                                                      |
| aon_sysrst_ctrl_wkup_req_o | output    |                 | OT wake to pwrmgr                                                    |
| aon_sysrst_ctrl_rst_req_o  | output    |                 | OT reset to rstmgr                                                   |
| intr_sysrst_ctrl_o         | output    |                 | sysrst_ctrl interrupt to PLIC                                        |
| cio_ac_present_i           | input     |                 | AC power is present                                                  |
| cio_ec_rst_l_i             | input     |                 | EC reset is asserted by some other system agent                      |
| cio_key0_in_i              | input     |                 | VolUp button in tablet; column output from the EC in a laptop        |
| cio_key1_in_i              | input     |                 | VolDown button in tablet; row input from keyboard matrix in a laptop |
| cio_key2_in_i              | input     |                 | TBD button in tablet; row input from keyboard matrix in a laptop     |
| cio_pwrb_in_i              | input     |                 | Power button in both tablet and laptop                               |
| cio_lid_open_i             | input     |                 | lid is open from GMR                                                 |
| cio_bat_disable_o          | output    |                 | Battery is disconnected                                              |
| cio_flash_wp_l_o           | output    |                 | Flash write protect is asserted by sysrst_ctrl                       |
| cio_ec_rst_l_o             | output    |                 | EC reset is asserted by sysrst_ctrl                                  |
| cio_key0_out_o             | output    |                 | Passthrough from key0_in, can be configured to invert                |
| cio_key1_out_o             | output    |                 | Passthrough from key1_in, can be configured to invert                |
| cio_key2_out_o             | output    |                 | Passthrough from key2_in, can be configured to invert                |
| cio_pwrb_out_o             | output    |                 | Passthrough from pwrb_in, can be configured to invert                |
| cio_z3_wakeup_o            | output    |                 | Exit from Z4 sleep mode and enter Z3 mode                            |
| cio_bat_disable_en_o       | output    |                 |                                                                      |
| cio_flash_wp_l_en_o        | output    |                 |                                                                      |
| cio_ec_rst_l_en_o          | output    |                 |                                                                      |
| cio_key0_out_en_o          | output    |                 |                                                                      |
| cio_key1_out_en_o          | output    |                 |                                                                      |
| cio_key2_out_en_o          | output    |                 |                                                                      |
| cio_pwrb_out_en_o          | output    |                 |                                                                      |
| cio_z3_wakeup_en_o         | output    |                 |                                                                      |
## Signals

| Name                       | Type                  | Description                                                                                                                                                                                                                             |
| -------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| reg2hw                     | sysrst_ctrl_reg2hw_t  |                                                                                                                                                                                                                                         |
| hw2reg                     | sysrst_ctrl_hw2reg_t  |                                                                                                                                                                                                                                         |
| alert_test                 | logic [NumAlerts-1:0] |                                                                                                                                                                                                                                         |
| alerts                     | logic [NumAlerts-1:0] |                                                                                                                                                                                                                                         |
| pwrb_int                   | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| key0_int                   | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| key1_int                   | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| key2_int                   | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| ac_present_int             | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| lid_open_int               | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| ec_rst_l_int               | logic                 | /////////////////////////////////////  Input inversion and Synchronizers // /////////////////////////////////////  Optionally invert some of the input signals                                                                          |
| aon_pwrb_int               | logic                 |  Synchronize input signals to AON clock                                                                                                                                                                                                 |
| aon_key0_int               | logic                 |  Synchronize input signals to AON clock                                                                                                                                                                                                 |
| aon_key1_int               | logic                 |  Synchronize input signals to AON clock                                                                                                                                                                                                 |
| aon_key2_int               | logic                 |  Synchronize input signals to AON clock                                                                                                                                                                                                 |
| aon_ac_present_int         | logic                 |                                                                                                                                                                                                                                         |
| aon_lid_open_int           | logic                 |                                                                                                                                                                                                                                         |
| aon_ec_rst_l_int           | logic                 |                                                                                                                                                                                                                                         |
| pwrb_out_hw                | logic                 | /////////////  Autoblock // /////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.                                                  |
| key0_out_hw                | logic                 | /////////////  Autoblock // /////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.                                                  |
| key1_out_hw                | logic                 | /////////////  Autoblock // /////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.                                                  |
| key2_out_hw                | logic                 | /////////////  Autoblock // /////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.                                                  |
| aon_z3_wakeup_hw           | logic                 | ///////  ULP // ///////  This module runs on the AON clock entirely.  Hence, its local signals are not prefixed with aon_*.                                                                                                             |
| aon_ulp_wakeup_pulse_int   | logic                 |                                                                                                                                                                                                                                         |
| aon_sysrst_ctrl_key_intr   | logic                 | ///////////////////////////  Key triggered interrups // ///////////////////////////  This module runs on the AON clock entirely.  Hence, its local signals are not prefixed with aon_*.                                                 |
| aon_sysrst_ctrl_combo_intr | logic                 | ///////////////////  Combo detection // ///////////////////  This module runs on the AON clock entirely.  Hence, its local signals are not prefixed with aon_*.                                                                         |
| aon_bat_disable_hw         | logic                 | ///////////////////  Combo detection // ///////////////////  This module runs on the AON clock entirely.  Hence, its local signals are not prefixed with aon_*.                                                                         |
| aon_ec_rst_l_hw            | logic                 | ///////////////////  Combo detection // ///////////////////  This module runs on the AON clock entirely.  Hence, its local signals are not prefixed with aon_*.                                                                         |
| pwrb_out_int               | logic                 | /////////////////////////////  Pin visibility / override // /////////////////////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.  |
| key0_out_int               | logic                 | /////////////////////////////  Pin visibility / override // /////////////////////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.  |
| key1_out_int               | logic                 | /////////////////////////////  Pin visibility / override // /////////////////////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.  |
| key2_out_int               | logic                 | /////////////////////////////  Pin visibility / override // /////////////////////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.  |
| aon_bat_disable_out_int    | logic                 | /////////////////////////////  Pin visibility / override // /////////////////////////////  This module operates on both synchronized and unsynchronized signals.  I.e., the passthrough signals are NOT synchronnous to the AON clock.  |
| aon_z3_wakeup_out_int      | logic                 |                                                                                                                                                                                                                                         |
| aon_ec_rst_out_int_l       | logic                 |                                                                                                                                                                                                                                         |
| aon_flash_wp_out_int_l     | logic                 |                                                                                                                                                                                                                                         |
| wkup_req                   | logic                 |  sync the wakeup request (level) to bus clock to trigger an IRQ.                                                                                                                                                                        |
## Instantiations

- u_reg: sysrst_ctrl_reg_top
- u_prim_flop_2sync_input: prim_flop_2sync
- u_sysrst_ctrl_autoblock: sysrst_ctrl_autoblock
- u_sysrst_ctrl_ulp: sysrst_ctrl_ulp
- u_sysrst_ctrl_keyintr: sysrst_ctrl_keyintr
- u_sysrst_ctrl_combo: sysrst_ctrl_combo
- u_sysrst_ctrl_pin: sysrst_ctrl_pin
- u_prim_flop_2sync: prim_flop_2sync
- u_prim_intr_hw: prim_intr_hw
</br>**Description**
 Instantiate the interrupt module

