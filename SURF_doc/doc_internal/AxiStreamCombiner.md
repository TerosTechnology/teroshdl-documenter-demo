# Entity: AxiStreamCombiner

## Diagram

![Diagram](AxiStreamCombiner.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Combines multiple "narrower" buses into a "wide" AXI stream bus
Note: This module does NOT support interleaving of TDEST
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name        | Type                | Value | Description |
| ------------------- | ------------------- | ----- | ----------- |
| TPD_G               | time                | 1 ns  |             |
| LANES_G             | positive            | 4     |             |
| SLAVE_AXI_CONFIG_G  | AxiStreamConfigType |       |             |
| MASTER_AXI_CONFIG_G | AxiStreamConfigType |       |             |
## Ports

| Port name    | Direction | Type                                     | Description     |
| ------------ | --------- | ---------------------------------------- | --------------- |
| axisClk      | in        | sl                                       | Clock and Reset |
| axisRst      | in        | sl                                       |                 |
| sAxisMasters | in        | AxiStreamMasterArray(LANES_G-1 downto 0) | Slave Ports     |
| sAxisSlaves  | out       | AxiStreamSlaveArray (LANES_G-1 downto 0) |                 |
| mAxisMaster  | out       | AxiStreamMasterType                      | Master Port     |
| mAxisSlave   | in        | AxiStreamSlaveType                       |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SEQ_C      | slv(15 downto 8) |  x"55"                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| REG_INIT_C | RegType          |  (       master  => axiStreamMasterInit(MASTER_AXI_CONFIG_G),<br><span style="padding-left:20px">       state   => SOF_S,<br><span style="padding-left:20px">       sof     => '0',<br><span style="padding-left:20px">       first   => (others => '1'),<br><span style="padding-left:20px">       discard => (others => '0'),<br><span style="padding-left:20px">       slaves  => (others => AXI_STREAM_SLAVE_INIT_C)) |             |
## Types

| Name       | Type                                                                                            | Description |
| ---------- | ----------------------------------------------------------------------------------------------- | ----------- |
| FrameState | ( SOF_S,<br><span style="padding-left:20px"> EOF_S,<br><span style="padding-left:20px"> ERR_S)  |             |
| RegType    |                                                                                                 |             |
## Processes
- comb: ( axisRst, mAxisSlave, r, sAxisMasters )
- seq: ( axisClk )
