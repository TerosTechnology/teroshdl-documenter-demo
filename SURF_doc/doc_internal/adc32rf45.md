# Entity: adc32rf45

- **File**: adc32rf45.vhd
## Diagram

![Diagram](adc32rf45.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SPI Master Wrapper that includes a state machine for SPI paging
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

| Generic name      | Type | Value           | Description |
| ----------------- | ---- | --------------- | ----------- |
| TPD_G             | time | 1 ns            |             |
| CLK_PERIOD_G      | real | (1.0/156.25E+6) |             |
| SPI_SCLK_PERIOD_G | real | (1.0/10.0E+6)   |             |
## Ports

| Port name      | Direction | Type                   | Description        |
| -------------- | --------- | ---------------------- | ------------------ |
| axiClk         | in        | sl                     | Clock and Reset    |
| axiRst         | in        | sl                     |                    |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                    |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                    |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                    |
| coreRst        | out       | sl                     | SPI Interface      |
| coreSclk       | out       | sl                     |                    |
| coreSDin       | in        | sl                     |                    |
| coreSDout      | out       | sl                     |                    |
| coreCsb        | out       | sl                     |                    |
## Signals

| Name   | Type             | Description |
| ------ | ---------------- | ----------- |
| r      | RegType          |             |
| rin    | RegType          |             |
| rdEn   | sl               |             |
| rdData | slv(23 downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description                        |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| DLY_C      | natural |  integer(1.0E-6/CLK_PERIOD_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  min. 1us delay between SPI cycles |
| REG_INIT_C | RegType |  (       rst           => '0',<br><span style="padding-left:20px">       axiRd         => '0',<br><span style="padding-left:20px">       wrEn          => '0',<br><span style="padding-left:20px">       wrData        => (others => '0'),<br><span style="padding-left:20px">       data          => (others => '0'),<br><span style="padding-left:20px">       addr          => (others => '0'),<br><span style="padding-left:20px">       xferType      => (others => '0'),<br><span style="padding-left:20px">       timer         => 0,<br><span style="padding-left:20px">       cnt           => 0,<br><span style="padding-left:20px">       size          => 0,<br><span style="padding-left:20px">       wrArray       => (others => (others => '0')),<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       state         => IDLE_S) |                                    |
## Types

| Name      | Type                                                                                                                                         | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> INIT_S,<br><span style="padding-left:20px"> REQ_S,<br><span style="padding-left:20px"> ACK_S)  |             |
| RegType   |                                                                                                                                              |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, r, rdData, rdEn )
- seq: ( axiClk )
## Instantiations

- U_SpiMaster: surf.SpiMaster
