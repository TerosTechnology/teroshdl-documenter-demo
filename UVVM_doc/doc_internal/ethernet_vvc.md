# Entity: ethernet_vvc

## Diagram

![Diagram](ethernet_vvc.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description : See library quick reference (under 'doc') and README-file(s)
## Generics

| Generic name                             | Type                                  | Value                                         | Description |
| ---------------------------------------- | ------------------------------------- | --------------------------------------------- | ----------- |
| GC_INSTANCE_IDX                          | natural                               |                                               |             |
| GC_PHY_INTERFACE                         | t_interface                           |                                               |             |
| GC_PHY_VVC_INSTANCE_IDX                  | natural                               |                                               |             |
| GC_PHY_MAX_ACCESS_TIME                   | time                                  | 1 us                                          |             |
| GC_DUT_IF_FIELD_CONFIG                   | t_dut_if_field_config_direction_array | C_DUT_IF_FIELD_CONFIG_DIRECTION_ARRAY_DEFAULT |             |
| GC_ETHERNET_PROTOCOL_CONFIG              | t_ethernet_protocol_config            | C_ETHERNET_PROTOCOL_CONFIG_DEFAULT            |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                               | 1000                                          |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                               | 950                                           |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                         | WARNING                                       |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                               | 1000                                          |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                               | 950                                           |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                         | WARNING                                       |             |
## Instantiations

- i_ethernet_tx: work.ethernet_tx_vvc
- i_ethernet_rx: work.ethernet_rx_vvc
**Description**
ETHERNET RX VVC

