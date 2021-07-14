# Package: spi_host_cmd_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Command & Configuration Options structure for SPI HOST.
 

## Constants

| Name    | Type | Value                                        | Description |
| ------- | ---- | -------------------------------------------- | ----------- |
| CSW     | int  | prim_util_pkg::vbits(spi_host_reg_pkg::NumCS |             |
| CmdSize | int  | CSW + 45                                     |             |
## Types

| Name            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| reg_direction_t | enum logic [1:0] {<br><span style="padding-left:20px">      Dummy  = 2'b00,<br><span style="padding-left:20px">      RdOnly = 2'b01,<br><span style="padding-left:20px">      WrOnly = 2'b10,<br><span style="padding-left:20px">      Bidir  = 2'b11    }                                                                                                                                                                                                                                           | For decoding the direction register  |
| speed_t         | enum logic [1:0] {<br><span style="padding-left:20px">      Standard = 2'b00,<br><span style="padding-left:20px">      Dual     = 2'b01,<br><span style="padding-left:20px">      Quad     = 2'b10,<br><span style="padding-left:20px">      RsvdSpd  = 2'b11    }                                                                                                                                                                                                                                   | For decoding the direction register  |
| configopts_t    | struct packed {<br><span style="padding-left:20px">     logic [15:0] clkdiv;<br><span style="padding-left:20px">     logic [3:0]  csnidle;<br><span style="padding-left:20px">     logic [3:0]  csnlead;<br><span style="padding-left:20px">     logic [3:0]  csntrail;<br><span style="padding-left:20px">     logic        full_cyc;<br><span style="padding-left:20px">     logic        cpha;<br><span style="padding-left:20px">     logic        cpol;<br><span style="padding-left:20px">   } |                                      |
| segment_t       | struct packed {<br><span style="padding-left:20px">     logic [1:0] speed;<br><span style="padding-left:20px">     logic       cmd_wr_en;<br><span style="padding-left:20px">     logic       cmd_rd_en;<br><span style="padding-left:20px">     logic [8:0] len;<br><span style="padding-left:20px">     logic       csaat;<br><span style="padding-left:20px">   }                                                                                                                                 |                                      |
| command_t       | struct packed {<br><span style="padding-left:20px">     logic [CSW-1:0] csid;<br><span style="padding-left:20px">     segment_t segment;<br><span style="padding-left:20px">     configopts_t configopts;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                    |                                      |
