# Entity: JesdAlignFrRepCh

- **File**: JesdAlignFrRepCh.vhd
## Diagram

![Diagram](JesdAlignFrRepCh.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Align bytes and replace control characters with data

 What is supported:
              Frame sizes 1, 2, 4
              GT Word sizes 2, 4  <--- I don't think 2 word is supported because hard coded in Jesd204bPkg.vhd

          Note:
          dataRx_i - is little endian and byte-swapped (directly from GTH)
                First sample in time:  dataRx_i(7  downto 0) & dataRx_i(15 downto 8)
                Second sample in time: dataRx_i(23 downto 16)& dataRx_i(31 downto 24)

          sampleData_o is big endian and not byte-swapped
                First sample in time:  sampleData_o(31 downto 16)
                Second sample in time: sampleData_o(15 downto 0)
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

| Generic name | Type     | Value | Description                 |
| ------------ | -------- | ----- | --------------------------- |
| TPD_G        | time     | 1 ns  |                             |
| F_G          | positive | 2     | Number of bytes in a frame  |
## Ports

| Port name         | Direction | Type                               | Description                                                                             |
| ----------------- | --------- | ---------------------------------- | --------------------------------------------------------------------------------------- |
| clk               | in        | sl                                 |                                                                                         |
| rst               | in        | sl                                 |                                                                                         |
| replEnable_i      | in        | sl                                 | Enable character replacement                                                            |
| scrEnable_i       | in        | sl                                 | Enable scrambling/descrambling                                                          |
| alignFrame_i      | in        | sl                                 | One c-c long pulse from syncFSM indicating that first non Kcharacter has been received  |
| dataValid_i       | in        | sl                                 | Data ready (replace control character with data when '1')                               |
| dataRx_i          | in        | slv((GT_WORD_SIZE_C*8)-1 downto 0) | Data and character indication                                                           |
| chariskRx_i       | in        | slv(GT_WORD_SIZE_C-1 downto 0)     |                                                                                         |
| sampleData_o      | out       | slv((GT_WORD_SIZE_C*8)-1 downto 0) | Sample data output (after alignment, character replacement and scrambling)              |
| sampleDataValid_o | out       | sl                                 |                                                                                         |
| alignErr_o        | out       | sl                                 |  Invalid or misaligned character in the data                                            |
| positionErr_o     | out       | sl                                 |  Invalid (comma) position received at time of alignment                                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name              | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| ----------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SAMPLES_IN_WORD_C | positive |  (GT_WORD_SIZE_C/F_G)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| REG_INIT_C        | RegType  |  (       dataRxD1      => (others => '0'),<br><span style="padding-left:20px">       chariskRxD1   => (others => '0'),<br><span style="padding-left:20px">       dataAlignedD1 => (others => '0'),<br><span style="padding-left:20px">       charAlignedD1 => (others => '0'),<br><span style="padding-left:20px">       scrData       => (others => '0'),<br><span style="padding-left:20px">       lfsr          => (others => '0'),<br><span style="padding-left:20px">       descrData     => (others => '0'),<br><span style="padding-left:20px">       scrDataValid  => '0',<br><span style="padding-left:20px">       sampleData    => (others => '0'),<br><span style="padding-left:20px">       descrDataValid  => '0',<br><span style="padding-left:20px">       dataValid     => '0',<br><span style="padding-left:20px">       position      => intToSlv(1,<br><span style="padding-left:20px"> GT_WORD_SIZE_C)  -- Initialize at "0001" or "01"       ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, rst, chariskRx_i, dataRx_i, alignFrame_i, dataValid_i, replEnable_i, scrEnable_i )
- seq: ( clk )
