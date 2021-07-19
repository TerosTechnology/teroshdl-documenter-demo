# Entity: Pgp4RxEb

- **File**: Pgp4RxEb.vhd
## Diagram

![Diagram](Pgp4RxEb.svg "Diagram")
## Description

Title      : PGPv4: https://confluence.slac.stanford.edu/x/1dzgEQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv4 Rx Elastic Buffer
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

| Port name   | Direction | Type             | Description                   |
| ----------- | --------- | ---------------- | ----------------------------- |
| phyRxClk    | in        | sl               |                               |
| phyRxRst    | in        | sl               |                               |
| phyRxValid  | in        | sl               |                               |
| phyRxData   | in        | slv(63 downto 0) | Unscrambled data from the PHY |
| phyRxHeader | in        | slv(1 downto 0)  |                               |
| pgpRxClk    | in        | sl               | User Transmit interface       |
| pgpRxRst    | in        | sl               |                               |
| pgpRxValid  | out       | sl               |                               |
| pgpRxData   | out       | slv(63 downto 0) |                               |
| pgpRxHeader | out       | slv(1 downto 0)  |                               |
| remLinkData | out       | slv(47 downto 0) |                               |
| overflow    | out       | sl               |                               |
| linkError   | out       | sl               |                               |
| status      | out       | slv(8 downto 0)  |                               |
## Signals

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| r           | RegType |             |
| rin         | RegType |             |
| valid       | sl      |             |
| overflowInt | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                        | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| REG_INIT_C | RegType |  (       linkError   => '0',<br><span style="padding-left:20px">       dataValid   => '0',<br><span style="padding-left:20px">       remLinkData => (others => '0'),<br><span style="padding-left:20px">       fifoIn      => (others => '0'),<br><span style="padding-left:20px">       fifoWrEn    => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( phyRxData, phyRxHeader, phyRxRst, phyRxValid, r )
- seq: ( phyRxClk )
## Instantiations

- U_remLinkData: surf.SynchronizerFifo
- U_FifoAsync_1: surf.FifoAsync
- U_overflow: surf.SynchronizerOneShot
- U_linkError: surf.SynchronizerOneShot
