# Entity: AxiStreamPipeline

## Diagram

![Diagram](AxiStreamPipeline.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:   This module is used to sync a AxiStream bus
               either as a pass through or with pipeline register stages.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type     | Value | Description              |
| ----------------- | -------- | ----- | ------------------------ |
| TPD_G             | time     | 1 ns  |                          |
| SIDE_BAND_WIDTH_G | positive | 1     | General purpose sideband |
| PIPE_STAGES_G     | natural  | 0     |                          |
## Ports

| Port name   | Direction | Type                              | Description     |
| ----------- | --------- | --------------------------------- | --------------- |
| axisClk     | in        | sl                                | Clock and Reset |
| axisRst     | in        | sl                                |                 |
| sAxisMaster | in        | AxiStreamMasterType               | Slave Port      |
| sSideBand   | in        | slv(SIDE_BAND_WIDTH_G-1 downto 0) |                 |
| sAxisSlave  | out       | AxiStreamSlaveType                |                 |
| mAxisMaster | out       | AxiStreamMasterType               | Master Port     |
| mSideBand   | out       | slv(SIDE_BAND_WIDTH_G-1 downto 0) |                 |
| mAxisSlave  | in        | AxiStreamSlaveType                |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                                                                                 | Description |
| ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PIPE_STAGES_C | natural |  PIPE_STAGES_G+1                                                                                                                                                                                                                      |             |
| REG_INIT_C    | RegType |  (       sAxisSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       mAxisMaster => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       mSideBand   => (others => (others => '0'))) |             |
## Types

| Name          | Type                                                           | Description |
| ------------- | -------------------------------------------------------------- | ----------- |
| SideBandArray | array (natural range <>) of slv(SIDE_BAND_WIDTH_G-1 downto 0)  |             |
| RegType       |                                                                |             |
