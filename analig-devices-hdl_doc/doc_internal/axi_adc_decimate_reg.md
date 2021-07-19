# Entity: axi_adc_decimate_reg

- **File**: axi_adc_decimate_reg.v
## Diagram

![Diagram](axi_adc_decimate_reg.svg "Diagram")
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

| Port name                    | Direction | Type   | Description   |
| ---------------------------- | --------- | ------ | ------------- |
| clk                          | input     |        |               |
| adc_decimation_ratio         | output    | [31:0] |               |
| adc_filter_mask              | output    | [ 2:0] |               |
| adc_correction_enable_a      | output    |        |               |
| adc_correction_enable_b      | output    |        |               |
| adc_correction_coefficient_a | output    | [15:0] |               |
| adc_correction_coefficient_b | output    | [15:0] |               |
| up_rstn                      | input     |        | bus interface |
| up_clk                       | input     |        |               |
| up_wreq                      | input     |        |               |
| up_waddr                     | input     | [ 4:0] |               |
| up_wdata                     | input     | [31:0] |               |
| up_wack                      | output    |        |               |
| up_rreq                      | input     |        |               |
| up_raddr                     | input     | [ 4:0] |               |
| up_rdata                     | output    | [31:0] |               |
| up_rack                      | output    |        |               |
## Signals

| Name                        | Type           | Description         |
| --------------------------- | -------------- | ------------------- |
| up_version                  | reg     [31:0] | internal registers  |
| up_scratch                  | reg     [31:0] |                     |
| up_decimation_ratio         | reg     [31:0] |                     |
| up_filter_mask              | reg     [ 2:0] |                     |
| up_config                   | reg     [ 1:0] |                     |
| up_correction_coefficient_a | reg     [15:0] |                     |
| up_correction_coefficient_b | reg     [15:0] |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_xfer_cntrl: up_xfer_cntrl
