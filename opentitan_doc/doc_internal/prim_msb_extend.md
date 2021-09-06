# Entity: prim_msb_extend

- **File**: prim_msb_extend.sv
## Diagram

![Diagram](prim_msb_extend.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Extend the output with the msb of the input

## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| InWidth      | int  | 2     |             |
| OutWidth     | int  | 2     |             |
## Ports

| Port name | Direction | Type           | Description |
| --------- | --------- | -------------- | ----------- |
| in_i      | input     | [InWidth-1:0]  |             |
| out_o     | output    | [OutWidth-1:0] |             |
## Constants

| Name      | Type | Value              | Description |
| --------- | ---- | ------------------ | ----------- |
| WidthDiff | int  | OutWidth - InWidth |             |
