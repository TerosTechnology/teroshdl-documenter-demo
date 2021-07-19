# Entity: AxiStreamGearboxPack

- **File**: AxiStreamGearboxPack.vhd
## Diagram

![Diagram](AxiStreamGearboxPack.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI stream Packer Module
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
| RANGE_HIGH_G        | integer             | 13    |             |
| RANGE_LOW_G         | integer             | 2     |             |
## Ports

| Port name        | Direction | Type                | Description |
| ---------------- | --------- | ------------------- | ----------- |
| axisClk          | in        | sl                  |             |
| axisRst          | in        | sl                  |             |
| rawAxisMaster    | in        | AxiStreamMasterType |             |
| rawAxisSlave     | out       | AxiStreamSlaveType  |             |
| rawAxisCtrl      | out       | AxiStreamCtrlType   |             |
| packedAxisMaster | out       | AxiStreamMasterType |             |
| packedAxisSlave  | in        | AxiStreamSlaveType  |             |
| packedAxisCtrl   | in        | AxiStreamCtrlType   |             |
## Signals

| Name           | Type          | Description |
| -------------- | ------------- | ----------- |
| r              | RegType       |             |
| rin            | RegType       |             |
| rawSsiMaster   | SsiMasterType |             |
| packedSsiSlave | SsiSlaveType  |             |
## Constants

| Name                  | Type         | Value                                                                                                                                                                                                                                                                                                                       | Description |
| --------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| STREAM_WIDTH_C        | integer      |  AXI_STREAM_CONFIG_G.TDATA_BYTES_C*8                                                                                                                                                                                                                                                                                        |             |
| PACK_SIZE_C           | integer      |  RANGE_HIGH_G-RANGE_LOW_G+1                                                                                                                                                                                                                                                                                                 |             |
| SIZE_DIFFERENCE_C     | integer      |  STREAM_WIDTH_C-PACK_SIZE_C                                                                                                                                                                                                                                                                                                 |             |
| ASSIGNMENT_INDECIES_C | IntegerArray |  computeIndicies                                                                                                                                                                                                                                                                                                            |             |
| REG_INIT_C            | RegType      |  (       packedSsiMaster => ssiMasterInit(AXI_STREAM_CONFIG_G),<br><span style="padding-left:20px">       rawSsiSlave     => ssiSlaveInit(AXI_STREAM_CONFIG_G),<br><span style="padding-left:20px">       data            => (others => '0'),<br><span style="padding-left:20px">       index           => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Functions
- computeIndicies <font id="function_arguments">()</font> <font id="function_return">return IntegerArray </font>
**Description**
Vivado chokes if you try to calculate these on the fly inside the comb process.Precompute all of the assignment indicies instead
## Processes
- comb: ( axisRst, r, rawSsiMaster )
- seq: ( axisClk )
