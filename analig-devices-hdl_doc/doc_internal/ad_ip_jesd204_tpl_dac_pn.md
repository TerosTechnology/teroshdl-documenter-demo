# Entity: ad_ip_jesd204_tpl_dac_pn

- **File**: ad_ip_jesd204_tpl_dac_pn.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_dac_pn.svg "Diagram")
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
| DATA_PATH_WIDTH      |      | 4     |             |
| CONVERTER_RESOLUTION |      | 16    |             |
## Ports

| Port name | Direction | Type                                       | Description |
| --------- | --------- | ------------------------------------------ | ----------- |
| clk       | input     |                                            |             |
| reset     | input     |                                            |             |
| pn7_data  | output    | [DATA_PATH_WIDTH*CONVERTER_RESOLUTION-1:0] |             |
| pn15_data | output    | [DATA_PATH_WIDTH*CONVERTER_RESOLUTION-1:0] |             |
## Signals

| Name            | Type            | Description |
| --------------- | --------------- | ----------- |
| pn7_state       | reg [PN7_W:0]   |             |
| pn15_state      | reg [PN15_W:0]  |             |
| pn7             | wire [DW:0]     |             |
| pn7_full_state  | wire [DW+7:0]   |             |
| pn7_reset       | wire [PN7_W:0]  |             |
| pn15            | wire [DW:0]     |             |
| pn15_full_state | wire [DW+15:0]  |             |
| pn15_reset      | wire [PN15_W:0] |             |
## Constants

| Name   | Type | Value                    | Description                                             |
| ------ | ---- | ------------------------ | ------------------------------------------------------- |
| CR     |      | CONVERTER_RESOLUTION     |                                                         |
| DW     |      | DATA_PATH_WIDTH * CR - 1 |                                                         |
| PN7_W  |      | DW > 6 ? DW : 6          |  We need at least enough bits to store the PN state */  |
| PN15_W |      | DW > 14 ? DW : 14        |                                                         |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
