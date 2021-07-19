# Package: entropy_src_pkg

- **File**: entropy_src_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name            | Type       | Description |
| --------------- | ---------- | ----------- |
| entropy_src_pkg | endpackage |             |
## Constants

| Name                    | Type                    | Value                            | Description |
| ----------------------- | ----------------------- | -------------------------------- | ----------- |
| RNG_BUS_WIDTH           | int                     | 4                                |             |
| CSRNG_BUS_WIDTH         | int                     | 384                              |             |
| FIPS_BUS_WIDTH          | int                     | 1                                |             |
| FIPS_CSRNG_BUS_WIDTH    | int                     | FIPS_BUS_WIDTH + CSRNG_BUS_WIDTH |             |
| entropy_src_hw_if_req_t | entropy_src_hw_if_req_t | undefined                        |             |
| entropy_src_hw_if_rsp_t | entropy_src_hw_if_rsp_t | undefined                        |             |
| cs_aes_halt_req_t       | cs_aes_halt_req_t       | undefined                        |             |
| cs_aes_halt_rsp_t       | cs_aes_halt_rsp_t       | undefined                        |             |
| entropy_src_rng_req_t   | entropy_src_rng_req_t   | undefined                        |             |
| entropy_src_rng_rsp_t   | entropy_src_rng_rsp_t   | undefined                        |             |
| entropy_src_xht_req_t   | entropy_src_xht_req_t   | undefined                        |             |
| entropy_src_xht_rsp_t   | entropy_src_xht_rsp_t   | undefined                        |             |
## Types

| Name                    | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                          |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| entropy_src_hw_if_rsp_t | struct packed {<br><span style="padding-left:20px">     logic es_ack;<br><span style="padding-left:20px">     logic [CSRNG_BUS_WIDTH-1:0] es_bits;<br><span style="padding-left:20px">     logic [FIPS_BUS_WIDTH-1:0] es_fips;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                          | es entropy i/f                       |
| entropy_src_hw_if_req_t | struct packed {<br><span style="padding-left:20px">     logic es_req;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                                   |                                      |
| cs_aes_halt_req_t       | struct packed {<br><span style="padding-left:20px">     logic cs_aes_halt_req;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                          | csrng block encrypt request/ack i/f  |
| cs_aes_halt_rsp_t       | struct packed {<br><span style="padding-left:20px">     logic cs_aes_halt_ack;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                          |                                      |
| entropy_src_rng_req_t   | struct packed {<br><span style="padding-left:20px">     logic rng_enable;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                               | ast rng i/f                          |
| entropy_src_rng_rsp_t   | struct packed {<br><span style="padding-left:20px">     logic rng_valid;<br><span style="padding-left:20px">     logic [RNG_BUS_WIDTH-1:0] rng_b;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                       |                                      |
| entropy_src_xht_req_t   | struct packed {<br><span style="padding-left:20px">     logic [RNG_BUS_WIDTH-1:0] entropy_bit;<br><span style="padding-left:20px">     logic entropy_bit_valid;<br><span style="padding-left:20px">     logic clear;<br><span style="padding-left:20px">     logic active;<br><span style="padding-left:20px">     logic [15:0] thresh_hi;<br><span style="padding-left:20px">     logic [15:0] thresh_lo;<br><span style="padding-left:20px">     logic [15:0] window;<br><span style="padding-left:20px">   } | external health test i/f             |
| entropy_src_xht_rsp_t   | struct packed {<br><span style="padding-left:20px">     logic[15:0] test_cnt;<br><span style="padding-left:20px">     logic test_fail_hi_pulse;<br><span style="padding-left:20px">     logic test_fail_lo_pulse;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                       |                                      |
