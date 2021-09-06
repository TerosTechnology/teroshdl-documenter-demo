# Entity: Dsp48Comparator4x12b

- **File**: Dsp48Comparator4x12b.vhd
## Diagram

![Diagram](Dsp48Comparator4x12b.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: This module is a quad 12-bit digital comparator using a DSP48
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

| Generic name       | Type    | Value | Description |
| ------------------ | ------- | ----- | ----------- |
| TPD_G              | time    | 1 ns  |             |
| EN_GREATER_EQUAL_G | boolean | false |             |
## Ports

| Port name | Direction | Type               | Description                |
| --------- | --------- | ------------------ | -------------------------- |
| polarity  | in        | sl                 | Data and Threshold Signals |
| dataIn    | in        | Slv12Array(0 to 3) |                            |
| threshIn  | in        | Slv12Array(0 to 3) |                            |
| compOut   | out       | slv(3 downto 0)    |  '1' when data > threshold |
| clk       | in        | sl                 | Clock and Reset Signals    |
| rst       | in        | sl                 |                            |
## Signals

| Name          | Type             | Description |
| ------------- | ---------------- | ----------- |
| carryOut      | slv(3 downto 0)  |             |
| din           | slv(47 downto 0) |             |
| A             | slv(29 downto 0) |             |
| B             | slv(17 downto 0) |             |
| C             | slv(47 downto 0) |             |
| reset         | sl               |             |
| 
      rstDly | sl               |             |
## Processes
- unnamed: ( clk )
</br>**Description**
 Reduce the fanout of the reset signal to help with timing 
## Instantiations

- DSP48E1_Inst: DSP48E1
