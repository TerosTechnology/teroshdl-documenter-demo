# Entity: axi_ad6676

- **File**: axi_ad6676.v
## Diagram

![Diagram](axi_ad6676.svg "Diagram")
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

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| ID              |      | 0     |             |
| NUM_LANES       |      | 2     |             |
| FPGA_TECHNOLOGY |      | 0     |             |
| FPGA_FAMILY     |      | 0     |             |
| SPEED_GRADE     |      | 0     |             |
| DEV_PACKAGE     |      | 0     |             |
## Ports

| Port name     | Direction | Type               | Description                             |
| ------------- | --------- | ------------------ | --------------------------------------- |
| rx_clk        | input     |                    | jesd interfacerx_clk is (line-rate/40)  |
| rx_sof        | input     | [ 3:0]             |                                         |
| rx_valid      | input     |                    |                                         |
| rx_ready      | output    |                    |                                         |
| rx_data       | input     | [32*NUM_LANES-1:0] |                                         |
| adc_clk       | output    |                    | dma interface                           |
| adc_valid_0   | output    |                    |                                         |
| adc_enable_0  | output    |                    |                                         |
| adc_data_0    | output    | [31:0]             |                                         |
| adc_valid_1   | output    |                    |                                         |
| adc_enable_1  | output    |                    |                                         |
| adc_data_1    | output    | [31:0]             |                                         |
| adc_dovf      | input     |                    |                                         |
| s_axi_aclk    | input     |                    | axi interface                           |
| s_axi_aresetn | input     |                    |                                         |
| s_axi_awvalid | input     |                    |                                         |
| s_axi_awaddr  | input     | [11:0]             |                                         |
| s_axi_awready | output    |                    |                                         |
| s_axi_wvalid  | input     |                    |                                         |
| s_axi_wdata   | input     | [31:0]             |                                         |
| s_axi_wstrb   | input     | [ 3:0]             |                                         |
| s_axi_wready  | output    |                    |                                         |
| s_axi_bvalid  | output    |                    |                                         |
| s_axi_bresp   | output    | [ 1:0]             |                                         |
| s_axi_bready  | input     |                    |                                         |
| s_axi_arvalid | input     |                    |                                         |
| s_axi_araddr  | input     | [11:0]             |                                         |
| s_axi_arready | output    |                    |                                         |
| s_axi_rvalid  | output    |                    |                                         |
| s_axi_rresp   | output    | [ 1:0]             |                                         |
| s_axi_rdata   | output    | [31:0]             |                                         |
| s_axi_rready  | input     |                    |                                         |
| s_axi_awprot  | input     | [ 2:0]             |                                         |
| s_axi_arprot  | input     | [ 2:0]             |                                         |
## Instantiations

- i_adc_jesd204: ad_ip_jesd204_tpl_adc
