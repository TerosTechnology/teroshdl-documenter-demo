# Entity: AdiConfigSlave

- **File**: AdiConfigSlave.vhd
## Diagram

![Diagram](AdiConfigSlave.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: An implementation of the common SPI configuration interface
 use by many AnalogDevices chips.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | in        | sl               |             |
| sclk      | in        | sl               |             |
| sdio      | inout     | sl               |             |
| csb       | in        | sl               |             |
| wrEn      | out       | sl               |             |
| rdEn      | out       | sl               |             |
| addr      | out       | slv(12 downto 0) |             |
| wrData    | out       | slv(31 downto 0) |             |
| byteValid | out       | slv(3 downto 0)  |             |
| rdData    | in        | slv(31 downto 0) |             |
## Signals

| Name     | Type    | Description |
| -------- | ------- | ----------- |
| r        | RegType |             |
| rin      | RegType |             |
| sdioRes  | sl      |             |
| sdioSync | sl      |             |
| sdioRise | sl      |             |
| sdioFall | sl      |             |
| sclkRes  | sl      |             |
| sclkSync | sl      |             |
| sclkRise | sl      |             |
| sclkFall | sl      |             |
| csbRes   | sl      |             |
| csbSync  | sl      |             |
| csbRise  | sl      |             |
| csbFall  | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state     => WAIT_CSB_FALL_S,<br><span style="padding-left:20px">       count     => (others => '0'),<br><span style="padding-left:20px">       shift     => (others => '0'),<br><span style="padding-left:20px">       bytes     => (others => '0'),<br><span style="padding-left:20px">       wrEn      => '0',<br><span style="padding-left:20px">       rdEn      => '0',<br><span style="padding-left:20px">       addr      => (others => '0'),<br><span style="padding-left:20px">       wrData    => (others => '0'),<br><span style="padding-left:20px">       byteValid => (others => '0'),<br><span style="padding-left:20px">       dataOut   => '1') |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( WAIT_CSB_FALL_S,<br><span style="padding-left:20px"> SHIFT_HEADER_S,<br><span style="padding-left:20px"> LATCH_HEADER_S,<br><span style="padding-left:20px"> WRITE_S,<br><span style="padding-left:20px"> LATCH_WRITE_BYTE_S,<br><span style="padding-left:20px"> READ_WAIT_S,<br><span style="padding-left:20px"> LATCH_READ_BYTE_S,<br><span style="padding-left:20px"> READ_S,<br><span style="padding-left:20px"> WAIT_SCLK_RISE_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
## Processes
- comb: ( csbFall, r, rdData, sclkFall, sclkRise, sdioSync )
- seq: ( clk )
## Instantiations

- SynchronizerEdge_SDIO: surf.SynchronizerEdge
- SynchronizerEdge_SCLK: surf.SynchronizerEdge
- SynchronizerEdge_CSB: surf.SynchronizerEdge
