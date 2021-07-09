# Entity: axi_ad9671_if

## Diagram

![Diagram](axi_ad9671_if.svg "Diagram")
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

| Generic name   | Type | Value | Description |
| -------------- | ---- | ----- | ----------- |
| QUAD_OR_DUAL_N |      | 1     |             |
| ID             |      | 0     |             |
## Ports

| Port name       | Direction | Type                       | Description                             |
| --------------- | --------- | -------------------------- | --------------------------------------- |
| rx_clk          | input     |                            | jesd interfacerx_clk is (line-rate/40)  |
| rx_sof          | input     | [ 3:0]                     |                                         |
| rx_data         | input     | [(64*QUAD_OR_DUAL_N)+63:0] |                                         |
| adc_clk         | output    |                            | adc data output                         |
| adc_rst         | input     |                            |                                         |
| adc_valid       | output    |                            |                                         |
| adc_data_a      | output    | [ 15:0]                    |                                         |
| adc_or_a        | output    |                            |                                         |
| adc_data_b      | output    | [ 15:0]                    |                                         |
| adc_or_b        | output    |                            |                                         |
| adc_data_c      | output    | [ 15:0]                    |                                         |
| adc_or_c        | output    |                            |                                         |
| adc_data_d      | output    | [ 15:0]                    |                                         |
| adc_or_d        | output    |                            |                                         |
| adc_data_e      | output    | [ 15:0]                    |                                         |
| adc_or_e        | output    |                            |                                         |
| adc_data_f      | output    | [ 15:0]                    |                                         |
| adc_or_f        | output    |                            |                                         |
| adc_data_g      | output    | [ 15:0]                    |                                         |
| adc_or_g        | output    |                            |                                         |
| adc_data_h      | output    | [ 15:0]                    |                                         |
| adc_or_h        | output    |                            |                                         |
| adc_start_code  | input     | [ 31:0]                    |                                         |
| adc_sync_in     | input     |                            |                                         |
| adc_sync_out    | output    |                            |                                         |
| adc_sync        | input     |                            |                                         |
| adc_sync_status | output    |                            |                                         |
| adc_status      | output    |                            |                                         |
| adc_raddr_in    | input     | [ 3:0]                     |                                         |
| adc_raddr_out   | output    | [ 3:0]                     |                                         |
## Signals

| Name         | Type                            | Description         |
| ------------ | ------------------------------- | ------------------- |
| rx_sof_s     | wire [(2*QUAD_OR_DUAL_N)+1:0]   | internal wires      |
| rx_data_s    | wire [(64*QUAD_OR_DUAL_N)+63:0] |                     |
| adc_wdata    | wire [127:0]                    |                     |
| adc_rdata    | wire [127:0]                    |                     |
| adc_data_a_s | wire [ 15:0]                    |                     |
| adc_data_b_s | wire [ 15:0]                    |                     |
| adc_data_c_s | wire [ 15:0]                    |                     |
| adc_data_d_s | wire [ 15:0]                    |                     |
| adc_data_e_s | wire [ 15:0]                    |                     |
| adc_data_f_s | wire [ 15:0]                    |                     |
| adc_data_g_s | wire [ 15:0]                    |                     |
| adc_data_h_s | wire [ 15:0]                    |                     |
| adc_raddr_s  | wire [  3:0]                    |                     |
| adc_sync_s   | wire                            |                     |
| int_valid    | reg                             | internal registers  |
| int_data     | reg     [127:0]                 |                     |
| rx_sof_d     | reg                             |                     |
| adc_waddr    | reg     [  3:0]                 |                     |
## Processes
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
## Instantiations

- i_mem: ad_mem
