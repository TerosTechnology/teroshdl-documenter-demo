# Entity: IBUFDS_GTE4

## Diagram

![Diagram](IBUFDS_GTE4.svg "Diagram")
## Description

    Copyright (c) 1995/2017 Xilinx, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____  ____
  /   /\/   / 
 /___/  \  /     Vendor      : Xilinx 
 \   \   \/      Version     : 2017.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        Gigabit Transceiver Buffer
 /___/   /\      Filename    : IBUFDS_GTE4.v
 \   \  /  \ 
  \___\/\___\                    
                                 
  Revision:
  03/27/2015 - Initial version from E3
  End Revision:
 
## Generics

| Generic name       | Type  | Value      | Description |
| ------------------ | ----- | ---------- | ----------- |
| XIL_TIMING         |       | "UNPLACED" |             |
| REFCLK_EN_TX_PATH  | [0:0] | 1'b0       |             |
| REFCLK_HROW_CK_SEL | [1:0] | 2'b00      |             |
| REFCLK_ICNTL_RX    | [1:0] | 2'b00      |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| ODIV2     | output    |      |             |
| CEB       | input     |      |             |
| I         | input     |      |             |
| IB        | input     |      |             |
## Signals

| Name                   | Type      | Description                                                                                                             |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| trig_attr              | reg       |                                                                                                                         |
| REFCLK_EN_TX_PATH_REG  | reg [0:0] |                                                                                                                         |
| REFCLK_HROW_CK_SEL_REG | reg [1:0] |                                                                                                                         |
| REFCLK_ICNTL_RX_REG    | reg [1:0] |                                                                                                                         |
| attr_test              | reg       |                                                                                                                         |
| attr_test              | reg       |                                                                                                                         |
| attr_err               | reg       |                                                                                                                         |
| glblGSR                | tri0      |                                                                                                                         |
| ODIV2_out              | reg       | wire CEB_in; wire IB_in; wire I_in; assign CEB_in = (CEB !== 1'bz) && CEB; // rv 0 assign IB_in = IB; assign I_in = I;  |
| ce_count               | reg [2:0] |                                                                                                                         |
| edge_count             | reg [2:0] |                                                                                                                         |
| allEqual               | reg       |                                                                                                                         |
## Constants

| Name        | Type | Value         | Description       |
| ----------- | ---- | ------------- | ----------------- |
| MODULE_NAME |      | "IBUFDS_GTE4" | define constants  |
## Processes
- unnamed: ( @(posedge I) )
**Description**
=====================
Count the rising edges of the clk
=====================

- unnamed: ( @(edge_count) )
**Description**
Generate synchronous reset after DIVIDE number of counts

- unnamed: ( @(*) )
**Description**
=====================
Generate ODIV2
=====================

