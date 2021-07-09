# Entity: AxiStreamBytePacker

## Diagram

![Diagram](AxiStreamBytePacker.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Byte packer for AXI-Stream.
Accepts an incoming stream and packs data into the outbound stream.
Similar to AxiStreamResize, but allows an input and output width to have
non multiples and for the input size to be dynamic.
This module does not downsize and creates more complex combinatorial logic
than in AxiStreamResize.
Ready handshaking is not supported.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type                | Value | Description |
| --------------- | ------------------- | ----- | ----------- |
| TPD_G           | time                | 1 ns  |             |
| SLAVE_CONFIG_G  | AxiStreamConfigType |       |             |
| MASTER_CONFIG_G | AxiStreamConfigType |       |             |
## Ports

| Port name   | Direction | Type                | Description            |
| ----------- | --------- | ------------------- | ---------------------- |
| axiClk      | in        | sl                  | System clock and reset |
| axiRst      | in        | sl                  |                        |
| sAxisMaster | in        | AxiStreamMasterType | Inbound frame          |
| mAxisMaster | out       | AxiStreamMasterType | Outbound frame         |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name           | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MAX_IN_BYTE_C  | integer |  SLAVE_CONFIG_G.TDATA_BYTES_C-1                                                                                                                                                                                                                                                                                                                                                                                              |             |
| MAX_OUT_BYTE_C | integer |  MASTER_CONFIG_G.TDATA_BYTES_C-1                                                                                                                                                                                                                                                                                                                                                                                             |             |
| REG_INIT_C     | RegType |  (       byteCount  => 0,<br><span style="padding-left:20px">       inTop      => 0,<br><span style="padding-left:20px">       inMaster   => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       curMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       nxtMaster  => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       outMaster  => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, axiRst, sAxisMaster )
- seq: ( axiClk )
