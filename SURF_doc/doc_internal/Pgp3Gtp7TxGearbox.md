# Entity: Pgp3Gtp7TxGearbox

## Diagram

![Diagram](Pgp3Gtp7TxGearbox.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv3 GTP7 64B66B to 32B33B TX Gearbox
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name    | Direction | Type             | Description      |
| ------------ | --------- | ---------------- | ---------------- |
| phyTxClkSlow | in        | sl               | Slave Interface  |
| phyTxRstSlow | in        | sl               |                  |
| phyTxHeader  | in        | slv(1 downto 0)  |                  |
| phyTxData    | in        | slv(63 downto 0) |                  |
| phyTxValid   | in        | sl               |                  |
| phyTxDataRdy | out       | sl               |                  |
| phyTxClkFast | in        | sl               | Master Interface |
| phyTxRstFast | in        | sl               |                  |
| txHeader     | out       | slv(1 downto 0)  |                  |
| txData       | out       | slv(31 downto 0) |                  |
| txSequence   | out       | slv(6 downto 0)  |                  |
## Signals

| Name        | Type             | Description |
| ----------- | ---------------- | ----------- |
| r           | RegType          |             |
| rin         | RegType          |             |
| writeEnable | sl               |             |
| almostFull  | sl               |             |
| slaveReady  | sl               |             |
| fifoRead    | sl               |             |
| fifoValid   | sl               |             |
| fifoData    | slv(65 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                  | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       fifoRead   => '0',<br><span style="padding-left:20px">       txHeader   => (others => '0'),<br><span style="padding-left:20px">       txSequence => (others => '0'),<br><span style="padding-left:20px">       txData     => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( fifoData, fifoValid, phyTxRstFast, r )
- seq: ( phyTxClkFast )
## Instantiations

- U_FifoAsync: surf.FifoAsync
