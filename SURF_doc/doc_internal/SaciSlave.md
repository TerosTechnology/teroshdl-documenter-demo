# Entity: SaciSlave

- **File**: SaciSlave.vhd
## Diagram

![Diagram](SaciSlave.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Slave module for SACI interface.
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

| Port name | Direction | Type             | Description                                                     |
| --------- | --------- | ---------------- | --------------------------------------------------------------- |
| rstL      | in        | sl               |  ASIC global reset                                              |
| saciClk   | in        | sl               | Serial Interface                                                |
| saciSelL  | in        | sl               |  chipSelect                                                     |
| saciCmd   | in        | sl               |                                                                 |
| saciRsp   | out       | sl               |                                                                 |
| rstOutL   | out       | sl               | Silly reset hack to get saciSelL | rst onto dedicated reset bar |
| rstInL    | in        | sl               |                                                                 |
| exec      | out       | sl               | Detector (Parallel) Interface                                   |
| ack       | in        | sl               |                                                                 |
| readL     | out       | sl               |                                                                 |
| cmd       | out       | slv(6 downto 0)  |                                                                 |
| addr      | out       | slv(11 downto 0) |                                                                 |
| wrData    | out       | slv(31 downto 0) |                                                                 |
| rdData    | in        | slv(31 downto 0) |                                                                 |
## Signals

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| r           | RegType |             |
|  rin        | RegType |             |
| saciCmdFall | sl      |             |
## Types

| Name      | Type                                                            | Description |
| --------- | --------------------------------------------------------------- | ----------- |
| StateType | (WAIT_START_S,<br><span style="padding-left:20px"> SHIFT_IN_S)  |             |
| RegType   |                                                                 |             |
## Functions
- shiftInLeft <font id="function_arguments">( i : in    sl;<br><span style="padding-left:20px"> v : inout slv) </font> <font id="function_return">return ()</font>
## Processes
- fall: ( saciClk, rstInL )
**Description**
 Clock in serial input on falling edge 
- seq: ( saciClk, rstInL )
- comb: ( r, saciCmdFall, ack, rdData, saciSelL )
