# Entity: axi_hdmi_rx_core

- **File**: axi_hdmi_rx_core.v
## Diagram

![Diagram](axi_hdmi_rx_core.svg "Diagram")
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
| IO_INTERFACE |      | 1     |             |
## Ports

| Port name        | Direction | Type   | Description     |
| ---------------- | --------- | ------ | --------------- |
| hdmi_clk         | input     |        |  hdmi interface |
| hdmi_rst         | input     |        |                 |
| hdmi_data        | input     | [15:0] |                 |
| hdmi_edge_sel    | input     |        |                 |
| hdmi_bgr         | input     |        |                 |
| hdmi_packed      | input     |        |                 |
| hdmi_csc_bypass  | input     |        |                 |
| hdmi_vs_count    | input     | [15:0] |                 |
| hdmi_hs_count    | input     | [15:0] |                 |
| hdmi_tpm_oos     | output    |        |                 |
| hdmi_vs_oos      | output    |        |                 |
| hdmi_hs_oos      | output    |        |                 |
| hdmi_vs_mismatch | output    |        |                 |
| hdmi_hs_mismatch | output    |        |                 |
| hdmi_vs          | output    | [15:0] |                 |
| hdmi_hs          | output    | [15:0] |                 |
| hdmi_dma_sof     | output    |        |  dma interface  |
| hdmi_dma_de      | output    |        |                 |
| hdmi_dma_data    | output    | [63:0] |                 |
## Signals

| Name               | Type               | Description          |
| ------------------ | ------------------ | -------------------- |
| hdmi_dma_de_cnt    | reg                |  internal registers  |
| hdmi_dma_sof_int   | reg                |                      |
| hdmi_dma_de_int    | reg                |                      |
| hdmi_dma_data_int  | reg         [31:0] |                      |
| hdmi_sof_422       | reg                |                      |
| hdmi_de_422        | reg                |                      |
| hdmi_de_422_cnt    | reg                |                      |
| hdmi_data_422      | reg         [15:0] |                      |
| hdmi_sof_444       | reg                |                      |
| hdmi_de_444        | reg                |                      |
| hdmi_data_444      | reg         [23:0] |                      |
| hdmi_de_444_cnt    | reg         [ 1:0] |                      |
| hdmi_data_444_hold | reg         [15:0] |                      |
| hdmi_sof_444_p     | reg                |                      |
| hdmi_de_444_p      | reg                |                      |
| hdmi_data_444_p    | reg         [31:0] |                      |
| hdmi_dma_enable    | reg                |                      |
| hdmi_hs_de_d       | reg                |                      |
| hdmi_vs_de_d       | reg                |                      |
| hdmi_sof           | reg                |                      |
| hdmi_hs_rcv        | reg         [15:0] |                      |
| hdmi_hs_cur        | reg         [15:0] |                      |
| hdmi_hs_oos_int    | reg                |                      |
| hdmi_vs_rcv        | reg         [15:0] |                      |
| hdmi_vs_cur        | reg         [15:0] |                      |
| hdmi_vs_oos_int    | reg                |                      |
| hdmi_data_p        | reg         [15:0] |                      |
| hdmi_data_p_s      | wire [15:0]        |  internal signals    |
| hdmi_data_n_s      | wire [15:0]        |                      |
| hdmi_sof_s         | wire               |                      |
| hdmi_sof_ss_s      | wire               |                      |
| hdmi_de_ss_s       | wire               |                      |
| hdmi_data_ss_s     | wire [23:0]        |                      |
| hdmi_sof_444_s     | wire               |                      |
| hdmi_de_444_s      | wire               |                      |
| hdmi_data_444_s    | wire [23:0]        |                      |
| hdmi_data_de_s     | wire [15:0]        |                      |
| hdmi_hs_de_s       | wire               |                      |
| hdmi_vs_de_s       | wire               |                      |
## Processes
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
</br>**Description**
 dma interface 
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
</br>**Description**
 32 bit interface 
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
</br>**Description**
 sof, enable and data on 422 and 444 domains 
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
</br>**Description**
 horizontal and vertical sync counters, active video size & mismatch 
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
- unnamed: ( @(posedge hdmi_clk) )
  - **Type:** always
## Instantiations

- i_ss: ad_ss_422to444
</br>**Description**
 super sampling, 422 to 444

- i_csc: ad_csc_CrYCb2RGB
</br>**Description**
 color space conversion, CrYCb to RGB

- i_es: axi_hdmi_rx_es
</br>**Description**
 embedded sync

- i_tpm: axi_hdmi_rx_tpm
</br>**Description**
 test pattern matcher

