# Entity: AxiLiteCrossbar

- **File**: AxiLiteCrossbar.vhd
## Diagram

![Diagram](AxiLiteCrossbar.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper around Xilinx generated Main AXI Crossbar for HPS Front End
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

| Generic name       | Type                             | Value                   | Description |
| ------------------ | -------------------------------- | ----------------------- | ----------- |
| TPD_G              | time                             | 1 ns                    |             |
| NUM_SLAVE_SLOTS_G  | natural range 1 to 16            | 4                       |             |
| NUM_MASTER_SLOTS_G | natural range 1 to 64            | 4                       |             |
| DEC_ERROR_RESP_G   | slv(1 downto 0)                  | AXI_RESP_DECERR_C       |             |
| MASTERS_CONFIG_G   | AxiLiteCrossbarMasterConfigArray | AXIL_XBAR_CFG_DEFAULT_C |             |
| DEBUG_G            | boolean                          | false                   |             |
## Ports

| Port name        | Direction | Type                                                   | Description                             |
| ---------------- | --------- | ------------------------------------------------------ | --------------------------------------- |
| axiClk           | in        | sl                                                     |                                         |
| axiClkRst        | in        | sl                                                     |                                         |
| sAxiWriteMasters | in        | AxiLiteWriteMasterArray(NUM_SLAVE_SLOTS_G-1 downto 0)  | Slave Slots (Connect to AxiLite Masters |
| sAxiWriteSlaves  | out       | AxiLiteWriteSlaveArray(NUM_SLAVE_SLOTS_G-1 downto 0)   |                                         |
| sAxiReadMasters  | in        | AxiLiteReadMasterArray(NUM_SLAVE_SLOTS_G-1 downto 0)   |                                         |
| sAxiReadSlaves   | out       | AxiLiteReadSlaveArray(NUM_SLAVE_SLOTS_G-1 downto 0)    |                                         |
| mAxiWriteMasters | out       | AxiLiteWriteMasterArray(NUM_MASTER_SLOTS_G-1 downto 0) | Master Slots (Connect to AXI Slaves)    |
| mAxiWriteSlaves  | in        | AxiLiteWriteSlaveArray(NUM_MASTER_SLOTS_G-1 downto 0)  |                                         |
| mAxiReadMasters  | out       | AxiLiteReadMasterArray(NUM_MASTER_SLOTS_G-1 downto 0)  |                                         |
| mAxiReadSlaves   | in        | AxiLiteReadSlaveArray(NUM_MASTER_SLOTS_G-1 downto 0)   |                                         |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name           | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REQ_NUM_SIZE_C | integer |  bitSize(NUM_MASTER_SLOTS_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| ACK_NUM_SIZE_C | integer |  bitSize(NUM_SLAVE_SLOTS_G-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C     | RegType |  (       slave            => (          others        => (             wrState    => S_WAIT_AXI_TXN_S,<br><span style="padding-left:20px">             wrReqs     => (others => '0'),<br><span style="padding-left:20px">             wrReqNum   => (others => '0'),<br><span style="padding-left:20px">             rdState    => S_WAIT_AXI_TXN_S,<br><span style="padding-left:20px">             rdReqs     => (others => '0'),<br><span style="padding-left:20px">             rdReqNum   => (others => '0'))),<br><span style="padding-left:20px">       master           => (          others        => (             wrState    => M_WAIT_REQ_S,<br><span style="padding-left:20px">             wrAcks     => (others => '0'),<br><span style="padding-left:20px">             wrAckNum   => (others => '0'),<br><span style="padding-left:20px">             wrValid    => '0',<br><span style="padding-left:20px">             rdState    => M_WAIT_REQ_S,<br><span style="padding-left:20px">             rdAcks     => (others => '0'),<br><span style="padding-left:20px">             rdAckNum   => (others => '0'),<br><span style="padding-left:20px">             rdValid    => '0')),<br><span style="padding-left:20px">       sAxiWriteSlaves  => (others => AXI_LITE_WRITE_SLAVE_INIT_C),<br><span style="padding-left:20px">       sAxiReadSlaves   => (others => AXI_LITE_READ_SLAVE_INIT_C),<br><span style="padding-left:20px">       mAxiWriteMasters => axiWriteMasterInit(MASTERS_CONFIG_G),<br><span style="padding-left:20px">       mAxiReadMasters  => axiReadMasterInit(MASTERS_CONFIG_G)) |             |
## Types

| Name            | Type                                                                                                                                                           | Description |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SlaveStateType  | (S_WAIT_AXI_TXN_S,<br><span style="padding-left:20px"> S_DEC_ERR_S,<br><span style="padding-left:20px"> S_ACK_S,<br><span style="padding-left:20px"> S_TXN_S)  |             |
| SlaveType       |                                                                                                                                                                |             |
| SlaveArray      | array (natural range <>) of SlaveType                                                                                                                          |             |
| MasterStateType | (M_WAIT_REQ_S,<br><span style="padding-left:20px"> M_WAIT_READYS_S,<br><span style="padding-left:20px"> M_WAIT_REQ_FALL_S)                                     |             |
| MasterType      |                                                                                                                                                                |             |
| MasterArray     | array (natural range <>) of MasterType                                                                                                                         |             |
| RegType         |                                                                                                                                                                |             |
| AxiStatusArray  | array (natural range <>) of AxiLiteStatusType                                                                                                                  |             |
## Processes
- comb: ( axiClkRst, mAxiReadSlaves, mAxiWriteSlaves, r, sAxiReadMasters, sAxiWriteMasters )
- seq: ( axiClk )
