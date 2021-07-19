# Package: hmac_pkg

- **File**: hmac_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name     | Type        | Description |
| -------- | ----------- | ----------- |
| compress | endfunction |             |
| hmac_pkg | endpackage  |             |
## Constants

| Name           | Type       | Value               | Description      |
| -------------- | ---------- | ------------------- | ---------------- |
| MsgFifoDepth   | int        | 16                  |                  |
| NumRound       | int        | 64                  | SHA-224, SHA-256 |
| WordByte       | int        | $bits(sha_word_t)/8 |                  |
| InitHash       | sha_word_t | undefined           |                  |
| CubicRootPrime | sha_word_t | undefined           |                  |
## Types

| Name       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| sha_word_t | logic [31:0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| sha_fifo_t | struct packed {<br><span style="padding-left:20px">     sha_word_t           data;<br><span style="padding-left:20px">     logic [WordByte-1:0] mask;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                        |             |
| err_code_e | enum logic [31:0] {<br><span style="padding-left:20px">     NoError                    = 32'h 0000_0000,<br><span style="padding-left:20px">     SwPushMsgWhenShaDisabled   = 32'h 0000_0001,<br><span style="padding-left:20px">     SwHashStartWhenShaDisabled = 32'h 0000_0002,<br><span style="padding-left:20px">     SwUpdateSecretKeyInProcess = 32'h 0000_0003,<br><span style="padding-left:20px">     SwHashStartWhenActive      = 32'h 0000_0004,<br><span style="padding-left:20px">     SwPushMsgWhenDisallowed    = 32'h 0000_0005   } |             |
## Functions
- calc_w <font id="function_arguments">(input sha_word_t)</font> <font id="function_return">return (sha_word_t)</font>
