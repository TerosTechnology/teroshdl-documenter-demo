# Package: crypto_dpi_present_pkg

- **File**: crypto_dpi_present_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Signals

| Name         | Type                    | Description |
| ------------ | ----------------------- | ----------- |
| key_high     | longint unsigned        |             |
| input        | longint unsigned        |             |
| key_low      | longint unsigned        |             |
| input        | longint unsigned        |             |
| num_rounds   | int unsigned            |             |
| input        | int unsigned            |             |
| key_size_80  | int unsigned            |             |
| output       | int unsigned            |             |
| key_schedule | bit [NumRounds:0][63:0] |             |
| plaintext    | longint unsigned        |             |
| input        | longint unsigned        |             |
| key_high     | longint unsigned        |             |
| input        | longint unsigned        |             |
| key_low      | longint unsigned        |             |
| input        | longint unsigned        |             |
| num_rounds   | int unsigned            |             |
| input        | int unsigned            |             |
| key_size_80  | int unsigned            |             |
| ciphertext   | longint unsigned        |             |
| input        | longint unsigned        |             |
| key_high     | longint unsigned        |             |
| input        | longint unsigned        |             |
| key_low      | longint unsigned        |             |
| input        | longint unsigned        |             |
| num_rounds   | int unsigned            |             |
| input        | int unsigned            |             |
| key_size_80  | int unsigned            |             |
## Constants

| Name      | Type         | Value | Description                                                            |
| --------- | ------------ | ----- | ---------------------------------------------------------------------- |
| NumRounds | int unsigned | 31    |  parameters  This is defined here so we can size all arrays properly.  |
## Functions
- get_keys <font id="function_arguments">(input bit [127:0] key,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
</br>**Description**
 Helper Functions

- sv_dpi_present_get_key_schedule <font id="function_arguments">(input bit [127:0]                   key,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
</br>**Description**
////////////////////////////////////////////////////
 SV wrapper functions to be used by the testbench //
////////////////////////////////////////////////////
 This function takes in a 128 bit key by default, it determines how to
 split this key for the DPI calls based on the value of key_size_80.

 This returns the list of round keys used during the course of the algorithm.

- sv_dpi_present_encrypt <font id="function_arguments">(input bit [63:0]                  plaintext,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
</br>**Description**
 This function encrypts the input plaintext with the PRESENT encryption
 algorithm using the specified number of rounds.

 This produces a list of all intermediate values produced after each round
 of the algorithm, including the final encrypted ciphertext value.

- sv_dpi_present_decrypt <font id="function_arguments">(input bit [NumRounds-1:0][63:0]   ciphertext,<br><span style="padding-left:20px">)</font> <font id="function_return">return (void)</font>
</br>**Description**
 This function decrypts the input ciphertext with the PRESENT decryption
 algorithm using the specified number of rounds.

 This produces a list of all intermediate values produced after each round
 of the algorithm, including the final decrypted plaintext value.

