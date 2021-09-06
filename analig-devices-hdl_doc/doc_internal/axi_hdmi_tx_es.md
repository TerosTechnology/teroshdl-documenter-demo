# Entity: axi_hdmi_tx_es

- **File**: axi_hdmi_tx_es.v
## Diagram

![Diagram](axi_hdmi_tx_es.svg "Diagram")
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
 Transmit HDMI, video dma data in, hdmi separate syncs data out.

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| DATA_WIDTH   |      | 32    |             |
## Ports

| Port name    | Direction | Type               | Description     |
| ------------ | --------- | ------------------ | --------------- |
| hdmi_clk     | input     |                    |  hdmi interface |
| hdmi_hs_de   | input     |                    |                 |
| hdmi_vs_de   | input     |                    |                 |
| hdmi_data_de | input     | [(DATA_WIDTH-1):0] |                 |
| hdmi_data    | output    | [(DATA_WIDTH-1):0] |                 |
## Signals

| Name          | Type                       | Description          |
| ------------- | -------------------------- | -------------------- |
| hdmi_hs_de_d  | reg                        |  internal registers  |
| hdmi_data_d   | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_2d | reg                        |                      |
| hdmi_data_2d  | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_3d | reg                        |                      |
| hdmi_data_3d  | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_4d | reg                        |                      |
| hdmi_data_4d  | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_hs_de_5d | reg                        |                      |
| hdmi_data_5d  | reg     [(DATA_WIDTH-1):0] |                      |
| hdmi_sav_s    | wire [(DATA_WIDTH-1):0]    |  internal wires      |
| hdmi_eav_s    | wire [(DATA_WIDTH-1):0]    |                      |
## Constants

| Name       | Type | Value        | Description |
| ---------- | ---- | ------------ | ----------- |
| BYTE_WIDTH |      | DATA_WIDTH/8 |             |
## Processes
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
