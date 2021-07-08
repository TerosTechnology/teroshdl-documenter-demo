# Entity: DSP_A_B_DATA

## Diagram

![Diagram](DSP_A_B_DATA.svg "Diagram")
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
  /   /                        DSP_A_B_DATA
 /___/   /\      Filename    : DSP_A_B_DATA.v
 \   \  /  \
  \___\/\___\
  Revision:
  07/15/12 - Migrate from E1.
  12/10/12 - Add dynamic registers
  03/06/13 - 701316 - A_B_reg no clk when REG=0
  04/08/13 - 710304 - AREG, BREG, ACASCREG and BCASCREG dynamic registers mis sized.
  04/22/13 - 714213 - ACOUT, BCOUT wrong logic
  04/23/13 - 714772 - remove sensitivity to negedge GSR
  05/07/13 - 716896 - AREG, BREG, ACASCREG and BCASCREG localparams mis sized.
  10/22/14 - 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name     | Type    | Value      | Description |
| ---------------- | ------- | ---------- | ----------- |
| XIL_TIMING       |         | "UNPLACED" |             |
| ACASCREG         | integer | 1          |             |
| AREG             | integer | 1          |             |
| A_INPUT          |         | "DIRECT"   |             |
| BCASCREG         | integer | 1          |             |
| BREG             | integer | 1          |             |
| B_INPUT          |         | "DIRECT"   |             |
| IS_CLK_INVERTED  | [0:0]   | 1'b0       |             |
| IS_RSTA_INVERTED | [0:0]   | 1'b0       |             |
| IS_RSTB_INVERTED | [0:0]   | 1'b0       |             |
## Ports

| Port name | Direction | Type   | Description |
| --------- | --------- | ------ | ----------- |
| A1_DATA   | output    | [26:0] |             |
| A2_DATA   | output    | [26:0] |             |
| ACOUT     | output    | [29:0] |             |
| A_ALU     | output    | [29:0] |             |
| B1_DATA   | output    | [17:0] |             |
| B2_DATA   | output    | [17:0] |             |
| BCOUT     | output    | [17:0] |             |
| B_ALU     | output    | [17:0] |             |
| A         | input     | [29:0] |             |
| ACIN      | input     | [29:0] |             |
| B         | input     | [17:0] |             |
| BCIN      | input     | [17:0] |             |
| CEA1      | input     |        |             |
| CEA2      | input     |        |             |
| CEB1      | input     |        |             |
| CEB2      | input     |        |             |
| CLK       | input     |        |             |
| RSTA      | input     |        |             |
| RSTB      | input     |        |             |
## Signals

| Name                 | Type              | Description |
| -------------------- | ----------------- | ----------- |
| trig_attr            | reg               |             |
| ACASCREG_REG         | reg [31:0]        |             |
| AREG_REG             | reg [31:0]        |             |
| A_INPUT_REG          | reg [56:1]        |             |
| BCASCREG_REG         | reg [31:0]        |             |
| BREG_REG             | reg [31:0]        |             |
| B_INPUT_REG          | reg [56:1]        |             |
| IS_CLK_INVERTED_REG  | reg [0:0]         |             |
| IS_RSTA_INVERTED_REG | reg [0:0]         |             |
| IS_RSTB_INVERTED_REG | reg [0:0]         |             |
| ACASCREG_BIN         | wire [1:0]        |             |
| AREG_BIN             | wire [1:0]        |             |
| A_INPUT_BIN          | wire              |             |
| BCASCREG_BIN         | wire [1:0]        |             |
| BREG_BIN             | wire [1:0]        |             |
| B_INPUT_BIN          | wire              |             |
| ACASCREG_BIN         | reg [1:0]         |             |
| AREG_BIN             | reg [1:0]         |             |
| A_INPUT_BIN          | reg               |             |
| BCASCREG_BIN         | reg [1:0]         |             |
| BREG_BIN             | reg [1:0]         |             |
| B_INPUT_BIN          | reg               |             |
| glblGSR              | reg               |             |
| glblGSR              | tri0              |             |
| CEA1_in              | wire              |             |
| CEA2_in              | wire              |             |
| CEB1_in              | wire              |             |
| CEB2_in              | wire              |             |
| CLK_in               | wire              |             |
| RSTA_in              | wire              |             |
| RSTB_in              | wire              |             |
| BCIN_in              | wire [17:0]       |             |
| B_in                 | wire [17:0]       |             |
| ACIN_in              | wire [29:0]       |             |
| A_in                 | wire [29:0]       |             |
| CEA1_delay           | wire              |             |
| CEA2_delay           | wire              |             |
| CEB1_delay           | wire              |             |
| CEB2_delay           | wire              |             |
| CLK_delay            | wire              |             |
| RSTA_delay           | wire              |             |
| RSTB_delay           | wire              |             |
| BCIN_delay           | wire [17:0]       |             |
| B_delay              | wire [17:0]       |             |
| ACIN_delay           | wire [29:0]       |             |
| A_delay              | wire [29:0]       |             |
| attr_test            | reg               |             |
| attr_err             | reg               |             |
| notifier             | reg               |             |
| A1_reg               | reg [29:0]        |             |
| A2_reg               | reg [29:0]        |             |
| B_BCIN_mux           | wire [17:0]       |             |
| B2_reg               | reg [17:0]        |             |
| B1_DATA_out          | reg [B_WIDTH-1:0] |             |
| clk_en_n             | wire              |             |
| clk_en_p             | wire              |             |
## Constants

| Name            | Type | Value          | Description                        |
| --------------- | ---- | -------------- | ---------------------------------- |
| MODULE_NAME     |      | "DSP_A_B_DATA" | define constants                   |
| A_INPUT_CASCADE |      | 1              | Parameter encodings and registers  |
| A_INPUT_DIRECT  |      | 0              |                                    |
| B_INPUT_CASCADE |      | 1              |                                    |
| B_INPUT_DIRECT  |      | 0              |                                    |
| A_WIDTH         |      | 30             |                                    |
| B_WIDTH         |      | 18             |                                    |
## Processes
- unnamed: ( @(trig_attr) )
- unnamed: ( @(trig_attr) )
- unnamed: ( @(trig_attr) )
**Description**
begin behavioral model

- unnamed: ( @(posedge CLK_in) )
- unnamed: ( @(posedge CLK_in) )
- unnamed: ( @(posedge CLK_in) )
- unnamed: ( @(posedge CLK_in) )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
