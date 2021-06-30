# Entity: sb_uart_sbi_demo_tb

## Diagram

![Diagram](sb_uart_sbi_demo_tb.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description   : See library quick reference (under 'doc') and README-file(s)
Test harness entity
## Signals

| Name           | Type                                                                                                                                                          | Description                               |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| clk            | std_logic                                                                                                                                                     | DSP interface and general control signals |
| clk_ena        | boolean                                                                                                                                                       |                                           |
| arst           | std_logic                                                                                                                                                     |                                           |
| sbi_if         | t_sbi_if(addr(C_ADDR_WIDTH-1 downto 0),                            wdata(C_DATA_WIDTH-1 downto 0),                            rdata(C_DATA_WIDTH-1 downto 0)) | SBI signals                               |
| terminate_loop | std_logic                                                                                                                                                     |                                           |
| uart_rx        | std_logic                                                                                                                                                     | UART signals                              |
| uart_tx        | std_logic                                                                                                                                                     |                                           |
## Constants

| Name         | Type    | Value  | Description |
| ------------ | ------- | ------ | ----------- |
| C_SCOPE      | string  |  "TB"  |             |
| C_ADDR_WIDTH | integer |  3     |             |
| C_DATA_WIDTH | integer |  8     |             |
| C_CLK_PERIOD | time    |  10 ns | 100 MHz     |
## Processes
- p_sequencer: (  )
**Description**
Sequencer

## Instantiations

- i_uart: bitvis_uart.uart
