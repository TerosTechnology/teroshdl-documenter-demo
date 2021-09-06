# Entity: ocram_sp

- **File**: ocram_sp.vhdl
## Diagram

![Diagram](ocram_sp.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Martin Zabel
									Patrick Lehmann

 Entity:				 	Single-port memory.

 Description:
 -------------------------------------
 Inferring / instantiating single port memory, with:

 * single clock, clock enable,
 * 1 read/write port.

 Command Truth Table:

 == == ================
 ce we Command
 == == ================
 0  X  No operation
 1  0  Read from memory
 1  1  Write to memory
 == == ================

 Both reading and writing are synchronous to the rising-edge of the clock.
 Thus, when reading, the memory data will be outputted after the
 clock edge, i.e, in the following clock cycle.

 When writing data, the read output will output the new data (in the
 following clock cycle) which is aka. "write-first behavior". This behavior
 also applies to Altera M20K memory blocks as described in the Altera:
 "Stratix 5 Device Handbook" (S5-5V1). The documentation in the Altera:
 "Embedded Memory User Guide" (UG-01068) is wrong.

 License:
 =============================================================================
 Copyright 2008-2015 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value | Description                       |
| ------------ | -------- | ----- | --------------------------------- |
| A_BITS       | positive |       |  number of address bits           |
| D_BITS       | positive |       |  number of data bits              |
| FILENAME     | string   | ""    |  file-name for RAM initialization |
## Ports

| Port name | Direction | Type                                | Description   |
| --------- | --------- | ----------------------------------- | ------------- |
| clk       | in        | std_logic                           |  clock        |
| ce        | in        | std_logic                           |  clock enable |
| we        | in        | std_logic                           |  write enable |
| a         | in        | unsigned(A_BITS-1 downto 0)         |  address      |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) |  write data   |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) |  read output  |
## Constants

| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
