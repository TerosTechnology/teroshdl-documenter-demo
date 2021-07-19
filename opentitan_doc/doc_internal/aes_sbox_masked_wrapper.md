# Entity: aes_sbox_masked_wrapper

- **File**: aes_sbox_masked_wrapper.sv
## Diagram

![Diagram](aes_sbox_masked_wrapper.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Wrapper to allow LEC of masked S-Boxes against LUT-based S-Box.
 
## Ports

| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| op_i      | input     |       |             |
| data_i    | input     | [7:0] |             |
| data_o    | output    | [7:0] |             |
## Signals

| Name        | Type         | Description |
| ----------- | ------------ | ----------- |
| in_data_m   | logic  [7:0] |             |
| out_data_m  | logic  [7:0] |             |
| in_mask     | logic  [7:0] |             |
| out_mask    | logic  [7:0] |             |
| prd_masking | logic [17:0] |             |
## Instantiations

- aes_sbox_masked: aes_sbox_masked
