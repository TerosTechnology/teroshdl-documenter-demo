# Entity: SaciMultiPixel

- **File**: SaciMultiPixel.vhd
## Diagram

![Diagram](SaciMultiPixel.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SACI Multi-pixel Module
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

| Generic name     | Type                 | Value       | Description |
| ---------------- | -------------------- | ----------- | ----------- |
| TPD_G            | time                 | 1 ns        |             |
| MASK_REG_ADDR_G  | slv(31 downto 0)     | x"00000034" |             |
| SACI_BASE_ADDR_G | slv(31 downto 0)     | x"02000000" |             |
| SACI_NUM_CHIPS_G | natural range 1 to 4 | 4           |             |
## Ports

| Port name        | Direction | Type                   | Description          |
| ---------------- | --------- | ---------------------- | -------------------- |
| axilClk          | in        | sl                     |                      |
| axilRst          | in        | sl                     |                      |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType | AXI lite slave port  |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType  |                      |
| sAxilReadMaster  | in        | AxiLiteReadMasterType  |                      |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType   |                      |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType | AXI lite master port |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType  |                      |
| mAxilReadMaster  | out       | AxiLiteReadMasterType  |                      |
| mAxilReadSlave   | in        | AxiLiteReadSlaveType   |                      |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       globalMultiPix       => MULTI_PIXEL_WRITE_INIT_C,<br><span style="padding-left:20px">       localMultiPix        => MULTI_PIXEL_WRITE_INIT_C,<br><span style="padding-left:20px">       asicMask             => (others=>'0'),<br><span style="padding-left:20px">       writeCnt             => (others=>'0'),<br><span style="padding-left:20px">       state                => S_IDLE_C,<br><span style="padding-left:20px">       timer                => (others => '1'),<br><span style="padding-left:20px">       timeout              => '0',<br><span style="padding-left:20px">       fail                 => '0',<br><span style="padding-left:20px">       mAxilWriteMaster  => AXI_LITE_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       mAxilReadMaster   => AXI_LITE_READ_MASTER_INIT_C,<br><span style="padding-left:20px">       sAxilWriteSlave   => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       sAxilReadSlave    => AXI_LITE_READ_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                               | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | (S_IDLE_C,<br><span style="padding-left:20px"> S_IS_ASIC_C,<br><span style="padding-left:20px"> S_WRITE_C,<br><span style="padding-left:20px"> S_WRITE_AXI_C,<br><span style="padding-left:20px"> S_READ_C,<br><span style="padding-left:20px"> S_READ_AXI_C,<br><span style="padding-left:20px"> S_DONE_OK_C,<br><span style="padding-left:20px"> S_DONE_FAIL_C)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                    |             |
## Processes
- comb: ( axilRst, sAxilReadMaster, sAxilWriteMaster, mAxilReadSlave, mAxilWriteSlave, r )
- seq: ( axilClk )
