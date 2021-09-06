# Entity: error_injection_slv

- **File**: error_injection_slv.vhd
## Diagram

![Diagram](error_injection_slv.svg "Diagram")
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
 VHDL unit     : Bitvis VIP Error Injection Library : error_injection_pkg

 Description   : See library quick reference (under 'doc') and README-file(s).

## Generics

| Generic name    | Type    | Value | Description |
| --------------- | ------- | ----- | ----------- |
| GC_START_TIME   | time    | 0 ns  |             |
| GC_INSTANCE_IDX | natural | 1     |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| ei_in     | in        | std_logic_vector |             |
| ei_out    | out       | std_logic_vector |             |
## Processes
- p_error_injection: (  )
