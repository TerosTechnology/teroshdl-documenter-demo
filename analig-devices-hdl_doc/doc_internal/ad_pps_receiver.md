# Entity: ad_pps_receiver

- **File**: ad_pps_receiver.v
## Diagram

![Diagram](ad_pps_receiver.svg "Diagram")
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

| Port name       | Direction | Type   | Description |
| --------------- | --------- | ------ | ----------- |
| clk             | input     |        |             |
| rst             | input     |        |             |
| gps_pps         | input     |        |             |
| up_clk          | input     |        |             |
| up_rstn         | input     |        |             |
| up_pps_rcounter | output    | [31:0] |             |
| up_pps_status   | output    |        |             |
| up_irq_mask     | input     |        |             |
| up_irq          | output    |        |             |
## Signals

| Name             | Type         | Description                                                                                                                                                                                                                                                 |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| gps_pps_m        | reg   [ 2:0] |  *************************************************************************  1PPS reception and reporting counter implementation  Note: this module should run on the core clock  *************************************************************************  |
| up_pps_m         | reg   [ 2:0] |                                                                                                                                                                                                                                                             |
| up_pps_status_m  | reg          |                                                                                                                                                                                                                                                             |
| pps_toggle       | reg          |                                                                                                                                                                                                                                                             |
| free_rcounter    | reg   [31:0] |                                                                                                                                                                                                                                                             |
| pps_rcounter     | reg   [31:0] |                                                                                                                                                                                                                                                             |
| pps_status       | reg          |                                                                                                                                                                                                                                                             |
| pps_posedge_s    | wire         |                                                                                                                                                                                                                                                             |
| up_pps_posedge_s | wire         |                                                                                                                                                                                                                                                             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 gps_pps is asynchronous from the clk 
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
**Description**
 up_tdd_pps_rcounter CDC 
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
**Description**
 IRQ generation 
