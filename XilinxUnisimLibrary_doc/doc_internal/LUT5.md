# Entity: LUT5

## Diagram

![Diagram](LUT5.svg "Diagram")
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
 /___/  \  /    Vendor      : Xilinx
 \   \   \/     Version     : 2017.1
  \   \         Description : Xilinx Unified Simulation Library Component
  /   /                  5-Bit Look-Up Table
 /___/   /\     Filename : LUT5.v
 \   \  /  \
  \___\/\___\
  Revision:
    03/23/04 - Initial version.
    02/04/05 - Replace primitive with function; Remove buf.
    01/07/06 - 222733 - Add LOC Parameter
    06/04/07 - Add wire declaration to internal signal.
    12/13/11 - 524859 - Added `celldefine and `endcelldefine
    09/12/16 - ANSI ports, speed improvements
  End Revision:
 
## Generics

| Generic name | Type   | Value        | Description |
| ------------ | ------ | ------------ | ----------- |
| XIL_TIMING   |        | "UNPLACED"   |             |
| INIT         | [31:0] | 32'h00000000 |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| I0        | input     |      |             |
| I1        | input     |      |             |
| I2        | input     |      |             |
| I3        | input     |      |             |
| I4        | input     |      |             |
## Signals

| Name      | Type       | Description             |
| --------- | ---------- | ----------------------- |
| trig_attr | reg        |                         |
| INIT_REG  | reg [31:0] |                         |
| O_out     | reg        | begin behavioral model  |
## Constants

| Name        | Type | Value  | Description       |
| ----------- | ---- | ------ | ----------------- |
| MODULE_NAME |      | "LUT5" | define constants  |
## Processes
- unnamed: ( @(I0 or I1 or I2 or I3 or I4) )
