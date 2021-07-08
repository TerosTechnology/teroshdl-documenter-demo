# Entity: IBUFDS_GTE3

## Diagram

![Diagram](IBUFDS_GTE3.svg "Diagram")
## Description

    Copyright (c) 2013 Xilinx Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____   ___
  /   /\/   / 
 /___/  \  /     Vendor      : Xilinx 
 \   \   \/      Version     : 2012.2
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        
 /___/   /\      Filename    : IBUFDS_GTE3.v
 \   \  /  \ 
  \___\/\___\                    
                                 
  Revision:
  12/11/2012 - Initial version
  03/22/2013 - Model added
  03/25/2013 - Sync 5 YML & model update
  04/12/2013 - Add attribute section
  08/28/2013 - Add specify section
  06/02/2014 - New simulation library message format.
    10/22/14 - Added #1 to $finish (CR 808642).
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

| Name                   | Type       | Description |
| ---------------------- | ---------- | ----------- |
| REFCLK_EN_TX_PATH_BIN  | wire       |             |
| REFCLK_HROW_CK_SEL_BIN | wire [1:0] |             |
| REFCLK_ICNTL_RX_BIN    | wire [1:0] |             |
| i_in                   | wire       |             |
| ib_in                  | wire       |             |
| ceb_in                 | wire       |             |
| GSR                    | tri0       |             |
| notifier               | reg        |             |
| ODIV2_out              | reg        |             |
| O_out                  | wire       |             |
| ce_count               | reg [2:0]  |             |
| edge_count             | reg [2:0]  |             |
| allEqual               | reg        |             |
## Constants

| Name                   | Type  | Value              | Description       |
| ---------------------- | ----- | ------------------ | ----------------- |
| MODULE_NAME            |       | "IBUFDS_GTE3"      | define constants  |
| REFCLK_EN_TX_PATH_REG  | [0:0] | REFCLK_EN_TX_PATH  |                   |
| REFCLK_HROW_CK_SEL_REG | [1:0] | REFCLK_HROW_CK_SEL |                   |
| REFCLK_ICNTL_RX_REG    | [1:0] | REFCLK_ICNTL_RX    |                   |
## Processes
- unnamed: ( @(posedge I) )
**Description**
initial begin
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

