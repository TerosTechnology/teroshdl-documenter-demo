# Entity: AxiAd9467Reg

- **File**: AxiAd9467Reg.vhd
## Diagram

![Diagram](AxiAd9467Reg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AD9467 AXI-Lite Register Access Module
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

| Generic name       | Type                  | Value               | Description |
| ------------------ | --------------------- | ------------------- | ----------- |
| TPD_G              | time                  | 1 ns                |             |
| DEMUX_INIT_G       | sl                    | '0'                 |             |
| DELAY_INIT_G       | Slv5Array(0 to 7)     | (others => "00000") |             |
| STATUS_CNT_WIDTH_G | natural range 1 to 32 | 32                  |             |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| axiClk         | in        | sl                     | AXI-Lite Register Interface (axiClk domain) |
| axiRst         | in        | sl                     |                                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  |                                             |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
| status         | in        | AxiAd9467StatusType    | Register Inputs/Outputs (axiClk domain)     |
| config         | out       | AxiAd9467ConfigType    |                                             |
| adcClk         | in        | sl                     | Global Signals                              |
| adcRst         | in        | sl                     |                                             |
| refClk200MHz   | in        | sl                     |                                             |
## Signals

| Name   | Type                | Description |
| ------ | ------------------- | ----------- |
| r      | RegType             |             |
| rin    | RegType             |             |
| syncIn | AxiAd9467StatusType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                             | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       AXI_AD9467_CONFIG_INIT_C,<br><span style="padding-left:20px">       IDLE_S,<br><span style="padding-left:20px">       AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType   |                                                                                                  |             |
## Functions
- CompressAddressSpace <font id="function_arguments">(vec : slv(7 downto 0)) </font> <font id="function_return">return slv </font>
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, r, syncIn )
- seq: ( axiClk )
## Instantiations

- SyncIn_delay_dmux: surf.Synchronizer
- SyncOut_delayIn_load: surf.RstSync
- SyncOut_delayIn_rst: surf.RstSync
- SyncIn_pllLocked: surf.Synchronizer
- SyncIn_delayOut_rdy: surf.Synchronizer
