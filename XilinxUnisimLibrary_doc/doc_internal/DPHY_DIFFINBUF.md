# Entity: DPHY_DIFFINBUF

## Diagram

![Diagram](DPHY_DIFFINBUF.svg "Diagram")
## Description

    Copyright (c) 1995/2015 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2015.4
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        _no_description_
 /___/   /\      Filename    : DPHY_DIFFINBUF.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name | Type | Value      | Description |
| ------------ | ---- | ---------- | ----------- |
| XIL_TIMING   |      | "UNPLACED" |             |
| DIFF_TERM    |      | "TRUE"     |             |
| ISTANDARD    |      | "DEFAULT"  |             |
## Ports

| Port name    | Direction | Type | Description |
| ------------ | --------- | ---- | ----------- |
| HSRX_O       | output    |      |             |
| LPRX_O_N     | output    |      |             |
| LPRX_O_P     | output    |      |             |
| HSRX_DISABLE | input     |      |             |
| I            | input     |      |             |
| IB           | input     |      |             |
| LPRX_DISABLE | input     |      |             |
## Signals

| Name            | Type        | Description |
| --------------- | ----------- | ----------- |
| trig_attr       | reg         |             |
| DIFF_TERM_BIN   | wire        |             |
| ISTANDARD_BIN   | wire        |             |
| attr_test       | reg         |             |
| attr_test       | reg         |             |
| attr_err        | reg         |             |
| glblGSR         | tri0        |             |
| HSRX_O_out      | wire        |             |
| LPRX_O_N_out    | wire        |             |
| LPRX_O_P_out    | wire        |             |
| HSRX_DISABLE_in | wire        |             |
| IB_in           | wire        |             |
| I_in            | wire        |             |
| LPRX_DISABLE_in | wire        |             |
| o_out           | reg         |             |
| lp_out          | wire [1:0]  |             |
| lp_mode         | wire        |             |
| hs_mode         | wire        |             |
| hs_out          | wire        |             |
| strP            | reg [3*8:1] |             |
| strN            | reg [3*8:1] |             |
## Constants

| Name              | Type   | Value            | Description                        |
| ----------------- | ------ | ---------------- | ---------------------------------- |
| MODULE_NAME       |        | "DPHY_DIFFINBUF" | define constants                   |
| DIFF_TERM_FALSE   |        | 1                | Parameter encodings and registers  |
| DIFF_TERM_TRUE    |        | 0                |                                    |
| ISTANDARD_DEFAULT |        | 0                |                                    |
| DIFF_TERM_REG     | [40:1] | DIFF_TERM        |                                    |
| ISTANDARD_REG     | [56:1] | ISTANDARD        |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(*) )
- unnamed: ( @ (I_in or IB_in) )
