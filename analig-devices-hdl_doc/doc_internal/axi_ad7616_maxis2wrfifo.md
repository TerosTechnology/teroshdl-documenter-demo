# Entity: axi_ad7616_maxis2wrfifo

## Diagram

![Diagram](axi_ad7616_maxis2wrfifo.svg "Diagram")
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
| DATA_WIDTH   |      | 16    |             |
## Ports

| Port name        | Direction | Type             | Description          |
| ---------------- | --------- | ---------------- | -------------------- |
| clk              | input     |                  |                      |
| rstn             | input     |                  |                      |
| sync_in          | input     |                  |                      |
| m_axis_data      | input     | [DATA_WIDTH-1:0] | m_axis interface     |
| m_axis_ready     | output    |                  |                      |
| m_axis_valid     | input     |                  |                      |
| m_axis_xfer_req  | output    |                  |                      |
| fifo_wr_en       | output    |                  | write fifo interface |
| fifo_wr_data     | output    | [DATA_WIDTH-1:0] |                      |
| fifo_wr_sync     | output    |                  |                      |
| fifo_wr_xfer_req | input     |                  |                      |
## Processes
- unnamed: ( @(posedge clk) )
