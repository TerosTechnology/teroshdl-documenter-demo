# Entity: uart_vvc_demo_tb
## Diagram
![Diagram](uart_vvc_demo_tb.svg "Diagram")
## Description
Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description   : See library quick reference (under 'doc') and README-file(s)
hdlunit:tb
Test bench entity
## Constants
| Name                  | Type                 | Value               | Description                   |
| --------------------- | -------------------- | ------------------- | ----------------------------- |
| C_SCOPE               | string               |  C_TB_SCOPE_DEFAULT |                               |
| C_CLK_PERIOD          | time                 |  10 ns              | Clock and bit period settings |
| C_BIT_PERIOD          | time                 |  16 * C_CLK_PERIOD  |                               |
| C_TIME_OF_ONE_UART_TX | time                 |  11*C_BIT_PERIOD    | =1760 ns;                     |
| C_ADDR_RX_DATA        | unsigned(2 downto 0) |  "000"              | Predefined SBI addresses      |
| C_ADDR_RX_DATA_VALID  | unsigned(2 downto 0) |  "001"              |                               |
| C_ADDR_TX_DATA        | unsigned(2 downto 0) |  "010"              |                               |
| C_ADDR_TX_READY       | unsigned(2 downto 0) |  "011"              |                               |
## Processes
- p_main: _(  )_
PROCESS: p_main

**Description**
PROCESS: p_main

## Instantiations
- i_test_harness: work.uart_vvc_demo_th
