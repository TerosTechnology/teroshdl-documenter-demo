# Entity: ocram_tdp_wf

- **File**: ocram_tdp_wf.vhdl
## Diagram

![Diagram](ocram_tdp_wf.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Martin Zabel
									Patrick Lehmann

 Entity:				 	True dual-port memory with write-first behavior.

 Description:
 -------------------------------------
 Inferring / instantiating true dual-port memory, with:

 * single clock, clock enable,
 * 2 read/write ports.

 Command truth table:

 == === === =====================================================
 ce we1 we2 Command
 == === === =====================================================
 0   X   X  No operation
 1   0   0  Read only from memory
 1   0   1  Read from memory on port 1, write to memory on port 2
 1   1   0  Write to memory on port 1, read from memory on port 2
 1   1   1  Write to memory on both ports
 == === === =====================================================

 Both reads and writes are synchronous to the clock.

 The generalized behavior across Altera and Xilinx FPGAs since
 Stratix/Cyclone and Spartan-3/Virtex-5, respectively, is as follows:

 Same-Port Read-During-Write
   When writing data through port 1, the read output of the same port
   (``q1``) will output the new data (``d1``, in the following clock cycle)
   which is aka. "write-first behavior".

   Same applies to port 2.

 Mixed-Port Read-During-Write
   When reading at the write address, the read value will be the new data,
   aka. "write-first behavior". Of course, the read is still synchronous,
   i.e, the latency is still one clock cyle.

 If a write is issued on both ports to the same address, then the output of
 this unit and the content of the addressed memory cell are undefined.

 For simulation, always our dedicated simulation model :ref:`IP:ocram_tdp_sim`
 is used.

 License:
 =============================================================================
 Copyright 2008-2016 Technische Universitaet Dresden - Germany
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

| Port name | Direction | Type                                | Description                |
| --------- | --------- | ----------------------------------- | -------------------------- |
| clk       | in        | std_logic                           |  clock                     |
| ce        | in        | std_logic                           |  clock-enable              |
| we1       | in        | std_logic                           |  write-enable for 1st port |
| we2       | in        | std_logic                           |  write-enable for 2nd port |
| a1        | in        | unsigned(A_BITS-1 downto 0)         |  address for 1st port      |
| a2        | in        | unsigned(A_BITS-1 downto 0)         |  address for 2nd port      |
| d1        | in        | std_logic_vector(D_BITS-1 downto 0) |  write-data for 1st port   |
| d2        | in        | std_logic_vector(D_BITS-1 downto 0) |  write-data for 2nd port   |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) |  read-data from 1st port   |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) |  read-data from 2nd port   |
## Signals

| Name   | Type                       | Description                               |
| ------ | -------------------------- | ----------------------------------------- |
| wd1_r  | std_logic_vector(d1'range) |  write data from port 1                   |
| wd2_r  | std_logic_vector(d2'range) |  write data from port 2                   |
| fwd1_r | std_logic                  |  forward write data from port 1 to port 2 |
| fwd2_r | std_logic                  |  forward write data from port 2 to port 1 |
| ram_q1 | std_logic_vector(q1'range) |  RAM output, port 1                       |
| ram_q2 | std_logic_vector(q2'range) |  RAM output, port 2                       |
## Functions
- addr_equal <font id="function_arguments">(a1 : unsigned;<br><span style="padding-left:20px"> a2 : unsigned) </font> <font id="function_return">return X01 </font>
**Description**
 Compares two addresses, returns 'X' if either ``a1`` or ``a2`` contains
 meta-values, otherwise returns '1' if ``a1 == a2`` is true else
 '0'. Returns 'X' even when the addresses contain '-' values, to signal an
 undefined outcome.

## Processes
- unnamed: ( clk )
## Instantiations

- ram_tdp: work.ocram_tdp
