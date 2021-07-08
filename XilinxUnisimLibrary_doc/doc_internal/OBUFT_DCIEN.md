# Entity: OBUFT_DCIEN

## Diagram

![Diagram](OBUFT_DCIEN.svg "Diagram")
## Description

   Copyright (c) 1995/2010 Xilinx, Inc.
 
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
  /   /                  3-State Output Buffer
 /___/   /\     Filename : OBUFT_DCIEN.v
 \   \  /  \    Timestamp : Thu Apr 29 14:59:30 PDT 2010
  \___\/\___\
 Revision:
    04/29/10 - Initial version.
    12/20/10 - CR 587760 -- For backend support only, no corresponding unisim 
    09/20/11 - CR 625725 -- Removed attribute CAPACITANCE
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
 End Revision
 
## Generics

| Generic name | Type    | Value      | Description        |
| ------------ | ------- | ---------- | ------------------ |
| DRIVE        | integer | 12         |                    |
| IOSTANDARD   |         | "DEFAULT"  |                    |
| LOC          |         | "UNPLACED" |                    |
| SLEW         |         | "SLOW"     | `ifdef XIL_TIMING  |
## Ports

| Port name      | Direction | Type | Description |
| -------------- | --------- | ---- | ----------- |
| O              | output    |      |             |
| DCITERMDISABLE | input     |      |             |
| I              | input     |      |             |
| T              | input     |      |             |
## Signals

| Name | Type | Description |
| ---- | ---- | ----------- |
| ts   | wire |             |
| GTS  | tri0 |             |
