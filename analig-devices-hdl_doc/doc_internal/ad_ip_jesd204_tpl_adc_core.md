# Entity: ad_ip_jesd204_tpl_adc_core

- **File**: ad_ip_jesd204_tpl_adc_core.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_adc_core.svg "Diagram")
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

| Generic name         | Type | Value                                                | Description |
| -------------------- | ---- | ---------------------------------------------------- | ----------- |
| NUM_LANES            |      | 1                                                    |             |
| NUM_CHANNELS         |      | 1                                                    |             |
| SAMPLES_PER_FRAME    |      | 1                                                    |             |
| CONVERTER_RESOLUTION |      | 14                                                   |             |
| BITS_PER_SAMPLE      |      | 16                                                   |             |
| DMA_BITS_PER_SAMPLE  |      | 16                                                   |             |
| OCTETS_PER_BEAT      |      | 4                                                    |             |
| EN_FRAME_ALIGN       |      | 0                                                    |             |
| DATA_PATH_WIDTH      |      | 1                                                    |             |
| LINK_DATA_WIDTH      |      | NUM_LANES * OCTETS_PER_BEAT * 8                      |             |
| DMA_DATA_WIDTH       |      | DATA_PATH_WIDTH * DMA_BITS_PER_SAMPLE * NUM_CHANNELS |             |
| TWOS_COMPLEMENT      |      | 1                                                    |             |
## Ports

| Port name        | Direction | Type                  | Description |
| ---------------- | --------- | --------------------- | ----------- |
| clk              | input     |                       |             |
| dfmt_enable      | input     | [NUM_CHANNELS-1:0]    |             |
| dfmt_sign_extend | input     | [NUM_CHANNELS-1:0]    |             |
| dfmt_type        | input     | [NUM_CHANNELS-1:0]    |             |
| pn_seq_sel       | input     | [NUM_CHANNELS*4-1:0]  |             |
| pn_err           | output    | [NUM_CHANNELS-1:0]    |             |
| pn_oos           | output    | [NUM_CHANNELS-1:0]    |             |
| adc_valid        | output    | [NUM_CHANNELS-1:0]    |             |
| adc_data         | output    | [DMA_DATA_WIDTH-1:0]  |             |
| adc_sync         | input     |                       |             |
| adc_sync_status  | output    |                       |             |
| adc_sync_in      | input     |                       |             |
| adc_rst_sync     | output    |                       |             |
| link_valid       | input     |                       |             |
| link_ready       | output    |                       |             |
| link_sof         | input     | [OCTETS_PER_BEAT-1:0] |             |
| link_data        | input     | [LINK_DATA_WIDTH-1:0] |             |
## Signals

| Name           | Type                      | Description |
| -------------- | ------------------------- | ----------- |
| raw_data_s     | wire [ADC_DATA_WIDTH-1:0] |             |
| adc_sync_armed | reg                       |             |
| adc_sync_in_d1 | reg                       |             |
| adc_sync_d1    | reg                       |             |
## Constants

| Name           | Type | Value                                  | Description                             |
| -------------- | ---- | -------------------------------------- | --------------------------------------- |
| CDW_RAW        |      | CONVERTER_RESOLUTION * DATA_PATH_WIDTH |  Raw and formatted channel data widths  |
| ADC_DATA_WIDTH |      | CDW_RAW * NUM_CHANNELS                 |                                         |
| CDW_FMT        |      | DMA_BITS_PER_SAMPLE * DATA_PATH_WIDTH  |                                         |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
## Instantiations

- i_deframer: ad_ip_jesd204_tpl_adc_deframer
**Description**
 synchronization logic

