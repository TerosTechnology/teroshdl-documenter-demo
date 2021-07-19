# Entity: rstmgr_crash_info

- **File**: rstmgr_crash_info.sv
## Diagram

![Diagram](rstmgr_crash_info.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module implements the crash dump functionality
 
## Generics

| Generic name   | Type | Value                                     | Description |
| -------------- | ---- | ----------------------------------------- | ----------- |
| CrashDumpWidth | int  | 32                                        |             |
| CrashRemainder | int  | CrashDumpWidth % RdWidth > 0 ? 1 : 0      |             |
| CrashStoreSlot | int  | CrashDumpWidth / RdWidth + CrashRemainder |             |
| SlotCntWidth   | int  | $clog2(CrashStoreSlot)                    |             |
## Ports

| Port name      | Direction | Type                 | Description |
| -------------- | --------- | -------------------- | ----------- |
| clk_i          | input     |                      |             |
| rst_ni         | input     |                      |             |
| dump_i         | input     | [CrashDumpWidth-1:0] |             |
| dump_capture_i | input     |                      |             |
| slot_sel_i     | input     | [IdxWidth-1:0]       |             |
| slots_cnt_o    | output    | [IdxWidth-1:0]       |             |
| slot_o         | output    | [RdWidth-1:0]        |             |
## Signals

| Name    | Type                                     | Description |
| ------- | ---------------------------------------- | ----------- |
| slots   | logic [2**SlotCntWidth-1:0][RdWidth-1:0] |             |
| slots_q | logic [ CrashStoreSlot-1:0][RdWidth-1:0] |             |
## Constants

| Name           | Type | Value                                     | Description |
| -------------- | ---- | ----------------------------------------- | ----------- |
| CrashRemainder | int  | CrashDumpWidth % RdWidth > 0 ? 1 : 0      |             |
| CrashStoreSlot | int  | CrashDumpWidth / RdWidth + CrashRemainder |             |
| SlotCntWidth   | int  | $clog2(CrashStoreSlot)                    |             |
| TotalWidth     | int  | CrashStoreSlot * RdWidth                  |             |
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
- unnamed: (  )
