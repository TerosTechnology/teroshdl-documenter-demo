# Entity: AxiStreamRingBuffer

- **File**: AxiStreamRingBuffer.vhd
## Diagram

![Diagram](AxiStreamRingBuffer.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for simple BRAM based ring buffer with AXI Stream interface
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

| Generic name        | Type                | Value      | Description                |
| ------------------- | ------------------- | ---------- | -------------------------- |
| TPD_G               | time                | 1 ns       |                            |
| SYNTH_MODE_G        | string              | "inferred" |                            |
| MEMORY_TYPE_G       | string              | "block"    |                            |
| DATA_BYTES_G        | positive            | 16         |                            |
| RAM_ADDR_WIDTH_G    | positive            | 9          |                            |
| INT_PIPE_STAGES_G   | natural             | 1          | AXI Stream Configurations  |
| PIPE_STAGES_G       | natural             | 1          |                            |
| GEN_SYNC_FIFO_G     | boolean             | false      |                            |
| FIFO_MEMORY_TYPE_G  | string              | "block"    |                            |
| FIFO_ADDR_WIDTH_G   | positive            | 9          |                            |
| AXI_STREAM_CONFIG_G | AxiStreamConfigType |            |                            |
## Ports

| Port name       | Direction | Type                           | Description                                   |
| --------------- | --------- | ------------------------------ | --------------------------------------------- |
| dataClk         | in        | sl                             | Data to store in ring buffer (dataClk domain) |
| dataRst         | in        | sl                             |                                               |
| dataValid       | in        | sl                             |                                               |
| dataValue       | in        | slv(8*DATA_BYTES_G-1 downto 0) |                                               |
| bufferEnable    | in        | sl                             |                                               |
| bufferClear     | in        | sl                             |                                               |
| axilClk         | in        | sl                             | AXI-Lite interface (axilClk domain)           |
| axilRst         | in        | sl                             |                                               |
| axilReadMaster  | in        | AxiLiteReadMasterType          |                                               |
| axilReadSlave   | out       | AxiLiteReadSlaveType           |                                               |
| axilWriteMaster | in        | AxiLiteWriteMasterType         |                                               |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType          |                                               |
| axisClk         | in        | sl                             | AXI-Stream Interface (axisClk domain)         |
| axisRst         | in        | sl                             |                                               |
| axisMaster      | out       | AxiStreamMasterType            |                                               |
| axisSlave       | in        | AxiStreamSlaveType             |                                               |
## Signals

| Name             | Type                             | Description |
| ---------------- | -------------------------------- | ----------- |
| dataR            | DataRegType                      |             |
| dataRin          | DataRegType                      |             |
| bufferEnableSync | sl                               |             |
| bufferClearSync  | sl                               |             |
| axilR            | AxilRegType                      |             |
| axilRin          | AxilRegType                      |             |
| ramRdData        | slv(8*DATA_BYTES_G-1 downto 0)   |             |
| firstAddr        | slv(RAM_ADDR_WIDTH_G-1 downto 0) |             |
| bufferLength     | slv(RAM_ADDR_WIDTH_G-1 downto 0) |             |
| extBufferEnable  | sl                               |             |
| extBufferClear   | sl                               |             |
| readReq          | sl                               |             |
| cleared          | sl                               |             |
| armed            | sl                               |             |
| txSlave          | AxiStreamSlaveType               |             |
## Constants

| Name            | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| --------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXIS_CONFIG_C   | AxiStreamConfigType |  ssiAxiStreamConfig(       dataBytes => DATA_BYTES_G,<br><span style="padding-left:20px">       tKeepMode => TKEEP_FIXED_C,<br><span style="padding-left:20px">       tUserMode => TUSER_FIRST_LAST_C,<br><span style="padding-left:20px">       tDestBits => 0,<br><span style="padding-left:20px">       tUserBits => 2,<br><span style="padding-left:20px">       tIdBits   => 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
| DATA_REG_INIT_C | DataRegType         |  (       enable       => '0',<br><span style="padding-left:20px">       cleared      => '1',<br><span style="padding-left:20px">              -- Only set HIGH after reset       armed        => '0',<br><span style="padding-left:20px">       ramWrEn      => '0',<br><span style="padding-left:20px">       readReq      => '0',<br><span style="padding-left:20px">       ramWrData    => (others => '0'),<br><span style="padding-left:20px">       bufferLength => (others => '0'),<br><span style="padding-left:20px">       firstAddr    => (others => '0'),<br><span style="padding-left:20px">       nextAddr     => (others => '0'))                                                                                                                                                                                                                                                      |             |
| AXIL_REG_INIT_C | AxilRegType         |  (       trigCnt        => (others => '0'),<br><span style="padding-left:20px">       continuous     => '0',<br><span style="padding-left:20px">       bufferEnable   => '0',<br><span style="padding-left:20px">       bufferClear    => '0',<br><span style="padding-left:20px">       wordCnt        => (others => '0'),<br><span style="padding-left:20px">       ramRdAddr      => (others => '0'),<br><span style="padding-left:20px">       rdEn           => "000",<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       txMaster       => axiStreamMasterInit(AXIS_CONFIG_C),<br><span style="padding-left:20px">       dataState      => IDLE_S,<br><span style="padding-left:20px">       trigState      => IDLE_S) |             |
## Types

| Name          | Type                                                                                                                                             | Description                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| DataRegType   |                                                                                                                                                  | ----------------------------  Stream clock domain signals ----------------------------        |
| DataStateType | ( IDLE_S,<br><span style="padding-left:20px"> MOVE_S)                                                                                            | ------------------------------  AXI-Lite clock domain signals ------------------------------  |
| TrigStateType | ( IDLE_S,<br><span style="padding-left:20px"> CLEAR_S,<br><span style="padding-left:20px"> ARMED_S,<br><span style="padding-left:20px"> WAIT_S)  |                                                                                               |
| AxilRegType   |                                                                                                                                                  |                                                                                               |
## Processes
- dataComb: ( bufferClear, bufferClearSync, bufferEnable,
                       bufferEnableSync, dataR, dataRst, dataValid, dataValue )
**Description**
------------------------  Main AXI-Stream process ------------------------ 
- dataSeq: ( dataClk )
- axiComb: ( armed, axilR, axilReadMaster, axilRst, axilWriteMaster,
                      bufferLength, cleared, extBufferClear, extBufferEnable,
                      firstAddr, ramRdData, readReq, txSlave )
**Description**
----------------------  Main AXI-Lite process ---------------------- 
- axiSeq: ( axilClk )
## Instantiations

- U_SyncVec_dataClk: surf.SynchronizerVector
**Description**
------------------------------------------------
 Synchronize AXI registers to data clock dataClk
------------------------------------------------

- U_Sync_ReadReq: surf.SynchronizerFifo
**Description**
---------------------------------------------------
 Synchronize write address across to AXI-Lite clock
---------------------------------------------------

- U_SyncVec_axilClk: surf.SynchronizerVector
- TX_FIFO: surf.AxiStreamFifoV2
