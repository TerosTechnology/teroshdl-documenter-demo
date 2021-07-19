# Entity: irqc_pif

- **File**: irqc_pif.vhd
## Diagram

![Diagram](irqc_pif.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
VHDL unit     : Bitvis IRQC Library : irqc_pif
Description   : See dedicated powerpoint presentation and README-file(s)
## Ports

| Port name | Direction | Type                         | Description   |
| --------- | --------- | ---------------------------- | ------------- |
| arst      | in        | std_logic                    |               |
| clk       | in        | std_logic                    |               |
| cs        | in        | std_logic                    | CPU interface |
| addr      | in        | unsigned                     |               |
| wr        | in        | std_logic                    |               |
| rd        | in        | std_logic                    |               |
| din       | in        | std_logic_vector(7 downto 0) |               |
| dout      | out       | std_logic_vector(7 downto 0) |               |
| p2c       | out       | t_p2c                        |               |
| c2p       | in        | t_c2p                        |               |
## Signals

| Name   | Type                         | Description                |
| ------ | ---------------------------- | -------------------------- |
| p2c_i  | t_p2c                        | internal version of output |
| dout_i | std_logic_vector(7 downto 0) |                            |
## Processes
- p_read_reg: ( cs, addr, rd, c2p, p2c_i )
- p_write_reg: ( clk, arst )
**Description**
Writing to registers that are not functionally manipulated

- p_aux: ( wr, addr, din )
**Description**
Writing to registers that are functionally manipulated and/or located outside PIF (or dummy registers)

