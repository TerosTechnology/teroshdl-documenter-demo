# Entity: tb_avalon_master

## Diagram

![Diagram](tb_avalon_master.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
Author Slawomir Siluk slaweksiluk@gazeta.pl
## Generics

| Generic name   | Type   | Value | Description |
| -------------- | ------ | ----- | ----------- |
| runner_cfg     | string |       |             |
| encoded_tb_cfg | string |       |             |
## Signals

| Name          | Type                                              | Description |
| ------------- | ------------------------------------------------- | ----------- |
| clk           | std_logic                                         |             |
| address       | std_logic_vector(tb_cfg.addr_width-1 downto 0)    |             |
| writedata     | std_logic_vector(tb_cfg.data_width-1 downto 0)    |             |
| readdata      | std_logic_vector(tb_cfg.data_width-1 downto 0)    |             |
| byteenable    | std_logic_vector(tb_cfg.data_width/8 -1 downto 0) |             |
| burstcount    | std_logic_vector(tb_cfg.burst_width -1 downto 0)  |             |
| write         | std_logic                                         |             |
| read          | std_logic                                         |             |
| readdatavalid | std_logic                                         |             |
| waitrequest   | std_logic                                         |             |
## Constants

| Name          | Type           | Value                                                                                                                                                                                                                                                                                                                | Description |
| ------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tb_cfg        | tb_cfg_t       |  decode(encoded_tb_cfg)                                                                                                                                                                                                                                                                                              |             |
| master_logger | logger_t       |  get_logger("master")                                                                                                                                                                                                                                                                                                |             |
| tb_logger     | logger_t       |  get_logger("tb")                                                                                                                                                                                                                                                                                                    |             |
| master_actor  | actor_t        |  new_actor("Avalon-MM Master")                                                                                                                                                                                                                                                                                       |             |
| bus_handle    | bus_master_t   |  new_bus(data_length => tb_cfg.data_width,<br><span style="padding-left:20px">       address_length => tb_cfg.addr_width,<br><span style="padding-left:20px"> logger => master_logger,<br><span style="padding-left:20px">       actor => master_actor)                                                              |             |
| memory        | memory_t       |  new_memory                                                                                                                                                                                                                                                                                                          |             |
| buf           | buffer_t       |  allocate(memory,<br><span style="padding-left:20px"> tb_cfg.transfers * byteenable'length)                                                                                                                                                                                                                          |             |
| avalon_slave  | avalon_slave_t |  new_avalon_slave(     memory => memory,<br><span style="padding-left:20px">     readdatavalid_high_probability => tb_cfg.readdatavalid_prob,<br><span style="padding-left:20px">     waitrequest_high_probability => tb_cfg.waitrequest_prob,<br><span style="padding-left:20px">     name => "Avalon-MM Slave"   ) |             |
## Types

| Name     | Type | Description |
| -------- | ---- | ----------- |
| tb_cfg_t |      |             |
## Functions
- gen_rndburst <font id="function_arguments">( variable rnd : inout RandomPType;<br><span style="padding-left:20px"> variable rndburst : inout positive;<br><span style="padding-left:20px"> variable transfers : inout natural ) </font> <font id="function_return">return ()</font>
## Processes
- main_stim: (  )
## Instantiations

- dut: work.avalon_master
- slave: work.avalon_slave
