# Entity: sha2_pad

- **File**: sha2_pad.sv
## Diagram

![Diagram](sha2_pad.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 SHA-256 Padding logic


## Ports

| Port name         | Direction | Type       | Description                             |
| ----------------- | --------- | ---------- | --------------------------------------- |
| clk_i             | input     |            |                                         |
| rst_ni            | input     |            |                                         |
| wipe_secret       | input     |            |                                         |
| wipe_v            | input     | sha_word_t |                                         |
| fifo_rvalid       | input     |            |  To actual FIFO                         |
| fifo_rdata        | input     | sha_fifo_t |                                         |
| fifo_rready       | output    |            |                                         |
| shaf_rvalid       | output    |            |  from SHA2 compress engine              |
| shaf_rdata        | output    | sha_word_t |                                         |
| shaf_rready       | input     |            |                                         |
| sha_en            | input     |            |                                         |
| hash_start        | input     |            |                                         |
| hash_process      | input     |            |                                         |
| hash_done         | input     |            |                                         |
| message_length    | input     | [63:0]     | # of bytes in bits (8 bits granularity) |
| msg_feed_complete | output    |            | Indicates, all message is feeded        |
## Signals

| Name              | Type         | Description                              |
| ----------------- | ------------ | ---------------------------------------- |
| tx_count          | logic [63:0] | fin received data count.                 |
| inc_txcount       | logic        |                                          |
| fifo_partial      | logic        |                                          |
| txcnt_eq_1a0      | logic        |                                          |
| hash_process_flag | logic        | Set by hash_process, clear by hash_done  |
| sel_data          | sel_data_e   |                                          |
| st_q              | pad_st_e     |                                          |
| st_d              | pad_st_e     |                                          |
## Types

| Name       | Type                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sel_data_e | enum logic [2:0] {<br><span style="padding-left:20px">     FifoIn,<br><span style="padding-left:20px">              Pad80,<br><span style="padding-left:20px">               Pad00,<br><span style="padding-left:20px">               LenHi,<br><span style="padding-left:20px">               LenLo              }                              |  Data path: fout_wdata                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| pad_st_e   | enum logic [2:0] {<br><span style="padding-left:20px">     StIdle,<br><span style="padding-left:20px">             StFifoReceive,<br><span style="padding-left:20px">      StPad80,<br><span style="padding-left:20px">            StPad00,<br><span style="padding-left:20px">     StLenHi,<br><span style="padding-left:20px">     StLenLo   } |  Padded length  $ceil(message_length + 8 + 64, 512) -> message_length [8:0] + 440 and ignore carry assign length_added = (message_length[8:0] + 9'h1b8) ;  fifo control  add 8'h 80 , N 8'h00, 64'h message_length  Steps  1. `hash_start` from CPU (or DMA?)  2. calculate `padded_length` from `message_length`  3. Check if tx_count == message_length, then go to 5  4. Receiving FIFO input (hand over to fifo output)  5. Padding bit 1 (8'h80) followed by 8'h00 if needed  6. Padding with length (high -> low)  State Machine  |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
</br>**Description**
 Next state 
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
</br>**Description**
 tx_count 
