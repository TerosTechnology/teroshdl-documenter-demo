# Package: rstmgr_env_pkg

- **File**: rstmgr_env_pkg.sv
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0


## Constants

| Name           | Type   | Value                                               | Description                                          |
| -------------- | ------ | --------------------------------------------------- | ---------------------------------------------------- |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |  parameters  TODO: add the names of alerts in order  |
| uint           | uint   | 1                                                   |                                                      |
## Types

| Name                    | Type                                            | Description |
| ----------------------- | ----------------------------------------------- | ----------- |
| linearized_alert_dump_t | logic [$bits(alert_pkg::alert_crashdump_t)-1:0] |  types      |
