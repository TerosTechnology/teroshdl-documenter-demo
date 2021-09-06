# Entity: MicroblazeBasicCoreWrapper

- **File**: MicroblazeBasicCoreWrapper.vhd
## Diagram

![Diagram](MicroblazeBasicCoreWrapper.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for Microblaze Basic Core for "90% case"
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

| Generic name    | Type    | Value | Description                                                      |
| --------------- | ------- | ----- | ---------------------------------------------------------------- |
| TPD_G           | time    | 1 ns  |                                                                  |
| AXIL_RESP_G     | boolean | false |                                                                  |
| AXIL_ADDR_MSB_G | boolean | false |  false = [0x00000000:0x7FFFFFFF], true = [0x80000000:0xFFFFFFFF] |
| AXIL_ADDR_SEL_G | boolean | false |                                                                  |
## Ports

| Port name        | Direction | Type                   | Description               |
| ---------------- | --------- | ---------------------- | ------------------------- |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType | Master AXI-Lite Interface |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType  |                           |
| mAxilReadMaster  | out       | AxiLiteReadMasterType  |                           |
| mAxilReadSlave   | in        | AxiLiteReadSlaveType   |                           |
| sAxisMaster      | in        | AxiStreamMasterType    | Master AXIS Interface     |
| sAxisSlave       | out       | AxiStreamSlaveType     |                           |
| mAxisMaster      | out       | AxiStreamMasterType    | Slave AXIS Interface      |
| mAxisSlave       | in        | AxiStreamSlaveType     |                           |
| interrupt        | in        | slv(7 downto 0)        | Interrupt Interface       |
| clk              | in        | sl                     | Clock and Reset           |
| pllLock          | in        | sl                     |                           |
| rst              | in        | sl                     |                           |
## Signals

| Name     | Type                | Description |
| -------- | ------------------- | ----------- |
| awaddr   | slv(31 downto 0)    |             |
| araddr   | slv(31 downto 0)    |             |
| bresp    | slv(1 downto 0)     |             |
| rresp    | slv(1 downto 0)     |             |
| addr_sel | sl                  |             |
| txMaster | AxiStreamMasterType |             |
| txSlave  | AxiStreamSlaveType  |             |
## Instantiations

- U_Microblaze: component MicroblazeBasicCore
- U_InsertSOF: surf.SsiInsertSof
