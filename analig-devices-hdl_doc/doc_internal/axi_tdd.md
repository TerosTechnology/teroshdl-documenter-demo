# Entity: axi_tdd

- **File**: axi_tdd.v
## Diagram

![Diagram](axi_tdd.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2021 (c) Analog Devices, Inc. All rights reserved.
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
| tdd_sync      | input     |        | sync signal                          |
| tdd_sync_cntr | output    |        |                                      |
| tdd_tx_valid  | output    |        | tx/rx data flow control              |
| tdd_rx_valid  | output    |        |                                      |
| s_axi_aresetn | input     |        | bus interface                        |
| s_axi_aclk    | input     |        |                                      |
| s_axi_awvalid | input     |        |                                      |
| s_axi_awaddr  | input     | [15:0] |                                      |
| s_axi_awready | output    |        |                                      |
| s_axi_wvalid  | input     |        |                                      |
| s_axi_wdata   | input     | [31:0] |                                      |
| s_axi_wstrb   | input     | [ 3:0] |                                      |
| s_axi_wready  | output    |        |                                      |
| s_axi_bvalid  | output    |        |                                      |
| s_axi_bresp   | output    | [ 1:0] |                                      |
| s_axi_bready  | input     |        |                                      |
| s_axi_arvalid | input     |        |                                      |
| s_axi_araddr  | input     | [15:0] |                                      |
| s_axi_arready | output    |        |                                      |
| s_axi_rvalid  | output    |        |                                      |
| s_axi_rresp   | output    | [ 1:0] |                                      |
| s_axi_rdata   | output    | [31:0] |                                      |
| s_axi_rready  | input     |        |                                      |
## Signals

| Name                   | Type        | Description       |
| ---------------------- | ----------- | ----------------- |
| up_rstn                | wire        | internal signals  |
| up_clk                 | wire        |                   |
| up_wreq                | wire        |                   |
| up_waddr               | wire [13:0] |                   |
| up_wdata               | wire [31:0] |                   |
| up_wack                | wire        |                   |
| up_rreq                | wire        |                   |
| up_raddr               | wire [13:0] |                   |
| up_rdata               | wire [31:0] |                   |
| up_rack                | wire        |                   |
| tdd_enable_s           | wire        |                   |
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
| tdd_status             | wire [ 7:0] |                   |
| tdd_counter_status     | wire [23:0] |                   |
| tdd_rx_dp_en_s         | wire        |                   |
| tdd_tx_dp_en_s         | wire        |                   |
| tdd_vco_overlap        | reg         |                   |
| tdd_rf_overlap         | reg         |                   |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
syncronization control signal

- unnamed: ( @(posedge clk) )
**Description**
tx/rx data flow control

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_up_tdd_cntrl: up_tdd_cntrl
**Description**
instantiations

- i_tdd_control: ad_tdd_control
- i_up_axi: up_axi
