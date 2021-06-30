# Entity: uart_vvc_th

## Diagram

![Diagram](uart_vvc_th.svg "Diagram")
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

| Name        | Type                         | Description      |
| ----------- | ---------------------------- | ---------------- |
| clk         | std_logic                    |                  |
| arst        | std_logic                    |                  |
| cs          | std_logic                    | SBI VVC signals  |
| addr        | unsigned(2 downto 0)         |                  |
| wr          | std_logic                    |                  |
| rd          | std_logic                    |                  |
| wdata       | std_logic_vector(7 downto 0) |                  |
| rdata       | std_logic_vector(7 downto 0) |                  |
| ready       | std_logic                    |                  |
| uart_vvc_rx | std_logic                    | UART VVC signals |
| uart_vvc_tx | std_logic                    |                  |
## Constants

| Name         | Type | Value  | Description |
| ------------ | ---- | ------ | ----------- |
| C_CLK_PERIOD | time |  10 ns |             |
## Processes
- p_clk: (  )
**Description**
Clock process

## Instantiations

- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_uart: bitvis_uart.uart
**Description**
Instantiate DUT

- i1_sbi_vvc: bitvis_vip_sbi.sbi_vvc
**Description**
SBI VVC

- i1_uart_vvc: bitvis_vip_uart.uart_vvc
**Description**
UART VVC

