# Entity: IBUFCTRL

## Diagram

![Diagram](IBUFCTRL.svg "Diagram")
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
  /   /                        _no_description_
 /___/   /\      Filename    : IBUFCTRL.v
 \   \  /  \
  \___\/\___\
  Revision:
    10/22/14 - Added #1 to $finish (CR 808642).
  End Revision:
 
## Generics

| Generic name    | Type | Value      | Description |
| --------------- | ---- | ---------- | ----------- |
| XIL_TIMING      |      | "UNPLACED" |             |
| ISTANDARD       |      | "UNUSED"   |             |
| USE_IBUFDISABLE |      | "FALSE"    |             |
## Ports

| Port name     | Direction | Type | Description |
| ------------- | --------- | ---- | ----------- |
| O             | output    |      |             |
| I             | input     |      |             |
| IBUFDISABLE   | input     |      |             |
| INTERMDISABLE | input     |      |             |
| T             | input     |      |             |
## Signals

| Name                 | Type | Description                                   |
| -------------------- | ---- | --------------------------------------------- |
| trig_attr            | reg  | include dynamic registers - XILINX test only  |
| USE_IBUFDISABLE_BIN  | wire |                                               |
| attr_test            | reg  |                                               |
| attr_test            | reg  |                                               |
| attr_err             | reg  |                                               |
| glblGSR              | tri0 |                                               |
| O_out                | wire |                                               |
| O_delay              | wire |                                               |
| IBUFDISABLE_in       | wire |                                               |
| INTERMDISABLE_in     | wire |                                               |
| I_in                 | wire |                                               |
| T_in                 | wire |                                               |
| IBUFDISABLE_delay    | wire |                                               |
| INTERMDISABLE_delay  | wire |                                               |
| I_delay              | wire |                                               |
| T_delay              | wire |                                               |
| NOT_T_OR_IBUFDISABLE | wire |                                               |
## Constants

| Name                  | Type   | Value           | Description                        |
| --------------------- | ------ | --------------- | ---------------------------------- |
| MODULE_NAME           |        | "IBUFCTRL"      | define constants                   |
| in_delay              |        | 0               |                                    |
| out_delay             |        | 0               |                                    |
| inclk_delay           |        | 0               |                                    |
| outclk_delay          |        | 0               |                                    |
| USE_IBUFDISABLE_FALSE |        | 0               | Parameter encodings and registers  |
| USE_IBUFDISABLE_TRUE  |        | 1               |                                    |
| USE_IBUFDISABLE_REG   | [40:1] | USE_IBUFDISABLE |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
