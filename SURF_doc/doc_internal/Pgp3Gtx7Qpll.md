# Entity: Pgp3Gtx7Qpll

- **File**: Pgp3Gtx7Qpll.vhd
## Diagram

![Diagram](Pgp3Gtx7Qpll.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: PGPv3 GTX7's QPLL Wrapper
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type    | Value         | Description |
| ------------- | ------- | ------------- | ----------- |
| TPD_G         | time    | 1 ns          |             |
| EN_DRP_G      | boolean | true          |             |
| REFCLK_FREQ_G | real    | 312.5E+6      |             |
| RATE_G        | string  | "10.3125Gbps" |             |
## Ports

| Port name       | Direction | Type                   | Description                          |
| --------------- | --------- | ---------------------- | ------------------------------------ |
| stableClk       | in        | sl                     | GT needs a stable clock to "boot up" |
| stableRst       | in        | sl                     |                                      |
| pgpRefClk       | in        | sl                     | QPLL Clocking                        |
| qpllLock        | out       | slv(3 downto 0)        |                                      |
| qpllClk         | out       | slv(3 downto 0)        |                                      |
| qpllRefclk      | out       | slv(3 downto 0)        |                                      |
| qpllRefClkLost  | out       | slv(3 downto 0)        |                                      |
| qpllRst         | in        | slv(3 downto 0)        |                                      |
| axilClk         | in        | sl                     | AXI-Lite Interface                   |
| axilRst         | in        | sl                     |                                      |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                                      |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                      |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                      |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                      |
## Signals

| Name          | Type            | Description |
| ------------- | --------------- | ----------- |
| pllOutClk     | sl              |             |
| pllOutRefClk  | sl              |             |
| pllLock       | sl              |             |
| pllRefClkLost | sl              |             |
| pllReset      | sl              |             |
| lockedStrobe  | slv(3 downto 0) |             |
| gtQPllReset   | slv(3 downto 0) |             |
## Constants

| Name               | Type       | Value                                                                                                                          | Description |
| ------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| QPLL_CFG_C         | bit_vector |  ite((RATE_G = "10.3125Gbps"),<br><span style="padding-left:20px"> x"0680181",<br><span style="padding-left:20px"> x"06801C1") |             |
| QPLL_FBDIV_TOP_C   | positive   |  GenQpllfbdivTop                                                                                                               |             |
| QPLL_FBDIV_C       | bit_vector |  GenQplFfbdivTop(QPLL_FBDIV_TOP_C)                                                                                             |             |
| QPLL_FBDIV_RATIO_C | bit        |  GenQpllFbdivRatio(QPLL_FBDIV_TOP_C)                                                                                           |             |
| QPLL_REFCLK_DIV_C  | positive   |  GenRefclkDiv                                                                                                                  |             |
## Functions
## Instantiations

- U_QPLL: surf.Gtx7QuadPll
