# Entity: ad_tdd_control

- **File**: ad_tdd_control.v
## Diagram

![Diagram](ad_tdd_control.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2017 (c) Analog Devices, Inc. All rights reserved.
 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.
 The user should read each of these license terms, and understand the
 freedoms and responsibilities that he or she has by using this source/core.
 This core is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE.
 Redistribution and use of source or resulting binaries, with or without modification
 of this file, are permitted under one of the following two license terms:
   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory
      of this repository (LICENSE_GPL2), and also online at:
      <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>
 OR
   2. An ADI specific BSD license, which can be found in the top level directory
      of this repository (LICENSE_ADIBSD), and also on-line at:
      https://github.com/analogdevicesinc/hdl/blob/master/LICENSE_ADIBSD
      This will allow to generate bit files and not release the source code,
      as long as it attaches to an ADI device.
 ***************************************************************************
 ***************************************************************************
 
## Generics

| Generic name       | Type    | Value | Description |
| ------------------ | ------- | ----- | ----------- |
| TX_DATA_PATH_DELAY | integer | 0     |             |
| CONTROL_PATH_DELAY | integer | 0     |             |
## Ports

| Port name          | Direction | Type   | Description         |
| ------------------ | --------- | ------ | ------------------- |
| clk                | input     |        | clock and reset     |
| rst                | input     |        |                     |
| tdd_enable         | input     |        | TDD timing signals  |
| tdd_secondary      | input     |        |                     |
| tdd_tx_only        | input     |        |                     |
| tdd_rx_only        | input     |        |                     |
| tdd_burst_count    | input     | [ 7:0] |                     |
| tdd_counter_init   | input     | [23:0] |                     |
| tdd_frame_length   | input     | [23:0] |                     |
| tdd_vco_rx_on_1    | input     | [23:0] |                     |
| tdd_vco_rx_off_1   | input     | [23:0] |                     |
| tdd_vco_tx_on_1    | input     | [23:0] |                     |
| tdd_vco_tx_off_1   | input     | [23:0] |                     |
| tdd_rx_on_1        | input     | [23:0] |                     |
| tdd_rx_off_1       | input     | [23:0] |                     |
| tdd_rx_dp_on_1     | input     | [23:0] |                     |
| tdd_rx_dp_off_1    | input     | [23:0] |                     |
| tdd_tx_on_1        | input     | [23:0] |                     |
| tdd_tx_off_1       | input     | [23:0] |                     |
| tdd_tx_dp_on_1     | input     | [23:0] |                     |
| tdd_tx_dp_off_1    | input     | [23:0] |                     |
| tdd_vco_rx_on_2    | input     | [23:0] |                     |
| tdd_vco_rx_off_2   | input     | [23:0] |                     |
| tdd_vco_tx_on_2    | input     | [23:0] |                     |
| tdd_vco_tx_off_2   | input     | [23:0] |                     |
| tdd_rx_on_2        | input     | [23:0] |                     |
| tdd_rx_off_2       | input     | [23:0] |                     |
| tdd_rx_dp_on_2     | input     | [23:0] |                     |
| tdd_rx_dp_off_2    | input     | [23:0] |                     |
| tdd_tx_on_2        | input     | [23:0] |                     |
| tdd_tx_off_2       | input     | [23:0] |                     |
| tdd_tx_dp_on_2     | input     | [23:0] |                     |
| tdd_tx_dp_off_2    | input     | [23:0] |                     |
| tdd_sync           | input     |        |                     |
| tdd_tx_dp_en       | output    |        | TDD control signals |
| tdd_rx_dp_en       | output    |        |                     |
| tdd_rx_vco_en      | output    |        |                     |
| tdd_tx_vco_en      | output    |        |                     |
| tdd_rx_rf_en       | output    |        |                     |
| tdd_tx_rf_en       | output    |        |                     |
| tdd_counter_status | output    | [23:0] |                     |
## Signals

| Name                        | Type         | Description                              |
| --------------------------- | ------------ | ---------------------------------------- |
| tdd_counter                 | reg   [23:0] | tdd control related tdd counter related  |
| tdd_burst_counter           | reg   [ 5:0] |                                          |
| tdd_cstate                  | reg          |                                          |
| tdd_cstate_next             | reg          |                                          |
| counter_at_tdd_vco_rx_on_1  | reg          |                                          |
| counter_at_tdd_vco_rx_off_1 | reg          |                                          |
| counter_at_tdd_vco_tx_on_1  | reg          |                                          |
| counter_at_tdd_vco_tx_off_1 | reg          |                                          |
| counter_at_tdd_rx_on_1      | reg          |                                          |
| counter_at_tdd_rx_off_1     | reg          |                                          |
| counter_at_tdd_rx_dp_on_1   | reg          |                                          |
| counter_at_tdd_rx_dp_off_1  | reg          |                                          |
| counter_at_tdd_tx_on_1      | reg          |                                          |
| counter_at_tdd_tx_off_1     | reg          |                                          |
| counter_at_tdd_tx_dp_on_1   | reg          |                                          |
| counter_at_tdd_tx_dp_off_1  | reg          |                                          |
| counter_at_tdd_vco_rx_on_2  | reg          |                                          |
| counter_at_tdd_vco_rx_off_2 | reg          |                                          |
| counter_at_tdd_vco_tx_on_2  | reg          |                                          |
| counter_at_tdd_vco_tx_off_2 | reg          |                                          |
| counter_at_tdd_rx_on_2      | reg          |                                          |
| counter_at_tdd_rx_off_2     | reg          |                                          |
| counter_at_tdd_rx_dp_on_2   | reg          |                                          |
| counter_at_tdd_rx_dp_off_2  | reg          |                                          |
| counter_at_tdd_tx_on_2      | reg          |                                          |
| counter_at_tdd_tx_off_2     | reg          |                                          |
| counter_at_tdd_tx_dp_on_2   | reg          |                                          |
| counter_at_tdd_tx_dp_off_2  | reg          |                                          |
| tdd_last_burst              | reg          |                                          |
| tdd_sync_d1                 | reg          |                                          |
| tdd_sync_d2                 | reg          |                                          |
| tdd_sync_d3                 | reg          |                                          |
| tdd_endof_frame             | reg          |                                          |
| tdd_vco_rx_on_1_s           | wire [23:0]  | internal signals                         |
| tdd_vco_rx_off_1_s          | wire [23:0]  |                                          |
| tdd_vco_tx_on_1_s           | wire [23:0]  |                                          |
| tdd_vco_tx_off_1_s          | wire [23:0]  |                                          |
| tdd_rx_on_1_s               | wire [23:0]  |                                          |
| tdd_rx_off_1_s              | wire [23:0]  |                                          |
| tdd_tx_on_1_s               | wire [23:0]  |                                          |
| tdd_tx_off_1_s              | wire [23:0]  |                                          |
| tdd_tx_dp_on_1_s            | wire [23:0]  |                                          |
| tdd_tx_dp_off_1_s           | wire [23:0]  |                                          |
| tdd_vco_rx_on_2_s           | wire [23:0]  |                                          |
| tdd_vco_rx_off_2_s          | wire [23:0]  |                                          |
| tdd_vco_tx_on_2_s           | wire [23:0]  |                                          |
| tdd_vco_tx_off_2_s          | wire [23:0]  |                                          |
| tdd_rx_on_2_s               | wire [23:0]  |                                          |
| tdd_rx_off_2_s              | wire [23:0]  |                                          |
| tdd_tx_on_2_s               | wire [23:0]  |                                          |
| tdd_tx_off_2_s              | wire [23:0]  |                                          |
| tdd_tx_dp_on_2_s            | wire [23:0]  |                                          |
| tdd_tx_dp_off_2_s           | wire [23:0]  |                                          |
| tdd_endof_burst             | wire         |                                          |
| tdd_txrx_only_en_s          | wire         |                                          |
## Constants

| Name | Type   | Value | Description |
| ---- | ------ | ----- | ----------- |
| ON   | [ 0:0] | 1     |             |
| OFF  | [ 0:0] | 0     |             |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
synchronization of tdd_sync

- unnamed: ( @(posedge clk) )
**Description**
***************************************************************************
tdd counter (state machine)
***************************************************************************

- unnamed: ( @* )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
tdd free running counter

- unnamed: ( @(posedge clk) )
**Description**
tdd burst counter

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
***************************************************************************
generate control signals
***************************************************************************
start/stop rx vco

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
start/stop tx vco

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
start/stop rx rf path

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
start/stop tx rf path

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
start/stop tx data path

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
start/stop rx data path

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_vco_rx_on_1_comp: ad_addsub
**Description**
control-path delay compensation

- i_vco_rx_off_1_comp: ad_addsub
- i_vco_tx_on_1_comp: ad_addsub
- i_vco_tx_off_1_comp: ad_addsub
- i_rx_on_1_comp: ad_addsub
- i_rx_off_1_comp: ad_addsub
- i_tx_on_1_comp: ad_addsub
- i_tx_off_1_comp: ad_addsub
- i_vco_rx_on_2_comp: ad_addsub
- i_vco_rx_off_2_comp: ad_addsub
- i_vco_tx_on_2_comp: ad_addsub
- i_vco_tx_off_2_comp: ad_addsub
- i_rx_on_2_comp: ad_addsub
- i_rx_off_2_comp: ad_addsub
- i_tx_on_2_comp: ad_addsub
- i_tx_off_2_comp: ad_addsub
- i_tx_dp_on_1_comp: ad_addsub
**Description**
internal data-path delay compensation

- i_tx_dp_on_2_comp: ad_addsub
- i_tx_dp_off_1_comp: ad_addsub
- i_tx_dp_off_2_comp: ad_addsub
