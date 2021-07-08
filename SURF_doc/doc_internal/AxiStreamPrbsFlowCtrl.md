# Entity: AxiStreamPrbsFlowCtrl

## Diagram

![Diagram](AxiStreamPrbsFlowCtrl.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Generates pseudo-random back pressure
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                 | Value                             | Description |
| ------------- | -------------------- | --------------------------------- | ----------- |
| TPD_G         | time                 | 1 ns                              |             |
| PIPE_STAGES_G | natural range 0 to 1 | 0                                 |             |
| SEED_G        | slv(31 downto 0)     | x"AAAA_5555"                      |             |
| PRBS_TAPS_G   | NaturalArray         | (0 => 31, 1 => 6, 2 => 2, 3 => 1) |             |
## Ports

| Port name   | Direction | Type                | Description |
| ----------- | --------- | ------------------- | ----------- |
| clk         | in        | sl                  |             |
| rst         | in        | sl                  |             |
| threshold   | in        | slv(31 downto 0)    |             |
| sAxisMaster | in        | AxiStreamMasterType | Slave Port  |
| sAxisSlave  | out       | AxiStreamSlaveType  |             |
| mAxisMaster | out       | AxiStreamMasterType | Master Port |
| mAxisSlave  | in        | AxiStreamSlaveType  |             |
## Signals

| Name     | Type                | Description |
| -------- | ------------------- | ----------- |
| r        | RegType             |             |
| rin      | RegType             |             |
| rxMaster | AxiStreamMasterType |             |
| rxSlave  | AxiStreamSlaveType  |             |
| txMaster | AxiStreamMasterType |             |
| txSlave  | AxiStreamSlaveType  |             |
| pause    | sl                  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                             | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       randomData => SEED_G,<br><span style="padding-left:20px">       rxSlave    => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       txMaster   => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( pause, r, rst, rxMaster, txSlave )
**Description**
 (a <  b)

- seq: ( clk )
## Instantiations

- U_DspComparator: surf.DspComparator
- U_Pipe: surf.AxiStreamPipeline
