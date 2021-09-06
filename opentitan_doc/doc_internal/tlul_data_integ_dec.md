# Entity: tlul_data_integ_dec

- **File**: tlul_data_integ_dec.sv
## Diagram

![Diagram](tlul_data_integ_dec.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Ports

| Port name   | Direction | Type                             | Description      |
| ----------- | --------- | -------------------------------- | ---------------- |
| data_intg_i | input     | [DataMaxWidth+DataIntgWidth-1:0] |  TL-UL interface |
| data_err_o  | output    |                                  |                  |
## Signals

| Name     | Type        | Description |
| -------- | ----------- | ----------- |
| data_err | logic [1:0] |             |
## Instantiations

- u_data_chk: prim_secded_39_32_dec
