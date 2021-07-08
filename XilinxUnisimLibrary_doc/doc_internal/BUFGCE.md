# Entity: BUFGCE

## Diagram

![Diagram](BUFGCE.svg "Diagram")
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
 \   \   \/      Version     : 2019.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        General Clock Buffer with Clock Enable
 /___/   /\      Filename    : BUFGCE.v
 \   \  /  \
  \___\/\___\
  Revision:
    05/15/12 - Initial version.
    10/22/14 - 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name   | Type  | Value        | Description |
| -------------- | ----- | ------------ | ----------- |
| XIL_TIMING     |       | "UNPLACED"   |             |
| CE_TYPE        |       | "SYNC"       |             |
| IS_CE_INVERTED | [0:0] | 1'b0         |             |
| IS_I_INVERTED  | [0:0] | 1'b0         |             |
| SIM_DEVICE     |       | "ULTRASCALE" |             |
| STARTUP_SYNC   |       | "FALSE"      |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| CE        | input     |      |             |
| I         | input     |      |             |
## Signals

| Name               | Type        | Description             |
| ------------------ | ----------- | ----------------------- |
| trig_attr          | reg         |                         |
| CE_TYPE_REG        | reg [64:1]  |                         |
| IS_CE_INVERTED_REG | reg [0:0]   |                         |
| IS_I_INVERTED_REG  | reg [0:0]   |                         |
| SIM_DEVICE_REG     | reg [144:1] |                         |
| STARTUP_SYNC_REG   | reg [40:1]  |                         |
| CE_TYPE_BIN        | wire [1:0]  |                         |
| SIM_DEVICE_BIN     | wire [4:0]  |                         |
| STARTUP_SYNC_BIN   | wire        |                         |
| CE_TYPE_BIN        | reg [1:0]   |                         |
| SIM_DEVICE_BIN     | reg [4:0]   |                         |
| STARTUP_SYNC_BIN   | reg         |                         |
| glblGSR            | reg         |                         |
| glblGSR            | tri0        |                         |
| CE_in              | wire        |                         |
| I_in               | wire        |                         |
| CE_delay           | wire        |                         |
| I_delay            | wire        |                         |
| attr_test          | reg         |                         |
| attr_err           | reg         |                         |
| notifier           | reg         |                         |
| O_out              | reg         | begin behavioral model  |
| enable_clk         | reg         |                         |
| gwe_sync           | reg [2:0]   |                         |
| gwe_muxed_sync     | wire        |                         |
| ce_sync            | reg [2:0]   |                         |
| ce_muxed_sync      | wire        |                         |
| cb                 | wire        |                         |
| i_en_n             | wire        |                         |
| i_en_p             | wire        |                         |
## Constants

| Name                          | Type | Value    | Description                        |
| ----------------------------- | ---- | -------- | ---------------------------------- |
| MODULE_NAME                   |      | "BUFGCE" | define constants                   |
| CE_TYPE_ASYNC                 |      | 1        | Parameter encodings and registers  |
| CE_TYPE_HARDSYNC              |      | 2        |                                    |
| CE_TYPE_SYNC                  |      | 0        |                                    |
| SIM_DEVICE_7SERIES            |      | 1        |                                    |
| SIM_DEVICE_ULTRASCALE         |      | 0        |                                    |
| SIM_DEVICE_ULTRASCALE_PLUS    |      | 2        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE     |      | 4        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES1 |      | 5        |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES2 |      | 6        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE     |      | 7        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES1 |      | 8        |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES2 |      | 9        |                                    |
| SIM_DEVICE_VERSAL_AI_RF       |      | 10       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES1   |      | 11       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES2   |      | 12       |                                    |
| SIM_DEVICE_VERSAL_HBM         |      | 15       |                                    |
| SIM_DEVICE_VERSAL_HBM_ES1     |      | 16       |                                    |
| SIM_DEVICE_VERSAL_HBM_ES2     |      | 17       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM     |      | 18       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES1 |      | 19       |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES2 |      | 20       |                                    |
| SIM_DEVICE_VERSAL_PRIME       |      | 21       |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES1   |      | 22       |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES2   |      | 23       |                                    |
| STARTUP_SYNC_FALSE            |      | 0        |                                    |
| STARTUP_SYNC_TRUE             |      | 1        |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(posedge I_in ) )
- unnamed: ( @(posedge I_in ) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
