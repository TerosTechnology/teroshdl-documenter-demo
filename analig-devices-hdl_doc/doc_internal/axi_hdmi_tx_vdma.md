# Entity: axi_hdmi_tx_vdma

- **File**: axi_hdmi_tx_vdma.v
## Diagram

![Diagram](axi_hdmi_tx_vdma.svg "Diagram")
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
 
## Ports

| Port name          | Direction | Type   | Description    |
| ------------------ | --------- | ------ | -------------- |
| hdmi_fs_toggle     | input     |        | hdmi interface |
| hdmi_raddr_g       | input     | [ 8:0] |                |
| vdma_clk           | input     |        | vdma interface |
| vdma_rst           | input     |        |                |
| vdma_end_of_frame  | input     |        |                |
| vdma_valid         | input     |        |                |
| vdma_data          | input     | [63:0] |                |
| vdma_ready         | output    |        |                |
| vdma_wr            | output    |        |                |
| vdma_waddr         | output    | [ 8:0] |                |
| vdma_wdata         | output    | [47:0] |                |
| vdma_fs_ret_toggle | output    |        |                |
| vdma_fs_waddr      | output    | [ 8:0] |                |
| vdma_tpm_oos       | output    |        |                |
| vdma_ovf           | output    |        |                |
| vdma_unf           | output    |        |                |
## Signals

| Name                | Type           | Description         |
| ------------------- | -------------- | ------------------- |
| vdma_fs_toggle_m1   | reg            | internal registers  |
| vdma_fs_toggle_m2   | reg            |                     |
| vdma_fs_toggle_m3   | reg            |                     |
| vdma_tpm_data       | reg     [22:0] |                     |
| vdma_raddr_g_m1     | reg     [ 8:0] |                     |
| vdma_raddr_g_m2     | reg     [ 8:0] |                     |
| vdma_raddr          | reg     [ 8:0] |                     |
| vdma_addr_diff      | reg     [ 8:0] |                     |
| vdma_almost_full    | reg            |                     |
| vdma_almost_empty   | reg            |                     |
| hdmi_fs             | reg            |                     |
| vdma_fs             | reg            |                     |
| vdma_end_of_frame_d | reg            |                     |
| vdma_active_frame   | reg            |                     |
| vdma_tpm_data_s     | wire [47:0]    | internal wires      |
| vdma_tpm_oos_s      | wire           |                     |
| vdma_addr_diff_s    | wire [ 9:0]    |                     |
| vdma_ovf_s          | wire           |                     |
| vdma_unf_s          | wire           |                     |
## Constants

| Name             | Type | Value  | Description |
| ---------------- | ---- | ------ | ----------- |
| BUF_THRESHOLD_LO |      | 9'd3   |             |
| BUF_THRESHOLD_HI |      | 9'd509 |             |
| RDY_THRESHOLD_LO |      | 9'd450 |             |
| RDY_THRESHOLD_HI |      | 9'd500 |             |
## Functions
- g2b <font id="function_arguments">()</font> <font id="function_return">return ([8:0])</font>
**Description**
grey to binary conversion

## Processes
- unnamed: ( @(posedge vdma_clk) )
**Description**
hdmi frame sync

- unnamed: ( @(posedge vdma_clk) )
**Description**
dma frame sync

- unnamed: ( @(posedge vdma_clk) )
**Description**
sync dma and hdmi frames

- unnamed: ( @(posedge vdma_clk) )
**Description**
accept new frame from dma

- unnamed: ( @(posedge vdma_clk) )
**Description**
vdma write

- unnamed: ( @(posedge vdma_clk) )
- unnamed: ( @(posedge vdma_clk) )
- unnamed: ( @(posedge vdma_clk) )
