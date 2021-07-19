# Package: nist_vectors_pkg

- **File**: nist_vectors_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name       | Type     | Description |
| ---------- | -------- | ----------- |
| num        | int      |             |
| endpackage | endclass |             |
## Types

| Name          | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| nist_vector_t | struct {<br><span style="padding-left:20px">     aes_mode_e   mode;<br><span style="padding-left:20px">     key_len_e    key_len;<br><span style="padding-left:20px">     aes_op_e     operation;<br><span style="padding-left:20px">     bit [127:0]  iv;<br><span style="padding-left:20px">     bit [255:0]  key;<br><span style="padding-left:20px">     bit [3:0] [31:0]  plain_text[4];<br><span style="padding-left:20px">     bit [3:0] [31:0]  cipher_text[4];<br><span style="padding-left:20px">   } |             |
## Functions
- vector2string <font id="function_arguments">(nist_vector_t vector)</font> <font id="function_return">return (string)</font>
- get_vectors <font id="function_arguments">(ref nist_vector_t nist_vectors[])</font> <font id="function_return">return (void)</font>
**Description**
new

- get_num_vectors <font id="function_arguments">()</font> <font id="function_return">return (int)</font>
