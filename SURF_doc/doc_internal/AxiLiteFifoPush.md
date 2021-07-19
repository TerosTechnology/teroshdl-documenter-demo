# Entity: AxiLiteFifoPush

- **File**: AxiLiteFifoPush.vhd
## Diagram

![Diagram](AxiLiteFifoPush.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Supports writing of general purpose FIFOs from the AxiLite bus.
16 address locations per FIFO.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type                  | Value         | Description |
| ------------------ | --------------------- | ------------- | ----------- |
| TPD_G              | time                  | 1 ns          |             |
| PUSH_FIFO_COUNT_G  | positive              | 1             |             |
| PUSH_SYNC_FIFO_G   | boolean               | false         |             |
| PUSH_MEMORY_TYPE_G | string                | "distributed" |             |
| PUSH_ADDR_WIDTH_G  | integer range 4 to 48 | 4             |             |
## Ports

| Port name      | Direction | Type                                     | Description                            |
| -------------- | --------- | ---------------------------------------- | -------------------------------------- |
| axiClk         | in        | sl                                       | AXI Interface (axiClk)                 |
| axiClkRst      | in        | sl                                       |                                        |
| axiReadMaster  | in        | AxiLiteReadMasterType                    |                                        |
| axiReadSlave   | out       | AxiLiteReadSlaveType                     |                                        |
| axiWriteMaster | in        | AxiLiteWriteMasterType                   |                                        |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType                    |                                        |
| pushFifoAFull  | out       | slv(PUSH_FIFO_COUNT_G-1 downto 0)        |                                        |
| pushFifoClk    | in        | slv(PUSH_FIFO_COUNT_G-1 downto 0)        | Push FIFO Read Interface (pushFifoClk) |
| pushFifoRst    | in        | slv(PUSH_FIFO_COUNT_G-1 downto 0)        |                                        |
| pushFifoValid  | out       | slv(PUSH_FIFO_COUNT_G-1 downto 0)        |                                        |
| pushFifoDout   | out       | Slv36Array(PUSH_FIFO_COUNT_G-1 downto 0) |                                        |
| pushFifoRead   | in        | slv(PUSH_FIFO_COUNT_G-1 downto 0)        |                                        |
## Signals

| Name           | Type                         | Description   |
| -------------- | ---------------------------- | ------------- |
| ipushFifoFull  | slv(PUSH_COUNT_C-1 downto 0) | Local Signals |
| ipushFifoAFull | slv(PUSH_COUNT_C-1 downto 0) |               |
| ipushFifoDin   | Slv(35 downto 0)             |               |
| ipushFifoWrite | slv(PUSH_COUNT_C-1 downto 0) |               |
| r              | RegType                      |               |
| rin            | RegType                      |               |
## Constants

| Name         | Type    | Value                                                                                                                                                                                                                                                                                                                     | Description |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PUSH_SIZE_C  | integer |  bitSize(PUSH_FIFO_COUNT_G-1)                                                                                                                                                                                                                                                                                             |             |
| PUSH_COUNT_C | integer |  2**PUSH_SIZE_C                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C   | RegType |  (       pushFifoWrite     => (others => '0'),<br><span style="padding-left:20px">       pushFifoDin       => (others => '0'),<br><span style="padding-left:20px">       axiReadSlave      => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave     => AXI_LITE_WRITE_SLAVE_INIT_C    ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- unnamed: ( axiClk )
**Description**
AXI Lite
Sync

- unnamed: ( r, axiClkRst, axiReadMaster, axiWriteMaster, ipushFifoFull, ipushFifoAFull )
**Description**
Async

