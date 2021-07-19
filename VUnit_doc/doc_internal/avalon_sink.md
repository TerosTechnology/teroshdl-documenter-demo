# Entity: avalon_sink

- **File**: avalon_sink.vhd
## Diagram

![Diagram](avalon_sink.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
Author Slawomir Siluk slaweksiluk@gazeta.pl
Avalon-St Sink Verification Component
TODO:
- timeout error
## Generics

| Generic name | Type          | Value | Description |
| ------------ | ------------- | ----- | ----------- |
| sink         | avalon_sink_t |       |             |
## Ports

| Port name | Direction | Type                                           | Description |
| --------- | --------- | ---------------------------------------------- | ----------- |
| clk       | in        | std_logic                                      |             |
| ready     | out       | std_logic                                      |             |
| valid     | in        | std_logic                                      |             |
| sop       | in        | std_logic                                      |             |
| eop       | in        | std_logic                                      |             |
| data      | in        | std_logic_vector(data_length(sink)-1 downto 0) |             |
## Processes
- main: (  )
