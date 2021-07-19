# Entity: tb_running_test_case

- **File**: tb_running_test_case.vhd
## Diagram

![Diagram](tb_running_test_case.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value              | Description |
| ------------ | ------ | ------------------ | ----------- |
| runner_cfg   | string | runner_cfg_default |             |
## Signals

| Name          | Type    | Description |
| ------------- | ------- | ----------- |
| start_stimuli | boolean |             |
|  stimuli_done | boolean |             |
## Processes
- test_runner: (  )
- stimuli_generator: (  )
