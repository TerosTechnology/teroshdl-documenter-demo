# Entity: ClinkUartThrottle

- **File**: ClinkUartThrottle.vhd
## Diagram

![Diagram](ClinkUartThrottle.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: CameraLink UART TX Throttle
Used when the camera cannot accept new bytes until the previous command processed
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name   | Direction | Type                | Description                   |
| ----------- | --------- | ------------------- | ----------------------------- |
| intClk      | in        | sl                  | Clock and reset, 200Mhz       |
| intRst      | in        | sl                  |                               |
| throttle    | in        | slv(15 downto 0)    | Throttle Config (units of us) |
| sUartMaster | in        | AxiStreamMasterType | Data In/Out                   |
| sUartSlave  | out       | AxiStreamSlaveType  |                               |
| mUartMaster | out       | AxiStreamMasterType |                               |
| mUartSlave  | in        | AxiStreamSlaveType  |                               |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | Regtype |             |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                 | Description          |
| ------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| TIMEOUT_C    | integer             |  199                                                                                                                                                                                                                                                                                                                                                                                                  | (200 MHz x 1 us) - 1 |
| INT_CONFIG_C | AxiStreamConfigType |  ssiAxiStreamConfig(dataBytes => 4,<br><span style="padding-left:20px"> tDestBits => 0)                                                                                                                                                                                                                                                                                                               |                      |
| REG_INIT_C   | RegType             |  (       heartbeat   => '0',<br><span style="padding-left:20px">       cnt         => 0,<br><span style="padding-left:20px">       timeout     => '0',<br><span style="padding-left:20px">       timer       => (others => '0'),<br><span style="padding-left:20px">       sUartSlave  => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       mUartMaster => AXI_STREAM_MASTER_INIT_C) |                      |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( intRst, mUartSlave, r, sUartMaster, throttle )
- seq: ( intClk )
