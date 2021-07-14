# Package: aes_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name           | Type   | Value                                                                                                            | Description |
| -------------- | ------ | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"recov_ctrl_update_err",<br><span style="padding-left:20px"> "fatal_fault"} | parameters  |
| uint           | uint   | 2                                                                                                                |             |
## Types

| Name             | Type                                                                                                                                                                                                                                           | Description |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| aes_item_type_e  | enum int {<br><span style="padding-left:20px"> AES_CFG=0,<br><span style="padding-left:20px"> AES_DATA=1,<br><span style="padding-left:20px"> AES_ERR_INJ=2 }                                                                                  |             |
| flip_rst_e       | enum bit {<br><span style="padding-left:20px"> Flip_bits = 0,<br><span style="padding-left:20px"> Pull_reset = 1 }                                                                                                                             |             |
| clear_t          | struct packed {<br><span style="padding-left:20px">     bit          dataout;<br><span style="padding-left:20px">     bit          key_iv_data_in;<br><span style="padding-left:20px">   }                                                     |             |
| error_types_t    | struct packed {<br><span style="padding-left:20px">     bit          reset;<br><span style="padding-left:20px">     bit          mal_inject;<br><span style="padding-left:20px">     bit          cfg;<br><span style="padding-left:20px">   } |             |
| cfg_error_type_t | struct packed {<br><span style="padding-left:20px">     bit          key_len;<br><span style="padding-left:20px">     bit          mode;<br><span style="padding-left:20px">   }                                                               |             |
