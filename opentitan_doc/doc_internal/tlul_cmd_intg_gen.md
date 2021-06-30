# Entity: tlul_cmd_intg_gen

## Diagram

![Diagram](tlul_cmd_intg_gen.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics

| Generic name      | Type | Value | Description                                                                             |
| ----------------- | ---- | ----- | --------------------------------------------------------------------------------------- |
| EnableDataIntgGen | bit  | 1'b1  | TODO: default generation of data integrity is on until host native generation is ready  |
## Ports

| Port name | Direction | Type     | Description     |
| --------- | --------- | -------- | --------------- |
| tl_i      | input     | tl_h2d_t | TL-UL interface |
| tl_o      | output    | tl_h2d_t |                 |
## Signals

| Name               | Type                        | Description |
| ------------------ | --------------------------- | ----------- |
| cmd                | tl_h2d_cmd_intg_t           |             |
| unused_cmd_payload | logic [H2DCmdMaxWidth-1:0]  |             |
| cmd_intg           | logic [H2DCmdIntgWidth-1:0] |             |
| data_final         | logic [top_pkg::TL_DW-1:0]  |             |
| data_intg          | logic [DataIntgWidth-1:0]   |             |
| unused_tl          | logic                       |             |
## Processes
- unnamed: (  )
## Instantiations

- u_cmd_gen: prim_secded_64_57_enc
