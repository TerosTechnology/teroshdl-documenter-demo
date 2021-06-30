# Entity: otbn_stack

## Diagram

![Diagram](otbn_stack.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| StackWidth   | int unsigned | 32    |             |
| StackDepth   | int unsigned | 4     |             |
## Ports

| Port name   | Direction | Type             | Description                                |
| ----------- | --------- | ---------------- | ------------------------------------------ |
| clk_i       | input     |                  |                                            |
| rst_ni      | input     |                  |                                            |
| full_o      | output    |                  | Stack is full                              |
| push_i      | input     |                  | Push the data                              |
| push_data_i | input     | [StackWidth-1:0] | Data to push                               |
| pop_i       | input     |                  | Pop top of the stack                       |
| top_data_o  | output    | [StackWidth-1:0] | Data on top of the stack                   |
| top_valid_o | output    |                  | Stack is non empty (`top_data_o` is valid) |
## Signals

| Name           | Type                    | Description |
| -------------- | ----------------------- | ----------- |
| stack_storage  | logic [StackWidth-1:0]  |             |
| stack_wr_ptr_q | logic [StackDepthW:0]   |             |
| stack_wr_ptr_d | logic [StackDepthW:0]   |             |
| stack_top_idx  | logic [StackDepthW-1:0] |             |
| stack_rd_idx   | logic [StackDepthW-1:0] |             |
| stack_wr_idx   | logic [StackDepthW-1:0] |             |
| stack_empty    | logic                   |             |
| stack_full     | logic                   |             |
| stack_write    | logic                   |             |
| stack_read     | logic                   |             |
## Constants

| Name        | Type         | Value                            | Description |
| ----------- | ------------ | -------------------------------- | ----------- |
| StackDepthW | int unsigned | prim_util_pkg::vbits(StackDepth) |             |
## Processes
- unnamed: (  )
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: ( @(posedge clk_i) )
