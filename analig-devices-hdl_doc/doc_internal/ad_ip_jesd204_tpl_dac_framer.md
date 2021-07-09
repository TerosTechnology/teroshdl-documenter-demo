# Entity: ad_ip_jesd204_tpl_dac_framer

## Diagram

![Diagram](ad_ip_jesd204_tpl_dac_framer.svg "Diagram")
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

| Generic name         | Type | Value                                                    | Description |
| -------------------- | ---- | -------------------------------------------------------- | ----------- |
| NUM_LANES            |      | 8                                                        |             |
| NUM_CHANNELS         |      | 4                                                        |             |
| BITS_PER_SAMPLE      |      | 16                                                       |             |
| CONVERTER_RESOLUTION |      | 16                                                       |             |
| SAMPLES_PER_FRAME    |      | 2                                                        |             |
| OCTETS_PER_BEAT      |      | 4                                                        |             |
| LINK_DATA_WIDTH      |      | OCTETS_PER_BEAT * 8 * NUM_LANES                          |             |
| DAC_DATA_WIDTH       |      | LINK_DATA_WIDTH * CONVERTER_RESOLUTION / BITS_PER_SAMPLE |             |
## Ports

| Port name | Direction | Type                  | Description    |
| --------- | --------- | --------------------- | -------------- |
| link_data | output    | [LINK_DATA_WIDTH-1:0] | jesd interface |
| dac_data  | input     | [DAC_DATA_WIDTH-1:0]  | dac interface  |
## Signals

| Name            | Type                       | Description |
| --------------- | -------------------------- | ----------- |
| link_data_msb_s | wire [LINK_DATA_WIDTH-1:0] |             |
| frame_data_s    | wire [LINK_DATA_WIDTH-1:0] |             |
| dac_data_msb    | wire [LINK_DATA_WIDTH-1:0] |             |
## Constants

| Name                       | Type | Value                                         | Description |
| -------------------------- | ---- | --------------------------------------------- | ----------- |
| BITS_PER_CHANNEL_PER_FRAME |      | BITS_PER_SAMPLE * SAMPLES_PER_FRAME           |             |
| BITS_PER_LANE_PER_FRAME    |      | BITS_PER_CHANNEL_PER_FRA                      |             |
| FRAMES_PER_BEAT            |      | OCTETS_PER_BEAT * 8 / BITS_PER_LANE_PER_FRAME |             |
| SAMPLES_PER_BEAT           |      | DAC_DATA_WIDTH / CONVERTER_RESOLUTION         |             |
| TAIL_BITS                  |      | BITS_PER_SAMPLE - CONVERTER_RESOLUTION        |             |
