# Entity: IprogUltraScale

- **File**: IprogUltraScale.vhd
## Diagram

![Diagram](IprogUltraScale.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:   Uses the ICAP primitive to internally
                toggle the PROG_B via IPROG command
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

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| TPD_G          | time    | 1 ns  |             |
| USE_SLOWCLK_G  | boolean | false |             |
| BUFR_CLK_DIV_G | natural | 8     |             |
| RST_POLARITY_G | sl      | '1'   |             |
## Ports

| Port name   | Direction | Type             | Description |
| ----------- | --------- | ---------------- | ----------- |
| clk         | in        | sl               |             |
| rst         | in        | sl               |             |
| slowClk     | in        | sl               |             |
| start       | in        | sl               |             |
| bootAddress | in        | slv(31 downto 0) |             |
## Signals

| Name            | Type             | Description |
| --------------- | ---------------- | ----------- |
| r               | RegType          |             |
| rin             | RegType          |             |
| divClk          | sl               |             |
| icape2Clk       | sl               |             |
| icape2Rst       | sl               |             |
| startEdge       | sl               |             |
| rdy             | sl               |             |
| bootAddressSync | slv(31 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state       => IDLE_S,<br><span style="padding-left:20px">       csl         => '1',<br><span style="padding-left:20px">       rdy         => '1',<br><span style="padding-left:20px">       rnw         => '1',<br><span style="padding-left:20px">       cnt         => (others => '0'),<br><span style="padding-left:20px">       configData  => (others => '0'),<br><span style="padding-left:20px">       bootAddress => (others => '0')) |             |
## Types

| Name      | Type                                                  | Description |
| --------- | ----------------------------------------------------- | ----------- |
| StateType | (IDLE_S,<br><span style="padding-left:20px"> PROG_S)  |             |
| RegType   |                                                       |             |
## Functions
- selectMapBitSwapping <font id="function_arguments">(input : slv) </font> <font id="function_return">return slv </font>
## Processes
- comb: ( bootAddressSync, icape2Rst, r, rdy, startEdge )
</br>**Description**
 1-bit input: Read/Write Select input 
- seq: ( icape2Clk )
## Instantiations

- BUFGCE_DIV_Inst: BUFGCE_DIV
- RstSync_Inst: surf.RstSync
- SynchronizerOneShot_1: surf.SynchronizerOneShot
- SynchronizerVector_1: work.SynchronizerVector
- ICAPE3_Inst: ICAPE3
