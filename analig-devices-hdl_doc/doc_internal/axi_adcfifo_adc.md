# Entity: axi_adcfifo_adc

- **File**: axi_adcfifo_adc.v
## Diagram

![Diagram](axi_adcfifo_adc.svg "Diagram")
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

| Generic name   | Type | Value | Description |
| -------------- | ---- | ----- | ----------- |
| ADC_DATA_WIDTH |      | 128   |             |
| AXI_DATA_WIDTH |      | 512   |             |
## Ports

| Port name       | Direction | Type                 | Description     |
| --------------- | --------- | -------------------- | --------------- |
| adc_rst         | input     |                      |  fifo interface |
| adc_clk         | input     |                      |                 |
| adc_wr          | input     |                      |                 |
| adc_wdata       | input     | [ADC_DATA_WIDTH-1:0] |                 |
| adc_wovf        | output    |                      |                 |
| adc_dwr         | output    |                      |                 |
| adc_ddata       | output    | [AXI_DATA_WIDTH-1:0] |                 |
| axi_drst        | input     |                      |  axi interface  |
| axi_clk         | input     |                      |                 |
| axi_xfer_status | input     | [ 3:0]               |                 |
## Signals

| Name              | Type            | Description          |
| ----------------- | --------------- | -------------------- |
| adc_wcnt_int      | reg     [  2:0] |  internal registers  |
| adc_xfer_status_s | wire [  3:0]    |  internal signals    |
## Constants

| Name          | Type | Value                         | Description |
| ------------- | ---- | ----------------------------- | ----------- |
| ADC_MEM_RATIO |      | AXI_DATA_WIDTH/ADC_DATA_WIDTH |             |
## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
</br>**Description**
 write interface: supports only 64, 128, 256 and 512 against 512 
## Instantiations

- i_xfer_status: up_xfer_status
</br>**Description**
 instantiations

