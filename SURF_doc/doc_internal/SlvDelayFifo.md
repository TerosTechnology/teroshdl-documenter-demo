# Entity: SlvDelayFifo

- **File**: SlvDelayFifo.vhd
## Diagram

![Diagram](SlvDelayFifo.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : FIFO-Based Delay Block
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Delays a logic vector by writing entries into a FIFO, and
 reading them some number of cycles later. The delay is determined by the
 delay input.

 Note that the underlying FIFO has a minimum delay of 4 cycles, so a delay
 of less than 4 is not possible.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library".
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Generics

| Generic name       | Type     | Value   | Description |
| ------------------ | -------- | ------- | ----------- |
| TPD_G              | time     | 1 ns    |             |
| DATA_WIDTH_G       | positive | 1       |             |
| DELAY_BITS_G       | positive | 64      |             |
| FIFO_ADDR_WIDTH_G  | positive | 7       |             |
| FIFO_MEMORY_TYPE_G | string   | "block" |             |
## Ports

| Port name   | Direction | Type                         | Description             |
| ----------- | --------- | ---------------------------- | ----------------------- |
| clk         | in        | sl                           | Clock and Reset         |
| rst         | in        | sl                           |                         |
| delay       | in        | slv(DELAY_BITS_G-1 downto 0) | Configuration Interface |
| inputData   | in        | slv(DATA_WIDTH_G-1 downto 0) | Input Interface         |
| inputValid  | in        | sl                           |                         |
| inputAFull  | out       | sl                           |  FIFO almost full       |
| outputData  | out       | slv(DATA_WIDTH_G-1 downto 0) | Output Interface        |
| outputValid | out       | sl                           |                         |
## Signals

| Name            | Type                         | Description |
| --------------- | ---------------------------- | ----------- |
| r               | RegType                      |             |
| rin             | RegType                      |             |
| fifoReadoutTime | slv(DELAY_BITS_G-1 downto 0) |             |
| fifoReadoutData | slv(DATA_WIDTH_G-1 downto 0) |             |
| fifoValid       | sl                           |             |
| fifoRdEn        | sl                           |             |
| fifoDin         | slv(FIFO_WIDTH_C-1 downto 0) |             |
| fifoDout        | slv(FIFO_WIDTH_C-1 downto 0) |             |
## Constants

| Name           | Type     | Value                                                                                                                                                                                                                                                                                                                    | Description             |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| FIFO_MIN_LAT_C | positive |  4                                                                                                                                                                                                                                                                                                                       |  FIFO's minimum latency |
| FIFO_WIDTH_C   | natural  |  DELAY_BITS_G + DATA_WIDTH_G                                                                                                                                                                                                                                                                                             |                         |
| REG_INIT_C     | RegType  |  (       timeNow     => (others => '0'),<br><span style="padding-left:20px">       readoutTime => (others => '0'),<br><span style="padding-left:20px">       fifoRdEn    => '0',<br><span style="padding-left:20px">       outputData  => (others => '0'),<br><span style="padding-left:20px">       outputValid => '0') |                         |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( delay, fifoReadoutData, fifoReadoutTime, fifoValid, r, rst )
- seq: ( clk )
## Instantiations

- U_DelayFifo: surf.Fifo
