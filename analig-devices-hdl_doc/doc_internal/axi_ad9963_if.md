# Entity: axi_ad9963_if

- **File**: axi_ad9963_if.v
## Diagram

![Diagram](axi_ad9963_if.svg "Diagram")
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

| Generic name           | Type | Value                | Description                                                           |
| ---------------------- | ---- | -------------------- | --------------------------------------------------------------------- |
| FPGA_TECHNOLOGY        |      | 0                    |  this parameter controls the buffer type based on the target device.  |
| ADC_IODELAY_ENABLE     |      | 0                    |                                                                       |
| IO_DELAY_GROUP         |      | "dev_if_delay_group" |                                                                       |
| DELAY_REFCLK_FREQUENCY |      | 200                  |                                                                       |
## Ports

| Port name      | Direction | Type   | Description                                  |
| -------------- | --------- | ------ | -------------------------------------------- |
| trx_clk        | input     |        |  physical interface (receive)                |
| trx_iq         | input     |        |                                              |
| trx_data       | input     | [11:0] |                                              |
| tx_clk         | input     |        |  physical interface (transmit)               |
| tx_iq          | output    |        |                                              |
| tx_data        | output    | [11:0] |                                              |
| adc_rst        | input     |        |  clock (common to both receive and transmit) |
| dac_rst        | input     |        |                                              |
| adc_clk        | output    |        |                                              |
| dac_clk        | output    |        |                                              |
| adc_valid      | output    |        |  receive data path interface                 |
| adc_data       | output    | [23:0] |                                              |
| adc_status     | output    |        |                                              |
| up_adc_ce      | input     |        |                                              |
| out_valid_q    | input     |        |  transmit data path interface                |
| out_valid_i    | input     |        |                                              |
| dac_data       | input     | [23:0] |                                              |
| up_dac_ce      | input     |        |                                              |
| tx_sample_hold | input     |        |                                              |
| up_clk         | input     |        |  delay interface                             |
| up_adc_dld     | input     | [12:0] |                                              |
| up_adc_dwdata  | input     | [64:0] |                                              |
| up_adc_drdata  | output    | [64:0] |                                              |
| delay_clk      | input     |        |                                              |
| delay_rst      | input     |        |                                              |
| delay_locked   | output    |        |                                              |
## Signals

| Name            | Type           | Description          |
| --------------- | -------------- | -------------------- |
| rx_data_p       | reg     [11:0] |  internal registers  |
| tx_data_p       | reg     [11:0] |                      |
| tx_data_n       | reg     [11:0] |                      |
| constant_sample | reg     [23:0] |                      |
| rx_data_p_s     | wire [11:0]    |  internal signals    |
| rx_data_n_s     | wire [11:0]    |                      |
| rx_iq_p_s       | wire           |                      |
| rx_iq_n_s       | wire           |                      |
| div_clk         | wire           |                      |
## Processes
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
- unnamed: ( @(posedge dac_clk) )
  - **Type:** always
- unnamed: ( @(posedge adc_clk) )
  - **Type:** always
## Instantiations

- bufgctrl_adc: BUFGCTRL
**Description**
 device clock interface (receive clock)

- i_rx_iq: ad_data_in
**Description**
 receive iq interface, ibuf -> idelay -> iddr

- i_div_clk_buf: BUFR
**Description**
 transmit data interface

- bufgctrl_dac: BUFGCTRL
- i_tx_data_oddr: ODDR
