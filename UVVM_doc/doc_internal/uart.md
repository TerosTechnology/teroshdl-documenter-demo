# Entity: uart

- **File**: uart.vhd
## Diagram

![Diagram](uart.svg "Diagram")
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

| Generic name                 | Type      | Value | Description |
| ---------------------------- | --------- | ----- | ----------- |
| GC_START_BIT                 | std_logic | '0'   |             |
| GC_STOP_BIT                  | std_logic | '1'   |             |
| GC_CLOCKS_PER_BIT            | integer   | 16    |             |
| GC_MIN_EQUAL_SAMPLES_PER_BIT | integer   | 15    |             |
## Ports

| Port name | Direction | Type                         | Description                               |
| --------- | --------- | ---------------------------- | ----------------------------------------- |
| clk       | in        | std_logic                    | DSP interface and general control signals |
| arst      | in        | std_logic                    |                                           |
| cs        | in        | std_logic                    | CPU interface                             |
| addr      | in        | unsigned(2 downto 0)         |                                           |
| wr        | in        | std_logic                    |                                           |
| rd        | in        | std_logic                    |                                           |
| wdata     | in        | std_logic_vector(7 downto 0) |                                           |
| rdata     | out       | std_logic_vector(7 downto 0) |                                           |
| rx_a      | in        | std_logic                    | UART related signals                      |
| tx        | out       | std_logic                    |                                           |
## Signals

| Name | Type  | Description |
| ---- | ----- | ----------- |
| p2c  | t_p2c |             |
| c2p  | t_c2p |             |
## Instantiations

- i_uart_pif: work.uart_pif
- i_uart_core: work.uart_core
