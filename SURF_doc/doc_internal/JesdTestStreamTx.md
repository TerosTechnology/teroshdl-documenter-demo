# Entity: JesdTestStreamTx

- **File**: JesdTestStreamTx.vhd
## Diagram

![Diagram](JesdTestStreamTx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Test Data Stream Generator
 Outputs a saw, ramp, or square wave test signal data stream for testing
 Saw signal increment (type_i = 00): Ramp step is determined by rampStep_i.
 Saw signal decrement (type_i = 01): Ramp step is determined by rampStep_i.
 Square wave(type_i = 10): Period is squarePeriod_i. Duty cycle is 50%.
                           Amplitude is determined by posAmplitude_i and negAmplitude_i.
                           pulse_o is a binary equivalent of the analogue square wave.
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

| Port name      | Direction | Type                             | Description                                 |
| -------------- | --------- | -------------------------------- | ------------------------------------------- |
| clk            | in        | sl                               |                                             |
| rst            | in        | sl                               |                                             |
| enable_i       | in        | sl                               | Enable signal generation                    |
| type_i         | in        | slv(1 downto 0)                  | Signal type                                 |
| rampStep_i     | in        | slv(PER_STEP_WIDTH_C-1 downto 0) | Increase counter by the step                |
| squarePeriod_i | in        | slv(PER_STEP_WIDTH_C-1 downto 0) |                                             |
| posAmplitude_i | in        | slv(F_G*8-1 downto 0)            | Positive and negative amplitude square wave |
| negAmplitude_i | in        | slv(F_G*8-1 downto 0)            |                                             |
| sampleData_o   | out       | slv(GT_WORD_SIZE_C*8-1 downto 0) | Sample data containing test signal          |
| pulse_o        | out       | sl                               | Digital out pulse for latency debug         |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type     | Value                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| SAM_IN_WORD_C | positive |  (GT_WORD_SIZE_C/F_G)                                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C    | RegType  |  (       typeDly   => (others => '0'),<br><span style="padding-left:20px">       squareCnt => (others => '0'),<br><span style="padding-left:20px">       rampCnt   => (others => '0'),<br><span style="padding-left:20px">       testData  => (others => '0'),<br><span style="padding-left:20px">       inc       => '1',<br><span style="padding-left:20px">       sign      => '0'    ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( r, rst,enable_i,rampStep_i,type_i,posAmplitude_i,squarePeriod_i,negAmplitude_i )
- seq: ( clk )
