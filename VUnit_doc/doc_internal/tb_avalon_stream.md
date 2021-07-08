# Entity: tb_avalon_stream

## Diagram

![Diagram](tb_avalon_stream.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
Author Slawomir Siluk slaweksiluk@gazeta.pl
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name  | Type                                                           | Description |
| ----- | -------------------------------------------------------------- | ----------- |
| clk   | std_logic                                                      |             |
| valid | std_logic                                                      |             |
| ready | std_logic                                                      |             |
| sop   | std_logic                                                      |             |
| eop   | std_logic                                                      |             |
| data  | std_logic_vector(data_length(avalon_source_stream)-1 downto 0) |             |
## Constants

| Name                 | Type            | Value                                                                                                       | Description |
| -------------------- | --------------- | ----------------------------------------------------------------------------------------------------------- | ----------- |
| avalon_source_stream | avalon_source_t |      new_avalon_source(data_length => 8,<br><span style="padding-left:20px"> valid_high_probability => 0.1) |             |
| master_stream        | stream_master_t |  as_stream(avalon_source_stream)                                                                            |             |
| avalon_sink_stream   | avalon_sink_t   |      new_avalon_sink(data_length => 8,<br><span style="padding-left:20px"> ready_high_probability => 0.3)   |             |
| slave_stream         | stream_slave_t  |  as_stream(avalon_sink_stream)                                                                              |             |
## Processes
- main: (  )
## Instantiations

- avalon_source_vc: work.avalon_source
- avalon_sink_vc: work.avalon_sink
