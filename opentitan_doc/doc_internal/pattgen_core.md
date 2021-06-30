# Entity: pattgen_core

## Diagram

![Diagram](pattgen_core.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Description: Pattgen Core Module
 
## Ports

| Port name       | Direction | Type             | Description |
| --------------- | --------- | ---------------- | ----------- |
| clk_i           | input     |                  |             |
| rst_ni          | input     |                  |             |
| reg2hw          | input     | pattgen_reg2hw_t |             |
| hw2reg          | output    | pattgen_hw2reg_t |             |
| pda0_tx_o       | output    |                  |             |
| pcl0_tx_o       | output    |                  |             |
| pda1_tx_o       | output    |                  |             |
| pcl1_tx_o       | output    |                  |             |
| intr_done_ch0_o | output    |                  |             |
| intr_done_ch1_o | output    |                  |             |
## Signals

| Name           | Type                | Description |
| -------------- | ------------------- | ----------- |
| event_done_ch0 | logic               |             |
| event_done_ch1 | logic               |             |
| ch0_ctrl       | pattgen_chan_ctrl_t |             |
| ch1_ctrl       | pattgen_chan_ctrl_t |             |
## Instantiations

- chan0: pattgen_chan
- chan1: pattgen_chan
- intr_hw_done_ch0: prim_intr_hw
- intr_hw_done_ch1: prim_intr_hw
