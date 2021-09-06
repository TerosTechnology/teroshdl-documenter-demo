# Entity: axi_ad9162

- **File**: axi_ad9162.v
## Diagram

![Diagram](axi_ad9162.svg "Diagram")
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

| Generic name            | Type | Value | Description |
| ----------------------- | ---- | ----- | ----------- |
| ID                      |      | 0     |             |
| FPGA_TECHNOLOGY         |      | 0     |             |
| FPGA_FAMILY             |      | 0     |             |
| SPEED_GRADE             |      | 0     |             |
| DEV_PACKAGE             |      | 0     |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 16    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 16    |             |
| DAC_DATAPATH_DISABLE    |      | 0     |             |
## Ports

| Port name     | Direction | Type    | Description                               |
| ------------- | --------- | ------- | ----------------------------------------- |
| tx_clk        | input     |         |  jesd interface tx_clk is (line-rate/40)  |
| tx_valid      | output    |         |                                           |
| tx_data       | output    | [255:0] |                                           |
| tx_ready      | input     |         |                                           |
| dac_clk       | output    |         |  dma interface                            |
| dac_valid     | output    |         |                                           |
| dac_enable    | output    |         |                                           |
| dac_ddata     | input     | [255:0] |                                           |
| dac_dunf      | input     |         |                                           |
| s_axi_aclk    | input     |         |  axi interface                            |
| s_axi_aresetn | input     |         |                                           |
| s_axi_awvalid | input     |         |                                           |
| s_axi_awaddr  | input     | [ 15:0] |                                           |
| s_axi_awprot  | input     | [ 2:0]  |                                           |
| s_axi_awready | output    |         |                                           |
| s_axi_wvalid  | input     |         |                                           |
| s_axi_wdata   | input     | [ 31:0] |                                           |
| s_axi_wstrb   | input     | [ 3:0]  |                                           |
| s_axi_wready  | output    |         |                                           |
| s_axi_bvalid  | output    |         |                                           |
| s_axi_bresp   | output    | [ 1:0]  |                                           |
| s_axi_bready  | input     |         |                                           |
| s_axi_arvalid | input     |         |                                           |
| s_axi_araddr  | input     | [ 15:0] |                                           |
| s_axi_arprot  | input     | [ 2:0]  |                                           |
| s_axi_arready | output    |         |                                           |
| s_axi_rvalid  | output    |         |                                           |
| s_axi_rdata   | output    | [ 31:0] |                                           |
| s_axi_rresp   | output    | [ 1:0]  |                                           |
| s_axi_rready  | input     |         |                                           |
## Signals

| Name       | Type         | Description                  |
| ---------- | ------------ | ---------------------------- |
| dac_rst    | wire         |  internal clocks and resets  |
| up_clk     | wire         |                              |
| up_rstn    | wire         |                              |
| dac_data_s | wire [255:0] |  internal signals            |
| up_wreq_s  | wire         |                              |
| up_waddr_s | wire [ 13:0] |                              |
| up_wdata_s | wire [ 31:0] |                              |
| up_wack_s  | wire         |                              |
| up_rreq_s  | wire         |                              |
| up_raddr_s | wire [ 13:0] |                              |
| up_rdata_s | wire [ 31:0] |                              |
| up_rack_s  | wire         |                              |
## Instantiations

- i_if: axi_ad9162_if
</br>**Description**
 device interface

- i_core: axi_ad9162_core
</br>**Description**
 core

- i_up_axi: up_axi
</br>**Description**
 up bus interface

