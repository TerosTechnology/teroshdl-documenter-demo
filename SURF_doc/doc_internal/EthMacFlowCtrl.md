# Entity: EthMacFlowCtrl

- **File**: EthMacFlowCtrl.vhd
## Diagram

![Diagram](EthMacFlowCtrl.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: ETH MAC Flow Control Module
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
| BYP_EN_G     | boolean               | false |             |
| VLAN_EN_G    | boolean               | false |             |
| VLAN_SIZE_G  | positive range 1 to 8 | 1     |             |
## Ports

| Port name | Direction | Type                                       | Description     |
| --------- | --------- | ------------------------------------------ | --------------- |
| ethClk    | in        | sl                                         | Clock and Reset |
| ethRst    | in        | sl                                         |                 |
| primCtrl  | in        | AxiStreamCtrlType                          | Inputs          |
| bypCtrl   | in        | AxiStreamCtrlType                          |                 |
| vlanCtrl  | in        | AxiStreamCtrlArray(VLAN_SIZE_G-1 downto 0) |                 |
| flowCtrl  | out       | AxiStreamCtrlType                          | Output          |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                        | Description |
| ---------- | ------- | -------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       flowCtrl => AXI_STREAM_CTRL_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( bypCtrl, ethRst, primCtrl, r, vlanCtrl )
- seq: ( ethClk )
