# Entity: I2cRegMasterAxiBridge

- **File**: I2cRegMasterAxiBridge.vhd
## Diagram

![Diagram](I2cRegMasterAxiBridge.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Maps a number of I2C devices on an I2C bus onto an AXI Bus.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type               | Value                        | Description |
| ------------ | ------------------ | ---------------------------- | ----------- |
| TPD_G        | time               | 1 ns                         |             |
| DEVICE_MAP_G | I2cAxiLiteDevArray | I2C_AXIL_DEV_ARRAY_DEFAULT_C |             |
## Ports

| Port name       | Direction | Type                                | Description |
| --------------- | --------- | ----------------------------------- | ----------- |
| axiClk          | in        | sl                                  |             |
| axiRst          | in        | sl                                  |             |
| axiReadMaster   | in        | AxiLiteReadMasterType               |             |
| axiReadSlave    | out       | AxiLiteReadSlaveType                |             |
| axiWriteMaster  | in        | AxiLiteWriteMasterType              |             |
| axiWriteSlave   | out       | AxiLiteWriteSlaveType               |             |
| i2cSelectOut    | out       | slv(DEVICE_MAP_G'length-1 downto 0) |             |
| i2cRegMasterIn  | out       | I2cRegMasterInType                  |             |
| i2cRegMasterOut | in        | I2cRegMasterOutType                 |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name                    | Type    | Value                                                                                                                                                                                                                                                                                                            | Description                                                                                                                  |
| ----------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| READ_C                  | boolean |  false                                                                                                                                                                                                                                                                                                           |                                                                                                                              |
| WRITE_C                 | boolean |  true                                                                                                                                                                                                                                                                                                            |                                                                                                                              |
| DEVICE_MAP_LENGTH_C     | natural |  DEVICE_MAP_G'length                                                                                                                                                                                                                                                                                             |                                                                                                                              |
| I2C_REG_ADDR_SIZE_C     | natural |  maxAddrSize(DEVICE_MAP_G)                                                                                                                                                                                                                                                                                       | Number of device register space address bits maped into axi bus is determined bythe maximum address size of all the devices. |
| I2C_REG_AXI_ADDR_LOW_C  | natural |  2                                                                                                                                                                                                                                                                                                               |                                                                                                                              |
| I2C_REG_AXI_ADDR_HIGH_C | natural |        ite(I2C_REG_ADDR_SIZE_C = 0,<br><span style="padding-left:20px">           2,<br><span style="padding-left:20px">           I2C_REG_AXI_ADDR_LOW_C + I2C_REG_ADDR_SIZE_C-1)                                                                                                                               |                                                                                                                              |
| I2C_DEV_AXI_ADDR_LOW_C  | natural |  I2C_REG_AXI_ADDR_HIGH_C + 1                                                                                                                                                                                                                                                                                     | Number of device address bits mapped into axi bus space is determined by number of devices                                   |
| I2C_DEV_AXI_ADDR_HIGH_C | natural |  ite(       (DEVICE_MAP_LENGTH_C = 1),<br><span style="padding-left:20px">       I2C_DEV_AXI_ADDR_LOW_C,<br><span style="padding-left:20px">       (I2C_DEV_AXI_ADDR_LOW_C + log2(DEVICE_MAP_LENGTH_C) - 1))                                                                                                     |                                                                                                                              |
| REG_INIT_C              | RegType |  (       axiReadSlave   => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave  => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       i2cSelectOut   => (others=>'0'),<br><span style="padding-left:20px">       i2cRegMasterIn => I2C_REG_MASTER_IN_INIT_C) |                                                                                                                              |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, i2cRegMasterOut, r )
- seq: ( axiClk )
**Description**
Sequential Process

