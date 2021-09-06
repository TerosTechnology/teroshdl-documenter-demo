# Entity: data_offload_regmap

- **File**: data_offload_regmap.v
## Diagram

![Diagram](data_offload_regmap.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.

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

| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| ID             |        | 0     |             |
| MEM_TYPE       | [ 0:0] | 1'b0  |             |
| MEM_SIZE       | [33:0] | 1024  |             |
| TX_OR_RXN_PATH |        | 0     |             |
| AUTO_BRINGUP   |        | 0     |             |
## Ports

| Port name           | Direction | Type   | Description                            |
| ------------------- | --------- | ------ | -------------------------------------- |
| up_clk              | input     |        |  microprocessor interface              |
| up_rstn             | input     |        |                                        |
| up_rreq             | input     |        |                                        |
| up_rack             | output    |        |                                        |
| up_raddr            | input     | [13:0] |                                        |
| up_rdata            | output    | [31:0] |                                        |
| up_wreq             | input     |        |                                        |
| up_wack             | output    |        |                                        |
| up_waddr            | input     | [13:0] |                                        |
| up_wdata            | input     | [31:0] |                                        |
| src_clk             | input     |        |  source clock domain                   |
| dst_clk             | input     |        |  destination clock domain              |
| src_sw_resetn       | output    |        |  resets for all clock domains          |
| dst_sw_resetn       | output    |        |                                        |
| ddr_calib_done      | input     |        |  status bit from the memory controller |
| src_bypass          | output    |        |  bypass control                        |
| dst_bypass          | output    |        |                                        |
| oneshot             | output    |        |                                        |
| sync                | output    |        |  synchronization                       |
| sync_config         | output    | [ 1:0] |                                        |
| src_transfer_length | output    | [33:0] |                                        |
| src_fsm_status      | input     | [ 1:0] |  FSM control and status                |
| dst_fsm_status      | input     | [ 1:0] |                                        |
| sample_count_msb    | input     | [31:0] |                                        |
| sample_count_lsb    | input     | [31:0] |                                        |
## Signals

| Name                  | Type         | Description          |
| --------------------- | ------------ | -------------------- |
| up_scratch            | reg   [31:0] |  internal registers  |
| up_sw_resetn          | reg          |                      |
| up_bypass             | reg          |                      |
| up_sync               | reg          |                      |
| up_sync_config        | reg   [ 1:0] |                      |
| up_oneshot            | reg          |                      |
| up_transfer_length    | reg   [33:0] |                      |
| up_ddr_calib_done_s   | wire         | internal signals     |
| up_wr_fsm_status_s    | wire [ 1:0]  |                      |
| up_rd_fsm_status_s    | wire [ 1:0]  |                      |
| up_sample_count_msb_s | wire [31:0]  |                      |
| up_sample_count_lsb_s | wire [31:0]  |                      |
| src_sw_resetn_s       | wire         |                      |
| dst_sw_resetn_s       | wire         |                      |
| src_transfer_length_s | wire [33:0]  |                      |
## Constants

| Name         | Type   | Value        | Description |
| ------------ | ------ | ------------ | ----------- |
| CORE_VERSION | [31:0] | 32'h00010061 | 1.00.a      |
| CORE_MAGIC   | [31:0] | 32'h44414F46 | DAOF        |
## Processes
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
</br>**Description**
 write interface 
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
</br>**Description**
read interface for common registers 
- unnamed: ( @(posedge src_clk) )
  - **Type:** always
- unnamed: ( @(posedge dst_clk) )
  - **Type:** always
## Instantiations

- i_dst_fsm_status: sync_data
</br>**Description**
 read interface */
 Clock Domain Crossing Logic for reset, control and status signals

- i_src_fsm_status: sync_data
- i_xfer_status: sync_data
- i_src_xfer_control: sync_bits
- i_dst_xfer_control: sync_bits
- i_ddr_calib_done_sync: sync_bits
- i_dst_oneshot_sync: sync_bits
- i_sync_src_transfer_length: sync_data
