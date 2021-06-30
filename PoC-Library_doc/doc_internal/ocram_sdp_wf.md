# Entity: ocram_sdp_wf

## Diagram

![Diagram](ocram_sdp_wf.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:				 	Martin Zabel
Entity:				 	Simple dual-port memory with write-first behavior.
Description:
-------------------------------------
Inferring / instantiating simple dual-port memory, with:
* single clock, clock enable,
* 1 read port plus 1 write port.
Command truth table:
== == ===============================
ce we Command
== == ===============================
0   X   No operation
1   0   Read only from memory
1   1   Read from and Write to memory
== == ===============================
Both reading and writing are synchronous to the rising-edge of the clock.
Thus, when reading, the memory data will be outputted after the
clock edge, i.e, in the following clock cycle.
Mixed-Port Read-During-Write
  When reading at the write address, the read value will be the new data,
  aka. "write-first behavior". Of course, the read is still synchronous,
  i.e, the latency is still one clock cyle.
License:
=============================================================================
Copyright 2008-2015 Technische Universitaet Dresden - Germany
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

| Port name | Direction | Type                                | Description   |
| --------- | --------- | ----------------------------------- | ------------- |
| clk       | in        | std_logic                           | clock         |
| ce        | in        | std_logic                           | clock-enable  |
| we        | in        | std_logic                           | write enable  |
| ra        | in        | unsigned(A_BITS-1 downto 0)         | read address  |
| wa        | in        | unsigned(A_BITS-1 downto 0)         | write address |
| d         | in        | std_logic_vector(D_BITS-1 downto 0) | data in       |
| q         | out       | std_logic_vector(D_BITS-1 downto 0) | data out      |
## Signals

| Name  | Type                      | Description        |
| ----- | ------------------------- | ------------------ |
| wd_r  | std_logic_vector(d'range) | write data         |
| fwd_r | std_logic                 | forward write data |
| ram_q | std_logic_vector(q'range) | RAM output         |
## Functions
- addr_equal <font id="function_arguments">(a1 : unsigned; a2 : unsigned) </font> <font id="function_return">return X01 </font>
**Description**
Compares two addresses, returns 'X' if either ``a1`` or ``a2`` containsmeta-values, otherwise returns '1' if ``a1 == a2`` is true else'0'. Returns 'X' even when the addresses contain '-' values, to signal anundefined outcome.
## Processes
- unnamed: ( clk )
## Instantiations

- ram_sdp: work.ocram_sdp
