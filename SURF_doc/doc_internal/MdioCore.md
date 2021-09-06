# Entity: MdioCore

- **File**: MdioCore.vhd
## Diagram

![Diagram](MdioCore.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : MDIO Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Execute a MDIO-read or -write transaction
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

| Generic name | Type                            | Value | Description                                                    |
| ------------ | ------------------------------- | ----- | -------------------------------------------------------------- |
| TPD_G        | time                            | 1 ns  |                                                                |
| DIV_G        | natural range 1 to natural'high | 1     | half-period of MDC in clk cycles; MDC is a subharmonic of clk  |
## Ports

| Port name | Direction | Type             | Description                          |
| --------- | --------- | ---------------- | ------------------------------------ |
| clk       | in        | sl               | clock and reset                      |
| rst       | in        | sl               |                                      |
| trg       | in        | sl               |  assert trg for ONE clock            |
| cmd       | in        | MdioCommandType  |  cmd is latched during 'trg'         |
| din       | out       | slv(15 downto 0) |  read back data - valid during 'don' |
| don       | out       | sl               |  cmd completed; asserted for one clk |
| mdc       | out       | sl               | MDIO interface                       |
| mdo       | out       | sl               |                                      |
| mdi       | in        | sl               |                                      |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| DIV_BITS_C | positive |  bitSize( DIV_G - 1)                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| REG_INIT_C | RegType  |  (      dataOut => ( others => '1' ),<br><span style="padding-left:20px">      din     => ( others => '0' ),<br><span style="padding-left:20px">      count   => ( others => '1' ),<br><span style="padding-left:20px">      div     => ( others => '0' ),<br><span style="padding-left:20px">      mdc     => '0',<br><span style="padding-left:20px">      don     => '0',<br><span style="padding-left:20px">      state   => IDLE    ) |             |
## Types

| Name    | Type                                               | Description |
| ------- | -------------------------------------------------- | ----------- |
| State   | ( IDLE,<br><span style="padding-left:20px"> RUN )  |             |
| RegType |                                                    |             |
## Processes
- COMB: ( r, trg, mdi, cmd )
- SEQ: ( clk )
