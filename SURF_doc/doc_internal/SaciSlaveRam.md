# Entity: SaciSlaveRam

- **File**: SaciSlaveRam.vhd
## Diagram

![Diagram](SaciSlaveRam.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : SACI Protocol: https://confluence.slac.stanford.edu/x/YYcRDQ
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Simulation testbed for SaciSlaveRam
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
## Ports

| Port name  | Direction | Type             | Description |
| ---------- | --------- | ---------------- | ----------- |
| saciClkOut | in        | sl               |             |
| exec       | in        | sl               |             |
| ack        | out       | sl               |             |
| readL      | in        | sl               |             |
| cmd        | in        | slv(6 downto 0)  |             |
| addr       | in        | slv(11 downto 0) |             |
| wrData     | in        | slv(31 downto 0) |             |
| rdData     | out       | slv(31 downto 0) |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| ram  | RamType |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RamType |      |             |
## Processes
- p: (  )
