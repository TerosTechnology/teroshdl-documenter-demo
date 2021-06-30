# Entity: tb_bus_master_pkg

## Diagram

![Diagram](tb_bus_master_pkg.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Constants

| Name                               | Type         | Value                                                                                   | Description |
| ---------------------------------- | ------------ | --------------------------------------------------------------------------------------- | ----------- |
| memory                             | memory_t     |  new_memory                                                                             |             |
| bus_handle                         | bus_master_t |  new_bus(data_length => 32, address_length => 32)                                       |             |
| logger                             | logger_t     |  get_logger("logger")                                                                   |             |
| actor                              | actor_t      |  new_actor("actor")                                                                     |             |
| custom_logger_and_actor_bus_handle | bus_master_t |      new_bus(data_length => 32, address_length => 32, logger => logger, actor => actor) |             |
## Processes
- main: (  )
## Instantiations

- bus2memory_inst: work.bus2memory
