# Entity: RssiParamSync

- **File**: RssiParamSync.vhd
## Diagram

![Diagram](RssiParamSync.svg "Diagram")
## Description

Title      : RSSI Protocol: https://confluence.slac.stanford.edu/x/1IyfD
Company    : SLAC National Accelerator Laboratory
Description:  Sync the RSSI parameter across clock doamins
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
| COMMON_CLK_G | boolean | false |             |
## Ports

| Port name   | Direction | Type          | Description |
| ----------- | --------- | ------------- | ----------- |
| clk         | in        | sl            |             |
| rssiParam_i | in        | RssiParamType |             |
| rssiParam_o | out       | RssiParamType |             |
## Signals

| Name      | Type          | Description |
| --------- | ------------- | ----------- |
| rssiParam | RssiParamType |             |
## Instantiations

- U_version: surf.SynchronizerVector
- U_chksumEn: surf.SynchronizerVector
- U_timeoutUnit: surf.SynchronizerVector
- U_maxOutsSeg: surf.SynchronizerVector
- U_maxSegSize: surf.SynchronizerVector
- U_retransTout: surf.SynchronizerVector
- U_cumulAckTout: surf.SynchronizerVector
- U_nullSegTout: surf.SynchronizerVector
- U_maxRetrans: surf.SynchronizerVector
- U_maxCumAck: surf.SynchronizerVector
- U_maxOutofseq: surf.SynchronizerVector
- U_connectionId: surf.SynchronizerVector
