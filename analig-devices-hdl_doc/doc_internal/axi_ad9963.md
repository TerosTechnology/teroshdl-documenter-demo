# Entity: axi_ad9963

## Diagram

![Diagram](axi_ad9963.svg "Diagram")
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

| Generic name             | Type | Value                | Description |
| ------------------------ | ---- | -------------------- | ----------- |
| ID                       |      | 0                    | parameters  |
| FPGA_TECHNOLOGY          |      | 0                    |             |
| FPGA_FAMILY              |      | 0                    |             |
| SPEED_GRADE              |      | 0                    |             |
| DEV_PACKAGE              |      | 0                    |             |
| ADC_IODELAY_ENABLE       |      | 0                    |             |
| IO_DELAY_GROUP           |      | "dev_if_delay_group" |             |
| IODELAY_ENABLE           |      | 0                    |             |
| DAC_DDS_TYPE             |      | 1                    |             |
| DAC_DDS_CORDIC_DW        |      | 14                   |             |
| DAC_DDS_CORDIC_PHASE_DW  |      | 13                   |             |
| DAC_DATAPATH_DISABLE     |      | 0                    |             |
| ADC_USERPORTS_DISABLE    |      | 0                    |             |
| ADC_DATAFORMAT_DISABLE   |      | 0                    |             |
| ADC_DCFILTER_DISABLE     |      | 0                    |             |
| ADC_IQCORRECTION_DISABLE |      | 0                    |             |
| ADC_SCALECORRECTION_ONLY |      | 1                    |             |
| DELAY_REFCLK_FREQUENCY   |      | 200                  |             |
## Ports

| Port name        | Direction | Type   | Description                   |
| ---------------- | --------- | ------ | ----------------------------- |
| trx_clk          | input     |        | physical interface (receive)  |
| trx_iq           | input     |        |                               |
| trx_data         | input     | [11:0] |                               |
| tx_clk           | input     |        | physical interface (transmit) |
| tx_iq            | output    |        |                               |
| tx_data          | output    | [11:0] |                               |
| dac_sync_in      | input     |        | transmit master/slave         |
| dac_sync_out     | output    |        |                               |
| delay_clk        | input     |        | delay clock                   |
| adc_clk          | output    |        | master interface              |
| dac_clk          | output    |        |                               |
| adc_rst          | output    |        |                               |
| dac_rst          | output    |        |                               |
| adc_enable_i     | output    |        | dma interface                 |
| adc_valid_i      | output    |        |                               |
| adc_data_i       | output    | [15:0] |                               |
| adc_enable_q     | output    |        |                               |
| adc_valid_q      | output    |        |                               |
| adc_data_q       | output    | [15:0] |                               |
| adc_dovf         | input     |        |                               |
| dac_enable_i     | output    |        |                               |
| dac_valid_i      | output    |        |                               |
| dac_data_i       | input     | [15:0] |                               |
| dma_valid_i      | input     |        |                               |
| dac_enable_q     | output    |        |                               |
| dac_valid_q      | output    |        |                               |
| dac_data_q       | input     | [15:0] |                               |
| dma_valid_q      | input     |        |                               |
| dac_dunf         | input     |        |                               |
| hold_last_sample | input     |        |                               |
| s_axi_aclk       | input     |        | axi interface                 |
| s_axi_aresetn    | input     |        |                               |
| s_axi_awvalid    | input     |        |                               |
| s_axi_awaddr     | input     | [15:0] |                               |
| s_axi_awprot     | input     | [ 2:0] |                               |
| s_axi_awready    | output    |        |                               |
| s_axi_wvalid     | input     |        |                               |
| s_axi_wdata      | input     | [31:0] |                               |
| s_axi_wstrb      | input     | [ 3:0] |                               |
| s_axi_wready     | output    |        |                               |
| s_axi_bvalid     | output    |        |                               |
| s_axi_bresp      | output    | [ 1:0] |                               |
| s_axi_bready     | input     |        |                               |
| s_axi_arvalid    | input     |        |                               |
| s_axi_araddr     | input     | [15:0] |                               |
| s_axi_arprot     | input     | [ 2:0] |                               |
| s_axi_arready    | output    |        |                               |
| s_axi_rvalid     | output    |        |                               |
| s_axi_rdata      | output    | [31:0] |                               |
| s_axi_rresp      | output    | [ 1:0] |                               |
| s_axi_rready     | input     |        |                               |
## Signals

| Name            | Type           | Description                 |
| --------------- | -------------- | --------------------------- |
| up_wack         | reg            | internal registers          |
| up_rack         | reg            |                             |
| up_rdata        | reg     [31:0] |                             |
| up_clk          | wire           | internal clocks and resets  |
| up_rstn         | wire           |                             |
| delay_rst       | wire           |                             |
| adc_valid_s     | wire           | internal signals            |
| adc_data_s      | wire [23:0]    |                             |
| adc_status_s    | wire           |                             |
| dac_data_s      | wire [23:0]    |                             |
| up_adc_dld_s    | wire [12:0]    |                             |
| up_adc_dwdata_s | wire [64:0]    |                             |
| up_adc_drdata_s | wire [64:0]    |                             |
| delay_locked_s  | wire           |                             |
| up_wreq_s       | wire           |                             |
| up_waddr_s      | wire [13:0]    |                             |
| up_wdata_s      | wire [31:0]    |                             |
| up_wack_rx_s    | wire           |                             |
| up_wack_tx_s    | wire           |                             |
| up_rreq_s       | wire           |                             |
| up_raddr_s      | wire [13:0]    |                             |
| up_rdata_rx_s   | wire [31:0]    |                             |
| up_rack_rx_s    | wire           |                             |
| up_rdata_tx_s   | wire [31:0]    |                             |
| up_rack_tx_s    | wire           |                             |
| up_adc_ce       | wire           |                             |
| up_dac_ce       | wire           |                             |
| valid_out_q_s   | wire           |                             |
| valid_out_i_s   | wire           |                             |
## Processes
- unnamed: ( @(*) )
**Description**
processor read interface

## Instantiations

- i_dev_if: axi_ad9963_if
**Description**
device interface

- i_rx: axi_ad9963_rx
**Description**
receive

- i_tx: axi_ad9963_tx
**Description**
transmit

- i_up_axi: up_axi
**Description**
axi interface

