# Entity: AxiAds42lb69Reg

- **File**: AxiAds42lb69Reg.vhd
## Diagram

![Diagram](AxiAds42lb69Reg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: AXI-Lite Register Access
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

| Generic name   | Type            | Value     | Description  |
| -------------- | --------------- | --------- | ------------ |
| TPD_G          | time            | 1 ns      |              |
| SIM_SPEEDUP_G  | boolean         | false     |              |
| ADC_CLK_FREQ_G | real            | 250.00E+6 |  units of Hz |
| DMODE_INIT_G   | slv(1 downto 0) | "00"      |              |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface (axiClk domain) |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
| status         | in        | AxiAds42lb69StatusType | Register Inputs/Outputs (Mixed domain)      |
| config         | out       | AxiAds42lb69ConfigType |                                             |
| adcClk         | in        | sl                     | Global Signals                              |
| adcRst         | in        | sl                     |                                             |
| axiClk         | in        | sl                     |                                             |
| axiRst         | in        | sl                     |                                             |
## Signals

| Name  | Type                   | Description |
| ----- | ---------------------- | ----------- |
| r     | RegType                |             |
| rin   | RegType                |             |
| ra    | AdcType                |             |
| rain  | AdcType                |             |
| regIn | AxiAds42lb69StatusType |             |
## Constants

| Name         | Type    | Value                                                                                                                                                                                                                                                                                                                                     | Description |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TIMEOUT_1S_C | natural |  ite(SIM_SPEEDUP_G,<br><span style="padding-left:20px"> 1000,<br><span style="padding-left:20px"> getTimeRatio(ADC_CLK_FREQ_G,<br><span style="padding-left:20px"> 1.0E+00))                                                                                                                                                              |             |
| REG_INIT_C   | RegType |  (       adcSmpl       => (others => (others => (others => '0'))),<br><span style="padding-left:20px">       regOut        => AXI_ADS42LB69_CONFIG_INIT_C,<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
| ADC_INIT_C   | AdcType |  (       timer         => 0,<br><span style="padding-left:20px">       smplCnt       => 0,<br><span style="padding-left:20px">       armed         => '0')                                                                                                                                                                                |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
| AdcType |      |             |
## Processes
- comb: ( axiRst, adcRst, axiReadMaster, axiWriteMaster, r, ra, regIn )
- seq: ( axiClk )
- seqa: ( adcClk )
