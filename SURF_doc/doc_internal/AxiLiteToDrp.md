# Entity: AxiLiteToDrp

- **File**: AxiLiteToDrp.vhd
## Diagram

![Diagram](AxiLiteToDrp.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite to Xilinx DRP Bridge
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

| Generic name     | Type                   | Value | Description |
| ---------------- | ---------------------- | ----- | ----------- |
| TPD_G            | time                   | 1 ns  |             |
| COMMON_CLK_G     | boolean                | false |             |
| EN_ARBITRATION_G | boolean                | false |             |
| TIMEOUT_G        | positive               | 4096  |             |
| ADDR_WIDTH_G     | positive range 1 to 32 | 16    |             |
| DATA_WIDTH_G     | positive range 1 to 32 | 16    |             |
## Ports

| Port name       | Direction | Type                         | Description                      |
| --------------- | --------- | ---------------------------- | -------------------------------- |
| axilClk         | in        | sl                           | AXI-Lite Port                    |
| axilRst         | in        | sl                           |                                  |
| axilReadMaster  | in        | AxiLiteReadMasterType        |                                  |
| axilReadSlave   | out       | AxiLiteReadSlaveType         |                                  |
| axilWriteMaster | in        | AxiLiteWriteMasterType       |                                  |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType        |                                  |
| drpClk          | in        | sl                           | DRP Interface                    |
| drpRst          | in        | sl                           |                                  |
| drpGnt          | in        | sl                           |  Used if EN_ARBITRATION_G = true |
| drpReq          | out       | sl                           |  Used if EN_ARBITRATION_G = true |
| drpRdy          | in        | sl                           |                                  |
| drpEn           | out       | sl                           |                                  |
| drpWe           | out       | sl                           |                                  |
| drpUsrRst       | out       | sl                           |                                  |
| drpAddr         | out       | slv(ADDR_WIDTH_G-1 downto 0) |                                  |
| drpDi           | out       | slv(DATA_WIDTH_G-1 downto 0) |                                  |
| drpDo           | in        | slv(DATA_WIDTH_G-1 downto 0) |                                  |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| r           | RegType                |             |
| rin         | RegType                |             |
| readMaster  | AxiLiteReadMasterType  |             |
| readSlave   | AxiLiteReadSlaveType   |             |
| writeMaster | AxiLiteWriteMasterType |             |
| writeSlave  | AxiLiteWriteSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       drpUsrRst  => '1',<br><span style="padding-left:20px">       drpReq     => '0',<br><span style="padding-left:20px">       drpEn      => '0',<br><span style="padding-left:20px">       drpWe      => '0',<br><span style="padding-left:20px">       drpAddr    => (others => '0'),<br><span style="padding-left:20px">       drpDi      => (others => '0'),<br><span style="padding-left:20px">       timer      => 0,<br><span style="padding-left:20px">       writeSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       readSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       state      => IDLE_S) |             |
## Types

| Name      | Type                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType   |                                                                                                  |             |
## Processes
- comb: ( drpDo, drpGnt, drpRdy, drpRst, r, readMaster, writeMaster )
- seq: ( drpClk )
