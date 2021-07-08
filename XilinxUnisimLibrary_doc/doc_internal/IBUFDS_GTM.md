# Entity: IBUFDS_GTM

## Diagram

![Diagram](IBUFDS_GTM.svg "Diagram")
## Description

    Copyright (c) 1995/2018 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2018.2
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        IBUFDS_GTM
 /___/   /\      Filename    : IBUFDS_GTM.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name       | Type    | Value      | Description |
| ------------------ | ------- | ---------- | ----------- |
| XIL_TIMING         |         | "UNPLACED" |             |
| REFCLK_EN_TX_PATH  | [0:0]   | 1'b0       |             |
| REFCLK_HROW_CK_SEL | integer | 0          |             |
| REFCLK_ICNTL_RX    | integer | 0          |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| ODIV2     | output    |      |             |
| CEB       | input     |      |             |
| I         | input     |      |             |
| IB        | input     |      |             |
## Signals

| Name                   | Type       | Description             |
| ---------------------- | ---------- | ----------------------- |
| trig_attr              | reg        |                         |
| REFCLK_EN_TX_PATH_REG  | reg [0:0]  |                         |
| REFCLK_HROW_CK_SEL_REG | reg [31:0] |                         |
| REFCLK_ICNTL_RX_REG    | reg [31:0] |                         |
| REFCLK_HROW_CK_SEL_BIN | wire [1:0] |                         |
| REFCLK_ICNTL_RX_BIN    | wire [1:0] |                         |
| REFCLK_HROW_CK_SEL_BIN | reg [1:0]  |                         |
| REFCLK_ICNTL_RX_BIN    | reg [1:0]  |                         |
| glblGSR                | reg        |                         |
| glblGSR                | tri0       |                         |
| attr_test              | reg        |                         |
| attr_err               | reg        |                         |
| ODIV2_out              | reg        | begin behavioral model  |
| ce_count               | reg [2:0]  |                         |
| edge_count             | reg [2:0]  |                         |
| allEqual               | reg        |                         |
## Constants

| Name        | Type | Value        | Description       |
| ----------- | ---- | ------------ | ----------------- |
| MODULE_NAME |      | "IBUFDS_GTM" | define constants  |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
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

