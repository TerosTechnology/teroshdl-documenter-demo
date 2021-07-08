# Entity: IBUFDS_INTERMDISABLE_INT

## Diagram

![Diagram](IBUFDS_INTERMDISABLE_INT.svg "Diagram")
## Description

   Copyright (c) 1995/2011 Xilinx, Inc.
 
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
 /___/  \  /    Vendor : Xilinx
 \   \   \/     Version : 13.1
  \   \         Description : Xilinx Unified Simulation Library Component
  /   /                  Differential Signaling Input Buffer
 /___/   /\     Filename : IBUFDS_INTERMDISABLE_INT.v
 \   \  /  \
  \___\/\___\
 Revision:
    11/09/11 - Initial -- added due to CR 631983 fix - for timing netlist only
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
    07/10/12 - 669215 - add parameter DQS_BIAS
    08/29/12 - 675511 - add DQS_BIAS functionality
    09/11/12 - 677753 - remove X glitch on O
    10/22/14 - Added #1 to $finish (CR 808642).
 End Revision
 
## Generics

| Generic name    | Type | Value      | Description        |
| --------------- | ---- | ---------- | ------------------ |
| LOC             |      | "UNPLACED" |                    |
| DIFF_TERM       |      | "FALSE"    | `ifdef XIL_TIMING  |
| DQS_BIAS        |      | "FALSE"    |                    |
| IBUF_LOW_PWR    |      | "TRUE"     |                    |
| IOSTANDARD      |      | "DEFAULT"  |                    |
| USE_IBUFDISABLE |      | "TRUE"     |                    |
## Ports

| Port name     | Direction | Type | Description |
| ------------- | --------- | ---- | ----------- |
| O             | output    |      |             |
| I             | input     |      |             |
| IB            | input     |      |             |
| IBUFDISABLE   | input     |      |             |
| INTERMDISABLE | input     |      |             |
## Signals

| Name                   | Type | Description |
| ---------------------- | ---- | ----------- |
| i_in                   | wire |             |
| ib_in                  | wire |             |
| ibufdisable_in         | wire |             |
| intermdisable_in       | wire |             |
| o_out                  | reg  |             |
| DQS_BIAS_BINARY        | reg  |             |
| USE_IBUFDISABLE_BINARY | reg  |             |
## Constants

| Name        | Type | Value                      | Description |
| ----------- | ---- | -------------------------- | ----------- |
| MODULE_NAME |      | "IBUFDS_INTERMDISABLE_INT" |             |
## Processes
- unnamed: ( @(i_in or ib_in or DQS_BIAS_BINARY) )
