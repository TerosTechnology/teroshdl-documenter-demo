# Entity: tlul_assert_multiple

- **File**: tlul_assert_multiple.sv
## Diagram

![Diagram](tlul_assert_multiple.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Protocol checker for multiple TL-UL ports
 
## Generics

| Generic name | Type         | Value    | Description               |
| ------------ | ------------ | -------- | ------------------------- |
| N            | int unsigned | 2        |                           |
| EndpointType |              | "Device" | can be "Device" or "Host" |
## Ports

| Port name | Direction | Type | Description     |
| --------- | --------- | ---- | --------------- |
| clk_i     | input     |      |                 |
| rst_ni    | input     |      |                 |
| h2d       | input     |      | tile link ports |
| d2h       | input     |      |                 |
