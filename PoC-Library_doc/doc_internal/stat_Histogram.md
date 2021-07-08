# Entity: stat_Histogram

## Diagram

![Diagram](stat_Histogram.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Patrick Lehmann
Entity:					Creates a histogram of all input data
Description:
-------------------------------------
.. TODO:: No documentation available.
License:
=============================================================================
Copyright 2007-2016 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_BITS    | positive | 16    |             |
| COUNTER_BITS | positive | 16    |             |
## Ports

| Port name | Direction | Type                                                        | Description |
| --------- | --------- | ----------------------------------------------------------- | ----------- |
| Clock     | in        | std_logic                                                   |             |
| Reset     | in        | std_logic                                                   |             |
| Enable    | in        | std_logic                                                   |             |
| DataIn    | in        | std_logic_vector(DATA_BITS - 1 downto 0)                    |             |
| Histogram | out       | T_SLM(2**DATA_BITS - 1 downto 0, COUNTER_BITS - 1 downto 0) |             |
## Signals

| Name            | Type                                          | Description |
| --------------- | --------------------------------------------- | ----------- |
| HistogramMemory | T_HISTOGRAM_MEMORY(2**DATA_BITS - 1 downto 0) |             |
## Types

| Name               | Type                                                        | Description |
| ------------------ | ----------------------------------------------------------- | ----------- |
| T_HISTOGRAM_MEMORY | array(natural range <>) of unsigned(COUNTER_BITS downto 0)  |             |
## Functions
- to_slm <font id="function_arguments">(usv : T_HISTOGRAM_MEMORY) </font> <font id="function_return">return T_SLM </font>
**Description**
create matrix from vector-vector
## Processes
- unnamed: ( Clock )
