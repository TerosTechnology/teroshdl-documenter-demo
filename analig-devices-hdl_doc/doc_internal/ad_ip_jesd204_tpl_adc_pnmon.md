# Entity: ad_ip_jesd204_tpl_adc_pnmon

- **File**: ad_ip_jesd204_tpl_adc_pnmon.v
## Diagram

![Diagram](ad_ip_jesd204_tpl_adc_pnmon.svg "Diagram")
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
| CONVERTER_RESOLUTION |      | 16    |             |
| DATA_PATH_WIDTH      |      | 1     |             |
| TWOS_COMPLEMENT      |      | 1     |             |
## Ports

| Port name  | Direction | Type                                       | Description                               |
| ---------- | --------- | ------------------------------------------ | ----------------------------------------- |
| clk        | input     |                                            |                                           |
| data       | input     | [CONVERTER_RESOLUTION*DATA_PATH_WIDTH-1:0] | data interface                            |
| pn_oos     | output    |                                            | pn out of sync and error                  |
| pn_err     | output    |                                            |                                           |
| pn_seq_sel | input     | [3:0]                                      | processor interface PN9 (0x0), PN23 (0x1) |
## Signals

| Name            | Type           | Description         |
| --------------- | -------------- | ------------------- |
| pn_data_pn      | reg [PN_W:0]   | internal registers  |
| pn_data_pn_s    | wire [PN_W:0]  | internal signals    |
| pn_data_in_s    | wire [DW:0]    |                     |
| pn_data_init    | wire [PN_W:0]  |                     |
| pn23            | wire [DW:0]    |                     |
| full_state_pn23 | wire [DW+23:0] |                     |
| pn9             | wire [DW:0]    |                     |
| full_state_pn9  | wire [DW+9:0]  |                     |
| tc              | wire           |                     |
## Constants

| Name | Type | Value                                  | Description                             |
| ---- | ---- | -------------------------------------- | --------------------------------------- |
| DW   |      | DATA_PATH_WIDTH*CONVERTER_RESOLUTION-1 |                                         |
| PN_W |      | DW > 22 ? DW : 22                      | Max width of largest PN and data width  |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- i_pnmon: ad_pnmon
**Description**
pn oos & pn err

