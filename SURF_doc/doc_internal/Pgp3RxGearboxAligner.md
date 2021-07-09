# Entity: Pgp3RxGearboxAligner

## Diagram

![Diagram](Pgp3RxGearboxAligner.svg "Diagram")
## Description

Title      : PGPv3: https://confluence.slac.stanford.edu/x/OndODQ
Company    : SLAC National Accelerator Laboratory
Description: Aligns a GT RX gearbox.
After reset, require GOOD_COUNT_C consecutive valid headers to lock.
Once locked, require BAD_COUNT_C invalid headers withing GOOD_COUNT_C
total headers to break the lock.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| TPD_G        | time    | 1 ns  |             |
| SLIP_WAIT_G  | integer | 32    |             |
## Ports

| Port name     | Direction | Type            | Description |
| ------------- | --------- | --------------- | ----------- |
| clk           | in        | sl              |             |
| rst           | in        | sl              |             |
| rxHeader      | in        | slv(1 downto 0) |             |
| rxHeaderValid | in        | sl              |             |
| slip          | out       | sl              |             |
| locked        | out       | sl              |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name               | Type    | Value                                                                                                                                                                                                                                                                                                     | Description |
| ------------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| GOOD_COUNT_C       | integer |  128                                                                                                                                                                                                                                                                                                      |             |
| BAD_COUNT_C        | integer |  16                                                                                                                                                                                                                                                                                                       |             |
| GOOD_COUNT_WIDTH_C | integer |  log2(maximum(GOOD_COUNT_C,<br><span style="padding-left:20px"> SLIP_WAIT_G))                                                                                                                                                                                                                             |             |
| REG_INIT_C         | RegType |  (       state     => UNLOCKED_S,<br><span style="padding-left:20px">       goodCount => (others => '0'),<br><span style="padding-left:20px">       badCount  => (others => '0'),<br><span style="padding-left:20px">       slip      => '0',<br><span style="padding-left:20px">       locked    => '0') |             |
## Types

| Name      | Type                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | (UNLOCKED_S,<br><span style="padding-left:20px"> SLIP_WAIT_S,<br><span style="padding-left:20px"> LOCKED_S)  |             |
| RegType   |                                                                                                              |             |
## Processes
- comb: ( r, rst, rxHeader, rxHeaderValid )
- seq: ( clk )
