# Entity: io_GlitchFilter

- **File**: io_GlitchFilter.vhdl
## Diagram

![Diagram](io_GlitchFilter.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	Glitch Filter

 Description:
 -------------------------------------
 This module filters glitches on a wire. The high and low spike suppression
 cycle counts can be configured.

 License:
 =============================================================================
 Copyright 2007-2016 Technische Universitaet Dresden - Germany
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
 use			PoC.io.all;
## Generics

| Generic name                  | Type    | Value | Description |
| ----------------------------- | ------- | ----- | ----------- |
| HIGH_SPIKE_SUPPRESSION_CYCLES | natural | 5     |             |
| LOW_SPIKE_SUPPRESSION_CYCLES  | natural | 5     |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| Clock     | in        | std_logic |             |
| Input     | in        | std_logic |             |
| Output    | out       | std_logic |             |
## Signals

| Name       | Type      | Description |
| ---------- | --------- | ----------- |
| State      | std_logic |             |
| NextState  | std_logic |             |
| TC_en      | std_logic |             |
| TC_Load    | std_logic |             |
| TC_Slot    | natural   |             |
| TC_Timeout | std_logic |             |
## Constants

| Name            | Type     | Value                                                                                                                                              | Description    |
| --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| TTID_HIGH_SPIKE | natural  |  0                                                                                                                                                 |                |
| TTID_LOW_SPIKE  | natural  |  1                                                                                                                                                 |                |
| TIMING_TABLE    | T_NATVEC |  ( 		TTID_HIGH_SPIKE			=> HIGH_SPIKE_SUPPRESSION_CYCLES,<br><span style="padding-left:20px"> 		TTID_LOW_SPIKE			=> LOW_SPIKE_SUPPRESSION_CYCLES 	) |  Timing table  |
## Processes
- unnamed: ( Clock )
- unnamed: ( State, Input, TC_Timeout )
## Instantiations

- TC: PoC.io_TimingCounter
