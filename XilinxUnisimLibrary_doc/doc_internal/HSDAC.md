# Entity: HSDAC

## Diagram

![Diagram](HSDAC.svg "Diagram")
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
 \   \   \/      Version     : 2018.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        HSDAC
 /___/   /\      Filename    : HSDAC.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name         | Type    | Value             | Description |
| -------------------- | ------- | ----------------- | ----------- |
| XIL_TIMING           |         | "UNPLACED"        |             |
| SIM_DEVICE           |         | "ULTRASCALE_PLUS" |             |
| XPA_CFG0             | integer | 0                 |             |
| XPA_CFG1             | integer | 0                 |             |
| XPA_NUM_DACS         | integer | 0                 |             |
| XPA_NUM_DUCS         | integer | 0                 |             |
| XPA_PLL_USED         |         | "No"              |             |
| XPA_SAMPLE_RATE_MSPS | integer | 0                 |             |
## Ports

| Port name        | Direction | Type    | Description |
| ---------------- | --------- | ------- | ----------- |
| CLK_DAC          | output    |         |             |
| DOUT             | output    | [15:0]  |             |
| DRDY             | output    |         |             |
| PLL_DMON_OUT     | output    |         |             |
| PLL_REFCLK_OUT   | output    |         |             |
| STATUS_COMMON    | output    | [15:0]  |             |
| STATUS_DAC0      | output    | [15:0]  |             |
| STATUS_DAC1      | output    | [15:0]  |             |
| STATUS_DAC2      | output    | [15:0]  |             |
| STATUS_DAC3      | output    | [15:0]  |             |
| SYSREF_OUT_NORTH | output    |         |             |
| SYSREF_OUT_SOUTH | output    |         |             |
| VOUT0_N          | output    |         |             |
| VOUT0_P          | output    |         |             |
| VOUT1_N          | output    |         |             |
| VOUT1_P          | output    |         |             |
| VOUT2_N          | output    |         |             |
| VOUT2_P          | output    |         |             |
| VOUT3_N          | output    |         |             |
| VOUT3_P          | output    |         |             |
| CLK_FIFO_LM      | input     |         |             |
| CONTROL_COMMON   | input     | [15:0]  |             |
| CONTROL_DAC0     | input     | [15:0]  |             |
| CONTROL_DAC1     | input     | [15:0]  |             |
| CONTROL_DAC2     | input     | [15:0]  |             |
| CONTROL_DAC3     | input     | [15:0]  |             |
| DAC_CLK_N        | input     |         |             |
| DAC_CLK_P        | input     |         |             |
| DADDR            | input     | [11:0]  |             |
| DATA_DAC0        | input     | [255:0] |             |
| DATA_DAC1        | input     | [255:0] |             |
| DATA_DAC2        | input     | [255:0] |             |
| DATA_DAC3        | input     | [255:0] |             |
| DCLK             | input     |         |             |
| DEN              | input     |         |             |
| DI               | input     | [15:0]  |             |
| DWE              | input     |         |             |
| FABRIC_CLK       | input     |         |             |
| PLL_MONCLK       | input     |         |             |
| PLL_REFCLK_IN    | input     |         |             |
| SYSREF_IN_NORTH  | input     |         |             |
| SYSREF_IN_SOUTH  | input     |         |             |
| SYSREF_N         | input     |         |             |
| SYSREF_P         | input     |         |             |
## Signals

