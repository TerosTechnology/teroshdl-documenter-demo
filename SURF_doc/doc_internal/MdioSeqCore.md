# Entity: MdioSeqCore

- **File**: MdioSeqCore.vhd
## Diagram

![Diagram](MdioSeqCore.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Title      : MDIO Support
-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
    Execute sequence(s) of MDIO transaction(s). A list (array) of all possible
    transaction sequences is passed in the MDIO_PROG_G generic. Individual (sub-)
    sequences are separated by the asserted 'theLast' flag in the last instruction
    of each individual sequence.

    A typical MDIO_PROG_G is a concatenation of sequences:

    constant MDIO_PROG_C : MdioProgramArray := ( SEQ_1_C & SEQ_2_C & SEQ_3_C );

    where each sequence (SEQ_1_C, SEQ_2_C, ...) is itself a MdioProgramArray and
    has in its last instruction the 'last' flag set. E.g.,:

    constant SEQ_1_C : MdioProgramArray := (
       mdioWriteInst( PHY, REG_0, DATA_0 );
       mdioWriteInst( PHY, REG_1, DATA_2 );
       mdioReadInst ( PHY, REG_2,        true);
    );


    The user would then trigger execution of a particular sequence by

    1)  setting 'pc' to the index of the starting position of the first instruction of
     the desired sequence.
    2)  asserting 'trg' high for one clock cycle.

    The sequencer then executes all instructions up to (and including) the last one
    of a sequence.
    When done, 'don' is asserted for a single clk cycle.
    When any read transaction completes 'rs' is asserted for one cycle and readback
    data is presented at 'din' (valid while 'don' is asserted).
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

| Generic name | Type                            | Value | Description                       |
| ------------ | ------------------------------- | ----- | --------------------------------- |
| TPD_G        | time                            | 1 ns  |                                   |
| DIV_G        | natural range 1 to natural'high | 1     | half-period of MDC in clk cycles  |
| MDIO_PROG_G  | MdioProgramArray                |       | see above...                      |
## Ports

| Port name | Direction | Type             | Description                         |
| --------- | --------- | ---------------- | ----------------------------------- |
| clk       | in        | sl               | clock and reset                     |
| rst       | in        | sl               |                                     |
| trg       | in        | sl               |  assert trg for ONE clock           |
| pc        | in        | natural          |                                     |
| rs        | out       | sl               |  read back data valid               |
| din       | out       | slv(15 downto 0) |  read back data - valid during 'rs' |
| don       | out       | sl               |  program completed                  |
| mdc       | out       | sl               | MDIO interface                      |
| mdo       | out       | sl               |                                     |
| mdi       | in        | sl               |                                     |
## Signals

| Name    | Type    | Description |
| ------- | ------- | ----------- |
| r       | RegType |             |
| rin     | RegType |             |
| oneDone | sl      |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                 | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state   => IDLE,<br><span style="padding-left:20px">       inst    => mdioReadInst(0,<br><span style="padding-left:20px">0,<br><span style="padding-left:20px">true),<br><span style="padding-left:20px">       pc      =>  0,<br><span style="padding-left:20px">       trg     => '0'    ) |             |
## Types

| Name      | Type                                                                                          | Description |
| --------- | --------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE,<br><span style="padding-left:20px"> TRIG,<br><span style="padding-left:20px"> PROG )  |             |
| RegType   |                                                                                               |             |
## Processes
- COMB: ( r, trg, pc, oneDone )
- SEQ: ( clk )
## Instantiations

- U_MdioCore: surf.MdioCore
