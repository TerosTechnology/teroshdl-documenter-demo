# Entity: tb_uart

## Diagram

![Diagram](tb_uart.svg "Diagram")
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

| Name | Type      | Description |
| ---- | --------- | ----------- |
| chan | std_logic |             |
## Constants

| Name          | Type            | Value                             | Description |
| ------------- | --------------- | --------------------------------- | ----------- |
| master_uart   | uart_master_t   |  new_uart_master                  |             |
| master_stream | stream_master_t |  as_stream(master_uart)           |             |
| slave_uart    | uart_slave_t    |  new_uart_slave(data_length => 8) |             |
| slave_stream  | stream_slave_t  |  as_stream(slave_uart)            |             |
## Processes
- main: (  )
## Instantiations

- uart_master_inst: work.uart_master
- uart_slave_inst: work.uart_slave
