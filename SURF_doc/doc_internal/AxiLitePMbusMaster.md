# Entity: AxiLitePMbusMaster

- **File**: AxiLitePMbusMaster.vhd
## Diagram

![Diagram](AxiLitePMbusMaster.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for AxiLitePMbusMasterCore
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type            | Value     | Description      |
| --------------- | --------------- | --------- | ---------------- |
| TPD_G           | time            | 1 ns      |                  |
| I2C_ADDR_G      | slv(6 downto 0) | "1010000" |                  |
| I2C_SCL_FREQ_G  | real            | 100.0E+3  | units of Hz      |
| I2C_MIN_PULSE_G | real            | 100.0E-9  | units of seconds |
| AXI_CLK_FREQ_G  | real            | 156.25E+6 |                  |
## Ports

| Port name       | Direction | Type                   | Description                 |
| --------------- | --------- | ---------------------- | --------------------------- |
| scl             | inout     | sl                     | PMbus Ports                 |
| sda             | inout     | sl                     |                             |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axilClk         | in        | sl                     | Clocks and Resets           |
| axilRst         | in        | sl                     |                             |
## Signals

| Name | Type         | Description |
| ---- | ------------ | ----------- |
| i2ci | i2c_in_type  |             |
| i2co | i2c_out_type |             |
## Instantiations

- U_Core: surf.AxiLitePMbusMasterCore
- IOBUF_SCL: IOBUF
- IOBUF_SDA: IOBUF
**Description**
3-state enable input, high=input, low=output

