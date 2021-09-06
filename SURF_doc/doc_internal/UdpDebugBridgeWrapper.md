# Entity: UdpDebugBridgeWrapper

- **File**: UdpDebugBridgeWrapper.vhd
## Diagram

![Diagram](UdpDebugBridgeWrapper.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for UDP 'XVC' Server
-----------------------------------------------------------------------------
 This file is part of 'xvc-udp-debug-bridge'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'xvc-udp-debug-bridge', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name      | Direction | Type                | Description       |
| -------------- | --------- | ------------------- | ----------------- |
| clk            | in        | sl                  | Clock and Reset   |
| rst            | in        | sl                  |                   |
| obServerMaster | in        | AxiStreamMasterType | UDP XVC Interface |
| obServerSlave  | out       | AxiStreamSlaveType  |                   |
| ibServerMaster | out       | AxiStreamMasterType |                   |
| ibServerSlave  | in        | AxiStreamSlaveType  |                   |
## Signals

| Name          | Type                | Description |
| ------------- | ------------------- | ----------- |
| rSof          | SofRegType          |             |
| rinSof        | SofRegType          |             |
| mXvcServerTdo | AxiStreamMasterType |             |
## Constants

| Name           | Type       | Value         | Description |
| -------------- | ---------- | ------------- | ----------- |
| SOF_REG_INIT_C | SofRegType |  (sof => '1') |             |
## Types

| Name       | Type | Description |
| ---------- | ---- | ----------- |
| SofRegType |      |             |
## Processes
- P_SOF_COMB: ( ibServerSlave, mXvcServerTdo, rSof )
- P_SOF_SEQ: ( clk )
- P_SOF_SPLICE: ( mXvcServerTdo, rSof )
**Description**
 splice in the SOF bit 
## Instantiations

- U_XvcServer: component UdpDebugBridge
