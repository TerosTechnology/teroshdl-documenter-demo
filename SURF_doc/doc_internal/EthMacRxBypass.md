# Entity: EthMacRxBypass

- **File**: EthMacRxBypass.vhd
## Diagram

![Diagram](EthMacRxBypass.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: RX bypass frame extractor.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type             | Value   | Description |
| -------------- | ---------------- | ------- | ----------- |
| TPD_G          | time             | 1 ns    |             |
| BYP_EN_G       | boolean          | false   |             |
| BYP_ETH_TYPE_G | slv(15 downto 0) | x"0000" |             |
## Ports

| Port name   | Direction | Type                | Description            |
| ----------- | --------- | ------------------- | ---------------------- |
| ethClk      | in        | sl                  | Clock and Reset        |
| ethRst      | in        | sl                  |                        |
| sAxisMaster | in        | AxiStreamMasterType | Incoming data from MAC |
| mPrimMaster | out       | AxiStreamMasterType | Outgoing primary data  |
| mBypMaster  | out       | AxiStreamMasterType | Outgoing bypass data   |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                 | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       mPrimMaster => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       mBypMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state       => IDLE_S) |             |
## Types

| Name      | Type                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> PRIM_S,<br><span style="padding-left:20px"> BYP_S)  |             |
| RegType   |                                                                                                   |             |
