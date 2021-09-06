# Entity: bus2memory

- **File**: bus2memory.vhd
## Diagram

![Diagram](bus2memory.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type         | Value | Description |
| ------------ | ------------ | ----- | ----------- |
| bus_handle   | bus_master_t |       |             |
| memory       | memory_t     |       |             |
## Constants

| Name      | Type     | Value                    | Description |
| --------- | -------- | ------------------------ | ----------- |
| my_memory | memory_t |  to_vc_interface(memory) |             |
## Processes
- main: (  )
