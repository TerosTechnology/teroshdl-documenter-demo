# Entity: AxiResize

- **File**: AxiResize.vhd
## Diagram

![Diagram](AxiResize.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Block to resize AXI. Re-sizing is always little endian.
Disclaimer: This module doesn't support the following:
            Narrow write transfers
            Unaligned transfers
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name        | Type          | Value | Description                     |
| ------------------- | ------------- | ----- | ------------------------------- |
| TPD_G               | time          | 1 ns  | General Configurations          |
| SLAVE_AXI_CONFIG_G  | AxiConfigType |       | AXI Stream Port Configurations  |
| MASTER_AXI_CONFIG_G | AxiConfigType |       |                                 |
## Ports

| Port name       | Direction | Type               | Description     |
| --------------- | --------- | ------------------ | --------------- |
| axiClk          | in        | sl                 | Clock and reset |
| axiRst          | in        | sl                 |                 |
| sAxiReadMaster  | in        | AxiReadMasterType  | Slave Port      |
| sAxiReadSlave   | out       | AxiReadSlaveType   |                 |
| sAxiWriteMaster | in        | AxiWriteMasterType |                 |
| sAxiWriteSlave  | out       | AxiWriteSlaveType  |                 |
| mAxiReadMaster  | out       | AxiReadMasterType  | Master Port     |
| mAxiReadSlave   | in        | AxiReadSlaveType   |                 |
| mAxiWriteMaster | out       | AxiWriteMasterType |                 |
| mAxiWriteSlave  | in        | AxiWriteSlaveType  |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name        | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SLV_BYTES_C | integer |  SLAVE_AXI_CONFIG_G.DATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| MST_BYTES_C | integer |  MASTER_AXI_CONFIG_G.DATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| MAX_BYTES_C | integer |  maximum(SLV_BYTES_C,<br><span style="padding-left:20px"> MST_BYTES_C)                                                                                                                                                                                                                                                                                                                                                                                               |             |
| COUNT_C     | integer |  ite(SLV_BYTES_C > MST_BYTES_C,<br><span style="padding-left:20px"> SLV_BYTES_C / MST_BYTES_C,<br><span style="padding-left:20px"> MST_BYTES_C / SLV_BYTES_C)                                                                                                                                                                                                                                                                                                        |             |
| BIT_CNT_C   | integer |  bitSize(COUNT_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| SHIFT_C     | integer |  log2(COUNT_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| REG_INIT_C  | RegType |  (       rdCount  => (others => '0'),<br><span style="padding-left:20px">       rdMaster => axiReadMasterInit(MASTER_AXI_CONFIG_G),<br><span style="padding-left:20px">       rdSlave  => AXI_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       wrCount  => (others => '0'),<br><span style="padding-left:20px">       wrMaster => axiWriteMasterInit(MASTER_AXI_CONFIG_G),<br><span style="padding-left:20px">       wrSlave  => AXI_WRITE_SLAVE_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
