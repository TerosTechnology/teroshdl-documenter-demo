# Entity: Ad9249Config

## Diagram

![Diagram](Ad9249Config.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AD9249 Configuration/Status Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name      | Type     | Value  | Description |
| ----------------- | -------- | ------ | ----------- |
| TPD_G             | time     | 1 ns   |             |
| NUM_CHIPS_G       | positive | 1      |             |
| SCLK_PERIOD_G     | real     | 1.0e-6 |             |
| AXIL_CLK_PERIOD_G | real     | 8.0e-9 |             |
## Ports

| Port name       | Direction | Type                          | Description |
| --------------- | --------- | ----------------------------- | ----------- |
| axilClk         | in        | sl                            |             |
| axilRst         | in        | sl                            |             |
| axilReadMaster  | in        | AxiLiteReadMasterType         |             |
| axilReadSlave   | out       | AxiLiteReadSlaveType          |             |
| axilWriteMaster | in        | AxiLiteWriteMasterType        |             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType         |             |
| adcPdwn         | out       | slv(NUM_CHIPS_G-1 downto 0)   |             |
| adcSclk         | out       | sl                            |             |
| adcSdio         | inout     | sl                            |             |
| adcCsb          | out       | slv(NUM_CHIPS_G*2-1 downto 0) |             |
## Signals

| Name       | Type                          | Description      |
| ---------- | ----------------------------- | ---------------- |
| rdData     | slv(23 downto 0)              |                  |
| rdEn       | sl                            |                  |
| coreSclk   | sl                            | Adc Core Chip IO |
| coreSDin   | sl                            |                  |
| coreSDout  | sl                            |                  |
| coreCsb    | slv(NUM_CHIPS_G*2-1 downto 0) |                  |
| sdioDir    | sl                            |                  |
| shiftCount | slv(bitSize(24)-1 downto 0)   |                  |
| r          | RegType                       |                  |
| rin        | RegType                       |                  |
## Constants

| Name             | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CHIP_SEL_WIDTH_C | integer                       |  log2(NUM_CHIPS_G*2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| PWDN_ADDR_BIT_C  | integer                       |  11 + CHIP_SEL_WIDTH_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |
| PWDN_ADDR_C      | slv(PWDN_ADDR_BIT_C downto 0) |  toSlv(2**PWDN_ADDR_BIT_C,<br><span style="padding-left:20px"> PWDN_ADDR_BIT_C+1)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| REG_INIT_C       | RegType                       |  (       state          => WAIT_AXI_TXN_S,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       chipSel        => (others => '0'),<br><span style="padding-left:20px">       wrData         => (others => '0'),<br><span style="padding-left:20px">       wrEn           => '0',<br><span style="padding-left:20px">       pdwn           => (others => '0')) |             |
## Types

| Name      | Type                                                                                                                         | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (WAIT_AXI_TXN_S,<br><span style="padding-left:20px"> WAIT_CYCLE_S,<br><span style="padding-left:20px"> WAIT_SPI_TXN_DONE_S)  |             |
| RegType   |                                                                                                                              | Registers   |
## Processes
- comb: ( axilRst, axilReadMaster, axilWriteMaster, r, rdData, rdEn )
- seq: ( axilClk )
## Instantiations

- SpiMaster_1: surf.SpiMaster
- SDIO_IOBUFT: IOBUF
