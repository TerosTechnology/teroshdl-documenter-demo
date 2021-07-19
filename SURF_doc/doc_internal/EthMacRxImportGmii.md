# Entity: EthMacRxImportGmii

- **File**: EthMacRxImportGmii.vhd
## Diagram

![Diagram](EthMacRxImportGmii.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: 1GbE Import MAC core with GMII interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type   | Value      | Description |
| ------------ | ------ | ---------- | ----------- |
| TPD_G        | time   | 1 ns       |             |
| SYNTH_MODE_G | string | "inferred" |             |
## Ports

| Port name   | Direction | Type                | Description              |
| ----------- | --------- | ------------------- | ------------------------ |
| ethClkEn    | in        | sl                  | Clock and Reset          |
| ethClk      | in        | sl                  |                          |
| ethRst      | in        | sl                  |                          |
| macIbMaster | out       | AxiStreamMasterType | AXIS Interface           |
| gmiiRxDv    | in        | sl                  | GMII PHY Interface       |
| gmiiRxEr    | in        | sl                  |                          |
| gmiiRxd     | in        | slv(7 downto 0)     |                          |
| phyReady    | in        | sl                  | Configuration and status |
| rxCountEn   | out       | sl                  |                          |
| rxCrcError  | out       | sl                  |                          |
## Signals

| Name      | Type                | Description |
| --------- | ------------------- | ----------- |
| r         | RegType             |             |
| rin       | RegType             |             |
| crcOut    | slv(31 downto 0)    |             |
| crcIn     | slv(31 downto 0)    |             |
| macMaster | AxiStreamMasterType |             |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| SFD_C        | slv(7 downto 0)     |  x"D5"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| AXI_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => INT_EMAC_AXIS_CONFIG_C.TSTRB_EN_C,<br><span style="padding-left:20px">       TDATA_BYTES_C => 1,<br><span style="padding-left:20px">               -- 8-bit AXI stream interface       TDEST_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TDEST_BITS_C,<br><span style="padding-left:20px">       TID_BITS_C    => INT_EMAC_AXIS_CONFIG_C.TID_BITS_C,<br><span style="padding-left:20px">       TKEEP_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TKEEP_MODE_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_BITS_C,<br><span style="padding-left:20px">       TUSER_MODE_C  => INT_EMAC_AXIS_CONFIG_C.TUSER_MODE_C)     |             |
| REG_INIT_C   | RegType             |  (       rxCountEn    => '0',<br><span style="padding-left:20px">       rxCrcError   => '0',<br><span style="padding-left:20px">       crcReset     => '0',<br><span style="padding-left:20px">       delRxDv      => '0',<br><span style="padding-left:20px">       delRxDvSr    => (others => '0'),<br><span style="padding-left:20px">       crcDataValid => '0',<br><span style="padding-left:20px">       sof          => '0',<br><span style="padding-left:20px">       state        => WAIT_SFD_S,<br><span style="padding-left:20px">       macData      => (others => '0'),<br><span style="padding-left:20px">       macMaster    => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                   | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( WAIT_SFD_S,<br><span style="padding-left:20px"> WAIT_DATA_S,<br><span style="padding-left:20px"> GET_DATA_S,<br><span style="padding-left:20px"> DELAY0_S,<br><span style="padding-left:20px"> DELAY1_S,<br><span style="padding-left:20px"> CRC_S)  |             |
| RegType   |                                                                                                                                                                                                                                                        |             |
## Processes
- comb: ( crcIn, crcOut, ethClkEn, ethRst, gmiiRxDv, gmiiRxEr,
                   gmiiRxd, phyReady, r )
- seq: ( ethClk )
## Instantiations

- DATA_MUX: surf.AxiStreamFifoV2
- U_Crc32: surf.Crc32Parallel
**Description**
CRC

