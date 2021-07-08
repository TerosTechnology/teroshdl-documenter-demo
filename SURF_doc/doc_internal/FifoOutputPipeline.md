# Entity: FifoOutputPipeline

## Diagram

![Diagram](FifoOutputPipeline.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:   This module is used to sync a FWFT FIFO bus
               either as a pass through or with pipeline register stages.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                       | Value | Description                                 |
| -------------- | -------------------------- | ----- | ------------------------------------------- |
| TPD_G          | time                       | 1 ns  |                                             |
| RST_POLARITY_G | sl                         | '1'   | '1' for active high rst, '0' for active low |
| RST_ASYNC_G    | boolean                    | false |                                             |
| DATA_WIDTH_G   | integer range 1 to (2**24) | 16    |                                             |
| PIPE_STAGES_G  | natural range 0 to 16      | 1     |                                             |
## Ports

| Port name | Direction | Type                         | Description     |
| --------- | --------- | ---------------------------- | --------------- |
| sData     | in        | slv(DATA_WIDTH_G-1 downto 0) | Slave Port      |
| sValid    | in        | sl                           |                 |
| sRdEn     | out       | sl                           |                 |
| mData     | out       | slv(DATA_WIDTH_G-1 downto 0) | Master Port     |
| mValid    | out       | sl                           |                 |
| mRdEn     | in        | sl                           |                 |
| clk       | in        | sl                           | Clock and Reset |
| rst       | in        | sl                           |                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                         | Description |
| ------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PIPE_STAGES_C | natural |  PIPE_STAGES_G+1                                                                                                                                                              |             |
| REG_INIT_C    | RegType |  (       sRdEn  => '0',<br><span style="padding-left:20px">       mValid => (others => '0'),<br><span style="padding-left:20px">       mData  => (others => (others => '0'))) |             |
## Types

| Name      | Type                                                      | Description |
| --------- | --------------------------------------------------------- | ----------- |
| DataArray | array (natural range <>) of slv(DATA_WIDTH_G-1 downto 0)  |             |
| RegType   |                                                           |             |
