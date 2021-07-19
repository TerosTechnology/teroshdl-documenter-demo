# Entity: axi_ad9371_rx_channel

- **File**: axi_ad9371_rx_channel.v
## Diagram

![Diagram](axi_ad9371_rx_channel.svg "Diagram")
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

| Generic name     | Type | Value | Description |
| ---------------- | ---- | ----- | ----------- |
| Q_OR_I_N         |      | 0     |             |
| COMMON_ID        |      | 0     |             |
| CHANNEL_ID       |      | 0     |             |
| DATAPATH_DISABLE |      | 0     |             |
| DATA_WIDTH       |      | 32    |             |
## Ports

| Port name       | Direction | Type               | Description         |
| --------------- | --------- | ------------------ | ------------------- |
| adc_clk         | input     |                    | adc interface       |
| adc_rst         | input     |                    |                     |
| adc_valid_in    | input     |                    |                     |
| adc_data_in     | input     | [(DATA_WIDTH-1):0] |                     |
| adc_valid_out   | output    |                    |                     |
| adc_data_out    | output    | [(DATA_WIDTH-1):0] |                     |
| adc_data_iq_in  | input     | [(DATA_WIDTH-1):0] |                     |
| adc_data_iq_out | output    | [(DATA_WIDTH-1):0] |                     |
| adc_enable      | output    |                    |                     |
| up_adc_pn_err   | output    |                    | channel interface   |
| up_adc_pn_oos   | output    |                    |                     |
| up_adc_or       | output    |                    |                     |
| up_rstn         | input     |                    | processor interface |
| up_clk          | input     |                    |                     |
| up_wreq         | input     |                    |                     |
| up_waddr        | input     | [13:0]             |                     |
| up_wdata        | input     | [31:0]             |                     |
| up_wack         | output    |                    |                     |
| up_rreq         | input     |                    |                     |
| up_raddr        | input     | [13:0]             |                     |
| up_rdata        | output    | [31:0]             |                     |
| up_rack         | output    |                    |                     |
## Signals

| Name                 | Type                        | Description       |
| -------------------- | --------------------------- | ----------------- |
| adc_dfmt_valid_s     | wire [(NUM_OF_SAMPLES-1):0] | internal signals  |
| adc_dfmt_data_s      | wire [(DATA_WIDTH-1):0]     |                   |
| adc_dcfilter_valid_s | wire [(NUM_OF_SAMPLES-1):0] |                   |
| adc_dcfilter_data_s  | wire [(DATA_WIDTH-1):0]     |                   |
| adc_valid_out_s      | wire [(NUM_OF_SAMPLES-1):0] |                   |
| adc_pn_err_s         | wire                        |                   |
| adc_pn_oos_s         | wire                        |                   |
| adc_dfmt_se_s        | wire                        |                   |
| adc_dfmt_type_s      | wire                        |                   |
| adc_dfmt_enable_s    | wire                        |                   |
| adc_dcfilt_enb_s     | wire                        |                   |
| adc_dcfilt_offset_s  | wire [15:0]                 |                   |
| adc_dcfilt_coeff_s   | wire [15:0]                 |                   |
| adc_iqcor_enb_s      | wire                        |                   |
| adc_iqcor_coeff_1_s  | wire [15:0]                 |                   |
| adc_iqcor_coeff_2_s  | wire [15:0]                 |                   |
## Constants

| Name           | Type | Value         | Description |
| -------------- | ---- | ------------- | ----------- |
| NUM_OF_SAMPLES |      | DATA_WIDTH/16 |             |
## Instantiations

- i_up_adc_channel: up_adc_channel
