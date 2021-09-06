# Entity: axi_ad9434_core

- **File**: axi_ad9434_core.v
## Diagram

![Diagram](axi_ad9434_core.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| ID              |      | 0     |             |
| FPGA_TECHNOLOGY |      | 0     |             |
| FPGA_FAMILY     |      | 0     |             |
| SPEED_GRADE     |      | 0     |             |
| DEV_PACKAGE     |      | 0     |             |
## Ports

| Port name     | Direction | Type   | Description                 |
| ------------- | --------- | ------ | --------------------------- |
| adc_clk       | input     |        |  device interface           |
| adc_data      | input     | [47:0] |                             |
| adc_or        | input     |        |                             |
| dma_dvalid    | output    |        |  dma interface              |
| dma_data      | output    | [63:0] |                             |
| dma_dovf      | input     |        |                             |
| up_drp_sel    | output    |        |  drp interface              |
| up_drp_wr     | output    |        |                             |
| up_drp_addr   | output    | [11:0] |                             |
| up_drp_wdata  | output    | [31:0] |                             |
| up_drp_rdata  | input     | [31:0] |                             |
| up_drp_ready  | input     |        |                             |
| up_drp_locked | input     |        |                             |
| up_dld        | output    | [12:0] |  delay interface            |
| up_dwdata     | output    | [64:0] |                             |
| up_drdata     | input     | [64:0] |                             |
| delay_clk     | input     |        |                             |
| delay_rst     | output    |        |                             |
| delay_locked  | input     |        |                             |
| up_rstn       | input     |        |  processor interface        |
| up_clk        | input     |        |                             |
| up_wreq       | input     |        |                             |
| up_waddr      | input     | [13:0] |                             |
| up_wdata      | input     | [31:0] |                             |
| up_wack       | output    |        |                             |
| up_rreq       | input     |        |                             |
| up_raddr      | input     | [13:0] |                             |
| up_rdata      | output    | [31:0] |                             |
| up_rack       | output    |        |                             |
| mmcm_rst      | output    |        |  status and control signals |
| adc_rst       | output    |        |                             |
| adc_enable    | output    |        |                             |
| adc_status    | input     |        |                             |
## Signals

| Name               | Type        | Description        |
| ------------------ | ----------- | ------------------ |
| up_status_pn_err_s | wire        |  internal signals  |
| up_status_pn_oos_s | wire        |                    |
| up_status_or_s     | wire        |                    |
| adc_dfmt_se_s      | wire        |                    |
| adc_dfmt_type_s    | wire        |                    |
| adc_dfmt_enable_s  | wire        |                    |
| adc_pnseq_sel_s    | wire [ 3:0] |                    |
| adc_pn_err_s       | wire        |                    |
| adc_pn_oos_s       | wire        |                    |
| up_wack_s          | wire        |                    |
| up_rdata_s         | wire [31:0] |                    |
| up_rack_s          | wire        |                    |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_pnmon: axi_ad9434_pnmon
**Description**
 instantiations

- i_adc_common: up_adc_common
- i_adc_channel: up_adc_channel
- i_delay_cntrl: up_delay_cntrl
**Description**
 adc delay control

