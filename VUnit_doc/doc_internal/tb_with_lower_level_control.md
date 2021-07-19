# Entity: tb_with_lower_level_control

- **File**: tb_with_lower_level_control.vhd
## Diagram

![Diagram](tb_with_lower_level_control.svg "Diagram")
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
## Instantiations

- test_control: work.test_control
