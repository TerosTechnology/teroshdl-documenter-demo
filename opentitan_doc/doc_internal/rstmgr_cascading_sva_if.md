# Package: rstmgr_pkg

- **File**: rstmgr_cascading_sva_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This has assertions that check the reset outputs of rstmgr cascade properly.
 This means higher level resets always cause the lower level ones to assert.
 The hierarchy is
   por > lc > sys > specific peripherals
 In addition, a scan reset is at the same level as por.


## Signals

| Name              | Type                                        | Description                                                              |
| ----------------- | ------------------------------------------- | ------------------------------------------------------------------------ |
| sequence          | endsequence                                 |                                                                          |
| rst_por_aon_n     | [0:PorCycles.rise.max - PorCycles.rise.min] |                                                                          |
| scan_reset_n      | logic                                       |                                                                          |
| scan_reset_n      | always_comb                                 |                                                                          |
| effective_aon_rst | logic [rstmgr_pkg::PowerDomains-1:0]        |                                                                          |
| effective_aon_rst | always_comb                                 |                                                                          |
| local_rst_n       | logic [rstmgr_pkg::PowerDomains-1:0]        |  The internal reset is triggered by one of the generated reset outputs.  |
| local_rst_n       | always_comb                                 |                                                                          |
| pd                | for                                         |                                                                          |
| power_domains     | pd < rstmgr_pkg::PowerDomains               |                                                                          |
