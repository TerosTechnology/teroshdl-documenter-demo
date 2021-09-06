# Entity: BoxcarFilter

- **File**: BoxcarFilter.vhd
## Diagram

![Diagram](BoxcarFilter.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Simple boxcar filter
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

| Generic name | Type     | Value | Description                            |
| ------------ | -------- | ----- | -------------------------------------- |
| TPD_G        | time     | 1 ns  |                                        |
| SIGNED_G     | boolean  | false |  Treat data as unsigned by default     |
| DOB_REG_G    | boolean  | false |  Extra reg on doutb (folded into BRAM) |
| DATA_WIDTH_G | positive | 16    |                                        |
| ADDR_WIDTH_G | positive | 10    |                                        |
## Ports

| Port name | Direction | Type                         | Description        |
| --------- | --------- | ---------------------------- | ------------------ |
| clk       | in        | sl                           |                    |
| rst       | in        | sl                           |                    |
| ibValid   | in        | sl                           | Inbound Interface  |
| ibData    | in        | slv(DATA_WIDTH_G-1 downto 0) |                    |
| obValid   | out       | sl                           | Outbound Interface |
| obData    | out       | slv(DATA_WIDTH_G-1 downto 0) |                    |
| obFull    | out       | sl                           |                    |
| obPeriod  | out       | sl                           |                    |
## Signals

| Name    | Type                                      | Description |
| ------- | ----------------------------------------- | ----------- |
| intData | slv(DATA_WIDTH_G+ADDR_WIDTH_G-1 downto 0) |             |
## Instantiations

- U_Integrator: surf.BoxcarIntegrator
