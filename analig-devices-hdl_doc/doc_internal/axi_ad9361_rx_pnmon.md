# Entity: axi_ad9361_rx_pnmon

- **File**: axi_ad9361_rx_pnmon.v
## Diagram

![Diagram](axi_ad9361_rx_pnmon.svg "Diagram")
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
 PN monitors

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Q_OR_I_N     |      | 0     |             |
| PRBS_SEL     |      | 0     |             |
## Ports

| Port name     | Direction | Type   | Description               |
| ------------- | --------- | ------ | ------------------------- |
| adc_clk       | input     |        |  adc interface            |
| adc_valid     | input     |        |                           |
| adc_data_i    | input     | [11:0] |                           |
| adc_data_q    | input     | [11:0] |                           |
| adc_pnseq_sel | input     | [ 3:0] |  pn out of sync and error |
| adc_pn_oos    | output    |        |                           |
| adc_pn_err    | output    |        |                           |
## Signals

| Name                 | Type           | Description          |
| -------------------- | -------------- | -------------------- |
| adc_pn0_valid        | reg            |  internal registers  |
| adc_pn0_data         | reg     [15:0] |                      |
| adc_pn0_valid_in     | reg            |                      |
| adc_pn0_data_in      | reg     [15:0] |                      |
| adc_pn0_data_pn      | reg     [15:0] |                      |
| adc_pn1_valid_t      | reg            |                      |
| adc_pn1_data_d       | reg     [11:0] |                      |
| adc_pn1_valid_in     | reg            |                      |
| adc_pn1_data_in      | reg     [23:0] |                      |
| adc_pn1_data_pn      | reg     [23:0] |                      |
| adc_pn_valid_in      | reg            |                      |
| adc_pn_data_in       | reg     [23:0] |                      |
| adc_pn_data_pn       | reg     [23:0] |                      |
| adc_pn0_data_i_s     | wire [11:0]    |  internal signals    |
| adc_pn0_data_q_s     | wire [11:0]    |                      |
| adc_pn0_data_q_rev_s | wire [11:0]    |                      |
| adc_pn0_data_s       | wire [15:0]    |                      |
| adc_pn0_iq_match_s   | wire           |                      |
| adc_pn0_data_pn_s    | wire [15:0]    |                      |
| adc_pn1_valid_s      | wire           |                      |
| adc_pn1_data_pn_s    | wire [23:0]    |                      |
## Constants

| Name     | Type | Value | Description |
| -------- | ---- | ----- | ----------- |
| PRBS_P09 |      | 0     |             |
| PRBS_P11 |      | 1     |             |
| PRBS_P15 |      | 2     |             |
| PRBS_P20 |      | 3     |             |
## Functions
- brfn <font id="function_arguments">()</font> <font id="function_return">return ([11:0])</font>
</br>**Description**
 bit reversal function

- pn0fn <font id="function_arguments">()</font> <font id="function_return">return ([15:0])</font>
</br>**Description**
 device-specific prbs function

- pn1fn <font id="function_arguments">()</font> <font id="function_return">return ([23:0])</font>
</br>**Description**
 standard prbs functions

## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
</br>**Description**
 pn mux 
## Instantiations

- i_pnmon: ad_pnmon
</br>**Description**
 pn oos & pn err

