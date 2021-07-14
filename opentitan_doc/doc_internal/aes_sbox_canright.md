# Entity: aes_sbox_canright

## Diagram

![Diagram](aes_sbox_canright.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES Canright SBox #4
 For details, see the technical report: Canright, "A very compact Rijndael S-box"
 available at https://hdl.handle.net/10945/25608
 
## Ports

| Port name | Direction | Type  | Description |
| --------- | --------- | ----- | ----------- |
| op_i      | input     |       |             |
| data_i    | input     | [7:0] |             |
| data_o    | output    | [7:0] |             |
## Signals

| Name         | Type        | Description |
| ------------ | ----------- | ----------- |
| data_basis_x | logic [7:0] |             |
| data_inverse | logic [7:0] |             |
## Functions
- aes_inverse_gf2p4 <font id="function_arguments">(logic [3:0])</font> <font id="function_return">return (logic [3:0])</font>
**Description**
Inverse in GF(2^4), using normal basis [alpha^8, alpha^2]
(see Figure 12 in the technical report)

- aes_inverse_gf2p8 <font id="function_arguments">(logic [7:0])</font> <font id="function_return">return (logic [7:0])</font>
**Description**
Inverse in GF(2^8), using normal basis [d^16, d]
(see Figure 11 in the technical report)

