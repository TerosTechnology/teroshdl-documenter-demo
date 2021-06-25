# Entity: ocram_tdp
## Diagram
![Diagram](ocram_tdp.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Martin Zabel
Entity:				 	True dual-port memory.
Description:
-------------------------------------
Inferring / instantiating true dual-port memory, with:
* dual clock, clock enable,
* 2 read/write ports.
Command truth table for port 1, same applies to port 2:
=== === ================
ce1 we1 Command
=== === ================
0   X   No operation
1   0   Read from memory
1   1   Write to memory
=== === ================
Both reading and writing are synchronous to the rising-edge of the clock.
Thus, when reading, the memory data will be outputted after the
clock edge, i.e, in the following clock cycle.
The generalized behavior across Altera and Xilinx FPGAs since
Stratix/Cyclone and Spartan-3/Virtex-5, respectively, is as follows:
Same-Port Read-During-Write
  When writing data through port 1, the read output of the same port
  (``q1``) will output the new data (``d1``, in the following clock cycle)
  which is aka. "write-first behavior".
  Same applies to port 2.
Mixed-Port Read-During-Write
  When reading at the write address, the read value will be unknown which is
  aka. "don't care behavior". This applies to all reads (at the same
  address) which are issued during the write-cycle time, which starts at the
  rising-edge of the write clock and (in the worst case) extends
  until the next rising-edge of that write clock.
For simulation, always our dedicated simulation model :ref:`IP:ocram_tdp_sim`
is used.
License:
=============================================================================
Copyright 2008-2016 Technische Universitaet Dresden - Germany
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
| Generic name | Type     | Value | Description                      |
| ------------ | -------- | ----- | -------------------------------- |
| A_BITS       | positive |       | number of address bits           |
| D_BITS       | positive |       | number of data bits              |
| FILENAME     | string   | ""    | file-name for RAM initialization |
## Ports
| Port name | Direction | Type                                | Description               |
| --------- | --------- | ----------------------------------- | ------------------------- |
| clk1      | in        | std_logic                           | clock for 1st port        |
| clk2      | in        | std_logic                           | clock for 2nd port        |
| ce1       | in        | std_logic                           | clock-enable for 1st port |
| ce2       | in        | std_logic                           | clock-enable for 2nd port |
| we1       | in        | std_logic                           | write-enable for 1st port |
| we2       | in        | std_logic                           | write-enable for 2nd port |
| a1        | in        | unsigned(A_BITS-1 downto 0)         | address for 1st port      |
| a2        | in        | unsigned(A_BITS-1 downto 0)         | address for 2nd port      |
| d1        | in        | std_logic_vector(D_BITS-1 downto 0) | write-data for 1st port   |
| d2        | in        | std_logic_vector(D_BITS-1 downto 0) | write-data for 2nd port   |
| q1        | out       | std_logic_vector(D_BITS-1 downto 0) | read-data from 1st port   |
| q2        | out       | std_logic_vector(D_BITS-1 downto 0) | read-data from 2nd port   |
## Constants
| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
