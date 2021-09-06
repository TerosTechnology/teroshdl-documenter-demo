# Entity: axi_dac_interpolate_filter

- **File**: axi_dac_interpolate_filter.v
## Diagram

![Diagram](axi_dac_interpolate_filter.svg "Diagram")
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

| Generic name       | Type | Value | Description |
| ------------------ | ---- | ----- | ----------- |
| CORRECTION_DISABLE |      | 1     |             |
## Ports

| Port name                  | Direction | Type   | Description |
| -------------------------- | --------- | ------ | ----------- |
| dac_clk                    | input     |        |             |
| dac_rst                    | input     |        |             |
| dac_data                   | input     | [15:0] |             |
| dac_valid                  | input     |        |             |
| dac_enable                 | input     |        |             |
| dac_int_data               | output    | [15:0] |             |
| dma_ready                  | output    |        |             |
| dac_valid_out              | output    |        |             |
| sync_stop_channels         | input     |        |             |
| underflow                  | output    |        |             |
| filter_mask                | input     | [ 2:0] |             |
| interpolation_ratio        | input     | [31:0] |             |
| dac_correction_coefficient | input     | [15:0] |             |
| dac_correction_enable      | input     |        |             |
| dma_transfer_suspend       | input     |        |             |
| start_sync_channels        | input     |        |             |
| trigger                    | input     |        |             |
| trigger_active             | input     |        |             |
| en_start_trigger           | input     |        |             |
| en_stop_trigger            | input     |        |             |
| dma_valid                  | input     |        |             |
| dma_valid_adjacent         | input     |        |             |
## Signals

| Name                    | Type           | Description        |
| ----------------------- | -------------- | ------------------ |
| dac_int_ready           | reg            |  internal signals  |
| dac_filt_int_valid      | reg            |                    |
| interp_rate_cic         | reg     [15:0] |                    |
| filter_mask_d1          | reg     [ 2:0] |                    |
| cic_change_rate         | reg            |                    |
| interpolation_counter   | reg     [31:0] |                    |
| transmit_ready          | reg            |                    |
| dma_data_valid          | reg            |                    |
| dma_data_valid_adjacent | reg            |                    |
| filter_enable           | reg            |                    |
| transfer                | reg            |                    |
| dma_valid_m             | reg     [15:0] |                    |
| stop_transfer           | reg            |                    |
| dac_valid_corrected     | wire           |                    |
| dac_data_corrected      | wire [15:0]    |                    |
| dac_fir_valid           | wire           |                    |
| dac_fir_data            | wire [35:0]    |                    |
| dac_cic_valid           | wire           |                    |
| dac_cic_data            | wire [109:0]   |                    |
| dma_valid_ch_sync       | wire           |                    |
| dma_valid_ch            | wire           |                    |
## Processes
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
</br>**Description**
 - for start synchronized, wait until the DMA has valid data on both channels  - for non synchronized channels the start of transmission gets the 2 data  paths randomly ready, only when using data buffers 
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
## Instantiations

- i_ad_iqcor: ad_iqcor
- fir_interpolation: fir_interp
- cic_interpolation: cic_interp
