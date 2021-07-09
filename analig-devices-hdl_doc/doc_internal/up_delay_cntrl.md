# Entity: up_delay_cntrl

## Diagram

![Diagram](up_delay_cntrl.svg "Diagram")
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DISABLE      |      | 0     | parameters  |
| INIT_DELAY   |      | 0     |             |
| DATA_WIDTH   |      | 8     |             |
| DRP_WIDTH    |      | 5     |             |
| BASE_ADDRESS |      | 6'h02 |             |
## Ports

| Port name    | Direction | Type                           | Description         |
| ------------ | --------- | ------------------------------ | ------------------- |
| delay_clk    | input     |                                | delay interface     |
| delay_rst    | output    |                                |                     |
| delay_locked | input     |                                |                     |
| up_dld       | output    | [(DATA_WIDTH-1):0]             | io interface        |
| up_dwdata    | output    | [((DATA_WIDTH*DRP_WIDTH)-1):0] |                     |
| up_drdata    | input     | [((DATA_WIDTH*DRP_WIDTH)-1):0] |                     |
| up_rstn      | input     |                                | processor interface |
| up_clk       | input     |                                |                     |
| up_wreq      | input     |                                |                     |
| up_waddr     | input     | [13:0]                         |                     |
| up_wdata     | input     | [31:0]                         |                     |
| up_wack      | output    |                                |                     |
| up_rreq      | input     |                                |                     |
| up_raddr     | input     | [13:0]                         |                     |
| up_rdata     | output    | [31:0]                         |                     |
| up_rack      | output    |                                |                     |
