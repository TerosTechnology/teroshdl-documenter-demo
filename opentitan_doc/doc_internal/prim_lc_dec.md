# Entity: prim_lc_dec
## Diagram
![Diagram](prim_lc_dec.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Decoder for life cycle control signals with additional
 input buffers.
 
## Ports
| Port name   | Direction | Type | Description |
| ----------- | --------- | ---- | ----------- |
| lc_en_i     | input     |      |             |
| lc_en_dec_o | output    |      |             |
## Signals
| Name      | Type                             | Description |
| --------- | -------------------------------- | ----------- |
| lc_en     | logic [lc_ctrl_pkg::TxWidth-1:0] |             |
| lc_en_out | logic [lc_ctrl_pkg::TxWidth-1:0] |             |
