# Entity: ClinkDataShift

- **File**: ClinkDataShift.vhd
## Diagram

![Diagram](ClinkDataShift.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:
Block to de-serialize a block of 28 bits packed into 4 7-bit serial streams.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type   | Value        | Description |
| ------------ | ------ | ------------ | ----------- |
| TPD_G        | time   | 1 ns         |             |
| XIL_DEVICE_G | string | "ULTRASCALE" |             |
## Ports

| Port name       | Direction | Type                   | Description                               |
| --------------- | --------- | ---------------------- | ----------------------------------------- |
| cblHalfP        | inout     | slv(4 downto 0)        | Input clock and data                      |
| cblHalfM        | inout     | slv(4 downto 0)        |                                           |
| linkRst         | in        | sl                     | Async link reset                          |
| dlyClk          | in        | sl                     | Delay clock, 200Mhz                       |
| dlyRst          | in        | sl                     |                                           |
| clinkClk        | out       | sl                     | Parallel Clock and reset Output, 85Mhz    |
| clinkRst        | out       | sl                     |                                           |
| parData         | out       | slv(27 downto 0)       | Parallel clock and data output (clinkClk) |
| parClock        | out       | slv(6 downto 0)        |                                           |
| delay           | in        | slv(4 downto 0)        | Control inputs                            |
| delayLd         | in        | sl                     |                                           |
| bitSlip         | in        | sl                     |                                           |
| clkInFreq       | out       | slv(31 downto 0)       | Frequency Measurements                    |
| clinkClkFreq    | out       | slv(31 downto 0)       |                                           |
| sysClk          | in        | sl                     | AXI-Lite Interface                        |
| sysRst          | in        | sl                     |                                           |
| axilReadMaster  | in        | AxiLiteReadMasterType  |                                           |
| axilReadSlave   | out       | AxiLiteReadSlaveType   |                                           |
| axilWriteMaster | in        | AxiLiteWriteMasterType |                                           |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                           |
## Signals

| Name      | Type                  | Description |
| --------- | --------------------- | ----------- |
| intClk    | sl                    |             |
| intRst    | sl                    |             |
| intClk4x  | sl                    |             |
| intClk1x  | sl                    |             |
| intDelay  | slv(8 downto 0)       |             |
| intLd     | sl                    |             |
| cblInDly  | slv(4 downto 0)       |             |
| cblIn     | slv(4 downto 0)       |             |
| rawIn     | slv(4 downto 0)       |             |
| serdes    | Slv8Array(4 downto 0) |             |
| dataShift | Slv7Array(4 downto 0) |             |
| clkReset  | sl                    |             |
| dlyRstL   | sl                    |             |
## Instantiations

- U_clkInFreq: surf.SyncClockFreq
- U_clinkClkFreq: surf.SyncClockFreq
- U_MMCM: surf.ClockManagerUltraScale
**Description**
Clock Generation

- U_SyncDelay: surf.SynchronizerFifo
**Description**
Sync delay inputs

