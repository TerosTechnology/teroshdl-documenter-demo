# Entity: aes_mix_columns
## Diagram
![Diagram](aes_mix_columns.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES MixColumns
 
## Ports
| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| op_i      | input     |       |             |
| data_i    | input     | [3:0] |             |
| data_o    | output    | [3:0] |             |
## Signals
| Name              | Type                  | Description                      |
| ----------------- | --------------------- | -------------------------------- |
| data_i_transposed | logic [3:0][3:0][7:0] | Transpose to operate on columns  |
| data_o_transposed | logic [3:0][3:0][7:0] |                                  |
