# Entity: avalon_mm_vvc

## Diagram

![Diagram](avalon_mm_vvc.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description   : See library quick reference (under 'doc') and README-file(s)
## Generics

| Generic name                             | Type                                         | Value                          | Description                                     |
| ---------------------------------------- | -------------------------------------------- | ------------------------------ | ----------------------------------------------- |
| GC_ADDR_WIDTH                            | integer range 1 to C_VVC_CMD_ADDR_MAX_LENGTH | 8                              | Avalon MM address bus                           |
| GC_DATA_WIDTH                            | integer range 1 to C_VVC_CMD_DATA_MAX_LENGTH | 32                             | Avalon MM data bus                              |
| GC_INSTANCE_IDX                          | natural                                      | 1                              | Instance index for this AVALON_MM_VVCT instance |
| GC_AVALON_MM_CONFIG                      | t_avalon_mm_bfm_config                       | C_AVALON_MM_BFM_CONFIG_DEFAULT | Behavior specification for BFM                  |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                                      | 1000                           |                                                 |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                                      | 950                            |                                                 |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                                | WARNING                        |                                                 |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                                      | 1000                           |                                                 |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                                      | 950                            |                                                 |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                                | WARNING                        |                                                 |
## Ports

| Port name               | Direction | Type           | Description |
| ----------------------- | --------- | -------------- | ----------- |
| clk                     | in        | std_logic      |             |
| avalon_mm_vvc_master_if | inout     | t_avalon_mm_if |             |
## Signals

| Name                               | Type                                                                                                                                                                                                                                                                                                                                    | Description                                                                                              |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| vvc_is_active                      | boolean                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| executor_is_busy                   | boolean                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| queue_is_increasing                | boolean                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| read_response_is_busy              | boolean                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| response_queue_is_increasing       | boolean                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| last_cmd_idx_executed              | natural                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| last_read_response_idx_executed    | natural                                                                                                                                                                                                                                                                                                                                 |                                                                                                          |
| terminate_current_cmd              | t_flag_record                                                                                                                                                                                                                                                                                                                           |                                                                                                          |
| entry_num_in_vvc_activity_register | integer                                                                                                                                                                                                                                                                                                                                 | VVC Activity                                                                                             |
| avalon_mm_vvc_master_if_pd         | t_avalon_mm_if(address(GC_ADDR_WIDTH-1 downto 0),                                                       byte_enable((GC_DATA_WIDTH/8)-1 downto 0),                                                       writedata(GC_DATA_WIDTH-1 downto 0),                                                       readdata(GC_DATA_WIDTH-1 downto 0)) | Propagation delayed interface signal used when reading data from the slave in the read_response process. |
## Constants

| Name         | Type         | Value                                                        | Description |
| ------------ | ------------ | ------------------------------------------------------------ | ----------- |
| C_SCOPE      | string       |  C_VVC_NAME & "," & to_string(GC_INSTANCE_IDX)               |             |
| C_VVC_LABELS | t_vvc_labels |  assign_vvc_labels(C_SCOPE, C_VVC_NAME, GC_INSTANCE_IDX, NA) |             |
## Functions
- get_msg_id_panel <font id="function_arguments">( constant command    : in t_vvc_cmd_record; constant vvc_config : in t_vvc_config ) </font> <font id="function_return">return t_msg_id_panel </font>
## Processes
- cmd_interpreter: (  )
**Description**
Command interpreter
- Interpret, decode and acknowledge commands from the central sequencer

- cmd_executor: (  )
**Description**
Command executor
- Fetch and execute the commands.
- Note that the read response is handled in the read_response process.

- read_response: (  )
**Description**
Read response command execution.
- READ (and CHECK) data received from the slave after the command executor has issued an
  read request (or check).
- Note the use of propagation delayed avalon_mm_vv_master_if signal

