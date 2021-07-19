# Entity: axi_ad9122_if

- **File**: axi_ad9122_if.v
## Diagram

![Diagram](axi_ad9122_if.svg "Diagram")
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
 This is the dac physical interface (drives samples from the low speed clock to the
 dac clock domain.
 
## Generics

| Generic name      | Type | Value                | Description |
| ----------------- | ---- | -------------------- | ----------- |
| FPGA_TECHNOLOGY   |      | 0                    |             |
| SERDES_OR_DDR_N   |      | 1                    |             |
| MMCM_OR_BUFIO_N   |      | 1                    |             |
| MMCM_CLKIN_PERIOD |      | 1.667                |             |
| MMCM_VCO_DIV      |      | 6                    |             |
| MMCM_VCO_MUL      |      | 12                   |             |
| MMCM_CLK0_DIV     |      | 2                    |             |
| MMCM_CLK1_DIV     |      | 8                    |             |
| IO_DELAY_GROUP    |      | "dac_if_delay_group" |             |
## Ports

| Port name       | Direction | Type   | Description                |
| --------------- | --------- | ------ | -------------------------- |
| dac_clk_in_p    | input     |        | dac interface              |
| dac_clk_in_n    | input     |        |                            |
| dac_clk_out_p   | output    |        |                            |
| dac_clk_out_n   | output    |        |                            |
| dac_frame_out_p | output    |        |                            |
| dac_frame_out_n | output    |        |                            |
| dac_data_out_p  | output    | [15:0] |                            |
| dac_data_out_n  | output    | [15:0] |                            |
| dac_rst         | input     |        | internal resets and clocks |
| dac_clk         | output    |        |                            |
| dac_div_clk     | output    |        |                            |
| dac_status      | output    |        |                            |
| dac_frame_i0    | input     |        | data interface             |
| dac_data_i0     | input     | [15:0] |                            |
| dac_frame_i1    | input     |        |                            |
| dac_data_i1     | input     | [15:0] |                            |
| dac_frame_i2    | input     |        |                            |
| dac_data_i2     | input     | [15:0] |                            |
| dac_frame_i3    | input     |        |                            |
| dac_data_i3     | input     | [15:0] |                            |
| dac_frame_q0    | input     |        |                            |
| dac_data_q0     | input     | [15:0] |                            |
| dac_frame_q1    | input     |        |                            |
| dac_data_q1     | input     | [15:0] |                            |
| dac_frame_q2    | input     |        |                            |
| dac_data_q2     | input     | [15:0] |                            |
| dac_frame_q3    | input     |        |                            |
| dac_data_q3     | input     | [15:0] |                            |
| mmcm_rst        | input     |        | mmcm reset                 |
| up_clk          | input     |        | drp interface              |
| up_rstn         | input     |        |                            |
| up_drp_sel      | input     |        |                            |
| up_drp_wr       | input     |        |                            |
| up_drp_addr     | input     | [11:0] |                            |
| up_drp_wdata    | input     | [31:0] |                            |
| up_drp_rdata    | output    | [31:0] |                            |
| up_drp_ready    | output    |        |                            |
| up_drp_locked   | output    |        |                            |
## Signals

| Name          | Type | Description         |
| ------------- | ---- | ------------------- |
| dac_status_m1 | reg  | internal registers  |
| dac_out_clk   | wire | internal signals    |
| loaden_s      | wire |                     |
## Processes
- unnamed: ( @(posedge dac_div_clk) )
**Description**
dac status

## Instantiations

- i_serdes_out_data: ad_serdes_out
**Description**
dac data output serdes(s) & buffers

- i_serdes_out_frame: ad_serdes_out
**Description**
dac frame output serdes & buffer

- i_serdes_out_clk: ad_serdes_out
**Description**
dac clock output serdes & buffer

- i_serdes_clk: ad_serdes_clk
**Description**
dac clock input buffers

