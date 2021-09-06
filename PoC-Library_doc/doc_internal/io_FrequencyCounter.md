# Entity: io_FrequencyCounter

- **File**: io_FrequencyCounter.vhdl
## Diagram

![Diagram](io_FrequencyCounter.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	TODO

 Description:
 -------------------------------------
 .. TODO:: No documentation available.

 License:
 =============================================================================
 Copyright 2007-2014 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value   | Description |
| ------------ | -------- | ------- | ----------- |
| CLOCK_FREQ   | FREQ     | 100 MHz |             |
| TIMEBASE     | time     | 1 sec   |             |
| RESOLUTION   | positive | 8       |             |
## Ports

| Port name | Direction | Type                                      | Description |
| --------- | --------- | ----------------------------------------- | ----------- |
| Clock     | in        | std_logic                                 |             |
| Reset     | in        | std_logic                                 |             |
| FreqIn    | in        | std_logic                                 |             |
| FreqOut   | out       | std_logic_vector(RESOLUTION - 1 downto 0) |             |
## Signals

| Name                | Type                                        | Description |
| ------------------- | ------------------------------------------- | ----------- |
| TimeBaseCounter_us  | unsigned(TIMEBASECOUNTER_BITS - 1 downto 0) |             |
| TimeBaseCounter_ov  | std_logic                                   |             |
| FrequencyCounter_us | unsigned(FREQUENCYCOUNTER_BITS downto 0)    |             |
| FrequencyCounter_ov | std_logic                                   |             |
| FreqIn_d            | std_logic                                   |             |
| FreqIn_re           | std_logic                                   |             |
| FreqOut_d           | std_logic_vector(RESOLUTION - 1 downto 0)   |             |
## Constants

| Name                  | Type     | Value                                                                     | Description |
| --------------------- | -------- | ------------------------------------------------------------------------- | ----------- |
| TIMEBASECOUNTER_MAX   | positive |  TimingToCycles(TIMEBASE,<br><span style="padding-left:20px"> CLOCK_FREQ) |             |
| TIMEBASECOUNTER_BITS  | positive |  log2ceilnz(TIMEBASECOUNTER_MAX)                                          |             |
| REQUENCYCOUNTER_MAX   | positive |  2**RESOLUTION                                                            |             |
| FREQUENCYCOUNTER_BITS | positive |  RESOLUTION                                                               |             |
## Processes
- unnamed: ( Clock )
</br>**Description**
 timebase counter 
- unnamed: ( Clock )
</br>**Description**
 frequency counter 
- unnamed: ( Clock )
</br>**Description**
 hold counter value until next TimeBaseCounter event 
