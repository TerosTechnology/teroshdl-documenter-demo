# Package: bus_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Types

| Name      | Type                                                                                                                                                                                                                                       | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| bus_reg_t | struct packed {<br><span style="padding-left:20px">     logic [11:0] addr;<br><span style="padding-left:20px">     logic [31:0] wdata;<br><span style="padding-left:20px">     logic        write;<br><span style="padding-left:20px">   } |             |
| reg_bus_t | struct packed {<br><span style="padding-left:20px">     logic [31:0] rdata;<br><span style="padding-left:20px">   }                                                                                                                        |             |
