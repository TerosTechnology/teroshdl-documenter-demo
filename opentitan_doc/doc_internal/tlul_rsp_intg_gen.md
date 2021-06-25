# Entity: tlul_rsp_intg_gen
## Diagram
![Diagram](tlul_rsp_intg_gen.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics
| Generic name      | Type | Value | Description |
| ----------------- | ---- | ----- | ----------- |
| EnableRspIntgGen  | bit  | 1'b1  |             |
| EnableDataIntgGen | bit  | 1'b1  |             |
## Ports
| Port name | Direction | Type     | Description     |
| --------- | --------- | -------- | --------------- |
| tl_i      | input     | tl_d2h_t | TL-UL interface |
| tl_o      | output    | tl_d2h_t |                 |
## Signals
| Name      | Type                        | Description |
| --------- | --------------------------- | ----------- |
| rsp_intg  | logic [D2HRspIntgWidth-1:0] |             |
| data_intg | logic [DataIntgWidth-1:0]   |             |
| unused_tl | logic                       |             |
## Processes
- unnamed: _(  )_

