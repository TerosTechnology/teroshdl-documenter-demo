# Entity: AxiWriteEmulate

- **File**: AxiWriteEmulate.vhd
## Diagram

![Diagram](AxiWriteEmulate.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI4 Write Emulation Module
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

| Port name      | Direction | Type               | Description   |
| -------------- | --------- | ------------------ | ------------- |
| axiClk         | in        | sl                 | Clock/Reset   |
| axiRst         | in        | sl                 |               |
| axiWriteMaster | in        | AxiWriteMasterType | AXI Interface |
| axiWriteSlave  | out       | AxiWriteSlaveType  |               |
## Signals

| Name           | Type               | Description |
| -------------- | ------------------ | ----------- |
| r              | RegType            |             |
| rin            | RegType            |             |
| intWriteMaster | AxiWriteMasterType |             |
| intWriteSlave  | AxiWriteSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                              | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       latency => 0,<br><span style="padding-left:20px">       cnt     => (others=>'0'),<br><span style="padding-left:20px">       state   => IDLE_S,<br><span style="padding-left:20px">       iMaster => AXI_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       iSlave  => AXI_WRITE_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                           | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> DATA_S,<br><span style="padding-left:20px"> WAIT_S,<br><span style="padding-left:20px"> RESP_S)  |             |
| RegType   |                                                                                                                                                |             |
## Processes
- comb: ( axiRst, intWriteMaster, r )
- seq: ( axiClk )
## Instantiations

- U_AxiWritePathFifo: surf.AxiWritePathFifo
