# Entity: SlaveAxiLiteIpIntegrator

## Diagram

![Diagram](SlaveAxiLiteIpIntegrator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Common shim layer between IP Integrator interface and surf AXI-Lite interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                 | Value     | Description |
| ------------- | -------------------- | --------- | ----------- |
| INTERFACENAME | string               | "S_AXI"   |             |
| EN_ERROR_RESP | boolean              | false     |             |
| HAS_PROT      | natural range 0 to 1 | 0         |             |
| HAS_WSTRB     | natural range 0 to 1 | 0         |             |
| FREQ_HZ       | positive             | 100000000 |             |
| ADDR_WIDTH    | positive             | 12        |             |
## Ports

| Port name       | Direction | Type                                    | Description                      |
| --------------- | --------- | --------------------------------------- | -------------------------------- |
| S_AXI_ACLK      | in        | std_logic                               | IP Integrator AXI-Lite Interface |
| S_AXI_ARESETN   | in        | std_logic                               |                                  |
| S_AXI_AWADDR    | in        | std_logic_vector(ADDR_WIDTH-1 downto 0) |                                  |
| S_AXI_AWPROT    | in        | std_logic_vector(2 downto 0)            |                                  |
| S_AXI_AWVALID   | in        | std_logic                               |                                  |
| S_AXI_AWREADY   | out       | std_logic                               |                                  |
| S_AXI_WDATA     | in        | std_logic_vector(31 downto 0)           |                                  |
| S_AXI_WSTRB     | in        | std_logic_vector(3 downto 0)            |                                  |
| S_AXI_WVALID    | in        | std_logic                               |                                  |
| S_AXI_WREADY    | out       | std_logic                               |                                  |
| S_AXI_BRESP     | out       | std_logic_vector(1 downto 0)            |                                  |
| S_AXI_BVALID    | out       | std_logic                               |                                  |
| S_AXI_BREADY    | in        | std_logic                               |                                  |
| S_AXI_ARADDR    | in        | std_logic_vector(ADDR_WIDTH-1 downto 0) |                                  |
| S_AXI_ARPROT    | in        | std_logic_vector(2 downto 0)            |                                  |
| S_AXI_ARVALID   | in        | std_logic                               |                                  |
| S_AXI_ARREADY   | out       | std_logic                               |                                  |
| S_AXI_RDATA     | out       | std_logic_vector(31 downto 0)           |                                  |
| S_AXI_RRESP     | out       | std_logic_vector(1 downto 0)            |                                  |
| S_AXI_RVALID    | out       | std_logic                               |                                  |
| S_AXI_RREADY    | in        | std_logic                               |                                  |
| axilClk         | out       | sl                                      | SURF AXI-Lite Interface          |
| axilRst         | out       | sl                                      |                                  |
| axilReadMaster  | out       | AxiLiteReadMasterType                   |                                  |
| axilReadSlave   | in        | AxiLiteReadSlaveType                    |                                  |
| axilWriteMaster | out       | AxiLiteWriteMasterType                  |                                  |
| axilWriteSlave  | in        | AxiLiteWriteSlaveType                   |                                  |
## Signals

| Name              | Type                   | Description |
| ----------------- | ---------------------- | ----------- |
| S_AXI_ReadMaster  | AxiLiteReadMasterType  |             |
| S_AXI_ReadSlave   | AxiLiteReadSlaveType   |             |
| S_AXI_WriteMaster | AxiLiteWriteMasterType |             |
| S_AXI_WriteSlave  | AxiLiteWriteSlaveType  |             |
## Instantiations

- U_RstSync: surf.RstSync
