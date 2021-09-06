# Entity: axi_ad9467

- **File**: axi_ad9467.v
## Diagram

![Diagram](axi_ad9467.svg "Diagram")
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

| Generic name           | Type | Value                | Description |
| ---------------------- | ---- | -------------------- | ----------- |
| ID                     |      | 0                    |             |
| FPGA_TECHNOLOGY        |      | 0                    |             |
| FPGA_FAMILY            |      | 0                    |             |
| SPEED_GRADE            |      | 0                    |             |
| DEV_PACKAGE            |      | 0                    |             |
| IO_DELAY_GROUP         |      | "dev_if_delay_group" |             |
| DELAY_REFCLK_FREQUENCY |      | 200                  |             |
## Ports

| Port name     | Direction | Type   | Description         |
| ------------- | --------- | ------ | ------------------- |
| adc_clk_in_p  | input     |        |  physical interface |
| adc_clk_in_n  | input     |        |                     |
| adc_data_in_p | input     | [ 7:0] |                     |
| adc_data_in_n | input     | [ 7:0] |                     |
| adc_or_in_p   | input     |        |                     |
| adc_or_in_n   | input     |        |                     |
| delay_clk     | input     |        |  delay_clock        |
| adc_clk       | output    |        |  dma interface      |
| adc_valid     | output    |        |                     |
| adc_enable    | output    |        |                     |
| adc_data      | output    | [15:0] |                     |
| adc_dovf      | input     |        |                     |
| s_axi_aclk    | input     |        |  axi interface      |
| s_axi_aresetn | input     |        |                     |
| s_axi_awvalid | input     |        |                     |
| s_axi_awaddr  | input     | [15:0] |                     |
| s_axi_awprot  | input     | [ 2:0] |                     |
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
| s_axi_arprot  | input     | [ 2:0] |                     |
| s_axi_arready | output    |        |                     |
| s_axi_rvalid  | output    |        |                     |
| s_axi_rresp   | output    | [ 1:0] |                     |
| s_axi_rdata   | output    | [31:0] |                     |
| s_axi_rready  | input     |        |                     |
## Signals

| Name               | Type           | Description                |
| ------------------ | -------------- | -------------------------- |
| up_wack            | reg            |  internal registers        |
| up_rdata           | reg     [31:0] |                            |
| up_rack            | reg            |                            |
| adc_rst            | wire           |  internal clocks & resets  |
| up_clk             | wire           |                            |
| up_rstn            | wire           |                            |
| delay_rst          | wire           |                            |
| adc_data_s         | wire [15:0]    |  internal signals          |
| adc_or_s           | wire           |                            |
| adc_ddr_edgesel_s  | wire           |                            |
| up_dld_s           | wire [ 8:0]    |                            |
| up_dwdata_s        | wire [44:0]    |                            |
| up_drdata_s        | wire [44:0]    |                            |
| delay_locked_s     | wire           |                            |
| up_status_pn_err_s | wire           |                            |
| up_status_pn_oos_s | wire           |                            |
| up_status_or_s     | wire           |                            |
| up_rreq_s          | wire           |                            |
| up_raddr_s         | wire [13:0]    |                            |
| up_rdata_s         | wire [31:0]    |                            |
| up_rack_s          | wire           |                            |
| up_wack_s          | wire           |                            |
| up_wreq_s          | wire           |                            |
| up_waddr_s         | wire [13:0]    |                            |
| up_wdata_s         | wire [31:0]    |                            |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_if: axi_ad9467_if
**Description**
 main (device interface)

- i_channel: axi_ad9467_channel
**Description**
 channel

- i_delay_cntrl: up_delay_cntrl
**Description**
 adc delay control

- i_up_adc_common: up_adc_common
**Description**
 common processor control

- i_up_axi: up_axi
**Description**
 up bus interface

