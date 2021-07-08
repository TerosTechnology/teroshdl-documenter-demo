# Entity: AxiVersionIpIntegrator

## Diagram

![Diagram](AxiVersionIpIntegrator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: IP Integrator Wrapper for surf.AxiVersion
TCL Command: create_bd_cell -type module -reference AxiVersionIpIntegrator AxiVersion_0
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type     | Value     | Description |
| ------------- | -------- | --------- | ----------- |
| EN_ERROR_RESP | boolean  | false     |             |
| FREQ_HZ       | positive | 125000000 |             |
## Ports

| Port name      | Direction | Type                                 | Description                        |
| -------------- | --------- | ------------------------------------ | ---------------------------------- |
| S_AXI_ACLK     | in        | std_logic                            | AXI-Lite Interface                 |
| S_AXI_ARESETN  | in        | std_logic                            |                                    |
| S_AXI_AWADDR   | in        | std_logic_vector(11 downto 0)        | Must match ADDR_WIDTH_C            |
| S_AXI_AWPROT   | in        | std_logic_vector(2 downto 0)         |                                    |
| S_AXI_AWVALID  | in        | std_logic                            |                                    |
| S_AXI_AWREADY  | out       | std_logic                            |                                    |
| S_AXI_WDATA    | in        | std_logic_vector(31 downto 0)        |                                    |
| S_AXI_WSTRB    | in        | std_logic_vector(3 downto 0)         |                                    |
| S_AXI_WVALID   | in        | std_logic                            |                                    |
| S_AXI_WREADY   | out       | std_logic                            |                                    |
| S_AXI_BRESP    | out       | std_logic_vector(1 downto 0)         |                                    |
| S_AXI_BVALID   | out       | std_logic                            |                                    |
| S_AXI_BREADY   | in        | std_logic                            |                                    |
| S_AXI_ARADDR   | in        | std_logic_vector(11 downto 0)        | Must match ADDR_WIDTH_C            |
| S_AXI_ARPROT   | in        | std_logic_vector(2 downto 0)         |                                    |
| S_AXI_ARVALID  | in        | std_logic                            |                                    |
| S_AXI_ARREADY  | out       | std_logic                            |                                    |
| S_AXI_RDATA    | out       | std_logic_vector(31 downto 0)        |                                    |
| S_AXI_RRESP    | out       | std_logic_vector(1 downto 0)         |                                    |
| S_AXI_RVALID   | out       | std_logic                            |                                    |
| S_AXI_RREADY   | in        | std_logic                            |                                    |
| userReset      | out       | std_logic                            | Optional: User Reset               |
| fpgaEnReload   | in        | std_logic                            | Optional: FPGA Reloading Interface |
| fpgaReload     | out       | std_logic                            |                                    |
| fpgaReloadAddr | out       | std_logic_vector(31 downto 0)        |                                    |
| upTimeCnt      | out       | std_logic_vector(31 downto 0)        |                                    |
| slowClk        | in        | std_logic                            | Optional: Serial Number outputs    |
| dnaValueOut    | out       | std_logic_vector(127 downto 0)       |                                    |
| fdValueOut     | out       | std_logic_vector(63 downto 0)        |                                    |
| userValues     | in        | std_logic_vector((64*32)-1 downto 0) | Optional: user values              |
| fdSerSdio      | inout     | std_logic                            | Optional: DS2411 interface         |
## Signals

| Name            | Type                   | Description |
| --------------- | ---------------------- | ----------- |
| axilClk         | sl                     |             |
| axilRst         | sl                     |             |
| axilReadMaster  | AxiLiteReadMasterType  |             |
| axilReadSlave   | AxiLiteReadSlaveType   |             |
| axilWriteMaster | AxiLiteWriteMasterType |             |
| axilWriteSlave  | AxiLiteWriteSlaveType  |             |
| userValuesArray | Slv32Array(0 to 63)    |             |
## Constants

| Name         | Type     | Value                | Description                        |
| ------------ | -------- | -------------------- | ---------------------------------- |
| ADDR_WIDTH_C | positive |  12                  | Must match the entity's port width |
| CLK_PERIOD_C | real     |  (1.0/real(FREQ_HZ)) | units of seconds                   |
## Processes
- unnamed: ( userValues )
## Instantiations

- U_ShimLayer: surf.SlaveAxiLiteIpIntegrator
- U_AxiVersion: surf.AxiVersion
