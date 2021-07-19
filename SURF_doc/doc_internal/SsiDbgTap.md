# Entity: SsiDbgTap

- **File**: SsiDbgTap.vhd
## Diagram

![Diagram](SsiDbgTap.svg "Diagram")
## Description

Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
Company    : SLAC National Accelerator Laboratory
Description: SSI debug tap, intended to be connect to chipscope for debugging
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                | Value | Description |
| ------------ | ------------------- | ----- | ----------- |
| TPD_G        | time                | 1 ns  |             |
| CNT_WIDTH_G  | positive            | 16    |             |
| AXI_CONFIG_G | AxiStreamConfigType |       |             |
## Ports

| Port name  | Direction | Type                | Description |
| ---------- | --------- | ------------------- | ----------- |
| axisClk    | in        | sl                  | Slave Port  |
| axisRst    | in        | sl                  |             |
| axisMaster | in        | AxiStreamMasterType |             |
| axisSlave  | in        | AxiStreamSlaveType  |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                      | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       cnt   => (others => '0'),<br><span style="padding-left:20px">       copy  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state => IDLE_S) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> MOVE_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( axisMaster, axisRst, axisSlave, r )
- seq: ( axisClk )
