# Entity: IOBUFDS_DIFF_OUT_DCIEN

## Diagram

![Diagram](IOBUFDS_DIFF_OUT_DCIEN.svg "Diagram")
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
  \   \         Description : Xilinx Timing Simulation Library Component
  /   /                  3-State Diffential Signaling I/O Buffer
 /___/   /\     Filename : IOBUFDS_DIFF_OUT_DCIEN.v
 \   \  /  \    Timestamp : Thu Apr 29 14:59:30 PDT 2010
  \___\/\___\
 Revision:
    04/29/10 - Initial version.
    03/28/11 - CR 603466 fix
    06/15/11 - CR 613347 -- made ouput logic_1 when IBUFDISABLE is active
    08/31/11 - CR 623170 -- Tristate powergating support
    09/20/11 - CR 625564 -- Fixed Tristate powergating polarity
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
    10/22/14 - Added #1 to $finish (CR 808642).
 End Revision
 
## Generics

| Generic name    | Type | Value      | Description |
| --------------- | ---- | ---------- | ----------- |
| DIFF_TERM       |      | "FALSE"    |             |
| DQS_BIAS        |      | "FALSE"    |             |
| IBUF_LOW_PWR    |      | "TRUE"     |             |
| IOSTANDARD      |      | "DEFAULT"  |             |
| SIM_DEVICE      |      | "7SERIES"  |             |
| USE_IBUFDISABLE |      | "TRUE"     |             |
| LOC             |      | "UNPLACED" |             |
## Ports

| Port name      | Direction | Type | Description       |
| -------------- | --------- | ---- | ----------------- |
| O              | output    |      | `ifdef XIL_TIMING |
| OB             | output    |      |                   |
| IO             | inout     |      |                   |
| IOB            | inout     |      |                   |
| DCITERMDISABLE | input     |      |                   |
| I              | input     |      |                   |
| IBUFDISABLE    | input     |      |                   |
| TM             | input     |      |                   |
| TS             | input     |      |                   |
## Signals

| Name               | Type | Description |
| ------------------ | ---- | ----------- |
| t1                 | wire |             |
| t2                 | wire |             |
| out_val            | wire |             |
| out_b_val          | wire |             |
| T_OR_IBUFDISABLE_1 | wire |             |
| T_OR_IBUFDISABLE_2 | wire |             |
| GTS                | tri0 |             |
| O_int              | reg  |             |
| OB_int             | reg  |             |
| DQS_BIAS_BINARY    | reg  |             |
## Constants

| Name        | Type | Value                    | Description       |
| ----------- | ---- | ------------------------ | ----------------- |
| MODULE_NAME |      | "IOBUFDS_DIFF_OUT_DCIEN" | define constants  |
## Processes
- unnamed: ( @(IO or IOB or DQS_BIAS_BINARY) )
