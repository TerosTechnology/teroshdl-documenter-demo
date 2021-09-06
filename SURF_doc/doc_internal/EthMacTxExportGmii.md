# Entity: EthMacTxExportGmii

- **File**: EthMacTxExportGmii.vhd
## Diagram

![Diagram](EthMacTxExportGmii.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: 1GbE Export MAC core with GMII interface
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

| Port name      | Direction | Type                | Description        |
| -------------- | --------- | ------------------- | ------------------ |
| ethClkEn       | in        | sl                  | Clock and Reset    |
| ethClk         | in        | sl                  |                    |
| ethRst         | in        | sl                  |                    |
| macObMaster    | in        | AxiStreamMasterType | AXIS Interface     |
| macObSlave     | out       | AxiStreamSlaveType  |                    |
| gmiiTxEn       | out       | sl                  | GMII PHY Interface |
| gmiiTxEr       | out       | sl                  |                    |
| gmiiTxd        | out       | slv(7 downto 0)     |                    |
| phyReady       | in        | sl                  |                    |
| txCountEn      | out       | sl                  | Status             |
| txUnderRun     | out       | sl                  |                    |
| txLinkNotReady | out       | sl                  |                    |
## Signals

| Name         | Type                | Description |
| ------------ | ------------------- | ----------- |
| r            | RegType             |             |
| rin          | RegType             |             |
| macMaster    | AxiStreamMasterType |             |
| macSlave     | AxiStreamSlaveType  |             |
| crcOut       | slv(31 downto 0)    |             |
| crcDataValid | sl                  |             |
| crcIn        | slv(7 downto 0)     |             |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AXI_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => INT_EMAC_AXIS_CONFIG_C.TSTRB_EN_C,<br><span style="padding-left:20px">       TDATA_BYTES_C => 1,<br><span style="padding-left:20px">               -- 8-bit AXI stream interface       TDEST_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TDEST_BITS_C,<br><span style="padding-left:20px">       TID_BITS_C    => INT_EMAC_AXIS_CONFIG_C.TID_BITS_C,<br><span style="padding-left:20px">       TKEEP_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TKEEP_MODE_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_BITS_C,<br><span style="padding-left:20px">       TUSER_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_MODE_C)                                                                                                                                                                                                                                               |             |
| REG_INIT_C   | RegType             |  (       gmiiTxEn       => '0',<br><span style="padding-left:20px">       gmiiTxEr       => '0',<br><span style="padding-left:20px">       gmiiTxd        => (others => '0'),<br><span style="padding-left:20px">       txCount        => (others => '0'),<br><span style="padding-left:20px">       txData         => (others => '0'),<br><span style="padding-left:20px">       txCountEn      => '0',<br><span style="padding-left:20px">       txUnderRun     => '0',<br><span style="padding-left:20px">       txLinkNotReady => '0',<br><span style="padding-left:20px">       crcReset       => '0',<br><span style="padding-left:20px">       crcDataValid   => '0',<br><span style="padding-left:20px">       crcIn          => (others => '0'),<br><span style="padding-left:20px">       state          => IDLE_S,<br><span style="padding-left:20px">       macSlave       => AXI_STREAM_SLAVE_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> TX_PREAMBLE_S,<br><span style="padding-left:20px"> TX_DATA_S,<br><span style="padding-left:20px"> PAD_S,<br><span style="padding-left:20px"> TX_CRC_S,<br><span style="padding-left:20px"> TX_CRC0_S,<br><span style="padding-left:20px"> TX_CRC1_S,<br><span style="padding-left:20px"> TX_CRC2_S,<br><span style="padding-left:20px"> TX_CRC3_S,<br><span style="padding-left:20px"> DUMP_S,<br><span style="padding-left:20px"> INTERGAP_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
## Processes
- comb: ( crcOut, ethClkEn, ethRst, macMaster, phyReady, r )
- seq: ( ethClk )
## Instantiations

- U_Resize: surf.AxiStreamResize
- U_Crc32: surf.Crc32Parallel
</br>**Description**
 CRC

