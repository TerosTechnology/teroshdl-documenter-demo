# Package: otp_ctrl_env_pkg

- **File**: otp_ctrl_if.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This interface collect the broadcast output data from OTP,
 and drive input requests coming into OTP.
 This only supports buffered partitions.


## Signals

| Name           | Type   | Description |
| -------------- | ------ | ----------- |
| gen_partitions | tb     |             |
| otp_cmd_o      | tb     |             |
| cmd_i          | tb     |             |
| otp_hw_cfg_o   | stable |             |
