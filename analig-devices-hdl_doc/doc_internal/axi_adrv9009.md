# Entity: axi_adrv9009

- **File**: axi_adrv9009.v
## Diagram

![Diagram](axi_adrv9009.svg "Diagram")
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

| Generic name                | Type | Value | Description |
| --------------------------- | ---- | ----- | ----------- |
| ID                          |      | 0     |             |
| FPGA_TECHNOLOGY             |      | 0     |             |
| FPGA_FAMILY                 |      | 0     |             |
| SPEED_GRADE                 |      | 0     |             |
| DEV_PACKAGE                 |      | 0     |             |
| ADC_DATAPATH_DISABLE        |      | 0     |             |
| ADC_DATAFORMAT_DISABLE      |      | 0     |             |
| ADC_DCFILTER_DISABLE        |      | 0     |             |
| ADC_IQCORRECTION_DISABLE    |      | 0     |             |
| ADC_OS_DATAPATH_DISABLE     |      | 0     |             |
| ADC_OS_DATAFORMAT_DISABLE   |      | 0     |             |
| ADC_OS_DCFILTER_DISABLE     |      | 0     |             |
| ADC_OS_IQCORRECTION_DISABLE |      | 0     |             |
| DAC_DATAPATH_DISABLE        |      | 0     |             |
| DAC_DDS_DISABLE             |      | 0     |             |
| DAC_IQCORRECTION_DISABLE    |      | 0     |             |
| DAC_DDS_TYPE                |      | 1     |             |
| DAC_DDS_CORDIC_DW           |      | 20    |             |
| DAC_DDS_CORDIC_PHASE_DW     |      | 18    |             |
## Ports

| Port name        | Direction | Type    | Description   |
| ---------------- | --------- | ------- | ------------- |
| adc_clk          | input     |         | receive       |
| adc_rx_valid     | input     |         |               |
| adc_rx_sof       | input     | [ 3:0]  |               |
| adc_rx_data      | input     | [ 63:0] |               |
| adc_rx_ready     | output    |         |               |
| adc_os_clk       | input     |         |               |
| adc_rx_os_valid  | input     |         |               |
| adc_rx_os_sof    | input     | [ 3:0]  |               |
| adc_rx_os_data   | input     | [ 63:0] |               |
| adc_rx_os_ready  | output    |         |               |
| dac_clk          | input     |         | transmit      |
| dac_tx_valid     | output    |         |               |
| dac_tx_data      | output    | [127:0] |               |
| dac_tx_ready     | input     |         |               |
| dac_sync_in      | input     |         | master/slave  |
| dac_sync_out     | output    |         |               |
| adc_enable_i0    | output    |         | dma interface |
| adc_valid_i0     | output    |         |               |
| adc_data_i0      | output    | [ 15:0] |               |
| adc_enable_q0    | output    |         |               |
| adc_valid_q0     | output    |         |               |
| adc_data_q0      | output    | [ 15:0] |               |
| adc_enable_i1    | output    |         |               |
| adc_valid_i1     | output    |         |               |
| adc_data_i1      | output    | [ 15:0] |               |
| adc_enable_q1    | output    |         |               |
| adc_valid_q1     | output    |         |               |
| adc_data_q1      | output    | [ 15:0] |               |
| adc_dovf         | input     |         |               |
| adc_os_enable_i0 | output    |         |               |
| adc_os_valid_i0  | output    |         |               |
| adc_os_data_i0   | output    | [ 31:0] |               |
| adc_os_enable_q0 | output    |         |               |
| adc_os_valid_q0  | output    |         |               |
| adc_os_data_q0   | output    | [ 31:0] |               |
| adc_os_enable_i1 | output    |         |               |
| adc_os_valid_i1  | output    |         |               |
| adc_os_data_i1   | output    | [ 31:0] |               |
| adc_os_enable_q1 | output    |         |               |
| adc_os_valid_q1  | output    |         |               |
| adc_os_data_q1   | output    | [ 31:0] |               |
| adc_os_dovf      | input     |         |               |
| dac_enable_i0    | output    |         |               |
| dac_valid_i0     | output    |         |               |
| dac_data_i0      | input     | [ 31:0] |               |
| dac_enable_q0    | output    |         |               |
| dac_valid_q0     | output    |         |               |
| dac_data_q0      | input     | [ 31:0] |               |
| dac_enable_i1    | output    |         |               |
| dac_valid_i1     | output    |         |               |
| dac_data_i1      | input     | [ 31:0] |               |
| dac_enable_q1    | output    |         |               |
| dac_valid_q1     | output    |         |               |
| dac_data_q1      | input     | [ 31:0] |               |
| dac_dunf         | input     |         |               |
| s_axi_aclk       | input     |         | axi interface |
| s_axi_aresetn    | input     |         |               |
| s_axi_awvalid    | input     |         |               |
| s_axi_awaddr     | input     | [ 15:0] |               |
| s_axi_awprot     | input     | [ 2:0]  |               |
| s_axi_awready    | output    |         |               |
| s_axi_wvalid     | input     |         |               |
| s_axi_wdata      | input     | [ 31:0] |               |
| s_axi_wstrb      | input     | [ 3:0]  |               |
| s_axi_wready     | output    |         |               |
| s_axi_bvalid     | output    |         |               |
| s_axi_bresp      | output    | [ 1:0]  |               |
| s_axi_bready     | input     |         |               |
| s_axi_arvalid    | input     |         |               |
| s_axi_araddr     | input     | [ 15:0] |               |
| s_axi_arprot     | input     | [ 2:0]  |               |
| s_axi_arready    | output    |         |               |
| s_axi_rvalid     | output    |         |               |
| s_axi_rdata      | output    | [ 31:0] |               |
| s_axi_rresp      | output    | [ 1:0]  |               |
| s_axi_rready     | input     |         |               |
## Signals

