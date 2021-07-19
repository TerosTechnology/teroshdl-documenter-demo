# Entity: tlul_cmd_intg_chk

- **File**: tlul_cmd_intg_chk.sv
## Diagram

![Diagram](tlul_cmd_intg_chk.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports

| Port name | Direction | Type     | Description     |
| --------- | --------- | -------- | --------------- |
| tl_i      | input     | tl_h2d_t | TL-UL interface |
| err_o     | output    |          | error output    |
## Signals

| Name      | Type              | Description                                                                                                        |
| --------- | ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| err       | logic [1:0]       |                                                                                                                    |
| data_err  | logic [1:0]       |                                                                                                                    |
| cmd       | tl_h2d_cmd_intg_t |                                                                                                                    |
| wr_txn    | logic             | error output is transactional, it is up to the instantiating module to determine if a permanent latch is feasible  |
| unused_tl | logic             |                                                                                                                    |
## Instantiations

- u_chk: prim_secded_64_57_dec
- u_data_chk: prim_secded_39_32_dec
