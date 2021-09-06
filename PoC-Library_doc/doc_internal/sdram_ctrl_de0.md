# Entity: sdram_ctrl_de0

- **File**: sdram_ctrl_de0.vhdl
## Diagram

![Diagram](sdram_ctrl_de0.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Martin Zabel

 Entity:					Controller for ISSI SDR-SDRAM for Altera DE0 Board

 Description:
 -------------------------------------
 Complete controller for ISSI SDR-SDRAM for Altera DE0 Board.

 SDRAM Device: IS42S16400F

 Configuration
 *************

 +------------+----------------------------------------------------+
 | Parameter  | Description                                        |
 +============+====================================================+
 | CLK_PERIOD | Clock period in nano seconds. All SDRAM timings are|
 |            | calculated for the device stated above.            |
 +------------+----------------------------------------------------+
 | CL         | CAS latency, choose according to clock frequency.  |
 +------------+----------------------------------------------------+
 | BL         | Burst length. Choose BL=1 for single cycle memory  |
 |            | transactions as required for the PoC.Mem interface.|
 +------------+----------------------------------------------------+

 Tested with: CLK_PERIOD = 7.5 (133 MHz), CL=2, BL=1.

 Operation
 *********

 Command, address and write data is sampled with ``clk``.
 Read data is also aligned with ``clk``.

 For description on ``clkout`` see
 :ref:`sdram_ctrl_phy_de0 <IP:sdram_ctrl_phy_de0>`.

 Synchronous resets are used.

 License:
 =============================================================================
 Copyright 2007-2016 Technische Universitaet Dresden - Germany,
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
| CLK_PERIOD   | real     |       |             |
| CL           | positive |       |             |
| BL           | positive |       |             |
## Ports

| Port name        | Direction | Type                          | Description |
| ---------------- | --------- | ----------------------------- | ----------- |
| clk              | in        | std_logic                     |             |
| clkout           | in        | std_logic                     |             |
| rst              | in        | std_logic                     |             |
| user_cmd_valid   | in        | std_logic                     |             |
| user_wdata_valid | in        | std_logic                     |             |
| user_write       | in        | std_logic                     |             |
| user_addr        | in        | std_logic_vector(21 downto 0) |             |
| user_wdata       | in        | std_logic_vector(15 downto 0) |             |
| user_got_cmd     | out       | std_logic                     |             |
| user_got_wdata   | out       | std_logic                     |             |
| user_rdata       | out       | std_logic_vector(15 downto 0) |             |
| user_rstb        | out       | std_logic                     |             |
| sd_ck            | out       | std_logic                     |             |
| sd_cke           | out       | std_logic                     |             |
| sd_cs            | out       | std_logic                     |             |
| sd_ras           | out       | std_logic                     |             |
| sd_cas           | out       | std_logic                     |             |
| sd_we            | out       | std_logic                     |             |
| sd_ba            | out       | std_logic_vector(1 downto 0)  |             |
| sd_a             | out       | std_logic_vector(11 downto 0) |             |
| sd_dq            | inout     | std_logic_vector(15 downto 0) |             |
## Signals

| Name       | Type                          | Description    |
| ---------- | ----------------------------- | -------------- |
| sd_cke_nxt | std_logic                     |   Signals<br>  |
| sd_cs_nxt  | std_logic                     |                |
| sd_ras_nxt | std_logic                     |                |
| sd_cas_nxt | std_logic                     |                |
| sd_we_nxt  | std_logic                     |                |
| sd_a_nxt   | std_logic_vector(11 downto 0) |                |
| sd_ba_nxt  | std_logic_vector(1 downto 0)  |                |
| rden_nxt   | std_logic                     |                |
| wren_nxt   | std_logic                     |                |
## Constants

| Name      | Type     | Value                                                                                                         | Description  |
| --------- | -------- | ------------------------------------------------------------------------------------------------------------- | ------------ |
| A_BITS    | positive |  22                                                                                                           |  4M          |
| D_BITS    | positive |  16                                                                                                           |  x16         |
| R_BITS    | positive |  12                                                                                                           |  4096 rows   |
| C_BITS    | positive |   8                                                                                                           |  256 columns |
| B_BITS    | positive |   2                                                                                                           |  4 banks     |
| T_MRD     | integer  |  2                                                                                                            |  fix         |
| T_RAS     | integer  |  integer(ceil(42.0/CLK_PERIOD))                                                                               |              |
| T_RCD     | integer  |  integer(ceil(18.0/CLK_PERIOD))                                                                               |              |
| T_RFC     | integer  |  integer(ceil(60.0/CLK_PERIOD))                                                                               |  t_RC        |
| T_RP      | integer  |  integer(ceil(18.0/CLK_PERIOD))                                                                               |              |
| T_WR      | integer  |  2                                                                                                            |  fix         |
| T_WTR     | integer  |  1                                                                                                            |              |
| T_REFI    | integer  |  integer(ceil(15625.0/  -- 64 ms / 4096 rows                                                CLK_PERIOD))-50   |              |
| INIT_WAIT | integer  |  integer(ceil(100000.0/  -- 100 us                                                (real(T_REFI)*CLK_PERIOD))) |              |
## Instantiations

- fsm: poc.sdram_ctrl_fsm
- phy: poc.sdram_ctrl_phy_de0
