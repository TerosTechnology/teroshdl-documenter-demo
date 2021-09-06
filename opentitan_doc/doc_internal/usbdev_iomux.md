# Entity: usbdev_iomux

- **File**: usbdev_iomux.sv
## Diagram

![Diagram](usbdev_iomux.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Copyright ETH Zurich.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 USB IO Mux

 Muxes the USB IO signals from register access, differential signaling, single-ended signaling
 and swaps D+/D- if configured. The incomming signals are also muxed and synchronized to the
 corresponding clock domain.

## Ports

| Port name              | Direction | Type                               | Description                             |
| ---------------------- | --------- | ---------------------------------- | --------------------------------------- |
| clk_i                  | input     |                                    |                                         |
| rst_ni                 | input     |                                    |                                         |
| clk_usb_48mhz_i        | input     |                                    | use usb_ prefix for signals in this clk |
| rst_usb_48mhz_ni       | input     |                                    |                                         |
| sys_hw2reg_sense_o     | output    | usbdev_hw2reg_phy_pins_sense_reg_t |  Register interface (system clk)        |
| sys_reg2hw_drive_i     | input     | usbdev_reg2hw_phy_pins_drive_reg_t |                                         |
| sys_reg2hw_config_i    | input     | usbdev_reg2hw_phy_config_reg_t     |                                         |
| sys_usb_sense_o        | output    |                                    |                                         |
| cio_usb_d_i            | input     |                                    |  External USB Interface(s) (async)      |
| cio_usb_dp_i           | input     |                                    |                                         |
| cio_usb_dn_i           | input     |                                    |                                         |
| cio_usb_d_o            | output    |                                    |                                         |
| cio_usb_se0_o          | output    |                                    |                                         |
| cio_usb_dp_o           | output    |                                    |                                         |
| cio_usb_dn_o           | output    |                                    |                                         |
| cio_usb_oe_o           | output    |                                    |                                         |
| cio_usb_tx_mode_se_o   | output    |                                    |                                         |
| cio_usb_sense_i        | input     |                                    |                                         |
| cio_usb_dp_pullup_en_o | output    |                                    |                                         |
| cio_usb_dn_pullup_en_o | output    |                                    |                                         |
| cio_usb_suspend_o      | output    |                                    |                                         |
| usb_rx_d_o             | output    |                                    |  Internal USB Interface (usb clk)       |
| usb_rx_dp_o            | output    |                                    |                                         |
| usb_rx_dn_o            | output    |                                    |                                         |
| usb_tx_d_i             | input     |                                    |                                         |
| usb_tx_se0_i           | input     |                                    |                                         |
| usb_tx_oe_i            | input     |                                    |                                         |
| usb_pwr_sense_o        | output    |                                    |                                         |
| usb_pullup_en_i        | input     |                                    |                                         |
| usb_suspend_i          | input     |                                    |                                         |
## Signals

| Name                        | Type  | Description |
| --------------------------- | ----- | ----------- |
| cio_usb_d_flipped           | logic |             |
| cio_usb_dp_pullup_en        | logic |             |
| cio_usb_dn_pullup_en        | logic |             |
| async_pwr_sense             | logic |             |
| sys_usb_sense               | logic |             |
| cio_usb_dp                  | logic |             |
| cio_usb_dn                  | logic |             |
| cio_usb_d                   | logic |             |
| pinflip                     | logic |             |
| unused_eop_single_bit       | logic |             |
| unused_rx_differential_mode | logic |             |
| unused_usb_ref_disable      | logic |             |
| unused_tx_osc_test_mode     | logic |             |
## Processes
- proc_drive_out: (  )
  - **Type:** always_comb
- proc_mux_pwr_sense: (  )
  - **Type:** always_comb
**Description**
 Power sense mux 
## Instantiations

- cdc_io_to_sys: prim_flop_2sync
**Description**
////////
 CDCs //
////////
 USB pins sense (to sysclk)

- cdc_io_to_usb: prim_flop_2sync
**Description**
 USB input pins (to usbclk)

- i_mux_tx_d_flip: prim_clock_mux2
- i_mux_dp_pull_flip: prim_clock_mux2
- i_mux_dn_pull_flip: prim_clock_mux2
- i_mux_tx_d: prim_clock_mux2
**Description**
 Use explicit muxes for the critical output signals, we do this
 to avoid glitches from synthesized logic on these signals.
 Clock muxes should be used here to achieve the best match between
 rising and falling edges on an ASIC. This mismatch on the data line
 degrades performance in the JK-KJ jitter test.

- i_mux_tx_se0: prim_clock_mux2
- i_mux_tx_oe: prim_clock_mux2
