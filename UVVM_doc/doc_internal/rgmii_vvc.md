# Entity: rgmii_vvc

- **File**: rgmii_vvc.vhd
## Diagram

![Diagram](rgmii_vvc.svg "Diagram")
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

| Generic name                             | Type               | Value                      | Description |
| ---------------------------------------- | ------------------ | -------------------------- | ----------- |
| GC_INSTANCE_IDX                          | natural            |                            |             |
| GC_RGMII_BFM_CONFIG                      | t_rgmii_bfm_config | C_RGMII_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural            | 1000                       |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural            | 950                        |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level      | WARNING                    |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural            | 1000                       |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural            | 950                        |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level      | WARNING                    |             |
## Ports

| Port name       | Direction | Type          | Description |
| --------------- | --------- | ------------- | ----------- |
| rgmii_vvc_tx_if | inout     | t_rgmii_tx_if |             |
| rgmii_vvc_rx_if | inout     | t_rgmii_rx_if |             |
## Instantiations

- i_rgmii_tx: work.rgmii_tx_vvc
- i_rgmii_rx: work.rgmii_rx_vvc
**Description**
RGMII RX VVC

