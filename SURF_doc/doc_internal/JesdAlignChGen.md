# Entity: JesdAlignChGen

- **File**: JesdAlignChGen.vhd
## Diagram

![Diagram](JesdAlignChGen.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description:  Alignment character generator
    Scrambles incoming data if enabled
    Inverts incoming data if enabled
    Replaces data with F and A characters.
    A(K28.3) - x"7C" - Inserted at the end of a multi-frame.
    F(K28.7) - x"FC" - Inserted at the end of a frame.
    Note: Character replacement mechanism is different weather scrambler is enabled or disabled.
    Disabled: The characters are inserted if two corresponding octets in consecutive samples have the same value.
    Enabled:  The characters are inserted it the corresponding octet has the same value as the inserted character.
    3 c-c data latency
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| F_G          | positive | 2     |             |
## Ports

| Port name    | Direction | Type                             | Description                    |
| ------------ | --------- | -------------------------------- | ------------------------------ |
| clk          | in        | sl                               |                                |
| rst          | in        | sl                               |                                |
| enable_i     | in        | sl                               | Enable counter                 |
| scrEnable_i  | in        | sl                               | Enable scrambling/descrambling |
| lmfc_i       | in        | sl                               | Local multi clock              |
| dataValid_i  | in        | sl                               | Valid data from Tx FSM         |
| inv_i        | in        | sl                               | Invert ADC data                |
| sampleData_i | in        | slv(GT_WORD_SIZE_C*8-1 downto 0) |                                |
| sampleData_o | out       | slv(GT_WORD_SIZE_C*8-1 downto 0) | Outs                           |
| sampleK_o    | out       | slv(GT_WORD_SIZE_C-1 downto 0)   |                                |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name              | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SAMPLES_IN_WORD_C | positive |  (GT_WORD_SIZE_C/F_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |             |
| REG_INIT_C        | RegType  |  (       sampleDataReg => (others => '0'),<br><span style="padding-left:20px">       sampleDataInv => (others => '0'),<br><span style="padding-left:20px">       sampleDataD1  => (others => '0'),<br><span style="padding-left:20px">       sampleDataD2  => (others => '0'),<br><span style="padding-left:20px">       sampleKD1     => (others => '0'),<br><span style="padding-left:20px">       lfsr          => (others => '0'),<br><span style="padding-left:20px">       lmfcD1        => '0'       ) |             |
## Types

| Name    | Type | Description   |
| ------- | ---- | ------------- |
| RegType |      | Register type |
## Processes
- comb: ( r, rst, sampleData_i, dataValid_i, enable_i, lmfc_i, scrEnable_i,
                   inv_i )
- seq: ( clk )
