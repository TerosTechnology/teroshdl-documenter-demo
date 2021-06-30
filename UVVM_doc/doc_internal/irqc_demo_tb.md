# Entity: irqc_demo_tb

## Diagram

![Diagram](irqc_demo_tb.svg "Diagram")
## Description

Copyright 2020 Bitvis
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 and in the provided LICENSE.TXT.
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
Note : Any functionality not explicitly described in the documentation is subject to change at any time
VHDL unit     : Bitvis IRQC Library : irqc_demo_tb
Description   : See dedicated powerpoint presentation and README-file(s)
Test case entity
## Signals

| Name        | Type                                                             | Description               |
| ----------- | ---------------------------------------------------------------- | ------------------------- |
| clk         | std_logic                                                        |                           |
| arst        | std_logic                                                        |                           |
| sbi_if      | t_sbi_if(addr(2 downto 0), wdata(7 downto 0), rdata(7 downto 0)) | CPU interface             |
| irq_source  | std_logic_vector(C_NUM_SOURCES-1 downto 0)                       | Interrupt related signals |
| irq2cpu     | std_logic                                                        |                           |
| irq2cpu_ack | std_logic                                                        |                           |
| clock_ena   | boolean                                                          |                           |
## Constants

| Name         | Type | Value  | Description |
| ------------ | ---- | ------ | ----------- |
| C_CLK_PERIOD | time |  10 ns |             |
## Functions
- trim <font id="function_arguments">( constant source   : std_logic_vector; constant num_bits : positive := C_NUM_SOURCES) </font> <font id="function_return">return t_irq_source </font>
**Description**
Trim (cut) a given vector to fit the number of irq sources (i.e. pot. reduce width)
- fit <font id="function_arguments">( constant source   : std_logic_vector; constant num_bits : positive := C_NUM_SOURCES) </font> <font id="function_return">return std_logic_vector </font>
**Description**
Fit a given vector to the number of irq sources by masking with zeros above irq width
## Processes
- p_main: (  )
**Description**
PROCESS: p_main

## Instantiations

- i_irqc: work.irqc
