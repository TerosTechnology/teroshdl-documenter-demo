# Entity: AxiStreamDmaV2Write

- **File**: AxiStreamDmaV2Write.vhd
## Diagram

![Diagram](AxiStreamDmaV2Write.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Block to transfer a single AXI Stream frame into memory using an AXI
 interface. Version 2 supports interleaved frames.
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

| Generic name      | Type                    | Value | Description |
| ----------------- | ----------------------- | ----- | ----------- |
| TPD_G             | time                    | 1 ns  |             |
| AXI_READY_EN_G    | boolean                 | false |             |
| AXIS_CONFIG_G     | AxiStreamConfigType     |       |             |
| AXI_CONFIG_G      | AxiConfigType           |       |             |
| PIPE_STAGES_G     | natural                 | 1     |             |
| BURST_BYTES_G     | integer range 1 to 4096 | 4096  |             |
| ACK_WAIT_BVALID_G | boolean                 | true  |             |
## Ports

| Port name       | Direction | Type                   | Description                                  |
| --------------- | --------- | ---------------------- | -------------------------------------------- |
| axiClk          | in        | sl                     | Clock/Reset                                  |
| axiRst          | in        | sl                     |                                              |
| dmaWrDescReq    | out       | AxiWriteDmaDescReqType | DMA write descriptor request, ack and return |
| dmaWrDescAck    | in        | AxiWriteDmaDescAckType |                                              |
| dmaWrDescRet    | out       | AxiWriteDmaDescRetType |                                              |
| dmaWrDescRetAck | in        | sl                     |                                              |
| dmaWrIdle       | out       | sl                     | Config and status                            |
| axiCache        | in        | slv(3 downto 0)        |                                              |
| axisMaster      | in        | AxiStreamMasterType    | Streaming Interface                          |
| axisSlave       | out       | AxiStreamSlaveType     |                                              |
| axiWriteMaster  | out       | AxiWriteMasterType     | AXI Interface                                |
| axiWriteSlave   | in        | AxiWriteSlaveType      |                                              |
| axiWriteCtrl    | in        | AxiCtrlType            |                                              |
## Signals

| Name          | Type                                       | Description |
| ------------- | ------------------------------------------ | ----------- |
| r             | RegType                                    |             |
| rin           | RegType                                    |             |
| pause         | sl                                         |             |
| intAxisMaster | AxiStreamMasterType                        |             |
| intAxisSlave  | AxiStreamSlaveType                         |             |
| trackDin      | slv(AXI_WRITE_DMA_TRACK_SIZE_C-1 downto 0) |             |
| trackDout     | slv(AXI_WRITE_DMA_TRACK_SIZE_C-1 downto 0) |             |
| trackData     | AxiWriteDmaTrackType                       |             |
## Constants

| Name              | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ----------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DATA_BYTES_C      | integer |  AXIS_CONFIG_G.TDATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| ADDR_LSB_C        | integer |  bitSize(DATA_BYTES_C-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| FIFO_ADDR_WIDTH_C | natural |  (AXI_CONFIG_G.LEN_BITS_C+1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| REG_INIT_C        | RegType |  (       dmaWrDescReq  => AXI_WRITE_DMA_DESC_REQ_INIT_C,<br><span style="padding-left:20px">       dmaWrTrack    => AXI_WRITE_DMA_TRACK_INIT_C,<br><span style="padding-left:20px">       dmaWrDescRet  => AXI_WRITE_DMA_DESC_RET_INIT_C,<br><span style="padding-left:20px">       result        => (others => '0'),<br><span style="padding-left:20px">       reqCount      => (others => '0'),<br><span style="padding-left:20px">       ackCount      => (others => '0'),<br><span style="padding-left:20px">       stCount       => (others => '0'),<br><span style="padding-left:20px">       awlen         => (others => '0'),<br><span style="padding-left:20px">       axiLen        => AXI_LEN_INIT_C,<br><span style="padding-left:20px">       wMaster       => axiWriteMasterInit(AXI_CONFIG_G,<br><span style="padding-left:20px"> '1',<br><span style="padding-left:20px"> "01",<br><span style="padding-left:20px"> "0000"),<br><span style="padding-left:20px">       slave         => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       state         => RESET_S,<br><span style="padding-left:20px">       lastUser      => (others=>'0'),<br><span style="padding-left:20px">       continue      => '0',<br><span style="padding-left:20px">       dmaWrIdle     => '0') |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( RESET_S,<br><span style="padding-left:20px"> INIT_S,<br><span style="padding-left:20px"> IDLE_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> ADDR_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> PAD_S,<br><span style="padding-left:20px"> META_S,<br><span style="padding-left:20px"> RETURN_S,<br><span style="padding-left:20px"> DUMP_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
## Processes
- comb: ( axiRst, axiWriteSlave, dmaWrDescAck, dmaWrDescRetAck,
                   intAxisMaster, trackData, pause, r, axiCache )
</br>**Description**
 State machine 
- seq: ( axiClk )
## Instantiations

- U_Pipeline: surf.AxiStreamPipeline
- U_TrackRam: surf.DualPortRam
</br>**Description**
------------------------
 Tracking RAM
------------------------

