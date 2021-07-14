# Package: spi_device_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name               | Type                          | Description |
| ------------------ | ----------------------------- | ----------- |
| msg_id             | string                        |             |
| get_mirrored_value | get_allocated_sram_size_bytes |             |
| get_mirrored_value | get_allocated_sram_size_bytes |             |
| get_mirrored_value | get_allocated_sram_size_bytes |             |
## Constants

| Name               | Type   | Value                                               | Description      |
| ------------------ | ------ | --------------------------------------------------- | ---------------- |
| uint               | uint   | 1                                                   | alerts           |
| LIST_OF_ALERTS     | string | {<br><span style="padding-left:20px">"fatal_fault"} |                  |
| uint               | uint   | 'h1000                                              | SPI SRAM is 2kB  |
| uint               | uint   | 4096                                                | 672 depth        |
| uint               | uint   | $clog2(SRAM_SIZE) - 1                               |                  |
| SRAM_PTR_PHASE_BIT | uint   | SRAM_MSB + 1                                        |                  |
| uint               | uint   | 4                                                   |                  |
| uint               | uint   | 8                                                   |                  |
## Types

| Name              | Type                                                                                                                                                                                                                                                                                                                                                                                                     | Description                 |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| spi_device_intr_e | enum {<br><span style="padding-left:20px">     RxFifoFull,<br><span style="padding-left:20px">     RxFifoGeLevel,<br><span style="padding-left:20px">     TxFifoLtLevel,<br><span style="padding-left:20px">     RxFwModeErr,<br><span style="padding-left:20px">     RxFifoOverflow,<br><span style="padding-left:20px">     TxFifoUnderflow,<br><span style="padding-left:20px">     NumSpiDevIntr   } | local parameters and types  |
| sram_avail_type_e | enum bit {<br><span style="padding-left:20px">     SramDataAvail,<br><span style="padding-left:20px">     SramSpaceAvail   }                                                                                                                                                                                                                                                                             |                             |
## Functions
- get_sram_space_bytes <font id="function_arguments">(uint wptr,<br><span style="padding-left:20px"> uint rpt)</font> <font id="function_return">return (uint)</font>
**Description**
functions
get size of empty space in mem

- get_sram_filled_bytes <font id="function_arguments">(uint wptr,<br><span style="padding-left:20px"> uint rpt)</font> <font id="function_return">return (uint)</font>
**Description**
get size of filled data in mem

- get_allocated_sram_size_bytes <font id="function_arguments">(uint base,<br><span style="padding-left:20px"> uint)</font> <font id="function_return">return (uint)</font>
**Description**
get the memory size

- get_sram_new_ptr <font id="function_arguments">(uint ptr,<br><span style="padding-left:20px">)</font> <font id="function_return">return (uint)</font>
**Description**
use this function to calculate the new ptr value
if new rx_rptr exceeds programmed sram size in bytes, then wrap it and flip the phase bit
else, restore the 'saved' phase bit

