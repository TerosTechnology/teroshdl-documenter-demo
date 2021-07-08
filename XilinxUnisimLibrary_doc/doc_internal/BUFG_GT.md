# Entity: BUFG_GT

## Diagram

![Diagram](BUFG_GT.svg "Diagram")
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
 \   \   \/      Version     : 2020.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        BUFG_GT
 /___/   /\      Filename    : BUFG_GT.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name | Type | Value        | Description |
| ------------ | ---- | ------------ | ----------- |
| XIL_TIMING   |      | "UNPLACED"   |             |
| SIM_DEVICE   |      | "ULTRASCALE" |             |
| STARTUP_SYNC |      | "FALSE"      |             |
## Ports

| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| O         | output    |       |             |
| CE        | input     |       |             |
| CEMASK    | input     |       |             |
| CLR       | input     |       |             |
| CLRMASK   | input     |       |             |
| DIV       | input     | [2:0] |             |
| I         | input     |       |             |
## Signals

| Name                       | Type        | Description             |
| -------------------------- | ----------- | ----------------------- |
| trig_attr                  | reg         |                         |
| SIM_DEVICE_REG             | reg [144:1] |                         |
| STARTUP_SYNC_REG           | reg [40:1]  |                         |
| SIM_DEVICE_BIN             | wire [4:0]  |                         |
| STARTUP_SYNC_BIN           | wire        |                         |
| SIM_DEVICE_BIN             | reg [4:0]   |                         |
| STARTUP_SYNC_BIN           | reg         |                         |
| glblGSR                    | reg         |                         |
| glblGSR                    | tri0        |                         |
| CEMASK_in                  | wire        |                         |
| CE_in                      | wire        |                         |
| CLRMASK_in                 | wire        |                         |
| CLR_in                     | wire        |                         |
| I_in                       | wire        |                         |
| DIV_in                     | wire [2:0]  |                         |
| attr_test                  | reg         |                         |
| attr_err                   | reg         |                         |
| notifier                   | reg         |                         |
| clk_count                  | integer     | begin behavioral model  |
| first_toggle_count         | integer     | begin behavioral model  |
| second_toggle_count        | integer     | begin behavioral model  |
| first_rise                 | reg         |                         |
| first_half_period          | reg         |                         |
| O_bufg_gt                  | reg         |                         |
| O_bufg_gt_dev              | reg         |                         |
| i_ce                       | wire        |                         |
| i_inv                      | wire        |                         |
| clr_inv                    | wire        |                         |
| ce_masked                  | wire        |                         |
| clrmask_inv                | wire        |                         |
| clr_masked                 | wire        |                         |
| ce_en                      | reg         |                         |
| ce_sync1                   | reg         |                         |
| ce_sync2                   | reg         |                         |
| clr_sync1                  | reg         |                         |
| clr_sync2                  | reg         |                         |
| ce_sync                    | wire        |                         |
| clr_sync                   | wire        |                         |
| gwe_sync                   | reg [2:0]   |                         |
| gsr_muxed_sync             | wire        |                         |
| sim_device_versal_or_later | reg         |                         |
## Constants

| Name                          | Type | Value     | Description                        |
| ----------------------------- | ---- | --------- | ---------------------------------- |
| MODULE_NAME                   |      | "BUFG_GT" | define constants                   |
| SIM_DEVICE_ULTRASCALE         |      | 0         | Parameter encodings and registers  |
| SIM_DEVICE_ULTRASCALE_PLUS    |      | 1         |                                    |
| SIM_DEVICE_VERSAL_AI_CORE     |      | 3         |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES1 |      | 4         |                                    |
| SIM_DEVICE_VERSAL_AI_CORE_ES2 |      | 5         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE     |      | 6         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES1 |      | 7         |                                    |
| SIM_DEVICE_VERSAL_AI_EDGE_ES2 |      | 8         |                                    |
| SIM_DEVICE_VERSAL_AI_RF       |      | 9         |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES1   |      | 10        |                                    |
| SIM_DEVICE_VERSAL_AI_RF_ES2   |      | 11        |                                    |
| SIM_DEVICE_VERSAL_HBM         |      | 14        |                                    |
| SIM_DEVICE_VERSAL_HBM_ES1     |      | 15        |                                    |
| SIM_DEVICE_VERSAL_HBM_ES2     |      | 16        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM     |      | 17        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES1 |      | 18        |                                    |
| SIM_DEVICE_VERSAL_PREMIUM_ES2 |      | 19        |                                    |
| SIM_DEVICE_VERSAL_PRIME       |      | 20        |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES1   |      | 21        |                                    |
| SIM_DEVICE_VERSAL_PRIME_ES2   |      | 22        |                                    |
| STARTUP_SYNC_FALSE            |      | 0         |                                    |
| STARTUP_SYNC_TRUE             |      | 1         |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(posedge I_in) )
- unnamed: ( @(DIV_in) )
- unnamed: ( @(gsr_muxed_sync) )
- unnamed: ( @(posedge I_in, posedge gsr_muxed_sync) )
- unnamed: ( @(posedge I_in, negedge clr_inv) )
- unnamed: ( @(i_inv, gsr_muxed_sync, ce_masked, clr_masked) )
- unnamed: ( @(i_ce or posedge gsr_muxed_sync or posedge clr_masked) )
- unnamed: ( @(*) )
**Description**
assign #1 O =   O_bufg_gt;

