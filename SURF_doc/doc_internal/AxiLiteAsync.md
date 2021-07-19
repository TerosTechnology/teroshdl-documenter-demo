# Entity: AxiLiteAsync

- **File**: AxiLiteAsync.vhd
## Diagram

![Diagram](AxiLiteAsync.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Asynchronous bridge for AXI Lite bus. Allows AXI transactions to cross
a clock boundary.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type                  | Value             | Description |
| ---------------- | --------------------- | ----------------- | ----------- |
| TPD_G            | time                  | 1 ns              |             |
| AXI_ERROR_RESP_G | slv(1 downto 0)       | AXI_RESP_SLVERR_C |             |
| COMMON_CLK_G     | boolean               | false             |             |
| NUM_ADDR_BITS_G  | natural               | 32                |             |
| PIPE_STAGES_G    | integer range 0 to 16 | 0                 |             |
## Ports

| Port name       | Direction | Type                   | Description |
| --------------- | --------- | ---------------------- | ----------- |
| sAxiClk         | in        | sl                     | Slave Port  |
| sAxiClkRst      | in        | sl                     |             |
| sAxiReadMaster  | in        | AxiLiteReadMasterType  |             |
| sAxiReadSlave   | out       | AxiLiteReadSlaveType   |             |
| sAxiWriteMaster | in        | AxiLiteWriteMasterType |             |
| sAxiWriteSlave  | out       | AxiLiteWriteSlaveType  |             |
| mAxiClk         | in        | sl                     | Master Port |
| mAxiClkRst      | in        | sl                     |             |
| mAxiReadMaster  | out       | AxiLiteReadMasterType  |             |
| mAxiReadSlave   | in        | AxiLiteReadSlaveType   |             |
| mAxiWriteMaster | out       | AxiLiteWriteMasterType |             |
| mAxiWriteSlave  | in        | AxiLiteWriteSlaveType  |             |
## Signals

| Name                      | Type                            | Description                    |
| ------------------------- | ------------------------------- | ------------------------------ |
| s2mRst                    | sl                              | Slave rst sync'd to master clk |
| m2sRst                    | sl                              | Master rst sync'd to slave clk |
| readSlaveToMastDin        | slv(NUM_ADDR_BITS_G+2 downto 0) |                                |
| readSlaveToMastDout       | slv(NUM_ADDR_BITS_G+2 downto 0) |                                |
| readSlaveToMastFull       | sl                              |                                |
| readSlaveToMastValid      | sl                              |                                |
| readSlaveToMastRead       | sl                              |                                |
| readSlaveToMastWrite      | sl                              |                                |
| readMastToSlaveDin        | slv(33 downto 0)                |                                |
| readMastToSlaveDout       | slv(33 downto 0)                |                                |
| readMastToSlaveFull       | sl                              |                                |
| readMastToSlaveValid      | sl                              |                                |
| readMastToSlaveRead       | sl                              |                                |
| readMastToSlaveWrite      | sl                              |                                |
| writeAddrSlaveToMastDin   | slv(NUM_ADDR_BITS_G+2 downto 0) |                                |
| writeAddrSlaveToMastDout  | slv(NUM_ADDR_BITS_G+2 downto 0) |                                |
| writeAddrSlaveToMastFull  | sl                              |                                |
| writeAddrSlaveToMastValid | sl                              |                                |
| writeAddrSlaveToMastRead  | sl                              |                                |
| writeAddrSlaveToMastWrite | sl                              |                                |
| writeDataSlaveToMastDin   | slv(35 downto 0)                |                                |
| writeDataSlaveToMastDout  | slv(35 downto 0)                |                                |
| writeDataSlaveToMastFull  | sl                              |                                |
| writeDataSlaveToMastValid | sl                              |                                |
| writeDataSlaveToMastRead  | sl                              |                                |
| writeDataSlaveToMastWrite | sl                              |                                |
| writeMastToSlaveDin       | slv(1 downto 0)                 |                                |
| writeMastToSlaveDout      | slv(1 downto 0)                 |                                |
| writeMastToSlaveFull      | sl                              |                                |
| writeMastToSlaveValid     | sl                              |                                |
| writeMastToSlaveRead      | sl                              |                                |
| writeMastToSlaveWrite     | sl                              |                                |
