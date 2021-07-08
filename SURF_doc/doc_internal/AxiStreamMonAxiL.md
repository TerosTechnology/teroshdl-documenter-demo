# Entity: AxiStreamMonAxiL

## Diagram

![Diagram](AxiStreamMonAxiL.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite Wrapper on AXI Stream Monitor Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name     | Type                | Value     | Description               |
| ---------------- | ------------------- | --------- | ------------------------- |
| TPD_G            | time                | 1 ns      |                           |
| COMMON_CLK_G     | boolean             | false     | true if axisClk = axilClk |
| AXIS_CLK_FREQ_G  | real                | 156.25E+6 | units of Hz               |
| AXIS_NUM_SLOTS_G | positive            | 1         |                           |
| AXIS_CONFIG_G    | AxiStreamConfigType |           |                           |
## Ports

| Port name        | Direction | Type                                              | Description                             |
| ---------------- | --------- | ------------------------------------------------- | --------------------------------------- |
| axisClk          | in        | sl                                                | AXIS Stream Interface                   |
| axisRst          | in        | sl                                                |                                         |
| axisMasters      | in        | AxiStreamMasterArray(AXIS_NUM_SLOTS_G-1 downto 0) |                                         |
| axisSlaves       | in        | AxiStreamSlaveArray(AXIS_NUM_SLOTS_G-1 downto 0)  |                                         |
| axilClk          | in        | sl                                                | AXI lite slave port for register access |
| axilRst          | in        | sl                                                |                                         |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType                            |                                         |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType                             |                                         |
| sAxilReadMaster  | in        | AxiLiteReadMasterType                             |                                         |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType                              |                                         |
## Signals

| Name         | Type                                    | Description |
| ------------ | --------------------------------------- | ----------- |
| r            | RegType                                 |             |
| rin          | RegType                                 |             |
| rstCnt       | sl                                      |             |
| localReset   | sl                                      |             |
| axisReset    | sl                                      |             |
| frameCnt     | Slv64Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameSize    | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameSizeMax | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameSizeMin | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameRate    | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameRateMax | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| frameRateMin | Slv32Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| bandwidth    | Slv64Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| bandwidthMax | Slv64Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
| bandwidthMin | Slv64Array(AXIS_NUM_SLOTS_G-1 downto 0) |             |
## Constants

| Name         | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ADDR_WIDTH_C | positive |  bitSize(AXIS_NUM_SLOTS_G*16-1)                                                                                                                                                                                                                                                                                                                                                                                     |             |
| REG_INIT_C   | RegType  |  (       we   => '0',<br><span style="padding-left:20px">       data => (others => '0'),<br><span style="padding-left:20px">       cnt  => (others => '1'),<br><span style="padding-left:20px">  -- pre-set to all ones so 1st write after reset is address=0x0       addr => (others => '1'),<br><span style="padding-left:20px">  -- pre-set to all ones so 1st write after reset is address=0x0       ch   => 0) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axisRst, bandwidth, bandwidthMax, bandwidthMin, frameCnt,
                   frameRate, frameRateMax, frameRateMin, frameSize,
                   frameSizeMax, frameSizeMin, r )
- seq: ( axisClk )
## Instantiations

- U_RstSync: surf.RstSync
- U_AxiDualPortRam: surf.AxiDualPortRam
