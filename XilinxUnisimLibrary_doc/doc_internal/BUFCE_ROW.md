# Entity: BUFCE_ROW

## Diagram

![Diagram](BUFCE_ROW.svg "Diagram")
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
  /   /                        Clock Buffer
 /___/   /\      Filename    : BUFCE_ROW.v
 \   \  /  \
  \___\/\___\
  Revision:
    05/15/12 - Initial version.
    02/04/14 - update specify block
    10/22/14 - 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name   | Type  | Value      | Description |
| -------------- | ----- | ---------- | ----------- |
| XIL_TIMING     |       | "UNPLACED" |             |
| CE_TYPE        |       | "SYNC"     |             |
| IS_CE_INVERTED | [0:0] | 1'b0       |             |
| IS_I_INVERTED  | [0:0] | 1'b0       |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| CE        | input     |      |             |
| I         | input     |      |             |
## Signals

| Name               | Type       | Description             |
| ------------------ | ---------- | ----------------------- |
| trig_attr          | reg        |                         |
| CE_TYPE_REG        | reg [64:1] |                         |
| IS_CE_INVERTED_REG | reg [0:0]  |                         |
| IS_I_INVERTED_REG  | reg [0:0]  |                         |
| CE_TYPE_BIN        | wire [1:0] |                         |
| CE_TYPE_BIN        | reg [1:0]  |                         |
| glblGSR            | reg        |                         |
| glblGSR            | tri0       |                         |
| CE_in              | wire       |                         |
| I_in               | wire       |                         |
| CE_delay           | wire       |                         |
| I_delay            | wire       |                         |
| attr_test          | reg        |                         |
| attr_err           | reg        |                         |
| notifier           | reg        |                         |
| enable_clk         | reg        | begin behavioral model  |
| i_en_n             | wire       |                         |
| i_en_p             | wire       |                         |
## Constants

| Name             | Type | Value       | Description                        |
| ---------------- | ---- | ----------- | ---------------------------------- |
| MODULE_NAME      |      | "BUFCE_ROW" | define constants                   |
| CE_TYPE_ASYNC    |      | 1           | Parameter encodings and registers  |
| CE_TYPE_HARDSYNC |      | 2           |                                    |
| CE_TYPE_SYNC     |      | 0           |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (trig_attr) )
- unnamed: ( @(I_in or CE_in or glblGSR) )
