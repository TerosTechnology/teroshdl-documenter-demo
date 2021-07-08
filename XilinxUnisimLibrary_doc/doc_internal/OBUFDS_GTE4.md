# Entity: OBUFDS_GTE4

## Diagram

![Diagram](OBUFDS_GTE4.svg "Diagram")
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
  /   /                        Gigabit Transceiver Buffer
 /___/   /\      Filename    : OBUFDS_GTE4.v
 \   \  /  \ 
  \___\/\___\                    
                                 
  Revision:
  03/27/2015 - Initial version from E3
  End Revision:
 
## Generics

| Generic name      | Type  | Value      | Description |
| ----------------- | ----- | ---------- | ----------- |
| XIL_TIMING        |       | "UNPLACED" |             |
| REFCLK_EN_TX_PATH | [0:0] | 1'b0       |             |
| REFCLK_ICNTL_TX   | [4:0] | 5'b00000   |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| OB        | output    |      |             |
| CEB       | input     |      |             |
| I         | input     |      |             |
## Signals

| Name                  | Type      | Description |
| --------------------- | --------- | ----------- |
| trig_attr             | reg       |             |
| REFCLK_EN_TX_PATH_REG | reg [0:0] |             |
| REFCLK_ICNTL_TX_REG   | reg [4:0] |             |
| glblGSR               | reg       |             |
| glblGTS               | reg       |             |
| glblGSR               | tri0      |             |
| glblGTS               | tri0      |             |
## Constants

| Name        | Type | Value         | Description       |
| ----------- | ---- | ------------- | ----------------- |
| MODULE_NAME |      | "OBUFDS_GTE4" | define constants  |
