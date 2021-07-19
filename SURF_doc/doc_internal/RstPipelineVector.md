# Entity: RstPipelineVector

- **File**: RstPipelineVector.vhd
## Diagram

![Diagram](RstPipelineVector.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Wrapper for multiple RstPipeline modules
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type     | Value | Description |
| ------------- | -------- | ----- | ----------- |
| TPD_G         | time     | 1 ns  |             |
| INV_RST_G     | boolean  | false |             |
| PIPE_STAGES_G | positive | 3     |             |
| MAX_FANOUT_G  | positive | 16384 |             |
| INIT_G        | slv      | "1"   |             |
| WIDTH_G       | positive | 16    |             |
## Ports

| Port name | Direction | Type                    | Description |
| --------- | --------- | ----------------------- | ----------- |
| clk       | in        | sl                      |             |
| rstIn     | in        | slv(WIDTH_G-1 downto 0) |             |
| rstOut    | out       | slv(WIDTH_G-1 downto 0) |             |
