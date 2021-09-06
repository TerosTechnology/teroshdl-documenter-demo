# Entity: io_Debounce

- **File**: io_Debounce.vhdl
## Diagram

![Diagram](io_Debounce.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann
									Thomas B. Preusser

 Entity:				 	Debounce module for BITS many bouncing input pins.

 Description:
 -------------------------------------
 This module debounces several input pins preventing input changes
 following a previous one within the configured ``BOUNCE_TIME`` to pass.
 Internally, the forwarded state is locked for, at least, this ``BOUNCE_TIME``.
 As the backing timer is restarted on every input fluctuation, the next
 passing input update must have seen a stabilized input.

 The parameter ``COMMON_LOCK`` uses a single internal timer for all processed
 inputs. Thus, all inputs must stabilize before any one may pass changed.
 This option is usually fully acceptable for user inputs such as push buttons.

 The parameter ``ADD_INPUT_SYNCHRONIZERS`` triggers the optional instantiation
 of a two-FF input synchronizer on each input bit.

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

| Generic name            | Type             | Value       | Description              |
| ----------------------- | ---------------- | ----------- | ------------------------ |
| CLOCK_FREQ              | FREQ             |             |                          |
| BOUNCE_TIME             | time             |             |                          |
| BITS                    | positive         | 1           |                          |
| INIT                    | std_logic_vector | x"00000000" |  initial state of Output |
| ADD_INPUT_SYNCHRONIZERS | boolean          | true        |                          |
| COMMON_LOCK             | boolean          | false       |                          |
## Ports

| Port name | Direction | Type                              | Description |
| --------- | --------- | --------------------------------- | ----------- |
| Clock     | in        | std_logic                         |             |
| Reset     | in        | std_logic                         |             |
| Input     | in        | std_logic_vector(BITS-1 downto 0) |             |
| Output    | out       | std_logic_vector(BITS-1 downto 0) |             |
## Signals

| Name   | Type                          | Description   |
| ------ | ----------------------------- | ------------- |
| sync   | std_logic_vector(Input'range) |  Synchronized |
| prev   | std_logic_vector(Input'range) |  Delayed      |
| active | std_logic_vector(Input'range) |               |
## Constants

| Name         | Type    | Value                                                                            | Description |
| ------------ | ------- | -------------------------------------------------------------------------------- | ----------- |
| LOCK_COUNT_X | integer |  TimingToCycles(BOUNCE_TIME,<br><span style="padding-left:20px"> CLOCK_FREQ) - 1 |             |
## Processes
- unnamed: ( Clock )
**Description**
---------------------------------------------------------------------------  Bounce Filter 
