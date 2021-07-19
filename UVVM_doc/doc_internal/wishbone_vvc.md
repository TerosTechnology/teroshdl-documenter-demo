# Entity: wishbone_vvc

- **File**: wishbone_vvc.vhd
## Diagram

![Diagram](wishbone_vvc.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
This VVC was generated with Bitvis VVC Generator
## Generics

| Generic name                             | Type                  | Value                         | Description                                    |
| ---------------------------------------- | --------------------- | ----------------------------- | ---------------------------------------------- |
| GC_ADDR_WIDTH                            | integer               | 8                             |                                                |
| GC_DATA_WIDTH                            | integer               | 32                            |                                                |
| GC_INSTANCE_IDX                          | natural               | 1                             | Instance index for this WISHBONE_VVCT instance |
| GC_WISHBONE_BFM_CONFIG                   | t_wishbone_bfm_config | C_WISHBONE_BFM_CONFIG_DEFAULT | Behavior specification for BFM                 |
| GC_CMD_QUEUE_COUNT_MAX                   | natural               | 1000                          |                                                |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural               | 950                           |                                                |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level         | WARNING                       |                                                |
| GC_RESULT_QUEUE_COUNT_MAX                | natural               | 1000                          |                                                |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural               | 950                           |                                                |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level         | WARNING                       |                                                |
## Ports

| Port name              | Direction | Type          | Description          |
| ---------------------- | --------- | ------------- | -------------------- |
| clk                    | in        | std_logic     | VVC control signals: |
| wishbone_vvc_master_if | inout     | t_wishbone_if |                      |
## Signals

| Name                               | Type          | Description   |
| ---------------------------------- | ------------- | ------------- |
| executor_is_busy                   | boolean       |               |
| queue_is_increasing                | boolean       |               |
| last_cmd_idx_executed              | natural       |               |
| terminate_current_cmd              | t_flag_record |               |
| entry_num_in_vvc_activity_register | integer       | VVC Activity  |
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

