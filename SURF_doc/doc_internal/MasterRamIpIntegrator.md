# Entity: MasterRamIpIntegrator

- **File**: MasterRamIpIntegrator.vhd
## Diagram

![Diagram](MasterRamIpIntegrator.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Common shim layer between IP Integrator interface and surf RAM interface
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

| Generic name  | Type                 | Value   | Description |
| ------------- | -------------------- | ------- | ----------- |
| INTERFACENAME | string               | "M_RAM" |             |
| READ_LATENCY  | natural range 0 to 3 | 1       |             |
| ADDR_WIDTH    | positive             | 5       |             |
| DATA_WIDTH    | positive             | 32      |             |
## Ports

| Port name  | Direction | Type                                        | Description                 |
| ---------- | --------- | ------------------------------------------- | --------------------------- |
| M_RAM_CLK  | out       | std_logic                                   | IP Integrator RAM Interface |
| M_RAM_EN   | out       | std_logic                                   |                             |
| M_RAM_WE   | out       | std_logic_vector((DATA_WIDTH/8)-1 downto 0) |                             |
| M_RAM_RST  | out       | std_logic                                   |                             |
| M_RAM_ADDR | out       | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                             |
| M_RAM_DIN  | out       | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| M_RAM_DOUT | in        | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| clk        | in        | std_logic                                   | SURF RAM Interface          |
| en         | in        | std_logic                                   |                             |
| we         | in        | std_logic_vector((DATA_WIDTH/8)-1 downto 0) |                             |
| rst        | in        | std_logic                                   |                             |
| addr       | in        | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                             |
| din        | in        | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| dout       | out       | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
