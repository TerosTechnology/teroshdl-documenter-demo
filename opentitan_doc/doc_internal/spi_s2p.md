# Entity: spi_s2p

- **File**: spi_s2p.sv
## Diagram

![Diagram](spi_s2p.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 SPI Serial-to-Parallel interface

## Ports

| Port name    | Direction | Type          | Description         |
| ------------ | --------- | ------------- | ------------------- |
| clk_i        | input     |               |                     |
| rst_ni       | input     |               | inverted CSb input  |
| s_i          | input     | [3:0]         |  SPI data           |
| data_valid_o | output    |               |  to following logic |
| data_o       | output    | spi_byte_t    |                     |
| bitcnt_o     | output    | [BitCntW-1:0] | up to 256B payload  |
| order_i      | input     |               |  Configuration      |
| io_mode_i    | input     |               |                     |
## Signals

| Name   | Type       | Description |
| ------ | ---------- | ----------- |
| cnt    | count_t    |             |
| bitcnt | bitcount_t |             |
| data_d | spi_byte_t |             |
| data_q | spi_byte_t |             |
## Constants

| Name     | Type         | Value             | Description                                                                                                                                                                                      |
| -------- | ------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Bits     | int unsigned | $bits(spi_byte_t) | ///////////////  Definitions // ///////////////  Maximum Length of a transaction is:  8 bit opcode + 24 or 32 bit address +  max 8 bit dummy cycle + 256B payload  Or in FwMode, half of DPSRAM  |
| BitWidth | int unsigned | $clog2(Bits)      |                                                                                                                                                                                                  |
## Types

| Name       | Type                 | Description |
| ---------- | -------------------- | ----------- |
| count_t    | logic [BitWidth-1:0] |             |
| bitcount_t | logic [BitCntW-1:0]  |             |
## Processes
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
**Description**
 total bit count 
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
**Description**
 Bitcount in a byte 
- unnamed: (  )
  - **Type:** always_comb
**Description**
 data valid 
