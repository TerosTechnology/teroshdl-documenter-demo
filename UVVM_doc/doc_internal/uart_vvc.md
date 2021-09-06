# Entity: uart_vvc

- **File**: uart_vvc.vhd
## Diagram

![Diagram](uart_vvc.svg "Diagram")
## Description

================================================================================================================================
 Copyright 2020 Bitvis
 Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
 You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.

 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
 an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and limitations under the License.
================================================================================================================================
 Note : Any functionality not explicitly described in the documentation is subject to change at any time
--------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
 Description   : See library quick reference (under 'doc') and README-file(s)
----------------------------------------------------------------------------------------
=================================================================================================
## Generics

| Generic name                          | Type              | Value                     | Description |
| ------------------------------------- | ----------------- | ------------------------- | ----------- |
| GC_DATA_WIDTH                         | natural           | 8                         |             |
| GC_INSTANCE_IDX                       | natural           | 1                         |             |
| GC_UART_CONFIG                        | t_uart_bfm_config | C_UART_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                | natural           | 1000                      |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD          | natural           | 950                       |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level     | WARNING                   |             |
## Ports

| Port name   | Direction | Type      | Description |
| ----------- | --------- | --------- | ----------- |
| uart_vvc_rx | in        | std_logic |             |
| uart_vvc_tx | inout     | std_logic |             |
## Instantiations

- i1_uart_rx: work.uart_rx_vvc
- i1_uart_tx: work.uart_tx_vvc
</br>**Description**
 UART TX VVC

