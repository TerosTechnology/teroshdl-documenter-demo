# Entity: Pgp3Gtp7RxGearbox

- **File**: Pgp3Gtp7RxGearbox.vhd
## Diagram

![Diagram](Pgp3Gtp7RxGearbox.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv3 GTP7 32B33B to 64B66B RX Gearbox
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

| Port name     | Direction | Type             | Description      |
| ------------- | --------- | ---------------- | ---------------- |
| phyRxClkFast  | in        | sl               | Slave Interface  |
| phyRxRstFast  | in        | sl               |                  |
| rxHeaderValid | in        | sl               |                  |
| rxHeader      | in        | slv(1 downto 0)  |                  |
| rxDataValid   | in        | sl               |                  |
| rxData        | in        | slv(31 downto 0) |                  |
| phyRxClkSlow  | in        | sl               | Master Interface |
| phyRxRstSlow  | in        | sl               |                  |
| phyRxValid    | out       | sl               |                  |
| phyRxHeader   | out       | slv(1 downto 0)  |                  |
| phyRxData     | out       | slv(63 downto 0) |                  |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                              | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       fifoWrite => '0',<br><span style="padding-left:20px">       fifoData  => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( phyRxRstFast, r, rxData, rxDataValid, rxHeader,
                   rxHeaderValid )
- seq: ( phyRxClkFast )
## Instantiations

- U_FifoAsync: surf.FifoAsync
