# Entity: AxiStreamResize

- **File**: AxiStreamResize.vhd
## Diagram

![Diagram](AxiStreamResize.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Block to resize AXI Streams. Re-sizing is always little endian.
 Resizer should not be used when interleaving tDests
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

| Generic name        | Type                | Value | Description                     |
| ------------------- | ------------------- | ----- | ------------------------------- |
| TPD_G               | time                | 1 ns  | General Configurations          |
| READY_EN_G          | boolean             | true  |                                 |
| PIPE_STAGES_G       | natural             | 0     |                                 |
| SIDE_BAND_WIDTH_G   | positive            | 1     |  General purpose sideband       |
| SLAVE_AXI_CONFIG_G  | AxiStreamConfigType |       | AXI Stream Port Configurations  |
| MASTER_AXI_CONFIG_G | AxiStreamConfigType |       |                                 |
## Ports

| Port name   | Direction | Type                              | Description     |
| ----------- | --------- | --------------------------------- | --------------- |
| axisClk     | in        | sl                                | Clock and reset |
| axisRst     | in        | sl                                |                 |
| sAxisMaster | in        | AxiStreamMasterType               | Slave Port      |
| sSideBand   | in        | slv(SIDE_BAND_WIDTH_G-1 downto 0) |                 |
| sAxisSlave  | out       | AxiStreamSlaveType                |                 |
| mAxisMaster | out       | AxiStreamMasterType               | Master Port     |
| mSideBand   | out       | slv(SIDE_BAND_WIDTH_G-1 downto 0) |                 |
| mAxisSlave  | in        | AxiStreamSlaveType                |                 |
## Signals

| Name           | Type                              | Description |
| -------------- | --------------------------------- | ----------- |
| r              | RegType                           |             |
| rin            | RegType                           |             |
| pipeAxisMaster | AxiStreamMasterType               |             |
| pipeSideBand   | slv(SIDE_BAND_WIDTH_G-1 downto 0) |             |
| pipeAxisSlave  | AxiStreamSlaveType                |             |
## Constants

| Name        | Type     | Value                                                                                                                                                                                                                                                                                              | Description |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SLV_BYTES_C | positive |  SLAVE_AXI_CONFIG_G.TDATA_BYTES_C                                                                                                                                                                                                                                                                  |             |
| MST_BYTES_C | positive |  MASTER_AXI_CONFIG_G.TDATA_BYTES_C                                                                                                                                                                                                                                                                 |             |
| SLV_USER_C  | positive |  ite(SLAVE_AXI_CONFIG_G.TUSER_BITS_C /= 0,<br><span style="padding-left:20px"> SLAVE_AXI_CONFIG_G.TUSER_BITS_C,<br><span style="padding-left:20px"> 1)                                                                                                                                             |             |
| MST_USER_C  | positive |  ite(MASTER_AXI_CONFIG_G.TUSER_BITS_C /= 0,<br><span style="padding-left:20px"> MASTER_AXI_CONFIG_G.TUSER_BITS_C,<br><span style="padding-left:20px"> 1)                                                                                                                                           |             |
| COUNT_C     | positive |  ite(SLV_BYTES_C > MST_BYTES_C,<br><span style="padding-left:20px"> SLV_BYTES_C / MST_BYTES_C,<br><span style="padding-left:20px"> MST_BYTES_C / SLV_BYTES_C)                                                                                                                                      |             |
| REG_INIT_C  | RegType  |  (       count    => (others => '0'),<br><span style="padding-left:20px">       obMaster => axiStreamMasterInit(MASTER_AXI_CONFIG_G),<br><span style="padding-left:20px">       sideBand => (others => '0'),<br><span style="padding-left:20px">       ibSlave  => AXI_STREAM_SLAVE_INIT_C       ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( pipeAxisSlave, r, sAxisMaster, sSideBand )
- seq: ( axisClk )
## Instantiations

- AxiStreamPipeline_1: surf.AxiStreamPipeline
**Description**
 Optional output pipeline registers to ease timing

