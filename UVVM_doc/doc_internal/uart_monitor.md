# Entity: uart_monitor

- **File**: uart_monitor.vhd
## Diagram

![Diagram](uart_monitor.svg "Diagram")
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

| Generic name      | Type                  | Value | Description |
| ----------------- | --------------------- | ----- | ----------- |
| GC_INSTANCE_IDX   | natural               | 1     |             |
| GC_MONITOR_CONFIG | t_uart_monitor_config |       |             |
## Ports

| Port name   | Direction | Type      | Description |
| ----------- | --------- | --------- | ----------- |
| uart_dut_rx | in        | std_logic |             |
| uart_dut_tx | in        | std_logic |             |
## Signals

| Name | Type      | Description |
| ---- | --------- | ----------- |
| tx_i | std_logic |             |
| rx_i | std_logic |             |
## Functions
- monitor_uart_line <font id="function_arguments">( constant  operation           : in    t_operation;<br><span style="padding-left:20px"> constant  C_LOG_PREFIX        : in    string;<br><span style="padding-left:20px"> signal    transaction_trigger : inout std_logic;<br><span style="padding-left:20px"> variable  transaction_info    : inout t_base_transaction;<br><span style="padding-left:20px"> signal    uart_line           : in    std_logic;<br><span style="padding-left:20px"> variable  monitor_config      : in    t_uart_monitor_config ) </font> <font id="function_return">return ()</font>
