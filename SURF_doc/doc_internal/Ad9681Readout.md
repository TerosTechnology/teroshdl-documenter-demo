# Entity: Ad9681Readout

- **File**: Ad9681Readout.vhd
## Diagram

![Diagram](Ad9681Readout.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 ADC Readout Controller
 Receives ADC Data from an AD9592 chip.
 Designed specifically for Xilinx 7 series FPGAs
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

| Generic name      | Type            | Value           | Description |
| ----------------- | --------------- | --------------- | ----------- |
| TPD_G             | time            | 1 ns            |             |
| SIMULATION_G      | boolean         | false           |             |
| IODELAY_GROUP_G   | string          | "DEFAULT_GROUP" |             |
| IDELAYCTRL_FREQ_G | real            | 200.0           |             |
| DEFAULT_DELAY_G   | slv(4 downto 0) | (others => '0') |             |
## Ports

| Port name       | Direction | Type                             | Description                 |
| --------------- | --------- | -------------------------------- | --------------------------- |
| axilClk         | in        | sl                               | Master system clock, 125Mhz |
| axilRst         | in        | sl                               |                             |
| axilWriteMaster | in        | AxiLiteWriteMasterType           | Axi Interface               |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType            |                             |
| axilReadMaster  | in        | AxiLiteReadMasterType            |                             |
| axilReadSlave   | out       | AxiLiteReadSlaveType             |                             |
| adcClkRst       | in        | sl                               | Reset for adc deserializer  |
| adcSerial       | in        | Ad9681SerialType                 | Serial Data from ADC        |
| adcStreamClk    | in        | sl                               | Deserialized ADC Data       |
| adcStreams      | out       | AxiStreamMasterArray(7 downto 0) |                             |
## Signals

| Name            | Type                                  | Description     |
| --------------- | ------------------------------------- | --------------- |
| lockedSync      | slv(1 downto 0)                       |                 |
| lockedFallCount | slv16Array(1 downto 0)                |                 |
| axilR           | AxilRegType                           |                 |
| axilRin         | AxilRegType                           |                 |
| adcR            | AdcRegArray(1 downto 0)               |                 |
| adcRin          | AdcRegArray(1 downto 0)               |                 |
| tmpAdcClk       | slv(1 downto 0)                       |  Local Signals  |
| adcBitClkIo     | slv(1 downto 0)                       |                 |
| adcBitClkIoInv  | slv(1 downto 0)                       |                 |
| adcBitClkR      | slv(1 downto 0)                       |                 |
| adcBitRst       | slv(1 downto 0)                       |                 |
| adcFramePad     | slv(1 downto 0)                       |                 |
| adcFrame        | slv8Array(1 downto 0)                 |                 |
| adcFrameSync    | slv8Array(1 downto 0)                 |                 |
| adcDataPad      | slv8Array(1 downto 0)                 |                 |
| adcData         | AdcDataArray(1 downto 0)              |                 |
| fifoWrData      | slv16Array(NUM_CHANNELS_C-1 downto 0) |                 |
| fifoDataValid   | sl                                    |                 |
| fifoDataOut     | slv(NUM_CHANNELS_C*16-1 downto 0)     |                 |
| fifoDataIn      | slv(NUM_CHANNELS_C*16-1 downto 0)     |                 |
| fifoDataTmp     | slv16Array(NUM_CHANNELS_C-1 downto 0) |                 |
| debugDataValid  | sl                                    |                 |
| debugDataOut    | slv(NUM_CHANNELS_C*16-1 downto 0)     |                 |
| debugDataTmp    | slv16Array(NUM_CHANNELS_C-1 downto 0) |                 |
| invertSync      | slv(1 downto 0)                       |                 |
| bitSlip         | slv(1 downto 0)                       |                 |
| dlyLoad         | slv(1 downto 0)                       |                 |
| dlyCfg          | Slv9Array(1 downto 0)                 |                 |
| enUsrDlyCfg     | slv(1 downto 0)                       |                 |
| usrDlyCfg       | slv9Array(1 downto 0)                 |                 |
| minEyeWidthSync | slv8Array(1 downto 0)                 |                 |
| lockingCntCfg   | slv(23 downto 0)                      |                 |
| locked          | slv(1 downto 0)                       |                 |
| realignSync     | slv(1 downto 0)                       |                 |
| curDelay        | slv5Array(1 downto 0)                 |                 |
| errorDetCount   | slv16Array(1 downto 0)                |                 |
| errorDet        | slv(1 downto 0)                       |                 |
## Constants

| Name            | Type        | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| --------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| NUM_CHANNELS_C  | natural     |  8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| AXIL_REG_INIT_C | AxilRegType |  (       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       delay          => DEFAULT_DELAY_G,<br><span style="padding-left:20px">       delaySet       => "00",<br><span style="padding-left:20px">       freezeDebug    => '0',<br><span style="padding-left:20px">       readoutDebug0  => (others => (others => '0')),<br><span style="padding-left:20px">       readoutDebug1  => (others => (others => '0')),<br><span style="padding-left:20px">       lockedCountRst => '0',<br><span style="padding-left:20px">       invert         => '0',<br><span style="padding-left:20px">       realign        => '0',<br><span style="padding-left:20px">       minEyeWidth    => X"50") |             |
| ADC_REG_INIT_C  | AdcRegType  |  (       errorDet => '0')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
## Types

| Name           | Type                                               | Description                                                                                                                                                                                                                     |
| -------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AdcDataArray   | array (natural range <>) of slv8Array(7 downto 0)  |                                                                                                                                                                                                                                 |
| DelayDataArray | array (natural range <>) of slv5Array(7 downto 0)  |                                                                                                                                                                                                                                 |
| AxilRegType    |                                                    | -----------------------------------------------------------------------------------------------  AXIL Registers -----------------------------------------------------------------------------------------------                 |
| AdcRegType     |                                                    | -----------------------------------------------------------------------------------------------  ADC Readout Clocked Registers -----------------------------------------------------------------------------------------------  |
| AdcRegArray    | array (natural range <>) of AdcRegType             |                                                                                                                                                                                                                                 |
## Processes
- axilComb: ( adcFrameSync, axilR, axilReadMaster, axilRst, axilWriteMaster, curDelay,
                       debugDataTmp, debugDataValid, errorDetCount, lockedFallCount, lockedSync )
**Description**
-----------------------------------------------------------------------------------------------  AXIL Interface ----------------------------------------------------------------------------------------------- 
- axilSeq: ( axilClk )
- GLUE_COMB: ( adcData, invertSync, locked )
## Instantiations

- U_DataFifo: surf.SynchronizerFifo
**Description**
 Single fifo to synchronize adc data to the Stream clock

- U_DataFifoDebug: surf.SynchronizerFifo
