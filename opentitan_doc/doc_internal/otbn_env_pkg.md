# Package: otbn_env_pkg

- **File**: otbn_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name   | Type    | Description |
| ------ | ------- | ----------- |
| helper | chandle |             |
| index  | chandle |             |
## Constants

| Name           | Type         | Value                                                                                      | Description                                                                                                 |
| -------------- | ------------ | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| LIST_OF_ALERTS | string       | {<br><span style="padding-left:20px">"fatal",<br><span style="padding-left:20px"> "recov"} | parameters                                                                                                  |
| uint           | uint         | otbn_reg_pkg::NumAlerts                                                                    |                                                                                                             |
| MNEM_STR_LEN   | int unsigned | 16                                                                                         | Used for coverage in otbn_env_cov.sv (where we need to convert string mnemonics to a packed integral type)  |
## Types

| Name                 | Type                                                                                                                                                                                                                                                              | Description                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| idle_vif             | virtual pins_if #(1)                                                                                                                                                                                                                                              | typedefs                                                                                                                  |
| tl_source_t          | logic [TL_AIW-1:0]                                                                                                                                                                                                                                                |                                                                                                                           |
| otbn_exp_read_data_t | struct packed {<br><span style="padding-left:20px">     bit                upd;<br><span style="padding-left:20px">     logic              chk;<br><span style="padding-left:20px">     logic [BUS_DW-1:0] val;<br><span style="padding-left:20px">   }           | Expected data for a pending read (see exp_read_values in otbn_scoreboard.sv)                                              |
| mnem_str_t           | bit [MNEM_STR_LEN*8-1:0]                                                                                                                                                                                                                                          |                                                                                                                           |
| otbn_loaded_word     | struct packed {<br><span style="padding-left:20px">          bit           for_imem;<br><span style="padding-left:20px">          bit [21:0]    offset;<br><span style="padding-left:20px">          bit [31:0]    data;<br><span style="padding-left:20px">    } | A very simple wrapper around a word that has been loaded from the input binary and needs storing to OTBN's IMEM or DMEM.  |
| stack_fullness_e     | enum {<br><span style="padding-left:20px">     StackEmpty,<br><span style="padding-left:20px">     StackPartial,<br><span style="padding-left:20px">     StackFull   }                                                                                            |                                                                                                                           |
| call_stack_flags_t   | struct packed {<br><span style="padding-left:20px">     logic pop_a;<br><span style="padding-left:20px">     logic pop_b;<br><span style="padding-left:20px">     logic push;<br><span style="padding-left:20px">   }                                             |                                                                                                                           |
