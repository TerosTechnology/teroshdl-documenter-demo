# Entity: MasterAxiStreamIpIntegrator

- **File**: MasterAxiStreamIpIntegrator.vhd
## Diagram

![Diagram](MasterAxiStreamIpIntegrator.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Common shim layer between IP Integrator interface and surf AXI Stream interface
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

| Generic name    | Type                   | Value    | Description |
| --------------- | ---------------------- | -------- | ----------- |
| INTERFACENAME   | string                 | "M_AXIS" |             |
| HAS_TLAST       | natural range 0 to 1   | 1        |             |
| HAS_TKEEP       | natural range 0 to 1   | 1        |             |
| HAS_TSTRB       | natural range 0 to 1   | 0        |             |
| HAS_TREADY      | natural range 0 to 1   | 1        |             |
| TUSER_WIDTH     | natural range 1 to 8   | 2        |             |
| TID_WIDTH       | natural range 1 to 8   | 1        |             |
| TDEST_WIDTH     | natural range 1 to 8   | 1        |             |
| TDATA_NUM_BYTES | natural range 1 to 128 | 1        |             |
## Ports

| Port name      | Direction | Type                                             | Description                        |
| -------------- | --------- | ------------------------------------------------ | ---------------------------------- |
| M_AXIS_ACLK    | in        | std_logic                                        | IP Integrator AXI Stream Interface |
| M_AXIS_ARESETN | in        | std_logic                                        |                                    |
| M_AXIS_TVALID  | out       | std_logic                                        |                                    |
| M_AXIS_TDATA   | out       | std_logic_vector((8*TDATA_NUM_BYTES)-1 downto 0) |                                    |
| M_AXIS_TSTRB   | out       | std_logic_vector(TDATA_NUM_BYTES-1 downto 0)     |                                    |
| M_AXIS_TKEEP   | out       | std_logic_vector(TDATA_NUM_BYTES-1 downto 0)     |                                    |
| M_AXIS_TLAST   | out       | std_logic                                        |                                    |
| M_AXIS_TDEST   | out       | std_logic_vector(TDEST_WIDTH-1 downto 0)         |                                    |
| M_AXIS_TID     | out       | std_logic_vector(TID_WIDTH-1 downto 0)           |                                    |
| M_AXIS_TUSER   | out       | std_logic_vector(TUSER_WIDTH-1 downto 0)         |                                    |
| M_AXIS_TREADY  | in        | std_logic                                        |                                    |
| axisClk        | out       | sl                                               | SURF AXI Stream Interface          |
| axisRst        | out       | sl                                               |                                    |
| axisMaster     | in        | AxiStreamMasterType                              |                                    |
| axisSlave      | out       | AxiStreamSlaveType                               |                                    |
## Signals

| Name          | Type                | Description |
| ------------- | ------------------- | ----------- |
| M_AXIS_Master | AxiStreamMasterType |             |
| M_AXIS_Slave  | AxiStreamSlaveType  |             |
## Instantiations

- U_RstSync: surf.RstSync
