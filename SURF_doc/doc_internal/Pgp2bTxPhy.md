# Entity: Pgp2bTxPhy

- **File**: Pgp2bTxPhy.vhd
## Diagram

![Diagram](Pgp2bTxPhy.svg "Diagram")
## Description

Title      : PGPv2b: https://confluence.slac.stanford.edu/x/q86fD
Company    : SLAC National Accelerator Laboratory
Description:
Physical interface receive module for the Pretty Good Protocol version 2 core.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                 | Value | Description                  |
| ------------- | -------------------- | ----- | ---------------------------- |
| TPD_G         | time                 | 1 ns  |                              |
| TX_LANE_CNT_G | integer range 1 to 2 | 1     | Number of receive lanes, 1-2 |
## Ports

| Port name       | Direction | Type                             | Description                     |
| --------------- | --------- | -------------------------------- | ------------------------------- |
| pgpTxClkEn      | in        | sl                               | Master clock Enable             |
| pgpTxClk        | in        | sl                               | Master clock                    |
| pgpTxClkRst     | in        | sl                               | Synchronous reset input         |
| pgpTxLinkReady  | out       | sl                               | Local side has link             |
| pgpTxOpCodeEn   | in        | sl                               | Opcode receive enable           |
| pgpTxOpCode     | in        | slv(7 downto 0)                  | Opcode receive value            |
| pgpLocLinkReady | in        | sl                               | Far end side has link           |
| pgpLocData      | in        | slv(7 downto 0)                  | Far end side User Data          |
| cellTxSOC       | in        | sl                               | Cell data start of cell         |
| cellTxSOF       | in        | sl                               | Cell data start of frame        |
| cellTxEOC       | in        | sl                               | Cell data end of cell           |
| cellTxEOF       | in        | sl                               | Cell data end of frame          |
| cellTxEOFE      | in        | sl                               | Cell data end of frame error    |
| cellTxData      | in        | slv(TX_LANE_CNT_G*16-1 downto 0) | Cell data data                  |
| phyTxData       | out       | slv(TX_LANE_CNT_G*16-1 downto 0) | PHY receive data                |
| phyTxDataK      | out       | slv(TX_LANE_CNT_G*2-1  downto 0) | PHY receive data is K character |
| phyTxReady      | in        | sl                               | PHY receive interface is ready  |
## Signals

| Name           | Type                             | Description |
| -------------- | -------------------------------- | ----------- |
| algnCnt        | slv(6 downto 0)                  |             |
| algnCntRst     | sl                               |             |
| intTxLinkReady | sl                               |             |
| nxtTxLinkReady | sl                               |             |
| nxtTxData      | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| nxtTxDataK     | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| dlyTxData      | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| dlyTxDataK     | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| dlySelect      | sl                               |             |
| intTxData      | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| intTxDataK     | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| intTxOpCode    | slv(7 downto 0)                  |             |
| intTxOpCodeEn  | sl                               |             |
| skpAData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| skpADataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| skpBData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| skpBDataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| alnAData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| alnADataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| alnBData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| alnBDataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| ltsAData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| ltsADataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| ltsBData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| ltsBDataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| cellData       | slv(TX_LANE_CNT_G*16-1 downto 0) |             |
| cellDataK      | slv(TX_LANE_CNT_G*2-1  downto 0) |             |
| dlyTxEOC       | sl                               |             |
| curState       | slv(3 downto 0)                  |             |
| nxtState       | slv(3 downto 0)                  |             |
## Constants

| Name       | Type            | Value   | Description         |
| ---------- | --------------- | ------- | ------------------- |
| ST_LOCK_C  | slv(3 downto 0) |  "0000" | Physical Link State |
| ST_SKP_A_C | slv(3 downto 0) |  "0001" |                     |
| ST_SKP_B_C | slv(3 downto 0) |  "0010" |                     |
| ST_LTS_A_C | slv(3 downto 0) |  "0011" |                     |
| ST_LTS_B_C | slv(3 downto 0) |  "0100" |                     |
| ST_ALN_A_C | slv(3 downto 0) |  "0101" |                     |
| ST_ALN_B_C | slv(3 downto 0) |  "0110" |                     |
| ST_CELL_C  | slv(3 downto 0) |  "0111" |                     |
| ST_EMPTY_C | slv(3 downto 0) |  "1000" |                     |
## Processes
- unnamed: ( pgpTxClk )
**Description**
State transition sync logic.

- unnamed: ( curState, intTxLinkReady, cellTxEOC, algnCnt,
             skpAData, skpADataK, skpBData, skpBDataK, alnAData, alnADataK, alnBData,
             alnBDataK, ltsAData, ltsADataK, ltsBData, ltsBDataK, cellData, cellDataK )
**Description**
Link control state machine

- unnamed: ( pgpTxClk )
**Description**
Delay chain select, used when an opcode is transmitted.
opcode will overwrite current position and delay chain will
be selected until an EOC is transmitted. At that time the
non-delayed chain will be select. An empty position is inserted
after EOC so that valid opcodes are not lost.

