# Entity: prim_slicer
## Diagram
![Diagram](prim_slicer.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Slicer chops the incoming bitstring into OutW granularity.
 It supports fractional InW/OutW which fills 0 at the end of message.
 
## Generics
| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| InW          | int  | 64    |             |
| OutW         | int  | 8     |             |
| IndexW       | int  | 4     |             |
## Ports
| Port name | Direction | Type         | Description |
| --------- | --------- | ------------ | ----------- |
| sel_i     | input     | [IndexW-1:0] |             |
| data_i    | input     | [InW-1:0]    |             |
| data_o    | output    | [OutW-1:0]   |             |
## Signals
| Name          | Type                | Description |
| ------------- | ------------------- | ----------- |
| unrolled_data | logic [UnrollW-1:0] |             |
## Constants
| Name    | Type | Value            | Description |
| ------- | ---- | ---------------- | ----------- |
| UnrollW | int  | OutW*(2**IndexW) |             |
