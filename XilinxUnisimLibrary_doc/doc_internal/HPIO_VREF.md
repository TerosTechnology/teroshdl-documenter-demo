# Entity: HPIO_VREF

## Diagram

![Diagram](HPIO_VREF.svg "Diagram")
## Description

    Copyright (c) 2011 Xilinx Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____   ___
  /   /\/   / 
 /___/  \  /     Vendor      : Xilinx 
 \   \   \/      Version     : 2012.2
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        
 /___/   /\      Filename    : HPIO_VREF.v
 \   \  /  \ 
  \___\/\___\                    
                                 
  Revision:
    10/22/14 - Added #1 to $finish (CR 808642).
  End Revision:
 
## Generics

| Generic name | Type | Value      | Description |
| ------------ | ---- | ---------- | ----------- |
| XIL_TIMING   |      | "UNPLACED" |             |
| VREF_CNTR    |      | "OFF"      |             |
## Ports

| Port name        | Direction | Type  | Description |
| ---------------- | --------- | ----- | ----------- |
| VREF             | output    |       |             |
| FABRIC_VREF_TUNE | input     | [6:0] |             |
## Signals

| Name                   | Type       | Description |
| ---------------------- | ---------- | ----------- |
| VREF_CNTR_BIN          | wire [1:0] |             |
| glblGSR                | tri0       |             |
| notifier               | reg        |             |
| trig_attr              | reg        |             |
| attr_test              | reg        |             |
| attr_test              | reg        |             |
| attr_err               | reg        |             |
| VREF_out               | wire       |             |
| VREF_delay             | wire       |             |
| FABRIC_VREF_TUNE_in    | wire [6:0] |             |
| FABRIC_VREF_TUNE_delay | wire [6:0] |             |
## Constants

| Name                    | Type    | Value       | Description                        |
| ----------------------- | ------- | ----------- | ---------------------------------- |
| MODULE_NAME             |         | "HPIO_VREF" | define constants                   |
| in_delay                |         | 0           |                                    |
| out_delay               |         | 0           |                                    |
| inclk_delay             |         | 0           |                                    |
| outclk_delay            |         | 0           |                                    |
| VREF_CNTR_FABRIC_RANGE1 |         | 1           | Parameter encodings and registers  |
| VREF_CNTR_FABRIC_RANGE2 |         | 2           |                                    |
| VREF_CNTR_OFF           |         | 0           |                                    |
| VREF_CNTR_REG           | [104:1] | VREF_CNTR   |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: ( @ (FABRIC_VREF_TUNE_in) )
