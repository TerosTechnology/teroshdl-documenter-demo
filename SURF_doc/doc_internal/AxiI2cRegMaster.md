# Entity: AxiI2cRegMaster

- **File**: AxiI2cRegMaster.vhd
## Diagram

![Diagram](AxiI2cRegMaster.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite I2C Register Master
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
| scl            | inout     | sl                                  |                             |
| sda            | inout     | sl                                  |                             |
## Signals

| Name | Type         | Description |
| ---- | ------------ | ----------- |
| i2ci | i2c_in_type  |             |
| i2co | i2c_out_type |             |
## Instantiations

- U_Core: surf.AxiI2cRegMasterCore
- IOBUF_SCL: IOBUF
- IOBUF_SDA: IOBUF
**Description**
 3-state enable input, high=input, low=output

