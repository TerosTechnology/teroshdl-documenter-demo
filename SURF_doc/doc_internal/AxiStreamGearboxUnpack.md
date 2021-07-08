# Entity: AxiStreamGearboxUnpack

## Diagram

![Diagram](AxiStreamGearboxUnpack.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Takes 8 80-bit (5x16) ADC frames and reformats them into
             7 80 bit (5x14) frames.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name        | Type                | Value | Description |
| ------------------- | ------------------- | ----- | ----------- |
| TPD_G               | time                | 1 ns  |             |
| AXI_STREAM_CONFIG_G | AxiStreamConfigType |       |             |
| RANGE_HIGH_G        | integer             | 119   |             |
| RANGE_LOW_G         | integer             | 8     |             |
## Ports

| Port name        | Direction | Type                | Description |
| ---------------- | --------- | ------------------- | ----------- |
| axisClk          | in        | sl                  |             |
| axisRst          | in        | sl                  |             |
| packedAxisMaster | in        | AxiStreamMasterType |             |
| packedAxisSlave  | out       | AxiStreamSlaveType  |             |
| packedAxisCtrl   | out       | AxiStreamCtrlType   |             |
| rawAxisMaster    | out       | AxiStreamMasterType |             |
| rawAxisSlave     | in        | AxiStreamSlaveType  |             |
| rawAxisCtrl      | in        | AxiStreamCtrlType   |             |
## Signals

| Name             | Type                | Description |
| ---------------- | ------------------- | ----------- |
| r                | RegType             |             |
| rin              | RegType             |             |
| rawSsiSlave      | SsiSlaveType        |             |
| packedSsiMaster  | SsiMasterType       |             |
| locRawAxisMaster | AxiStreamMasterType |             |
| locRawAxisSlave  | AxiStreamSlaveType  |             |
| locRawAxisCtrl   | AxiStreamCtrlType   |             |
## Constants

| Name              | Type                              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| STREAM_WIDTH_C    | integer                           |  AXI_STREAM_CONFIG_G.TDATA_BYTES_C*8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| PACK_SIZE_C       | integer                           |  RANGE_HIGH_G-RANGE_LOW_G+1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| SIZE_DIFFERENCE_C | integer                           |  STREAM_WIDTH_C-PACK_SIZE_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| ZERO_C            | slv(SIZE_DIFFERENCE_C-1 downto 0) |  slvZero(SIZE_DIFFERENCE_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C        | RegType                           |  (       packedSsiSlave => ssiSlaveInit(AXI_STREAM_CONFIG_G),<br><span style="padding-left:20px">       rawSsiMaster   => ssiMasterInit(AXI_STREAM_CONFIG_G),<br><span style="padding-left:20px">       data           => (others => '0'),<br><span style="padding-left:20px">       splitIndex     => (others => '0'),<br><span style="padding-left:20px">       eof            => '0',<br><span style="padding-left:20px">       eofe           => '0',<br><span style="padding-left:20px">       doLast         => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axisRst, packedSsiMaster, r )
- seq: ( axisClk )
