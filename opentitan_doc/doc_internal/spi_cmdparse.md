# Entity: spi_cmdparse

- **File**: spi_cmdparse.sv
## Diagram

![Diagram](spi_cmdparse.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 SPI Device Flash/ Passthrough mode Command Parser

 This module decodes the incoming SPI Flash commands. Then activates proper
 downstream module.

## Ports

| Port name        | Direction | Type              | Description                                                                                                                                                                                                                                                                                                      |
| ---------------- | --------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| clk_i            | input     |                   |                                                                                                                                                                                                                                                                                                                  |
| rst_ni           | input     |                   |                                                                                                                                                                                                                                                                                                                  |
| data_valid_i     | input     |                   |  Data from spi_s2p                                                                                                                                                                                                                                                                                               |
| data_i           | input     | spi_byte_t        |                                                                                                                                                                                                                                                                                                                  |
| spi_mode_i       | input     | spi_mode_e        |  Configurations                                                                                                                                                                                                                                                                                                  |
| cmd_info_i       | input     | [NumCmdInfo-1:0]  |  Command info slot  cmdparse uses the command info slot to activate sub-datapath. It uses  pre-assigned index and search opcode. e.g) if cmdslot[0].opcode == 'h03,  then if received opcode matches to the cmdslot[0] opcode, then it activates  Read Status module as Index 0 is pre-assigned to Read Status.  |
| io_mode_o        | output    | io_mode_e         |  control to spi_s2p                                                                                                                                                                                                                                                                                              |
| sel_dp_o         | output    | sel_datapath_e    |  Activate downstream modules cmd_info_o is a registered output, latched at 8th posedge SCK                                                                                                                                                                                                                       |
| cmd_info_o       | output    | cmd_info_t        |                                                                                                                                                                                                                                                                                                                  |
| cmd_info_idx_o   | output    | [CmdInfoIdxW-1:0] |                                                                                                                                                                                                                                                                                                                  |
| cmd_config_req_o | output    |                   |  Command Config is not implemented yet. Indicator of command config. The pulse is generated at 3rd bit position  of Opcode. The upper 5 bits are used as address to fetch command configs  from DPSRAM.                                                                                                          |
| cmd_config_idx_o | output    | [4:0]             |                                                                                                                                                                                                                                                                                                                  |
## Signals

| Name                   | Type                    | Description                                                                                                                                                                  |
| ---------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unused_cmdinfo_members | logic                   |  Only opcode in the cmd_info is used. Tie the rest of the members.                                                                                                           |
| st                     | st_e                    |                                                                                                                                                                              |
| st_d                   | st_e                    |                                                                                                                                                                              |
| sel_dp                 | sel_datapath_e          | //////////  Signal // //////////                                                                                                                                             |
| latch_cmdinfo          | logic                   |  FSM asserts latching enable signal for cmd_info in 8th opcode cycle.                                                                                                        |
| cmd_info_d             | cmd_info_t              |                                                                                                                                                                              |
| cmd_info_idx_d         | logic [CmdInfoIdxW-1:0] |                                                                                                                                                                              |
| module_active          | logic                   |  the logic operates only when module_active condition is met                                                                                                                 |
| in_flashmode           | logic                   |                                                                                                                                                                              |
| in_passthrough         | logic                   |                                                                                                                                                                              |
| opcode_readstatus      | logic                   |  below signals are used in the FSM to determine to activate a certain  datapath based on the received input (opcode). The opcode is the SW  configurable CSRs `cmd_info_i`.  |
| opcode_readjedec       | logic                   |  below signals are used in the FSM to determine to activate a certain  datapath based on the received input (opcode). The opcode is the SW  configurable CSRs `cmd_info_i`.  |
| opcode_readsfdp        | logic                   |  below signals are used in the FSM to determine to activate a certain  datapath based on the received input (opcode). The opcode is the SW  configurable CSRs `cmd_info_i`.  |
| opcode_readcmd         | logic                   |  below signals are used in the FSM to determine to activate a certain  datapath based on the received input (opcode). The opcode is the SW  configurable CSRs `cmd_info_i`.  |
| upload                 | logic                   |  Check upload field in the cmd_info                                                                                                                                          |
## Types

| Name            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                               |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| st_e            | enum logic [2:0] {<br><span style="padding-left:20px">                         StIdle,<br><span style="padding-left:20px">                StStatus,<br><span style="padding-left:20px">     StSfdp,<br><span style="padding-left:20px">     StJedec,<br><span style="padding-left:20px">           StReadCmd,<br><span style="padding-left:20px">      StUpload,<br><span style="padding-left:20px">           StWait   }                                                                                                                                                                                                                                                                                                                       | //////////////  Definition // //////////////                                                                                                                                              |
| spi_flash_cmd_e | enum logic [7:0] {<br><span style="padding-left:20px">     OpReadStatus1 = 'h 05,<br><span style="padding-left:20px">     OpReadStatus2 = 'h 35,<br><span style="padding-left:20px">     OpReadStatus3 = 'h 15,<br><span style="padding-left:20px">     OpReadJEDEC   = 'h 9F,<br><span style="padding-left:20px">     OpReadSfdp    = 'h 5A,<br><span style="padding-left:20px">     OpReadNormal  = 'h 03,<br><span style="padding-left:20px">     OpReadFast    = 'h 0B,<br><span style="padding-left:20px">     OpReadDual    = 'h 3B,<br><span style="padding-left:20px">     OpReadQuad    = 'h 6B,<br><span style="padding-left:20px">          OpReadDualIO  = 'h BB,<br><span style="padding-left:20px">     OpReadQuadIO  = 'h EB   } |  spi_flash_cmd_e defines HW supported (TBD for IO) commands.  If received SPI Flash command falls into one of these commands, the module  processes the command without SW intervention.  |
## Processes
- unnamed: (  )
  - **Type:** always_comb
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
**Description**
 cmd_info latch  TODO: This can be furthur optimized. At 7th beat, check the opcode[7:1]  with cmd_info[NumCmdInfo-1:0].opcode[7:1]. Unless SW configures more than  one cmd_info slots with same opcode, at most two slots match with the  opcode[7:1]. The two can be latched then at 8th beat, only the last bit  of the opcode in the two cmd_info entries can be compared.<br>  It reduces the logic from 8bit compare with 24 logic depth into 1bit  compare with 1 logic depth. 
- unnamed: (  )
  - **Type:** always_comb
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
- unnamed: (  )
  - **Type:** always_comb
