# Entity: HtspRx

- **File**: HtspRx.vhd
## Diagram

![Diagram](HtspRx.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : HTSP: https://confluence.slac.stanford.edu/x/pQmODw
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: HTSP Ethernet Receiver
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

| Generic name | Type                  | Value | Description |
| ------------ | --------------------- | ----- | ----------- |
| TPD_G        | time                  | 1 ns  |             |
| NUM_VC_G     | integer range 1 to 16 | 4     |             |
## Ports

| Port name      | Direction | Type                                      | Description                   |
| -------------- | --------- | ----------------------------------------- | ----------------------------- |
| remoteMac      | out       | slv(47 downto 0)                          | Ethernet Configuration        |
| localMac       | in        | slv(47 downto 0)                          |                               |
| broadcastMac   | in        | slv(47 downto 0)                          |                               |
| etherType      | in        | slv(15 downto 0)                          |                               |
| htspClk        | in        | sl                                        | User interface                |
| htspRst        | in        | sl                                        |                               |
| htspRxIn       | in        | HtspRxInType                              |                               |
| htspRxOut      | out       | HtspRxOutType                             |                               |
| htspRxMasters  | out       | AxiStreamMasterArray(NUM_VC_G-1 downto 0) |                               |
| remRxFifoCtrl  | out       | AxiStreamCtrlArray(NUM_VC_G-1 downto 0)   | Status of local receive FIFOs |
| remRxLinkReady | out       | sl                                        |                               |
| locRxLinkReady | out       | sl                                        |                               |
| phyRxRdy       | in        | sl                                        | PHY interface                 |
| phyRxMaster    | in        | AxiStreamMasterType                       |                               |
## Signals

| Name         | Type                | Description |
| ------------ | ------------------- | ----------- |
| r            | RegType             |             |
| rin          | RegType             |             |
| htspRxMaster | AxiStreamMasterType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       aliveCnt       => (others => '0'),<br><span style="padding-left:20px">       sof            => '0',<br><span style="padding-left:20px">       locRxLinkReady => '0',<br><span style="padding-left:20px">       remRxLinkReady => '0',<br><span style="padding-left:20px">       tid            => (others => '0'),<br><span style="padding-left:20px">       tDest          => (others => '0'),<br><span style="padding-left:20px">       remoteMac      => (others => '0'),<br><span style="padding-left:20px">       htspRxOut      => HTSP_RX_OUT_INIT_C,<br><span style="padding-left:20px">       remRxFifoCtrl  => (others => AXI_STREAM_CTRL_INIT_C),<br><span style="padding-left:20px">       htspRxMasters  => (others => AXI_STREAM_MASTER_INIT_C),<br><span style="padding-left:20px">       state          => IDLE_S) |             |
## Types

| Name      | Type                                                      | Description |
| --------- | --------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> PAYLOAD_S)  |             |
| RegType   |                                                           |             |
## Processes
- comb: ( broadcastMac, etherType, htspRst, localMac, phyRxMaster,
                   phyRxRdy, r )
- seq: ( htspClk )
## Instantiations

- U_DeMux: surf.AxiStreamDeMux
