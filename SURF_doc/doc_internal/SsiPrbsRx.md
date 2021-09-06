# Entity: SsiPrbsRx

- **File**: SsiPrbsRx.vhd
## Diagram

![Diagram](SsiPrbsRx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:   This module generates
                PseudoRandom Binary Sequence (PRBS) on Virtual Channel Lane.
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

| Generic name              | Type                     | Value                             | Description             |
| ------------------------- | ------------------------ | --------------------------------- | ----------------------- |
| TPD_G                     | time                     | 1 ns                              | General Configurations  |
| STATUS_CNT_WIDTH_G        | natural range 1 to 32    | 32                                |                         |
| SLAVE_READY_EN_G          | boolean                  | true                              | FIFO configurations     |
| GEN_SYNC_FIFO_G           | boolean                  | false                             |                         |
| CASCADE_SIZE_G            | positive                 | 1                                 |                         |
| FIFO_ADDR_WIDTH_G         | positive                 | 9                                 |                         |
| FIFO_PAUSE_THRESH_G       | positive                 | 2**8                              |                         |
| SYNTH_MODE_G              | string                   | "inferred"                        |                         |
| MEMORY_TYPE_G             | string                   | "block"                           |                         |
| PRBS_SEED_SIZE_G          | positive range 32 to 512 | 32                                | PRBS Config             |
| PRBS_TAPS_G               | NaturalArray             | (0 => 31, 1 => 6, 2 => 2, 3 => 1) |                         |
| SLAVE_AXI_STREAM_CONFIG_G | AxiStreamConfigType      |                                   | AXI Stream IO Config    |
| SLAVE_AXI_PIPE_STAGES_G   | natural                  | 0                                 |                         |
## Ports

| Port name       | Direction | Type                   | Description                                                     |
| --------------- | --------- | ---------------------- | --------------------------------------------------------------- |
| sAxisClk        | in        | sl                     | Streaming RX Data Interface (sAxisClk domain)                   |
| sAxisRst        | in        | sl                     |                                                                 |
| sAxisMaster     | in        | AxiStreamMasterType    |                                                                 |
| sAxisSlave      | out       | AxiStreamSlaveType     |                                                                 |
| sAxisCtrl       | out       | AxiStreamCtrlType      |                                                                 |
| mAxisMaster     | out       | AxiStreamMasterType    | Optional: TX Data Interface with EOFE tagging (sAxisClk domain) |
| mAxisSlave      | in        | AxiStreamSlaveType     |                                                                 |
| axiClk          | in        | sl                     | Optional: AXI-Lite Register Interface (axiClk domain)           |
| axiRst          | in        | sl                     |                                                                 |
| axiReadMaster   | in        | AxiLiteReadMasterType  |                                                                 |
| axiReadSlave    | out       | AxiLiteReadSlaveType   |                                                                 |
| axiWriteMaster  | in        | AxiLiteWriteMasterType |                                                                 |
| axiWriteSlave   | out       | AxiLiteWriteSlaveType  |                                                                 |
| updatedResults  | out       | sl                     | Error Detection Signals (sAxisClk domain)                       |
| errorDet        | out       | sl                     |  '1' if any error detected                                      |
| busy            | out       | sl                     |                                                                 |
| errMissedPacket | out       | sl                     |                                                                 |
| errLength       | out       | sl                     |                                                                 |
| errDataBus      | out       | sl                     |                                                                 |
| errEofe         | out       | sl                     |                                                                 |
| errWordCnt      | out       | slv(31 downto 0)       |                                                                 |
| packetRate      | out       | slv(31 downto 0)       |                                                                 |
| packetLength    | out       | slv(31 downto 0)       |                                                                 |
## Signals

| Name                | Type                                                                                                       | Description |
| ------------------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| r                   | RegType                                                                                                    |             |
| rin                 | RegType                                                                                                    |             |
| rxAxisMaster        | AxiStreamMasterType                                                                                        |             |
| rxAxisSlave         | AxiStreamSlaveType                                                                                         |             |
| txAxisMaster        | AxiStreamMasterType                                                                                        |             |
| txAxisSlave         | AxiStreamSlaveType                                                                                         |             |
| bypCheck            | sl                                                                                                         |             |
| axisCtrl            | AxiStreamCtrlArray(1 downto 0)                                                                             |             |
| rAxiLite            | LocRegType                                                                                                 |             |
| rinAxiLite          | LocRegType                                                                                                 |             |
| errBitStrbSync      | sl                                                                                                         |             |
| errWordStrbSync     | sl                                                                                                         |             |
| errDataBusSync      | sl                                                                                                         |             |
| errEofeSync         | sl                                                                                                         |             |
| errLengthSync       | sl                                                                                                         |             |
| errMissedPacketSync | sl                                                                                                         |             |
| overflow            | slv(1 downto 0)                                                                                            |             |
| pause               | slv(1 downto 0)                                                                                            |             |
| cntOut              | SlVectorArray(STATUS_SIZE_C-1 downto 0,<br><span style="padding-left:20px"> STATUS_CNT_WIDTH_G-1 downto 0) |             |
| packetLengthSync    | slv(31 downto 0)                                                                                           |             |
| packetRateSync      | slv(31 downto 0)                                                                                           |             |
| errWordCntSync      | slv(31 downto 0)                                                                                           |             |
| pause1Cnt           | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| overflow1Cnt        | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| pause0Cnt           | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| overflow0Cnt        | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| errWordStrbCnt      | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| errDataBusCnt       | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| errEofeCnt          | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| errLengthCnt        | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
| errMissedPacketCnt  | slv(STATUS_CNT_WIDTH_G-1 downto 0)                                                                         |             |
## Constants

| Name              | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ----------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| MAX_CNT_C         | slv(31 downto 0)    |  (others => '1')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |             |
| PRBS_BYTES_C      | natural             |  wordCount(PRBS_SEED_SIZE_G,<br><span style="padding-left:20px"> 8)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| PRBS_SSI_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => false,<br><span style="padding-left:20px">       TDATA_BYTES_C => PRBS_BYTES_C,<br><span style="padding-left:20px">       TDEST_BITS_C  => 8,<br><span style="padding-left:20px">       TID_BITS_C    => 8,<br><span style="padding-left:20px">       TKEEP_MODE_C  => TKEEP_COMP_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => 8,<br><span style="padding-left:20px">       TUSER_MODE_C  => TUSER_FIRST_LAST_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C        | RegType             |  (       busy            => '1',<br><span style="padding-left:20px">       packetLength    => toSlv(2,<br><span style="padding-left:20px"> 32),<br><span style="padding-left:20px">       errorDet        => '0',<br><span style="padding-left:20px">       eofe            => '0',<br><span style="padding-left:20px">       errLength       => '0',<br><span style="padding-left:20px">       updatedResults  => '0',<br><span style="padding-left:20px">       errMissedPacket => '0',<br><span style="padding-left:20px">       errDataBus      => '0',<br><span style="padding-left:20px">       errWordStrb     => '0',<br><span style="padding-left:20px">       txCnt           => (others => '0'),<br><span style="padding-left:20px">       bitPntr         => (others => '0'),<br><span style="padding-left:20px">       errorBits       => (others => '0'),<br><span style="padding-left:20px">       errWordCnt      => (others => '0'),<br><span style="padding-left:20px">       eventCnt        => toSlv(1,<br><span style="padding-left:20px"> PRBS_SEED_SIZE_G),<br><span style="padding-left:20px">       randomData      => (others => '0'),<br><span style="padding-left:20px">       dataCnt         => (others => '0'),<br><span style="padding-left:20px">       stopTime        => (others => '0'),<br><span style="padding-left:20px">       startTime       => (others => '1'),<br><span style="padding-left:20px">       packetRate      => (others => '1'),<br><span style="padding-left:20px">       rxAxisSlave     => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       txAxisMaster    => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       state           => IDLE_S) |             |
| STATUS_SIZE_C     | positive            |  10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| LOC_REG_INIT_C    | LocRegType          |  (       cntRst        => '1',<br><span style="padding-left:20px">       bypCheck      => '0',<br><span style="padding-left:20px">       dummy         => (others => '0'),<br><span style="padding-left:20px">       rollOverEn    => (others => '0'),<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
## Types

| Name       | Type                                                                                                 | Description |
| ---------- | ---------------------------------------------------------------------------------------------------- | ----------- |
| StateType  | ( IDLE_S,<br><span style="padding-left:20px"> LENGTH_S,<br><span style="padding-left:20px"> DATA_S)  |             |
| RegType    |                                                                                                      |             |
| LocRegType |                                                                                                      |             |
## Processes
- comb: ( bypCheck, r, rxAxisMaster, sAxisRst, txAxisSlave )
- seq: ( sAxisClk )
- combAxiLite: ( axiReadMaster, axiRst, axiWriteMaster, errDataBusCnt,
                          errDataBusSync, errEofeCnt, errEofeSync,
                          errLengthCnt, errLengthSync, errMissedPacketCnt,
                          errMissedPacketSync, errWordCntSync, errWordStrbCnt,
                          errWordStrbSync, overflow, overflow0Cnt,
                          overflow1Cnt, packetLengthSync, packetRateSync,
                          pause, pause0Cnt, pause1Cnt, rAxiLite )
**Description**
-----------------------------  Configuration Register ----------------------------- 
- seqAxiLite: ( axiClk )
## Instantiations

- AxiStreamFifo_Rx: surf.AxiStreamFifoV2
- U_Tx: surf.AxiStreamGearbox
- U_bypCheck: surf.Synchronizer
- SyncFifo_Inst: surf.SynchronizerFifo
- SyncStatusVec_Inst: surf.SyncStatusVector
