# Entity: aon_timer

- **File**: aon_timer.sv
## Diagram

![Diagram](aon_timer.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Generics

| Generic name | Type                  | Value     | Description |
| ------------ | --------------------- | --------- | ----------- |
| NumAlerts    | logic [NumAlerts-1:0] | undefined |             |
## Ports

| Port name                 | Direction | Type            | Description                     |
| ------------------------- | --------- | --------------- | ------------------------------- |
| clk_i                     | input     |                 |                                 |
| clk_aon_i                 | input     |                 |                                 |
| rst_ni                    | input     |                 |                                 |
| rst_aon_ni                | input     |                 |                                 |
| tl_i                      | input     |                 |  TLUL interface on clk_i domain |
| tl_o                      | output    |                 |                                 |
| alert_rx_i                | input     | [NumAlerts-1:0] |  Alerts                         |
| alert_tx_o                | output    | [NumAlerts-1:0] |                                 |
| lc_escalate_en_i          | input     |                 |  clk_i domain                   |
| intr_wkup_timer_expired_o | output    |                 |                                 |
| intr_wdog_timer_bark_o    | output    |                 |                                 |
| nmi_wdog_timer_bark_o     | output    |                 |                                 |
| aon_timer_wkup_req_o      | output    |                 |  clk_aon_i domain               |
| aon_timer_rst_req_o       | output    |                 |                                 |
| sleep_mode_i              | input     |                 |  async domain                   |
## Signals

| Name                   | Type                       | Description                                                                             |
| ---------------------- | -------------------------- | --------------------------------------------------------------------------------------- |
| reg2hw                 | aon_timer_reg2hw_t         |  Register structs                                                                       |
| hw2reg                 | aon_timer_hw2reg_t         |                                                                                         |
| aon_wkup_count_reg_wr  | logic                      |  Register write signals                                                                 |
| aon_wkup_count_wr_data | logic [31:0]               |                                                                                         |
| aon_wdog_count_reg_wr  | logic                      |                                                                                         |
| aon_wdog_count_wr_data | logic [31:0]               |                                                                                         |
| lc_escalate_en         | lc_ctrl_pkg::lc_tx_t [2:0] |  Other sync signals                                                                     |
| aon_wkup_intr_set      | logic                      |  Interrupt signals                                                                      |
| aon_wdog_intr_set      | logic                      |                                                                                         |
| intr_test_q            | logic [1:0]                |                                                                                         |
| intr_test_qe           | logic                      |                                                                                         |
| intr_state_q           | logic [1:0]                |                                                                                         |
| intr_state_de          | logic                      |                                                                                         |
| intr_state_d           | logic [1:0]                |                                                                                         |
| intr_out               | logic [1:0]                |                                                                                         |
| aon_rst_req_set        | logic                      |  Reset signals                                                                          |
| aon_rst_req_d          | logic                      |                                                                                         |
| aon_rst_req_q          | logic                      |                                                                                         |
| alert_test             | logic [NumAlerts-1:0]      |  Alert signals                                                                          |
| alerts                 | logic [NumAlerts-1:0]      |  Alert signals                                                                          |
| aon_sleep_mode         | logic                      | ////////////////////////////  Register Write Interface // ////////////////////////////  |
| aon_intr_set           | logic [1:0]                |                                                                                         |
| intr_set               | logic [1:0]                |                                                                                         |
## Constants

| Name     | Type | Value | Description |
| -------- | ---- | ----- | ----------- |
| AON_WKUP | int  | 0     |             |
| AON_WDOG | int  | 1     |             |
## Processes
- unnamed: ( @(posedge clk_aon_i or negedge rst_aon_ni) )
  - **Type:** always_ff
## Instantiations

- u_sync_sleep_mode: prim_flop_2sync
- u_reg: aon_timer_reg_top
**Description**
 registers instantiation

- u_lc_sync_escalate_en: prim_lc_sync
**Description**
 Lifecycle sync

- u_core: aon_timer_core
**Description**
//////////////
 Timer Core //
//////////////

- u_intr_hw: prim_intr_hw
