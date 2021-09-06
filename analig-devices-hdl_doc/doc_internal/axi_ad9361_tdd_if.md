# Entity: axi_ad9361_tdd_if

- **File**: axi_ad9361_tdd_if.v
## Diagram

![Diagram](axi_ad9361_tdd_if.svg "Diagram")
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
| LEVEL_OR_PULSE_N |      | 0     |             |
## Ports

| Port name         | Direction | Type   | Description                           |
| ----------------- | --------- | ------ | ------------------------------------- |
| clk               | input     |        |  clock                                |
| rst               | input     |        |                                       |
| tdd_rx_vco_en     | input     |        |  control signals from the tdd control |
| tdd_tx_vco_en     | input     |        |                                       |
| tdd_rx_rf_en      | input     |        |                                       |
| tdd_tx_rf_en      | input     |        |                                       |
| ad9361_txnrx      | output    |        |  device interface                     |
| ad9361_enable     | output    |        |                                       |
| ad9361_tdd_status | output    | [ 7:0] |  interface status                     |
## Signals

| Name            | Type | Description          |
| --------------- | ---- | -------------------- |
| tdd_vco_overlap | reg  |  internal registers  |
| tdd_rf_overlap  | reg  |                      |
| ad9361_txnrx_s  | wire |                      |
| ad9361_enable_s | wire |                      |
## Constants

| Name       | Type | Value | Description |
| ---------- | ---- | ----- | ----------- |
| PULSE_MODE |      | 0     |             |
| LEVEL_MODE |      | 1     |             |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
