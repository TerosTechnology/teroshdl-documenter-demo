# Entity: ddrio_out_xilinx

- **File**: ddrio_out_xilinx.vhdl
## Diagram

![Diagram](ddrio_out_xilinx.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Martin Zabel
									Patrick Lehmann

 Entity:					Instantiates Chip-Specific DDR Output Registers for Xilinx FPGAs.

 Description:
 -------------------------------------
	See PoC.io.ddrio.out for interface description.

 License:
 =============================================================================
 Copyright 2007-2015 Technische Universitaet Dresden - Germany,
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

| Generic name     | Type       | Value       | Description |
| ---------------- | ---------- | ----------- | ----------- |
| NO_OUTPUT_ENABLE | boolean    | false       |             |
| BITS             | positive   |             |             |
| INIT_VALUE       | bit_vector | x"FFFFFFFF" |             |
## Ports

| Port name    | Direction | Type                                | Description |
| ------------ | --------- | ----------------------------------- | ----------- |
| Clock        | in        | std_logic                           |             |
| ClockEnable  | in        | std_logic                           |             |
| OutputEnable | in        | std_logic                           |             |
| DataOut_high | in        | std_logic_vector(BITS - 1 downto 0) |             |
| DataOut_low  | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Pad          | out       | std_logic_vector(BITS - 1 downto 0) |             |
