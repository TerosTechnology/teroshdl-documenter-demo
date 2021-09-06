# Entity: AxiSy56040Reg

- **File**: AxiSy56040Reg.vhd
## Diagram

![Diagram](AxiSy56040Reg.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: This controller is designed around the Micrel SY56040AR.
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

| Generic name   | Type                  | Value                    | Description  |
| -------------- | --------------------- | ------------------------ | ------------ |
| TPD_G          | time                  | 1 ns                     |              |
| AXI_CLK_FREQ_G | real                  | 200.0E+6                 |  units of Hz |
| XBAR_DEFAULT_G | Slv2Array(3 downto 0) | ("11", "10", "01", "00") |              |
## Ports

| Port name      | Direction | Type                   | Description                 |
| -------------- | --------- | ---------------------- | --------------------------- |
| xBarSin        | out       | slv(1 downto 0)        | XBAR Ports                  |
| xBarSout       | out       | slv(1 downto 0)        |                             |
| xBarConfig     | out       | sl                     |                             |
| xBarLoad       | out       | sl                     |                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                             |
| axiClk         | in        | sl                     | Clocks and Resets           |
| axiRst         | in        | sl                     |                             |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name          | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description       |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| PULSE_WIDTH_C | real    |  10.0E-9                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |  units of seconds |
| PULSE_FREQ_C  | real    |  1.0 / PULSE_WIDTH_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  units of Hz      |
| MAX_CNT_C     | natural |  getTimeRatio(AXI_CLK_FREQ_G,<br><span style="padding-left:20px"> PULSE_FREQ_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                   |
| REG_INIT_C    | RegType |  (       sin           => (others => '0'),<br><span style="padding-left:20px">       sout          => (others => '0'),<br><span style="padding-left:20px">       load          => '0',<br><span style="padding-left:20px">       config        => XBAR_DEFAULT_G,<br><span style="padding-left:20px">       cnt           => 0,<br><span style="padding-left:20px">       index         => 0,<br><span style="padding-left:20px">       -- AXI-Lite Signals       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       -- Status Machine       state         => SETUP_S) |                   |
## Types

| Name      | Type                                                                                                                                            | Description |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| stateType | ( IDLE_S,<br><span style="padding-left:20px"> SETUP_S,<br><span style="padding-left:20px"> LOAD_S,<br><span style="padding-left:20px"> HOLD_S)  |             |
| RegType   |                                                                                                                                                 |             |
## Processes
- comb: ( axiReadMaster, axiRst, axiWriteMaster, r )
- seq: ( axiClk )
