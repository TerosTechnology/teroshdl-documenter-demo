# Entity: ClinkReg

- **File**: ClinkReg.vhd
## Diagram

![Diagram](ClinkReg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 CameraLink Registers
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

| Generic name | Type                 | Value | Description |
| ------------ | -------------------- | ----- | ----------- |
| TPD_G        | time                 | 1 ns  |             |
| CHAN_COUNT_G | integer range 1 to 2 | 1     |             |
## Ports

| Port name       | Direction | Type                          | Description        |
| --------------- | --------- | ----------------------------- | ------------------ |
| chanStatus      | in        | ClChanStatusArray(1 downto 0) |                    |
| linkStatus      | in        | ClLinkStatusArray(2 downto 0) |                    |
| chanConfig      | out       | ClChanConfigArray(1 downto 0) |                    |
| linkConfig      | out       | ClLinkConfigType              |                    |
| sysClk          | in        | sl                            | Axi-Lite Interface |
| sysRst          | in        | sl                            |                    |
| axilReadMaster  | in        | AxiLiteReadMasterType         |                    |
| axilReadSlave   | out       | AxiLiteReadSlaveType          |                    |
| axilWriteMaster | in        | AxiLiteWriteMasterType        |                    |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType         |                    |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       locked         => "000",<br><span style="padding-left:20px">       lockCnt        => (others => x"00"),<br><span style="padding-left:20px">       chanConfig     => (others => CL_CHAN_CONFIG_INIT_C),<br><span style="padding-left:20px">       linkConfig     => CL_LINK_CONFIG_INIT_C,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axilReadMaster, axilWriteMaster, chanStatus, linkStatus, r,
                   sysRst )
- seq: ( sysClk )
