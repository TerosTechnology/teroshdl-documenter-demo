# Entity: tb_axi_stream_protocol_checker

## Diagram

![Diagram](tb_axi_stream_protocol_checker.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| runner_cfg   | string  |       |             |
| data_length  | natural | 8     |             |
| id_length    | natural | 4     |             |
| dest_length  | natural | 4     |             |
| user_length  | natural | 8     |             |
| max_waits    | natural | 16    |             |
## Signals

| Name     | Type                                         | Description |
| -------- | -------------------------------------------- | ----------- |
| aclk     | std_logic                                    |             |
| areset_n | std_logic                                    |             |
| tvalid   | std_logic                                    |             |
| tready   | std_logic                                    |             |
| tdata    | std_logic_vector(data_length - 1 downto 0)   |             |
| tlast    | std_logic                                    |             |
| tdest    | std_logic_vector(dest_length - 1 downto 0)   |             |
| tid      | std_logic_vector(id_length - 1 downto 0)     |             |
| tstrb    | std_logic_vector(data_length/8 - 1 downto 0) |             |
| tkeep    | std_logic_vector(data_length/8 - 1 downto 0) |             |
| tuser    | std_logic_vector(user_length - 1 downto 0)   |             |
## Constants

| Name             | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| logger           | logger_t                      |  get_logger("protocol_checker")                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| protocol_checker | axi_stream_protocol_checker_t |  new_axi_stream_protocol_checker(     data_length => tdata'length,<br><span style="padding-left:20px"> id_length => tid'length,<br><span style="padding-left:20px"> dest_length => tdest'length,<br><span style="padding-left:20px"> user_length => tuser'length,<br><span style="padding-left:20px">     logger => logger,<br><span style="padding-left:20px"> actor => new_actor("protocol_checker"),<br><span style="padding-left:20px"> max_waits => max_waits   ) |             |
| meta_values      | std_logic_vector(1 to 5)      |  "-XWZU"                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| valid_values     | std_logic_vector(1 to 4)      |  "01LH"                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
## Processes
- main: (  )
## Instantiations

- axi_stream_protocol_checker_inst: work.axi_stream_protocol_checker
