# Entity: tb_com

- **File**: tb_com.vhd
## Diagram

![Diagram](tb_com.svg "Diagram")
## Description

Test suite for com package
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name                           | Type                     | Description |
| ------------------------------ | ------------------------ | ----------- |
| hello_world_received           | boolean                  |             |
|  start_receiver                | boolean                  |             |
|  start_server                  | boolean                  |             |
| start_server2                  | boolean                  |             |
|  start_server3                 | boolean                  |             |
|  start_server4                 | boolean                  |             |
|  start_server5                 | boolean                  |             |
| start_server6                  | boolean                  |             |
|  start_subscribers             | boolean                  |             |
|  start_publishers              | boolean                  |             |
| hello_subscriber_received      | std_logic_vector(1 to 2) |             |
| start_limited_inbox            | boolean                  |             |
|  limited_inbox_actor_done      | boolean                  |             |
| start_limited_inbox_subscriber | boolean                  |             |
## Constants

| Name       | Type     | Value                        | Description |
| ---------- | -------- | ---------------------------- | ----------- |
| com_logger | logger_t |  get_logger("vunit_lib:com") |             |
## Processes
- test_runner: (  )
- my_receiver: (  )
- server: (  )
- server2: (  )
- server3: (  )
- server4: (  )
- server5: (  )
- server6: (  )
- limited_inbox_actor: (  )
- limited_inbox_subscriber: (  )
