# Package: rv_timer_env_pkg

- **File**: rv_timer_env_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Constants

| Name           | Type   | Value                                               | Description                                                                                                       |
| -------------- | ------ | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| uint           | uint   | 1                                                   |  local parameters and types  These are currently hardcoded to 1 - this will need to change if design is modified  |
| uint           | uint   | 1                                                   |                                                                                                                   |
| uint           | uint   | 1                                                   |  alerts                                                                                                           |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |                                                                                                                   |
## Types

| Name                       | Type                                                                                                                                        | Description |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| rv_timer_env_cfg           | undefined                                                                                                                                   |             |
| rv_timer_env_cov           | undefined                                                                                                                                   |             |
| rv_timer_virtual_sequencer | cip_base_virtual_sequencer #(rv_timer_env_cfg,<br><span style="padding-left:20px">                                        rv_timer_env_cov) |             |
