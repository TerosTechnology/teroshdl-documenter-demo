# Entity: AxiStreamSelector

- **File**: AxiStreamSelector.vhd
## Diagram

![Diagram](AxiStreamSelector.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : JTAG Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Select between two input streams under control of a binary signal
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name | Direction | Type                             | Description |
| --------- | --------- | -------------------------------- | ----------- |
| clk       | in        | sl                               |             |
| rst       | in        | sl                               |             |
| sel       | in        | sl                               |             |
| mIb       | in        | AxiStreamMasterArray(1 downto 0) |             |
| sIb       | out       | AxiStreamSlaveArray (1 downto 0) |             |
| mOb       | out       | AxiStreamMasterType              |             |
| sOb       | in        | AxiStreamSlaveType               |             |
## Signals

| Name   | Type    | Description |
| ------ | ------- | ----------- |
| r      | RegType |             |
| rin    | RegType |             |
| rdyLoc | sl      |             |
## Constants

| Name       | Type    | Value                                               | Description |
| ---------- | ------- | --------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       streamBuf => AXI_STREAM_MASTER_INIT_C    ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- P_COMB: ( r, rdyLoc, sel, mIb, sOb )
- P_SEQ: ( clk )
