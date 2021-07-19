# Entity: SlaveAxiIpIntegrator

- **File**: SlaveAxiIpIntegrator.vhd
## Diagram

![Diagram](SlaveAxiIpIntegrator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Common shim layer between IP Integrator interface and surf AXI interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name          | Type                      | Value   | Description              |
| --------------------- | ------------------------- | ------- | ------------------------ |
| INTERFACENAME         | string                    | "S_AXI" |                          |
| EN_ERROR_RESP         | boolean                   | false   |                          |
| MAX_BURST_LENGTH      | positive range 1 to 256   | 256     | [1, 256]                 |
| NUM_WRITE_OUTSTANDING | natural range 0 to 32     | 1       | [0, 32]                  |
| NUM_READ_OUTSTANDING  | natural range 0 to 32     | 1       | [0, 32]                  |
| SUPPORTS_NARROW_BURST | natural range 0 to 1      | 1       |                          |
| ADDR_WIDTH            | positive range 1 to 64    | 32      | [1, 64]                  |
| ID_WIDTH              | positive                  | 1       |                          |
| DATA_WIDTH            | positive range 32 to 1024 | 32      | [32,64,128,256,512,1024] |
| HAS_BURST             | natural range 0 to 1      | 1       |                          |
| HAS_CACHE             | natural range 0 to 1      | 1       |                          |
| HAS_LOCK              | natural range 0 to 1      | 1       |                          |
| HAS_PROT              | natural range 0 to 1      | 1       |                          |
| HAS_QOS               | natural range 0 to 1      | 1       |                          |
| HAS_REGION            | natural range 0 to 1      | 1       |                          |
| HAS_WSTRB             | natural range 0 to 1      | 1       |                          |
| HAS_BRESP             | natural range 0 to 1      | 1       |                          |
| HAS_RRESP             | natural range 0 to 1      | 1       |                          |
## Ports

| Port name      | Direction | Type                                        | Description                                                          |
| -------------- | --------- | ------------------------------------------- | -------------------------------------------------------------------- |
| S_AXI_ACLK     | in        | std_logic                                   | IP Integrator AXI-Lite Interface                                     |
| S_AXI_ARESETN  | in        | std_logic                                   |                                                                      |
| S_AXI_AWID     | in        | std_logic_vector(ID_WIDTH-1 downto 0)       |                                                                      |
| S_AXI_AWADDR   | in        | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                                                                      |
| S_AXI_AWLEN    | in        | std_logic_vector(7 downto 0)                |                                                                      |
| S_AXI_AWSIZE   | in        | std_logic_vector(2 downto 0)                |                                                                      |
| S_AXI_AWBURST  | in        | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_AWLOCK   | in        | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_AWCACHE  | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_AWPROT   | in        | std_logic_vector(2 downto 0)                |                                                                      |
| S_AXI_AWREGION | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_AWQOS    | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_AWVALID  | in        | std_logic                                   |      S_AXI_AWUSER   : in  std_logic_vector(AWUSER_WIDTH-1 downto 0); |
| S_AXI_AWREADY  | out       | std_logic                                   |                                                                      |
| S_AXI_WID      | in        | std_logic_vector(ID_WIDTH-1 downto 0)       |                                                                      |
| S_AXI_WDATA    | in        | std_logic_vector(DATA_WIDTH-1 downto 0)     |                                                                      |
| S_AXI_WSTRB    | in        | std_logic_vector((DATA_WIDTH/8)-1 downto 0) |                                                                      |
| S_AXI_WLAST    | in        | std_logic                                   |                                                                      |
| S_AXI_WVALID   | in        | std_logic                                   |      S_AXI_WUSER    : in  std_logic_vector(WUSER_WIDTH-1 downto 0);  |
| S_AXI_WREADY   | out       | std_logic                                   |                                                                      |
| S_AXI_BID      | out       | std_logic_vector(ID_WIDTH-1 downto 0)       |                                                                      |
| S_AXI_BRESP    | out       | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_BVALID   | out       | std_logic                                   |      S_AXI_BUSER    : out std_logic_vector(BUSER_WIDTH downto 0);    |
| S_AXI_BREADY   | in        | std_logic                                   |                                                                      |
| S_AXI_ARID     | in        | std_logic_vector(ID_WIDTH-1 downto 0)       |                                                                      |
| S_AXI_ARADDR   | in        | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                                                                      |
| S_AXI_ARLEN    | in        | std_logic_vector(7 downto 0)                |                                                                      |
| S_AXI_ARSIZE   | in        | std_logic_vector(2 downto 0)                |                                                                      |
| S_AXI_ARBURST  | in        | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_ARLOCK   | in        | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_ARCACHE  | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_ARPROT   | in        | std_logic_vector(2 downto 0)                |                                                                      |
| S_AXI_ARREGION | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_ARQOS    | in        | std_logic_vector(3 downto 0)                |                                                                      |
| S_AXI_ARVALID  | in        | std_logic                                   |      S_AXI_ARUSER   : in  std_logic_vector(ARUSER_WIDTH-1 downto 0); |
| S_AXI_ARREADY  | out       | std_logic                                   |                                                                      |
| S_AXI_RID      | out       | std_logic_vector(ID_WIDTH-1 downto 0)       |                                                                      |
| S_AXI_RDATA    | out       | std_logic_vector(DATA_WIDTH-1 downto 0)     |                                                                      |
| S_AXI_RRESP    | out       | std_logic_vector(1 downto 0)                |                                                                      |
| S_AXI_RLAST    | out       | std_logic                                   |                                                                      |
| S_AXI_RVALID   | out       | std_logic                                   |      S_AXI_RUSER    : out std_logic_vector(RUSER_WIDTH-1 downto 0);  |
| S_AXI_RREADY   | in        | std_logic                                   |                                                                      |
| axiClk         | out       | sl                                          | SURF AXI Interface                                                   |
| axiRst         | out       | sl                                          |                                                                      |
| axiReadMaster  | out       | AxiReadMasterType                           |                                                                      |
| axiReadSlave   | in        | AxiReadSlaveType                            |                                                                      |
| axiWriteMaster | out       | AxiWriteMasterType                          |                                                                      |
| axiWriteSlave  | in        | AxiWriteSlaveType                           |                                                                      |
## Signals

| Name              | Type               | Description |
| ----------------- | ------------------ | ----------- |
| S_AXI_ReadMaster  | AxiReadMasterType  |             |
| S_AXI_ReadSlave   | AxiReadSlaveType   |             |
| S_AXI_WriteMaster | AxiWriteMasterType |             |
| S_AXI_WriteSlave  | AxiWriteSlaveType  |             |
## Instantiations

- U_RstSync: surf.RstSync
