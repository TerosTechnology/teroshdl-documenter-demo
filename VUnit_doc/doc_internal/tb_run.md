# Entity: tb_run

- **File**: tb_run.vhd
## Diagram

![Diagram](tb_run.svg "Diagram")
## Description

This test suite verifies the VHDL test runner functionality
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
| output_path  | string |       |             |
## Instantiations

- tests: work.run_tests
