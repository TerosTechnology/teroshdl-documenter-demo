# Entity: Lmk048Base

- **File**: Lmk048Base.vhd
## Diagram

![Diagram](Lmk048Base.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Wrapper for Lmk048Base to handle 3-wire SPI and address mapping
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

| Generic name      | Type | Value    | Description       |
| ----------------- | ---- | -------- | ----------------- |
| TPD_G             | time | 1 ns     |                   |
| CLK_PERIOD_G      | real | 6.4E-9   |  units of seconds |
| SPI_SCLK_PERIOD_G | real | 100.0E-6 |                   |
## Ports

| Port name       | Direction | Type                   | Description        |
| --------------- | --------- | ---------------------- | ------------------ |
| lmkCsL          | out       | sl                     | 3-Wire SPI Ports   |
| lmkSck          | out       | sl                     |                    |
| lmkSdio         | inout     | sl                     |                    |
| axilClk         | in        | sl                     | AXI-Lite Interface |
| axilRst         | in        | sl                     |                    |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                    |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                    |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                    |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                    |
## Signals

| Name        | Type                   | Description |
| ----------- | ---------------------- | ----------- |
| writeMaster | AxiLiteWriteMasterType |             |
| readMaster  | AxiLiteReadMasterType  |             |
| lmkSDin     | sl                     |             |
| lmkSDout    | sl                     |             |
## Processes
- unnamed: ( axilReadMaster, axilWriteMaster )
## Instantiations

- U_LMK: surf.AxiSpiMaster
- U_lmkSdio: IOBUF
