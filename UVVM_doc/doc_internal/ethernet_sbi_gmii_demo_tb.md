# Entity: ethernet_sbi_gmii_demo_tb

## Diagram

![Diagram](ethernet_sbi_gmii_demo_tb.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
Description : See library quick reference (under 'doc') and README-file(s)
Test case entity
## Constants

| Name                | Type                  | Value                 | Description |
| ------------------- | --------------------- | --------------------- | ----------- |
| C_CLK_PERIOD        | time                  |  8 ns                 |             |
| C_SCOPE             | string                |  C_TB_SCOPE_DEFAULT   |             |
| C_VVC_ETH_SBI       | natural               |  1                    |             |
| C_VVC_SBI           | natural               |  1                    |             |
| C_VVC_ETH_GMII      | natural               |  2                    |             |
| C_VVC_GMII          | natural               |  2                    |             |
| C_ETH_SBI_MAC_ADDR  | unsigned(47 downto 0) |  x"00_00_00_00_00_01" |             |
| C_ETH_GMII_MAC_ADDR | unsigned(47 downto 0) |  x"00_00_00_00_00_02" |             |
## Processes
- p_main: (  )
**Description**
PROCESS: p_main

## Instantiations

- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- i_test_harness: bitvis_vip_ethernet.ethernet_sbi_gmii_demo_th
**Description**
Instantiate test harness, containing DUT and VVCs

