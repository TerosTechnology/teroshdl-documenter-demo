# Entity: MdioLinkIrqHandler

- **File**: MdioLinkIrqHandler.vhd
## Diagram

![Diagram](MdioLinkIrqHandler.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : MDIO Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
    Handle link interrupts signaled by an external PHY and determine
    updated link status and speed. This modules uses the MdioSeqCore
    sequencer core.
-----------------------------------------------------------------------------
 This file is part of 'SLAC Firmware Standard Library'.
 It is subject to the license terms in the LICENSE.txt file found in the
 top-level directory of this distribution and at:
    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
 No part of 'SLAC Firmware Standard Library', including this file,
 may be copied, modified, propagated, or distributed except according to
 the terms contained in the LICENSE.txt file.
-----------------------------------------------------------------------------
 This module processes two simple sequences of MDIO commands:

 1. An initialization sequence upon startup and after reset
 2. A 'IRQ handler sequence' as a response to a phyIrq.
    This handler sequence usually contains read transactions
    which determine the new link status. The first
    NUM_HDLR_ARGS_G replies to such read transactions are
    stored and passed back to the user in the 'args' array for
    further processing by the user.
## Generics

| Generic name    | Type                            | Value | Description                                                |
| --------------- | ------------------------------- | ----- | ---------------------------------------------------------- |
| TPD_G           | time                            | 1 ns  |                                                            |
| DIV_G           | natural range 1 to natural'high | 1     | half-period of MDC in clk cycles                           |
| PROG_INIT_G     | MdioProgramArray                |       | initialization sequence                                    |
| PROG_HDLR_G     | MdioProgramArray                |       |                                                            |
| NUM_HDLR_ARGS_G | natural                         |       | number of readback values the PROG_HDLR_G sequence reads.  |
## Ports

| Port name | Direction | Type                                 | Description                                                     |
| --------- | --------- | ------------------------------------ | --------------------------------------------------------------- |
| clk       | in        | sl                                   | clock and reset                                                 |
| rst       | in        | sl                                   |                                                                 |
| initDone  | out       | sl                                   | misc                                                            |
| hdlrDone  | out       | sl                                   | interrupt handled; args array is 'valid' while this is asserted |
| args      | out       | Slv16Array(0 to NUM_HDLR_ARGS_G - 1) | readback values of the PROG_HDLR_G sequence                     |
| mdc       | out       | sl                                   | MDIO interface                                                  |
| mdo       | out       | sl                                   |                                                                 |
| mdi       | in        | sl                                   |                                                                 |
| phyIrq    | in        | sl                                   | phy interrupt (link status change)                              |
## Signals

| Name     | Type             | Description |
| -------- | ---------------- | ----------- |
| r        | RegType          |             |
| rin      | RegType          |             |
| mdioRead | sl               |             |
| mdioDone | sl               |             |
| mdioData | slv(15 downto 0) |             |
## Constants

| Name        | Type             | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PC_INIT_C   | natural          |  0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| PC_HDLR_C   | natural          |  PC_INIT_C + PROG_INIT_G'length                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |             |
| REG_INIT_C  | RegType          |  (       state      => INIT,<br><span style="padding-left:20px">       nextState  => INIT,<br><span style="padding-left:20px">       pc         => PC_INIT_C,<br><span style="padding-left:20px">       mdioData   => (others => (others => '0')),<br><span style="padding-left:20px">       rbp        =>  0,<br><span style="padding-left:20px">       trg        => '0',<br><span style="padding-left:20px">       initDone   => '0',<br><span style="padding-left:20px">       hdlrDone   => '0'    ) |             |
| MDIO_PROG_C | MdioProgramArray |        (       PROG_INIT_G &       PROG_HDLR_G       )                                                                                                                                                                                                                                                                                                                                                                                                                                                    |             |
## Types

| Name      | Type                                                                                                                                                                                                | Description |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (INIT,<br><span style="padding-left:20px"> START_HDLR,<br><span style="padding-left:20px"> HDLR_DONE,<br><span style="padding-left:20px"> IDLE,<br><span style="padding-left:20px"> WAIT_FOR_MDIO)  |             |
| RegType   |                                                                                                                                                                                                     |             |
## Processes
- COMB: ( r, phyIrq, mdioDone, mdioRead, mdioData )
- SEQ: ( clk )
## Instantiations

- U_MdioCtrl: surf.MdioSeqCore
