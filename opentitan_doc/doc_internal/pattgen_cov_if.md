# Package: uvm_pkg

- **File**: pattgen_cov_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Implements functional coverage for PATTGEN.


## Signals

| Name            | Type            | Description                                                                      |
| --------------- | --------------- | -------------------------------------------------------------------------------- |
| en_full_cov     | bit             |                                                                                  |
| en_intg_cov     | bit             |                                                                                  |
| en_intg_cov_loc | bit             |  If en_full_cov is set, then en_intg_cov must also be set since it is a subset.  |
| en_intg_cov_loc | assign          |                                                                                  |
| ch0_perf        | bit             |                                                                                  |
| ch1_perf        | bit             |                                                                                  |
| ch0_perf        | assign          |                                                                                  |
| ch1_perf        | assign          |                                                                                  |
| enable          | covergroup      |                                                                                  |
| name            | option          |                                                                                  |
| comment         | option          |                                                                                  |
| per_instance    | option          |                                                                                  |
| enable          | cp_enable       |  Channel 0 coverpoints                                                           |
| CH0_ENABLE      | cp_enable       |  Channel 0 coverpoints                                                           |
| CH0_DISABLE     | bins            |                                                                                  |
| CH1_ENABLE      | bins            |                                                                                  |
| CH1_DISABLE     | bins            |                                                                                  |
| CHX_ENABLE      | bins            | CHX: dual channels                                                               |
| CHX_DISABLE     | bins            |                                                                                  |
| CHX_OTHERS      | bins            |                                                                                  |
| LOW_PERF        | cp_ch0_perf     |  Channel 0 coverpoints                                                           |
| TYP_PERF        | bins            |                                                                                  |
| TX_CLK_FALL     | cp_ch0_polarity |                                                                                  |
| TX_CLK_RISE     | bins            |                                                                                  |
| LOW_PERF        | cp_ch1_perf     |  Channel 1 coverpoints                                                           |
| TYP_PERF        | bins            |                                                                                  |
| TX_CLK_FALL     | cp_ch1_polarity |                                                                                  |
| TX_CLK_RISE     | bins            |                                                                                  |
| cp_enable       | cr_ch0_op       |  Cross coverpoints                                                               |
| cp_ch0_polarity | cr_ch0_op       |  Cross coverpoints                                                               |
| CH0_OP_ENABLE   | cr_ch0_op       |  Cross coverpoints                                                               |
| CH0_OP_DISABLE  | bins            |                                                                                  |
| cp_enable       | cr_ch1_op       |                                                                                  |
| cp_ch1_polarity | cr_ch1_op       |                                                                                  |
| CH1_OP_ENABLE   | cr_ch1_op       |                                                                                  |
| CH1_OP_DISABLE  | bins            |                                                                                  |
| cp_enable       | cr_chx_op       |                                                                                  |
| cp_ch0_polarity | cr_chx_op       |                                                                                  |
| cp_ch0_perf     | cr_chx_op       |                                                                                  |
| cp_ch1_polarity | cr_chx_op       |                                                                                  |
| CHX_OP_ENABLE   | cr_chx_op       |                                                                                  |
| CHX_OP_DISABLE  | bins            |                                                                                  |
| pattgen_cov_if  | endinterface    |                                                                                  |
