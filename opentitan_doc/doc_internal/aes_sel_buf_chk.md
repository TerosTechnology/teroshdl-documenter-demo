# Entity: aes_sel_buf_chk

- **File**: aes_sel_buf_chk.sv
## Diagram

![Diagram](aes_sel_buf_chk.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 AES mux selector buffer and checker
 When using sparse encodings for mux selector signals, this module can be used to:
 1. Prevent aggressive synthesis optimizations on the selector signal, and
 2. to check that the selector signal is valid, i.e., doesn't take on invalid values.
 Whenever the selector signal takes on an invalid value, an error is signaled.
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Num          | int  | 2     |             |
| Width        | int  | 1     |             |
## Ports

| Port name | Direction | Type        | Description               |
| --------- | --------- | ----------- | ------------------------- |
| clk_i     | input     |             | Used for assertions only. |
| rst_ni    | input     |             | Used for assertions only. |
| sel_i     | input     | [Width-1:0] |                           |
| sel_o     | output    | [Width-1:0] |                           |
| err_o     | output    |             |                           |
## Signals

| Name       | Type  | Description             |
| ---------- | ----- | ----------------------- |
| unused_clk | logic | Tie off unused inputs.  |
| unused_rst | logic |                         |
