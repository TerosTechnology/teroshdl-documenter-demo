# Entity: AxiI2cEeprom

## Diagram

![Diagram](AxiI2cEeprom.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for AxiI2cEepromCore
Supported Devices:
   24AA01F/24LC01F/24FC01F    (1kb:   ADDR_WIDTH_G = 7)
   24AA02F/24LC02F/24FC02F    (2kb:   ADDR_WIDTH_G = 8)
   24AA04F/24LC04F/24FC04F    (4kb:   ADDR_WIDTH_G = 9)
   24AA08F/24LC08F/24FC08F    (8kb:   ADDR_WIDTH_G = 10)
   24AA16F/24LC16F/24FC16F    (16kb:  ADDR_WIDTH_G = 11)
   24AA32F/24LC32F/24FC32F    (32kb:  ADDR_WIDTH_G = 12)
   24AA64F/24LC64F/24FC64F    (64kb:  ADDR_WIDTH_G = 13)
   24AA128F/24LC128F/24FC128F (128kb: ADDR_WIDTH_G = 14)
   24AA256F/24LC256F/24FC256F (256kb: ADDR_WIDTH_G = 15)
   24AA512F/24LC512F/24FC512F (512kb: ADDR_WIDTH_G = 16)
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
| AXIL_PROXY_G    | boolean         | false     |                  |
| ADDR_WIDTH_G    | positive        | 16        |                  |
| POLL_TIMEOUT_G  | positive        | 16        |                  |
| I2C_ADDR_G      | slv(6 downto 0) | "1010000" |                  |
| I2C_SCL_FREQ_G  | real            | 100.0E+3  | units of Hz      |
| I2C_MIN_PULSE_G | real            | 100.0E-9  | units of seconds |
| AXI_CLK_FREQ_G  | real            | 156.25E+6 |                  |
## Ports

| Port name       | Direction | Type                   | Description                 |
| --------------- | --------- | ---------------------- | --------------------------- |
| scl             | inout     | sl                     | I2C Ports                   |
| sda             | inout     | sl                     |                             |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axilClk         | in        | sl                     | Clocks and Resets           |
| axilRst         | in        | sl                     |                             |
## Signals

| Name             | Type                   | Description |
| ---------------- | ---------------------- | ----------- |
| i2ci             | i2c_in_type            |             |
| i2co             | i2c_out_type           |             |
| proxyReadMaster  | AxiLiteReadMasterType  |             |
| proxyReadSlave   | AxiLiteReadSlaveType   |             |
| proxyWriteMaster | AxiLiteWriteMasterType |             |
| proxyWriteSlave  | AxiLiteWriteSlaveType  |             |
## Instantiations

- U_AxiI2cEepromCore: surf.AxiI2cEepromCore
- IOBUF_SCL: IOBUF
- IOBUF_SDA: IOBUF
**Description**
3-state enable input, high=input, low=output

