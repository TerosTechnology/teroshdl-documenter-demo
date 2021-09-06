# Entity: axi_dma

- **File**: axi_dma.vhd
## Diagram

![Diagram](axi_dma.svg "Diagram")
## Description

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this file,
 You can obtain one at http://mozilla.org/MPL/2.0/.

 Copyright (c) 2014-2021, Lars Asplund lars.anders.asplund@gmail.com
## Generics

| Generic name     | Type                   | Value | Description |
| ---------------- | ---------------------- | ----- | ----------- |
| max_burst_length | natural range 0 to 256 |       |             |
## Ports

| Port name  | Direction | Type         | Description          |
| ---------- | --------- | ------------ | -------------------- |
| clk        | in        | std_logic    |                      |
| axils_m2s  | in        | axil_m2s_t   | Control register bus |
| axils_s2m  | out       | axil_s2m_t   |                      |
| axi_rd_m2s | out       | axi_rd_m2s_t | Read data bus        |
| axi_rd_s2m | in        | axi_rd_s2m_t |                      |
| axi_wr_m2s | out       | axi_wr_m2s_t | Write data bus       |
| axi_wr_s2m | in        | axi_wr_s2m_t |                      |
## Signals

| Name                        | Type                                   | Description |
| --------------------------- | -------------------------------------- | ----------- |
| start_transfer              | std_logic                              |             |
| transfer_done               | std_logic                              |             |
| src_address                 | std_logic_vector(31 downto 0)          |             |
| dst_address                 | std_logic_vector(31 downto 0)          |             |
| num_bytes                   | std_logic_vector(31 downto 0)          |             |
| last_beat_written           | boolean                                |             |
| num_beats_read              | natural range 0 to max_counter_value-1 |             |
| num_beats_written           | natural range 0 to max_counter_value-1 |             |
| outstanding_write_responses | natural                                |             |
## Constants

| Name                            | Type    | Value                                                | Description                                                                                                                                                                                                                               |
| ------------------------------- | ------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bytes_per_beat                  | natural |  axi_rd_s2m.r.data'length/8                          |                                                                                                                                                                                                                                           |
| c4kbyte                         | natural |  4096                                                |                                                                                                                                                                                                                                           |
| max_num_burst_buffered          | natural |  2                                                   |                                                                                                                                                                                                                                           |
| max_num_beats_buffered          | natural |  max_num_burst_buffered * max_burst_length           |                                                                                                                                                                                                                                           |
| max_counter_value               | natural |  2**clog2(max_num_beats_buffered + max_burst_length) |  The maximum difference between two counters can only be  max_num_beats_buffered + max_burst_length  Thus it is enough to compare counters MOD max_num_beats_buffered  We round up to nearest power of two to avoid non power of two MOD  |
| max_outstanding_write_responses | natural |  7                                                   |                                                                                                                                                                                                                                           |
## Instantiations

- axi_dma_regs_inst: work.axi_dma_regs
