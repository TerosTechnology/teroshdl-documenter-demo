# Entity: RawEthFramerWrapper

- **File**: RawEthFramerWrapper.vhd
## Diagram

![Diagram](RawEthFramerWrapper.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for RawEthFramer Module
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

| Generic name | Type             | Value   | Description |
| ------------ | ---------------- | ------- | ----------- |
| TPD_G        | time             | 1 ns    |             |
| ETH_TYPE_G   | slv(15 downto 0) | x"0010" |             |
## Ports

| Port name       | Direction | Type                   | Description                                         |
| --------------- | --------- | ---------------------- | --------------------------------------------------- |
| localMac        | in        | slv(47 downto 0)       |   big-Endian configuration                          |
| obMacMaster     | in        | AxiStreamMasterType    | Interface to Ethernet Media Access Controller (MAC) |
| obMacSlave      | out       | AxiStreamSlaveType     |                                                     |
| ibMacMaster     | out       | AxiStreamMasterType    |                                                     |
| ibMacSlave      | in        | AxiStreamSlaveType     |                                                     |
| ibAppMaster     | out       | AxiStreamMasterType    | Interface to Application engine(s)                  |
| ibAppSlave      | in        | AxiStreamSlaveType     |                                                     |
| obAppMaster     | in        | AxiStreamMasterType    |                                                     |
| obAppSlave      | out       | AxiStreamSlaveType     |                                                     |
| axilReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Interface                                  |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                                     |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                                     |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                                     |
| clk             | in        | sl                     | Clock and Reset                                     |
| rst             | in        | sl                     |                                                     |
## Signals

| Name      | Type             | Description |
| --------- | ---------------- | ----------- |
| tDest     | slv(7 downto 0)  |             |
| remoteMac | slv(47 downto 0) |             |
## Instantiations

- U_Core: surf.RawEthFramer
- U_RemoteMacLut: surf.AxiDualPortRam
**Description**
---------------
 Remote MAC LUT
---------------

