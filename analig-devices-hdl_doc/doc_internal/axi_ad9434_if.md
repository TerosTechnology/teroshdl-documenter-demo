# Entity: axi_ad9434_if

## Diagram

![Diagram](axi_ad9434_if.svg "Diagram")
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

| Generic name    | Type | Value                | Description |
| --------------- | ---- | -------------------- | ----------- |
| FPGA_TECHNOLOGY |      | 0                    |             |
| IO_DELAY_GROUP  |      | "dev_if_delay_group" |             |
## Ports

| Port name     | Direction | Type   | Description                         |
| ------------- | --------- | ------ | ----------------------------------- |
| adc_clk_in_p  | input     |        | device interface                    |
| adc_clk_in_n  | input     |        |                                     |
| adc_data_in_p | input     | [11:0] |                                     |
| adc_data_in_n | input     | [11:0] |                                     |
| adc_or_in_p   | input     |        |                                     |
| adc_or_in_n   | input     |        |                                     |
| adc_data      | output    | [47:0] | interface outputs                   |
| adc_or        | output    |        |                                     |
| adc_clk       | output    |        | internl reset and clocks            |
| adc_rst       | input     |        |                                     |
| adc_status    | output    |        |                                     |
| up_clk        | input     |        | delay interface (for IDELAY macros) |
| up_adc_dld    | input     | [12:0] |                                     |
| up_adc_dwdata | input     | [64:0] |                                     |
| up_adc_drdata | output    | [64:0] |                                     |
| delay_clk     | input     |        |                                     |
| delay_rst     | input     |        |                                     |
| delay_locked  | output    |        |                                     |
| mmcm_rst      | input     |        | mmcm reset                          |
| up_rstn       | input     |        | drp interface for MMCM_OR_BUFR_N    |
| up_drp_sel    | input     |        |                                     |
| up_drp_wr     | input     |        |                                     |
| up_drp_addr   | input     | [11:0] |                                     |
| up_drp_wdata  | input     | [31:0] |                                     |
| up_drp_rdata  | output    | [31:0] |                                     |
| up_drp_ready  | output    |        |                                     |
| up_drp_locked | output    |        |                                     |
## Signals

| Name          | Type       | Description         |
| ------------- | ---------- | ------------------- |
| adc_status_m1 | reg        | internal registers  |
| adc_or_s      | wire [3:0] | internal signals    |
| adc_clk_in    | wire       |                     |
| adc_div_clk   | wire       |                     |
## Constants

| Name | Type | Value | Description |
| ---- | ---- | ----- | ----------- |
| SDR  |      | 0     |             |
## Processes
- unnamed: ( @(posedge adc_div_clk) )
**Description**
adc status: adc is up, if both the MMCM_OR_BUFR_N and DELAY blocks are up

## Instantiations

- i_adc_data: ad_serdes_in
**Description**
data interface

- i_adc_or: ad_serdes_in
**Description**
over-range interface

- i_serdes_clk: ad_serdes_clk
**Description**
clock input buffers and MMCM_OR_BUFR_N

