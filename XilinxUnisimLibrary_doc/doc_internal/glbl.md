# Entity: glbl

## Diagram

![Diagram](glbl.svg "Diagram")
## Description

   Copyright (c) 2010 Xilinx, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
 $Header: /devl/xcs/repo/env/Databases/CAEInterfaces/verunilibs/data/glbl.v,v 1.14 2010/10/28 20:44:00 fphillip Exp $
 
## Generics

| Generic name | Type | Value  | Description |
| ------------ | ---- | ------ | ----------- |
| ROC_WIDTH    |      | 100000 |             |
| TOC_WIDTH    |      | 0      |             |
| GRES_WIDTH   |      | 10000  |             |
| GRES_START   |      | 10000  |             |
## Signals

| Name                | Type       | Description |
| ------------------- | ---------- | ----------- |
| GSR                 | wire       |             |
| GTS                 | wire       |             |
| GWE                 | wire       |             |
| PRLD                | wire       |             |
| GRESTORE            | wire       |             |
| p_up_tmp            | tri1       |             |
| PLL_LOCKG           | tri        |             |
| PROGB_GLBL          | wire       |             |
| CCLKO_GLBL          | wire       |             |
| FCSBO_GLBL          | wire       |             |
| DO_GLBL             | wire [3:0] |             |
| DI_GLBL             | wire [3:0] |             |
| GSR_int             | reg        |             |
| GTS_int             | reg        |             |
| PRLD_int            | reg        |             |
| GRESTORE_int        | reg        |             |
| JTAG_TDO_GLBL       | wire       |             |
| JTAG_TCK_GLBL       | wire       |             |
| JTAG_TDI_GLBL       | wire       |             |
| JTAG_TMS_GLBL       | wire       |             |
| JTAG_TRST_GLBL      | wire       |             |
| JTAG_CAPTURE_GLBL   | reg        |             |
| JTAG_RESET_GLBL     | reg        |             |
| JTAG_SHIFT_GLBL     | reg        |             |
| JTAG_UPDATE_GLBL    | reg        |             |
| JTAG_RUNTEST_GLBL   | reg        |             |
| JTAG_SEL1_GLBL      | reg        |             |
| JTAG_SEL2_GLBL      | reg        |             |
| JTAG_SEL3_GLBL      | reg        |             |
| JTAG_SEL4_GLBL      | reg        |             |
| JTAG_USER_TDO1_GLBL | reg        |             |
| JTAG_USER_TDO2_GLBL | reg        |             |
| JTAG_USER_TDO3_GLBL | reg        |             |
| JTAG_USER_TDO4_GLBL | reg        |             |
