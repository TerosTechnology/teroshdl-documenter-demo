# Entity: entropy_src_repcnt_ht

- **File**: entropy_src_repcnt_ht.sv
## Diagram

![Diagram](entropy_src_repcnt_ht.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: entropy_src repetitive count health test module
 
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| RegWidth     | int  | 16    |             |
| RngBusWidth  | int  | 4     |             |
## Ports

| Port name         | Direction | Type              | Description       |
| ----------------- | --------- | ----------------- | ----------------- |
| clk_i             | input     |                   |                   |
| rst_ni            | input     |                   |                   |
| entropy_bit_i     | input     | [RngBusWidth-1:0] | ins req interface |
| entropy_bit_vld_i | input     |                   |                   |
| clear_i           | input     |                   |                   |
| active_i          | input     |                   |                   |
| thresh_i          | input     | [RegWidth-1:0]    |                   |
| test_cnt_o        | output    | [RegWidth-1:0]    |                   |
| test_fail_pulse_o | output    |                   |                   |
## Signals

| Name                   | Type                    | Description |
| ---------------------- | ----------------------- | ----------- |
| samples_match_pulse    | logic [RngBusWidth-1:0] | signals     |
| samples_no_match_pulse | logic [RngBusWidth-1:0] |             |
| rep_cnt_fail           | logic [RngBusWidth-1:0] |             |
| prev_sample_q          | logic [RngBusWidth-1:0] | flops       |
| prev_sample_d          | logic [RngBusWidth-1:0] | flops       |
| rep_cntr_q             | logic [RegWidth-1:0]    |             |
| rep_cntr_d             | logic [RegWidth-1:0]    |             |
| test_cnt_q             | logic [RegWidth-1:0]    |             |
| test_cnt_d             | logic [RegWidth-1:0]    |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
