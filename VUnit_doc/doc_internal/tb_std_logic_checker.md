# Entity: tb_std_logic_checker

## Diagram

![Diagram](tb_std_logic_checker.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name  | Type                         | Description |
| ----- | ---------------------------- | ----------- |
| value | std_logic_vector(1 downto 0) |             |
## Constants

| Name           | Type             | Value                                 | Description |
| -------------- | ---------------- | ------------------------------------- | ----------- |
| logger         | logger_t         |  get_logger("signal_checker")         |             |
| signal_checker | signal_checker_t |  new_signal_checker(logger => logger) |             |
## Processes
- main: (  )
## Instantiations

- dut: work.std_logic_checker
