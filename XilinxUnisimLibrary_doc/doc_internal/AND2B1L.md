# Entity: AND2B1L

## Diagram

![Diagram](AND2B1L.svg "Diagram")
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
 /___/  \  /    Vendor : Xilinx
 \   \   \/     Version : 2018.1
  \   \         Description : Xilinx Unified Simulation Library Component
  /   /                        Two input AND gate implemented in place of a CLB Latch
 /___/   /\     Filename : AND2B1L.v
 \   \  /  \
  \___\/\___\
  Revision:
    04/01/08 - Initial version.
    04/14/09 - 517897 - Invert SRI not DI
    12/13/11 - 524859 - Added `celldefine and `endcelldefine
    04/16/13 - 683925 - add invertible pin support.
  End Revision:
 
## Generics

| Generic name    | Type  | Value      | Description |
| --------------- | ----- | ---------- | ----------- |
| XIL_TIMING      |       | "UNPLACED" |             |
| IS_SRI_INVERTED | [0:0] | 1'b0       |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| DI        | input     |      |             |
| SRI       | input     |      |             |
## Signals

| Name                | Type      | Description |
| ------------------- | --------- | ----------- |
| trig_attr           | reg       |             |
| IS_SRI_INVERTED_REG | reg [0:0] |             |
| glblGSR             | tri0      |             |
| glblGSR             | tri0      |             |
| DI_in               | wire      |             |
| SRI_in              | wire      |             |
| notifier            | reg       |             |
## Constants

| Name        | Type | Value     | Description       |
| ----------- | ---- | --------- | ----------------- |
| MODULE_NAME |      | "AND2B1L" | define constants  |
