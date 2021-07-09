# Entity: axi_ad9625_if

## Diagram

![Diagram](axi_ad9625_if.svg "Diagram")
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
## Ports

| Port name     | Direction | Type    | Description                             |
| ------------- | --------- | ------- | --------------------------------------- |
| rx_clk        | input     |         | jesd interfacerx_clk is (line-rate/40)  |
| rx_sof        | input     | [  3:0] |                                         |
| rx_data       | input     | [255:0] |                                         |
| adc_clk       | output    |         | adc data output                         |
| adc_rst       | input     |         |                                         |
| adc_data      | output    | [191:0] |                                         |
| adc_or        | output    |         |                                         |
| adc_status    | output    |         |                                         |
| adc_sref      | output    | [ 15:0] |                                         |
| adc_sref_sync | input     |         |                                         |
| adc_raddr_in  | input     | [  3:0] |                                         |
| adc_raddr_out | output    | [  3:0] |                                         |
## Signals

| Name           | Type                | Description         |
| -------------- | ------------------- | ------------------- |
| adc_data_int   | reg         [191:0] | internal registers  |
| adc_status_int | reg                 |                     |
| adc_sref_int   | reg         [ 15:0] |                     |
| adc_data_cur   | reg         [191:0] |                     |
| adc_data_prv   | reg         [191:0] |                     |
| adc_waddr      | reg         [  3:0] |                     |
| adc_wdata      | reg         [191:0] |                     |
| adc_raddr      | reg         [  3:0] |                     |
| adc_rdata_s    | wire [191:0]        | internal signals    |
| adc_raddr_s    | wire [  3:0]        |                     |
| adc_sref_s     | wire [ 15:0]        |                     |
| adc_data_s     | wire [191:0]        |                     |
| adc_data_s15_s | wire [ 15:0]        |                     |
| adc_data_s14_s | wire [ 15:0]        |                     |
| adc_data_s13_s | wire [ 15:0]        |                     |
| adc_data_s12_s | wire [ 15:0]        |                     |
| adc_data_s11_s | wire [ 15:0]        |                     |
| adc_data_s10_s | wire [ 15:0]        |                     |
| adc_data_s09_s | wire [ 15:0]        |                     |
| adc_data_s08_s | wire [ 15:0]        |                     |
| adc_data_s07_s | wire [ 15:0]        |                     |
| adc_data_s06_s | wire [ 15:0]        |                     |
| adc_data_s05_s | wire [ 15:0]        |                     |
| adc_data_s04_s | wire [ 15:0]        |                     |
| adc_data_s03_s | wire [ 15:0]        |                     |
| adc_data_s02_s | wire [ 15:0]        |                     |
| adc_data_s01_s | wire [ 15:0]        |                     |
| adc_data_s00_s | wire [ 15:0]        |                     |
| rx_data0_s     | wire [ 31:0]        |                     |
| rx_data1_s     | wire [ 31:0]        |                     |
| rx_data2_s     | wire [ 31:0]        |                     |
| rx_data3_s     | wire [ 31:0]        |                     |
| rx_data4_s     | wire [ 31:0]        |                     |
| rx_data5_s     | wire [ 31:0]        |                     |
| rx_data6_s     | wire [ 31:0]        |                     |
| rx_data7_s     | wire [ 31:0]        |                     |
| rx_data_s      | wire [255:0]        |                     |
## Processes
- unnamed: ( @(posedge rx_clk) )
- unnamed: ( @(posedge rx_clk) )
**Description**
status

## Instantiations

- i_mem: ad_mem
**Description**
alignment fifo