| Name                  | Type         | Description |
| --------------------- | ------------ | ----------- |
| trig_attr             | reg          |             |
| attr_test             | reg          |             |
| attr_test             | reg          |             |
| attr_err              | reg          |             |
| glblGSR               | tri0         |             |
| CLK_DAC_SPARE_out     | wire         |             |
| CLK_DAC_out           | wire         |             |
| DRDY_out              | wire         |             |
| PLL_DMON_OUT_out      | wire         |             |
| PLL_REFCLK_OUT_out    | wire         |             |
| SYSREF_OUT_NORTH_out  | wire         |             |
| SYSREF_OUT_SOUTH_out  | wire         |             |
| VOUT0_N_out           | wire         |             |
| VOUT0_P_out           | wire         |             |
| VOUT1_N_out           | wire         |             |
| VOUT1_P_out           | wire         |             |
| VOUT2_N_out           | wire         |             |
| VOUT2_P_out           | wire         |             |
| VOUT3_N_out           | wire         |             |
| VOUT3_P_out           | wire         |             |
| DOUT_out              | wire [15:0]  |             |
| STATUS_COMMON_out     | wire [15:0]  |             |
| STATUS_DAC0_out       | wire [15:0]  |             |
| STATUS_DAC1_out       | wire [15:0]  |             |
| STATUS_DAC2_out       | wire [15:0]  |             |
| STATUS_DAC3_out       | wire [15:0]  |             |
| TEST_STATUS_out       | wire [15:0]  |             |
| PLL_SCAN_OUT_B_FD_out | wire [1:0]   |             |
| TEST_SO_out           | wire [299:0] |             |
| CLK_FIFO_LM_in        | wire         |             |
| DAC_CLK_N_in          | wire         |             |
| DAC_CLK_P_in          | wire         |             |
| DCLK_in               | wire         |             |
| DEN_in                | wire         |             |
| DWE_in                | wire         |             |
| FABRIC_CLK_in         | wire         |             |
| PLL_MONCLK_in         | wire         |             |
| PLL_REFCLK_IN_in      | wire         |             |
| PLL_SCAN_EN_B_FD_in   | wire         |             |
| PLL_SCAN_MODE_B_FD_in | wire         |             |
| PLL_SCAN_RST_EN_FD_in | wire         |             |
| SYSREF_IN_NORTH_in    | wire         |             |
| SYSREF_IN_SOUTH_in    | wire         |             |
| SYSREF_N_in           | wire         |             |
| SYSREF_P_in           | wire         |             |
| TEST_SCAN_MODE_B_in   | wire         |             |
| TEST_SCAN_RESET_in    | wire         |             |
| TEST_SE_B_in          | wire         |             |
| DADDR_in              | wire [11:0]  |             |
| CONTROL_COMMON_in     | wire [15:0]  |             |
| CONTROL_DAC0_in       | wire [15:0]  |             |
| CONTROL_DAC1_in       | wire [15:0]  |             |
| CONTROL_DAC2_in       | wire [15:0]  |             |
| CONTROL_DAC3_in       | wire [15:0]  |             |
| DI_in                 | wire [15:0]  |             |
| TEST_SCAN_CTRL_in     | wire [15:0]  |             |
| PLL_SCAN_CLK_FD_in    | wire [1:0]   |             |
| PLL_SCAN_IN_FD_in     | wire [1:0]   |             |
| DATA_DAC0_in          | wire [255:0] |             |
| DATA_DAC1_in          | wire [255:0] |             |
| DATA_DAC2_in          | wire [255:0] |             |
| DATA_DAC3_in          | wire [255:0] |             |
| TEST_SI_in            | wire [299:0] |             |
| TEST_SCAN_CLK_in      | wire [4:0]   |             |
| DCLK_delay            | wire         |             |
| DEN_delay             | wire         |             |
| DWE_delay             | wire         |             |
| FABRIC_CLK_delay      | wire         |             |
| DADDR_delay           | wire [11:0]  |             |
| CONTROL_COMMON_delay  | wire [15:0]  |             |
| DI_delay              | wire [15:0]  |             |
| VOUT0_N_real          | real         |             |
| VOUT0_P_real          | real         |             |
| VOUT1_N_real          | real         |             |
| VOUT1_P_real          | real         |             |
| VOUT2_N_real          | real         |             |
| VOUT2_P_real          | real         |             |
| VOUT3_N_real          | real         |             |
| VOUT3_P_real          | real         |             |
| notifier              | reg          |             |
## Constants

| Name                     | Type    | Value                | Description       |
| ------------------------ | ------- | -------------------- | ----------------- |
| MODULE_NAME              |         | "HSDAC"              | define constants  |
| SIM_DEVICE_REG           | [152:1] | SIM_DEVICE           |                   |
| XPA_CFG0_REG             | [15:0]  | XPA_CFG0             |                   |
| XPA_CFG1_REG             | [15:0]  | XPA_CFG1             |                   |
| XPA_NUM_DACS_REG         | [2:0]   | XPA_NUM_DACS         |                   |
| XPA_NUM_DUCS_REG         | [2:0]   | XPA_NUM_DUCS         |                   |
| XPA_PLL_USED_REG         | [24:1]  | XPA_PLL_USED         |                   |
| XPA_SAMPLE_RATE_MSPS_REG | [13:0]  | XPA_SAMPLE_RATE_MSPS |                   |
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

- SIP_HSDAC_INST: SIP_HSDAC
**Description**
tie off

