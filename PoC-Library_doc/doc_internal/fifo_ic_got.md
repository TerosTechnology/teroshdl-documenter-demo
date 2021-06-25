# Entity: fifo_ic_got
## Diagram
![Diagram](fifo_ic_got.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					FIFO, independent clocks (ic), first-word-fall-through mode
Description:
-------------------------------------
Independent clocks meens that read and write clock are unrelated.
This implementation uses dedicated block RAM for storing data.
First-word-fall-through (FWFT) mode is implemented, so data can be read out
as soon as ``valid`` goes high. After the data has been captured, then the
signal ``got`` must be asserted.
Synchronous reset is used. Both resets may overlap.
``DATA_REG`` (=true) is a hint, that distributed memory or registers should be
used as data storage. The actual memory type depends on the device
architecture. See implementation for details.
``*STATE_*_BITS`` defines the granularity of the fill state indicator
``*state_*``. ``fstate_rd`` is associated with the read clock domain and outputs
the guaranteed number of words available in the FIFO. ``estate_wr`` is
associated with the write clock domain and outputs the number of words that
is guaranteed to be accepted by the FIFO without a capacity overflow. Note
that both these indicators cannot replace the ``full`` or ``valid`` outputs as
they may be implemented as giving pessimistic bounds that are minimally off
the true fill state.
If a fill state is not of interest, set *STATE_*_BITS = 0.
``fstate_rd`` and ``estate_wr`` are combinatorial outputs and include an address
comparator (subtractor) in their path.
Examples:
- FSTATE_RD_BITS = 1: fstate_rd == 0 => 0/2 full
                      fstate_rd == 1 => 1/2 full (half full)
- FSTATE_RD_BITS = 2: fstate_rd == 0 => 0/4 full
                      fstate_rd == 1 => 1/4 full
                      fstate_rd == 2 => 2/4 full
                      fstate_rd == 3 => 3/4 full
License:
=============================================================================
Copyright 2007-2014 Technische Universitaet Dresden - Germany
                    Chair of VLSI-Design, Diagnostics and Architecture
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
"all" required by Quartus RTL simulation
## Generics
| Generic name   | Type     | Value | Description                     |
| -------------- | -------- | ----- | ------------------------------- |
| D_BITS         | positive |       | Data Width                      |
| MIN_DEPTH      | positive |       | Minimum FIFO Depth              |
| DATA_REG       | boolean  | false | Store Data Content in Registers |
| OUTPUT_REG     | boolean  | false | Registered FIFO Output          |
| ESTATE_WR_BITS | natural  | 0     | Empty State Bits                |
| FSTATE_RD_BITS | natural  | 0     | Full State Bits                 |
## Ports
| Port name | Direction | Type                                                 | Description     |
| --------- | --------- | ---------------------------------------------------- | --------------- |
| clk_wr    | in        | std_logic                                            | Write Interface |
| rst_wr    | in        | std_logic                                            |                 |
| put       | in        | std_logic                                            |                 |
| din       | in        | std_logic_vector(D_BITS-1 downto 0)                  |                 |
| full      | out       | std_logic                                            |                 |
| estate_wr | out       | std_logic_vector(imax(ESTATE_WR_BITS-1, 0) downto 0) |                 |
| clk_rd    | in        | std_logic                                            | Read Interface  |
| rst_rd    | in        | std_logic                                            |                 |
| got       | in        | std_logic                                            |                 |
| valid     | out       | std_logic                                            |                 |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0)                  |                 |
| fstate_rd | out       | std_logic_vector(imax(FSTATE_RD_BITS-1, 0) downto 0) |                 |
## Signals
| Name | Type                                | Description             |
| ---- | ----------------------------------- | ----------------------- |
| IP1  | std_logic_vector(AN-1 downto 0)     | IP + 1                  |
| IP0  | std_logic_vector(AN-1 downto 0)     | Write Pointer IP        |
| IPz  | std_logic_vector(AN-1 downto 0)     | IP delayed by one clock |
| OPs  | std_logic_vector(AN-1 downto 0)     | Sync stage: OP0 -> OPc  |
| OPc  | std_logic_vector(AN-1 downto 0)     | Copy of OP              |
| Ful  | std_logic                           | RAM full                |
| OP1  | std_logic_vector(AN-1 downto 0)     | OP + 1                  |
| OP0  | std_logic_vector(AN-1 downto 0)     | Read Pointer OP         |
| IPs  | std_logic_vector(AN-1 downto 0)     | Sync stage: IPz -> IPc  |
| IPc  | std_logic_vector(AN-1 downto 0)     | Copy of IP              |
| Avl  | std_logic                           | RAM Data available      |
| Vld  | std_logic                           | Output Valid            |
| wa   | unsigned(A_BITS-1 downto 0)         | Memory Connectivity     |
| di   | std_logic_vector(D_BITS-1 downto 0) |                         |
| puti | std_logic                           |                         |
| ra   | unsigned(A_BITS-1 downto 0)         |                         |
| do   | std_logic_vector(D_BITS-1 downto 0) |                         |
| geti | std_logic                           |                         |
| goti | std_logic                           |                         |
## Constants
| Name   | Type     | Value                  | Description |
| ------ | -------- | ---------------------- | ----------- |
| A_BITS | positive |  log2ceilnz(MIN_DEPTH) |             |
| AN     | positive |  A_BITS + 1            |             |
## Processes
- unnamed: _( clk_wr )_
Update Write Pointer upon puti

**Description**
Update Write Pointer upon puti

- unnamed: _( clk_rd )_

