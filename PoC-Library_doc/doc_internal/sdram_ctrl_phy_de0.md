# Entity: sdram_ctrl_phy_de0

- **File**: sdram_ctrl_phy_de0.vhdl
## Diagram

![Diagram](sdram_ctrl_phy_de0.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Martin Zabel
Entity:					Physical layer of SDRAM-Controller for Altera DE0 Board
Description:
-------------------------------------
Physical layer used by module :ref:`sdram_ctrl_de0 <IP:sdram_ctrl_de0>`.
Instantiates input and output buffer components and adjusts the timing for
the Altera DE0 board.
Clock and Reset Signals
***********************
+-----------+-----------------------------------------------------------+
| Port      | Description                                               |
+===========+===========================================================+
|clk        | Base clock for command and write data path.               |
+-----------+-----------------------------------------------------------+
|rst        | Reset for ``clk``.                                        |
+-----------+-----------------------------------------------------------+
Command signals and write data are sampled with ``clk``.
Read data is also aligned with ``clk``.
Write and read enable (wren_nxt, rden_nxt) must be hold for:
* 1 clock cycle  if BL = 1,
* 2 clock cycles if BL = 2, or
* 4 clock cycles if BL = 4, or
* 8 clock cycles if BL = 8.
They must be first asserted with the read and write command. Proper delay is
included in this unit.
The first word to write must be asserted with the write command. Proper
delay is included in this unit.
Synchronous resets are used. Reset must be hold for at least two cycles.
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany,
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
Naming Conventions:
(Based on: Keating and Bricaud: "Reuse Methodology Manual")
active low signals: "*_n"
clock signals: "clk", "clk_div#", "clk_#x"
reset signals: "rst", "rst_n"
generics: all UPPERCASE
user defined types: "*_TYPE"
state machine next state: "*_ns"
state machine current state: "*_cs"
output of a register: "*_r"
asynchronous signal: "*_a"
pipelined or register delay signals: "*_p#"
data before being registered into register with the same name: "*_nxt"
clock enable signals: "*_ce"
internal version of output port: "*_i"
tristate internal signal "*_z"
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| CL           | positive |       |             |
## Ports

| Port name  | Direction | Type                          | Description |
| ---------- | --------- | ----------------------------- | ----------- |
| clk        | in        | std_logic                     |             |
| clkout     | in        | std_logic                     |             |
| rst        | in        | std_logic                     |             |
| sd_cke_nxt | in        | std_logic                     |             |
| sd_cs_nxt  | in        | std_logic                     |             |
| sd_ras_nxt | in        | std_logic                     |             |
| sd_cas_nxt | in        | std_logic                     |             |
| sd_we_nxt  | in        | std_logic                     |             |
| sd_ba_nxt  | in        | std_logic_vector(1 downto 0)  |             |
| sd_a_nxt   | in        | std_logic_vector(11 downto 0) |             |
| wren_nxt   | in        | std_logic                     |             |
| wdata_nxt  | in        | std_logic_vector(15 downto 0) |             |
| rden_nxt   | in        | std_logic                     |             |
| rdata      | out       | std_logic_vector(15 downto 0) |             |
| rstb       | out       | std_logic                     |             |
| sd_ck      | out       | std_logic                     |             |
| sd_cke     | out       | std_logic                     |             |
| sd_cs      | out       | std_logic                     |             |
| sd_ras     | out       | std_logic                     |             |
| sd_cas     | out       | std_logic                     |             |
| sd_we      | out       | std_logic                     |             |
| sd_ba      | out       | std_logic_vector(1 downto 0)  |             |
| sd_a       | out       | std_logic_vector(11 downto 0) |             |
| sd_dq      | inout     | std_logic_vector(15 downto 0) |             |
## Signals

| Name     | Type                          | Description                                                               |
| -------- | ----------------------------- | ------------------------------------------------------------------------- |
| sd_cke_r | std_logic                     |                                                                           |
| sd_cs_r  | std_logic                     |                                                                           |
| sd_ras_r | std_logic                     |                                                                           |
| sd_cas_r | std_logic                     |                                                                           |
| sd_we_r  | std_logic                     |                                                                           |
| sd_ba_r  | std_logic_vector(1 downto 0)  |                                                                           |
| sd_a_r   | std_logic_vector(11 downto 0) |                                                                           |
| dq_en_r  | std_logic_vector(15 downto 0) | control / data signals for write                                          |
| dq_o_r   | std_logic_vector(15 downto 0) |                                                                           |
| dq_i     | std_logic_vector(15 downto 0) | control / data signals for readadjust read delay through length of vector |
| rden_r   | std_logic_vector(CL downto 0) |                                                                           |
| rstb_r   | std_logic                     |                                                                           |
| rdata_r  | std_logic_vector(15 downto 0) |                                                                           |
## Processes
- unnamed: ( clk )
**Description**
Output clock 180 deg phase-shifted with respect to control/data signals
 generic map (
   WIDTH => 1)
 port map (
   datain_h   => "0",
   datain_l   => "1",
   dataout(0) => sd_ck,
   outclock   => clk);
SDRAM command & address
These registers should be placed in the I/O blocks.
Use appriopate timing constraints.

- unnamed: ( clk )
**Description**
Write data
These registers should be placed in the I/O blocks.
Use appriopate timing constraints.

- unnamed: ( clk )
**Description**
Read data capture

## Instantiations

- sd_ck_obuf: altiobuf_out
- dq_obuf: altiobuf_out
**Description**
DQ I/O Buffers
Explicit instantiation of I/O buffers. May be required if entity is part
of a netlist, which is used in another design.
If altiobuf_bidir is used instead, then meaningless warnings are issued by
Quartus.

- dq_ibuf: altiobuf_in
