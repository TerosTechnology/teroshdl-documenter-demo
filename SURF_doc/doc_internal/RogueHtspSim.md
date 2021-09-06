# Entity: RogueHtspSim

- **File**: RogueHtspSim.vhd
## Diagram

![Diagram](RogueHtspSim.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : HTSP: https://confluence.slac.stanford.edu/x/pQmODw
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper on RogueStreamSim to simulate a HTSP
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
| htspRefClk      | in        | sl                                        | GT Ports                 |
| htspClk         | out       | sl                                        | HTSP Clock and Reset     |
| htspRst         | out       | sl                                        |                          |
| htspRxIn        | in        | HtspRxInType                              | Non VC Rx Signals        |
| htspRxOut       | out       | HtspRxOutType                             |                          |
| htspTxIn        | in        | HtspTxInType                              | Non VC Tx Signals        |
| htspTxOut       | out       | HtspTxOutType                             |                          |
| htspTxMasters   | in        | AxiStreamMasterArray(NUM_VC_G-1 downto 0) | Frame Transmit Interface |
| htspTxSlaves    | out       | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                          |
| htspRxMasters   | out       | AxiStreamMasterArray(NUM_VC_G-1 downto 0) | Frame Receive Interface  |
| htspRxSlaves    | in        | AxiStreamSlaveArray(NUM_VC_G-1 downto 0)  |                          |
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
| txOut | HtspTxOutType |             |
| rxOut | HtspRxOutType |             |
## Instantiations

- PwrUpRst_Inst: surf.PwrUpRst
