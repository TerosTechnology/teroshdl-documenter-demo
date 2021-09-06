# Entity: RoguePgp3Sim

- **File**: RoguePgp3Sim.vhd
## Diagram

![Diagram](RoguePgp3Sim.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper on RogueStreamSim to simulate a PGPv3
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

| Generic name  | Type                        | Value | Description |
| ------------- | --------------------------- | ----- | ----------- |
| TPD_G         | time                        | 1 ns  |             |
| PORT_NUM_G    | natural range 1024 to 49151 | 9000  |             |
| NUM_VC_G      | integer range 1 to 16       | 4     |             |
| EN_SIDEBAND_G | boolean                     | true  |             |
## Ports

| Port name       | Direction | Type                                      | Description              |
| --------------- | --------- | ----------------------------------------- | ------------------------ |
| pgpRefClk       | in        | sl                                        | GT Ports                 |
| pgpGtRxP        | in        | sl                                        |                          |
| pgpGtRxN        | in        | sl                                        |                          |
| pgpGtTxP        | out       | sl                                        |                          |
| pgpGtTxN        | out       | sl                                        |                          |
| pgpClk          | out       | sl                                        | PGP Clock and Reset      |
| pgpClkRst       | out       | sl                                        |                          |
| pgpRxIn         | in        | Pgp3RxInType                              | Non VC Rx Signals        |
| pgpRxOut        | out       | Pgp3RxOutType                             |                          |
| pgpTxIn         | in        | Pgp3TxInType                              | Non VC Tx Signals        |
| pgpTxOut        | out       | Pgp3TxOutType                             |                          |
| pgpTxMasters    | in        | AxiStreamMasterArray(NUM_VC_G-1 downto 0) | Frame Transmit Interface |
| pgpTxSlaves     | out       | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                          |
| pgpRxMasters    | out       | AxiStreamMasterArray(NUM_VC_G-1 downto 0) | Frame Receive Interface  |
| pgpRxSlaves     | in        | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                          |
| axilClk         | in        | sl                                        |  Stable Clock            |
| axilRst         | in        | sl                                        |                          |
| axilReadMaster  | in        | AxiLiteReadMasterType                     |                          |
| axilReadSlave   | out       | AxiLiteReadSlaveType                      |                          |
| axilWriteMaster | in        | AxiLiteWriteMasterType                    |                          |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                     |                          |
## Signals

| Name  | Type          | Description |
| ----- | ------------- | ----------- |
| clk   | sl            |             |
| rst   | sl            |             |
| txOut | Pgp3TxOutType |             |
| rxOut | Pgp3RxOutType |             |
## Instantiations

- PwrUpRst_Inst: surf.PwrUpRst
