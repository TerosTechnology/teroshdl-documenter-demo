# Entity: ad_ip_jesd204_tpl_adc_channel

- **File**: ad_ip_jesd204_tpl_adc_channel.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_adc_channel.svg "Diagram")
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
| CONVERTER_RESOLUTION |      | 14    |             |
| DATA_PATH_WIDTH      |      | 2     |             |
| TWOS_COMPLEMENT      |      | 1     |             |
| BITS_PER_SAMPLE      |      | 16    |             |
## Ports

| Port name        | Direction | Type                                       | Description              |
| ---------------- | --------- | ------------------------------------------ | ------------------------ |
| clk              | input     |                                            |                          |
| raw_data         | input     | [CONVERTER_RESOLUTION*DATA_PATH_WIDTH-1:0] |                          |
| fmt_data         | output    | [BITS_PER_SAMPLE*DATA_PATH_WIDTH-1:0]      |                          |
| dfmt_enable      | input     |                                            | Configuration and status |
| dfmt_type        | input     |                                            |                          |
| dfmt_sign_extend | input     |                                            |                          |
| pn_seq_sel       | input     | [3:0]                                      |                          |
| pn_oos           | output    |                                            |                          |
| pn_err           | output    |                                            |                          |
## Constants

| Name              | Type | Value               | Description |
| ----------------- | ---- | ------------------- | ----------- |
| OCTETS_PER_SAMPLE |      | BITS_PER_SAMPLE / 8 |             |
## Instantiations

- i_pnmon: ad_ip_jesd204_tpl_adc_pnmon
**Description**
instantiations

