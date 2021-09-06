# Entity: DspPreSubMult

- **File**: DspPreSubMult.vhd
## Diagram

![Diagram](DspPreSubMult.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Generalized DSP inferred multiplier with pre-adder
              configured as subtractor (based on UG901)
 Equation: p = (a - b) x c
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

| Generic name   | Type                 | Value | Description                                  |
| -------------- | -------------------- | ----- | -------------------------------------------- |
| TPD_G          | time                 | 1 ns  |                                              |
| RST_POLARITY_G | sl                   | '1'   |  '1' for active high rst, '0' for active low |
| USE_DSP_G      | string               | "yes" |                                              |
| PIPE_STAGES_G  | natural range 0 to 1 | 0     |                                              |
| A_WIDTH_G      | natural              | 12    |                                              |
| B_WIDTH_G      | natural              | 16    |                                              |
| C_WIDTH_G      | natural              | 17    |                                              |
## Ports

| Port name | Direction | Type                                | Description        |
| --------- | --------- | ----------------------------------- | ------------------ |
| clk       | in        | sl                                  |                    |
| rst       | in        | sl                                  |                    |
| ibValid   | in        | sl                                  | Inbound Interface  |
| ibReady   | out       | sl                                  |                    |
| ain       | in        | slv(A_WIDTH_G-1 downto 0)           |                    |
| bin       | in        | slv(B_WIDTH_G-1 downto 0)           |                    |
| cin       | in        | slv(C_WIDTH_G-1 downto 0)           |                    |
| obValid   | out       | sl                                  | Outbound Interface |
| obReady   | in        | sl                                  |                    |
| pOut      | out       | slv(B_WIDTH_G + C_WIDTH_G downto 0) |                    |
## Signals

| Name   | Type                                | Description |
| ------ | ----------------------------------- | ----------- |
| r      | RegType                             |             |
| rin    | RegType                             |             |
| tReady | slv(1 downto 0)                     |             |
| p      | slv(B_WIDTH_G + C_WIDTH_G downto 0) |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ibReady => '0',<br><span style="padding-left:20px">       tReady  => '0',<br><span style="padding-left:20px">       tValid  => (others => '0'),<br><span style="padding-left:20px">       diff    => (others => '0'),<br><span style="padding-left:20px">       c       => (others => '0'),<br><span style="padding-left:20px">       p       => (others => '0')) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( ain, bin, cin, ibValid, r, rst, tReady )
- seq: ( clk )
## Instantiations

- U_Pipe: surf.FifoOutputPipeline
