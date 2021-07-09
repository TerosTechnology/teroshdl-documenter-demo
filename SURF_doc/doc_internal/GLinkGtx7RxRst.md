# Entity: GLinkGtx7RxRst

## Diagram

![Diagram](GLinkGtx7RxRst.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: G-Link GTX7 Reset module
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name           | Type                  | Value | Description |
| ---------------------- | --------------------- | ----- | ----------- |
| TPD_G                  | time                  | 1 ns  |             |
| EXAMPLE_SIMULATION     | integer               | 0     |             |
| GT_TYPE                | string                | "GTX" |             |
| STABLE_CLOCK_PERIOD    | integer range 4 to 20 | 8     |             |
| RETRY_COUNTER_BITWIDTH | integer range 2 to 8  | 8     |             |
## Ports

| Port name              | Direction | Type                                                 | Description                              |
| ---------------------- | --------- | ---------------------------------------------------- | ---------------------------------------- |
| lpmMode                | in        | std_logic                                            |                                          |
| STABLE_CLOCK           | in        | std_logic                                            |                                          |
| RXUSERCLK              | in        | std_logic                                            |                                          |
| SOFT_RESET             | in        | std_logic                                            |                                          |
| PLLREFCLKLOST          | in        | std_logic                                            |                                          |
| PLLLOCK                | in        | std_logic                                            |                                          |
| RXRESETDONE            | in        | std_logic                                            |                                          |
| MMCM_LOCK              | in        | std_logic                                            |                                          |
| RECCLK_STABLE          | in        | std_logic                                            |                                          |
| RECCLK_MONITOR_RESTART | in        | std_logic                                            |                                          |
| DATA_VALID             | in        | std_logic                                            |                                          |
| TXUSERRDY              | in        | std_logic                                            |                                          |
| GTRXRESET              | out       | std_logic                                            |                                          |
| MMCM_RESET             | out       | std_logic                                            |                                          |
| PLL_RESET              | out       | std_logic                                            |                                          |
| RX_FSM_RESET_DONE      | out       | std_logic                                            |                                          |
| RXUSERRDY              | out       | std_logic                                            |                                          |
| RUN_PHALIGNMENT        | out       | std_logic                                            |                                          |
| PHALIGNMENT_DONE       | in        | std_logic                                            | Drive high if phase alignment not needed |
| RESET_PHALIGNMENT      | out       | std_logic                                            |                                          |
| RXDFEAGCHOLD           | out       | std_logic                                            |                                          |
| RXDFELFHOLD            | out       | std_logic                                            |                                          |
| RXLPMLFHOLD            | out       | std_logic                                            |                                          |
| RXLPMHFHOLD            | out       | std_logic                                            |                                          |
| RETRY_COUNTER          | out       | std_logic_vector (RETRY_COUNTER_BITWIDTH-1 downto 0) | Number of                                |
## Signals

| Name                       | Type                                   | Description |
| -------------------------- | -------------------------------------- | ----------- |
| rx_state                   | rx_rst_fsm_type                        |             |
| soft_reset_sync            | std_logic                              |             |
| soft_reset_rise            | std_logic                              |             |
| soft_reset_fall            | std_logic                              |             |
| init_wait_count            | integer range 0 to WAIT_MAX            |             |
| init_wait_done             | std_logic                              |             |
| pll_reset_asserted         | std_logic                              |             |
| rx_fsm_reset_done_int      | std_logic                              |             |
| rx_fsm_reset_done_int_s3   | std_logic                              |             |
| rxresetdone_s3             | std_logic                              |             |
| retry_counter_int          | integer range 0 to MAX_RETRIES         |             |
| time_out_counter           | integer range 0 to WAIT_TIMEOUT_2ms    |             |
| recclk_mon_restart_count   | integer range 0 to 3                   |             |
| recclk_mon_count_reset     | std_logic                              |             |
| reset_time_out             | std_logic                              |             |
| time_out_2ms               | std_logic                              |             |
| time_tlock_max             | std_logic                              |             |
| time_out_500us             | std_logic                              |             |
| time_out_1us               | std_logic                              |             |
| time_out_100us             | std_logic                              |             |
| check_tlock_max            | std_logic                              |             |
| mmcm_lock_count            | integer range 0 to MMCM_LOCK_CNT_MAX-1 |             |
| mmcm_lock_int              | std_logic                              |             |
| mmcm_lock_reclocked        | std_logic_vector(3 downto 0)           |             |
| run_phase_alignment_int    | std_logic                              |             |
| run_phase_alignment_int_s3 | std_logic                              |             |
| wait_bypass_count          | integer range 0 to MAX_WAIT_BYPASS-1   |             |
| time_out_wait_bypass       | std_logic                              |             |
| time_out_wait_bypass_s3    | std_logic                              |             |
| refclk_lost                | std_logic                              |             |
| time_out_adapt             | std_logic                              |             |
| adapt_count_reset          | std_logic                              |             |
| adapt_count                | integer range 0 to WAIT_TIME_ADAPT-1   |             |
| data_valid_sync            | std_logic                              |             |
| plllock_sync               | std_logic                              |             |
| phalignment_done_sync      | std_logic                              |             |
| fsmCnt                     | std_logic_vector(15 downto 0)          |             |
## Constants

| Name               | Type    | Value                                           | Description                                        |
| ------------------ | ------- | ----------------------------------------------- | -------------------------------------------------- |
| MMCM_LOCK_CNT_MAX  | integer |  1024                                           |                                                    |
| STARTUP_DELAY      | integer |  500                                            |                                                    |
| WAIT_CYCLES        | integer |  STARTUP_DELAY / STABLE_CLOCK_PERIOD            | Number of Clock-Cycles to wait after configuration |
| WAIT_MAX           | integer |  WAIT_CYCLES + 10                               | 500 ns plus some additional margin                 |
| WAIT_TIMEOUT_2ms   | integer |  3000000 / STABLE_CLOCK_PERIOD                  |  2 ms time-out                                     |
| WAIT_TLOCK_MAX     | integer |  100000 / STABLE_CLOCK_PERIOD                   |                                                    |
| WAIT_TIMEOUT_500us | integer |  500000 / STABLE_CLOCK_PERIOD                   |                                                    |
| WAIT_TIMEOUT_1us   | integer |  1000 / STABLE_CLOCK_PERIOD                     |                                                    |
| WAIT_TIMEOUT_100us | integer |  100000 / STABLE_CLOCK_PERIOD                   |                                                    |
| WAIT_TIME_ADAPT    | integer |  (37000000 /integer(3.125))/STABLE_CLOCK_PERIOD |                                                    |
| MAX_RETRIES        | integer |  2**RETRY_COUNTER_BITWIDTH-1                    |                                                    |
| MAX_WAIT_BYPASS    | integer |  5000                                           |                                                    |
## Types

| Name            | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| rx_rst_fsm_type | ( INIT,<br><span style="padding-left:20px"> ASSERT_ALL_RESETS,<br><span style="padding-left:20px"> RELEASE_PLL_RESET,<br><span style="padding-left:20px"> VERIFY_RECCLK_STABLE,<br><span style="padding-left:20px"> RELEASE_MMCM_RESET,<br><span style="padding-left:20px"> WAIT_RESET_DONE,<br><span style="padding-left:20px"> DO_PHASE_ALIGNMENT,<br><span style="padding-left:20px"> MONITOR_DATA_VALID,<br><span style="padding-left:20px"> FSM_DONE)  |             |
## Processes
- unnamed: ( STABLE_CLOCK )
- retries_recclk_monitor: ( STABLE_CLOCK )
- timeouts: ( STABLE_CLOCK )
- mmcm_lock_wait: ( RXUSERCLK, MMCM_LOCK )
- timeout_buffer_bypass: ( RXUSERCLK )
- reset_fsm: ( STABLE_CLOCK )
**Description**
Following steps are performed:
1) After configuration wait for approximately 500 ns as specified in
   answer-record 43482
