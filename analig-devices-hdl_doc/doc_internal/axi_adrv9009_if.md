# Entity: axi_adrv9009_if

- **File**: axi_adrv9009_if.v
## Diagram

![Diagram](axi_adrv9009_if.svg "Diagram")
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

| Port name      | Direction | Type    | Description |
| -------------- | --------- | ------- | ----------- |
| adc_clk        | input     |         |  receive    |
| adc_rx_sof     | input     | [ 3:0]  |             |
| adc_rx_data    | input     | [ 63:0] |             |
| adc_os_clk     | input     |         |             |
| adc_rx_os_sof  | input     | [ 3:0]  |             |
| adc_rx_os_data | input     | [ 63:0] |             |
| adc_r1_mode    | input     |         |             |
| adc_data       | output    | [ 63:0] |             |
| adc_os_valid   | output    |         |             |
| adc_os_data    | output    | [127:0] |             |
| dac_clk        | input     |         |  transmit   |
| dac_tx_data    | output    | [127:0] |             |
| dac_data       | input     | [127:0] |             |
## Signals

| Name             | Type         | Description        |
| ---------------- | ------------ | ------------------ |
| adc_rx_data_s    | wire [ 63:0] |  internal signals  |
| adc_rx_os_data_s | wire [ 63:0] |                    |
| rx_os_sof        | wire         |                    |
## Processes
- unnamed: ( @(posedge adc_os_clk) )
  - **Type:** always
**Description**
 instantiations 
