# Entity: tb_axi_dma

## Diagram

![Diagram](tb_axi_dma.svg "Diagram")
## Description

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at http://mozilla.org/MPL/2.0/.
Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name | Type   | Value | Description |
| ------------ | ------ | ----- | ----------- |
| runner_cfg   | string |       |             |
## Signals

| Name       | Type         | Description |
| ---------- | ------------ | ----------- |
| clk        | std_logic    |             |
| axil_m2s   | axil_m2s_t   |             |
| axil_s2m   | axil_s2m_t   |             |
| axi_rd_m2s | axi_rd_m2s_t |             |
| axi_rd_s2m | axi_rd_s2m_t |             |
| axi_wr_m2s | axi_wr_m2s_t |             |
| axi_wr_s2m | axi_wr_s2m_t |             |
## Constants

| Name             | Type         | Value                                                                                                                                                                                                                                                   | Description |
| ---------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| clk_period       | time         |  1 ns                                                                                                                                                                                                                                                   |             |
| axil_bus         | bus_master_t |  new_bus(data_length => 32,<br><span style="padding-left:20px">                                               address_length => 32,<br><span style="padding-left:20px">                                               logger => get_logger("axil_bus")) |             |
| memory           | memory_t     |  new_memory                                                                                                                                                                                                                                             |             |
| axi_rd_slave     | axi_slave_t  |  new_axi_slave(memory => memory,<br><span style="padding-left:20px">                                                        logger => get_logger("axi_rd_slave"))                                                                                       |             |
| axi_wr_slave     | axi_slave_t  |  new_axi_slave(memory => memory,<br><span style="padding-left:20px">                                                        logger => get_logger("axi_wr_slave"))                                                                                       |             |
| max_burst_length | natural      |  256                                                                                                                                                                                                                                                    |             |
| bytes_per_beat   | natural      |  axi_rd_s2m.r.data'length / 8                                                                                                                                                                                                                           |             |
## Functions
## Processes
- main: (  )
## Instantiations

- dut: work.axi_dma
- axi_lite_master_inst: vunit_lib.axi_lite_master
- axi_read_slave_inst: vunit_lib.axi_read_slave
- axi_write_slave_inst: vunit_lib.axi_write_slave
