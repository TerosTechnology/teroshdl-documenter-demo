# Entity: AxiWritePathMux

## Diagram

![Diagram](AxiWritePathMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Block to connect multiple incoming AXI write path interfaces.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                  | Value | Description |
| ------------ | --------------------- | ----- | ----------- |
| TPD_G        | time                  | 1 ns  |             |
| NUM_SLAVES_G | integer range 1 to 32 | 4     |             |
## Ports

| Port name        | Direction | Type                                         | Description     |
| ---------------- | --------- | -------------------------------------------- | --------------- |
| axiClk           | in        | sl                                           | Clock and reset |
| axiRst           | in        | sl                                           |                 |
| sAxiWriteMasters | in        | AxiWriteMasterArray(NUM_SLAVES_G-1 downto 0) | Slaves          |
| sAxiWriteSlaves  | out       | AxiWriteSlaveArray(NUM_SLAVES_G-1 downto 0)  |                 |
| mAxiWriteMaster  | out       | AxiWriteMasterType                           | Master          |
| mAxiWriteSlave   | in        | AxiWriteSlaveType                            |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DEST_SIZE_C | integer |  bitSize(NUM_SLAVES_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
| ARB_BITS_C  | integer |  2**DEST_SIZE_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| REG_INIT_C  | RegType |  (       addrState  => S_IDLE_C,<br><span style="padding-left:20px">       addrAcks   => (others => '0'),<br><span style="padding-left:20px">       addrAckNum => (others => '0'),<br><span style="padding-left:20px">       addrValid  => '0',<br><span style="padding-left:20px">       dataReq    => '0',<br><span style="padding-left:20px">       dataAck    => '0',<br><span style="padding-left:20px">       dataState  => S_IDLE_C,<br><span style="padding-left:20px">       dataAckNum => (others => '0'),<br><span style="padding-left:20px">       slaves     => (others => AXI_WRITE_SLAVE_INIT_C),<br><span style="padding-left:20px">       master     => AXI_WRITE_MASTER_INIT_C       ) |             |
## Types

| Name      | Type                                                                                                                                                  | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (S_IDLE_C,<br><span style="padding-left:20px"> S_MOVE_C,<br><span style="padding-left:20px"> S_LAST_C,<br><span style="padding-left:20px"> S_WAIT_C)  |             |
| RegType   |                                                                                                                                                       |             |
## Processes
- comb: ( axiRst, r, sAxiWriteMasters, mAxiWriteSlave )
- seq: ( axiClk )
