# Entity: axi_stream_slave

- **File**: axi_stream_slave.vhd
## Diagram

![Diagram](axi_stream_slave.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type               | Value | Description |
| ------------ | ------------------ | ----- | ----------- |
| slave        | axi_stream_slave_t |       |             |
## Ports

| Port name | Direction | Type                                              | Description |
| --------- | --------- | ------------------------------------------------- | ----------- |
| aclk      | in        | std_logic                                         |             |
| areset_n  | in        | std_logic                                         |             |
| tvalid    | in        | std_logic                                         |             |
| tready    | out       | std_logic                                         |             |
| tdata     | in        | std_logic_vector(data_length(slave)-1 downto 0)   |             |
| tlast     | in        | std_logic                                         |             |
| tkeep     | in        | std_logic_vector(data_length(slave)/8-1 downto 0) |             |
| tstrb     | in        | std_logic_vector(data_length(slave)/8-1 downto 0) |             |
| tid       | in        | std_logic_vector(id_length(slave)-1 downto 0)     |             |
| tdest     | in        | std_logic_vector(dest_length(slave)-1 downto 0)   |             |
| tuser     | in        | std_logic_vector(user_length(slave)-1 downto 0)   |             |
## Signals

| Name                    | Type      | Description |
| ----------------------- | --------- | ----------- |
| notify_bus_process_done | std_logic |             |
## Constants

| Name               | Type       | Value                           | Description |
| ------------------ | ---------- | ------------------------------- | ----------- |
| notify_request_msg | msg_type_t |  new_msg_type("notify request") |             |
| message_queue      | queue_t    |  new_queue                      |             |
## Processes
- main: (  )
- bus_process: (  )
