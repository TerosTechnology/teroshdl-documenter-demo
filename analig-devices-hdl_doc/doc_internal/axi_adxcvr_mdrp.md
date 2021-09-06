# Entity: axi_adxcvr_mdrp

- **File**: axi_adxcvr_mdrp.v
## Diagram

![Diagram](axi_adxcvr_mdrp.svg "Diagram")
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

| Generic name | Type    | Value | Description  |
| ------------ | ------- | ----- | ------------ |
| XCVR_ID      | integer | 0     |  parameters  |
| NUM_OF_LANES | integer | 8     |              |
## Ports

| Port name    | Direction | Type   | Description |
| ------------ | --------- | ------ | ----------- |
| up_rstn      | input     |        |             |
| up_clk       | input     |        |             |
| up_sel       | input     | [ 7:0] |             |
| up_enb       | input     |        |             |
| up_enb_out   | output    |        |             |
| up_rdata_in  | input     | [15:0] |             |
| up_ready_in  | input     |        |             |
| up_rdata     | input     | [15:0] |             |
| up_ready     | input     |        |             |
| up_rdata_out | output    | [15:0] |             |
| up_ready_out | output    |        |             |
## Signals

| Name          | Type           | Description          |
| ------------- | -------------- | -------------------- |
| up_rdata_int  | reg     [15:0] |  internal registers  |
| up_ready_int  | reg            |                      |
| up_ready_mi   | reg            |                      |
| up_rdata_i    | reg     [15:0] |                      |
| up_ready_i    | reg            |                      |
| up_rdata_m    | reg     [15:0] |                      |
| up_ready_m    | reg            |                      |
| up_ready_s    | wire           |  internal signals    |
| up_rdata_mi_s | wire [15:0]    |                      |
| up_ready_mi_s | wire           |                      |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
