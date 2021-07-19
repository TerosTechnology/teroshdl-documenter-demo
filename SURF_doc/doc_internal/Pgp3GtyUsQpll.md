# Entity: Pgp3GtyUsQpll

- **File**: Pgp3GtyUsQpll.vhd
## Diagram

![Diagram](Pgp3GtyUsQpll.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: PGP3 GTY Ultrascale+ QPLL Wrapper
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value         | Description                  |
| ------------ | ------- | ------------- | ---------------------------- |
| TPD_G        | time    | 1 ns          |                              |
| RATE_G       | string  | "10.3125Gbps" | or "6.25Gbps" or "3.125Gbps" |
| EN_DRP_G     | boolean | true          |                              |
## Ports

| Port name       | Direction | Type                   | Description                          |
| --------------- | --------- | ---------------------- | ------------------------------------ |
| stableClk       | in        | sl                     | GT needs a stable clock to "boot up" |
| stableRst       | in        | sl                     |                                      |
| pgpRefClk       | in        | sl                     | 156.25 MHz                           |
| qpllLock        | out       | Slv2Array(3 downto 0)  |                                      |
| qpllClk         | out       | Slv2Array(3 downto 0)  |                                      |
| qpllRefclk      | out       | Slv2Array(3 downto 0)  |                                      |
| qpllRst         | in        | Slv2Array(3 downto 0)  |                                      |
| axilClk         | in        | sl                     | AXI-Lite Interface                   |
| axilRst         | in        | sl                     |                                      |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                                      |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                      |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                      |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                      |
## Signals

| Name          | Type                  | Description |
| ------------- | --------------------- | ----------- |
| pllRefClk     | slv(1 downto 0)       |             |
| pllOutClk     | slv(1 downto 0)       |             |
| pllOutRefClk  | slv(1 downto 0)       |             |
| pllFbClkLost  | slv(1 downto 0)       | unused      |
| pllLock       | slv(1 downto 0)       |             |
| pllLockDetClk | slv(1 downto 0)       |             |
| pllRefClkLost | slv(1 downto 0)       |             |
| pllPowerDown  | slv(1 downto 0)       |             |
| pllReset      | slv(1 downto 0)       |             |
| lockedStrobe  | Slv2Array(3 downto 0) |             |
| gtQPllReset   | Slv2Array(3 downto 0) |             |
## Constants

| Name            | Type             | Value                                                                                                                                                                                                                                                                                                       | Description |
| --------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| QPLL_CFG2_C     | slv(15 downto 0) |        ite((RATE_G = "10.3125Gbps"),<br><span style="padding-left:20px"> b"0000111111000000",<br><span style="padding-left:20px">           ite((RATE_G = "15.46875Gbps"),<br><span style="padding-left:20px"> b"0000111111000001",<br><span style="padding-left:20px">               b"0000111111000011")) |             |
| QPLL_CP_G3_C    | slv(9 downto 0)  |  ite((RATE_G = "3.125Gbps"),<br><span style="padding-left:20px"> b"0001111111",<br><span style="padding-left:20px"> b"0000001111")                                                                                                                                                                          |             |
| QPLL_FBDIV_C    | positive         |        ite((RATE_G = "6.25Gbps") or (RATE_G = "12.5Gbps"),<br><span style="padding-left:20px"> 80,<br><span style="padding-left:20px">           ite((RATE_G = "15.46875Gbps"),<br><span style="padding-left:20px"> 99,<br><span style="padding-left:20px">               66))                              |             |
| QPLL_FBDIV_G3_C | positive         |  ite((RATE_G = "3.125Gbps"),<br><span style="padding-left:20px"> 80,<br><span style="padding-left:20px"> 160)                                                                                                                                                                                               |             |
| QPLL_LPF_C      | slv(9 downto 0)  |        ite((RATE_G = "10.3125Gbps"),<br><span style="padding-left:20px"> b"1000111111",<br><span style="padding-left:20px">           ite((RATE_G = "15.46875Gbps"),<br><span style="padding-left:20px"> b"1101111111",<br><span style="padding-left:20px">               b"1000011111"))                   |             |
| QPLL_LPF_G3_C   | slv(9 downto 0)  |  ite((RATE_G = "3.125Gbps"),<br><span style="padding-left:20px"> b"0111010100",<br><span style="padding-left:20px"> b"0111010101")                                                                                                                                                                          |             |
## Instantiations

- U_QPLL: surf.GtyUltraScaleQuadPll
