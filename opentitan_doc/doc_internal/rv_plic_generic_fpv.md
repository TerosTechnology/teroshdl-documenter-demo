# Entity: rv_plic_generic_fpv

## Diagram

![Diagram](rv_plic_generic_fpv.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Testbench module for rv_plic. Intended to use with a formal tool.
 
## Generics

| Generic name | Type         | Value | Description               |
| ------------ | ------------ | ----- | ------------------------- |
| NumInstances | int unsigned | 1     | test all implementations  |
## Ports

| Port name  | Direction | Type                              | Description |
| ---------- | --------- | --------------------------------- | ----------- |
| clk_i      | input     |                                   |             |
| rst_ni     | input     |                                   |             |
| tl_i       | input     | [NumInstances-1:0]                |             |
| tl_o       | output    | [NumInstances-1:0]                |             |
| intr_src_i | input     | [NumInstances-1:0][NumSrc-1:0]    |             |
| alert_rx_i | input     | [NumInstances-1:0]                |             |
| alert_tx_o | output    | [NumInstances-1:0]                |             |
| irq_o      | output    | [NumInstances-1:0][NumTarget-1:0] |             |
| irq_id_o   | output    | [$clog2(NumSrc+1)-1:0]            |             |
| msip_o     | output    | [NumInstances-1:0]                |             |
## Constants

| Name         | Type         | Value | Description               |
| ------------ | ------------ | ----- | ------------------------- |
| NumInstances | int unsigned | 1     | test all implementations  |
## Instantiations

- dut: rv_plic
**Description**
TODO: once the PLIC is fully parameterizable in RTL, generate
several instances with different NumSrc and NumTarget configs here
(in a similar way as this has been done in prim_lfsr_fpv)
for (genvar k = 0; k < NumInstances; k++) begin : geNumInstances

