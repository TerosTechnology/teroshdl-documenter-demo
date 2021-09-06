# Entity: ei_demo_tb

- **File**: ei_demo_tb.vhd
## Diagram

![Diagram](ei_demo_tb.svg "Diagram")
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
hdlunit:tb
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| GC_TESTCASE  | natural | 0     |             |
## Signals

| Name       | Type                                      | Description                                            |
| ---------- | ----------------------------------------- | ------------------------------------------------------ |
| output_sl  | std_logic                                 |  Error Injection VIPs input/output signals  std_logic  |
| input_sl   | std_logic                                 |                                                        |
| input_slv  | std_logic_vector(C_DATA_WIDTH-1 downto 0) |  vector                                                |
| output_slv | std_logic_vector(C_DATA_WIDTH-1 downto 0) |                                                        |
## Constants

| Name                 | Type                                      | Value            | Description |
| -------------------- | ----------------------------------------- | ---------------- | ----------- |
| C_SCOPE              | string                                    |  "EI_DEMO_TB"    |             |
| C_SL_EI_IDX          | natural                                   |  1               |             |
| C_SLV_EI_IDX         | natural                                   |  2               |             |
| C_DATA_WIDTH         | natural                                   |  8               |             |
| C_SL_SIGNAL_DEFAULT  | std_logic                                 |  '0'             |             |
| C_SLV_SIGNAL_DEFAULT | std_logic_vector(C_DATA_WIDTH-1 downto 0) |  (others => '0') |             |
| C_PULSE_WIDTH        | time                                      |  20 ns           |             |
## Processes
- p_sequencer: (  )
</br>**Description**
---------------------------------------------------------------------------  Testbench sequencer --------------------------------------------------------------------------- 
## Instantiations

- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- error_injector_sl: work.error_injection_sl
</br>**Description**
---------------------------------------------------------------------------
 Error injector
---------------------------------------------------------------------------

- error_injector_slv: work.error_injection_slv
