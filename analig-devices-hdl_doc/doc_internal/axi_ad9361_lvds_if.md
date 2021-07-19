# Entity: axi_ad9361_lvds_if

- **File**: axi_ad9361_lvds_if.v
## Diagram

![Diagram](axi_ad9361_lvds_if.svg "Diagram")
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

| Generic name           | Type | Value                | Description |
| ---------------------- | ---- | -------------------- | ----------- |
| FPGA_TECHNOLOGY        |      | 0                    |             |
| DAC_IODELAY_ENABLE     |      | 0                    |             |
| IO_DELAY_GROUP         |      | "dev_if_delay_group" |             |
| CLK_DESKEW             |      | 0                    |             |
| USE_SSI_CLK            |      | 1                    |             |
| DELAY_REFCLK_FREQUENCY |      | 200                  |             |
| RX_NODPA               |      | 0                    |             |
## Ports

| Port name       | Direction | Type   | Description                                 |
| --------------- | --------- | ------ | ------------------------------------------- |
| rx_clk_in_p     | input     |        | physical interface (receive)                |
| rx_clk_in_n     | input     |        |                                             |
| rx_frame_in_p   | input     |        |                                             |
| rx_frame_in_n   | input     |        |                                             |
| rx_data_in_p    | input     | [ 5:0] |                                             |
| rx_data_in_n    | input     | [ 5:0] |                                             |
| tx_clk_out_p    | output    |        | physical interface (transmit)               |
| tx_clk_out_n    | output    |        |                                             |
| tx_frame_out_p  | output    |        |                                             |
| tx_frame_out_n  | output    |        |                                             |
| tx_data_out_p   | output    | [ 5:0] |                                             |
| tx_data_out_n   | output    | [ 5:0] |                                             |
| enable          | output    |        | ensm control                                |
| txnrx           | output    |        |                                             |
| rst             | input     |        | clock (common to both receive and transmit) |
| clk             | input     |        |                                             |
| l_clk           | output    |        |                                             |
| adc_valid       | output    |        | receive data path interface                 |
| adc_data        | output    | [47:0] |                                             |
| adc_status      | output    |        |                                             |
| adc_r1_mode     | input     |        |                                             |
| adc_ddr_edgesel | input     |        |                                             |
| dac_valid       | input     |        | transmit data path interface                |
| dac_data        | input     | [47:0] |                                             |
| dac_clksel      | input     |        |                                             |
| dac_r1_mode     | input     |        |                                             |
| tdd_enable      | input     |        | tdd interface                               |
| tdd_txnrx       | input     |        |                                             |
| tdd_mode        | input     |        |                                             |
| mmcm_rst        | input     |        | delay interface                             |
| up_clk          | input     |        |                                             |
| up_rstn         | input     |        |                                             |
| up_enable       | input     |        |                                             |
| up_txnrx        | input     |        |                                             |
| up_adc_dld      | input     | [ 6:0] |                                             |
| up_adc_dwdata   | input     | [34:0] |                                             |
| up_adc_drdata   | output    | [34:0] |                                             |
| up_dac_dld      | input     | [ 9:0] |                                             |
| up_dac_dwdata   | input     | [49:0] |                                             |
| up_dac_drdata   | output    | [49:0] |                                             |
| delay_clk       | input     |        |                                             |
| delay_rst       | input     |        |                                             |
| delay_locked    | output    |        |                                             |
| up_drp_sel      | input     |        | drp interface                               |
| up_drp_wr       | input     |        |                                             |
| up_drp_addr     | input     | [11:0] |                                             |
| up_drp_wdata    | input     | [31:0] |                                             |
| up_drp_rdata    | output    | [31:0] |                                             |
| up_drp_ready    | output    |        |                                             |
| up_drp_locked   | output    |        |                                             |
## Signals

| Name           | Type           | Description              |
| -------------- | -------------- | ------------------------ |
| rx_r1_mode     | reg            | internal registers       |
| rx_locked_m1   | reg            |                          |
| rx_locked      | reg            |                          |
| rx_frame       | reg     [ 1:0] |                          |
| rx_data_1      | reg     [ 5:0] |                          |
| rx_data_0      | reg     [ 5:0] |                          |
| adc_valid_p    | reg            |                          |
| adc_data_p     | reg     [47:0] |                          |
| adc_status_p   | reg            |                          |
| adc_valid_int  | reg            |                          |
| adc_data_int   | reg     [47:0] |                          |
| adc_status_int | reg            |                          |
| tx_data_sel    | reg     [ 1:0] |                          |
| tx_data        | reg     [47:0] |                          |
| tx_clk_p       | reg     [ 1:0] |                          |
| tx_frame_p     | reg            |                          |
| tx_data_0_p    | reg     [ 5:0] |                          |
| tx_data_1_p    | reg     [ 5:0] |                          |
| tx_clk         | reg     [ 1:0] |                          |
| tx_frame       | reg            |                          |
| tx_data_0      | reg     [ 5:0] |                          |
| tx_data_1      | reg     [ 5:0] |                          |
| up_enable_int  | reg            |                          |
| up_txnrx_int   | reg            |                          |
| enable_up_m1   | reg            |                          |
| txnrx_up_m1    | reg            |                          |
| enable_up      | reg            |                          |
| txnrx_up       | reg            |                          |
| enable_int     | reg            |                          |
| txnrx_int      | reg            |                          |
| enable_int_p   | reg            |                          |
| txnrx_int_p    | reg            |                          |
| rx_data_1_s    | wire [ 5:0]    | internal signals         |
| rx_data_0_s    | wire [ 5:0]    |                          |
| rx_frame_s     | wire [ 1:0]    |                          |
| locked_s       | wire           |                          |
| rx_error_r1    | reg            | frame check delineation  |
| rx_error_r2    | reg            |                          |
## Processes
- unnamed: ( @(posedge l_clk) )
- unnamed: ( @(posedge l_clk) )
**Description**
intel-equivalence

- unnamed: ( @(posedge l_clk) )
- unnamed: ( @(posedge l_clk) )
- unnamed: ( @(posedge l_clk) )
**Description**
adc-status

- unnamed: ( @(posedge clk) )
**Description**
dac-tx interface

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge up_clk) )
**Description**
tdd/ensm control

- unnamed: ( @(posedge clk or posedge rst) )
- unnamed: ( @(posedge clk) )
## Instantiations

- i_rx_frame: ad_data_in
**Description**
receive frame interface, ibuf -> idelay -> iddr

- i_tx_frame: ad_data_out
**Description**
transmit frame interface, oddr -> obuf

- i_tx_clk: ad_data_out
**Description**
transmit clock interface, oddr -> obuf

- i_enable: ad_data_out
**Description**
enable, oddr -> obuf

- i_txnrx: ad_data_out
**Description**
txnrx, oddr -> obuf

