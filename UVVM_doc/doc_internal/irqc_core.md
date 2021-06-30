# Entity: irqc_core

## Diagram

![Diagram](irqc_core.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
VHDL unit     : Bitvis IRQC Library : irqc_core
Description   : See dedicated powerpoint presentation and README-file(s)
## Ports

| Port name   | Direction | Type                                       | Description                               |
| ----------- | --------- | ------------------------------------------ | ----------------------------------------- |
| clk         | in        | std_logic                                  | DSP interface and general control signals |
| arst        | in        | std_logic                                  |                                           |
| p2c         | in        | t_p2c                                      | PIF-core interface                        |
| c2p         | out       | t_c2p                                      |                                           |
| irq_source  | in        | std_logic_vector(C_NUM_SOURCES-1 downto 0) | Interrupt related signals                 |
| irq2cpu     | out       | std_logic                                  |                                           |
| irq2cpu_ack | in        | std_logic                                  |                                           |
## Signals

| Name  | Type      | Description                |
| ----- | --------- | -------------------------- |
| c2p_i | t_c2p     | Internal version of output |
| igr   | std_logic |                            |
## Functions
- or_reduce <font id="function_arguments">( constant value : std_logic_vector ) </font> <font id="function_return">return std_logic </font>
## Processes
- p_irr: ( clk, arst )
- p_irq2cpu: ( clk, arst )
