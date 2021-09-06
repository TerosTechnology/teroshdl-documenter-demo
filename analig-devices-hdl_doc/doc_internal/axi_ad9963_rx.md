# Entity: axi_ad9963_rx

- **File**: axi_ad9963_rx.v
## Diagram

![Diagram](axi_ad9963_rx.svg "Diagram")
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

| Generic name         | Type | Value | Description  |
| -------------------- | ---- | ----- | ------------ |
| USERPORTS_DISABLE    |      | 0     |  parameters  |
| DATAFORMAT_DISABLE   |      | 0     |              |
| DCFILTER_DISABLE     |      | 0     |              |
| IQCORRECTION_DISABLE |      | 0     |              |
| SCALECORRECTION_ONLY |      | 1     |              |
| IODELAY_ENABLE       |      | 0     |              |
| ID                   |      | 0     |              |
| FPGA_TECHNOLOGY      |      | 0     |              |
| FPGA_FAMILY          |      | 0     |              |
| SPEED_GRADE          |      | 0     |              |
| DEV_PACKAGE          |      | 0     |              |
## Ports

| Port name    | Direction | Type   | Description          |
| ------------ | --------- | ------ | -------------------- |
| adc_rst      | output    |        |  adc interface       |
| adc_clk      | input     |        |                      |
| adc_valid    | input     |        |                      |
| adc_data     | input     | [23:0] |                      |
| adc_status   | input     |        |                      |
| up_dld       | output    | [12:0] |  delay interface     |
| up_dwdata    | output    | [64:0] |                      |
| up_drdata    | input     | [64:0] |                      |
| delay_clk    | input     |        |                      |
| delay_rst    | output    |        |                      |
| delay_locked | input     |        |                      |
| adc_enable_i | output    |        |  dma interface       |
| adc_valid_i  | output    |        |                      |
| adc_data_i   | output    | [15:0] |                      |
| adc_enable_q | output    |        |                      |
| adc_valid_q  | output    |        |                      |
| adc_data_q   | output    | [15:0] |                      |
| adc_dovf     | input     |        |                      |
| up_adc_ce    | output    |        |                      |
| up_rstn      | input     |        |  processor interface |
| up_clk       | input     |        |                      |
| up_wreq      | input     |        |                      |
| up_waddr     | input     | [13:0] |                      |
| up_wdata     | input     | [31:0] |                      |
| up_wack      | output    |        |                      |
| up_rreq      | input     |        |                      |
| up_raddr     | input     | [13:0] |                      |
| up_rdata     | output    | [31:0] |                      |
| up_rack      | output    |        |                      |
## Signals

| Name                      | Type        | Description        |
| ------------------------- | ----------- | ------------------ |
| up_status_pn_oos          | reg         |                    |
| up_status_or              | reg         |                    |
| adc_dcfilter_data_out_0_s | wire [15:0] |  internal signals  |
| adc_dcfilter_data_out_1_s | wire [15:0] |                    |
| up_adc_pn_err_s           | wire [ 1:0] |                    |
| up_adc_pn_oos_s           | wire [ 1:0] |                    |
| up_adc_or_s               | wire [ 1:0] |                    |
| up_rdata_s                | wire [31:0] |                    |
| up_rack_s                 | wire        |                    |
| up_wack_s                 | wire        |                    |
## Constants

| Name   | Type | Value | Description              |
| ------ | ---- | ----- | ------------------------ |
| CONFIG |      |       |  configuration settings  |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
</br>**Description**
 processor read interface 
- unnamed: ( @(*) )
  - **Type:** always
## Instantiations

- i_rx_channel_0: axi_ad9963_rx_channel
</br>**Description**
 channel 0 (i)

- i_rx_channel_1: axi_ad9963_rx_channel
</br>**Description**
 channel 1 (q)

- i_up_adc_common: up_adc_common
</br>**Description**
 common processor control

