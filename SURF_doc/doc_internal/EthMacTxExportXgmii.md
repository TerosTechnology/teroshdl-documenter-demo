# Entity: EthMacTxExportXgmii

- **File**: EthMacTxExportXgmii.vhd
## Diagram

![Diagram](EthMacTxExportXgmii.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: 10GbE Export MAC core with GMII interface
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

| Generic name | Type   | Value      | Description |
| ------------ | ------ | ---------- | ----------- |
| TPD_G        | time   | 1 ns       |             |
| SYNTH_MODE_G | string | "inferred" |             |
## Ports

| Port name      | Direction | Type                | Description     |
| -------------- | --------- | ------------------- | --------------- |
| ethClk         | in        | sl                  | Clock and Reset |
| ethRst         | in        | sl                  |                 |
| macObMaster    | in        | AxiStreamMasterType | AXIS Interface  |
| macObSlave     | out       | AxiStreamSlaveType  |                 |
| phyTxd         | out       | slv(63 downto 0)    | XAUI Interface  |
| phyTxc         | out       | slv(7 downto 0)     |                 |
| phyReady       | in        | sl                  |                 |
| txCountEn      | out       | sl                  | Errors          |
| txUnderRun     | out       | sl                  |                 |
| txLinkNotReady | out       | sl                  |                 |
## Signals

| Name             | Type                | Description     |
| ---------------- | ------------------- | --------------- |
| macMaster        | AxiStreamMasterType |  Local Signals  |
| macSlave         | AxiStreamSlaveType  |                 |
| intAdvance       | sl                  |                 |
| intDump          | sl                  |                 |
| intPad           | sl                  |                 |
| intLastLine      | sl                  |                 |
| intLastValidByte | slv(2 downto 0)     |                 |
| frameShift0      | sl                  |                 |
| frameShift1      | sl                  |                 |
| txEnable0        | sl                  |                 |
| txEnable1        | sl                  |                 |
| txEnable2        | sl                  |                 |
| txEnable3        | sl                  |                 |
| nxtMaskIn        | slv(7 downto 0)     |                 |
| nxtEOF           | sl                  |                 |
| intData          | slv(63 downto 0)    |                 |
| stateCount       | slv(3 downto 0)     |                 |
| stateCountRst    | sl                  |                 |
| wordCountRst     | sl                  |                 |
| exportWordCnt    | slv(3 downto 0)     |                 |
| crcFifoIn        | slv(71 downto 0)    |                 |
| crcFifoOut       | slv(71 downto 0)    |                 |
| crcTx            | slv(31 downto 0)    |                 |
| crcIn            | slv(63 downto 0)    |                 |
| crcInit          | sl                  |                 |
| crcMaskIn        | slv(7 downto 0)     |                 |
| crcInAdj         | slv(63 downto 0)    |                 |
| crcDataWidth     | slv(2 downto 0)     |                 |
| crcDataValid     | sl                  |                 |
| crcReset         | sl                  |                 |
| crcOut           | slv(31 downto 0)    |                 |
| intError         | sl                  |                 |
| nxtError         | sl                  |                 |
| curState         | slv(2 downto 0)     |  MAC States     |
| nxtState         | slv(2 downto 0)     |                 |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| INTERGAP_C   | slv(3 downto 0)     |  x"3"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
| AXI_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => INT_EMAC_AXIS_CONFIG_C.TSTRB_EN_C,<br><span style="padding-left:20px">       TDATA_BYTES_C => 8,<br><span style="padding-left:20px">               -- 64-bit AXI stream interface       TDEST_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TDEST_BITS_C,<br><span style="padding-left:20px">       TID_BITS_C    => INT_EMAC_AXIS_CONFIG_C.TID_BITS_C,<br><span style="padding-left:20px">       TKEEP_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TKEEP_MODE_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_BITS_C,<br><span style="padding-left:20px">       TUSER_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_MODE_C) |             |
| ST_IDLE_C    | slv(2 downto 0)     |  "000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| ST_DUMP_C    | slv(2 downto 0)     |  "001"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| ST_READ_C    | slv(2 downto 0)     |  "010"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| ST_WAIT_C    | slv(2 downto 0)     |  "011"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| ST_PAD_C     | slv(2 downto 0)     |  "100"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
## Processes
- unnamed: ( intPad, macMaster )
**Description**
 Data processing 
- unnamed: ( ethClk )
**Description**
 State machine logic 
- unnamed: ( curState, exportWordCnt, intLastLine, macMaster )
**Description**
 Pad runt frames 
- unnamed: ( curState, ethRst, exportWordCnt, intError, macMaster, phyReady, stateCount )
**Description**
 State machine 
- unnamed: ( ethClk )
**Description**
 Format data for input into CRC delay FIFO. 
- unnamed: ( ethClk )
**Description**
 Output Stage to PHY 
## Instantiations

- DATA_MUX: surf.AxiStreamFifoV2
- U_CrcFifo: surf.Fifo
**Description**
 CRC Delay FIFO

- U_Crc32: surf.Crc32Parallel
**Description**
 CRC

