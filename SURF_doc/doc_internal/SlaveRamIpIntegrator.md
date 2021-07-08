# Entity: SlaveRamIpIntegrator

## Diagram

![Diagram](SlaveRamIpIntegrator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Common shim layer between IP Integrator interface and surf RAM interface
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type                 | Value   | Description |
| ------------- | -------------------- | ------- | ----------- |
| INTERFACENAME | string               | "S_RAM" |             |
| READ_LATENCY  | natural range 0 to 3 | 1       |             |
| ADDR_WIDTH    | positive             | 5       |             |
| DATA_WIDTH    | positive             | 32      |             |
## Ports

| Port name  | Direction | Type                                        | Description                 |
| ---------- | --------- | ------------------------------------------- | --------------------------- |
| S_RAM_CLK  | in        | std_logic                                   | IP Integrator RAM Interface |
| S_RAM_EN   | in        | std_logic                                   |                             |
| S_RAM_WE   | in        | std_logic_vector((DATA_WIDTH/8)-1 downto 0) |                             |
| S_RAM_RST  | in        | std_logic                                   |                             |
| S_RAM_ADDR | in        | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                             |
| S_RAM_DIN  | in        | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| S_RAM_DOUT | out       | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| clk        | out       | std_logic                                   | SURF RAM Interface          |
| en         | out       | std_logic                                   |                             |
| we         | out       | std_logic_vector((DATA_WIDTH/8)-1 downto 0) |                             |
| rst        | out       | std_logic                                   |                             |
| addr       | out       | std_logic_vector(ADDR_WIDTH-1 downto 0)     |                             |
| din        | out       | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
| dout       | in        | std_logic_vector(DATA_WIDTH-1 downto 0)     |                             |
