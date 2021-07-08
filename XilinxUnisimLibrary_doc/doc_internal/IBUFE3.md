# Entity: IBUFE3

## Diagram

![Diagram](IBUFE3.svg "Diagram")
## Description

    Copyright (c) 1995/2014 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2014.2
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        Input Buffer with Offset Calibration and VREF Tuning
 /___/   /\      Filename    : IBUFE3.v
 \   \  /  \
  \___\/\___\
  Revision:
    10/22/14 - Added #1 to $finish (CR 808642).
  End Revision:
 
## Generics

| Generic name            | Type    | Value        | Description |
| ----------------------- | ------- | ------------ | ----------- |
| XIL_TIMING              |         | "UNPLACED"   |             |
| IBUF_LOW_PWR            |         | "TRUE"       |             |
| IOSTANDARD              |         | "DEFAULT"    |             |
| SIM_DEVICE              |         | "ULTRASCALE" |             |
| SIM_INPUT_BUFFER_OFFSET | integer | 0            |             |
| USE_IBUFDISABLE         |         | "FALSE"      |             |
## Ports

| Port name   | Direction | Type  | Description |
| ----------- | --------- | ----- | ----------- |
| O           | output    |       |             |
| I           | input     |       |             |
| IBUFDISABLE | input     |       |             |
| OSC         | input     | [3:0] |             |
| OSC_EN      | input     |       |             |
| VREF        | input     |       |             |
## Signals

| Name                        | Type       | Description                                   |
| --------------------------- | ---------- | --------------------------------------------- |
| trig_attr                   | reg        | include dynamic registers - XILINX test only  |
| IBUF_LOW_PWR_BIN            | wire       |                                               |
| SIM_DEVICE_BIN              | wire [4:0] |                                               |
| SIM_INPUT_BUFFER_OFFSET_BIN | wire [6:0] |                                               |
| USE_IBUFDISABLE_BIN         | wire       |                                               |
| attr_test                   | reg        |                                               |
| attr_test                   | reg        |                                               |
| attr_err                    | reg        |                                               |
| glblGSR                     | tri0       |                                               |
| O_out                       | wire       |                                               |
| O_OSC_in                    | reg        |                                               |
| O_delay                     | wire       |                                               |
| IBUFDISABLE_in              | wire       |                                               |
| I_in                        | wire       |                                               |
| OSC_EN_in                   | wire       |                                               |
| VREF_in                     | wire       |                                               |
| OSC_in                      | wire [3:0] |                                               |
| IBUFDISABLE_delay           | wire       |                                               |
| I_delay                     | wire       |                                               |
| OSC_EN_delay                | wire       |                                               |
| VREF_delay                  | wire       |                                               |
| OSC_delay                   | wire [3:0] |                                               |
| OSC_int                     | integer    | begin behavioral model                        |
| versal_or_later             | wire       |                                               |
| OSC_EN_in_muxed             | wire [1:0] |                                               |
| OSC_in_muxed                | wire [3:0] |                                               |
## Constants

| Name                          | Type    | Value                   | Description                        |
| ----------------------------- | ------- | ----------------------- | ---------------------------------- |
| MODULE_NAME                   |         | "IBUFE3"                | define constants                   |
| in_delay                      |         | 0                       |                                    |
| out_delay                     |         | 0                       |                                    |
| inclk_delay                   |         | 0                       |                                    |
| outclk_delay                  |         | 0                       |                                    |
| IBUF_LOW_PWR_FALSE            |         | 1                       | Parameter encodings and registers  |
| IBUF_LOW_PWR_TRUE             |         | 0                       |                                    |
| SIM_DEVICE_ULTRASCALE         |         | 0                       |                                    |
| SIM_DEVICE_ULTRASCALE_PLUS    |         | 1                       |                                    |
| SIM_DEVICE_VERSAL_AI_CORE     |         | 2                       |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES1 |         | 3                       |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES2 |         | 4                       |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE     |         | 5                       |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES1 |         | 6                       |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES2 |         | 7                       |                                    |
| SIM_DEVICE_VERSAL_AI_RF       |         | 8                       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES1   |         | 9                       |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES2   |         | 10                      |                                    |
| SIM_DEVICE_VERSAL_HBM         |         | 11                      |                                    |
| SIM_DEVICE_VERSAL_HBM_ES1     |         | 12                      |                                    |
| SIM_DEVICE_VERSAL_HBM_ES2     |         | 13                      |                                    |
| SIM_DEVICE_VERSAL_PREMIUM     |         | 14                      |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES1 |         | 15                      |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES2 |         | 16                      |                                    |
| SIM_DEVICE_VERSAL_PRIME       |         | 17                      |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES1   |         | 18                      |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES2   |         | 19                      |                                    |
| USE_IBUFDISABLE_FALSE         |         | 0                       |                                    |
| USE_IBUFDISABLE_TRUE          |         | 1                       |                                    |
| IBUF_LOW_PWR_REG              | [40:1]  | IBUF_LOW_PWR            |                                    |
| SIM_INPUT_BUFFER_OFFSET_REG   | integer | SIM_INPUT_BUFFER_OFFSET |                                    |
| USE_IBUFDISABLE_REG           | [40:1]  | USE_IBUFDISABLE         |                                    |
| SIM_DEVICE_REG                | [144:1] | SIM_DEVICE              |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (OSC_in_muxed or OSC_EN_in_muxed) )
