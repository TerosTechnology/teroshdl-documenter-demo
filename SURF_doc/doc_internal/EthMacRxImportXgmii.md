# Entity: EthMacRxImportXgmii

- **File**: EthMacRxImportXgmii.vhd
## Diagram

![Diagram](EthMacRxImportXgmii.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: 10GbE Import MAC core with GMII interface
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name   | Direction | Type                | Description              |
| ----------- | --------- | ------------------- | ------------------------ |
| ethClk      | in        | sl                  | Clock and Reset          |
| ethRst      | in        | sl                  |                          |
| macIbMaster | out       | AxiStreamMasterType | AXIS Interface           |
| phyRxdata   | in        | slv(63 downto 0)    | PHY Interface            |
| phyRxChar   | in        | slv(7 downto 0)     |                          |
| phyReady    | in        | sl                  | Configuration and status |
| rxCountEn   | out       | sl                  |                          |
| rxCrcError  | out       | sl                  |                          |
## Signals

| Name         | Type                | Description     |
| ------------ | ------------------- | --------------- |
| r            | RegType             |                 |
| rin          | RegType             |                 |
| macMaster    | AxiStreamMasterType |  Local Signals  |
| frameShift0  | sl                  |                 |
| frameShift1  | sl                  |                 |
| frameShift2  | sl                  |                 |
| frameShift3  | sl                  |                 |
| frameShift4  | sl                  |                 |
| frameShift5  | sl                  |                 |
| rxdAlign     | sl                  |                 |
| dlyRxd       | slv(31 downto 0)    |                 |
| crcDataWidth | slv(2 downto 0)     |                 |
| nxtCrcWidth  | slv(2 downto 0)     |                 |
| nxtCrcValid  | sl                  |                 |
| crcDataValid | sl                  |                 |
| crcFifoIn    | slv(63 downto 0)    |                 |
| crcFifoOut   | slv(63 downto 0)    |                 |
| phyRxcDly    | slv(7 downto 0)     |                 |
| crcWidthDly0 | slv(2 downto 0)     |                 |
| crcWidthDly1 | slv(2 downto 0)     |                 |
| crcWidthDly2 | slv(2 downto 0)     |                 |
| crcWidthDly3 | slv(2 downto 0)     |                 |
| crcShift0    | sl                  |                 |
| crcShift1    | sl                  |                 |
| endDetect    | sl                  |                 |
| endShift0    | sl                  |                 |
| endShift1    | sl                  |                 |
| crcGood      | sl                  |                 |
| intLastLine  | sl                  |                 |
| intFirstLine | sl                  |                 |
| intAdvance   | sl                  |                 |
| lastSOF      | sl                  |                 |
| crcIn        | slv(63 downto 0)    |                 |
| crcInit      | sl                  |                 |
| crcReset     | sl                  |                 |
| crcOut       | slv(31 downto 0)    |                 |
| macData      | slv(63 downto 0)    |                 |
| macSize      | slv(2 downto 0)     |                 |
| phyRxd       | slv(63 downto 0)    |                 |
| phyRxc       | slv(7 downto 0)     |                 |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ------------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXI_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => INT_EMAC_AXIS_CONFIG_C.TSTRB_EN_C,<br><span style="padding-left:20px">       TDATA_BYTES_C => 8,<br><span style="padding-left:20px">               -- 64-bit AXI stream interface       TDEST_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TDEST_BITS_C,<br><span style="padding-left:20px">       TID_BITS_C    => INT_EMAC_AXIS_CONFIG_C.TID_BITS_C,<br><span style="padding-left:20px">       TKEEP_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TKEEP_MODE_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_BITS_C,<br><span style="padding-left:20px">       TUSER_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_MODE_C) |             |
| REG_INIT_C   | RegType             |  (       phyRxd      => x"0707070707070707",<br><span style="padding-left:20px">       phyRxc      => x"FF",<br><span style="padding-left:20px">       phyRxdDly   => x"0707070707070707",<br><span style="padding-left:20px">       phyRxcDly   => x"FF",<br><span style="padding-left:20px">       gapInserted => '0')                                                                                                                                                                                                                                                                                                                                              |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( phyRxChar, phyRxdata, r )
- seq: ( ethClk )
- unnamed: ( ethClk )
**Description**
 Convert to AXI stream 
- unnamed: ( crcDataValid, crcDataWidth, phyRxc, phyRxcDly, rxdAlign )
**Description**
 Logic to dermine CRC width and valid clear timing. 
- unnamed: ( ethClk )
**Description**
 Delay stages and input to CRC block 
- unnamed: ( ethClk )
**Description**
 Delay stages for output of CRC delay chain 
## Instantiations

- U_Resize: surf.AxiStreamResize
- U_CrcFifo: surf.Fifo
**Description**
 CRC Delay FIFO

- U_Crc32: surf.Crc32Parallel
**Description**
 CRC

