# Entity: SspEncoder12b14b

- **File**: SspEncoder12b14b.vhd
## Diagram

![Diagram](SspEncoder12b14b.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SimpleStreamingProtocol - A simple protocol layer for inserting
 idle and framing control characters into a raw data stream. This module
 ties the framing core to an RTL 12b14b encoder.
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

| Generic name   | Type    | Value | Description |
| -------------- | ------- | ----- | ----------- |
| TPD_G          | time    | 1 ns  |             |
| RST_POLARITY_G | sl      | '0'   |             |
| RST_ASYNC_G    | boolean | true  |             |
| AUTO_FRAME_G   | boolean | true  |             |
| FLOW_CTRL_EN_G | boolean | false |             |
## Ports

| Port name | Direction | Type             | Description |
| --------- | --------- | ---------------- | ----------- |
| clk       | in        | sl               |             |
| rst       | in        | sl               |             |
| validIn   | in        | sl               |             |
| readyIn   | out       | sl               |             |
| sof       | in        | sl               |             |
| eof       | in        | sl               |             |
| dataIn    | in        | slv(11 downto 0) |             |
| validOut  | out       | sl               |             |
| readyOut  | in        | sl               |             |
| dataOut   | out       | slv(13 downto 0) |             |
## Signals

| Name        | Type             | Description |
| ----------- | ---------------- | ----------- |
| framedData  | slv(11 downto 0) |             |
| framedDataK | slv(0 downto 0)  |             |
| validInt    | sl               |             |
| readyInt    | sl               |             |
## Instantiations

- SspFramer_1: surf.SspFramer
- Encoder12b14b_1: surf.Encoder12b14b
