# Package: flash_ctrl_env_pkg

- **File**: flash_ctrl_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name                    | Type   | Value                                                   | Description |
| ----------------------- | ------ | ------------------------------------------------------- | ----------- |
| LIST_OF_ALERTS          | string |                                                         | parameters  |
| uint                    | uint   | 4                                                       |             |
| FlashNumPages           | uint   | flash_ctrl_pkg::NumBanks * flash_ctrl_pkg::PagesPerBank |             |
| FlashSizeBytes          | uint   | FlashNumPages * flash_ctrl_pk                           |             |
| FlashNumBusWords        | uint   | FlashSizeBytes / top_pkg::TL_DBW                        |             |
| FlashNumBusWordsPerBank | uint   | FlashNumBusWords / flash_ctrl_pkg::NumBanks             |             |
| FlashNumBusWordsPerPage | uint   | FlashNumBusWordsPerBank / flash_ctrl_pkg::PagesPerBank  |             |
| FlashBankBytesPerWord   | uint   | flash_ctrl_pkg::DataWidth / 8                           |             |
| uint                    | uint   | $clog2(FlashBankBytesPerWord)                           |             |
| uint                    | uint   | $clog2(flash_ctrl_pkg::WordsPerPage)                    |             |
| uint                    | uint   | $clog2(flash_ctrl_pkg::PagesPerBank)                    |             |
| uint                    | uint   | $clog2(flash_ctrl_pkg::NumBanks)                        |             |
| uint                    | uint   | flash_ctrl_pkg::BusPgmRes                               |             |
| uint                    | uint   | $clog2(FlashPgmRes)                                     |             |
| FlashMemAddrWordMsbBit  | uint   | FlashDataByteWidth - 1                                  |             |
| FlashMemAddrLineMsbBit  | uint   | FlashDataByteWidth + FlashWordLineWidth - 1             |             |
| FlashMemAddrPageMsbBit  | uint   | FlashDataByteWidth                                      |             |
| FlashMemAddrBankMsbBit  | uint   | FlashDataByteWidth + FlashWordLineW                     |             |
## Types

| Name                  | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| flash_ctrl_intr_e     | enum int {<br><span style="padding-left:20px">     FlashCtrlIntrProgEmpty  = 0,<br><span style="padding-left:20px">     FlashCtrlIntrProgLvl    = 1,<br><span style="padding-left:20px">     FlashCtrlIntrRdFull     = 2,<br><span style="padding-left:20px">     FlashCtrlIntrRdLvl      = 3,<br><span style="padding-left:20px">     FlashCtrlIntrOpDone     = 4,<br><span style="padding-left:20px">     FlashCtrlIntrErr        = 5,<br><span style="padding-left:20px">     NumFlashCtrlIntr        = 6   }                             | types                                  |
| flash_mem_init_e      | enum {<br><span style="padding-left:20px">     FlashMemInitCustom,<br><span style="padding-left:20px">          FlashMemInitSet,<br><span style="padding-left:20px">             FlashMemInitClear,<br><span style="padding-left:20px">           FlashMemInitRandomize,<br><span style="padding-left:20px">       FlashMemInitInvalidate     }                                                                                                                                                                                              |                                        |
| flash_dv_part_e       | enum logic [flash_ctrl_pkg::InfoTypes:0] {<br><span style="padding-left:20px">      FlashPartData  = 0,<br><span style="padding-left:20px">     FlashPartInfo  = 1,<br><span style="padding-left:20px">     FlashPartInfo1 = 2,<br><span style="padding-left:20px">     FlashPartRed   = 4   }                                                                                                                                                                                                                                               | Data partition and all info partitions |
| flash_mp_region_cfg_t | struct packed {<br><span style="padding-left:20px">     bit           en;<br><span style="padding-left:20px">              bit           read_en;<br><span style="padding-left:20px">         bit           program_en;<br><span style="padding-left:20px">      bit           erase_en;<br><span style="padding-left:20px">        flash_part_e  partition;<br><span style="padding-left:20px">       uint          num_pages;<br><span style="padding-left:20px">       uint          start_page;<br><span style="padding-left:20px">    } |                                        |
| flash_op_t            | struct packed {<br><span style="padding-left:20px">     flash_dv_part_e partition;<br><span style="padding-left:20px">       flash_erase_e   erase_type;<br><span style="padding-left:20px">      flash_op_e      op;<br><span style="padding-left:20px">              uint            num_words;<br><span style="padding-left:20px">       bit [TL_AW-1:0] addr;<br><span style="padding-left:20px">          }                                                                                                                             |                                        |
