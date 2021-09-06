# Entity: tlul_data_integ_enc

- **File**: tlul_data_integ_enc.sv
## Diagram

![Diagram](tlul_data_integ_enc.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Ports

| Port name   | Direction | Type                             | Description      |
| ----------- | --------- | -------------------------------- | ---------------- |
| data_i      | input     | [DataMaxWidth-1:0]               |  TL-UL interface |
| data_intg_o | output    | [DataMaxWidth+DataIntgWidth-1:0] |                  |
## Instantiations

- u_data_gen: prim_secded_39_32_enc
