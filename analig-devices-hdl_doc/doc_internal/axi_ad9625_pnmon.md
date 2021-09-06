# Entity: axi_ad9625_pnmon

- **File**: axi_ad9625_pnmon.v
## Diagram

![Diagram](axi_ad9625_pnmon.svg "Diagram")
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

| Port name     | Direction | Type    | Description                                |
| ------------- | --------- | ------- | ------------------------------------------ |
| adc_clk       | input     |         |  adc interface                             |
| adc_data      | input     | [191:0] |                                            |
| adc_pn_oos    | output    |         |  pn out of sync and error                  |
| adc_pn_err    | output    |         |                                            |
| adc_pnseq_sel | input     | [  3:0] |  processor interface PN9 (0x0), PN23 (0x1) |
## Signals

| Name             | Type                | Description          |
| ---------------- | ------------------- | -------------------- |
| adc_pn_data_in   | reg         [191:0] |  internal registers  |
| adc_pn_data_pn   | reg         [191:0] |                      |
| adc_pn_data_pn_s | wire [191:0]        |  internal signals    |
## Functions
- pn23 <font id="function_arguments">()</font> <font id="function_return">return ([191:0])</font>
**Description**
 PN23 function

- pn9 <font id="function_arguments">()</font> <font id="function_return">return ([191:0])</font>
**Description**
 PN9 function

## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
## Instantiations

- i_pnmon: ad_pnmon
**Description**
 pn oos & pn error

