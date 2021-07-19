# Entity: BoxcarIntegrator

- **File**: BoxcarIntegrator.vhd
## Diagram

![Diagram](BoxcarIntegrator.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Simple boxcar integrator
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type     | Value | Description                           |
| ------------ | -------- | ----- | ------------------------------------- |
| TPD_G        | time     | 1 ns  |                                       |
| SIGNED_G     | boolean  | false | Treat data as unsigned by default     |
| DOB_REG_G    | boolean  | false | Extra reg on doutb (folded into BRAM) |
| DATA_WIDTH_G | positive | 16    |                                       |
| ADDR_WIDTH_G | positive | 10    |                                       |
## Ports

| Port name | Direction | Type                                      | Description                                                   |
| --------- | --------- | ----------------------------------------- | ------------------------------------------------------------- |
| clk       | in        | sl                                        |                                                               |
| rst       | in        | sl                                        |                                                               |
| intCount  | in        | slv(ADDR_WIDTH_G-1 downto 0)              | Configuration, intCount is 0 based, 0 = 1, 1 = 2, 1023 = 1024 |
| ibValid   | in        | sl                                        | Inbound Interface                                             |
| ibData    | in        | slv(DATA_WIDTH_G-1 downto 0)              |                                                               |
| obValid   | out       | sl                                        | Outbound Interface                                            |
| obAck     | in        | sl                                        |                                                               |
| obData    | out       | slv(DATA_WIDTH_G+ADDR_WIDTH_G-1 downto 0) |                                                               |
| obFull    | out       | sl                                        |                                                               |
| obPeriod  | out       | sl                                        |                                                               |
## Signals

| Name     | Type                          | Description |
| -------- | ----------------------------- | ----------- |
| r        | RegType                       |             |
| rin      | RegType                       |             |
| ramDout  | slv(DATA_WIDTH_G-1 downto 0)  |             |
| ramDoutE | signed(DATA_WIDTH_G downto 0) |             |
| ibDataE  | signed(DATA_WIDTH_G downto 0) |             |
| rAddr    | slv(ADDR_WIDTH_G-1 downto 0)  |             |
| wAddr    | slv(ADDR_WIDTH_G-1 downto 0)  |             |
## Constants

| Name          | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| ACCUM_WIDTH_C | positive |  (DATA_WIDTH_G+ADDR_WIDTH_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| REG_INIT_C    | RegType  |  (       obFull    => '0',<br><span style="padding-left:20px">       intCount  => (others => '0'),<br><span style="padding-left:20px">       rAddr     => (others => '0'),<br><span style="padding-left:20px">       wAddr     => (others => '0'),<br><span style="padding-left:20px">       ibValid   => '0',<br><span style="padding-left:20px">       ibData    => (others => '0'),<br><span style="padding-left:20px">       obValid   => '0',<br><span style="padding-left:20px">       obPeriod  => '0',<br><span style="padding-left:20px">       obData    => (others => '0'),<br><span style="padding-left:20px">       ibDataE   => (others => '0'),<br><span style="padding-left:20px">       obFullD   => '0',<br><span style="padding-left:20px">       ibValidD  => '0',<br><span style="padding-left:20px">       obPeriodD => '0') |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( ibData, ibDataE, ibValid, intCount, obAck, r, ramDoutE, rst )
- seq: ( clk )
## Instantiations

- U_RAM: surf.SimpleDualPortRam
