# Entity: Gearbox

- **File**: Gearbox.vhd
## Diagram

![Diagram](Gearbox.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : Gearbox
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: A generic gearbox
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

| Generic name         | Type     | Value | Description |
| -------------------- | -------- | ----- | ----------- |
| TPD_G                | time     | 1 ns  |             |
| SLAVE_BIT_REVERSE_G  | boolean  | false |             |
| SLAVE_WIDTH_G        | positive |       |             |
| MASTER_BIT_REVERSE_G | boolean  | false |             |
| MASTER_WIDTH_G       | positive |       |             |
## Ports

| Port name      | Direction | Type                           | Description                       |
| -------------- | --------- | ------------------------------ | --------------------------------- |
| clk            | in        | sl                             | Clock and Reset                   |
| rst            | in        | sl                             |                                   |
| slaveData      | in        | slv(SLAVE_WIDTH_G-1 downto 0)  | input side data and flow control  |
| slaveValid     | in        | sl                             |                                   |
| slaveReady     | out       | sl                             |                                   |
| slaveBitOrder  | in        | sl                             |                                   |
| startOfSeq     | in        | sl                             | sequencing and slip               |
| slip           | in        | sl                             |                                   |
| masterData     | out       | slv(MASTER_WIDTH_G-1 downto 0) | output side data and flow control |
| masterValid    | out       | sl                             |                                   |
| masterReady    | in        | sl                             |                                   |
| masterBitOrder | in        | sl                             |                                   |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                                                                                                                                          | Description                              |
| ------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| MAX_C         | integer |  maximum(MASTER_WIDTH_G,<br><span style="padding-left:20px"> SLAVE_WIDTH_G)                                                                                                                                                                                                                    |                                          |
| MIN_C         | integer |  minimum(MASTER_WIDTH_G,<br><span style="padding-left:20px"> SLAVE_WIDTH_G)                                                                                                                                                                                                                    |                                          |
| SHIFT_WIDTH_C | integer |  wordCount(MAX_C,<br><span style="padding-left:20px"> MIN_C) * MIN_C + MIN_C + 1                                                                                                                                                                                                               |  Don't need the +1 if slip is not used.  |
| REG_INIT_C    | RegType |  (       masterValid => '0',<br><span style="padding-left:20px">       shiftReg    => (others => '0'),<br><span style="padding-left:20px">       writeIndex  => 0,<br><span style="padding-left:20px">       slaveReady  => '0',<br><span style="padding-left:20px">       slip        => '0') |                                          |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( masterBitOrder, masterReady, r, rst, slaveBitOrder,
                   slaveData, slaveValid, slip, startOfSeq )
- sync: ( clk )
