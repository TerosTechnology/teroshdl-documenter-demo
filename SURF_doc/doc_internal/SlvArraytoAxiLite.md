# Entity: SlvArraytoAxiLite

- **File**: SlvArraytoAxiLite.vhd
## Diagram

![Diagram](SlvArraytoAxiLite.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: SLV array to AXI-Lite Master Bridge
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type       | Value              | Description               |
| ------------ | ---------- | ------------------ | ------------------------- |
| TPD_G        | time       | 1 ns               |                           |
| COMMON_CLK_G | boolean    | false              | Set true if axilClk = clk |
| SIZE_G       | positive   | 1                  |                           |
| ADDR_G       | Slv32Array | (0 => x"00000000") |                           |
## Ports

| Port name       | Direction | Type                          | Description               |
| --------------- | --------- | ----------------------------- | ------------------------- |
| clk             | in        | sl                            | SLV Array Interface       |
| rst             | in        | sl                            |                           |
| input           | in        | Slv32Array(SIZE_G-1 downto 0) |                           |
| axilClk         | in        | sl                            | AXI-Lite Master Interface |
| axilRst         | in        | sl                            |                           |
| axilReadMaster  | out       | AxiLiteReadMasterType         |                           |
| axilReadSlave   | in        | AxiLiteReadSlaveType          |                           |
| axilWriteMaster | out       | AxiLiteWriteMasterType        |                           |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType         |                           |
## Signals

| Name  | Type                          | Description |
| ----- | ----------------------------- | ----------- |
| r     | RegType                       |             |
| rin   | RegType                       |             |
| inSlv | Slv32Array(SIZE_G-1 downto 0) |             |
| ack   | AxiLiteAckType                |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                       | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       cnt   => 0,<br><span style="padding-left:20px">       valid => (others => '0'),<br><span style="padding-left:20px">       inSlv => (others => (others => '0')),<br><span style="padding-left:20px">       req   => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       state => IDLE_S) |             |
## Types

| Name      | Type                                                   | Description |
| --------- | ------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_S)  |             |
| RegType   |                                                        |             |
## Processes
- comb: ( ack, axilRst, inSlv, r )
- seq: ( axilClk )
## Instantiations

- U_AxiLiteMaster: surf.AxiLiteMaster
