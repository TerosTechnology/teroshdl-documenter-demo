# Entity: CARRY8

## Diagram

![Diagram](CARRY8.svg "Diagram")
## Description

    Copyright (c) 1995/2016 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2016.4
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        Fast Carry Logic with Look Ahead
 /___/   /\      Filename    : CARRY8.v
 \   \  /  \
  \___\/\___\
  Revision
    09/26/12 - Initial functional version.
    05/24/13 - Add CARRY_TYPE, CI_TOP
    10/22/14 - 808642 - Added #1 to $finish
  End Revision
 
## Generics

| Generic name | Type | Value        | Description |
| ------------ | ---- | ------------ | ----------- |
| XIL_TIMING   |      | "UNPLACED"   |             |
| CARRY_TYPE   |      | "SINGLE_CY8" |             |
## Ports

| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| CO        | output    | [7:0] |             |
| O         | output    | [7:0] |             |
| CI        | input     |       |             |
| CI_TOP    | input     |       |             |
| DI        | input     | [7:0] |             |
| S         | input     | [7:0] |             |
## Signals

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| trig_attr      | reg        |             |
| CARRY_TYPE_REG | reg [80:1] |             |
| CARRY_TYPE_BIN | wire       |             |
| CARRY_TYPE_BIN | reg        |             |
| attr_test      | reg        |             |
| attr_test      | reg        |             |
| attr_err       | reg        |             |
| CI_TOP_in      | wire       |             |
| CI_in          | wire       |             |
| DI_in          | wire [7:0] |             |
| S_in           | wire [7:0] |             |
| CO_fb          | wire [7:0] |             |
## Constants

| Name                  | Type | Value    | Description                        |
| --------------------- | ---- | -------- | ---------------------------------- |
| MODULE_NAME           |      | "CARRY8" | define constants                   |
| CARRY_TYPE_DUAL_CY4   |      | 1        | Parameter encodings and registers  |
| CARRY_TYPE_SINGLE_CY8 |      | 0        |                                    |
## Processes
- unnamed: ( @(trig_attr) )
- unnamed: ( @ (trig_attr) )
