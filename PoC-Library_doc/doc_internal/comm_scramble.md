# Entity: comm_scramble

- **File**: comm_scramble.vhdl
## Diagram

![Diagram](comm_scramble.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Thomas B. Preusser

 Entity:					Computes XOR masks for stream scrambling from an LFSR generator.

 Description:
 -------------------------------------
 The LFSR computation is unrolled to generate an arbitrary number of mask
 bits in parallel. The mask are output in little endian. The generated bit
 sequence is independent from the chosen output width.

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

| Generic name | Type       | Value | Description                                                 |
| ------------ | ---------- | ----- | ----------------------------------------------------------- |
| GEN          | bit_vector |       |  Generator Polynomial (little endian)                       |
| BITS         | positive   |       |  Width of Mask Bits to be computed in parallel in each step |
## Ports

| Port name | Direction | Type                                    | Description                        |
| --------- | --------- | --------------------------------------- | ---------------------------------- |
| clk       | in        | std_logic                               |  Clock                             |
| set       | in        | std_logic                               |  Set LFSR to value provided on din |
| din       | in        | std_logic_vector(GEN'length-2 downto 0) |                                    |
| step      | in        | std_logic                               |  Compute a Mask Output             |
| mask      | out       | std_logic_vector(BITS-1 downto 0)       |                                    |
## Signals

| Name | Type                       | Description  |
| ---- | -------------------------- | ------------ |
| lfsr | std_logic_vector(GN'range) |  LFSR Value  |
## Constants

| Name | Type       | Value           | Description            |
| ---- | ---------- | --------------- | ---------------------- |
| GN   | bit_vector |  normalize(GEN) |  Normalized Generator  |
## Functions
- normalize <font id="function_arguments">(G : bit_vector) </font> <font id="function_return">return bit_vector </font>
## Processes
- unnamed: ( clk )
