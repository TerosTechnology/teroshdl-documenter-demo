# Entity: ad_pngen

## Diagram

![Diagram](ad_pngen.svg "Diagram")
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
 Generic parallel PN generator
 
## Generics

| Generic name | Type | Value                                       | Description                                 |
| ------------ | ---- | ------------------------------------------- | ------------------------------------------- |
| POL_MASK     |      | 32'b0000_0000_0000_0000_0000_0000_1100_0000 | PN7 x^7 + x^6 + 1                           |
| POL_W        |      | 7                                           |                                             |
| DW           |      | 16                                          | Number of output bits at every clock cycle  |
## Ports

| Port name   | Direction | Type     | Description                                                        |
| ----------- | --------- | -------- | ------------------------------------------------------------------ |
| clk         | input     |          |                                                                    |
| reset       | input     |          |                                                                    |
| clk_en      | input     |          |                                                                    |
| pn_data_out | output    | [DW-1:0] | MSB has the oldest value,                                          |
| pn_init     | input     |          | LSB has the latest valueInput stream to synchronize to (Optional)  |
| pn_data_in  | input     | [DW-1:0] |                                                                    |
## Signals

| Name          | Type                | Description |
| ------------- | ------------------- | ----------- |
| pn_state      | reg [PN_W-1:0]      |             |
| pn            | wire [DW-1:0]       |             |
| pn_full_state | wire [DW+POL_W-1:0] |             |
| pn_reset      | wire [PN_W-1:0]     |             |
| pn_state_     | wire [PN_W-1:0]     |             |
| pn_init_data  | wire [PN_W-1:0]     |             |
## Constants

| Name | Type | Value                   | Description                                            |
| ---- | ---- | ----------------------- | ------------------------------------------------------ |
| PN_W |      | DW > POL_W ? DW : POL_W | We need at least enough bits to store the PN state */  |
## Processes
- unnamed: ( @(posedge clk) )
