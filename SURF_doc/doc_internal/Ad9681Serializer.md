# Entity: Ad9681Serializer

- **File**: Ad9681Serializer.vhd
## Diagram

![Diagram](Ad9681Serializer.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: 14 bit DDR deserializer using 7 series IDELAYE2 and ISERDESE2.
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

| Port name | Direction | Type            | Description               |
| --------- | --------- | --------------- | ------------------------- |
| clk       | in        | sl              |  Serial High speed clock  |
| clkDiv    | in        | sl              |  Parallel low speed clock |
| rst       | in        | sl              |  Reset                    |
| iData     | in        | slv(7 downto 0) |                           |
| oData     | out       | sl              |                           |
## Instantiations

- oserdese2_master: OSERDESE2
