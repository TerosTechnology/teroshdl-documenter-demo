# Entity: misc_FrequencyMeasurement

- **File**: misc_FrequencyMeasurement.vhdl
## Diagram

![Diagram](misc_FrequencyMeasurement.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Patrick Lehmann

 Entity:					measures a input frequency relativ to a reference frequency

 Description:
 -------------------------------------
 This module counts 1 second in a reference timer at reference clock. This
 reference time is used to start and stop a timer at input clock. The counter
 value is the measured frequency in Hz.

 License:
 =============================================================================
 Copyright 2007-2015 Technische Universitaet Dresden - Germany
										 Chair of VLSI-Design, Diagnostics and Architecture

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name         | Type | Value   | Description |
| -------------------- | ---- | ------- | ----------- |
| REFERENCE_CLOCK_FREQ | FREQ | 100 MHz |             |
## Ports

| Port name       | Direction | Type      | Description |
| --------------- | --------- | --------- | ----------- |
| Reference_Clock | in        | std_logic |             |
| Input_Clock     | in        | std_logic |             |
| Start           | in        | std_logic |             |
| Done            | out       | std_logic |             |
| Result          | out       | T_SLV_32  |             |
## Signals

| Name                   | Type                                   | Description |
| ---------------------- | -------------------------------------- | ----------- |
| TimeBase_Counter_rst   | std_logic                              |             |
| TimeBase_Counter_s     | signed(TIMEBASE_COUNTER_BITS downto 0) |             |
| TimeBase_Counter_nxt   | signed(TIMEBASE_COUNTER_BITS downto 0) |             |
| TimeBase_Counter_uf    | std_logic                              |             |
| Stop                   | std_logic                              |             |
| sync_Start             | std_logic                              |             |
| sync_Stop              | std_logic                              |             |
| sync1_Busy             | T_SLV_2                                |             |
| Frequency_Counter_en_r | std_logic                              |             |
| Frequency_Counter_us   | unsigned(31 downto 0)                  |             |
| CaptureResult          | std_logic                              |             |
| CaptureResult_d        | std_logic                              |             |
| Result_en              | std_logic                              |             |
| Result_d               | T_SLV_32                               |             |
| Done_r                 | std_logic                              |             |
## Constants

| Name                  | Type     | Value                                                                                                                                                                            | Description |
| --------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TIMEBASE_COUNTER_MAX  | positive |  TimingToCycles(ite(SIMULATION,<br><span style="padding-left:20px"> 10 us,<br><span style="padding-left:20px"> 1 sec),<br><span style="padding-left:20px"> REFERENCE_CLOCK_FREQ) |             |
| TIMEBASE_COUNTER_BITS | positive |  log2ceilnz(TIMEBASE_COUNTER_MAX)                                                                                                                                                |             |
## Processes
- unnamed: ( Reference_Clock )
- unnamed: ( Input_Clock )
- unnamed: ( Reference_Clock )
**Description**
 Result_d can becaptured from Frequency_Counter_us, because it's stable  for more than one clock cycle and will not change until the next Start 
## Instantiations

- sync1: poc.sync_Strobe
