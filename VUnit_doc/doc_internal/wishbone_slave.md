# Entity: wishbone_slave

## Diagram

![Diagram](wishbone_slave.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
Author Slawomir Siluk slaweksiluk@gazeta.pl
Wishbone slave wrapper for Vunit memory VC
TODO:
* wb sel
* err and rty responses
## Generics

| Generic name   | Type             | Value | Description |
| -------------- | ---------------- | ----- | ----------- |
| wishbone_slave | wishbone_slave_t |       |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | in        | std_logic        |             |
| adr       | in        | std_logic_vector |             |
| dat_i     | in        | std_logic_vector |             |
| dat_o     | out       | std_logic_vector |             |
| sel       | in        | std_logic_vector |             |
| cyc       | in        | std_logic        |             |
| stb       | in        | std_logic        |             |
| we        | in        | std_logic        |             |
| stall     | out       | std_logic        |             |
| ack       | out       | std_logic        |             |
## Constants

| Name            | Type       | Value                           | Description |
| --------------- | ---------- | ------------------------------- | ----------- |
| slave_write_msg | msg_type_t |  new_msg_type("wb slave write") |             |
| slave_read_msg  | msg_type_t |  new_msg_type("wb slave read")  |             |
## Processes
- request: (  )
- acknowledge: (  )
- stall_stim: (  )
