# Entity: axi_usb_fx3_if

- **File**: axi_usb_fx3_if.v
## Diagram

![Diagram](axi_usb_fx3_if.svg "Diagram")
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

## Ports

| Port name      | Direction | Type   | Description |
| -------------- | --------- | ------ | ----------- |
| dma_rdy        | input     |        |             |
| dma_wmk        | input     |        |             |
| fifo_rdy       | input     | [ 3:0] |             |
| pclk           | input     |        |             |
| reset_n        | input     |        |             |
| data           | inout     | [31:0] |             |
| addr           | output    | [ 1:0] |             |
| slcs_n         | output    |        |             |
| slrd_n         | output    |        |             |
| sloe_n         | output    |        |             |
| slwr_n         | output    |        |             |
| pktend_n       | output    |        |             |
| epswitch_n     | output    |        |             |
| fifo_num       | input     | [ 4:0] |             |
| fifo_direction | input     | [10:0] |             |
| trig           | input     |        |             |
| fifo_ready     | output    | [10:0] |             |
| fx32dma_valid  | output    |        |             |
| fx32dma_ready  | input     |        |             |
| fx32dma_data   | output    | [31:0] |             |
| fx32dma_sop    | output    |        |             |
| fx32dma_eop    | input     |        |             |
| eot_fx32dma    | input     |        |             |
| dma2fx3_ready  | output    |        |             |
| dma2fx3_valid  | input     |        |             |
| dma2fx3_data   | input     | [31:0] |             |
| dma2fx3_eop    | input     |        |             |
## Signals

| Name               | Type       | Description          |
| ------------------ | ---------- | -------------------- |
| state_gpif_ii      | reg [ 3:0] |  internal registers  |
| next_state_gpif_ii | reg [ 3:0] |                      |
| current_direction  | reg        |                      |
| current_fifo       | reg        |                      |
| slcs_n_d1          | reg        |                      |
| slcs_n_d2          | reg        |                      |
| slcs_n_d3          | reg        |                      |
| slcs_n_d4          | reg        |                      |
| slrd_n_d1          | reg        |                      |
| slrd_n_d2          | reg        |                      |
| slrd_n_d3          | reg        |                      |
| sloe_n_d1          | reg        |                      |
| pip                | reg        |                      |
## Constants

| Name       | Type | Value   | Description |
| ---------- | ---- | ------- | ----------- |
| IDLE       |      | 4'b0001 |             |
| READ_START |      | 4'b0010 |             |
| READ_DATA  |      | 4'b0100 |             |
| WRITE_DATA |      | 4'b1000 |             |
## Processes
- unnamed: ( @(fifo_num, fifo_rdy, fifo_direction) )
  - **Type:** always
- unnamed: ( @(posedge pclk) )
  - **Type:** always
</br>**Description**
 STATE MACHINE GPIF II 
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(posedge pclk) )
  - **Type:** always
