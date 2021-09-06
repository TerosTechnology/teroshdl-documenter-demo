# Entity: SaciMasterSync

- **File**: SaciMasterSync.vhd
## Diagram

![Diagram](SaciMasterSync.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Saci Master Synchronization Wrapper
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

| Generic name          | Type    | Value | Description |
| --------------------- | ------- | ----- | ----------- |
| TPD_G                 | time    | 1 ns  |             |
| SYNCHRONIZE_CONTROL_G | boolean | true  |             |
## Ports

| Port name     | Direction | Type                              | Description        |
| ------------- | --------- | --------------------------------- | ------------------ |
| clk           | in        | sl                                |  Main clock        |
| rst           | in        | sl                                |                    |
| saciClk       | out       | sl                                | Serial interface   |
| saciSelL      | out       | slv(SACI_NUM_SLAVES_C-1 downto 0) |                    |
| saciCmd       | out       | sl                                |                    |
| saciRsp       | in        | sl                                |                    |
| saciHalfClk   | in        | slv(7 downto 0)                   |                    |
| saciMasterIn  | in        | SaciMasterInType                  | Parallel interface |
| saciMasterOut | out       | SaciMasterOutType                 |                    |
## Signals

| Name           | Type                  | Description |
| -------------- | --------------------- | ----------- |
| r              | RegType               |             |
|  rin           | RegType               |             |
| saciRspFall    | sl                    |             |
| saciClkCnt     | unsigned(31 downto 0) |             |
| saciClkCntRst  | std_logic             |             |
| saciClkRising  | std_logic             |             |
| saciClkFalling | std_logic             |             |
| iSaciClk       | std_logic             |             |
| iSaciClkD      | std_logic             |             |
## Constants

| Name                  | Type             | Value                                                                                                           | Description |
| --------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------- | ----------- |
| SYNCHRONIZER_INIT_0_C | SynchronizerType |  (tmp => '0',<br><span style="padding-left:20px"> sync => '0',<br><span style="padding-left:20px"> last => '0') |             |
| SYNCHRONIZER_INIT_1_C | SynchronizerType |  (tmp => '1',<br><span style="padding-left:20px"> sync => '1',<br><span style="padding-left:20px"> last => '1') |             |
## Types

| Name             | Type                                                                                                                                                                                                                                                                                              | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SynchronizerType |                                                                                                                                                                                                                                                                                                   |             |
| StateType        | (IDLE_S,<br><span style="padding-left:20px"> CHIP_SELECT_S,<br><span style="padding-left:20px"> TX_S,<br><span style="padding-left:20px"> RX_START_S,<br><span style="padding-left:20px"> RX_HEADER_S,<br><span style="padding-left:20px"> RX_DATA_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType          |                                                                                                                                                                                                                                                                                                   |             |
## Functions
- synchronize <font id="function_arguments">( input   : in  sl;<br><span style="padding-left:20px"> current : in  SynchronizerType;<br><span style="padding-left:20px"> nextOut : out SynchronizerType) </font> <font id="function_return">return ()</font>
## Processes
- saci_clk_p: ( clk, rst )
- fall: ( clk, rst )
</br>**Description**
------------------------------------------------------------------------------------------------  Capture serial input ------------------------------------------------------------------------------------------------ 
- seq: ( clk, rst )
- comb: ( r, saciRspFall, saciMasterIn, saciClkRising )
