# Entity: MMCME4_BASE

## Diagram

![Diagram](MMCME4_BASE.svg "Diagram")
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
  /   /                        Base Mixed Mode Clock Manager (MMCM)
 /___/   /\      Filename    : MMCME4_BASE.v
 \   \  /  \
  \___\/\___\
  Revision:
  10/22/2014 808642 - Added #1 to $finish
  End Revision:
 
## Generics

| Generic name        | Type    | Value       | Description |
| ------------------- | ------- | ----------- | ----------- |
| XIL_TIMING          |         | "UNPLACED"  |             |
| BANDWIDTH           |         | "OPTIMIZED" |             |
| CLKFBOUT_MULT_F     | real    | 5.000       |             |
| CLKFBOUT_PHASE      | real    | 0.000       |             |
| CLKIN1_PERIOD       | real    | 0.000       |             |
| CLKOUT0_DIVIDE_F    | real    | 1.000       |             |
| CLKOUT0_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT0_PHASE       | real    | 0.000       |             |
| CLKOUT1_DIVIDE      | integer | 1           |             |
| CLKOUT1_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT1_PHASE       | real    | 0.000       |             |
| CLKOUT2_DIVIDE      | integer | 1           |             |
| CLKOUT2_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT2_PHASE       | real    | 0.000       |             |
| CLKOUT3_DIVIDE      | integer | 1           |             |
| CLKOUT3_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT3_PHASE       | real    | 0.000       |             |
| CLKOUT4_CASCADE     |         | "FALSE"     |             |
| CLKOUT4_DIVIDE      | integer | 1           |             |
| CLKOUT4_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT4_PHASE       | real    | 0.000       |             |
| CLKOUT5_DIVIDE      | integer | 1           |             |
| CLKOUT5_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT5_PHASE       | real    | 0.000       |             |
| CLKOUT6_DIVIDE      | integer | 1           |             |
| CLKOUT6_DUTY_CYCLE  | real    | 0.500       |             |
| CLKOUT6_PHASE       | real    | 0.000       |             |
| DIVCLK_DIVIDE       | integer | 1           |             |
| IS_CLKFBIN_INVERTED | [0:0]   | 1'b0        |             |
| IS_CLKIN1_INVERTED  | [0:0]   | 1'b0        |             |
| IS_PWRDWN_INVERTED  | [0:0]   | 1'b0        |             |
| IS_RST_INVERTED     | [0:0]   | 1'b0        |             |
| REF_JITTER1         | real    | 0.010       |             |
| STARTUP_WAIT        |         | "FALSE"     |             |
## Ports

| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| CLKFBOUT  | output    |      |             |
| CLKFBOUTB | output    |      |             |
| CLKOUT0   | output    |      |             |
| CLKOUT0B  | output    |      |             |
| CLKOUT1   | output    |      |             |
| CLKOUT1B  | output    |      |             |
| CLKOUT2   | output    |      |             |
| CLKOUT2B  | output    |      |             |
| CLKOUT3   | output    |      |             |
| CLKOUT3B  | output    |      |             |
| CLKOUT4   | output    |      |             |
| CLKOUT5   | output    |      |             |
| CLKOUT6   | output    |      |             |
| LOCKED    | output    |      |             |
| CLKFBIN   | input     |      |             |
| CLKIN1    | input     |      |             |
| PWRDWN    | input     |      |             |
| RST       | input     |      |             |
## Signals

| Name         | Type        | Description |
| ------------ | ----------- | ----------- |
| trig_attr    | reg         |             |
| attr_test    | reg         |             |
| attr_test    | reg         |             |
| attr_err     | reg         |             |
| CLKFBIN_in   | wire        |             |
| CLKIN1_in    | wire        |             |
| PWRDWN_in    | wire        |             |
| RST_in       | wire        |             |
| CDDCDONE     | wire        |             |
| DRDY         | wire        |             |
| PSDONE       | wire        |             |
| CLKFBSTOPPED | wire        |             |
| CLKINSTOPPED | wire        |             |
| DO           | wire [15:0] |             |
| notifier     | reg         |             |
## Constants

| Name                    | Type  | Value               | Description       |
| ----------------------- | ----- | ------------------- | ----------------- |
| MODULE_NAME             |       | "MMCME4_BASE"       | define constants  |
| IS_CLKFBIN_INVERTED_REG | [0:0] | IS_CLKFBIN_INVERTED |                   |
| IS_CLKIN1_INVERTED_REG  | [0:0] | IS_CLKIN1_INVERTED  |                   |
| IS_PWRDWN_INVERTED_REG  | [0:0] | IS_PWRDWN_INVERTED  |                   |
| IS_RST_INVERTED_REG     | [0:0] | IS_RST_INVERTED     |                   |
## Processes
- unnamed: ( @ (trig_attr) )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
- unnamed: (  )
## Instantiations

- mmcm_adv_1: MMCME4_ADV
