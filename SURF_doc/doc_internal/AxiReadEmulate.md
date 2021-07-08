# Entity: AxiReadEmulate

## Diagram

![Diagram](AxiReadEmulate.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI4 Read Emulation Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type          | Value | Description |
| ------------ | ------------- | ----- | ----------- |
| TPD_G        | time          | 1 ns  |             |
| LATENCY_G    | natural       | 31    |             |
| AXI_CONFIG_G | AxiConfigType |       |             |
| SIM_DEBUG_G  | boolean       | false |             |
## Ports

| Port name     | Direction | Type              | Description   |
| ------------- | --------- | ----------------- | ------------- |
| axiClk        | in        | sl                | Clock/Reset   |
| axiRst        | in        | sl                |               |
| axiReadMaster | in        | AxiReadMasterType | AXI Interface |
| axiReadSlave  | out       | AxiReadSlaveType  |               |
## Signals

| Name          | Type              | Description |
| ------------- | ----------------- | ----------- |
| r             | RegType           |             |
| rin           | RegType           |             |
| intReadMaster | AxiReadMasterType |             |
| intReadSlave  | AxiReadSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                              | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       latency => 0,<br><span style="padding-left:20px">       state   => IDLE_S,<br><span style="padding-left:20px">       cnt     => (others => '0'),<br><span style="padding-left:20px">       iMaster => AXI_READ_MASTER_INIT_C,<br><span style="padding-left:20px">       iSlave  => AXI_READ_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> DATA_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( axiRst, intReadMaster, r )
- seq: ( axiClk )
## Instantiations

- U_AxiReadPathFifo: surf.AxiReadPathFifo
