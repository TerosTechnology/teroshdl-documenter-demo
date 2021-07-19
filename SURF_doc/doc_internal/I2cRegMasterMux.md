# Entity: I2cRegMasterMux

- **File**: I2cRegMasterMux.vhd
## Diagram

![Diagram](I2cRegMasterMux.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Multiplexes access to a single I2cRegMaster module
Attached devices may also lock others out in order to execute multiple
transactions in a row. To do this, lockReq must be set high for the first
transaction and set low for the last transaction.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                 | Value | Description |
| ------------ | -------------------- | ----- | ----------- |
| TPD_G        | time                 | 1 ns  |             |
| NUM_INPUTS_C | natural range 2 to 8 | 2     |             |
## Ports

| Port name | Direction | Type                                      | Description |
| --------- | --------- | ----------------------------------------- | ----------- |
| clk       | in        | sl                                        |             |
| srst      | in        | sl                                        |             |
| arst      | in        | sl                                        |             |
| lockReq   | in        | slv(NUM_INPUTS_C-1 downto 0)              |             |
| regIn     | in        | I2cRegMasterInArray(0 to NUM_INPUTS_C-1)  |             |
| regOut    | out       | I2cRegMasterOutArray(0 to NUM_INPUTS_C-1) |             |
| masterIn  | out       | I2cRegMasterInType                        |             |
| masterOut | in        | I2cRegMasterOutType                       |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       locked   => '0',<br><span style="padding-left:20px">       sel      => (others => '0'),<br><span style="padding-left:20px">       regOut   => (others => I2C_REG_MASTER_OUT_INIT_C),<br><span style="padding-left:20px">       masterIn => I2C_REG_MASTER_IN_INIT_C) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( lockReq, masterOut, r, regIn, srst )
- seq: ( arst, clk )
