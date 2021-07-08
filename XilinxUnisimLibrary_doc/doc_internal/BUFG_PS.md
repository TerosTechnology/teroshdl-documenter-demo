# Entity: BUFG_PS

## Diagram

![Diagram](BUFG_PS.svg "Diagram")
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
 \   \   \/      Version     : 2019.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        A high-fanout buffer for low-skew distribution of the PS Clock signals
 /___/   /\      Filename    : BUFG_PS.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name | Type | Value             | Description |
| ------------ | ---- | ----------------- | ----------- |
| XIL_TIMING   |      | "UNPLACED"        |             |
| SIM_DEVICE   |      | "ULTRASCALE_PLUS" |             |
| STARTUP_SYNC |      | "FALSE"           |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| I         | input     |      |             |
## Signals

| Name             | Type        | Description             |
| ---------------- | ----------- | ----------------------- |
| trig_attr        | reg         |                         |
| SIM_DEVICE_REG   | reg [144:1] |                         |
| STARTUP_SYNC_REG | reg [40:1]  |                         |
| SIM_DEVICE_BIN   | wire [4:0]  |                         |
| STARTUP_SYNC_BIN | wire        |                         |
| SIM_DEVICE_BIN   | reg [4:0]   |                         |
| STARTUP_SYNC_BIN | reg         |                         |
| glblGSR          | reg         |                         |
| glblGSR          | tri0        |                         |
| attr_test        | reg         |                         |
| attr_err         | reg         |                         |
| notifier         | reg         |                         |
| enable_clk       | reg         | begin behavioral model  |
| gwe_sync         | reg [2:0]   |                         |
| gwe_muxed_sync   | wire        |                         |
| gwe_latch        | reg         |                         |
| I_in             | wire        |                         |
| O_out            | reg         |                         |
## Constants

| Name                          | Type | Value     | Description                        |
| ----------------------------- | ---- | --------- | ---------------------------------- |
| MODULE_NAME                   |      | "BUFG_PS" | define constants                   |
| SIM_DEVICE_ULTRASCALE_PLUS    |      | 0         | Parameter encodings and registers  |
| SIM_DEVICE_VERSAL_AI_CORE     |      | 2         |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES1 |      | 3         |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES2 |      | 4         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE     |      | 5         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES1 |      | 6         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES2 |      | 7         |                                    |
| SIM_DEVICE_VERSAL_AI_RF       |      | 8         |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES1   |      | 9         |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES2   |      | 10        |                                    |
| SIM_DEVICE_VERSAL_HBM         |      | 13        |                                    |
| SIM_DEVICE_VERSAL_HBM_ES1     |      | 14        |                                    |
| SIM_DEVICE_VERSAL_HBM_ES2     |      | 15        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM     |      | 16        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES1 |      | 17        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES2 |      | 18        |                                    |
| SIM_DEVICE_VERSAL_PRIME       |      | 19        |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES1   |      | 20        |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES2   |      | 21        |                                    |
| STARTUP_SYNC_FALSE            |      | 0         |                                    |
| STARTUP_SYNC_TRUE             |      | 1         |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(posedge I_in) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
