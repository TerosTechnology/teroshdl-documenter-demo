# Entity: SynchronizerFifo

- **File**: SynchronizerFifo.vhd
## Diagram

![Diagram](SynchronizerFifo.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Synchronizing FIFO wrapper
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name  | Type                       | Value         | Description                                                 |
| ------------- | -------------------------- | ------------- | ----------------------------------------------------------- |
| TPD_G         | time                       | 1 ns          |                                                             |
| COMMON_CLK_G  | boolean                    | false         |  Bypass FifoAsync module for synchronous data configuration |
| MEMORY_TYPE_G | string                     | "distributed" |                                                             |
| SYNC_STAGES_G | integer range 3 to (2**24) | 3             |                                                             |
| PIPE_STAGES_G | natural range 0 to 16      | 0             |                                                             |
| DATA_WIDTH_G  | integer range 1 to (2**24) | 16            |                                                             |
| ADDR_WIDTH_G  | integer range 2 to 48      | 4             |                                                             |
| INIT_G        | slv                        | "0"           |                                                             |
## Ports

| Port name | Direction | Type                         | Description                 |
| --------- | --------- | ---------------------------- | --------------------------- |
| rst       | in        | sl                           | Asynchronous Reset          |
| wr_clk    | in        | sl                           | Write Ports (wr_clk domain) |
| wr_en     | in        | sl                           |                             |
| din       | in        | slv(DATA_WIDTH_G-1 downto 0) |                             |
| rd_clk    | in        | sl                           | Read Ports (rd_clk domain)  |
| rd_en     | in        | sl                           |                             |
| valid     | out       | sl                           |                             |
| dout      | out       | slv(DATA_WIDTH_G-1 downto 0) |                             |
## Constants

| Name   | Type                         | Value                                                                                                                     | Description |
| ------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| INIT_C | slv(DATA_WIDTH_G-1 downto 0) |  ite(INIT_G = "0",<br><span style="padding-left:20px"> slvZero(DATA_WIDTH_G),<br><span style="padding-left:20px"> INIT_G) |             |
