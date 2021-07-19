# Entity: up_xfer_status

- **File**: up_xfer_status.v
## Diagram

![Diagram](up_xfer_status.svg "Diagram")
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
| DATA_WIDTH   |      | 8     |             |
## Ports

| Port name      | Direction | Type               | Description      |
| -------------- | --------- | ------------------ | ---------------- |
| up_rstn        | input     |                    | up interface     |
| up_clk         | input     |                    |                  |
| up_data_status | output    | [(DATA_WIDTH-1):0] |                  |
| d_rst          | input     |                    | device interface |
| d_clk          | input     |                    |                  |
| d_data_status  | input     | [(DATA_WIDTH-1):0] |                  |
## Signals

| Name               | Type                       | Description         |
| ------------------ | -------------------------- | ------------------- |
| d_xfer_state_m1    | reg                        | internal registers  |
| d_xfer_state_m2    | reg                        |                     |
| d_xfer_state       | reg                        |                     |
| d_xfer_count       | reg     [ 5:0]             |                     |
| d_xfer_toggle      | reg                        |                     |
| d_xfer_data        | reg     [(DATA_WIDTH-1):0] |                     |
| d_acc_data         | reg     [(DATA_WIDTH-1):0] |                     |
| up_xfer_toggle_m1  | reg                        |                     |
| up_xfer_toggle_m2  | reg                        |                     |
| up_xfer_toggle_m3  | reg                        |                     |
| up_xfer_toggle     | reg                        |                     |
| up_data_status_int | reg     [(DATA_WIDTH-1):0] |                     |
| d_xfer_enable_s    | wire                       | internal signals    |
| up_xfer_toggle_s   | wire                       |                     |
## Processes
- unnamed: ( @(posedge d_clk or posedge d_rst) )
- unnamed: ( @(posedge up_clk) )
