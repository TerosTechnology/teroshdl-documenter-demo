# Entity: AxiStreamDepacketizer

- **File**: AxiStreamDepacketizer.vhd
## Diagram

![Diagram](AxiStreamDepacketizer.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : AxiStreamPackerizerV0 Protocol: https://confluence.slac.stanford.edu/x/1oyfD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI stream DePacketerizer Module (non-interleave only)
    Formats an AXI-Stream for a transport link.
    Sideband fields are placed into the data stream in a header.
    Long frames are broken into smaller packets.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name         | Type    | Value | Description |
| -------------------- | ------- | ----- | ----------- |
| TPD_G                | time    | 1 ns  |             |
| INPUT_PIPE_STAGES_G  | integer | 0     |             |
| OUTPUT_PIPE_STAGES_G | integer | 0     |             |
## Ports

| Port name   | Direction | Type                | Description                                |
| ----------- | --------- | ------------------- | ------------------------------------------ |
| axisClk     | in        | sl                  | AXI-Lite Interface for local registers     |
| axisRst     | in        | sl                  |                                            |
| restart     | in        | sl                  |  Reset the expected frame number back to 0 |
| sAxisMaster | in        | AxiStreamMasterType |                                            |
| sAxisSlave  | out       | AxiStreamSlaveType  |                                            |
| mAxisMaster | out       | AxiStreamMasterType |                                            |
| mAxisSlave  | in        | AxiStreamSlaveType  |                                            |
## Signals

| Name             | Type                | Description |
| ---------------- | ------------------- | ----------- |
| r                | RegType             |             |
| rin              | RegType             |             |
| inputAxisMaster  | AxiStreamMasterType |             |
| inputAxisSlave   | AxiStreamSlaveType  |             |
| outputAxisMaster | AxiStreamMasterType |             |
| outputAxisSlave  | AxiStreamSlaveType  |             |
## Constants

| Name          | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AXIS_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => false,<br><span style="padding-left:20px">       TDATA_BYTES_C => 8,<br><span style="padding-left:20px">       TDEST_BITS_C  => 8,<br><span style="padding-left:20px">       TID_BITS_C    => 8,<br><span style="padding-left:20px">       TKEEP_MODE_C  => TKEEP_NORMAL_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => 8,<br><span style="padding-left:20px">       TUSER_MODE_C  => TUSER_FIRST_LAST_C)                                                                                                                                                                 |             |
| VERSION_C     | slv(3 downto 0)     |  "0000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |             |
| REG_INIT_C    | RegType             |  (       state            => HEADER_S,<br><span style="padding-left:20px">       frameNumber      => (others => '0'),<br><span style="padding-left:20px">       packetNumber     => (others => '0'),<br><span style="padding-left:20px">       sof              => '1',<br><span style="padding-left:20px">       startup          => '1',<br><span style="padding-left:20px">       sideband         => '0',<br><span style="padding-left:20px">       inputAxisSlave   => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       outputAxisMaster => (others => axiStreamMasterInit(AXIS_CONFIG_C))) |             |
## Types

| Name      | Type                                                                                                                                             | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | (HEADER_S,<br><span style="padding-left:20px"> BLEED_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> DONE_S)  |             |
| RegType   |                                                                                                                                                  |             |
## Processes
- comb: ( axisRst, inputAxisMaster, outputAxisSlave, r, restart )
</br>**Description**
 [in] -----------------------------------------------------------------------------------------------  Accumulation sequencing, DMA ring buffer, and AXI-Lite logic ----------------------------------------------------------------------------------------------- 
- seq: ( axisClk )
## Instantiations

- U_AxiStreamPipeline_Input: surf.AxiStreamPipeline
- U_AxiStreamPipeline_Output: surf.AxiStreamPipeline
</br>**Description**
 [in]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Output pipeline
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

