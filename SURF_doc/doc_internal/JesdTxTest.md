# Entity: JesdTxTest

- **File**: JesdTxTest.vhd
## Diagram

![Diagram](JesdTxTest.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: JesdTx simple module for testing RX
              Transmitter module for testing JESD RX module.
              - it replaces GT core and generates a dummy data stream for JESD Rx testing.
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

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name     | Direction | Type                           | Description                                                 |
| ------------- | --------- | ------------------------------ | ----------------------------------------------------------- |
| devClk_i      | in        | sl                             | JESDClocks and Resets                                       |
| devRst_i      | in        | sl                             |                                                             |
| subClass_i    | in        | sl                             | JESD subclass selection: '0' or '1'(default)                |
| enable_i      | in        | sl                             | Control and status register records                         |
| lmfc_i        | in        | sl                             | Local multi frame clock                                     |
| nSync_i       | in        | sl                             | Synchronization request input                               |
| delay_i       | in        | slv(3 downto 0)                |  1 to 16 clock cycles                                       |
| align_i       | in        | slv(GT_WORD_SIZE_C-1 downto 0) |  0001, 0010, 0100, 1000                                     |
| txDataValid_o | out       | sl                             |                                                             |
| r_jesdGtRx    | out       | jesdGtRxLaneType               | Data and character output and GT signals (simple generated) |
## Signals

| Name        | Type                        | Description                                  |
| ----------- | --------------------------- | -------------------------------------------- |
| r           | RegType                     |                                              |
| rin         | RegType                     |                                              |
| s_testCntr  | slv(7 downto 0)             |  Internal signals  Control signals from FSM  |
| s_dataValid | sl                          |                                              |
| s_align     | sl                          |                                              |
| s_lmfc_dly  | sl                          |                                              |
| s_nsync_dly | sl                          |                                              |
| s_dataK     | slv(r_jesdGtRx.dataK'range) |                                              |
| s_data      | slv(r_jesdGtRx.data'range)  |                                              |
| s_data_sel  | slv(1 downto 0)             |                                              |
## Constants

| Name       | Type    | Value                                                                                                             | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       dataD1  => (others => '0'),<br><span style="padding-left:20px">       dataKD1 => (others => '0')       ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( devRst_i, r, s_data, s_dataK )
- seq: ( devClk_i )
## Instantiations

- lmfcDly_INST: surf.SlvDelay
- nsyncDly_INST: surf.SlvDelay
**Description**
 Delay nsync input (for 1 to 16 c-c) to

- syncFSM_INST: surf.JesdSyncFsmTxTest
**Description**
 Synchronization FSM

