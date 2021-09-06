# Entity: AxiLiteRegs

- **File**: AxiLiteRegs.vhd
## Diagram

![Diagram](AxiLiteRegs.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Description:
 Generic register slave endpoint on AXI-Lite bus
 Supports a configurable number of write and read vectors.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name    | Type                  | Value               | Description |
| --------------- | --------------------- | ------------------- | ----------- |
| TPD_G           | time                  | 1 ns                |             |
| NUM_WRITE_REG_G | integer range 1 to 32 | 1                   |             |
| INI_WRITE_REG_G | Slv32Array            | (0 => x"0000_0000") |             |
| NUM_READ_REG_G  | integer range 1 to 32 | 1                   |             |
## Ports

| Port name      | Direction | Type                                   | Description               |
| -------------- | --------- | -------------------------------------- | ------------------------- |
| axiClk         | in        | sl                                     | AXI-Lite Bus              |
| axiClkRst      | in        | sl                                     |                           |
| axiReadMaster  | in        | AxiLiteReadMasterType                  |                           |
| axiReadSlave   | out       | AxiLiteReadSlaveType                   |                           |
| axiWriteMaster | in        | AxiLiteWriteMasterType                 |                           |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType                  |                           |
| writeRegister  | out       | Slv32Array(NUM_WRITE_REG_G-1 downto 0) | User Read/Write registers |
| readRegister   | in        | Slv32Array(NUM_READ_REG_G-1 downto 0)  |                           |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                    | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       writeRegister => writeRegIni( INI_WRITE_REG_G ),<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Functions
- writeRegIni <font id="function_arguments">(iniVal : Slv32Array) </font> <font id="function_return">return WriteRegArray </font>
## Processes
- comb: ( axiClkRst, axiReadMaster, axiWriteMaster, r, readRegister )
- seq: ( axiClk )
