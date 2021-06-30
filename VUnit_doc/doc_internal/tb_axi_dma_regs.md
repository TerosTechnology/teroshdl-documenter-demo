# Entity: tb_axi_dma_regs

## Diagram

![Diagram](tb_axi_dma_regs.svg "Diagram")
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

| Name           | Type                          | Description |
| -------------- | ----------------------------- | ----------- |
| clk            | std_logic                     |             |
| axil_m2s       | axil_m2s_t                    |             |
| axil_s2m       | axil_s2m_t                    |             |
| start_transfer | std_logic                     |             |
| transfer_done  | std_logic                     |             |
| src_address    | std_logic_vector(31 downto 0) |             |
| dst_address    | std_logic_vector(31 downto 0) |             |
| num_bytes      | std_logic_vector(31 downto 0) |             |
## Constants

| Name                   | Type             | Value                                                                    | Description |
| ---------------------- | ---------------- | ------------------------------------------------------------------------ | ----------- |
| axil_bus               | bus_master_t     |  new_bus(data_length => 32, address_length => 32)                        |             |
| clk_period             | time             |  1 ns                                                                    |             |
| src_address_checker    | signal_checker_t |  new_signal_checker(     logger => get_logger("src_address_checker"))    |             |
| dst_address_checker    | signal_checker_t |  new_signal_checker(     logger => get_logger("dst_address_checker"))    |             |
| num_bytes_checker      | signal_checker_t |  new_signal_checker(     logger => get_logger("num_bytes_checker"))      |             |
| start_transfer_checker | signal_checker_t |  new_signal_checker(     logger => get_logger("start_transfer_checker")) |             |
## Processes
- main: (  )
## Instantiations

- dut: work.axi_dma_regs
- axi_lite_master_inst: vunit_lib.axi_lite_master
- src_address_checker_inst: vunit_lib.std_logic_checker
- dst_address_checker_inst: vunit_lib.std_logic_checker
- num_bytes_checker_inst: vunit_lib.std_logic_checker
- start_transfer_checker_inst: vunit_lib.std_logic_checker
