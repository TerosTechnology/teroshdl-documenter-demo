# Entity: SaciPrepRdout

## Diagram

![Diagram](SaciPrepRdout.svg "Diagram")
## Description

Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
Company    : SLAC National Accelerator Laboratory
Description: The AXI lite master to issue SACI prepare for readout command
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type                 | Value       | Description |
| ---------------- | -------------------- | ----------- | ----------- |
| TPD_G            | time                 | 1 ns        |             |
| MASK_REG_ADDR_G  | slv(31 downto 0)     | x"00000034" |             |
| MASK_REG_READ_G  | boolean              | true        |             |
| SACI_BASE_ADDR_G | slv(31 downto 0)     | x"02000000" |             |
| SACI_NUM_CHIPS_G | natural range 1 to 4 | 4           |             |
## Ports

| Port name        | Direction | Type                             | Description                                     |
| ---------------- | --------- | -------------------------------- | ----------------------------------------------- |
| axilClk          | in        | sl                               |                                                 |
| axilRst          | in        | sl                               |                                                 |
| prepRdoutReq     | in        | sl                               | Prepare for readout req/ack                     |
| prepRdoutAck     | out       | sl                               |                                                 |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType           | Optional AXI lite slave port for status readout |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType            |                                                 |
| sAxilReadMaster  | in        | AxiLiteReadMasterType            |                                                 |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType             |                                                 |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType           | AXI lite master port for command issue          |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType            |                                                 |
| mAxilReadMaster  | out       | AxiLiteReadMasterType            |                                                 |
| mAxilReadSlave   | in        | AxiLiteReadSlaveType             |                                                 |
| asicMask         | in        | slv(SACI_NUM_CHIPS_G-1 downto 0) | optianally provide ASIC mask                    |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       asicMask          => (others=>'0'),<br><span style="padding-left:20px">       state             => S_IDLE_C,<br><span style="padding-left:20px">       timer             => (others => '1'),<br><span style="padding-left:20px">       asicCnt           =>  0,<br><span style="padding-left:20px">       rdTimeout         => (others=>'0'),<br><span style="padding-left:20px">       rdFail            => (others=>'0'),<br><span style="padding-left:20px">       wrTimeout         => (others=>'0'),<br><span style="padding-left:20px">       wrFail            => (others=>'0'),<br><span style="padding-left:20px">       prepRdoutAck      => '0',<br><span style="padding-left:20px">       mAxilWriteMaster  => AXI_LITE_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       mAxilReadMaster   => AXI_LITE_READ_MASTER_INIT_C,<br><span style="padding-left:20px">       sAxilWriteSlave   => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       sAxilReadSlave    => AXI_LITE_READ_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                           | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (S_IDLE_C,<br><span style="padding-left:20px"> S_IS_ASIC_C,<br><span style="padding-left:20px"> S_WRITE_C,<br><span style="padding-left:20px"> S_WRITE_AXI_C,<br><span style="padding-left:20px"> S_READ_C,<br><span style="padding-left:20px"> S_READ_AXI_C)  |             |
| RegType   |                                                                                                                                                                                                                                                                |             |
## Functions
- asicBaseAddr <font id="function_arguments">(asic : natural) </font> <font id="function_return">return slv </font>
## Processes
- comb: ( axilRst, sAxilReadMaster, sAxilWriteMaster, mAxilReadSlave, mAxilWriteSlave, r, prepRdoutReq, asicMask )
- seq: ( axilClk )
