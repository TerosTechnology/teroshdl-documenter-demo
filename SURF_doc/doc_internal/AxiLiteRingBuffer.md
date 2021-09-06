# Entity: AxiLiteRingBuffer

- **File**: AxiLiteRingBuffer.vhd
## Diagram

![Diagram](AxiLiteRingBuffer.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for simple BRAM based ring buffer with AXI-Lite interface
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

| Generic name     | Type                   | Value   | Description             |
| ---------------- | ---------------------- | ------- | ----------------------- |
| TPD_G            | time                   | 1 ns    | General Configurations  |
| EXT_CTRL_ONLY_G  | boolean                | false   |                         |
| MEMORY_TYPE_G    | string                 | "block" |                         |
| REG_EN_G         | boolean                | true    |                         |
| DATA_WIDTH_G     | positive range 1 to 32 | 32      |                         |
| RAM_ADDR_WIDTH_G | positive range 1 to 19 | 10      |                         |
## Ports

| Port name       | Direction | Type                         | Description                    |
| --------------- | --------- | ---------------------------- | ------------------------------ |
| dataClk         | in        | sl                           | Data to store in ring buffer   |
| dataRst         | in        | sl                           |                                |
| dataValid       | in        | sl                           |                                |
| dataValue       | in        | slv(DATA_WIDTH_G-1 downto 0) |                                |
| bufferEnable    | in        | sl                           |                                |
| bufferClear     | in        | sl                           |                                |
| axilClk         | in        | sl                           | AXI-Lite interface for readout |
| axilRst         | in        | sl                           |                                |
| axilReadMaster  | in        | AxiLiteReadMasterType        |                                |
| axilReadSlave   | out       | AxiLiteReadSlaveType         |                                |
| axilWriteMaster | in        | AxiLiteWriteMasterType       |                                |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType        |                                |
## Signals

| Name             | Type                             | Description                |
| ---------------- | -------------------------------- | -------------------------- |
| dataR            | DataRegType                      |                            |
| dataRin          | DataRegType                      |                            |
| axilBufferEnable | sl                               |  Synchronized AXI register |
| axilBufferClear  | sl                               |  Synchronized AXI register |
| axilR            | AxilRegType                      |                            |
| axilRin          | AxilRegType                      |                            |
| axilRamRdData    | slv(DATA_WIDTH_G-1 downto 0)     |                            |
| axilFirstAddr    | slv(RAM_ADDR_WIDTH_G-1 downto 0) |                            |
| axilLength       | slv(RAM_ADDR_WIDTH_G-1 downto 0) |                            |
| extBufferEnable  | sl                               |                            |
| extBufferClear   | sl                               |                            |
## Constants

| Name              | Type        | Value                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                   |
| ----------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| DATA_REG_INIT_C   | DataRegType |  (       ramWrEn      => '0',<br><span style="padding-left:20px">       ramWrData    => (others => '0'),<br><span style="padding-left:20px">       bufferLength => (others => '0'),<br><span style="padding-left:20px">       firstAddr    => (others => '0'),<br><span style="padding-left:20px">       nextAddr     => (others => '0'))                                                                                         |                                                                                               |
| AXIL_ADDR_WIDTH_C | integer     |  RAM_ADDR_WIDTH_G+3                                                                                                                                                                                                                                                                                                                                                                                                               | ------------------------------  AXI-Lite clock domain signals ------------------------------  |
| AXIL_REG_INIT_C   | AxilRegType |  (       bufferEnable   => '0',<br><span style="padding-left:20px">       bufferClear    => '0',<br><span style="padding-left:20px">       ramRdAddr      => (others => '0'),<br><span style="padding-left:20px">       axilRdEn       => "000",<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |                                                                                               |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| DataRegType |      |             |
| AxilRegType |      |             |
## Processes
- dataComb: ( axilBufferClear, axilBufferEnable, bufferClear, bufferEnable, dataR, dataRst,
                       dataValid, dataValue )
</br>**Description**
------------------------  Main AXI-Stream process ------------------------ 
- dataSeq: ( dataClk )
- axiComb: ( axilFirstAddr, axilLength, axilR, axilRamRdData, axilReadMaster, axilRst,
                      axilWriteMaster, extBufferClear, extBufferEnable )
</br>**Description**
----------------------  Main AXI-Lite process ---------------------- 
- axiSeq: ( axilClk )
## Instantiations

- DualPortRam_1: surf.DualPortRam
- Synchronizer_bufferEn: surf.Synchronizer
</br>**Description**
-----------------------------
 Synchronize AXI registers to data clock dataClk
-----------------------------

- Synchronizer_bufferClear: surf.SynchronizerOneShot
- SynchronizerFifo_1: surf.SynchronizerFifo
</br>**Description**
---------------------------------------------------
 Synchronize write address across to AXI-Lite clock
---------------------------------------------------

- SynchronizerFifo_2: surf.SynchronizerFifo
- Synchronizer_dataBufferEn: surf.Synchronizer
- Synchronizer_dataBufferClr: surf.Synchronizer
