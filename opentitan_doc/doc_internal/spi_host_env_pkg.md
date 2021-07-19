# Package: spi_host_env_pkg

- **File**: spi_host_env_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name             | Type       | Description |
| ---------------- | ---------- | ----------- |
| spi_host_env_pkg | endpackage |             |
## Constants

| Name           | Type   | Value                                               | Description |
| -------------- | ------ | --------------------------------------------------- | ----------- |
| uint           | uint   | 1                                                   | alerts      |
| LIST_OF_ALERTS | string | {<br><span style="padding-left:20px">"fatal_fault"} |             |
## Types

| Name            | Type                                                                                                                                                                                                    | Description       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| spi_host_intr_e | enum int {<br><span style="padding-left:20px">     SpiHostError     = 0,<br><span style="padding-left:20px">     SpiHostEvent     = 1,<br><span style="padding-left:20px">     NumSpiHostIntr   = 2   } | types parameters  |
