# Entity: SsiCmdMasterPulser

- **File**: SsiCmdMasterPulser.vhd
## Diagram

![Diagram](SsiCmdMasterPulser.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SSI Command Master Pulser Module
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

| Generic name   | Type     | Value | Description                 |
| -------------- | -------- | ----- | --------------------------- |
| TPD_G          | time     | 1 ns  |  Simulation FF output delay |
| OUT_POLARITY_G | sl       | '1'   |                             |
| PULSE_WIDTH_G  | positive | 1     |                             |
## Ports

| Port name   | Direction | Type             | Description                 |
| ----------- | --------- | ---------------- | --------------------------- |
| cmdSlaveOut | in        | SsiCmdMasterType | Local command signal        |
| opCode      | in        | slv(7 downto 0)  | ddressed cmdOpCode          |
| syncPulse   | out       | sl               | output pulse to sync module |
| locClk      | in        | sl               | Local clock and reset       |
| locRst      | in        | sl               |                             |
## Signals

| Name  | Type                                  | Description |
| ----- | ------------------------------------- | ----------- |
| pulse | sl                                    |             |
| cnt   | positive range 1 to (PULSE_WIDTH_G+1) |             |
## Processes
- unnamed: ( locClk )
