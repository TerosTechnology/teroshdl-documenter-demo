# Entity: AxiStreamFlush

- **File**: AxiStreamFlush.vhd
## Diagram

![Diagram](AxiStreamFlush.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Block to flush AXI Stream frames, being mindfull of frame boundaries.
This module is designed to feed into an AxiStreamFifo using pause to determine
backpressure situations.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                | Value | Description |
| ------------- | ------------------- | ----- | ----------- |
| TPD_G         | time                | 1 ns  |             |
| AXIS_CONFIG_G | AxiStreamConfigType |       |             |
| SSI_EN_G      | boolean             | false |             |
## Ports

| Port name   | Direction | Type                | Description     |
| ----------- | --------- | ------------------- | --------------- |
| axisClk     | in        | sl                  | Clock and reset |
| axisRst     | in        | sl                  |                 |
| flushEn     | in        | sl                  | Flush enable    |
| sAxisMaster | in        | AxiStreamMasterType | Slave Port      |
| sAxisSlave  | out       | AxiStreamSlaveType  |                 |
| mAxisMaster | out       | AxiStreamMasterType | Master Port     |
| mAxisCtrl   | in        | AxiStreamCtrlType   |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                     | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state    => IDLE_S,<br><span style="padding-left:20px">       obMaster => axiStreamMasterInit(AXIS_CONFIG_G),<br><span style="padding-left:20px">       ibSlave  => AXI_STREAM_SLAVE_INIT_C    ) |             |
## Types

| Name      | Type                                                                                                 | Description |
| --------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> FLUSH_S )  |             |
| RegType   |                                                                                                      |             |
## Processes
- comb: ( mAxisCtrl, sAxisMaster, axisRst, flushEn, r )
- seq: ( axisClk )
