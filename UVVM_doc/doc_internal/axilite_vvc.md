# Entity: axilite_vvc

## Diagram

![Diagram](axilite_vvc.svg "Diagram")
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

| Generic name                             | Type                                         | Value                        | Description                                   |
| ---------------------------------------- | -------------------------------------------- | ---------------------------- | --------------------------------------------- |
| GC_ADDR_WIDTH                            | integer range 1 to C_VVC_CMD_ADDR_MAX_LENGTH | 8                            |                                               |
| GC_DATA_WIDTH                            | integer range 1 to C_VVC_CMD_DATA_MAX_LENGTH | 32                           |                                               |
| GC_INSTANCE_IDX                          | natural                                      | 1                            | Instance index for this AXILITE_VVCT instance |
| GC_AXILITE_CONFIG                        | t_axilite_bfm_config                         | C_AXILITE_BFM_CONFIG_DEFAULT | Behavior specification for BFM                |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                                      | 1000                         |                                               |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                                      | 950                          |                                               |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                                | WARNING                      |                                               |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                                      | 1000                         |                                               |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                                      | 950                          |                                               |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                                | WARNING                      |                                               |
## Ports

| Port name             | Direction | Type         | Description |
| --------------------- | --------- | ------------ | ----------- |
| clk                   | in        | std_logic    |             |
| axilite_vvc_master_if | inout     | t_axilite_if |             |
## Signals

| Name                                       | Type          | Description  |
| ------------------------------------------ | ------------- | ------------ |
| executor_is_busy                           | boolean       |              |
| write_address_channel_executor_is_busy     | boolean       |              |
| write_data_channel_executor_is_busy        | boolean       |              |
| write_response_channel_executor_is_busy    | boolean       |              |
| read_address_channel_executor_is_busy      | boolean       |              |
| read_data_channel_executor_is_busy         | boolean       |              |
| any_executors_busy                         | boolean       |              |
| queue_is_increasing                        | boolean       |              |
| write_address_channel_queue_is_increasing  | boolean       |              |
| write_data_channel_queue_is_increasing     | boolean       |              |
| write_response_channel_queue_is_increasing | boolean       |              |
| read_address_channel_queue_is_increasing   | boolean       |              |
| read_data_channel_queue_is_increasing      | boolean       |              |
| last_cmd_idx_executed                      | natural       |              |
| last_write_response_channel_idx_executed   | natural       |              |
| last_read_data_channel_idx_executed        | natural       |              |
| terminate_current_cmd                      | t_flag_record |              |
| entry_num_in_vvc_activity_register         | integer       | VVC Activity |
## Constants

| Name         | Type         | Value                                                                                                                                                                    | Description |
| ------------ | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| C_SCOPE      | string       |  C_VVC_NAME & ",<br><span style="padding-left:20px">" & to_string(GC_INSTANCE_IDX)                                                                                       |             |
| C_VVC_LABELS | t_vvc_labels |  assign_vvc_labels(C_SCOPE,<br><span style="padding-left:20px"> C_VVC_NAME,<br><span style="padding-left:20px"> GC_INSTANCE_IDX,<br><span style="padding-left:20px"> NA) |             |
## Functions
- get_msg_id_panel <font id="function_arguments">( constant command    : in t_vvc_cmd_record;<br><span style="padding-left:20px"> constant vvc_config : in t_vvc_config ) </font> <font id="function_return">return t_msg_id_panel </font>
## Processes
- cmd_interpreter: (  )
**Description**
Command interpreter
- Interpret, decode and acknowledge commands from the central sequencer

- cmd_executor: (  )
**Description**
Command executor
- Fetch and execute the commands

- read_address_channel_executor: (  )
**Description**
Read address channel executor
- Fetch and execute the read address channel transactions

- read_data_channel_executor: (  )
**Description**
Read data channel executor
- Fetch and execute the read data channel transactions

- write_address_channel_executor: (  )
**Description**
write address channel executor
- Fetch and execute the write address channel transactions

- write_data_channel_executor: (  )
**Description**
write data channel executor
- Fetch and execute the write data channel transactions

- write_response_channel_executor: (  )
**Description**
write response channel executor
- Fetch and execute the write response channel transactions

