# Entity: entropy_src_watermark_reg

- **File**: entropy_src_watermark_reg.sv
## Diagram

![Diagram](entropy_src_watermark_reg.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: entropy_src high or how watermark register module
 
## Generics

| Generic name  | Type | Value | Description |
| ------------- | ---- | ----- | ----------- |
| RegWidth      | int  | 16    |             |
| HighWatermark | bit  | 1     |             |
## Ports

| Port name | Direction | Type           | Description          |
| --------- | --------- | -------------- | -------------------- |
| clk_i     | input     |                |                      |
| rst_ni    | input     |                |                      |
| clear_i   | input     |                | functional interface |
| active_i  | input     |                |                      |
| event_i   | input     |                |                      |
| value_i   | input     | [RegWidth-1:0] |                      |
| value_o   | output    | [RegWidth-1:0] |                      |
## Signals

| Name              | Type                 | Description |
| ----------------- | -------------------- | ----------- |
| event_cntr_change | logic [RegWidth-1:0] | signals     |
| reg_reset         | logic [RegWidth-1:0] |             |
| event_cntr_q      | logic [RegWidth-1:0] | flops       |
| event_cntr_d      | logic [RegWidth-1:0] | flops       |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
