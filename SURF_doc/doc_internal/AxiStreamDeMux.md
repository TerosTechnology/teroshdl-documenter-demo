# Entity: AxiStreamDeMux

- **File**: AxiStreamDeMux.vhd
## Diagram

![Diagram](AxiStreamDeMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Block to connect a single incoming AXI stream to multiple outgoing AXI
streams based upon the incoming tDest value.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                   | Value             | Description              |
| -------------- | ---------------------- | ----------------- | ------------------------ |
| TPD_G          | time                   | 1 ns              |                          |
| NUM_MASTERS_G  | integer range 1 to 256 | 12                |                          |
| MODE_G         | string                 | "INDEXED"         | Or "ROUTED" Or "DYNAMIC" |
| TDEST_ROUTES_G | slv8Array              | (0 => "--------") | Only used in ROUTED mode |
| PIPE_STAGES_G  | integer range 0 to 16  | 0                 |                          |
| TDEST_HIGH_G   | integer range 0 to 7   | 7                 |                          |
| TDEST_LOW_G    | integer range 0 to 7   | 0                 |                          |
## Ports

| Port name         | Direction | Type                                           | Description                                             |
| ----------------- | --------- | ---------------------------------------------- | ------------------------------------------------------- |
| axisClk           | in        | sl                                             | Clock and reset                                         |
| axisRst           | in        | sl                                             |                                                         |
| dynamicRouteMasks | in        | slv8Array(NUM_MASTERS_G-1 downto 0)            | Dynamic Route Table (only used when MODE_G = "DYNAMIC") |
| dynamicRouteDests | in        | slv8Array(NUM_MASTERS_G-1 downto 0)            |                                                         |
| sAxisMaster       | in        | AxiStreamMasterType                            | Slave                                                   |
| sAxisSlave        | out       | AxiStreamSlaveType                             |                                                         |
| mAxisMasters      | out       | AxiStreamMasterArray(NUM_MASTERS_G-1 downto 0) | Masters                                                 |
| mAxisSlaves       | in        | AxiStreamSlaveArray(NUM_MASTERS_G-1 downto 0)  |                                                         |
## Signals

| Name            | Type                                           | Description |
| --------------- | ---------------------------------------------- | ----------- |
| pipeAxisMasters | AxiStreamMasterArray(NUM_MASTERS_G-1 downto 0) |             |
| pipeAxisSlaves  | AxiStreamSlaveArray(NUM_MASTERS_G-1 downto 0)  |             |
| r               | RegType                                        |             |
| rin             | RegType                                        |             |
## Constants

| Name       | Type    | Value                                                                                                                                   | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       slave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       masters => (others => AXI_STREAM_MASTER_INIT_C)) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axisRst, dynamicRouteDests, dynamicRouteMasks, pipeAxisSlaves, r, sAxisMaster )
- seq: ( axisClk )
