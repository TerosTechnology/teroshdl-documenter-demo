# Entity: Pgp3Gtp7Qpll

- **File**: Pgp3Gtp7Qpll.vhd
## Diagram

![Diagram](Pgp3Gtp7Qpll.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv3 GTP7 QPLL Wrapper
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type    | Value      | Description |
| ------------- | ------- | ---------- | ----------- |
| TPD_G         | time    | 1 ns       |             |
| EN_DRP_G      | boolean | true       |             |
| REFCLK_FREQ_G | real    | 250.0E+6   |             |
| RATE_G        | string  | "6.25Gbps" |             |
## Ports

| Port name       | Direction | Type                   | Description                          |
| --------------- | --------- | ---------------------- | ------------------------------------ |
| stableClk       | in        | sl                     | GT needs a stable clock to "boot up" |
| stableRst       | in        | sl                     |                                      |
| pgpRefClk       | in        | sl                     | QPLL Clocking                        |
| qPllOutClk      | out       | Slv2Array(3 downto 0)  |                                      |
| qPllOutRefClk   | out       | Slv2Array(3 downto 0)  |                                      |
| qPllLock        | out       | Slv2Array(3 downto 0)  |                                      |
| qPllRefClkLost  | out       | Slv2Array(3 downto 0)  |                                      |
| qpllRst         | in        | Slv2Array(3 downto 0)  |                                      |
| axilClk         | in        | sl                     | AXI-Lite Interface                   |
| axilRst         | in        | sl                     |                                      |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                                      |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                      |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                      |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                      |
## Signals

| Name           | Type                  | Description |
| -------------- | --------------------- | ----------- |
| qPllRefClk     | slv(1 downto 0)       |             |
| qPllLockDetClk | slv(1 downto 0)       |             |
| pllOutClk      | slv(1 downto 0)       |             |
| pllOutRefClk   | slv(1 downto 0)       |             |
| pllLock        | slv(1 downto 0)       |             |
| pllRefClkLost  | slv(1 downto 0)       |             |
| pllReset       | slv(1 downto 0)       |             |
| lockedStrobe   | Slv2Array(3 downto 0) |             |
| gtQPllReset    | Slv2Array(3 downto 0) |             |
## Constants

| Name            | Type     | Value          | Description |
| --------------- | -------- | -------------- | ----------- |
| FBDIV_IN_C      | positive |  GenQpllFbDiv  |             |
| FBDIV_45_IN_C   | positive |  5             |             |
| REFCLK_DIV_IN_C | positive |  GenQpllRefDiv |             |
## Functions
## Instantiations

- U_QPLL: surf.Gtp7QuadPll
