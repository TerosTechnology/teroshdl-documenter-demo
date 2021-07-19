# Entity: UartRx

- **File**: UartRx.vhd
## Diagram

![Diagram](UartRx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: UART Receiver
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                  | Value  | Description         |
| ------------ | --------------------- | ------ | ------------------- |
| TPD_G        | time                  | 1 ns   |                     |
| PARITY_G     | string                | "NONE" | "NONE" "ODD" "EVEN" |
| BAUD_MULT_G  | integer range 2 to 16 | 16     |                     |
| DATA_WIDTH_G | integer range 5 to 8  | 8      |                     |
## Ports

| Port name   | Direction | Type                         | Description |
| ----------- | --------- | ---------------------------- | ----------- |
| clk         | in        | sl                           |             |
| rst         | in        | sl                           |             |
| baudClkEn   | in        | sl                           |             |
| rdData      | out       | slv(DATA_WIDTH_G-1 downto 0) |             |
| rdValid     | out       | sl                           |             |
| parityError | out       | sl                           |             |
| rdReady     | in        | sl                           |             |
| rx          | in        | sl                           |             |
## Signals

| Name   | Type    | Description |
| ------ | ------- | ----------- |
| r      | RegType |             |
| rin    | RegType |             |
| rxSync | sl      |             |
| rxFall | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       rdValid        => '0',<br><span style="padding-left:20px">       rdData         => (others => '0'),<br><span style="padding-left:20px">       rxState        => WAIT_START_BIT_S,<br><span style="padding-left:20px">       waitState      => SAMPLE_RX_S,<br><span style="padding-left:20px">       rxShiftReg     => (others => '0'),<br><span style="padding-left:20px">       rxShiftCount   => (others => '0'),<br><span style="padding-left:20px">       baudClkEnCount => (others => '0'),<br><span style="padding-left:20px">       parity         => '0',<br><span style="padding-left:20px">       parityError    => '0') |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                   | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (WAIT_START_BIT_S,<br><span style="padding-left:20px"> WAIT_HALF_S,<br><span style="padding-left:20px"> WAIT_FULL_S,<br><span style="padding-left:20px"> SAMPLE_RX_S,<br><span style="padding-left:20px"> PARITY_S,<br><span style="padding-left:20px"> WAIT_STOP_S,<br><span style="padding-left:20px"> WRITE_OUT_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                        |             |
## Processes
- comb: ( baudClkEn, r, rdReady, rst, rxFall, rxSync )
**Description**
[out]

- sync: ( clk )
## Instantiations

- U_SynchronizerEdge_1: surf.SynchronizerEdge
