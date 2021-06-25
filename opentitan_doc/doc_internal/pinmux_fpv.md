# Entity: pinmux_fpv
## Diagram
![Diagram](pinmux_fpv.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Testbench module for pinmux. Intended to use with a formal tool.
 
## Ports
| Port name          | Direction | Type                                       | Description             |
| ------------------ | --------- | ------------------------------------------ | ----------------------- |
| clk_i              | input     |                                            |                         |
| rst_ni             | input     |                                            |                         |
| tl_i               | input     |                                            |                         |
| tl_o               | output    |                                            |                         |
| periph_to_mio_i    | input     | [pinmux_reg_pkg::NMioPeriphOut-1:0]        |                         |
| periph_to_mio_oe_i | input     | [pinmux_reg_pkg::NMioPeriphOut-1:0]        |                         |
| mio_to_periph_o    | output    | [pinmux_reg_pkg::NMioPeriphIn-1:0]         |                         |
| mio_out_o          | output    | [pinmux_reg_pkg::NMioPads-1:0]             |                         |
| mio_oe_o           | output    | [pinmux_reg_pkg::NMioPads-1:0]             |                         |
| mio_in_i           | input     | [pinmux_reg_pkg::NMioPads-1:0]             |                         |
| periph_sel_i       | input     | [$clog2(pinmux_reg_pkg::NMioPeriphIn)-1:0] | symbolic inputs for FPV |
| mio_sel_i          | input     | [$clog2(pinmux_reg_pkg::NMioPads)-1:0]     |                         |
## Instantiations
- dut: pinmux
