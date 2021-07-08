# Entity: tb_axi_stream

## Diagram

![Diagram](tb_axi_stream.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name              | Type                   | Value | Description |
| ------------------------- | ---------------------- | ----- | ----------- |
| runner_cfg                | string                 |       |             |
| g_id_length               | natural                | 8     |             |
| g_dest_length             | natural                | 8     |             |
| g_user_length             | natural                | 8     |             |
| g_stall_percentage_master | natural range 0 to 100 | 0     |             |
| g_stall_percentage_slave  | natural range 0 to 100 | 0     |             |
## Signals

| Name             | Type                                                         | Description |
| ---------------- | ------------------------------------------------------------ | ----------- |
| aclk             | std_logic                                                    |             |
| areset_n         | std_logic                                                    |             |
| tvalid           | std_logic                                                    |             |
| tready           | std_logic                                                    |             |
| tdata            | std_logic_vector(data_length(slave_axi_stream)-1 downto 0)   |             |
| tlast            | std_logic                                                    |             |
| tkeep            | std_logic_vector(data_length(slave_axi_stream)/8-1 downto 0) |             |
| tstrb            | std_logic_vector(data_length(slave_axi_stream)/8-1 downto 0) |             |
| tid              | std_logic_vector(id_length(slave_axi_stream)-1 downto 0)     |             |
| tdest            | std_logic_vector(dest_length(slave_axi_stream)-1 downto 0)   |             |
| tuser            | std_logic_vector(user_length(slave_axi_stream)-1 downto 0)   |             |
| not_valid        | std_logic                                                    |             |
| not_valid_data   | std_logic                                                    |             |
| not_valid_keep   | std_logic                                                    |             |
| not_valid_strb   | std_logic                                                    |             |
| not_valid_id     | std_logic                                                    |             |
| not_valid_dest   | std_logic                                                    |             |
| not_valid_user   | std_logic                                                    |             |
| axis_stall_stats | axis_stall_stats_t                                           |             |
## Constants

| Name                | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| min_stall_cycles    | natural                       |  5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| max_stall_cycles    | natural                       |  15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| master_stall_config | stall_config_t                |  new_stall_config(stall_probability => real(g_stall_percentage_master)/100.0,<br><span style="padding-left:20px"> min_stall_cycles => min_stall_cycles,<br><span style="padding-left:20px"> max_stall_cycles => max_stall_cycles)                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
| slave_stall_config  | stall_config_t                |  new_stall_config(stall_probability => real(g_stall_percentage_slave)/100.0 ,<br><span style="padding-left:20px"> min_stall_cycles => min_stall_cycles,<br><span style="padding-left:20px"> max_stall_cycles => max_stall_cycles)                                                                                                                                                                                                                                                                                                                                                                                                                 |             |
| master_axi_stream   | axi_stream_master_t           |  new_axi_stream_master(     data_length => 8,<br><span style="padding-left:20px"> id_length => g_id_length,<br><span style="padding-left:20px"> dest_length => g_dest_length,<br><span style="padding-left:20px"> user_length => g_user_length,<br><span style="padding-left:20px">     stall_config => master_stall_config,<br><span style="padding-left:20px"> logger => get_logger("master"),<br><span style="padding-left:20px"> actor => new_actor("master"),<br><span style="padding-left:20px">     monitor => default_axi_stream_monitor,<br><span style="padding-left:20px"> protocol_checker => default_axi_stream_protocol_checker   ) |             |
| master_stream       | stream_master_t               |  as_stream(master_axi_stream)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
| master_sync         | sync_handle_t                 |  as_sync(master_axi_stream)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| slave_axi_stream    | axi_stream_slave_t            |  new_axi_stream_slave(     data_length => 8,<br><span style="padding-left:20px"> id_length => g_id_length,<br><span style="padding-left:20px"> dest_length => g_dest_length,<br><span style="padding-left:20px"> user_length => g_user_length,<br><span style="padding-left:20px">     stall_config => slave_stall_config,<br><span style="padding-left:20px"> logger => get_logger("slave"),<br><span style="padding-left:20px"> actor => new_actor("slave"),<br><span style="padding-left:20px">     monitor => default_axi_stream_monitor,<br><span style="padding-left:20px"> protocol_checker => default_axi_stream_protocol_checker   )     |             |
| slave_stream        | stream_slave_t                |  as_stream(slave_axi_stream)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| slave_sync          | sync_handle_t                 |  as_sync(slave_axi_stream)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| monitor             | axi_stream_monitor_t          |  new_axi_stream_monitor(     data_length => 8,<br><span style="padding-left:20px"> id_length => g_id_length,<br><span style="padding-left:20px"> dest_length => g_dest_length,<br><span style="padding-left:20px"> user_length => g_user_length,<br><span style="padding-left:20px">     logger => get_logger("monitor"),<br><span style="padding-left:20px"> actor => new_actor("monitor"),<br><span style="padding-left:20px">     protocol_checker => default_axi_stream_protocol_checker   )                                                                                                                                                  |             |
| protocol_checker    | axi_stream_protocol_checker_t |  new_axi_stream_protocol_checker(     data_length => 8,<br><span style="padding-left:20px"> id_length => g_id_length,<br><span style="padding-left:20px"> dest_length => g_dest_length,<br><span style="padding-left:20px"> user_length => g_user_length,<br><span style="padding-left:20px">     logger      => get_logger("protocol_checker"),<br><span style="padding-left:20px">     max_waits   => 8   )                                                                                                                                                                                                                                     |             |
| n_monitors          | natural                       |  3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
## Types

| Name                      | Type | Description                                          |
| ------------------------- | ---- | ---------------------------------------------------- |
| axis_stall_stats_fields_t |      | signals used for the statistics for stall evaluation |
| axis_stall_stats_t        |      |                                                      |
## Processes
- main: (  )
- statistics: ( aclk )
## Instantiations

- axi_stream_master_inst: work.axi_stream_master
- axi_stream_slave_inst: work.axi_stream_slave
- axi_stream_monitor_inst: work.axi_stream_monitor
- axi_stream_protocol_checker_inst: work.axi_stream_protocol_checker
