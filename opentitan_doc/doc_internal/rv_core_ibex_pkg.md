# Package: rv_core_ibex_pkg

- **File**: rv_core_ibex_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 rv_core_ibex package
 

## Types

| Name          | Type                                                                                                                                                                                                                                             | Description |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| alert_event_e | enum logic [1:0] {<br><span style="padding-left:20px">     EventOn = 2'b10,<br><span style="padding-left:20px">     EventOff = 2'b01   }                                                                                                         |             |
| alert_event_t | alert_event_e                                                                                                                                                                                                                                    |             |
| region_cfg_t  | struct packed {<br><span style="padding-left:20px">     logic en;<br><span style="padding-left:20px">     logic [31:0] matching_region;<br><span style="padding-left:20px">     logic [31:0] remap_addr;<br><span style="padding-left:20px">   } |             |
