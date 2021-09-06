# Entity: RogueTcpMemory

- **File**: RogueTcpMemory.vhd
## Diagram

![Diagram](RogueTcpMemory.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Rogue Stream Module
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Ports

| Port name | Direction | Type                          | Description    |
| --------- | --------- | ----------------------------- | -------------- |
| clock     | in        | std_logic                     |                |
| reset     | in        | std_logic                     |                |
| portNum   | in        | std_logic_vector(15 downto 0) |                |
| araddr    | out       | std_logic_vector(31 downto 0) | axiReadMaster  |
| arprot    | out       | std_logic_vector(2 downto 0)  |                |
| arvalid   | out       | std_logic                     |                |
| rready    | out       | std_logic                     |                |
| arready   | in        | std_logic                     | axiReadSlave   |
| rdata     | in        | std_logic_vector(31 downto 0) |                |
| rresp     | in        | std_logic_vector(1 downto 0)  |                |
| rvalid    | in        | std_logic                     |                |
| awaddr    | out       | std_logic_vector(31 downto 0) | axiWriteMaster |
| awprot    | out       | std_logic_vector(2 downto 0)  |                |
| awvalid   | out       | std_logic                     |                |
| wdata     | out       | std_logic_vector(31 downto 0) |                |
| wstrb     | out       | std_logic_vector(3 downto 0)  |                |
| wvalid    | out       | std_logic                     |                |
| bready    | out       | std_logic                     |                |
| awready   | in        | std_logic                     | axiWriteSlave  |
| wready    | in        | std_logic                     |                |
| bresp     | in        | std_logic_vector(1 downto 0)  |                |
| bvalid    | in        | std_logic                     |                |
