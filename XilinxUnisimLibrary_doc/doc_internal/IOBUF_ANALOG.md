# Entity: IOBUF_ANALOG

## Diagram

![Diagram](IOBUF_ANALOG.svg "Diagram")
## Description

    Copyright (c) 1995/2017 Xilinx, Inc.
 
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
 \   \   \/      Version     : 2017.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        Analog Auxiliary SYSMON Input Output Buffer
 /___/   /\      Filename    : IOBUF_ANALOG.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name | Type    | Value      | Description |
| ------------ | ------- | ---------- | ----------- |
| XIL_TIMING   |         | "UNPLACED" |             |
| DRIVE        | integer | 12         |             |
| IBUF_LOW_PWR |         | "TRUE"     |             |
| IOSTANDARD   |         | "DEFAULT"  |             |
| SLEW         |         | "SLOW"     |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| O         | output    |      |             |
| IO        | inout     |      |             |
| I         | input     |      |             |
| T         | input     |      |             |
## Signals

| Name      | Type | Description |
| --------- | ---- | ----------- |
| trig_attr | reg  |             |
| attr_test | reg  |             |
| attr_test | reg  |             |
| attr_err  | reg  |             |
| glblGSR   | tri0 |             |
| I_in      | wire |             |
| T_in      | wire |             |
## Constants

| Name               | Type   | Value          | Description                        |
| ------------------ | ------ | -------------- | ---------------------------------- |
| MODULE_NAME        |        | "IOBUF_ANALOG" | define constants                   |
| IBUF_LOW_PWR_FALSE |        | 1              | Parameter encodings and registers  |
| IBUF_LOW_PWR_TRUE  |        | 0              |                                    |
| IOSTANDARD_DEFAULT |        | 0              |                                    |
| SLEW_FAST          |        | 1              |                                    |
| SLEW_SLOW          |        | 0              |                                    |
| DRIVE_REG          | [4:0]  | DRIVE          |                                    |
| IBUF_LOW_PWR_REG   | [40:1] | IBUF_LOW_PWR   |                                    |
| IOSTANDARD_REG     | [56:1] | IOSTANDARD     |                                    |
| SLEW_REG           | [32:1] | SLEW           |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
