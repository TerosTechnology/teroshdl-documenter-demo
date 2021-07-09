# Entity: axi_ad9371_rx_os

## Diagram

![Diagram](axi_ad9371_rx_os.svg "Diagram")
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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| ID               |      | 0     |             |
| FPGA_TECHNOLOGY  |      | 0     |             |
| FPGA_FAMILY      |      | 0     |             |
| SPEED_GRADE      |      | 0     |             |
| DEV_PACKAGE      |      | 0     |             |
| DATAPATH_DISABLE |      | 0     |             |
## Ports

| Port name        | Direction | Type    | Description         |
| ---------------- | --------- | ------- | ------------------- |
| adc_os_rst       | output    |         | adc interface       |
| adc_os_clk       | input     |         |                     |
| adc_os_valid     | input     |         |                     |
| adc_os_data      | input     | [ 63:0] |                     |
| adc_os_enable_i0 | output    |         | dma interface       |
| adc_os_valid_i0  | output    |         |                     |
| adc_os_data_i0   | output    | [ 31:0] |                     |
| adc_os_enable_q0 | output    |         |                     |
| adc_os_valid_q0  | output    |         |                     |
| adc_os_data_q0   | output    | [ 31:0] |                     |
| adc_os_dovf      | input     |         |                     |
| up_rstn          | input     |         | processor interface |
| up_clk           | input     |         |                     |
| up_wreq          | input     |         |                     |
| up_waddr         | input     | [ 13:0] |                     |
| up_wdata         | input     | [ 31:0] |                     |
| up_wack          | output    |         |                     |
| up_rreq          | input     |         |                     |
| up_raddr         | input     | [ 13:0] |                     |
| up_rdata         | output    | [ 31:0] |                     |
| up_rack          | output    |         |                     |
## Signals

| Name                | Type         | Description         |
| ------------------- | ------------ | ------------------- |
| up_status_pn_err    | reg          | internal registers  |
| up_status_pn_oos    | reg          |                     |
| up_status_or        | reg          |                     |
| adc_os_data_iq_i0_s | wire [ 31:0] | internal signals    |
| adc_os_data_iq_q0_s | wire [ 31:0] |                     |
| up_adc_pn_err_s     | wire [  1:0] |                     |
| up_adc_pn_oos_s     | wire [  1:0] |                     |
| up_adc_or_s         | wire [  1:0] |                     |
| up_wack_s           | wire [  2:0] |                     |
| up_rack_s           | wire [  2:0] |                     |
| up_rdata_s          | wire [ 31:0] |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_rx_os_channel_0: axi_ad9371_rx_channel
**Description**
channel o/s (i)

- i_rx_os_channel_1: axi_ad9371_rx_channel
**Description**
channel o/s (q)

- i_up_adc_common: up_adc_common
**Description**
common processor control

