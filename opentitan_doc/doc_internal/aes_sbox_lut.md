# Entity: aes_sbox_lut

- **File**: aes_sbox_lut.sv
## Diagram

![Diagram](aes_sbox_lut.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 AES LUT-based SBox

## Ports

| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| op_i      | input     |       |             |
| data_i    | input     | [7:0] |             |
| data_o    | output    | [7:0] |             |
## Constants

| Name     | Type        | Value     | Description       |
| -------- | ----------- | --------- | ----------------- |
| SBOX_FWD | logic [7:0] | undefined |  Define the LUTs  |
| SBOX_INV | logic [7:0] | undefined |                   |