2) Assert all resets on the GT and on an MMCM potentially connected.
   After that wait until a reference-clock has been detected.
3) Release the reset to the GT and wait until the GT-PLL has locked.
4) Release the MMCM-reset and wait until the MMCM has signalled lock.
   Also get info from the TX-side which PLL has been reset.
5) Wait for the RESET_DONE-signal from the GT.
6) Signal to start the phase-alignment procedure and wait for it to
   finish.
7) Reset-sequence has successfully run through. Signal this to the
   rest of the design by asserting RX_FSM_RESET_DONE.

## Instantiations

- Synchronizer_run_phase_alignment: surf.Synchronizer
**Description**
Clock Domain Crossing

- Synchronizer_fsm_reset_done: surf.Synchronizer
- Synchronizer_SOFT_RESET: surf.SynchronizerEdge
- Synchronizer_RXRESETDONE: surf.Synchronizer
- Synchronizer_time_out_wait_bypass: surf.Synchronizer
- Synchronizer_mmcm_lock_reclocked: surf.Synchronizer
- Synchronizer_data_valid: surf.Synchronizer
- Synchronizer_PLLLOCK: surf.Synchronizer
- Synchronizer_PHALIGNMENT_DONE: surf.Synchronizer
**Description**
Phase aligner might run on rxusrclk in some cases
Synchronizer it just in case

## State machines

- FSM for resetting the GTX/GTH/GTP in the 7-series.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following steps are performed:
1) After configuration wait for approximately 500 ns as specified in
answer-record 43482
2) Assert all resets on the GT and on an MMCM potentially connected.
After that wait until a reference-clock has been detected.
3) Release the reset to the GT and wait until the GT-PLL has locked.
4) Release the MMCM-reset and wait until the MMCM has signalled lock.
Also get info from the TX-side which PLL has been reset.
5) Wait for the RESET_DONE-signal from the GT.
6) Signal to start the phase-alignment procedure and wait for it to
finish.
7) Reset-sequence has successfully run through. Signal this to the
rest of the design by asserting RX_FSM_RESET_DONE.
![Diagram_state_machine_0]( stm_GLinkGtx7RxRst_00.svg "Diagram")