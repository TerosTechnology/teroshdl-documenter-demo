# Package: prim_cipher_pkg

- **File**: prim_cipher_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This package holds common constants and functions for PRESENT- and
 PRINCE-based scrambling devices.
 See also: prim_present, prim_prince
 References: - https://en.wikipedia.org/wiki/PRESENT
             - https://en.wikipedia.org/wiki/Prince_(cipher)
             - http://www.lightweightcrypto.org/present/present_ches2007.pdf
             - https://eprint.iacr.org/2012/529.pdf
             - https://eprint.iacr.org/2015/372.pdf
             - https://eprint.iacr.org/2014/656.pdf
 

## Signals

| Name            | Type       | Description |
| --------------- | ---------- | ----------- |
| prim_cipher_pkg | endpackage |             |
## Constants

| Name                     | Type              | Value                                                                                                                                                                                                            | Description                                                                                                       |
| ------------------------ | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| PRINCE_SBOX4             | logic [15:0][3:0] | {<br><span style="padding-left:20px">4'h4,<br><span style="padding-left:20px"> 4'hD,<br><span style="padding-left:20px"> 4'h5,<br><span style="padding-left:20px"> 4'hE,<br><span style="padding-left:20px">     |                                                                                                                   |
| PRINCE_SBOX4_INV         | logic [15:0][3:0] | {<br><span style="padding-left:20px">4'h1,<br><span style="padding-left:20px"> 4'hC,<br><span style="padding-left:20px"> 4'hE,<br><span style="padding-left:20px"> 4'h5,<br><span style="padding-left:20px">     |                                                                                                                   |
| PRINCE_SHIFT_ROWS64      | logic [15:0][3:0] | undefined                                                                                                                                                                                                        | nibble permutations                                                                                               |
| PRINCE_SHIFT_ROWS64_INV  | logic [15:0][3:0] | logic [11:0][63:0]                                                                                                                                                                                               |                                                                                                                   |
| PRINCE_ALPHA_CONST       | logic [63:0]      | 64'hC0AC29B7C97C50DD                                                                                                                                                                                             | tweak constant for key modification between enc/dec modes                                                         |
| PRINCE_SHIFT_ROWS_CONST0 | logic [15:0]      | 16'h7BDE                                                                                                                                                                                                         | masking constants for shift rows function below                                                                   |
| PRINCE_SHIFT_ROWS_CONST1 | logic [15:0]      | 16'hBDE7                                                                                                                                                                                                         |                                                                                                                   |
| PRINCE_SHIFT_ROWS_CONST2 | logic [15:0]      | 16'hDE7B                                                                                                                                                                                                         |                                                                                                                   |
| PRINCE_SHIFT_ROWS_CONST3 | logic [15:0]      | 16'hE7BD                                                                                                                                                                                                         |                                                                                                                   |
| PRESENT_SBOX4            | logic [15:0][3:0] | {<br><span style="padding-left:20px">4'h2,<br><span style="padding-left:20px"> 4'h1,<br><span style="padding-left:20px"> 4'h7,<br><span style="padding-left:20px"> 4'h4,<br><span style="padding-left:20px">     | this is the sbox from the present cipher                                                                          |
| PRESENT_SBOX4_INV        | logic [15:0][3:0] | {<br><span style="padding-left:20px">4'hA,<br><span style="padding-left:20px"> 4'h9,<br><span style="padding-left:20px"> 4'h7,<br><span style="padding-left:20px"> 4'h0,<br><span style="padding-left:20px">     |                                                                                                                   |
| PRESENT_PERM32           | logic [31:0][4:0] | {<br><span style="padding-left:20px">5'd31,<br><span style="padding-left:20px"> 5'd23,<br><span style="padding-left:20px"> 5'd15,<br><span style="padding-left:20px"> 5'd07,<br><span style="padding-left:20px"> | these are modified permutation indices for a 32bit version that follow the same pattern as for the 64bit version  |
| PRESENT_PERM32_INV       | logic [31:0][4:0] | {<br><span style="padding-left:20px">5'd31,<br><span style="padding-left:20px"> 5'd27,<br><span style="padding-left:20px"> 5'd23,<br><span style="padding-left:20px"> 5'd19,<br><span style="padding-left:20px"> |                                                                                                                   |
| PRESENT_PERM64           | logic [63:0][5:0] | {<br><span style="padding-left:20px">6'd63,<br><span style="padding-left:20px"> 6'd47,<br><span style="padding-left:20px"> 6'd31,<br><span style="padding-left:20px"> 6'd15,<br><span style="padding-left:20px"> | these are the permutation indices of the present cipher                                                           |
| PRESENT_PERM64_INV       | logic [63:0][5:0] | {<br><span style="padding-left:20px">6'd63,<br><span style="padding-left:20px"> 6'd59,<br><span style="padding-left:20px"> 6'd55,<br><span style="padding-left:20px"> 6'd51,<br><span style="padding-left:20px"> |                                                                                                                   |
## Functions
- prince_shiftrows_32bit <font id="function_arguments">(logic [31:0]      state_)</font> <font id="function_return">return (logic [31:0])</font>
**Description**
nibble shifts

- prince_shiftrows_64bit <font id="function_arguments">(logic [63:0]      state_)</font> <font id="function_return">return (logic [63:0])</font>
- prince_nibble_red16 <font id="function_arguments">(logic [15:0])</font> <font id="function_return">return (logic [3:0])</font>
**Description**
XOR reduction of four nibbles in a 16bit subvector

- prince_mult_prime_32bit <font id="function_arguments">(logic [31:0] state_in)</font> <font id="function_return">return (logic [31:0])</font>
**Description**
M prime multiplication

- prince_mult_prime_64bit <font id="function_arguments">(logic [63:0] state_in)</font> <font id="function_return">return (logic [63:0])</font>
**Description**
M prime multiplication

- present_update_key64 <font id="function_arguments">(logic [63:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [63:0])</font>
**Description**
forward key schedule

- present_update_key80 <font id="function_arguments">(logic [79:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [79:0])</font>
- present_update_key128 <font id="function_arguments">(logic [127:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [127:0])</font>
- present_inv_update_key64 <font id="function_arguments">(logic [63:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [63:0])</font>
**Description**
inverse key schedule

- present_inv_update_key80 <font id="function_arguments">(logic [79:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [79:0])</font>
- present_inv_update_key128 <font id="function_arguments">(logic [127:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [127:0])</font>
- present_get_dec_key64 <font id="function_arguments">(logic [63:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [63:0])</font>
**Description**
these functions can be used to derive the DEC key from the ENC key by
stepping the key by the correct number of rounds using the keyschedule functions above.

- present_get_dec_key80 <font id="function_arguments">(logic [79:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [79:0])</font>
- present_get_dec_key128 <font id="function_arguments">(logic [127:0] key_in,<br><span style="padding-left:20px">)</font> <font id="function_return">return (logic [127:0])</font>
- sbox4_8bit <font id="function_arguments">(logic [7:0] state_in,<br><span style="padding-left:20px"> logic [15:0][3:0])</font> <font id="function_return">return (logic [7:0])</font>
- sbox4_16bit <font id="function_arguments">(logic [15:0] state_in,<br><span style="padding-left:20px"> logic [15:0][3:0])</font> <font id="function_return">return (logic [15:0])</font>
- sbox4_32bit <font id="function_arguments">(logic [31:0] state_in,<br><span style="padding-left:20px"> logic [15:0][3:0])</font> <font id="function_return">return (logic [31:0])</font>
- sbox4_64bit <font id="function_arguments">(logic [63:0] state_in,<br><span style="padding-left:20px"> logic [15:0][3:0])</font> <font id="function_return">return (logic [63:0])</font>
- perm_8bit <font id="function_arguments">(logic [7:0] state_in,<br><span style="padding-left:20px"> logic [7:0][2:0])</font> <font id="function_return">return (logic [7:0])</font>
- perm_16bit <font id="function_arguments">(logic [15:0] state_in,<br><span style="padding-left:20px"> logic [15:0][3:0])</font> <font id="function_return">return (logic [15:0])</font>
- perm_32bit <font id="function_arguments">(logic [31:0] state_in,<br><span style="padding-left:20px"> logic [31:0][4:0])</font> <font id="function_return">return (logic [31:0])</font>
- perm_64bit <font id="function_arguments">(logic [63:0] state_in,<br><span style="padding-left:20px"> logic [63:0][5:0])</font> <font id="function_return">return (logic [63:0])</font>