| Name           | Type            | Description         |
| -------------- | --------------- | ------------------- |
| up_wack        | reg             | internal registers  |
| up_rack        | reg             |                     |
| up_rdata       | reg     [ 31:0] |                     |
| up_clk         | wire            | internal signals    |
| up_rstn        | wire            |                     |
| adc_rst        | wire            |                     |
| adc_os_rst     | wire            |                     |
| adc_data_s     | wire [ 63:0]    |                     |
| adc_os_valid_s | wire            |                     |
| adc_os_data_s  | wire [127:0]    |                     |
| dac_rst        | wire            |                     |
| dac_data_s     | wire [127:0]    |                     |
| up_wreq_s      | wire            |                     |
| up_waddr_s     | wire [ 13:0]    |                     |
| up_wdata_s     | wire [ 31:0]    |                     |
| up_wack_s      | wire [  2:0]    |                     |
| up_rreq_s      | wire            |                     |
| up_raddr_s     | wire [ 13:0]    |                     |
| up_rdata_s     | wire [ 31:0]    |                     |
| up_rack_s      | wire [  2:0]    |                     |
## Constants

| Name                            | Type | Value                       | Description         |
| ------------------------------- | ---- | --------------------------- | ------------------- |
| ADC_DATAFORMAT_DISABLE_INT      |      | ADC_DATAFORMAT_DISABLE      | derived parameters  |
| ADC_DCFILTER_DISABLE_INT        |      | ADC_DCFILTER_DISABLE        |                     |
| ADC_IQCORRECTION_DISABLE_INT    |      | ADC_IQCORRECTION_DISABLE    |                     |
| ADC_OS_DATAFORMAT_DISABLE_INT   |      | ADC_OS_DATAFORMAT_DISABLE   |                     |
| ADC_OS_DCFILTER_DISABLE_INT     |      | ADC_OS_DCFILTER_DISABLE     |                     |
| ADC_OS_IQCORRECTION_DISABLE_INT |      | ADC_OS_IQCORRECTION_DISABLE |                     |
| DAC_DDS_DISABLE_INT             |      | DAC_DDS_DISABLE             |                     |
| DAC_IQCORRECTION_DISABLE_INT    |      | DAC_IQCORRECTION_DISABLE    |                     |
## Processes
- unnamed: ( @(negedge up_rstn or posedge up_clk) )
**Description**
processor read interface

## Instantiations

- i_if: axi_adrv9009_if
**Description**
device interface

- i_rx: axi_adrv9009_rx
**Description**
receive

- i_rx_os: axi_adrv9009_rx_os
**Description**
receive (o/s)

- i_tx: axi_adrv9009_tx
**Description**
transmit

- i_up_axi: up_axi
**Description**
axi interface

