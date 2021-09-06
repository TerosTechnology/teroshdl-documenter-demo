# Entity: avalon_source

- **File**: avalon_source.vhd
## Diagram

![Diagram](avalon_source.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
 Author Slawomir Siluk slaweksiluk@gazeta.pl
 Avalon-St Source Verification Component
## Generics

| Generic name | Type            | Value | Description |
| ------------ | --------------- | ----- | ----------- |
| source       | avalon_source_t |       |             |
## Ports

| Port name | Direction | Type                                             | Description |
| --------- | --------- | ------------------------------------------------ | ----------- |
| clk       | in        | std_logic                                        |             |
| ready     | in        | std_logic                                        |             |
| valid     | out       | std_logic                                        |             |
| sop       | out       | std_logic                                        |             |
| eop       | out       | std_logic                                        |             |
| data      | out       | std_logic_vector(data_length(source)-1 downto 0) |             |
## Processes
- main: (  )
