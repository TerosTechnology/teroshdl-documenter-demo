# Package: uvm_pkg

- **File**: keymgr_if.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 interface for input data from LC, OTP and flash
 

## Signals

| Name                  | Type        | Description                                        |
| --------------------- | ----------- | -------------------------------------------------- |
| edn_req_sync          | always      | for EDN assertion sync req/ack to core clk domain  |
| edn_req_sync          | end         |                                                    |
| edn_req_sync          | end         |                                                    |
| edn_req_ack_sync      | end         |                                                    |
| end                   | end         |                                                    |
| edn_req_ack_sync_done | always      |                                                    |
| edn_req_ack_sync_done | end         |                                                    |
| edn_req_ack_sync_done | end         |                                                    |
| end                   | end         |                                                    |
| edn_wait_cnt          | always      |                                                    |
| edn_wait_cnt          | end         |                                                    |
| else                  | end         |                                                    |
| edn_wait_cnt          | begin       |                                                    |
| end                   | end         |                                                    |
| begin                 | initial     |                                                    |
| rst_n                 | forever     |                                                    |
| edn_req_cnt           | edn_req_cnt |                                                    |
