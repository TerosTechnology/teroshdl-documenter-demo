# Entity: uart_slave

## Diagram

![Diagram](uart_slave.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| uart         | uart_slave_t |       |             |
## Ports

| Port name | Direction | Type      | Description |
| --------- | --------- | --------- | ----------- |
| rx        | in        | std_logic |             |
## Signals

| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| baud_rate   | natural   |             |
| local_event | std_logic |             |
## Constants

| Name       | Type    | Value      | Description |
| ---------- | ------- | ---------- | ----------- |
| data_queue | queue_t |  new_queue |             |
## Processes
- main: (  )
- recv: (  )
