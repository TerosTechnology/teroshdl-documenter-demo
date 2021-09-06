# Entity: axi_dac_interpolate_reg

- **File**: axi_dac_interpolate_reg.v
## Diagram

![Diagram](axi_dac_interpolate_reg.svg "Diagram")
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

## Ports

| Port name                    | Direction | Type   | Description    |
| ---------------------------- | --------- | ------ | -------------- |
| clk                          | input     |        |                |
| dac_interpolation_ratio_a    | output    | [31:0] |                |
| dac_filter_mask_a            | output    | [ 2:0] |                |
| dac_interpolation_ratio_b    | output    | [31:0] |                |
| dac_filter_mask_b            | output    | [ 2:0] |                |
| dma_transfer_suspend         | output    |        |                |
| start_sync_channels          | output    |        |                |
| dac_correction_enable_a      | output    |        |                |
| dac_correction_enable_b      | output    |        |                |
| dac_correction_coefficient_a | output    | [15:0] |                |
| dac_correction_coefficient_b | output    | [15:0] |                |
| trigger_config               | output    | [19:0] |                |
| lsample_hold_config          | output    | [ 1:0] |                |
| up_rstn                      | input     |        |  bus interface |
| up_clk                       | input     |        |                |
| up_wreq                      | input     |        |                |
| up_waddr                     | input     | [ 4:0] |                |
| up_wdata                     | input     | [31:0] |                |
| up_wack                      | output    |        |                |
| up_rreq                      | input     |        |                |
| up_raddr                     | input     | [ 4:0] |                |
| up_rdata                     | output    | [31:0] |                |
| up_rack                      | output    |        |                |
## Signals

| Name                        | Type           | Description          |
| --------------------------- | -------------- | -------------------- |
| up_version                  | reg     [31:0] |  internal registers  |
| up_scratch                  | reg     [31:0] |                      |
| up_interpolation_ratio_a    | reg     [31:0] |                      |
| up_filter_mask_a            | reg     [ 2:0] |                      |
| up_interpolation_ratio_b    | reg     [31:0] |                      |
| up_filter_mask_b            | reg     [ 2:0] |                      |
| up_flags                    | reg     [1:0]  |                      |
| up_config                   | reg     [1:0]  |                      |
| up_correction_coefficient_a | reg     [15:0] |                      |
| up_correction_coefficient_b | reg     [15:0] |                      |
| up_trigger_config           | reg     [19:0] |                      |
| up_lsample_hold_config      | reg     [ 1:0] |                      |
| flags                       | wire [ 1:0]    |                      |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_xfer_cntrl: up_xfer_cntrl
