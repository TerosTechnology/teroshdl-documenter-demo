# Entity: tlul_rsp_intg_chk

## Diagram

![Diagram](tlul_rsp_intg_chk.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports

| Port name | Direction | Type     | Description     |
| --------- | --------- | -------- | --------------- |
| tl_i      | input     | tl_d2h_t | TL-UL interface |
| err_o     | output    |          | error output    |
## Signals

| Name      | Type              | Description |
| --------- | ----------------- | ----------- |
| err       | logic [1:0]       |             |
| rsp       | tl_d2h_rsp_intg_t |             |
| unused_tl | logic             |             |
## Instantiations

- u_chk: prim_secded_64_57_dec
