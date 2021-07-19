# Entity: AxiStreamPacketizer

- **File**: AxiStreamPacketizer.vhd
## Diagram

![Diagram](AxiStreamPacketizer.svg "Diagram")
## Description

Title      : AxiStreamPackerizerV0 Protocol: https://confluence.slac.stanford.edu/x/1oyfD
Company    : SLAC National Accelerator Laboratory
Description: AXI stream DePacketerizer Module (non-interleave only)
   Formats an AXI-Stream for a transport link.
   Sideband fields are placed into the data stream in a header.
   Long frames are broken into smaller packets.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name         | Type            | Value | Description                         |
| -------------------- | --------------- | ----- | ----------------------------------- |
| TPD_G                | time            | 1 ns  |                                     |
| MAX_PACKET_BYTES_G   | integer         | 1440  | Must be a multiple of 8             |
| MIN_TKEEP_G          | slv(7 downto 0) | x"01" |                                     |
| OUTPUT_SSI_G         | boolean         | true  | SSI compliant output (SOF on tuser) |
| INPUT_PIPE_STAGES_G  | integer         | 0     |                                     |
| OUTPUT_PIPE_STAGES_G | integer         | 0     |                                     |
## Ports

| Port name   | Direction | Type                                          | Description                                                   |
| ----------- | --------- | --------------------------------------------- | ------------------------------------------------------------- |
| axisClk     | in        | sl                                            | AXI-Lite Interface for local registers                        |
| axisRst     | in        | sl                                            |                                                               |
| maxPktBytes | in        | slv(bitSize(MAX_PACKET_BYTES_G) - 1 downto 0) | Actual byte count; will be truncated to multiple of word-size |
| sAxisMaster | in        | AxiStreamMasterType                           |                                                               |
| sAxisSlave  | out       | AxiStreamSlaveType                            |                                                               |
| mAxisMaster | out       | AxiStreamMasterType                           |                                                               |
| mAxisSlave  | in        | AxiStreamSlaveType                            |                                                               |
## Signals

| Name             | Type                | Description |
| ---------------- | ------------------- | ----------- |
| r                | RegType             |             |
| rin              | RegType             |             |
| inputAxisMaster  | AxiStreamMasterType |             |
| inputAxisSlave   | AxiStreamSlaveType  |             |
| outputAxisMaster | AxiStreamMasterType |             |
| outputAxisSlave  | AxiStreamSlaveType  |             |
| maxWords         | WordCounterType     |             |
## Constants

| Name             | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| LD_WORD_SIZE_C   | positive            |  3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| WORD_SIZE_C      | positive            |  2**LD_WORD_SIZE_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| PROTO_WORDS_C    | positive            |  3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| MAX_WORD_COUNT_C | WordCounterType     |  to_unsigned(MAX_PACKET_BYTES_G / WORD_SIZE_C,<br><span style="padding-left:20px"> WordCounterType'length)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |             |
| AXIS_CONFIG_C    | AxiStreamConfigType |  (       TSTRB_EN_C    => false,<br><span style="padding-left:20px">       TDATA_BYTES_C => 8,<br><span style="padding-left:20px">       TDEST_BITS_C  => 0,<br><span style="padding-left:20px">       TID_BITS_C    => 0,<br><span style="padding-left:20px">       TKEEP_MODE_C  => TKEEP_NORMAL_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => ite(OUTPUT_SSI_G,<br><span style="padding-left:20px"> 2,<br><span style="padding-left:20px"> 0),<br><span style="padding-left:20px">       TUSER_MODE_C  => TUSER_FIRST_LAST_C)                                                                                                                                                                                                                       |             |
| VERSION_C        | slv(3 downto 0)     |  "0000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C       | RegType             |  (       state            => IDLE_S,<br><span style="padding-left:20px">       frameNumber      => (others => '0'),<br><span style="padding-left:20px">       packetNumber     => (others => '0'),<br><span style="padding-left:20px">       wordCount        => (others => '0'),<br><span style="padding-left:20px">       maxWords         => to_unsigned(1,<br><span style="padding-left:20px"> WordCounterType'length),<br><span style="padding-left:20px">       eof              => '0',<br><span style="padding-left:20px">       tUserLast        => (others => '0'),<br><span style="padding-left:20px">       inputAxisSlave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       outputAxisMaster => axiStreamMasterInit(AXIS_CONFIG_C)) |             |
## Types

| Name      | Type                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> TAIL_S)  |             |
| RegType   |                                                                                                    |             |
## Processes
- comb: ( axisRst, inputAxisMaster, outputAxisSlave, r, maxWords )
- seq: ( axisClk )
## Instantiations

- U_Input: surf.AxiStreamPipeline
**Description**
Input pipeline

- U_Output: surf.AxiStreamPipeline
**Description**
Output pipeline

