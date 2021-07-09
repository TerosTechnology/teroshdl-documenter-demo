# Entity: Pgp4TxLiteWrapper

## Diagram

![Diagram](Pgp4TxLiteWrapper.svg "Diagram")
## Description

Title      : PGPv4: https://confluence.slac.stanford.edu/x/1dzgEQ
Company    : SLAC National Accelerator Laboratory
Description: Wrapper for Pgp4TxLite (targeted/optimized for ASIC integration)
This file is part of SURF. It is subject to
the license terms in the LICENSE.txt file found in the top-level directory
of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of SURF, including this file, may be
copied, modified, propagated, or distributed except according to the terms
contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name  | Direction | Type             | Description             |
| ---------- | --------- | ---------------- | ----------------------- |
| clk        | in        | sl               | Clock and Reset         |
| rst        | in        | sl               | Active HIGH reset       |
| txValid    | in        | sl               | tValid                  |
| txReady    | out       | sl               | tReady                  |
| txData     | in        | slv(63 downto 0) | tData                   |
| txEnable   | in        | sl               |                         |
| txSof      | in        | sl               | tUser.FirstByte.BIT1    |
| txEof      | in        | sl               | tLast                   |
| txEofe     | in        | sl               | tUser.LastByte.BIT0     |
| phyTxValid | out       | sl               | 66-bit Output Interface |
| phyTxData  | out       | slv(65 downto 0) |                         |
## Signals

| Name        | Type                | Description                            |
| ----------- | ------------------- | -------------------------------------- |
| pgpTxIn     | Pgp4TxInType        |                                        |
| pgpTxMaster | AxiStreamMasterType | sideband locData not being implemented |
| pgpTxSlave  | AxiStreamSlaveType  |                                        |
## Instantiations

- U_Pgp4TxLite: surf.Pgp4TxLite
