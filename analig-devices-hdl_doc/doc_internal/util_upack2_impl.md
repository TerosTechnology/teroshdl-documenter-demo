# Entity: util_upack2_impl

- **File**: util_upack2_impl.v
## Diagram

![Diagram](util_upack2_impl.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2017 (c) Analog Devices, Inc. All rights reserved.

 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.

 The user should read each of these license terms, and understand the
 freedoms and responsabilities that he or she has by using this source/core.

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

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| NUM_OF_CHANNELS     |      | 4     |             |
| SAMPLES_PER_CHANNEL |      | 1     |             |
| SAMPLE_DATA_WIDTH   |      | 16    |             |
## Ports

| Port name         | Direction | Type                                                        | Description |
| ----------------- | --------- | ----------------------------------------------------------- | ----------- |
| clk               | input     |                                                             |             |
| reset             | input     |                                                             |             |
| enable            | input     | [NUM_OF_CHANNELS-1:0]                                       |             |
| fifo_rd_en        | input     | [NUM_OF_CHANNELS-1:0]                                       |             |
| fifo_rd_valid     | output    |                                                             |             |
| fifo_rd_underflow | output    |                                                             |             |
| fifo_rd_data      | output    | [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |             |
| s_axis_valid      | input     |                                                             |             |
| s_axis_ready      | output    |                                                             |             |
| s_axis_data       | input     | [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |             |
## Signals

| Name               | Type                                                             | Description                                                                                                                  |
| ------------------ | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| out_data           | wire [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |     * Final output data of the routing network that will be written to    * `fifo_rd_data` after being deinterleaved.    */  |
| deinterleaved_data | wire [NUM_OF_CHANNELS*SAMPLE_DATA_WIDTH*SAMPLES_PER_CHANNEL-1:0] |     * Deinterleaved version of `out_data`    */                                                                              |
| data_rd_en         | wire                                                             |     * Internal read signal.    */                                                                                            |
| ce                 | wire                                                             |     * Control signals from/to the pack shell.    */                                                                          |
| ready              | wire                                                             |                                                                                                                              |
| reset_data         | wire                                                             |                                                                                                                              |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_pack_shell: pack_shell
- i_deinterleave: ad_perfect_shuffle
**Description**

   * Data at the output of the routing network is interleaved. The upack
   * core is supposed to produce deinterleaved data. This just rearrange the
   * bits in the data vector and does not consume any FPGA resources.
   */

