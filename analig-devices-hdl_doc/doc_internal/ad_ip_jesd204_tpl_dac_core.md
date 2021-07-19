# Entity: ad_ip_jesd204_tpl_dac_core

- **File**: ad_ip_jesd204_tpl_dac_core.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_dac_core.svg "Diagram")
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

| Generic name         | Type | Value                           | Description |
| -------------------- | ---- | ------------------------------- | ----------- |
| DATAPATH_DISABLE     |      | 0                               |             |
| IQCORRECTION_DISABLE |      | 1                               |             |
| XBAR_ENABLE          |      | 1                               |             |
| NUM_LANES            |      | 1                               |             |
| NUM_CHANNELS         |      | 1                               |             |
| BITS_PER_SAMPLE      |      | 16                              |             |
| CONVERTER_RESOLUTION |      | 16                              |             |
| SAMPLES_PER_FRAME    |      | 1                               |             |
| OCTETS_PER_BEAT      |      | 4                               |             |
| DATA_PATH_WIDTH      |      | 4                               |             |
| LINK_DATA_WIDTH      |      | NUM_LANES * OCTETS_PER_BEAT * 8 |             |
| DDS_TYPE             |      | 1                               |             |
| DDS_CORDIC_DW        |      | 16                              |             |
| DDS_CORDIC_PHASE_DW  |      | 16                              |             |
| EXT_SYNC             |      | 0                               |             |
## Ports

| Port name          | Direction | Type                  | Description             |
| ------------------ | --------- | --------------------- | ----------------------- |
| clk                | input     |                       | dac interface           |
| link_valid         | output    |                       |                         |
| link_ready         | input     |                       |                         |
| link_data          | output    | [LINK_DATA_WIDTH-1:0] |                         |
| dac_valid          | output    | [NUM_CHANNELS-1:0]    | dma interface           |
| dac_ddata          | input     | [LINK_DATA_WIDTH-1:0] |                         |
| dac_sync           | input     |                       | Configuration interface |
| dac_sync_in        | input     |                       |                         |
| dac_sync_in_status | output    |                       |                         |
| dac_dds_format     | input     |                       |                         |
| dac_data_sel       | input     | [NUM_CHANNELS*4-1:0]  |                         |
| dac_mask_enable    | input     | [NUM_CHANNELS-1:0]    |                         |
| dac_dds_scale_0    | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_dds_init_0     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_dds_incr_0     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_dds_scale_1    | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_dds_init_1     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_dds_incr_1     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_pat_data_0     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_pat_data_1     | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_iqcor_enb      | input     | [NUM_CHANNELS-1:0]    |                         |
| dac_iqcor_coeff_1  | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_iqcor_coeff_2  | input     | [NUM_CHANNELS*16-1:0] |                         |
| dac_src_chan_sel   | input     | [NUM_CHANNELS*8-1:0]  |                         |
| enable             | output    | [NUM_CHANNELS-1:0]    |                         |
## Signals

| Name            | Type                      | Description |
| --------------- | ------------------------- | ----------- |
| dac_data_s      | wire [DAC_DATA_WIDTH-1:0] |             |
| dac_ddata_muxed | wire [DAC_DATA_WIDTH-1:0] |             |
| pn7_data        | wire [DAC_CDW-1:0]        |             |
| pn15_data       | wire [DAC_CDW-1:0]        |             |
| dac_sync_in_d1  | reg                       |             |
| dac_sync_in_d2  | reg                       |             |
| dac_sync_in_arm | reg                       |             |
| dac_sync_d1     | reg                       |             |
## Constants

| Name           | Type | Value                                  | Description |
| -------------- | ---- | -------------------------------------- | ----------- |
| DAC_CDW        |      | CONVERTER_RESOLUTION * DATA_PATH_WIDTH |             |
| DAC_DATA_WIDTH |      | DAC_CDW * NUM_CHANNELS                 |             |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- i_framer: ad_ip_jesd204_tpl_dac_framer
**Description**
device interface

- i_pn_gen: ad_ip_jesd204_tpl_dac_pn
**Description**
PN generator

