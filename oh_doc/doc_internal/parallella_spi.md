# Entity: parallella_spi

- **File**: parallella_spi.v
## Diagram

![Diagram](parallella_spi.svg "Diagram")
## Description

#############################################################################
# Purpose: Parallella SPI top                                               #
#############################################################################
# Author:   Ola Jeppsson                                                    #
# SPDX-License-Identifier:     MIT                                          #
#############################################################################

## Generics

| Generic name | Type | Value   | Description           |
| ------------ | ---- | ------- | --------------------- |
| AW           |      | 32      |  address width        |
| DW           |      | 32      |                       |
| PW           |      | 2*AW+40 |  packet width         |
| ID           |      | 12'h7fe |  addr[31:20] id       |
| S_IDW        |      | 12      |  ID width for S_AXI   |
| NGPIO        |      | 24      |  number of gpio pins  |
## Ports

| Port name     | Direction | Type        | Description               |
| ------------- | --------- | ----------- | ------------------------- |
| constant_zero | input     |             | Always 0                  |
| constant_one  | input     |             | Always 1                  |
| sys_nreset    | input     |             | active low async reset    |
| sys_clk       | input     |             | system clock for AXI      |
| gpio_n        | inout     | [NGPIO-1:0] | physical spi pins         |
| gpio_p        | inout     | [NGPIO-1:0] | physical spi pins         |
| s_axi_araddr  | input     | [31:0]      | To axi_spi of axi_spi.v   |
| s_axi_arburst | input     | [1:0]       | To axi_spi of axi_spi.v   |
| s_axi_arcache | input     | [3:0]       | To axi_spi of axi_spi.v   |
| s_axi_aresetn | input     |             | To axi_spi of axi_spi.v   |
| s_axi_arid    | input     | [S_IDW-1:0] | To axi_spi of axi_spi.v   |
| s_axi_arlen   | input     | [7:0]       | To axi_spi of axi_spi.v   |
| s_axi_arlock  | input     |             | To axi_spi of axi_spi.v   |
| s_axi_arprot  | input     | [2:0]       | To axi_spi of axi_spi.v   |
| s_axi_arqos   | input     | [3:0]       | To axi_spi of axi_spi.v   |
| s_axi_arsize  | input     | [2:0]       | To axi_spi of axi_spi.v   |
| s_axi_arvalid | input     |             | To axi_spi of axi_spi.v   |
| s_axi_awaddr  | input     | [31:0]      | To axi_spi of axi_spi.v   |
| s_axi_awburst | input     | [1:0]       | To axi_spi of axi_spi.v   |
| s_axi_awcache | input     | [3:0]       | To axi_spi of axi_spi.v   |
| s_axi_awid    | input     | [S_IDW-1:0] | To axi_spi of axi_spi.v   |
| s_axi_awlen   | input     | [7:0]       | To axi_spi of axi_spi.v   |
| s_axi_awlock  | input     |             | To axi_spi of axi_spi.v   |
| s_axi_awprot  | input     | [2:0]       | To axi_spi of axi_spi.v   |
| s_axi_awqos   | input     | [3:0]       | To axi_spi of axi_spi.v   |
| s_axi_awsize  | input     | [2:0]       | To axi_spi of axi_spi.v   |
| s_axi_awvalid | input     |             | To axi_spi of axi_spi.v   |
| s_axi_bready  | input     |             | To axi_spi of axi_spi.v   |
| s_axi_rready  | input     |             | To axi_spi of axi_spi.v   |
| s_axi_wdata   | input     | [31:0]      | To axi_spi of axi_spi.v   |
| s_axi_wid     | input     | [S_IDW-1:0] | To axi_spi of axi_spi.v   |
| s_axi_wlast   | input     |             | To axi_spi of axi_spi.v   |
| s_axi_wstrb   | input     | [3:0]       | To axi_spi of axi_spi.v   |
| s_axi_wvalid  | input     |             | To axi_spi of axi_spi.v   |
| s_axi_arready | output    |             | From axi_spi of axi_spi.v |
| s_axi_awready | output    |             | From axi_spi of axi_spi.v |
| s_axi_bid     | output    | [S_IDW-1:0] | From axi_spi of axi_spi.v |
| s_axi_bresp   | output    | [1:0]       | From axi_spi of axi_spi.v |
| s_axi_bvalid  | output    |             | From axi_spi of axi_spi.v |
| s_axi_rdata   | output    | [31:0]      | From axi_spi of axi_spi.v |
| s_axi_rid     | output    | [S_IDW-1:0] | From axi_spi of axi_spi.v |
| s_axi_rlast   | output    |             | From axi_spi of axi_spi.v |
| s_axi_rresp   | output    | [1:0]       | From axi_spi of axi_spi.v |
| s_axi_rvalid  | output    |             | From axi_spi of axi_spi.v |
| s_axi_wready  | output    |             | From axi_spi of axi_spi.v |
| spi_irq       | output    |             | From axi_spi of axi_spi.v |
| spi_m_mosi    | output    |             | From axi_spi of axi_spi.v |
| spi_m_sclk    | output    |             | From axi_spi of axi_spi.v |
| spi_m_ss      | output    |             | From axi_spi of axi_spi.v |
| spi_s_miso    | output    |             | From axi_spi of axi_spi.v |
## Signals

| Name       | Type             | Description         |
| ---------- | ---------------- | ------------------- |
| gpio_in    | wire [NGPIO-1:0] | out gpio pins       |
| gpio_out   | wire [NGPIO-1:0] | in gpio pins        |
| gpio_dir   | wire [NGPIO-1:0] | gpio pin direction  |
| spi_s_miso | wire             |  spi                |
| spi_m_ss   | wire             |                     |
| spi_m_sclk | wire             |                     |
| spi_m_mosi | wire             |                     |
| spi_s_ss   | wire             |                     |
| spi_s_sclk | wire             |                     |
| spi_s_mosi | wire             |                     |
| spi_m_miso | wire             |                     |
