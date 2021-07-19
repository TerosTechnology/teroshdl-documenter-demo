# Entity: axi_adrv9001_tdd

- **File**: axi_adrv9001_tdd.v
## Diagram

![Diagram](axi_adrv9001_tdd.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2020 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| ID           |      | 0     |             |
| BASE_ADDRESS |      | 6'h20 |             |
## Ports

| Port name     | Direction | Type   | Description                          |
| ------------- | --------- | ------ | ------------------------------------ |
| clk           | input     |        | clock                                |
| rst           | input     |        |                                      |
| tdd_rx_vco_en | output    |        | control signals from the tdd control |
| tdd_tx_vco_en | output    |        |                                      |
| tdd_rx_rf_en  | output    |        |                                      |
| tdd_tx_rf_en  | output    |        |                                      |
| tdd_enabled   | output    |        | status signal                        |
| tdd_status    | input     | [ 7:0] |                                      |
| tdd_sync      | input     |        | sync signal                          |
| tdd_sync_cntr | output    |        |                                      |
| tdd_tx_valid  | output    | reg    | tx/rx data flow control              |
| tdd_rx_valid  | output    | reg    |                                      |
| up_rstn       | input     |        | bus interface                        |
| up_clk        | input     |        |                                      |
| up_wreq       | input     |        |                                      |
| up_waddr      | input     | [13:0] |                                      |
| up_wdata      | input     | [31:0] |                                      |
| up_wack       | output    |        |                                      |
| up_rreq       | input     |        |                                      |
| up_raddr      | input     | [13:0] |                                      |
| up_rdata      | output    | [31:0] |                                      |
| up_rack       | output    |        |                                      |
## Signals

| Name                   | Type        | Description       |
| ---------------------- | ----------- | ----------------- |
| tdd_enable_s           | wire        | internal signals  |
| tdd_secondary_s        | wire        |                   |
| tdd_burst_count_s      | wire [ 7:0] |                   |
| tdd_rx_only_s          | wire        |                   |
| tdd_tx_only_s          | wire        |                   |
| tdd_gated_rx_dmapath_s | wire        |                   |
| tdd_gated_tx_dmapath_s | wire        |                   |
| tdd_counter_init_s     | wire [23:0] |                   |
| tdd_frame_length_s     | wire [23:0] |                   |
| tdd_terminal_type_s    | wire        |                   |
| tdd_sync_enable_s      | wire        |                   |
| tdd_vco_rx_on_1_s      | wire [23:0] |                   |
| tdd_vco_rx_off_1_s     | wire [23:0] |                   |
| tdd_vco_tx_on_1_s      | wire [23:0] |                   |
| tdd_vco_tx_off_1_s     | wire [23:0] |                   |
| tdd_rx_on_1_s          | wire [23:0] |                   |
| tdd_rx_off_1_s         | wire [23:0] |                   |
| tdd_rx_dp_on_1_s       | wire [23:0] |                   |
| tdd_rx_dp_off_1_s      | wire [23:0] |                   |
| tdd_tx_on_1_s          | wire [23:0] |                   |
| tdd_tx_off_1_s         | wire [23:0] |                   |
| tdd_tx_dp_on_1_s       | wire [23:0] |                   |
| tdd_tx_dp_off_1_s      | wire [23:0] |                   |
| tdd_vco_rx_on_2_s      | wire [23:0] |                   |
| tdd_vco_rx_off_2_s     | wire [23:0] |                   |
| tdd_vco_tx_on_2_s      | wire [23:0] |                   |
| tdd_vco_tx_off_2_s     | wire [23:0] |                   |
| tdd_rx_on_2_s          | wire [23:0] |                   |
| tdd_rx_off_2_s         | wire [23:0] |                   |
| tdd_rx_dp_on_2_s       | wire [23:0] |                   |
| tdd_rx_dp_off_2_s      | wire [23:0] |                   |
| tdd_tx_on_2_s          | wire [23:0] |                   |
| tdd_tx_off_2_s         | wire [23:0] |                   |
| tdd_tx_dp_on_2_s       | wire [23:0] |                   |
| tdd_tx_dp_off_2_s      | wire [23:0] |                   |
| tdd_counter_status     | wire [23:0] |                   |
| tdd_rx_dp_en_s         | wire        |                   |
| tdd_tx_dp_en_s         | wire        |                   |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
syncronization control signal

- unnamed: ( @(posedge clk) )
**Description**
tx/rx data flow control

- unnamed: ( @(posedge clk) )
## Instantiations

- i_up_tdd_cntrl: up_tdd_cntrl
**Description**
instantiations

- i_tdd_control: ad_tdd_control
**Description**
the TX_DATA_PATH_DELAY and CONTROL_PATH_DELAY are specificly defined
for the axi_adrv9001 core

