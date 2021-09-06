# Entity: entropy_src_bucket_ht

- **File**: entropy_src_bucket_ht.sv
## Diagram

![Diagram](entropy_src_bucket_ht.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Description: entropy_src bucket health test module


## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| RegWidth     | int  | 16    |             |
| RngBusWidth  | int  | 4     |             |
## Ports

| Port name           | Direction | Type              | Description        |
| ------------------- | --------- | ----------------- | ------------------ |
| clk_i               | input     |                   |                    |
| rst_ni              | input     |                   |                    |
| entropy_bit_i       | input     | [RngBusWidth-1:0] |  ins req interface |
| entropy_bit_vld_i   | input     |                   |                    |
| clear_i             | input     |                   |                    |
| active_i            | input     |                   |                    |
| thresh_i            | input     | [RegWidth-1:0]    |                    |
| window_wrap_pulse_i | input     |                   |                    |
| test_cnt_o          | output    | [RegWidth-1:0]    |                    |
| test_fail_pulse_o   | output    |                   |                    |
## Signals

| Name                   | Type                 | Description |
| ---------------------- | -------------------- | ----------- |
| bin_incr               | logic [NUM_BINS-1:0] |  signals    |
| bin_cnt_exceeds_thresh | logic [NUM_BINS-1:0] |             |
| test_cnt_q             | logic [RegWidth-1:0] |  flops      |
| test_cnt_d             | logic [RegWidth-1:0] |  flops      |
| bin_cntr_q             | logic [RegWidth-1:0] |             |
| bin_cntr_d             | logic [RegWidth-1:0] |             |
## Constants

| Name     | Type | Value          | Description |
| -------- | ---- | -------------- | ----------- |
| NUM_BINS | int  | 2**RngBusWidth |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
