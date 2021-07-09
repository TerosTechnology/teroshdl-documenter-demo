# Entity: axi_mc_speed

## Diagram

![Diagram](axi_mc_speed.svg "Diagram")
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
 
## Ports

| Port name     | Direction | Type   | Description        |
| ------------- | --------- | ------ | ------------------ |
| position_i    | input     | [2:0]  | physical interface |
| position_o    | output    | [2:0]  |                    |
| speed_o       | output    | [31:0] |                    |
| new_speed_o   | output    |        |                    |
| hall_bemf_i   | input     | [1:0]  |                    |
| ref_clk       | input     |        |                    |
| s_axi_aclk    | input     |        | axi interface      |
| s_axi_aresetn | input     |        |                    |
| s_axi_awvalid | input     |        |                    |
| s_axi_awaddr  | input     | [15:0] |                    |
| s_axi_awready | output    |        |                    |
| s_axi_wvalid  | input     |        |                    |
| s_axi_wdata   | input     | [31:0] |                    |
| s_axi_wstrb   | input     | [ 3:0] |                    |
| s_axi_wready  | output    |        |                    |
| s_axi_bvalid  | output    |        |                    |
| s_axi_bresp   | output    | [ 1:0] |                    |
| s_axi_bready  | input     |        |                    |
| s_axi_arvalid | input     |        |                    |
| s_axi_araddr  | input     | [15:0] |                    |
| s_axi_arready | output    |        |                    |
| s_axi_rvalid  | output    |        |                    |
| s_axi_rresp   | output    | [ 1:0] |                    |
| s_axi_rdata   | output    | [31:0] |                    |
| s_axi_rready  | input     |        |                    |
| s_axi_awprot  | input     | [ 2:0] |                    |
| s_axi_arprot  | input     | [ 2:0] |                    |
## Signals

| Name                  | Type           | Description               |
| --------------------- | -------------- | ------------------------- |
| up_rdata              | reg     [31:0] |                           |
| up_wack               | reg            |                           |
| up_rack               | reg            |                           |
| adc_rst               | wire           | internal clocks & resets  |
| up_rstn               | wire           |                           |
| up_clk                | wire           |                           |
| speed_data_s          | wire [31:0]    | internal signals          |
| adc_enable_s          | wire           |                           |
| adc_status_s          | wire           |                           |
| up_rreq_s             | wire           |                           |
| up_wreq_s             | wire           |                           |
| up_waddr_s            | wire [13:0]    |                           |
| up_raddr_s            | wire [13:0]    |                           |
| up_wdata_s            | wire [31:0]    |                           |
| up_adc_common_rdata_s | wire [31:0]    |                           |
| up_adc_common_wack_s  | wire           |                           |
| up_adc_common_rack_s  | wire           |                           |
| pid_s                 | wire [31:0]    |                           |
| position_s            | wire [ 2:0]    |                           |
| bemf_s                | wire [ 2:0]    |                           |
| bemf_delayed_s        | wire [ 2:0]    |                           |
| new_speed_s           | wire           |                           |
| bemf_multiplex_s      | wire [ 2:0]    |                           |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- position_0: debouncer
**Description**
HALL sensors debouncers

- position_1: debouncer
- position_2: debouncer
- delay_30_degrees_i1: delay_30_degrees
- speed_detector_inst: speed_detector
- i_up_adc_common: up_adc_common
**Description**
common processor control

- i_up_axi: up_axi
**Description**
up bus interface

