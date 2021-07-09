# Entity: GtpTxPhaseAligner

## Diagram

![Diagram](GtpTxPhaseAligner.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: GTH7 TX phase aligner
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

| Port name            | Direction | Type      | Description |
| -------------------- | --------- | --------- | ----------- |
| gtpTxUsrClk2         | in        | std_logic |             |
| gtpReset             | in        | std_logic |             |
| gtpPllLockDetect     | in        | std_logic |             |
| gtpTxEnPmaPhaseAlign | out       | std_logic |             |
| gtpTxPmaSetPhase     | out       | std_logic |             |
| gtpTxAligned         | out       | std_logic |             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
|  rin | RegType |             |
## Types

| Name      | Type                                                                                                             | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (PHASE_ALIGN_S,<br><span style="padding-left:20px"> SET_PHASE_S,<br><span style="padding-left:20px"> ALIGNED_S)  |             |
| RegType   |                                                                                                                  |             |
## Processes
- seq: ( gtpTxUsrClk2, gtpReset, gtpPllLockDetect )
- comb: ( r )
