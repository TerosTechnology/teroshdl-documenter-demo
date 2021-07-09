# Entity: axi_ad9265_if

## Diagram

![Diagram](axi_ad9265_if.svg "Diagram")
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
 This is the LVDS/DDR interface, note that overrange is independent of data path,
 software will not be able to relate overrange to a specific sample!
 
## Generics

| Generic name           | Type | Value                | Description |
| ---------------------- | ---- | -------------------- | ----------- |
| FPGA_TECHNOLOGY        |      | 0                    |             |
| IO_DELAY_GROUP         |      | "adc_if_delay_group" |             |
| DELAY_REFCLK_FREQUENCY |      | 200                  |             |
## Ports

| Port name     | Direction | Type   | Description                                                                |
| ------------- | --------- | ------ | -------------------------------------------------------------------------- |
| adc_clk_in_p  | input     |        | adc interface (clk, data, over-range)nominal clock 125 MHz, up to 300 MHz  |
| adc_clk_in_n  | input     |        |                                                                            |
| adc_data_in_p | input     | [ 7:0] |                                                                            |
| adc_data_in_n | input     | [ 7:0] |                                                                            |
| adc_or_in_p   | input     |        |                                                                            |
| adc_or_in_n   | input     |        |                                                                            |
| adc_clk       | output    |        | interface outputs                                                          |
| adc_data      | output    | [15:0] |                                                                            |
| adc_or        | output    |        |                                                                            |
| adc_status    | output    |        |                                                                            |
| up_clk        | input     |        | delay control signals                                                      |
| up_dld        | input     | [ 8:0] |                                                                            |
| up_dwdata     | input     | [44:0] |                                                                            |
| up_drdata     | output    | [44:0] |                                                                            |
| delay_clk     | input     |        |                                                                            |
| delay_rst     | input     |        |                                                                            |
| delay_locked  | output    |        |                                                                            |
## Signals

| Name         | Type           | Description         |
| ------------ | -------------- | ------------------- |
| adc_data_p   | reg     [ 7:0] | internal registers  |
| adc_data_n   | reg     [ 7:0] |                     |
| adc_or_p     | reg            |                     |
| adc_or_n     | reg            |                     |
| adc_data_p_s | wire [ 7:0]    | internal signals    |
| adc_data_n_s | wire [ 7:0]    |                     |
| adc_or_p_s   | wire           |                     |
| adc_or_n_s   | wire           |                     |
## Processes
- unnamed: ( @(posedge adc_clk) )
## Instantiations

- i_adc_or: ad_data_in
**Description**
over-range interface

- i_adc_clk: ad_data_clk
**Description**
clock

