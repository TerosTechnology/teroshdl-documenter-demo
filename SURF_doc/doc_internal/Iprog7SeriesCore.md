# Entity: Iprog7SeriesCore

- **File**: Iprog7SeriesCore.vhd
## Diagram

![Diagram](Iprog7SeriesCore.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for Xilinx 7-Series IPROG CMD
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

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| TPD_G         | time    | 1 ns  |             |
| SYNC_RELOAD_G | boolean | true  |             |
## Ports

| Port name  | Direction | Type             | Description                                |
| ---------- | --------- | ---------------- | ------------------------------------------ |
| reload     | in        | sl               | Can be asynchronous if SYNC_RELOAD_G=false |
| reloadAddr | in        | slv(31 downto 0) |                                            |
| icapClk    | in        | sl               |                                            |
| icapClkRst | in        | sl               |                                            |
| icapReq    | out       | sl               |                                            |
| icapGrant  | in        | sl               |                                            |
| icapCsl    | out       | sl               |                                            |
| icapRnw    | out       | sl               |                                            |
| icapI      | out       | slv(31 downto 0) |                                            |
## Signals

| Name           | Type             | Description |
| -------------- | ---------------- | ----------- |
| r              | RegType          |             |
| rin            | RegType          |             |
| icapReloadAddr | slv(31 downto 0) |             |
| icapReload     | sl               |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| BYPASS_SYNC_C | boolean |  not SYNC_RELOAD_G                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C    | RegType |  (       state      => IDLE_S,<br><span style="padding-left:20px">       req        => '0',<br><span style="padding-left:20px">       csl        => '1',<br><span style="padding-left:20px">       rnw        => '1',<br><span style="padding-left:20px">       cnt        => (others => '0'),<br><span style="padding-left:20px">       configData => (others => '0')) |             |
## Types

| Name      | Type                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------ | ----------- |
| StateType | (IDLE_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> PROG_S)  |             |
| RegType   |                                                                                                  |             |
## Functions
- selectMapBitSwapping <font id="function_arguments">(input : slv) </font> <font id="function_return">return slv </font>
## Processes
- comb: ( icapClkRst, icapGrant, icapReload, icapReloadAddr, r )
- seq: ( icapClk )
## Instantiations

- SynchronizerAddress_1: surf.SynchronizerVector
- SynchronizerStart_1: surf.SynchronizerEdge
**Description**
 Capture edge of start on icapClk

