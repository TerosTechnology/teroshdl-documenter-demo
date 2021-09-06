# Package: spi_device_pkg

- **File**: spi_device_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Serial Peripheral Interface (SPI) Device module.



## Types

| Name              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| passthrough_req_t | struct packed {<br><span style="padding-left:20px">               logic       passthrough_en;<br><span style="padding-left:20px">                logic       sck;<br><span style="padding-left:20px">     logic       sck_gate_en;<br><span style="padding-left:20px">      logic       sck_en;<br><span style="padding-left:20px">                     logic       csb;<br><span style="padding-left:20px">     logic       csb_en;<br><span style="padding-left:20px">           logic [3:0] s;<br><span style="padding-left:20px">     logic [3:0] s_en;<br><span style="padding-left:20px">   } |             |
| passthrough_rsp_t | struct packed {<br><span style="padding-left:20px">          logic [3:0] s;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
