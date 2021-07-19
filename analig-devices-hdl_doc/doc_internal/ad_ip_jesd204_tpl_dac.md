# Entity: ad_ip_jesd204_tpl_dac

- **File**: ad_ip_jesd204_tpl_dac.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_dac.svg "Diagram")
## Description

***************************************************************************
 ***************************************************************************
 Copyright 2018 (c) Analog Devices, Inc. All rights reserved.
 Each core or library found in this collection may have its own licensing terms.
 The user should keep this in in mind while exploring these cores.
 Redistribution and use in source and binary forms,
 with or without modification of this file, are permitted under the terms of either
  (at the option of the user):
   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory, or at:
 https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
 OR
   2.  An ADI specific BSD license as noted in the top level directory, or on-line at:
 https://github.com/analogdevicesinc/hdl/blob/dev/LICENSE
 ***************************************************************************
 ***************************************************************************
 
## Generics

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| ID                   |      | 0     |             |
| FPGA_TECHNOLOGY      |      | 0     |             |
| FPGA_FAMILY          |      | 0     |             |
| SPEED_GRADE          |      | 0     |             |
| DEV_PACKAGE          |      | 0     |             |
| NUM_LANES            |      | 4     |             |
| NUM_CHANNELS         |      | 2     |             |
| SAMPLES_PER_FRAME    |      | 1     |             |
| CONVERTER_RESOLUTION |      | 16    | JESD_N      |
| BITS_PER_SAMPLE      |      | 16    | JESD_NP     |
| DMA_BITS_PER_SAMPLE  |      | 16    |             |
| PADDING_TO_MSB_LSB_N |      | 0     |             |
| OCTETS_PER_BEAT      |      | 4     |             |
| DDS_TYPE             |      | 1     |             |
| DDS_CORDIC_DW        |      | 16    |             |
| DDS_CORDIC_PHASE_DW  |      | 16    |             |
| DATAPATH_DISABLE     |      | 0     |             |
| IQCORRECTION_DISABLE |      | 1     |             |
| EXT_SYNC             |      | 0     |             |
| XBAR_ENABLE          |      | 0     |             |
## Ports

| Port name     | Direction | Type                                                                          | Description                                           |
| ------------- | --------- | ----------------------------------------------------------------------------- | ----------------------------------------------------- |
| link_clk      | input     |                                                                               | jesd interfacelink_clk is (line-rate/40)              |
| link_valid    | output    |                                                                               |                                                       |
| link_ready    | input     |                                                                               |                                                       |
| link_data     | output    | [NUM_LANES*8*OCTETS_PER_BEAT-1:0]                                             |                                                       |
| enable        | output    | [NUM_CHANNELS-1:0]                                                            | dma interface                                         |
| dac_valid     | output    | [NUM_CHANNELS-1:0]                                                            |                                                       |
| dac_ddata     | input     | [DMA_BITS_PER_SAMPLE * OCTETS_PER_BEAT * 8 * NUM_LANES / BITS_PER_SAMPLE-1:0] |                                                       |
| dac_dunf      | input     |                                                                               |                                                       |
| dac_sync_in   | input     |                                                                               | external sync, should be on the link_clk clock domain |
| s_axi_aclk    | input     |                                                                               | axi interface                                         |
| s_axi_aresetn | input     |                                                                               |                                                       |
| s_axi_awvalid | input     |                                                                               |                                                       |
| s_axi_awready | output    |                                                                               |                                                       |
| s_axi_awaddr  | input     | [12:0]                                                                        |                                                       |
| s_axi_awprot  | input     | [2:0]                                                                         |                                                       |
| s_axi_wvalid  | input     |                                                                               |                                                       |
| s_axi_wready  | output    |                                                                               |                                                       |
| s_axi_wdata   | input     | [31:0]                                                                        |                                                       |
| s_axi_wstrb   | input     | [3:0]                                                                         |                                                       |
| s_axi_bvalid  | output    |                                                                               |                                                       |
| s_axi_bready  | input     |                                                                               |                                                       |
| s_axi_bresp   | output    | [1:0]                                                                         |                                                       |
| s_axi_arvalid | input     |                                                                               |                                                       |
| s_axi_arready | output    |                                                                               |                                                       |
| s_axi_araddr  | input     | [12:0]                                                                        |                                                       |
| s_axi_arprot  | input     | [2:0]                                                                         |                                                       |
| s_axi_rvalid  | output    |                                                                               |                                                       |
| s_axi_rready  | input     |                                                                               |                                                       |
| s_axi_rdata   | output    | [31:0]                                                                        |                                                       |
| s_axi_rresp   | output    | [1:0]                                                                         |                                                       |
## Signals

| Name               | Type                       | Description                                                       |
| ------------------ | -------------------------- | ----------------------------------------------------------------- |
| dac_sync           | wire                       | internal signals                                                  |
| dac_sync_in_status | wire                       |                                                                   |
| dac_dds_format     | wire                       |                                                                   |
| dac_dds_scale_0_s  | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_dds_init_0_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_dds_incr_0_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_dds_scale_1_s  | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_dds_init_1_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_dds_incr_1_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_pat_data_0_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_pat_data_1_s   | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_data_sel_s     | wire [NUM_CHANNELS*4-1:0]  |                                                                   |
| dac_mask_enable_s  | wire [NUM_CHANNELS-1:0]    |                                                                   |
| dac_iqcor_enb      | wire [NUM_CHANNELS-1:0]    |                                                                   |
| dac_iqcor_coeff_1  | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_iqcor_coeff_2  | wire [NUM_CHANNELS*16-1:0] |                                                                   |
| dac_src_chan_sel   | wire [NUM_CHANNELS*8-1:0]  |                                                                   |
| dac_ddata_cr       | reg [LINK_DATA_WIDTH-1:0]  |                                                                   |
| i                  | integer                    | Drop DMA padding bits from the LSB or MSB based on configuration  |
## Constants

| Name            | Type | Value                                                            | Description |
| --------------- | ---- | ---------------------------------------------------------------- | ----------- |
| DATA_PATH_WIDTH |      | OCTETS_PER_BEAT * 8 * NUM_LANES / NUM_CHANNELS / BITS_PER_SAMPLE |             |
| LINK_DATA_WIDTH |      | NUM_LANES * OCTETS_PER_BEAT * 8                                  |             |
| DMA_DATA_WIDTH  |      | DMA_BITS_PER_SAMPLE * DATA_PATH_WIDTH * NUM_CHANNELS             |             |
| BYTES_PER_FRAME |      | ( 8 * NUM_LANES)                                                 |             |
## Processes
- unnamed: ( @(*) )
## Instantiations

- i_regmap: ad_ip_jesd204_tpl_dac_regmap
**Description**
regmap

- i_core: ad_ip_jesd204_tpl_dac_core
**Description**
core

