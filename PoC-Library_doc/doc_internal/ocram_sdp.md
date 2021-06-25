# Entity: ocram_sdp
## Diagram
![Diagram](ocram_sdp.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Martin Zabel
Entity:				 	Simple dual-port memory.
Description:
-------------------------------------
Inferring / instantiating simple dual-port memory, with:
* dual clock, clock enable,
* 1 read port plus 1 write port.
Both reading and writing are synchronous to the rising-edge of the clock.
Thus, when reading, the memory data will be outputted after the
clock edge, i.e, in the following clock cycle.
The generalized behavior across Altera and Xilinx FPGAs since
Stratix/Cyclone and Spartan-3/Virtex-5, respectively, is as follows:
Mixed-Port Read-During-Write
  When reading at the write address, the read value will be unknown which is
  aka. "don't care behavior". This applies to all reads (at the same
  address) which are issued during the write-cycle time, which starts at the
  rising-edge of the write clock and (in the worst case) extends until the
  next rising-edge of the write clock.
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
| Port name | Direction | Type                                | Description        |
| --------- | --------- | ----------------------------------- | ------------------ |
| rclk      | in        | std_logic                           | read clock         |
| rce       | in        | std_logic                           | read clock-enable  |
| wclk      | in        | std_logic                           | write clock        |
| wce       | in        | std_logic                           | write clock-enable |
| we        | in        | std_logic                           | write enable       |
| ra        | in        | unsigned(A_BITS-1 downto 0)         | read address       |
| wa        | in        | unsigned(A_BITS-1 downto 0)         | write address      |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) | data in            |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) | data out           |
## Constants
| Name  | Type     | Value      | Description |
| ----- | -------- | ---------- | ----------- |
| DEPTH | positive |  2**A_BITS |             |
