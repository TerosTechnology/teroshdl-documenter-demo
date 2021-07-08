# Entity: AxiMonAxiL

## Diagram

![Diagram](AxiMonAxiL.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite Wrapper on AXI4 Monitor Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type          | Value     | Description              |
| --------------- | ------------- | --------- | ------------------------ |
| TPD_G           | time          | 1 ns      |                          |
| COMMON_CLK_G    | boolean       | false     | true if axiClk = axilClk |
| AXI_CLK_FREQ_G  | real          | 156.25E+6 | units of Hz              |
| AXI_NUM_SLOTS_G | positive      | 1         |                          |
| AXI_CONFIG_G    | AxiConfigType |           |                          |
## Ports

| Port name        | Direction | Type                                            | Description                  |
| ---------------- | --------- | ----------------------------------------------- | ---------------------------- |
| axiClk           | in        | sl                                              | AXI4 Memory Interfaces       |
| axiRst           | in        | sl                                              |                              |
| axiWriteMasters  | in        | AxiWriteMasterArray(AXI_NUM_SLOTS_G-1 downto 0) |                              |
| axiWriteSlaves   | in        | AxiWriteSlaveArray(AXI_NUM_SLOTS_G-1 downto 0)  |                              |
| axiReadMasters   | in        | AxiReadMasterArray(AXI_NUM_SLOTS_G-1 downto 0)  |                              |
| axiReadSlaves    | in        | AxiReadSlaveArray(AXI_NUM_SLOTS_G-1 downto 0)   |                              |
| axilClk          | in        | sl                                              | AXI-Lite for register access |
| axilRst          | in        | sl                                              |                              |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType                          |                              |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType                           |                              |
| sAxilReadMaster  | in        | AxiLiteReadMasterType                           |                              |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType                            |                              |
## Signals

| Name        | Type                                               | Description |
| ----------- | -------------------------------------------------- | ----------- |
| axisMasters | AxiStreamMasterArray(2*AXI_NUM_SLOTS_G-1 downto 0) |             |
| axisSlaves  | AxiStreamSlaveArray(2*AXI_NUM_SLOTS_G-1 downto 0)  |             |
## Constants

| Name          | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AXIS_CONFIG_C | AxiStreamConfigType |  (       TSTRB_EN_C    => AXI_STREAM_CONFIG_INIT_C.TSTRB_EN_C,<br><span style="padding-left:20px">       TDATA_BYTES_C => AXI_CONFIG_G.DATA_BYTES_C,<br><span style="padding-left:20px">       TDEST_BITS_C  => AXI_STREAM_CONFIG_INIT_C.TDEST_BITS_C,<br><span style="padding-left:20px">       TID_BITS_C    => AXI_STREAM_CONFIG_INIT_C.TID_BITS_C,<br><span style="padding-left:20px">       TKEEP_MODE_C  => AXI_STREAM_CONFIG_INIT_C.TKEEP_MODE_C,<br><span style="padding-left:20px">       TUSER_BITS_C  => AXI_STREAM_CONFIG_INIT_C.TUSER_BITS_C,<br><span style="padding-left:20px">       TUSER_MODE_C  => AXI_STREAM_CONFIG_INIT_C.TUSER_MODE_C) |             |
## Instantiations

- U_Monitor: surf.AxiStreamMonAxiL
**Description**
Re-propose the existing AXI stream monitor as a AXI4 memory monitor

