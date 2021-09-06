# Entity: AxiStreamBytePackerTbTx

- **File**: AxiStreamBytePackerTbTx.vhd
## Diagram

![Diagram](AxiStreamBytePackerTbTx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 AxiStream data packer tester, tx module
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

| Generic name  | Type                | Value | Description |
| ------------- | ------------------- | ----- | ----------- |
| TPD_G         | time                | 1 ns  |             |
| BYTE_SIZE_C   | positive            | 1     |             |
| AXIS_CONFIG_G | AxiStreamConfigType |       |             |
## Ports

| Port name   | Direction | Type                | Description            |
| ----------- | --------- | ------------------- | ---------------------- |
| axiClk      | in        | sl                  | System clock and reset |
| axiRst      | in        | sl                  |                        |
| mAxisMaster | out       | AxiStreamMasterType | Outbound frame         |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                  | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       byteCount  => 0,<br><span style="padding-left:20px">       frameCount => 0,<br><span style="padding-left:20px">       master     => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, axiRst )
- seq: ( axiClk )
