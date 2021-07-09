# Entity: axi_hdmi_rx

## Diagram

![Diagram](axi_hdmi_rx.svg "Diagram")
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
| ID           |      | 0     |             |
| IO_INTERFACE |      | 1     |             |
## Ports

| Port name     | Direction | Type   | Description         |
| ------------- | --------- | ------ | ------------------- |
| hdmi_rx_clk   | input     |        | hdmi interface      |
| hdmi_rx_data  | input     | [15:0] |                     |
| hdmi_clk      | output    |        | dma interface       |
| hdmi_dma_sof  | output    |        |                     |
| hdmi_dma_de   | output    |        |                     |
| hdmi_dma_data | output    | [63:0] |                     |
| hdmi_dma_ovf  | input     |        |                     |
| hdmi_dma_unf  | input     |        |                     |
| s_axi_aclk    | input     |        | processor interface |
| s_axi_aresetn | input     |        |                     |
| s_axi_awvalid | input     |        |                     |
| s_axi_awaddr  | input     | [15:0] |                     |
| s_axi_awready | output    |        |                     |
| s_axi_wvalid  | input     |        |                     |
| s_axi_wdata   | input     | [31:0] |                     |
| s_axi_wstrb   | input     | [ 3:0] |                     |
| s_axi_wready  | output    |        |                     |
| s_axi_bvalid  | output    |        |                     |
| s_axi_bresp   | output    | [ 1:0] |                     |
| s_axi_bready  | input     |        |                     |
| s_axi_arvalid | input     |        |                     |
| s_axi_araddr  | input     | [15:0] |                     |
| s_axi_arready | output    |        |                     |
| s_axi_rvalid  | output    |        |                     |
| s_axi_rresp   | output    | [ 1:0] |                     |
| s_axi_rdata   | output    | [31:0] |                     |
| s_axi_rready  | input     |        |                     |
| s_axi_awprot  | input     | [ 2:0] |                     |
| s_axi_arprot  | input     | [ 2:0] |                     |
## Signals

| Name               | Type        | Description       |
| ------------------ | ----------- | ----------------- |
| up_wreq_s          | wire        | internal signals  |
| up_waddr_s         | wire [13:0] |                   |
| up_wdata_s         | wire [31:0] |                   |
| up_wack_s          | wire        |                   |
| up_rreq_s          | wire        |                   |
| up_raddr_s         | wire [13:0] |                   |
| up_rdata_s         | wire [31:0] |                   |
| up_rack_s          | wire        |                   |
| hdmi_edge_sel_s    | wire        |                   |
| hdmi_bgr_s         | wire        |                   |
| hdmi_packed_s      | wire        |                   |
| hdmi_csc_bypass_s  | wire        |                   |
| hdmi_vs_count_s    | wire [15:0] |                   |
| hdmi_hs_count_s    | wire [15:0] |                   |
| hdmi_tpm_oos_s     | wire        |                   |
| hdmi_vs_oos_s      | wire        |                   |
| hdmi_hs_oos_s      | wire        |                   |
| hdmi_vs_mismatch_s | wire        |                   |
| hdmi_hs_mismatch_s | wire        |                   |
| hdmi_vs_s          | wire [15:0] |                   |
| hdmi_hs_s          | wire [15:0] |                   |
| hdmi_rst           | wire        |                   |
| hdmi_data          | wire [15:0] |                   |
## Instantiations

- i_up_axi: up_axi
**Description**
axi interface

- i_up: up_hdmi_rx
**Description**
processor interface

- i_rx_core: axi_hdmi_rx_core
**Description**
hdmi interface

