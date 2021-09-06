# Entity: axi_stream_master

- **File**: axi_stream_master.vhd
## Diagram

![Diagram](axi_stream_master.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name           | Type                | Value | Description |
| ---------------------- | ------------------- | ----- | ----------- |
| master                 | axi_stream_master_t |       |             |
| drive_invalid          | boolean             | true  |             |
| drive_invalid_val      | std_logic           | 'X'   |             |
| drive_invalid_val_user | std_logic           | '0'   |             |
## Ports

| Port name | Direction | Type                                               | Description |
| --------- | --------- | -------------------------------------------------- | ----------- |
| aclk      | in        | std_logic                                          |             |
| areset_n  | in        | std_logic                                          |             |
| tvalid    | out       | std_logic                                          |             |
| tready    | in        | std_logic                                          |             |
| tdata     | out       | std_logic_vector(data_length(master)-1 downto 0)   |             |
| tlast     | out       | std_logic                                          |             |
| tkeep     | out       | std_logic_vector(data_length(master)/8-1 downto 0) |             |
| tstrb     | out       | std_logic_vector(data_length(master)/8-1 downto 0) |             |
| tid       | out       | std_logic_vector(id_length(master)-1 downto 0)     |             |
| tdest     | out       | std_logic_vector(dest_length(master)-1 downto 0)   |             |
| tuser     | out       | std_logic_vector(user_length(master)-1 downto 0)   |             |
## Signals

| Name                    | Type      | Description |
| ----------------------- | --------- | ----------- |
| notify_bus_process_done | std_logic |             |
## Constants

| Name               | Type       | Value                           | Description |
| ------------------ | ---------- | ------------------------------- | ----------- |
| notify_request_msg | msg_type_t |  new_msg_type("notify request") |             |
| message_queue      | queue_t    |  new_queue                      |             |
## Functions
- drive_invalid_output <font id="function_arguments">(signal l_tdata : out std_logic_vector(data_length(master)-1 downto 0);<br><span style="padding-left:20px"> signal l_tkeep : out std_logic_vector(data_length(master)/8-1 downto 0);<br><span style="padding-left:20px"> signal l_tstrb : out std_logic_vector(data_length(master)/8-1 downto 0);<br><span style="padding-left:20px"> signal l_tid   : out std_logic_vector(id_length(master)-1 downto 0);<br><span style="padding-left:20px"> signal l_tdest : out std_logic_vector(dest_length(master)-1 downto 0);<br><span style="padding-left:20px"> signal l_tuser : out std_logic_vector(user_length(master)-1 downto 0)) </font> <font id="function_return">return ()</font>
## Processes
- main: (  )
- bus_process: (  )
