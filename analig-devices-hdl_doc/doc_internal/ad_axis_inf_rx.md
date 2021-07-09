# Entity: ad_axis_inf_rx

## Diagram

![Diagram](ad_axis_inf_rx.svg "Diagram")
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

| Port name | Direction | Type               | Description      |
| --------- | --------- | ------------------ | ---------------- |
| clk       | input     |                    | adi interface    |
| rst       | input     |                    |                  |
| valid     | input     |                    |                  |
| last      | input     |                    |                  |
| data      | input     | [(DATA_WIDTH-1):0] |                  |
| inf_valid | output    |                    | xilinx interface |
| inf_last  | output    |                    |                  |
| inf_data  | output    | [(DATA_WIDTH-1):0] |                  |
| inf_ready | input     |                    |                  |
## Signals

| Name        | Type                       | Description         |
| ----------- | -------------------------- | ------------------- |
| wcnt        | reg     [ 2:0]             | internal registers  |
| wlast_0     | reg                        |                     |
| wdata_0     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_1     | reg                        |                     |
| wdata_1     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_2     | reg                        |                     |
| wdata_2     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_3     | reg                        |                     |
| wdata_3     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_4     | reg                        |                     |
| wdata_4     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_5     | reg                        |                     |
| wdata_5     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_6     | reg                        |                     |
| wdata_6     | reg     [(DATA_WIDTH-1):0] |                     |
| wlast_7     | reg                        |                     |
| wdata_7     | reg     [(DATA_WIDTH-1):0] |                     |
| rcnt        | reg     [ 2:0]             |                     |
| inf_ready_s | wire                       | internal signals    |
| inf_last_s  | reg                        |                     |
| inf_data_s  | reg     [(DATA_WIDTH-1):0] |                     |
## Processes
- unnamed: ( @(posedge clk) )
**Description**
write interface

- unnamed: ( @(rcnt or wlast_0 or wdata_0 or wlast_1 or wdata_1 or )
- unnamed: ( @(posedge clk) )
