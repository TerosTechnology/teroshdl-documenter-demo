# Entity: ODDRE1

## Diagram

![Diagram](ODDRE1.svg "Diagram")
## Description

    Copyright (c) 1995/2019 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2019.2
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        ODDRE1
 /___/   /\      Filename    : ODDRE1.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name   | Type  | Value        | Description |
| -------------- | ----- | ------------ | ----------- |
| XIL_TIMING     |       | "UNPLACED"   |             |
| IS_C_INVERTED  | [0:0] | 1'b0         |             |
| IS_D1_INVERTED | [0:0] | 1'b0         |             |
| IS_D2_INVERTED | [0:0] | 1'b0         |             |
| SIM_DEVICE     |       | "ULTRASCALE" |             |
| SRVAL          | [0:0] | 1'b0         |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| Q         | output    |      |             |
| C         | input     |      |             |
| D1        | input     |      |             |
| D2        | input     |      |             |
| SR        | input     |      |             |
## Signals

| Name               | Type        | Description             |
| ------------------ | ----------- | ----------------------- |
| trig_attr          | reg         |                         |
| IS_C_INVERTED_REG  | reg [0:0]   |                         |
| IS_D1_INVERTED_REG | reg [0:0]   |                         |
| IS_D2_INVERTED_REG | reg [0:0]   |                         |
| SIM_DEVICE_REG     | reg [152:1] |                         |
| SRVAL_REG          | reg [0:0]   |                         |
| SIM_DEVICE_BIN     | wire [4:0]  |                         |
| SIM_DEVICE_BIN     | reg [4:0]   |                         |
| glblGSR            | reg         |                         |
| glblGSR            | tri0        |                         |
| C_in               | wire        |                         |
| D1_in              | wire        |                         |
| D2_in              | wire        |                         |
| SR_in              | wire        |                         |
| C_delay            | wire        |                         |
| D1_delay           | wire        |                         |
| D2_delay           | wire        |                         |
| SR_delay           | wire        |                         |
| attr_test          | reg         |                         |
| attr_err           | reg         |                         |
| notifier           | reg         |                         |
| Q_out              | reg         | begin behavioral model  |
| QD2_posedge_int    | reg         |                         |
| R_sync1            | reg         |                         |
| R_sync2            | reg         |                         |
| R_sync3            | reg         |                         |
| R_sync             | wire        |                         |
| R_async            | wire        |                         |
| c_en_n             | wire        |                         |
| c_en_p             | wire        |                         |
## Constants

| Name                           | Type | Value    | Description                        |
| ------------------------------ | ---- | -------- | ---------------------------------- |
| MODULE_NAME                    |      | "ODDRE1" | define constants                   |
| SIM_DEVICE_ULTRASCALE          |      | 0        | Parameter encodings and registers  |
| SIM_DEVICE_ULTRASCALE_PLUS     |      | 1        |                                    |
| SIM_DEVICE_ULTRASCALE_PLUS_ES1 |      | 2        |                                    |
| SIM_DEVICE_ULTRASCALE_PLUS_ES2 |      | 3        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE      |      | 5        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES1  |      | 6        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES2  |      | 7        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE      |      | 8        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES1  |      | 9        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES2  |      | 10       |                                    |
| SIM_DEVICE_VERSAL_AI_RF        |      | 11       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES1    |      | 12       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES2    |      | 13       |                                    |
| SIM_DEVICE_VERSAL_HBM          |      | 16       |                                    |
| SIM_DEVICE_VERSAL_HBM_ES1      |      | 17       |                                    |
| SIM_DEVICE_VERSAL_HBM_ES2      |      | 18       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM      |      | 19       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES1  |      | 20       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES2  |      | 21       |                                    |
| SIM_DEVICE_VERSAL_PRIME        |      | 22       |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES1    |      | 23       |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES2    |      | 24       |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(posedge C_in) )
- unnamed: ( @ (glblGSR or SR_in or R_sync) )
- unnamed: ( @(posedge C_in) )
- unnamed: ( @(negedge C_in) )
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
