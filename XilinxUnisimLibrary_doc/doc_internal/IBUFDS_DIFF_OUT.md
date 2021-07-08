# Entity: IBUFDS_DIFF_OUT

## Diagram

![Diagram](IBUFDS_DIFF_OUT.svg "Diagram")
## Description

   Copyright (c) 1995/2004 Xilinx, Inc.
 
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
 \   \   \/     Version : 10.1
  \   \         Description : Xilinx Functional Simulation Library Component
  /   /                  Differential Signaling Input Buffer with Differential Outputs
 /___/   /\     Filename : IBUFDS_DIFF_OUT.v
 \   \  /  \    Timestamp : Thu Mar 25 16:42:23 PST 2004
  \___\/\___\
 Revision:
    03/23/04 - Initial version.
    05/23/07 - Changed timescale to 1 ps / 1 ps.
    05/13/08 - CR 458290 -- Added else condition to handle x case.
    02/10/09 - CR 430124 -- Added attribute DIFF_TERM.
    06/02/09 - CR 523083 -- Added attribute IBUF_LOW_PWR.
    11/03/10 - CR 576577 -- changed default value of IOSTANDARD from LVDS_25 to DEFAULT.
    09/30/11 - CR 626400 -- Added PATHPULSE 
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
    10/22/14 - Added #1 to $finish (CR 808642).
 End Revision
 
## Generics

| Generic name | Type | Value       | Description |
| ------------ | ---- | ----------- | ----------- |
| DIFF_TERM    |      | "FALSE"     |             |
| DQS_BIAS     |      | "FALSE"     |             |
| IBUF_LOW_PWR |      | "TRUE"      |             |
| IOSTANDARD   |      | "DEFAULT"   |             |
| LOC          |      | " UNPLACED" |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| OB        | output    |      |             |
| I         | input     |      |             |
|  IB       | input     |      |             |
## Signals

| Name            | Type | Description |
| --------------- | ---- | ----------- |
| o_out           | reg  |             |
| DQS_BIAS_BINARY | reg  |             |
## Processes
- unnamed: ( @(I or IB or DQS_BIAS_BINARY) )
