# Entity: prim_subst_perm
## Diagram
![Diagram](prim_subst_perm.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This is a simple data diffusion primitive that is constructed in a similar fashion
 as the PRESENT cipher (i.e. it uses a substitution/permutation network). Note however
 that this is **not** cryptographically secure. The main purpose of this primitive is to
 provide a cheap diffusion mechanism for arbitrarily sized vectors.
 See also: prim_prince, prim_present, prim_cipher_pkg
 
## Generics
| Generic name | Type | Value | Description            |
| ------------ | ---- | ----- | ---------------------- |
| DataWidth    | int  | 64    |                        |
| NumRounds    | int  | 31    |                        |
| Decrypt      | bit  | 0     | 0: encrypt, 1: decrypt |
## Ports
| Port name | Direction | Type            | Description |
| --------- | --------- | --------------- | ----------- |
| data_i    | input     | [DataWidth-1:0] |             |
| key_i     | input     | [DataWidth-1:0] |             |
| data_o    | output    | [DataWidth-1:0] |             |
## Signals
| Name       | Type                               | Description            |
| ---------- | ---------------------------------- | ---------------------- |
| data_state | logic [NumRounds:0][DataWidth-1:0] | verilator split_var */ |
