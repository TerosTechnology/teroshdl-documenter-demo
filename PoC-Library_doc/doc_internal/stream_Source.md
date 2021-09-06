# Entity: stream_Source

- **File**: stream_Source.vhdl
## Diagram

![Diagram](stream_Source.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	A generic buffer module for the PoC.Stream protocol.

 Description:
 -------------------------------------
 .. TODO:: No documentation available.

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
 WITHOUT WARRANTIES OR CONDITIONS of ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name | Type                             | Value | Description |
| ------------ | -------------------------------- | ----- | ----------- |
| TESTCASES    | T_SIM_STREAM_FRAMEGROUP_VECTOR_8 |       |             |
## Ports

| Port name | Direction | Type      | Description       |
| --------- | --------- | --------- | ----------------- |
| Clock     | in        | std_logic |                   |
| Reset     | in        | std_logic |                   |
| Enable    | in        | std_logic | Control interface |
| Out_Valid | out       | std_logic | OUT Port          |
| Out_Data  | out       | T_SLV_8   |                   |
| Out_SOF   | out       | std_logic |                   |
| Out_EOF   | out       | std_logic |                   |
| Out_Ack   | in        | std_logic |                   |
## Signals

| Name                | Type                                                | Description              |
| ------------------- | --------------------------------------------------- | ------------------------ |
| FrameGroupNumber_us | unsigned(log2ceilnz(TESTCASES'length) - 1 downto 0) |  dummy signals for iSIM  |
## Constants

| Name       | Type    | Value      | Description |
| ---------- | ------- | ---------- | ----------- |
| MAX_CYCLES | natural |  10 * 1000 |             |
| MAX_ERRORS | natural | 				50     |             |
## Processes
- unnamed: (  )
