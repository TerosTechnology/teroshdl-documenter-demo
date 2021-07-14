# Package: xbar_env_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 ---------------------------------------------
 Xbar environment package
 ---------------------------------------------
 

## Types

| Name        | Type                                                                                                                                                                                                                                                                                               | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tl_device_t | struct {<br><span style="padding-left:20px">     string                      device_name;<br><span style="padding-left:20px">     addr_range_t                addr_ranges[$];<br><span style="padding-left:20px">   }                                                                              |             |
| tl_host_t   | struct {<br><span style="padding-left:20px">     string                      host_name;<br><span style="padding-left:20px">     int                         host_id;<br><span style="padding-left:20px">     string                      valid_devices[$];<br><span style="padding-left:20px">   } |             |
## Functions
- get_host_id <font id="function_arguments">(string)</font> <font id="function_return">return (int)</font>
- is_valid_path <font id="function_arguments">(string host_name,<br><span style="padding-left:20px"> string device_name)</font> <font id="function_return">return (bit)</font>
- is_device_valid_addr <font id="function_arguments">(string device_name,<br><span style="padding-left:20px"> bit [top_pkg::TL_AW-1 : 0])</font> <font id="function_return">return (bit)</font>
