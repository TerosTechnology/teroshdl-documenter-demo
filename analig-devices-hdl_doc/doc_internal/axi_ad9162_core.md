# Entity: axi_ad9162_core

- **File**: axi_ad9162_core.v
## Diagram

![Diagram](axi_ad9162_core.svg "Diagram")
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

| Generic name            | Type | Value | Description |
| ----------------------- | ---- | ----- | ----------- |
| ID                      |      | 0     |             |
| FPGA_TECHNOLOGY         |      | 0     |             |
| FPGA_FAMILY             |      | 0     |             |
| SPEED_GRADE             |      | 0     |             |
| DEV_PACKAGE             |      | 0     |             |
| DAC_DDS_TYPE            |      | 1     |             |
| DAC_DDS_CORDIC_DW       |      | 16    |             |
| DAC_DDS_CORDIC_PHASE_DW |      | 16    |             |
| DATAPATH_DISABLE        |      | 0     |             |
## Ports

| Port name  | Direction | Type    | Description          |
| ---------- | --------- | ------- | -------------------- |
| dac_clk    | input     |         |  dac interface       |
| dac_rst    | output    |         |                      |
| dac_data   | output    | [255:0] |                      |
| dac_valid  | output    |         |  dma interface       |
| dac_enable | output    |         |                      |
| dac_ddata  | input     | [255:0] |                      |
| dac_dunf   | input     |         |                      |
| up_rstn    | input     |         |  processor interface |
| up_clk     | input     |         |                      |
| up_wreq    | input     |         |                      |
| up_waddr   | input     | [ 13:0] |                      |
| up_wdata   | input     | [ 31:0] |                      |
| up_wack    | output    |         |                      |
| up_rreq    | input     |         |                      |
| up_raddr   | input     | [ 13:0] |                      |
| up_rdata   | output    | [ 31:0] |                      |
| up_rack    | output    |         |                      |
## Signals

| Name          | Type         | Description        |
| ------------- | ------------ | ------------------ |
| dac_sync_s    | wire         |  internal signals  |
| dac_datafmt_s | wire         |                    |
| up_rdata_0_s  | wire [ 31:0] |                    |
| up_rack_0_s   | wire         |                    |
| up_wack_0_s   | wire         |                    |
| up_rdata_s    | wire [ 31:0] |                    |
| up_rack_s     | wire         |                    |
| up_wack_s     | wire         |                    |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
  - **Type:** always
**Description**
 processor read interface 
## Instantiations

- i_channel_0: axi_ad9162_channel
**Description**
 dac channel

- i_up_dac_common: up_dac_common
**Description**
 dac common processor interface

