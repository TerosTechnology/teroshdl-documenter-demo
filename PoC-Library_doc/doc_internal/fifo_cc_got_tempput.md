# Entity: fifo_cc_got_tempput

- **File**: fifo_cc_got_tempput.vhdl
## Diagram

![Diagram](fifo_cc_got_tempput.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Thomas B. Preusser
									Steffen Koehler
									Martin Zabel
									Patrick Lehmann

 Entity:					FIFO, common clock (cc), pipelined interface, writes only become effective after explicit commit

 Description:
 -------------------------------------
 The specified depth (``MIN_DEPTH``) is rounded up to the next suitable value.

 As uncommitted writes populate FIFO space that is not yet available for
 reading, an instance of this FIFO can, indeed, report ``full`` and ``not vld``
 at the same time. While a ``commit`` would eventually make data available for
 reading (``vld``), a ``rollback`` would free the space for subsequent writing
 (``not ful``).

 ``commit`` and ``rollback`` are inclusive and apply to all writes (``put``) since
 the previous 'commit' or 'rollback' up to and including a potentially
 simultaneous write.

 The FIFO state upon a simultaneous assertion of ``commit`` and ``rollback`` is
 *undefined*.

 ``*STATE_*_BITS`` defines the granularity of the fill state indicator
 ``*state_*``. ``fstate_rd`` is associated with the read clock domain and outputs
 the guaranteed number of words available in the FIFO. ``estate_wr`` is
 associated with the write clock domain and outputs the number of words that
 is guaranteed to be accepted by the FIFO without a capacity overflow. Note
 that both these indicators cannot replace the ``full`` or ``valid`` outputs as
 they may be implemented as giving pessimistic bounds that are minimally off
 the true fill state.

 If a fill state is not of interest, set ``*STATE_*_BITS = 0``.

 ``fstate_rd`` and ``estate_wr`` are combinatorial outputs and include an address
 comparator (subtractor) in their path.

 **Examples:**

 * FSTATE_RD_BITS = 1:

   * fstate_rd == 0 => 0/2 full
   * fstate_rd == 1 => 1/2 full (half full)

 * FSTATE_RD_BITS = 2:

   * fstate_rd == 0 => 0/4 full
   * fstate_rd == 1 => 1/4 full
   * fstate_rd == 2 => 2/4 full
   * fstate_rd == 3 => 3/4 full

 License:
 =============================================================================
 Copyright 2007-2014 Technische Universitaet Dresden - Germany,
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

| Generic name   | Type     | Value | Description                       |
| -------------- | -------- | ----- | --------------------------------- |
| D_BITS         | positive |       |  Data Width                       |
| MIN_DEPTH      | positive |       |  Minimum FIFO Depth               |
| DATA_REG       | boolean  | false |  Store Data Content in Registers  |
| STATE_REG      | boolean  | false |  Registered Full/Empty Indicators |
| OUTPUT_REG     | boolean  | false |  Registered FIFO Output           |
| ESTATE_WR_BITS | natural  | 0     |  Empty State Bits                 |
| FSTATE_RD_BITS | natural  | 0     |  Full State Bits                  |
## Ports

| Port name | Direction | Type                                                 | Description            |
| --------- | --------- | ---------------------------------------------------- | ---------------------- |
| rst       | in        | std_logic                                            | Global Reset and Clock |
| clk       | in        | std_logic                                            | Global Reset and Clock |
| put       | in        | std_logic                                            |  Write Request         |
| din       | in        | std_logic_vector(D_BITS-1 downto 0)                  |  Input Data            |
| full      | out       | std_logic                                            |                        |
| estate_wr | out       | std_logic_vector(imax(0, ESTATE_WR_BITS-1) downto 0) |                        |
| commit    | in        | std_logic                                            |                        |
| rollback  | in        | std_logic                                            |                        |
| got       | in        | std_logic                                            |  Read Completed        |
| dout      | out       | std_logic_vector(D_BITS-1 downto 0)                  |  Output Data           |
| valid     | out       | std_logic                                            |                        |
| fstate_rd | out       | std_logic_vector(imax(0, FSTATE_RD_BITS-1) downto 0) |                        |
## Signals

| Name  | Type                        | Description                                                                                                                     |
| ----- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| IP0   | unsigned(A_BITS-1 downto 0) | ---------------------------------------------------------------------------  Memory Pointers  Actual Input and Output Pointers  |
| OP0   | unsigned(A_BITS-1 downto 0) |                                                                                                                                 |
| IP1   | unsigned(A_BITS-1 downto 0) |  Incremented Input and Output Pointers                                                                                          |
| OP1   | unsigned(A_BITS-1 downto 0) |                                                                                                                                 |
| IPm   | unsigned(A_BITS-1 downto 0) |  Committed Write Pointer (Commit Marker)                                                                                        |
| wa    | unsigned(A_BITS-1 downto 0) | ---------------------------------------------------------------------------  Backing Memory Connectivity  Write Port            |
| we    | std_logic                   |                                                                                                                                 |
| ra    | unsigned(A_BITS-1 downto 0) |  Read Port                                                                                                                      |
| re    | std_logic                   |                                                                                                                                 |
| fulli | std_logic                   |  Internal full and empty indicators                                                                                             |
| empti | std_logic                   |                                                                                                                                 |
## Constants

| Name        | Type    | Value                                                                         | Description                                                            |
| ----------- | ------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| A_BITS      | natural |  log2ceil(MIN_DEPTH)                                                          |                                                                        |
| FORCE_XILCY | boolean |  (not SIMULATION) and (VENDOR = VENDOR_XILINX) and STATE_REG and (A_BITS > 4) |  Force Carry-Chain Use for Pointer Increments on Xilinx Architectures  |
## Processes
- unnamed: ( clk )
- unnamed: ( fulli, IP0, IPm, OP0 )
</br>**Description**
 Fill State Computation (soft indicators) 
