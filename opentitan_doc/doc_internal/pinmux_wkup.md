# Entity: pinmux_wkup

- **File**: pinmux_wkup.sv
## Diagram

![Diagram](pinmux_wkup.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Cycles       | int  | 4     |             |
## Ports

| Port name        | Direction | Type               | Description                  |
| ---------------- | --------- | ------------------ | ---------------------------- |
| clk_i            | input     |                    |                              |
| rst_ni           | input     |                    |                              |
| wkup_en_i        | input     |                    |                              |
| filter_en_i      | input     |                    |                              |
| wkup_mode_i      | input     | wkup_mode_e        |                              |
| wkup_cnt_th_i    | input     | [WkupCntWidth-1:0] |                              |
| pin_value_i      | input     |                    |                              |
| aon_wkup_pulse_o | output    |                    |  Wakeup request pulse signal |
## Signals

| Name         | Type                     | Description                                                                                                                                                                                                                                                |
| ------------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter_out   | logic                    | //////////////////////////  Optional Signal Filter // //////////////////////////  This uses a lower value for filtering than GPIO since  the always-on clock is slower. This can be disabled,  in which case the signal is just combinationally bypassed.  |
| filter_out_d | logic                    | //////////////////////////  Optional Signal Filter // //////////////////////////  This uses a lower value for filtering than GPIO since  the always-on clock is slower. This can be disabled,  in which case the signal is just combinationally bypassed.  |
| filter_out_q | logic                    | //////////////////////////  Optional Signal Filter // //////////////////////////  This uses a lower value for filtering than GPIO since  the always-on clock is slower. This can be disabled,  in which case the signal is just combinationally bypassed.  |
| rising       | logic                    | ////////////////////  Pattern Matching // ////////////////////                                                                                                                                                                                             |
| falling      | logic                    | ////////////////////  Pattern Matching // ////////////////////                                                                                                                                                                                             |
| cnt_en       | logic                    |                                                                                                                                                                                                                                                            |
| cnt_eq_th    | logic                    |                                                                                                                                                                                                                                                            |
| cnt_d        | logic [WkupCntWidth-1:0] |                                                                                                                                                                                                                                                            |
| cnt_q        | logic [WkupCntWidth-1:0] |                                                                                                                                                                                                                                                            |
## Processes
- p_mode: (  )
  - **Type:** always_comb
- p_aon_pattern: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always_ff
## Instantiations

- u_prim_filter: prim_filter
- u_prim_flop_2sync_filter: prim_flop_2sync
</br>**Description**
 Run this through a 2 stage synchronizer to
 prevent metastability.

