# Entity: prim_subreg_ext
## Diagram
![Diagram](prim_subreg_ext.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Register slice conforming to Comportibility guide.
 
## Generics
| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| DW           | int unsigned | 32    |             |
## Ports
| Port name | Direction | Type     | Description               |
| --------- | --------- | -------- | ------------------------- |
| re        | input     |          |                           |
| we        | input     |          |                           |
| wd        | input     | [DW-1:0] |                           |
| d         | input     | [DW-1:0] |                           |
| qe        | output    |          | output to HW and Reg Read |
| qre       | output    |          |                           |
| q         | output    | [DW-1:0] |                           |
| qs        | output    | [DW-1:0] |                           |
