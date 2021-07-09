# Entity: XauiGth7Core

## Diagram

![Diagram](XauiGth7Core.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: 10 GigE XAUI for Gth7 Core
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Ports

| Port name            | Direction | Type                          | Description  |
| -------------------- | --------- | ----------------------------- | ------------ |
| dclk                 | in        | std_logic                     |              |
| reset                | in        | std_logic                     |              |
| clk156_out           | out       | std_logic                     |              |
| clk156_lock          | out       | std_logic                     |              |
| refclk               | in        | std_logic                     |              |
| xgmii_txd            | in        | std_logic_vector(63 downto 0) |              |
| xgmii_txc            | in        | std_logic_vector(7 downto 0)  |              |
| xgmii_rxd            | out       | std_logic_vector(63 downto 0) |              |
| xgmii_rxc            | out       | std_logic_vector(7 downto 0)  |              |
| xaui_tx_l0_p         | out       | std_logic                     |              |
| xaui_tx_l0_n         | out       | std_logic                     |              |
| xaui_tx_l1_p         | out       | std_logic                     |              |
| xaui_tx_l1_n         | out       | std_logic                     |              |
| xaui_tx_l2_p         | out       | std_logic                     |              |
| xaui_tx_l2_n         | out       | std_logic                     |              |
| xaui_tx_l3_p         | out       | std_logic                     |              |
| xaui_tx_l3_n         | out       | std_logic                     |              |
| xaui_rx_l0_p         | in        | std_logic                     |              |
| xaui_rx_l0_n         | in        | std_logic                     |              |
| xaui_rx_l1_p         | in        | std_logic                     |              |
| xaui_rx_l1_n         | in        | std_logic                     |              |
| xaui_rx_l2_p         | in        | std_logic                     |              |
| xaui_rx_l2_n         | in        | std_logic                     |              |
| xaui_rx_l3_p         | in        | std_logic                     |              |
| xaui_rx_l3_n         | in        | std_logic                     |              |
| signal_detect        | in        | std_logic_vector(3 downto 0)  |              |
| debug                | out       | std_logic_vector(5 downto 0)  | Debug vector |
| configuration_vector | in        | std_logic_vector(6 downto 0)  |              |
| status_vector        | out       | std_logic_vector(7 downto 0)  |              |
## Instantiations

- U0: XauiGth7Core_block
