# Entity: SemWrapper

## Diagram

![Diagram](SemWrapper.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for 7-series SEM module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name      | Direction | Type             | Description     |
| -------------- | --------- | ---------------- | --------------- |
| semClk         | in        | sl               | Clock and Reset |
| semRst         | in        | sl               |                 |
| fpgaReload     | in        | sl               | IPROG Interface |
| fpgaReloadAddr | in        | slv(31 downto 0) |                 |
| semIb          | in        | SemIbType        | SEM Interface   |
| semOb          | out       | SemObType        |                 |
## Signals

| Name               | Type             | Description |
| ------------------ | ---------------- | ----------- |
| fecc_crcerr        | sl               |             |
| fecc_eccerr        | sl               |             |
| fecc_eccerrsingle  | sl               |             |
| fecc_syndromevalid | sl               |             |
| fecc_syndrome      | slv(12 downto 0) |             |
| fecc_far           | slv(25 downto 0) |             |
| fecc_synbit        | slv(4 downto 0)  |             |
| fecc_synword       | slv(6 downto 0)  |             |
| icap_o             | slv(31 downto 0) |             |
| icap_i             | slv(31 downto 0) |             |
| icap_csib          | sl               |             |
| icap_rdwrb         | sl               |             |
| sem_icap_csib      | sl               |             |
| sem_icap_rdwrb     | sl               |             |
| sem_icap_i         | slv(31 downto 0) |             |
| iprogIcapReq       | sl               |             |
| iprogIcapGrant     | sl               |             |
| iprogIcapCsl       | sl               |             |
| iprogIcapRnw       | sl               |             |
| iprogIcapI         | slv(31 downto 0) |             |
## Instantiations

- U_FRAME_ECCE2: FRAME_ECCE2
- U_ICAPE2: ICAPE2
- U_IPROG: surf.Iprog7SeriesCore
- U_SemCore: SemCore
