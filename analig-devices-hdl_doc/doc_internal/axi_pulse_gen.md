# Entity: axi_pulse_gen

- **File**: axi_pulse_gen.v
## Diagram

![Diagram](axi_pulse_gen.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2019 (c) Analog Devices, Inc. All rights reserved.

 In this HDL repository, there are many different and unique modules, consisting
 of various HDL (Verilog or VHDL) components. The individual modules are
 developed independently, and may be accompanied by separate and unique license
 terms.

 The user should read each of these license terms, and understand the
 freedoms and responsibilities that he or she has by using this source/core.

 This core is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE.

 Redistribution and use of source or resulting binaries, with or without modification
 of this file, are permitted under one of the following two license terms:

   1. The GNU General Public License version 2 as published by the
      Free Software Foundation, which can be found in the top level directory
      of this repository (LICENSE_GPL2), and also online at:
      <https://www.gnu.org/licenses/old-licenses/gpl-2.0.html>

 OR

   2. An ADI specific BSD license, which can be found in the top level directory
      of this repository (LICENSE_ADIBSD), and also on-line at:
      https://github.com/analogdevicesinc/hdl/blob/master/LICENSE_ADIBSD
      This will allow to generate bit files and not release the source code,
      as long as it attaches to an ADI device.

 ***************************************************************************
 ***************************************************************************

## Generics

| Generic name | Type  | Value | Description |
| ------------ | ----- | ----- | ----------- |
| ID           |       | 0     |             |
| ASYNC_CLK_EN | [0:0] | 1     |             |
| PULSE_WIDTH  |       | 7     |             |
| PULSE_PERIOD |       | 10    |             |
## Ports

| Port name     | Direction | Type   | Description    |
| ------------- | --------- | ------ | -------------- |
| s_axi_aclk    | input     |        |  axi interface |
| s_axi_aresetn | input     |        |                |
| s_axi_awvalid | input     |        |                |
| s_axi_awaddr  | input     | [15:0] |                |
| s_axi_awprot  | input     | [ 2:0] |                |
| s_axi_awready | output    |        |                |
| s_axi_wvalid  | input     |        |                |
| s_axi_wdata   | input     | [31:0] |                |
| s_axi_wstrb   | input     | [ 3:0] |                |
| s_axi_wready  | output    |        |                |
| s_axi_bvalid  | output    |        |                |
| s_axi_bresp   | output    | [ 1:0] |                |
| s_axi_bready  | input     |        |                |
| s_axi_arvalid | input     |        |                |
| s_axi_araddr  | input     | [15:0] |                |
| s_axi_arprot  | input     | [ 2:0] |                |
| s_axi_arready | output    |        |                |
| s_axi_rvalid  | output    |        |                |
| s_axi_rresp   | output    | [ 1:0] |                |
| s_axi_rdata   | output    | [31:0] |                |
| s_axi_rready  | input     |        |                |
| ext_clk       | input     |        |                |
| pulse         | output    |        |                |
## Signals

| Name             | Type        | Description        |
| ---------------- | ----------- | ------------------ |
| clk              | wire        |  internal signals  |
| up_clk           | wire        |                    |
| up_rstn          | wire        |                    |
| up_rreq_s        | wire        |                    |
| up_wack_s        | wire        |                    |
| up_rack_s        | wire        |                    |
| up_raddr_s       | wire [13:0] |                    |
| up_rdata_s       | wire [31:0] |                    |
| up_wreq_s        | wire        |                    |
| up_waddr_s       | wire [13:0] |                    |
| up_wdata_s       | wire [31:0] |                    |
| pulse_width_s    | wire [31:0] |                    |
| pulse_period_s   | wire [31:0] |                    |
| load_config_s    | wire        |                    |
| pulse_gen_resetn | wire        |                    |
## Constants

| Name         | Type   | Value                                        | Description |
| ------------ | ------ | -------------------------------------------- | ----------- |
| CORE_VERSION | [31:0] | {<br><span style="padding-left:20px">16'h000 | MAJOR */    |
| CORE_MAGIC   | [31:0] | 32'h504c5347                                 | PLSG        |
## Instantiations

- i_regmap: axi_pulse_gen_regmap
- util_pulse_gen_i: util_pulse_gen
- i_up_axi: up_axi
