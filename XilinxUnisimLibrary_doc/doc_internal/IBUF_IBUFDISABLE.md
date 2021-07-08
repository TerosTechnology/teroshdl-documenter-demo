# Entity: IBUF_IBUFDISABLE

## Diagram

![Diagram](IBUF_IBUFDISABLE.svg "Diagram")
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
  /   /                  Input Buffer
 /___/   /\     Filename : IBUF_IBUFDISABLE.v
 \   \  /  \    Timestamp : Wed Dec  8 17:04:24 PST 2010
  \___\/\___\
 Revision:
    12/08/10 - Initial version.
    04/04/11 - CR 604808 fix
    06/15/11 - CR 613347 -- made ouput logic_1 when IBUFDISABLE is active
    08/31/11 - CR 623170 -- added attribute USE_IBUFDISABLE
    09/20/11 - CR 624774, 625725 -- Removed attributes IBUF_DELAY_VALUE, IFD_DELAY_VALUE and CAPACITANCE
    12/13/11 - Added `celldefine and `endcelldefine (CR 524859).
    10/22/14 - Added #1 to $finish (CR 808642).
 End Revision
 
## Generics

| Generic name    | Type | Value      | Description |
| --------------- | ---- | ---------- | ----------- |
| IBUF_LOW_PWR    |      | "TRUE"     |             |
| IOSTANDARD      |      | "DEFAULT"  |             |
| SIM_DEVICE      |      | "7SERIES"  |             |
| USE_IBUFDISABLE |      | "TRUE"     |             |
| LOC             |      | "UNPLACED" |             |
## Ports

| Port name   | Direction | Type | Description       |
| ----------- | --------- | ---- | ----------------- |
| O           | output    |      | `ifdef XIL_TIMING |
| I           | input     |      |                   |
| IBUFDISABLE | input     |      |                   |
## Signals

| Name    | Type | Description |
| ------- | ---- | ----------- |
| out_val | wire |             |
## Constants

| Name        | Type | Value              | Description       |
| ----------- | ---- | ------------------ | ----------------- |
| MODULE_NAME |      | "IBUF_IBUFDISABLE" | define constants  |
