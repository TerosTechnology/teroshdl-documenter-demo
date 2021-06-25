# Entity: aes_mix_single_column
## Diagram
![Diagram](aes_mix_single_column.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES MixColumns for one single column of the state matrix
 For details, see Equations 4-7 of:
 Satoh et al., "A Compact Rijndael Hardware Architecture with S-Box Optimization"
 
## Ports
| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| op_i      | input     |       |             |
| data_i    | input     | [3:0] |             |
| data_o    | output    | [3:0] |             |
## Signals
| Name        | Type             | Description |
| ----------- | ---------------- | ----------- |
| x           | logic [3:0][7:0] |             |
| y           | logic [1:0][7:0] |             |
| z           | logic [1:0][7:0] |             |
| x_mul2      | logic [3:0][7:0] |             |
| y_pre_mul4  | logic [1:0][7:0] |             |
| y2          | logic      [7:0] |             |
| y2_pre_mul2 | logic      [7:0] |             |
| z_muxed     | logic [1:0][7:0] |             |
