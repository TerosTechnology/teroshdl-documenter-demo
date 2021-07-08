# Entity: HARD_SYNC

## Diagram

![Diagram](HARD_SYNC.svg "Diagram")
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
 \   \   \/      Version     : 2016.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        Metastability Hardened Registers
 /___/   /\      Filename    : HARD_SYNC.v
 \   \  /  \
  \___\/\___\
  Revision:
  01/30/13 Initial version
  05/08/13 712367 - fix blocking assignments
  05/17/13 718960 - fix BIN encoding
  05/17/13 719092 - remove SR, add IS_CLK_INVERTED
  10/22/14 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name    | Type    | Value      | Description |
| --------------- | ------- | ---------- | ----------- |
| XIL_TIMING      |         | "UNPLACED" |             |
| INIT            | [0:0]   | 1'b0       |             |
| IS_CLK_INVERTED | [0:0]   | 1'b0       |             |
| LATENCY         | integer | 2          |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| DOUT      | output    |      |             |
| CLK       | input     |      |             |
| DIN       | input     |      |             |
## Signals

| Name                | Type      | Description |
| ------------------- | --------- | ----------- |
| trig_attr           | reg       |             |
| INIT_BIN            | wire      |             |
| IS_CLK_INVERTED_BIN | wire      |             |
| LATENCY_BIN         | wire      |             |
| glblGSR             | tri0      |             |
| attr_test           | reg       |             |
| attr_test           | reg       |             |
| attr_err            | reg       |             |
| glblGSR             | tri0      |             |
| CLK_in              | wire      |             |
| DIN_in              | wire      |             |
| CLK_delay           | wire      |             |
| DIN_delay           | wire      |             |
| DIN_reg             | reg [2:0] |             |
| notifier            | reg       |             |
| clk_en_n            | wire      |             |
| clk_en_p            | wire      |             |
## Constants

| Name                | Type  | Value           | Description                        |
| ------------------- | ----- | --------------- | ---------------------------------- |
| MODULE_NAME         |       | "HARD_SYNC"     | define constants                   |
| LATENCY_2           |       | 0               | Parameter encodings and registers  |
| LATENCY_3           |       | 1               |                                    |
| INIT_REG            | [0:0] | INIT            |                                    |
| IS_CLK_INVERTED_REG | [0:0] | IS_CLK_INVERTED |                                    |
| LATENCY_REG         | [1:0] | LATENCY         |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (posedge CLK_in or posedge glblGSR) )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
