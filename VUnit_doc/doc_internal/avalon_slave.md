# Entity: avalon_slave
## Diagram
![Diagram](avalon_slave.svg "Diagram")
## Description
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
Author Slawomir Siluk slaweksiluk@gazeta.pl
Avalon memory mapped slave wrapper for Vunit memory VC
## Generics
| Generic name | Type           | Value | Description |
| ------------ | -------------- | ----- | ----------- |
| avalon_slave | avalon_slave_t |       |             |
## Ports
| Port name     | Direction | Type             | Description |
| ------------- | --------- | ---------------- | ----------- |
| clk           | in        | std_logic        |             |
| address       | in        | std_logic_vector |             |
| byteenable    | in        | std_logic_vector |             |
| burstcount    | in        | std_logic_vector |             |
| waitrequest   | out       | std_logic        |             |
| write         | in        | std_logic        |             |
| writedata     | in        | std_logic_vector |             |
| read          | in        | std_logic        |             |
| readdata      | out       | std_logic_vector |             |
| readdatavalid | out       | std_logic        |             |
## Constants
| Name           | Type       | Value                            | Description |
| -------------- | ---------- | -------------------------------- | ----------- |
| slave_read_msg | msg_type_t |  new_msg_type("avmm slave read") |             |
## Processes
- write_handler: _(  )_

- read_request: _(  )_

- read_handler: _(  )_

- waitrequest_stim: _(  )_

