# Entity: SsiPrbsRateGen

- **File**: SsiPrbsRateGen.vhd
## Diagram

![Diagram](SsiPrbsRateGen.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SsiPrbsTx + AxiStreamMon Wrapper
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

| Generic name       | Type                       | Value     | Description                  |
| ------------------ | -------------------------- | --------- | ---------------------------- |
| TPD_G              | time                       | 1 ns      | General Configurations       |
| VALID_THOLD_G      | integer range 0 to (2**24) | 1         | PRBS TX FIFO Configurations  |
| VALID_BURST_MODE_G | boolean                    | false     |                              |
| MEMORY_TYPE_G      | string                     | "block"   |                              |
| CASCADE_SIZE_G     | natural range 1 to (2**24) | 1         |                              |
| FIFO_ADDR_WIDTH_G  | natural range 4 to 48      | 9         |                              |
| AXIS_CLK_FREQ_G    | real                       | 156.25E+6 |  units of Hz                 |
| AXIS_CONFIG_G      | AxiStreamConfigType        |           |                              |
## Ports

| Port name       | Direction | Type                   | Description            |
| --------------- | --------- | ---------------------- | ---------------------- |
| mAxisClk        | in        | sl                     | Master Port (mAxisClk) |
| mAxisRst        | in        | sl                     |                        |
| mAxisMaster     | out       | AxiStreamMasterType    |                        |
| mAxisSlave      | in        | AxiStreamSlaveType     |                        |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                        |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                        |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                        |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                        |
## Signals

| Name         | Type                | Description |
| ------------ | ------------------- | ----------- |
| r            | RegType             |             |
| rin          | RegType             |             |
| iAxisMaster  | AxiStreamMasterType |             |
| iAxisSlave   | AxiStreamSlaveType  |             |
| frameRate    | slv(31 downto 0)    |             |
| frameRateMax | slv(31 downto 0)    |             |
| frameRateMin | slv(31 downto 0)    |             |
| bandwidth    | slv(63 downto 0)    |             |
| bandwidthMax | slv(63 downto 0)    |             |
| bandwidthMin | slv(63 downto 0)    |             |
| busy         | sl                  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       trig           => '0',<br><span style="padding-left:20px">       packetLength   => (others=>'0'),<br><span style="padding-left:20px">       genPeriod      => (others=>'0'),<br><span style="padding-left:20px">       genEnable      => '0',<br><span style="padding-left:20px">       genOne         => '0',<br><span style="padding-left:20px">       genMissed      => (others=>'0'),<br><span style="padding-left:20px">       genCount       => (others=>'0'),<br><span style="padding-left:20px">       frameCount     => (others=>'0'),<br><span style="padding-left:20px">       statReset      => '1') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( axilReadMaster, axilWriteMaster, r, mAxisRst, busy,
                   frameRate, frameRateMax, frameRateMin,
                   bandwidth, bandwidthMax, bandwidthMin,
                   iAxisMaster, iAxisSlave )
- seq: ( mAxisClk )
## Instantiations

- U_PrbsTx: surf.SsiPrbsTx
- U_Monitor: surf.AxiStreamMon
