# Entity: axi_hdmi_rx_es

- **File**: axi_hdmi_rx_es.v
## Diagram

![Diagram](axi_hdmi_rx_es.svg "Diagram")
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
 Receive HDMI, hdmi embedded syncs data in, video dma data out.

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_WIDTH   |      | 32    |             |
## Ports

| Port name    | Direction | Type               | Description     |
| ------------ | --------- | ------------------ | --------------- |
| hdmi_clk     | input     |                    |  hdmi interface |
| hdmi_data    | input     | [(DATA_WIDTH-1):0] |                 |
| hdmi_vs_de   | output    |                    |                 |
| hdmi_hs_de   | output    |                    |                 |
| hdmi_data_de | output    | [(DATA_WIDTH-1):0] |                 |
## Signals

| Name              | Type                       | Description          |
| ----------------- | -------------------------- | -------------------- |
| hdmi_data_d       | reg     [(DATA_WIDTH-1):0] |  internal registers  |
| hdmi_hs_de_rcv_d  | reg                        |                      |
| hdmi_vs_de_rcv_d  | reg                        |                      |
| hdmi_data_2d      | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_rcv_2d | reg                        |                      |
| hdmi_vs_de_rcv_2d | reg                        |                      |
| hdmi_data_3d      | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_rcv_3d | reg                        |                      |
| hdmi_vs_de_rcv_3d | reg                        |                      |
| hdmi_data_4d      | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_rcv_4d | reg                        |                      |
| hdmi_vs_de_rcv_4d | reg                        |                      |
| hdmi_preamble_cnt | reg     [ 1:0]             |                      |
| hdmi_hs_de_rcv    | reg                        |                      |
| hdmi_vs_de_rcv    | reg                        |                      |
| hdmi_ff_s         | wire [(DATA_WIDTH-1):0]    |  internal signals    |
| hdmi_00_s         | wire [(DATA_WIDTH-1):0]    |                      |
| hdmi_b6_s         | wire [(DATA_WIDTH-1):0]    |                      |
| hdmi_9d_s         | wire [(DATA_WIDTH-1):0]    |                      |
| hdmi_ab_s         | wire [(DATA_WIDTH-1):0]    |                      |
| hdmi_80_s         | wire [(DATA_WIDTH-1):0]    |                      |
## Constants

| Name       | Type | Value        | Description |
| ---------- | ---- | ------------ | ----------- |
| BYTE_WIDTH |      | DATA_WIDTH/8 |             |
## Processes
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
**Description**
 delay to get rid of eav's 4 bytes 
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
**Description**
 check for sav and eav and generate the corresponding enables 
