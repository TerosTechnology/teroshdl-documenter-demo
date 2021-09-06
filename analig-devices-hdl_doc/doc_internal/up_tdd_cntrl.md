# Entity: up_tdd_cntrl

- **File**: up_tdd_cntrl.v
## Diagram

![Diagram](up_tdd_cntrl.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| ID           |      | 0     |             |
| BASE_ADDRESS |      | 6'h20 |             |
## Ports

| Port name            | Direction | Type   | Description              |
| -------------------- | --------- | ------ | ------------------------ |
| clk                  | input     |        |                          |
| rst                  | input     |        |                          |
| tdd_enable           | output    |        | rf tdd interface control |
| tdd_secondary        | output    |        |                          |
| tdd_rx_only          | output    |        |                          |
| tdd_tx_only          | output    |        |                          |
| tdd_gated_rx_dmapath | output    |        |                          |
| tdd_gated_tx_dmapath | output    |        |                          |
| tdd_burst_count      | output    | [ 7:0] |                          |
| tdd_counter_init     | output    | [23:0] |                          |
| tdd_frame_length     | output    | [23:0] |                          |
| tdd_terminal_type    | output    |        |                          |
| tdd_vco_rx_on_1      | output    | [23:0] |                          |
| tdd_vco_rx_off_1     | output    | [23:0] |                          |
| tdd_vco_tx_on_1      | output    | [23:0] |                          |
| tdd_vco_tx_off_1     | output    | [23:0] |                          |
| tdd_rx_on_1          | output    | [23:0] |                          |
| tdd_rx_off_1         | output    | [23:0] |                          |
| tdd_rx_dp_on_1       | output    | [23:0] |                          |
| tdd_rx_dp_off_1      | output    | [23:0] |                          |
| tdd_tx_on_1          | output    | [23:0] |                          |
| tdd_tx_off_1         | output    | [23:0] |                          |
| tdd_tx_dp_on_1       | output    | [23:0] |                          |
| tdd_tx_dp_off_1      | output    | [23:0] |                          |
| tdd_vco_rx_on_2      | output    | [23:0] |                          |
| tdd_vco_rx_off_2     | output    | [23:0] |                          |
| tdd_vco_tx_on_2      | output    | [23:0] |                          |
| tdd_vco_tx_off_2     | output    | [23:0] |                          |
| tdd_rx_on_2          | output    | [23:0] |                          |
| tdd_rx_off_2         | output    | [23:0] |                          |
| tdd_rx_dp_on_2       | output    | [23:0] |                          |
| tdd_rx_dp_off_2      | output    | [23:0] |                          |
| tdd_tx_on_2          | output    | [23:0] |                          |
| tdd_tx_off_2         | output    | [23:0] |                          |
| tdd_tx_dp_on_2       | output    | [23:0] |                          |
| tdd_tx_dp_off_2      | output    | [23:0] |                          |
| tdd_status           | input     | [ 7:0] |                          |
| up_rstn              | input     |        |  bus interface           |
| up_clk               | input     |        |                          |
| up_wreq              | input     |        |                          |
| up_waddr             | input     | [13:0] |                          |
| up_wdata             | input     | [31:0] |                          |
| up_wack              | output    |        |                          |
| up_rreq              | input     |        |                          |
| up_raddr             | input     | [13:0] |                          |
| up_rdata             | output    | [31:0] |                          |
| up_rack              | output    |        |                          |
## Signals

| Name                    | Type           | Description          |
| ----------------------- | -------------- | -------------------- |
| up_scratch              | reg     [31:0] |  internal registers  |
| up_tdd_enable           | reg            |                      |
| up_tdd_secondary        | reg            |                      |
| up_tdd_rx_only          | reg            |                      |
| up_tdd_tx_only          | reg            |                      |
| up_tdd_gated_tx_dmapath | reg            |                      |
| up_tdd_gated_rx_dmapath | reg            |                      |
| up_tdd_terminal_type    | reg            |                      |
| up_tdd_burst_count      | reg     [ 7:0] |                      |
| up_tdd_counter_init     | reg     [23:0] |                      |
| up_tdd_frame_length     | reg     [23:0] |                      |
| up_tdd_vco_rx_on_1      | reg     [23:0] |                      |
| up_tdd_vco_rx_off_1     | reg     [23:0] |                      |
| up_tdd_vco_tx_on_1      | reg     [23:0] |                      |
| up_tdd_vco_tx_off_1     | reg     [23:0] |                      |
| up_tdd_rx_on_1          | reg     [23:0] |                      |
| up_tdd_rx_off_1         | reg     [23:0] |                      |
| up_tdd_rx_dp_on_1       | reg     [23:0] |                      |
| up_tdd_rx_dp_off_1      | reg     [23:0] |                      |
| up_tdd_tx_on_1          | reg     [23:0] |                      |
| up_tdd_tx_off_1         | reg     [23:0] |                      |
| up_tdd_tx_dp_on_1       | reg     [23:0] |                      |
| up_tdd_tx_dp_off_1      | reg     [23:0] |                      |
| up_tdd_vco_rx_on_2      | reg     [23:0] |                      |
| up_tdd_vco_rx_off_2     | reg     [23:0] |                      |
| up_tdd_vco_tx_on_2      | reg     [23:0] |                      |
| up_tdd_vco_tx_off_2     | reg     [23:0] |                      |
| up_tdd_rx_on_2          | reg     [23:0] |                      |
| up_tdd_rx_off_2         | reg     [23:0] |                      |
| up_tdd_rx_dp_on_2       | reg     [23:0] |                      |
| up_tdd_rx_dp_off_2      | reg     [23:0] |                      |
| up_tdd_tx_on_2          | reg     [23:0] |                      |
| up_tdd_tx_off_2         | reg     [23:0] |                      |
| up_tdd_tx_dp_on_2       | reg     [23:0] |                      |
| up_tdd_tx_dp_off_2      | reg     [23:0] |                      |
| up_wreq_s               | wire           |  internal signals    |
| up_rreq_s               | wire           |                      |
| up_tdd_status_s         | wire [ 7:0]    |                      |
## Constants

| Name          | Type | Value        | Description         |
| ------------- | ---- | ------------ | ------------------- |
| PCORE_VERSION |      | 32'h00010061 |                     |
| PCORE_MAGIC   |      | 32'h54444443 | "TDDC", big endian  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor write interface 
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor read interface 
## Instantiations

- i_xfer_tdd_control: up_xfer_cntrl
</br>**Description**
 rf tdd control signal CDC

- i_xfer_tdd_counter_values_rx_1: up_xfer_cntrl
- i_xfer_tdd_counter_values_tx_1: up_xfer_cntrl
- i_xfer_tdd_counter_values_rx_2: up_xfer_cntrl
- i_xfer_tdd_counter_values_tx_2: up_xfer_cntrl
- i_xfer_tdd_status: up_xfer_status
