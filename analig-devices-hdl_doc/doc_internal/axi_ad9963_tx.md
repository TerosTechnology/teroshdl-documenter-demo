# Entity: axi_ad9963_tx

- **File**: axi_ad9963_tx.v
## Diagram

![Diagram](axi_ad9963_tx.svg "Diagram")
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

| Generic name            | Type | Value | Description  |
| ----------------------- | ---- | ----- | ------------ |
| ID                      |      | 0     |  parameters  |
| FPGA_TECHNOLOGY         |      | 0     |              |
| FPGA_FAMILY             |      | 0     |              |
| SPEED_GRADE             |      | 0     |              |
| DEV_PACKAGE             |      | 0     |              |
| DAC_DDS_TYPE            |      | 1     |              |
| DAC_DDS_CORDIC_DW       |      | 14    |              |
| DAC_DDS_CORDIC_PHASE_DW |      | 13    |              |
| DATAPATH_DISABLE        |      | 0     |              |
## Ports

| Port name    | Direction | Type   | Description          |
| ------------ | --------- | ------ | -------------------- |
| dac_clk      | input     |        |  dac interface       |
| dac_rst      | output    |        |                      |
| dac_data     | output    | [23:0] |                      |
| adc_data     | input     | [23:0] |                      |
| dac_sync_in  | input     |        |  master/slave        |
| dac_sync_out | output    |        |                      |
| dac_enable_i | output    |        |  dma interface       |
| dac_valid_i  | output    |        |                      |
| dac_data_i   | input     | [15:0] |                      |
| dma_valid_i  | input     |        |                      |
| out_valid_i  | output    |        |                      |
| dac_enable_q | output    |        |                      |
| dac_valid_q  | output    |        |                      |
| dac_data_q   | input     | [15:0] |                      |
| dma_valid_q  | input     |        |                      |
| out_valid_q  | output    |        |                      |
| dac_dunf     | input     |        |                      |
| up_dac_ce    | output    |        |                      |
| up_rstn      | input     |        |  processor interface |
| up_clk       | input     |        |                      |
| up_wreq      | input     |        |                      |
| up_waddr     | input     | [13:0] |                      |
| up_wdata     | input     | [31:0] |                      |
| up_wack      | output    |        |                      |
| up_rreq      | input     |        |                      |
| up_raddr     | input     | [13:0] |                      |
| up_rdata     | output    | [31:0] |                      |
| up_rack      | output    |        |                      |
## Signals

| Name             | Type        | Description        |
| ---------------- | ----------- | ------------------ |
| dac_data_sync_s  | wire        |  internal signals  |
| dac_dds_format_s | wire        |                    |
| dac_data_int_s   | wire [23:0] |                    |
| up_rdata_s       | wire [31:0] |                    |
| up_rack_s        | wire        |                    |
| up_wack_s        | wire        |                    |
## Processes
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
</br>**Description**
 dma interface 
- unnamed: ( @(*) )
  - **Type:** always
</br>**Description**
 processor read interface 
## Instantiations

- i_tx_channel_0: axi_ad9963_tx_channel
</br>**Description**
 dac channel

- i_tx_channel_1: axi_ad9963_tx_channel
</br>**Description**
 dac channel

- i_up_dac_common: up_dac_common
</br>**Description**
 dac common processor interface

