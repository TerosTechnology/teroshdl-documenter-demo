# Entity: irqc

## Diagram

![Diagram](irqc.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
VHDL unit     : Bitvis IRQC Library : irqc
Description   : See dedicated powerpoint presentation and README-file(s)
## Ports

| Port name   | Direction | Type                                       | Description                               |
| ----------- | --------- | ------------------------------------------ | ----------------------------------------- |
| clk         | in        | std_logic                                  | DSP interface and general control signals |
| arst        | in        | std_logic                                  |                                           |
| cs          | in        | std_logic                                  | CPU interface                             |
| addr        | in        | unsigned(2 downto 0)                       |                                           |
| wr          | in        | std_logic                                  |                                           |
| rd          | in        | std_logic                                  |                                           |
| din         | in        | std_logic_vector(7 downto 0)               |                                           |
| dout        | out       | std_logic_vector(7 downto 0)               |                                           |
| irq_source  | in        | std_logic_vector(C_NUM_SOURCES-1 downto 0) | Interrupt related signals                 |
| irq2cpu     | out       | std_logic                                  |                                           |
| irq2cpu_ack | in        | std_logic                                  |                                           |
## Signals

| Name | Type  | Description |
| ---- | ----- | ----------- |
| p2c  | t_p2c |             |
| c2p  | t_c2p |             |
## Instantiations

- i_irqc_pif: work.irqc_pif
- i_irqc_core: work.irqc_core
