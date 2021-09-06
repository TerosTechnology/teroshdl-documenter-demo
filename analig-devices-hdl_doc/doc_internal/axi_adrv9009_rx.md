# Entity: axi_adrv9009_rx

- **File**: axi_adrv9009_rx.v
## Diagram

![Diagram](axi_adrv9009_rx.svg "Diagram")
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

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| ID                   |      | 0     |             |
| FPGA_TECHNOLOGY      |      | 0     |             |
| FPGA_FAMILY          |      | 0     |             |
| SPEED_GRADE          |      | 0     |             |
| DEV_PACKAGE          |      | 0     |             |
| DATAFORMAT_DISABLE   |      | 0     |             |
| DCFILTER_DISABLE     |      | 0     |             |
| IQCORRECTION_DISABLE |      | 0     |             |
## Ports

| Port name     | Direction | Type    | Description          |
| ------------- | --------- | ------- | -------------------- |
| adc_rst       | output    |         |  adc interface       |
| adc_clk       | input     |         |                      |
| adc_data      | input     | [ 63:0] |                      |
| adc_enable_i0 | output    |         |  dma interface       |
| adc_valid_i0  | output    |         |                      |
| adc_data_i0   | output    | [ 15:0] |                      |
| adc_enable_q0 | output    |         |                      |
| adc_valid_q0  | output    |         |                      |
| adc_data_q0   | output    | [ 15:0] |                      |
| adc_enable_i1 | output    |         |                      |
| adc_valid_i1  | output    |         |                      |
| adc_data_i1   | output    | [ 15:0] |                      |
| adc_enable_q1 | output    |         |                      |
| adc_valid_q1  | output    |         |                      |
| adc_data_q1   | output    | [ 15:0] |                      |
| adc_dovf      | input     |         |                      |
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

| Name             | Type         | Description        |
| ---------------- | ------------ | ------------------ |
| up_status_pn_oos | reg          |                    |
| up_status_or     | reg          |                    |
| adc_data_iq_i0_s | wire [ 15:0] |  internal signals  |
| adc_data_iq_q0_s | wire [ 15:0] |                    |
| adc_data_iq_i1_s | wire [ 15:0] |                    |
| adc_data_iq_q1_s | wire [ 15:0] |                    |
| up_adc_pn_err_s  | wire [  3:0] |                    |
| up_adc_pn_oos_s  | wire [  3:0] |                    |
| up_adc_or_s      | wire [  3:0] |                    |
| up_wack_s        | wire [  4:0] |                    |
| up_rack_s        | wire [  4:0] |                    |
| up_rdata_s       | wire [ 31:0] |                    |
## Constants

| Name   | Type | Value | Description              |
| ------ | ---- | ----- | ------------------------ |
| CONFIG |      |       |  configuration settings  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_rx_channel_0: axi_adrv9009_rx_channel
**Description**
 channel 0 (i)

- i_rx_channel_1: axi_adrv9009_rx_channel
**Description**
 channel 1 (q)

- i_rx_channel_2: axi_adrv9009_rx_channel
**Description**
 channel 2 (i)

- i_rx_channel_3: axi_adrv9009_rx_channel
**Description**
 channel 3 (q)

- i_up_adc_common: up_adc_common
**Description**
 common processor control

