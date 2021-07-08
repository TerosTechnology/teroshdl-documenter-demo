# Entity: AxiLtc2270Core

## Diagram

![Diagram](AxiLtc2270Core.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AXI-Lite interface to LTC2270 ADC IC
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name       | Type                            | Value                                   | Description |
| ------------------ | ------------------------------- | --------------------------------------- | ----------- |
| TPD_G              | time                            | 1 ns                                    |             |
| DMODE_INIT_G       | slv(1 downto 0)                 | "00"                                    |             |
| DELAY_INIT_G       | Slv5VectorArray(0 to 1, 0 to 7) | (others => (others => (others => '0'))) |             |
| IODELAY_GROUP_G    | string                          | "AXI_LTC2270_IODELAY_GRP"               |             |
| STATUS_CNT_WIDTH_G | natural range 1 to 32           | 32                                      |             |
| AXI_CLK_FREQ_G     | real                            | 200.0E+6                                |             |
## Ports

| Port name      | Direction | Type                   | Description                                 |
| -------------- | --------- | ---------------------- | ------------------------------------------- |
| adcIn          | in        | AxiLtc2270InType       | ADC Ports                                   |
| adcOut         | out       | AxiLtc2270OutType      |                                             |
| adcInOut       | inout     | AxiLtc2270InOutType    |                                             |
| adcValid       | out       | slv(0 to 1)            | ADC signals (axiClk domain)                 |
| adcData        | out       | Slv16Array(0 to 1)     |                                             |
| axiReadMaster  | in        | AxiLiteReadMasterType  | AXI-Lite Register Interface (axiClk domain) |
| axiReadSlave   | out       | AxiLiteReadSlaveType   |                                             |
| axiWriteMaster | in        | AxiLiteWriteMasterType |                                             |
| axiWriteSlave  | out       | AxiLiteWriteSlaveType  |                                             |
| axiClk         | in        | sl                     | Clocks and Resets                           |
| axiRst         | in        | sl                     |                                             |
| adcClk         | in        | sl                     | up to 20 MHz                                |
| refclk200MHz   | in        | sl                     |                                             |
## Signals

| Name   | Type                 | Description |
| ------ | -------------------- | ----------- |
| status | AxiLtc2270StatusType |             |
| config | AxiLtc2270ConfigType |             |
## Instantiations

- AxiLtc2270Reg_Inst: surf.AxiLtc2270Reg
- AxiLtc2270Deser_Inst: surf.AxiLtc2270Deser
