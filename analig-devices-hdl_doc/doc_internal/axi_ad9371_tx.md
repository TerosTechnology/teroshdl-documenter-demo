# Entity: axi_ad9371_tx

- **File**: axi_ad9371_tx.v
## Diagram

![Diagram](axi_ad9371_tx.svg "Diagram")
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

| Generic name            | Type | Value | Description |
| ----------------------- | ---- | ----- | ----------- |
| ID                      |      | 0     |             |
| FPGA_TECHNOLOGY         |      | 0     |             |
| FPGA_FAMILY             |      | 0     |             |
| SPEED_GRADE             |      | 0     |             |
| DEV_PACKAGE             |      | 0     |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 16    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 16    |             |
| DATAPATH_DISABLE        |      | 0     |             |
## Ports

| Port name     | Direction | Type    | Description          |
| ------------- | --------- | ------- | -------------------- |
| dac_rst       | output    |         |  dac interface       |
| dac_clk       | input     |         |                      |
| dac_data      | output    | [127:0] |                      |
| dac_sync_in   | input     |         |  master/slave        |
| dac_sync_out  | output    |         |                      |
| dac_enable_i0 | output    |         |  dma interface       |
| dac_valid_i0  | output    |         |                      |
| dac_data_i0   | input     | [ 31:0] |                      |
| dac_enable_q0 | output    |         |                      |
| dac_valid_q0  | output    |         |                      |
| dac_data_q0   | input     | [ 31:0] |                      |
| dac_enable_i1 | output    |         |                      |
| dac_valid_i1  | output    |         |                      |
| dac_data_i1   | input     | [ 31:0] |                      |
| dac_enable_q1 | output    |         |                      |
| dac_valid_q1  | output    |         |                      |
| dac_data_q1   | input     | [ 31:0] |                      |
| dac_dunf      | input     |         |                      |
| up_rstn       | input     |         |  processor interface |
| up_clk        | input     |         |                      |
| up_wreq       | input     |         |                      |
| up_waddr      | input     | [ 13:0] |                      |
| up_wdata      | input     | [ 31:0] |                      |
| up_wack       | output    |         |                      |
| up_rreq       | input     |         |                      |
| up_raddr      | input     | [ 13:0] |                      |
| up_rdata      | output    | [ 31:0] |                      |
| up_rack       | output    |         |                      |
## Signals

| Name             | Type         | Description          |
| ---------------- | ------------ | -------------------- |
| dac_data_sync    | reg          |  internal registers  |
| dac_data_sync_s  | wire         |  internal signals    |
| dac_data_iq_i0_s | wire [ 31:0] |                      |
| dac_data_iq_q0_s | wire [ 31:0] |                      |
| dac_data_iq_i1_s | wire [ 31:0] |                      |
| dac_data_iq_q1_s | wire [ 31:0] |                      |
| dac_dds_format_s | wire         |                      |
| up_wack_s        | wire [  4:0] |                      |
| up_rack_s        | wire [  4:0] |                      |
| up_rdata_s       | wire [ 31:0] |                      |
## Processes
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor read interface 
## Instantiations

- i_tx_channel_0: axi_ad9371_tx_channel
- i_tx_channel_1: axi_ad9371_tx_channel
- i_tx_channel_2: axi_ad9371_tx_channel
- i_tx_channel_3: axi_ad9371_tx_channel
- i_up_dac_common: up_dac_common
</br>**Description**
 dac common processor interface

