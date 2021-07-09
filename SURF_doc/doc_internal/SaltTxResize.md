# Entity: SaltTxResize

## Diagram

![Diagram](SaltTxResize.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: SALT TX Engine Resizer Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name | Direction | Type                | Description          |
| --------- | --------- | ------------------- | -------------------- |
| clk       | in        | sl                  | Clock and Reset      |
| rst       | in        | sl                  |                      |
| rxMaster  | in        | AxiStreamMasterType | AXI Stream Interface |
| rxSlave   | out       | AxiStreamSlaveType  |                      |
| txEn      | out       | sl                  | GMII Interface       |
| txData    | out       | slv(7 downto 0)     |                      |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                     | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       txEn    => '0',<br><span style="padding-left:20px">       txData  => (others => '0'),<br><span style="padding-left:20px">       idx     => 0,<br><span style="padding-left:20px">       gapCnt  => 0,<br><span style="padding-left:20px">       rxSlave => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state   => MOVE_S) |             |
## Types

| Name      | Type                                                        | Description |
| --------- | ----------------------------------------------------------- | ----------- |
| StateType | ( MOVE_S,<br><span style="padding-left:20px"> INTER_GAP_S)  |             |
| RegType   |                                                             |             |
## Processes
- comb: ( r, rst, rxMaster )
- seq: ( clk )
