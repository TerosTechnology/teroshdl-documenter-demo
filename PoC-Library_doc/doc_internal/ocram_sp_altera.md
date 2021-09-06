# Entity: ocram_sp_altera

- **File**: ocram_sp_altera.vhdl
## Diagram

![Diagram](ocram_sp_altera.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Martin Zabel
									Patrick Lehmann

 Entity:				 	Instantiate single-port memory on Altera FPGAs.

 Description:
 -------------------------------------
 Quartus synthesis does not infer this RAM type correctly.
 Instead, altsyncram is instantiated directly.

 For further documentation see module "ocram_sp"
 (src/mem/ocram/ocram_sp.vhdl).

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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| A_BITS       | positive |       |             |
| D_BITS       | positive |       |             |
| FILENAME     | string   | ""    |             |
## Ports

| Port name | Direction | Type                                | Description |
| --------- | --------- | ----------------------------------- | ----------- |
| clk       | in        | std_logic                           |             |
| ce        | in        | std_logic                           |             |
| we        | in        | std_logic                           |             |
| a         | in        | unsigned(A_BITS-1 downto 0)         |             |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) |             |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) |             |
## Signals

| Name | Type                                | Description |
| ---- | ----------------------------------- | ----------- |
| a_sl | std_logic_vector(A_BITS-1 downto 0) |             |
## Constants

| Name      | Type     | Value                                                                                                                        | Description |
| --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DEPTH     | positive |  2**A_BITS                                                                                                                   |             |
| INIT_FILE | string   |  ite((str_length(FILENAME) = 0),<br><span style="padding-left:20px"> "UNUSED",<br><span style="padding-left:20px"> FILENAME) |             |
## Instantiations

- mem: altsyncram
