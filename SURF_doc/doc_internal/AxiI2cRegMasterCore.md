# Entity: AxiI2cRegMasterCore

- **File**: AxiI2cRegMasterCore.vhd
## Diagram

![Diagram](AxiI2cRegMasterCore.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite I2C Register Master Core
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

| Generic name    | Type               | Value                        | Description       |
| --------------- | ------------------ | ---------------------------- | ----------------- |
| TPD_G           | time               | 1 ns                         |                   |
| AXIL_PROXY_G    | boolean            | false                        |                   |
| DEVICE_MAP_G    | I2cAxiLiteDevArray | I2C_AXIL_DEV_ARRAY_DEFAULT_C |                   |
| I2C_SCL_FREQ_G  | real               | 100.0E+3                     |  units of Hz      |
| I2C_MIN_PULSE_G | real               | 100.0E-9                     |  units of seconds |
| AXI_CLK_FREQ_G  | real               | 156.25E+6                    |                   |
## Ports

| Port name      | Direction | Type                                | Description                 |
| -------------- | --------- | ----------------------------------- | --------------------------- |
| axiClk         | in        | sl                                  | Clocks and Resets           |
| axiRst         | in        | sl                                  |                             |
| axiReadMaster  | in        | AxiLiteReadMasterType               | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType                |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType              |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType               |                             |
| sel            | out       | slv(DEVICE_MAP_G'length-1 downto 0) | I2C Ports                   |
| i2ci           | in        | i2c_in_type                         |                             |
| i2co           | out       | i2c_out_type                        |                             |
## Signals

| Name             | Type                   | Description |
| ---------------- | ---------------------- | ----------- |
| i2cRegMasterIn   | I2cRegMasterInType     |             |
| i2cRegMasterOut  | I2cRegMasterOutType    |             |
| proxyReadMaster  | AxiLiteReadMasterType  |             |
| proxyReadSlave   | AxiLiteReadSlaveType   |             |
| proxyWriteMaster | AxiLiteWriteMasterType |             |
| proxyWriteSlave  | AxiLiteWriteSlaveType  |             |
## Constants

| Name             | Type    | Value                                                                                     | Description |
| ---------------- | ------- | ----------------------------------------------------------------------------------------- | ----------- |
| I2C_SCL_5xFREQ_C | real    |  5.0 * I2C_SCL_FREQ_G                                                                     |             |
| PRESCALE_C       | natural |  (getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> I2C_SCL_5xFREQ_C)) - 1 |             |
| FILTER_C         | natural |  natural(AXI_CLK_FREQ_G * I2C_MIN_PULSE_G) + 1                                            |             |
## Instantiations

- U_I2cRegMasterAxiBridge: surf.I2cRegMasterAxiBridge
- U_I2cRegMaster: surf.I2cRegMaster
