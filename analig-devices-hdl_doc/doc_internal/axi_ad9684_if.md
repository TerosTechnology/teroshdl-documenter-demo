# Entity: axi_ad9684_if

- **File**: axi_ad9684_if.v
## Diagram

![Diagram](axi_ad9684_if.svg "Diagram")
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
| OR_STATUS       |      | 0                    |             |
## Ports

| Port name     | Direction | Type   | Description       |
| ------------- | --------- | ------ | ----------------- |
| adc_clk_in_p  | input     |        |  device interface |
| adc_clk_in_n  | input     |        |                   |
| adc_data_in_p | input     | [13:0] |                   |
| adc_data_in_n | input     | [13:0] |                   |
| adc_data_or_p | input     |        |                   |
| adc_data_or_n | input     |        |                   |
| adc_clk       | output    |        |  data interface   |
| adc_rst       | input     |        |                   |
| adc_data_a    | output    | [27:0] |                   |
| adc_or_a      | output    |        |                   |
| adc_data_b    | output    | [27:0] |                   |
| adc_or_b      | output    |        |                   |
| adc_status    | output    |        |                   |
| delay_clk     | input     |        |  delay interface  |
| delay_rst     | input     |        |                   |
| delay_dload   | input     | [14:0] |                   |
| delay_wdata   | input     | [74:0] |                   |
| delay_rdata   | output    | [74:0] |                   |
| delay_locked  | output    |        |                   |
| rst           | input     |        |  reset            |
| up_clk        | input     |        |  drp interface    |
| up_rstn       | input     |        |                   |
| up_drp_sel    | input     |        |                   |
| up_drp_wr     | input     |        |                   |
| up_drp_addr   | input     | [11:0] |                   |
| up_drp_wdata  | input     | [31:0] |                   |
| up_drp_rdata  | output    | [31:0] |                   |
| up_drp_ready  | output    |        |                   |
| up_drp_locked | output    |        |                   |
## Signals

| Name            | Type        | Description          |
| --------------- | ----------- | -------------------- |
| adc_status_m1   | reg         |  internal registers  |
| adc_clk_in      | wire        |  internal signals    |
| adc_div_clk     | wire        |                      |
| adc_data_or_a_s | wire [ 1:0] |                      |
| adc_data_or_b_s | wire [ 1:0] |                      |
| loaden_s        | wire        |                      |
| phase_s         | wire [ 7:0] |                      |
## Constants

| Name         | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DDR_OR_SDR_N |      | 1     |             |
## Processes
- unnamed: ( @(posedge adc_div_clk) )
  - **Type:** always
</br>**Description**
 adc status: adc is up, if both the MMCM_OR_BUFR_N and DELAY blocks are up 
## Instantiations

- i_adc_data: ad_serdes_in
</br>**Description**
 data interface

- i_serdes_clk: ad_serdes_clk
</br>**Description**
 clock input buffers and MMCM_OR_BUFR_N

