# Entity: OBUFT

## Diagram

![Diagram](OBUFT.svg "Diagram")
## Description

   Copyright (c) 1995/2009 Xilinx, Inc.
 
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
  /   /                  3-State Output Buffer
 /___/   /\     Filename : OBUFT.v
 \   \  /  \    Timestamp : Thu Mar 25 16:43:01 PST 2004
  \___\/\___\
 Revision:
    03/23/04 - Initial version.
    02/22/06 - CR#226003 - Added integer, real parameter type
    05/23/07 - Changed timescale to 1 ps / 1 ps.
    05/23/07 - Added wire declaration for internal signals.
 
## Generics

| Generic name | Type    | Value       | Description |
| ------------ | ------- | ----------- | ----------- |
| CAPACITANCE  |         | "DONT_CARE" |             |
| DRIVE        | integer | 12          |             |
| IOSTANDARD   |         | "DEFAULT"   |             |
| LOC          |         | " UNPLACED" |             |
| SLEW         |         | "SLOW"      |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| I         | input     |      |             |
|  T        | input     |      |             |
## Signals

| Name | Type | Description |
| ---- | ---- | ----------- |
| ts   | wire |             |
| GTS  | tri0 |             |
