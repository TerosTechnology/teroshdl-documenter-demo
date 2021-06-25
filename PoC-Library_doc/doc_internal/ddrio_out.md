# Entity: ddrio_out
## Diagram
![Diagram](ddrio_out.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Martin Zabel
Entity:					Chip-Specific DDR Output Registers
Description:
-------------------------------------
Instantiates chip-specific :abbr:`DDR (Double Data Rate)` output registers.
Both data ``DataOut_high/low`` as well as ``OutputEnable`` are sampled with
the ``rising_edge(Clock)`` from the on-chip logic. ``DataOut_high`` is brought
out with this rising edge. ``DataOut_low`` is brought out with the falling
edge.
``OutputEnable`` (Tri-State) is high-active. It is automatically inverted if
necessary. If an output enable is not required, you may save some logic by
setting ``NO_OUTPUT_ENABLE = true``.
If ``NO_OUTPUT_ENABLE = false`` then output is disabled after power-up.
If ``NO_OUTPUT_ENABLE = true`` then output after power-up equals ``INIT_VALUE``.
.. wavedrom::
   
![alt text](wavedrom_6a610.svg "title") 

``Pad`` must be connected to a PAD because FPGAs only have these registers in
IOBs.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany,
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
## Generics
| Generic name     | Type       | Value       | Description |
| ---------------- | ---------- | ----------- | ----------- |
| NO_OUTPUT_ENABLE | boolean    | false       |             |
| BITS             | positive   |             |             |
| INIT_VALUE       | bit_vector | x"FFFFFFFF" |             |
## Ports
| Port name    | Direction | Type                                | Description |
| ------------ | --------- | ----------------------------------- | ----------- |
| Clock        | in        | std_logic                           |             |
| ClockEnable  | in        | std_logic                           |             |
| OutputEnable | in        | std_logic                           |             |
| DataOut_high | in        | std_logic_vector(BITS - 1 downto 0) |             |
| DataOut_low  | in        | std_logic_vector(BITS - 1 downto 0) |             |
| Pad          | out       | std_logic_vector(BITS - 1 downto 0) |             |
