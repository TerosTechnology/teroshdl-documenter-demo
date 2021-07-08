# Entity: StreamPatternTester

## Diagram

![Diagram](StreamPatternTester.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:   Test which compares the data stream to selected pattern
               Designed for the automated delay alignment of the fast LVDS lines
               of ADCs with single or multiple serial data lanes
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                   | Value | Description |
| -------------- | ---------------------- | ----- | ----------- |
| TPD_G          | time                   | 1 ns  |             |
| NUM_CHANNELS_G | integer range 1 to 128 | 8     |             |
## Ports

| Port name       | Direction | Type                                            | Description            |
| --------------- | --------- | ----------------------------------------------- | ---------------------- |
| clk             | in        | std_logic                                       | Master system clock    |
| rst             | in        | std_logic                                       |                        |
| adcStreams      | in        | AxiStreamMasterArray(NUM_CHANNELS_G-1 downto 0) | ADC data stream inputs |
| axilWriteMaster | in        | AxiLiteWriteMasterType                          | Axi Interface          |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                           |                        |
| axilReadMaster  | in        | AxiLiteReadMasterType                           |                        |
| axilReadSlave   | out       | AxiLiteReadSlaveType                            |                        |
## Signals

| Name         | Type                          | Description |
| ------------ | ----------------------------- | ----------- |
| axilR        | AxilRegType                   |             |
| axilRin      | AxilRegType                   |             |
| dataMux      | std_logic_vector(31 downto 0) |             |
| dataValidMux | std_logic                     |             |
| testCnt      | unsigned(31 downto 0)         |             |
| testDone     | std_logic                     |             |
| testPassed   | std_logic                     |             |
| testFailed   | std_logic                     |             |
| passCnt      | unsigned(31 downto 0)         |             |
| timeoutCnt   | unsigned(31 downto 0)         |             |
## Constants

| Name            | Type        | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| --------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| AXIL_REG_INIT_C | AxilRegType |  (       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       testChannel    => (others=>'0'),<br><span style="padding-left:20px">       testPattern    => (others=>'0'),<br><span style="padding-left:20px">       testDataMask   => (others=>'0'),<br><span style="padding-left:20px">       testSamples    => (others=>'0'),<br><span style="padding-left:20px">       testTimeout    => (others=>'0'),<br><span style="padding-left:20px">       testRequest    => '0'    ) |             |
## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| AxilRegType |      |             |
## Processes
- axilComb: ( axilR, axilReadMaster, rst, axilWriteMaster, testPassed, testFailed )
- axilSeq: ( clk )
- testProc: ( clk )
