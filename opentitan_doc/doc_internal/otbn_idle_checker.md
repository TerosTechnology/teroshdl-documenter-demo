# Entity: otbn_idle_checker

## Diagram

![Diagram](otbn_idle_checker.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Ports

| Port name | Direction | Type          | Description |
| --------- | --------- | ------------- | ----------- |
| clk_i     | input     |               |             |
| rst_ni    | input     |               |             |
| reg2hw    | input     | otbn_reg2hw_t |             |
| done_i    | input     |               |             |
| idle_o_i  | input     |               |             |
## Signals

| Name      | Type  | Description                                                                                                                                                                                          |
| --------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cmd_start | logic | Detect writes of 1 to CMD.START (the "start" bit has been eaten by reggen because the register only contains the one bit).                                                                           |
| running_q | logic | Our model of whether OTBN is running or not. We start on cmd_start if we're not already running and stop on done if we are. Note that the "running" signal includes the cycle that we see cmd_start  |
| running_d | logic | Our model of whether OTBN is running or not. We start on cmd_start if we're not already running and stop on done if we are. Note that the "running" signal includes the cycle that we see cmd_start  |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
