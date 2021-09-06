# Entity: util_gmii_to_rgmii

- **File**: util_gmii_to_rgmii.v
## Diagram

![Diagram](util_gmii_to_rgmii.svg "Diagram")
## Description

 ***************************************************************************
 ***************************************************************************
 Copyright 2014 - 2017 (c) Analog Devices, Inc. All rights reserved.

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
 based on XILINX xapp692
 specific for MOTCON2 ADI board
 works correctly if the PHY is set with Autonegotiation on

## Generics

| Generic name     | Type | Value            | Description |
| ---------------- | ---- | ---------------- | ----------- |
| PHY_AD           |      | 5'b10000         |             |
| IODELAY_CTRL     |      | 1'b0             |             |
| IDELAY_VALUE     |      | 18               |             |
| IODELAY_GROUP    |      | "if_delay_group" |             |
| REFCLK_FREQUENCY |      | 200              |             |
## Ports

| Port name      | Direction | Type   | Description |
| -------------- | --------- | ------ | ----------- |
| clk_20m        | input     |        |             |
| clk_25m        | input     |        |             |
| clk_125m       | input     |        |             |
| idelayctrl_clk | input     |        |             |
| reset          | input     |        |             |
| rgmii_td       | output    | [ 3:0] |             |
| rgmii_tx_ctl   | output    |        |             |
| rgmii_txc      | output    |        |             |
| rgmii_rd       | input     | [ 3:0] |             |
| rgmii_rx_ctl   | input     |        |             |
| rgmii_rxc      | input     |        |             |
| mdio_mdc       | input     |        |             |
| mdio_in_w      | input     |        |             |
| mdio_in_r      | input     |        |             |
| gmii_txd       | input     | [ 7:0] |             |
| gmii_tx_en     | input     |        |             |
| gmii_tx_er     | input     |        |             |
| gmii_tx_clk    | output    |        |             |
| gmii_crs       | output    |        |             |
| gmii_col       | output    |        |             |
| gmii_rxd       | output    | [ 7:0] |             |
| gmii_rx_dv     | output    |        |             |
| gmii_rx_er     | output    |        |             |
| gmii_rx_clk    | output    |        |             |
## Signals

| Name               | Type         | Description                        |
| ------------------ | ------------ | ---------------------------------- |
| clk_2_5m           | wire         |  wires                             |
| clk_100msps        | wire         |                                    |
| rgmii_rd_delay     | wire [ 3:0]  |                                    |
| gmii_rxd_s         | wire [ 7:0]  |                                    |
| rgmii_rx_ctl_delay | wire         |                                    |
| rgmii_rx_ctl_s     | wire         |                                    |
| speed_selection    | wire [ 1:0]  | 1x gigabit, 01 100Mbps, 00 10mbps  |
| duplex_mode        | wire         | 1 full, 0 half                     |
| tx_reset_d1        | reg          |  registers                         |
| tx_reset_sync      | reg          |                                    |
| rx_reset_d1        | reg          |                                    |
| gmii_txd_r         | reg   [ 7:0] |                                    |
| gmii_tx_en_r       | reg          |                                    |
| gmii_tx_er_r       | reg          |                                    |
| gmii_txd_r_d1      | reg   [ 7:0] |                                    |
| gmii_tx_en_r_d1    | reg          |                                    |
| gmii_tx_er_r_d1    | reg          |                                    |
| rgmii_tx_ctl_r     | reg          |                                    |
| gmii_txd_low       | reg   [ 3:0] |                                    |
| idelayctrl_reset   | reg          |                                    |
| idelay_reset_cnt   | reg [ 3:0]   |                                    |
## Processes
- unnamed: ( @(posedge gmii_rx_clk) )
  - **Type:** always
- unnamed: ( @(posedge gmii_tx_clk_s) )
  - **Type:** always
- unnamed: ( @(posedge gmii_tx_clk_s) )
  - **Type:** always
- unnamed: ( @(posedge gmii_tx_clk_s) )
  - **Type:** always
## Instantiations

- clk_2_5_divide: BUFR
- clk_tx_mux0: BUFGMUX
- clk_tx_mux1: BUFGMUX
- rgmii_txc_out: ODDR
- rgmii_tx_ctl_out: ODDR
- bufmr_rgmii_rxc: BUFG
- delay_rgmii_rx_ctl: IDELAYE2
- rgmii_rx_ctl_iddr: IDDR
- mdc_mdio_in: mdc_mdio
