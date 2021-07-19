# Entity: AxiRam

- **File**: AxiRam.vhd
## Diagram

![Diagram](AxiRam.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: General AXI RAM Module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name   | Type                 | Value      | Description |
| -------------- | -------------------- | ---------- | ----------- |
| TPD_G          | time                 | 1 ns       |             |
| SYNTH_MODE_G   | string               | "inferred" |             |
| MEMORY_TYPE_G  | string               | "block"    |             |
| READ_LATENCY_G | natural range 0 to 2 | 2          |             |
| AXI_CONFIG_G   | AxiConfigType        |            |             |
## Ports

| Port name       | Direction | Type               | Description           |
| --------------- | --------- | ------------------ | --------------------- |
| axiClk          | in        | sl                 | Clock and Reset       |
| axiRst          | in        | sl                 |                       |
| sAxiWriteMaster | in        | AxiWriteMasterType | Slave Write Interface |
| sAxiWriteSlave  | out       | AxiWriteSlaveType  |                       |
| sAxiReadMaster  | in        | AxiReadMasterType  | Slave Read Interface  |
| sAxiReadSlave   | out       | AxiReadSlaveType   |                       |
## Signals

| Name   | Type                         | Description |
| ------ | ---------------------------- | ----------- |
| r      | RegType                      |             |
| rin    | RegType                      |             |
| wrEn   | sl                           |             |
| wrData | slv(DATA_WIDTH_C-1 downto 0) |             |
| wrAddr | slv(ADDR_WIDTH_C-1 downto 0) |             |
| wstrb  | slv(DATA_BYTES_C-1 downto 0) |             |
| rdEn   | slv(1 downto 0)              |             |
| rdData | slv(DATA_WIDTH_C-1 downto 0) |             |
| rdAddr | slv(ADDR_WIDTH_C-1 downto 0) |             |
## Constants

| Name         | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| DATA_BYTES_C | positive |  AXI_CONFIG_G.DATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| DATA_WIDTH_C | positive |  8*DATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
| OFFSET_C     | positive |  ite(DATA_BYTES_C = 1,<br><span style="padding-left:20px"> 0,<br><span style="padding-left:20px"> log2(DATA_BYTES_C))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |
| ADDR_WIDTH_C | positive |  AXI_CONFIG_G.ADDR_WIDTH_C-OFFSET_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C   | RegType  |  (       -- Write Signals       wrData         => (others => '0'),<br><span style="padding-left:20px">       wrAddr         => (others => '0'),<br><span style="padding-left:20px">       wstrb          => (others => '0'),<br><span style="padding-left:20px">       wid            => (others => '0'),<br><span style="padding-left:20px">       awlen          => (others => '0'),<br><span style="padding-left:20px">       sAxiWriteSlave => AXI_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       wrState        => WR_ADDR_S,<br><span style="padding-left:20px">       -- Read Signals       rdAddr         => (others => '0'),<br><span style="padding-left:20px">       rid            => (others => '0'),<br><span style="padding-left:20px">       arlen          => (others => '0'),<br><span style="padding-left:20px">       sAxiReadSlave  => AXI_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       rdEn           => (others => '0'),<br><span style="padding-left:20px">       rdLat          => (others => '0'),<br><span style="padding-left:20px">       rdState        => RD_ADDR_S) |             |
## Types

| Name        | Type                                                                                                            | Description |
| ----------- | --------------------------------------------------------------------------------------------------------------- | ----------- |
| WrStateType | ( WR_ADDR_S,<br><span style="padding-left:20px"> WR_DATA_S,<br><span style="padding-left:20px"> WR_BLOWOFF_S)   |             |
| RdStateType | ( RD_ADDR_S,<br><span style="padding-left:20px"> RD_PIPELINE_S,<br><span style="padding-left:20px"> RD_DATA_S)  |             |
| RegType     |                                                                                                                 |             |
## Processes
- comb: ( axiRst, r, rdData, sAxiReadMaster, sAxiWriteMaster )
- seq: ( axiClk )
