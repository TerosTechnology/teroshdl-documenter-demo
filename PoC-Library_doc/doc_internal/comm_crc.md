# Entity: comm_crc

- **File**: comm_crc.vhdl
## Diagram

![Diagram](comm_crc.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					Computes the Cyclic Redundancy Check (CRC)
Description:
-------------------------------------
Computes the Cyclic Redundancy Check (CRC) for a data packet as remainder
of the polynomial division of the message by the given generator
polynomial (GEN).
The computation is unrolled so as to process an arbitrary number of
message bits per step. The generated CRC is independent from the chosen
processing width.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
## Generics

| Generic name | Type             | Value | Description                                |
| ------------ | ---------------- | ----- | ------------------------------------------ |
| GEN          | bit_vector       |       | Generator Polynomial                       |
| BITS         | positive         |       | Number of Bits to be processed in parallel |
| STARTUP_RMD  | std_logic_vector | "0"   |                                            |
| OUTPUT_REGS  | boolean          | true  |                                            |
## Ports

| Port name | Direction | Type                                                      | Description                    |
| --------- | --------- | --------------------------------------------------------- | ------------------------------ |
| clk       | in        | std_logic                                                 | Clock                          |
| set       | in        | std_logic                                                 | Parallel Preload of Remainder  |
| init      | in        | std_logic_vector(abs(mssb_idx(GEN)-GEN'right)-1 downto 0) |                                |
| step      | in        | std_logic                                                 | Process Input Data (MSB first) |
| din       | in        | std_logic_vector(BITS-1 downto 0)                         |                                |
| rmd       | out       | std_logic_vector(abs(mssb_idx(GEN)-GEN'right)-1 downto 0) | Remainder                      |
| zero      | out       | std_logic                                                 | Remainder is Zero              |
## Signals

| Name | Type                       | Description |
| ---- | -------------------------- | ----------- |
| lfsr | std_logic_vector(GN'range) | LFSR Value  |
| lfsn | std_logic_vector(GN'range) | Next Value  |
| lfso | std_logic_vector(GN'range) |             |
## Constants

| Name | Type             | Value                              | Description          |
| ---- | ---------------- | ---------------------------------- | -------------------- |
| GN   | std_logic_vector |  to_stdlogicvector(normalize(GEN)) | Normalized Generator |
## Functions
- normalize <font id="function_arguments">(G : bit_vector) </font> <font id="function_return">return bit_vector </font>
## Processes
- unnamed: ( lfsr, din )
- unnamed: ( clk )
**Description**
Remainder Register

