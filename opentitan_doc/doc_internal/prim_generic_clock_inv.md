# Entity: prim_generic_clock_inv

- **File**: prim_generic_clock_inv.sv
## Diagram

![Diagram](prim_generic_clock_inv.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Clock inverter
   Varies on the process
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| HasScanMode  | bit  | 1'b1  |             |
## Ports

| Port name  | Direction | Type | Description |
| ---------- | --------- | ---- | ----------- |
| clk_i      | input     |      |             |
| scanmode_i | input     |      |             |
| clk_no     | output    |      | Inverted    |
