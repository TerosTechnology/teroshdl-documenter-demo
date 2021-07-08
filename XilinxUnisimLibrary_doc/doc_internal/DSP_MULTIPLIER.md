# Entity: DSP_MULTIPLIER

## Diagram

![Diagram](DSP_MULTIPLIER.svg "Diagram")
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
 \   \   \/      Version     : 2018.3
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        DSP_MULTIPLIER
 /___/   /\      Filename    : DSP_MULTIPLIER.v
 \   \  /  \
  \___\/\___\
  Revision:
  07/15/12 - Migrate from E1.
  12/10/12 - Add dynamic registers
  10/22/14 - 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name | Type | Value      | Description |
| ------------ | ---- | ---------- | ----------- |
| XIL_TIMING   |      | "UNPLACED" |             |
| AMULTSEL     |      | "A"        |             |
| BMULTSEL     |      | "B"        |             |
| USE_MULT     |      | "MULTIPLY" |             |
## Ports

| Port name | Direction | Type   | Description |
| --------- | --------- | ------ | ----------- |
| AMULT26   | output    |        |             |
| BMULT17   | output    |        |             |
| U         | output    | [44:0] |             |
| V         | output    | [44:0] |             |
| A2A1      | input     | [26:0] |             |
| AD_DATA   | input     | [26:0] |             |
| B2B1      | input     | [17:0] |             |
## Signals

| Name         | Type              | Description |
| ------------ | ----------------- | ----------- |
| trig_attr    | reg               |             |
| AMULTSEL_REG | reg [16:1]        |             |
| BMULTSEL_REG | reg [16:1]        |             |
| USE_MULT_REG | reg [64:1]        |             |
| AMULTSEL_BIN | wire              |             |
| BMULTSEL_BIN | wire              |             |
| USE_MULT_BIN | wire [1:0]        |             |
| AMULTSEL_BIN | reg               |             |
| BMULTSEL_BIN | reg               |             |
| USE_MULT_BIN | reg [1:0]         |             |
| glblGSR      | reg               |             |
| glblGSR      | tri0              |             |
| attr_test    | reg               |             |
| attr_err     | reg               |             |
| b_mult_mux   | reg [17:0]        |             |
| a_mult_mux   | reg [26:0]        |             |
| mult         | reg [M_WIDTH-1:0] |             |
| ps_u_mask    | reg [M_WIDTH-2:0] |             |
| ps_v_mask    | reg [M_WIDTH-2:0] |             |
## Constants

| Name              | Type | Value            | Description                        |
| ----------------- | ---- | ---------------- | ---------------------------------- |
| MODULE_NAME       |      | "DSP_MULTIPLIER" | define constants                   |
| AMULTSEL_A        |      | 0                | Parameter encodings and registers  |
| AMULTSEL_AD       |      | 1                |                                    |
| BMULTSEL_AD       |      | 1                |                                    |
| BMULTSEL_B        |      | 0                |                                    |
| USE_MULT_DYNAMIC  |      | 1                |                                    |
| USE_MULT_MULTIPLY |      | 0                |                                    |
| USE_MULT_NONE     |      | 2                |                                    |
| M_WIDTH           |      | 45               | begin behavioral model             |
## Processes
- unnamed: ( @(trig_attr) )
- unnamed: ( @(trig_attr) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
