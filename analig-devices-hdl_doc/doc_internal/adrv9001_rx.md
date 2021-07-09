# Entity: adrv9001_rx

## Diagram

![Diagram](adrv9001_rx.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2020 (c) Analog Devices, Inc. All rights reserved.
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

| Generic name    | Type | Value                | Description |
| --------------- | ---- | -------------------- | ----------- |
| CMOS_LVDS_N     |      | 0                    |             |
| FPGA_TECHNOLOGY |      | 0                    |             |
| NUM_LANES       |      | 3                    |             |
| DRP_WIDTH       |      | 5                    |             |
| IODELAY_CTRL    |      | 0                    |             |
| IO_DELAY_GROUP  |      | "dev_if_delay_group" |             |
## Ports

| Port name                | Direction | Type                      | Description                         |
| ------------------------ | --------- | ------------------------- | ----------------------------------- |
| rx_dclk_in_n_NC          | input     |                           | device interface                    |
| rx_dclk_in_p_dclk_in     | input     |                           |                                     |
| rx_idata_in_n_idata0     | input     |                           |                                     |
| rx_idata_in_p_idata1     | input     |                           |                                     |
| rx_qdata_in_n_qdata2     | input     |                           |                                     |
| rx_qdata_in_p_qdata3     | input     |                           |                                     |
| rx_strobe_in_n_NC        | input     |                           |                                     |
| rx_strobe_in_p_strobe_in | input     |                           |                                     |
| adc_rst                  | input     |                           | internal reset and clocks           |
| adc_clk                  | output    |                           |                                     |
| adc_clk_div              | output    |                           |                                     |
| adc_data_0               | output    | [7:0]                     |                                     |
| adc_data_1               | output    | [7:0]                     |                                     |
| adc_data_2               | output    | [7:0]                     |                                     |
| adc_data_3               | output    | [7:0]                     |                                     |
| adc_data_strobe          | output    | [7:0]                     |                                     |
| adc_valid                | output    |                           |                                     |
| adc_clk_ratio            | output    | [31:0]                    |                                     |
| up_clk                   | input     |                           | delay interface (for IDELAY macros) |
| up_adc_dld               | input     | [NUM_LANES-1:0]           |                                     |
| up_adc_dwdata            | input     | [DRP_WIDTH*NUM_LANES-1:0] |                                     |
| up_adc_drdata            | output    | [DRP_WIDTH*NUM_LANES-1:0] |                                     |
| delay_clk                | input     |                           |                                     |
| delay_rst                | input     |                           |                                     |
| delay_locked             | output    |                           |                                     |
| mssi_sync                | input     |                           |                                     |
| ssi_sync_out             | output    |                           |                                     |
| ssi_sync_in              | input     |                           |                                     |
| ssi_rst                  | output    |                           |                                     |
## Signals

| Name      | Type        | Description |
| --------- | ----------- | ----------- |
| valid_gen | reg [3:0]   |             |
| gpio_in   | wire [4:0]  |             |
| deser_out | wire [39:0] |             |
## Processes
- unnamed: ( @(posedge rx_clk) )
## Instantiations

- rx_clk_buf: periphery_clk_buf
