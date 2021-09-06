# Package: uart_env_pkg

- **File**: uart_env_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Constants

| Name           | Type   | Value                                               | Description   |
| -------------- | ------ | --------------------------------------------------- | ------------- |
| uint           | uint   | 32                                                  |  local types  |
| uint           | uint   | 1                                                   |  alerts       |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |               |
## Types

| Name        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| uart_intr_e | enum int {<br><span style="padding-left:20px">     TxWatermark = 0,<br><span style="padding-left:20px">     RxWatermark = 1,<br><span style="padding-left:20px">     TxEmpty     = 2,<br><span style="padding-left:20px">     RxOverflow  = 3,<br><span style="padding-left:20px">     RxFrameErr  = 4,<br><span style="padding-left:20px">     RxBreakErr  = 5,<br><span style="padding-left:20px">     RxTimeout   = 6,<br><span style="padding-left:20px">     RxParityErr = 7,<br><span style="padding-left:20px">     NumUartIntr = 8   } |             |
## Functions
- get_watermark_bytes_by_level <font id="function_arguments">(int lvl,<br><span style="padding-left:20px"> uart_dir_e)</font> <font id="function_return">return (int)</font>
</br>**Description**
 get the number of bytes that triggers watermark interrupt

- get_break_bytes_by_level <font id="function_arguments">(int)</font> <font id="function_return">return (int)</font>
</br>**Description**
 get the number of bytes that triggers break interrupt

- get_nco <font id="function_arguments">(baud_rate_e baud_rate,<br><span style="padding-left:20px"> int clk_freq_mhz,<br><span style="padding-left:20px"> int nco_width)</font> <font id="function_return">return (int)</font>
</br>**Description**
 calculate the nco

