# Entity: HBM_ONE_STACK_INTF

## Diagram

![Diagram](HBM_ONE_STACK_INTF.svg "Diagram")
## Description

    Copyright (c) 1995/2017 Xilinx, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
 
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   ____  ____
  /   /\/   /
 /___/  \  /     Vendor      : Xilinx
 \   \   \/      Version     : 2018.1
  \   \          Description : Xilinx Unified Simulation Library Component
  /   /                        HBM_ONE_STACK_INTF
 /___/   /\      Filename    : HBM_ONE_STACK_INTF.v
 \   \  /  \
  \___\/\___\
  Revision:
  End Revision:
 
## Generics

| Generic name                | Type    | Value             | Description |
| --------------------------- | ------- | ----------------- | ----------- |
| XIL_TIMING                  |         | "UNPLACED"        |             |
| CLK_SEL_00                  |         | "FALSE"           |             |
| CLK_SEL_01                  |         | "FALSE"           |             |
| CLK_SEL_02                  |         | "FALSE"           |             |
| CLK_SEL_03                  |         | "FALSE"           |             |
| CLK_SEL_04                  |         | "FALSE"           |             |
| CLK_SEL_05                  |         | "FALSE"           |             |
| CLK_SEL_06                  |         | "FALSE"           |             |
| CLK_SEL_07                  |         | "FALSE"           |             |
| CLK_SEL_08                  |         | "FALSE"           |             |
| CLK_SEL_09                  |         | "FALSE"           |             |
| CLK_SEL_10                  |         | "FALSE"           |             |
| CLK_SEL_11                  |         | "FALSE"           |             |
| CLK_SEL_12                  |         | "FALSE"           |             |
| CLK_SEL_13                  |         | "FALSE"           |             |
| CLK_SEL_14                  |         | "FALSE"           |             |
| CLK_SEL_15                  |         | "FALSE"           |             |
| DATARATE_00                 | integer | 1800              |             |
| DATARATE_01                 | integer | 1800              |             |
| DATARATE_02                 | integer | 1800              |             |
| DATARATE_03                 | integer | 1800              |             |
| DATARATE_04                 | integer | 1800              |             |
| DATARATE_05                 | integer | 1800              |             |
| DATARATE_06                 | integer | 1800              |             |
| DATARATE_07                 | integer | 1800              |             |
| DA_LOCKOUT                  |         | "FALSE"           |             |
| IS_APB_0_PCLK_INVERTED      | [0:0]   | 1'b0              |             |
| IS_APB_0_PRESET_N_INVERTED  | [0:0]   | 1'b0              |             |
| IS_AXI_00_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_00_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_01_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_01_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_02_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_02_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_03_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_03_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_04_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_04_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_05_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_05_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_06_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_06_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_07_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_07_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_08_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_08_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_09_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_09_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_10_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_10_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_11_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_11_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_12_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_12_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_13_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_13_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_14_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_14_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| IS_AXI_15_ACLK_INVERTED     | [0:0]   | 1'b0              |             |
| IS_AXI_15_ARESET_N_INVERTED | [0:0]   | 1'b0              |             |
| MC_ENABLE_0                 |         | "FALSE"           |             |
| MC_ENABLE_1                 |         | "FALSE"           |             |
| MC_ENABLE_2                 |         | "FALSE"           |             |
| MC_ENABLE_3                 |         | "FALSE"           |             |
| MC_ENABLE_4                 |         | "FALSE"           |             |
| MC_ENABLE_5                 |         | "FALSE"           |             |
| MC_ENABLE_6                 |         | "FALSE"           |             |
| MC_ENABLE_7                 |         | "FALSE"           |             |
| MC_ENABLE_APB               |         | "FALSE"           |             |
| PAGEHIT_PERCENT_00          | integer | 75                |             |
| PHY_ENABLE_00               |         | "FALSE"           |             |
| PHY_ENABLE_01               |         | "FALSE"           |             |
| PHY_ENABLE_02               |         | "FALSE"           |             |
| PHY_ENABLE_03               |         | "FALSE"           |             |
| PHY_ENABLE_04               |         | "FALSE"           |             |
| PHY_ENABLE_05               |         | "FALSE"           |             |
| PHY_ENABLE_06               |         | "FALSE"           |             |
| PHY_ENABLE_07               |         | "FALSE"           |             |
| PHY_ENABLE_08               |         | "FALSE"           |             |
| PHY_ENABLE_09               |         | "FALSE"           |             |
| PHY_ENABLE_10               |         | "FALSE"           |             |
| PHY_ENABLE_11               |         | "FALSE"           |             |
| PHY_ENABLE_12               |         | "FALSE"           |             |
| PHY_ENABLE_13               |         | "FALSE"           |             |
| PHY_ENABLE_14               |         | "FALSE"           |             |
| PHY_ENABLE_15               |         | "FALSE"           |             |
| PHY_ENABLE_APB              |         | "FALSE"           |             |
| PHY_PCLK_INVERT_01          |         | "FALSE"           |             |
| READ_PERCENT_00             | integer | 50                |             |
| READ_PERCENT_01             | integer | 50                |             |
| READ_PERCENT_02             | integer | 50                |             |
| READ_PERCENT_03             | integer | 50                |             |
| READ_PERCENT_04             | integer | 50                |             |
| READ_PERCENT_05             | integer | 50                |             |
| READ_PERCENT_06             | integer | 50                |             |
| READ_PERCENT_07             | integer | 50                |             |
| READ_PERCENT_08             | integer | 50                |             |
| READ_PERCENT_09             | integer | 50                |             |
| READ_PERCENT_10             | integer | 50                |             |
| READ_PERCENT_11             | integer | 50                |             |
| READ_PERCENT_12             | integer | 50                |             |
| READ_PERCENT_13             | integer | 50                |             |
| READ_PERCENT_14             | integer | 50                |             |
| READ_PERCENT_15             | integer | 50                |             |
| SIM_DEVICE                  |         | "ULTRASCALE_PLUS" |             |
| STACK_LOCATION              | integer | 0                 |             |
| SWITCH_ENABLE               |         | "FALSE"           |             |
| WRITE_PERCENT_00            | integer | 50                |             |
| WRITE_PERCENT_01            | integer | 50                |             |
| WRITE_PERCENT_02            | integer | 50                |             |
| WRITE_PERCENT_03            | integer | 50                |             |
| WRITE_PERCENT_04            | integer | 50                |             |
| WRITE_PERCENT_05            | integer | 50                |             |
| WRITE_PERCENT_06            | integer | 50                |             |
| WRITE_PERCENT_07            | integer | 50                |             |
| WRITE_PERCENT_08            | integer | 50                |             |
| WRITE_PERCENT_09            | integer | 50                |             |
| WRITE_PERCENT_10            | integer | 50                |             |
| WRITE_PERCENT_11            | integer | 50                |             |
| WRITE_PERCENT_12            | integer | 50                |             |
| WRITE_PERCENT_13            | integer | 50                |             |
| WRITE_PERCENT_14            | integer | 50                |             |
| WRITE_PERCENT_15            | integer | 50                |             |
## Ports

| Port name                   | Direction | Type    | Description |
| --------------------------- | --------- | ------- | ----------- |
| APB_0_PRDATA                | output    | [31:0]  |             |
| APB_0_PREADY                | output    |         |             |
| APB_0_PSLVERR               | output    |         |             |
| AXI_00_ARREADY              | output    |         |             |
| AXI_00_AWREADY              | output    |         |             |
| AXI_00_BID                  | output    | [5:0]   |             |
| AXI_00_BRESP                | output    | [1:0]   |             |
| AXI_00_BVALID               | output    |         |             |
| AXI_00_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_00_DFI_CLK_BUF          | output    |         |             |
| AXI_00_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_00_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_00_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_00_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_00_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_00_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_00_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_00_DFI_RST_N_BUF        | output    |         |             |
| AXI_00_MC_STATUS            | output    | [5:0]   |             |
| AXI_00_PHY_STATUS           | output    | [7:0]   |             |
| AXI_00_RDATA                | output    | [255:0] |             |
| AXI_00_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_00_RID                  | output    | [5:0]   |             |
| AXI_00_RLAST                | output    |         |             |
| AXI_00_RRESP                | output    | [1:0]   |             |
| AXI_00_RVALID               | output    |         |             |
| AXI_00_WREADY               | output    |         |             |
| AXI_01_ARREADY              | output    |         |             |
| AXI_01_AWREADY              | output    |         |             |
| AXI_01_BID                  | output    | [5:0]   |             |
| AXI_01_BRESP                | output    | [1:0]   |             |
| AXI_01_BVALID               | output    |         |             |
| AXI_01_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_01_DFI_CLK_BUF          | output    |         |             |
| AXI_01_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_01_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_01_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_01_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_01_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_01_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_01_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_01_DFI_RST_N_BUF        | output    |         |             |
| AXI_01_RDATA                | output    | [255:0] |             |
| AXI_01_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_01_RID                  | output    | [5:0]   |             |
| AXI_01_RLAST                | output    |         |             |
| AXI_01_RRESP                | output    | [1:0]   |             |
| AXI_01_RVALID               | output    |         |             |
| AXI_01_WREADY               | output    |         |             |
| AXI_02_ARREADY              | output    |         |             |
| AXI_02_AWREADY              | output    |         |             |
| AXI_02_BID                  | output    | [5:0]   |             |
| AXI_02_BRESP                | output    | [1:0]   |             |
| AXI_02_BVALID               | output    |         |             |
| AXI_02_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_02_DFI_CLK_BUF          | output    |         |             |
| AXI_02_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_02_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_02_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_02_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_02_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_02_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_02_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_02_DFI_RST_N_BUF        | output    |         |             |
| AXI_02_MC_STATUS            | output    | [5:0]   |             |
| AXI_02_PHY_STATUS           | output    | [7:0]   |             |
| AXI_02_RDATA                | output    | [255:0] |             |
| AXI_02_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_02_RID                  | output    | [5:0]   |             |
| AXI_02_RLAST                | output    |         |             |
| AXI_02_RRESP                | output    | [1:0]   |             |
| AXI_02_RVALID               | output    |         |             |
| AXI_02_WREADY               | output    |         |             |
| AXI_03_ARREADY              | output    |         |             |
| AXI_03_AWREADY              | output    |         |             |
| AXI_03_BID                  | output    | [5:0]   |             |
| AXI_03_BRESP                | output    | [1:0]   |             |
| AXI_03_BVALID               | output    |         |             |
| AXI_03_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_03_DFI_CLK_BUF          | output    |         |             |
| AXI_03_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_03_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_03_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_03_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_03_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_03_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_03_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_03_DFI_RST_N_BUF        | output    |         |             |
| AXI_03_RDATA                | output    | [255:0] |             |
| AXI_03_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_03_RID                  | output    | [5:0]   |             |
| AXI_03_RLAST                | output    |         |             |
| AXI_03_RRESP                | output    | [1:0]   |             |
| AXI_03_RVALID               | output    |         |             |
| AXI_03_WREADY               | output    |         |             |
| AXI_04_ARREADY              | output    |         |             |
| AXI_04_AWREADY              | output    |         |             |
| AXI_04_BID                  | output    | [5:0]   |             |
| AXI_04_BRESP                | output    | [1:0]   |             |
| AXI_04_BVALID               | output    |         |             |
| AXI_04_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_04_DFI_CLK_BUF          | output    |         |             |
| AXI_04_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_04_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_04_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_04_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_04_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_04_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_04_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_04_DFI_RST_N_BUF        | output    |         |             |
| AXI_04_MC_STATUS            | output    | [5:0]   |             |
| AXI_04_PHY_STATUS           | output    | [7:0]   |             |
| AXI_04_RDATA                | output    | [255:0] |             |
| AXI_04_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_04_RID                  | output    | [5:0]   |             |
| AXI_04_RLAST                | output    |         |             |
| AXI_04_RRESP                | output    | [1:0]   |             |
| AXI_04_RVALID               | output    |         |             |
| AXI_04_WREADY               | output    |         |             |
| AXI_05_ARREADY              | output    |         |             |
| AXI_05_AWREADY              | output    |         |             |
| AXI_05_BID                  | output    | [5:0]   |             |
| AXI_05_BRESP                | output    | [1:0]   |             |
| AXI_05_BVALID               | output    |         |             |
| AXI_05_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_05_DFI_CLK_BUF          | output    |         |             |
| AXI_05_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_05_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_05_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_05_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_05_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_05_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_05_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_05_DFI_RST_N_BUF        | output    |         |             |
| AXI_05_RDATA                | output    | [255:0] |             |
| AXI_05_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_05_RID                  | output    | [5:0]   |             |
| AXI_05_RLAST                | output    |         |             |
| AXI_05_RRESP                | output    | [1:0]   |             |
| AXI_05_RVALID               | output    |         |             |
| AXI_05_WREADY               | output    |         |             |
| AXI_06_ARREADY              | output    |         |             |
| AXI_06_AWREADY              | output    |         |             |
| AXI_06_BID                  | output    | [5:0]   |             |
| AXI_06_BRESP                | output    | [1:0]   |             |
| AXI_06_BVALID               | output    |         |             |
| AXI_06_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_06_DFI_CLK_BUF          | output    |         |             |
| AXI_06_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_06_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_06_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_06_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_06_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_06_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_06_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_06_DFI_RST_N_BUF        | output    |         |             |
| AXI_06_MC_STATUS            | output    | [5:0]   |             |
| AXI_06_PHY_STATUS           | output    | [7:0]   |             |
| AXI_06_RDATA                | output    | [255:0] |             |
| AXI_06_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_06_RID                  | output    | [5:0]   |             |
| AXI_06_RLAST                | output    |         |             |
| AXI_06_RRESP                | output    | [1:0]   |             |
| AXI_06_RVALID               | output    |         |             |
| AXI_06_WREADY               | output    |         |             |
| AXI_07_ARREADY              | output    |         |             |
| AXI_07_AWREADY              | output    |         |             |
| AXI_07_BID                  | output    | [5:0]   |             |
| AXI_07_BRESP                | output    | [1:0]   |             |
| AXI_07_BVALID               | output    |         |             |
| AXI_07_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_07_DFI_CLK_BUF          | output    |         |             |
| AXI_07_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_07_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_07_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_07_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_07_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_07_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_07_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_07_DFI_RST_N_BUF        | output    |         |             |
| AXI_07_RDATA                | output    | [255:0] |             |
| AXI_07_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_07_RID                  | output    | [5:0]   |             |
| AXI_07_RLAST                | output    |         |             |
| AXI_07_RRESP                | output    | [1:0]   |             |
| AXI_07_RVALID               | output    |         |             |
| AXI_07_WREADY               | output    |         |             |
| AXI_08_ARREADY              | output    |         |             |
| AXI_08_AWREADY              | output    |         |             |
| AXI_08_BID                  | output    | [5:0]   |             |
| AXI_08_BRESP                | output    | [1:0]   |             |
| AXI_08_BVALID               | output    |         |             |
| AXI_08_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_08_DFI_CLK_BUF          | output    |         |             |
| AXI_08_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_08_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_08_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_08_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_08_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_08_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_08_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_08_DFI_RST_N_BUF        | output    |         |             |
| AXI_08_MC_STATUS            | output    | [5:0]   |             |
| AXI_08_PHY_STATUS           | output    | [7:0]   |             |
| AXI_08_RDATA                | output    | [255:0] |             |
| AXI_08_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_08_RID                  | output    | [5:0]   |             |
| AXI_08_RLAST                | output    |         |             |
| AXI_08_RRESP                | output    | [1:0]   |             |
| AXI_08_RVALID               | output    |         |             |
| AXI_08_WREADY               | output    |         |             |
| AXI_09_ARREADY              | output    |         |             |
| AXI_09_AWREADY              | output    |         |             |
| AXI_09_BID                  | output    | [5:0]   |             |
| AXI_09_BRESP                | output    | [1:0]   |             |
| AXI_09_BVALID               | output    |         |             |
| AXI_09_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_09_DFI_CLK_BUF          | output    |         |             |
| AXI_09_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_09_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_09_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_09_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_09_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_09_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_09_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_09_DFI_RST_N_BUF        | output    |         |             |
| AXI_09_RDATA                | output    | [255:0] |             |
| AXI_09_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_09_RID                  | output    | [5:0]   |             |
| AXI_09_RLAST                | output    |         |             |
| AXI_09_RRESP                | output    | [1:0]   |             |
| AXI_09_RVALID               | output    |         |             |
| AXI_09_WREADY               | output    |         |             |
| AXI_10_ARREADY              | output    |         |             |
| AXI_10_AWREADY              | output    |         |             |
| AXI_10_BID                  | output    | [5:0]   |             |
| AXI_10_BRESP                | output    | [1:0]   |             |
| AXI_10_BVALID               | output    |         |             |
| AXI_10_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_10_DFI_CLK_BUF          | output    |         |             |
| AXI_10_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_10_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_10_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_10_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_10_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_10_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_10_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_10_DFI_RST_N_BUF        | output    |         |             |
| AXI_10_MC_STATUS            | output    | [5:0]   |             |
| AXI_10_PHY_STATUS           | output    | [7:0]   |             |
| AXI_10_RDATA                | output    | [255:0] |             |
| AXI_10_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_10_RID                  | output    | [5:0]   |             |
| AXI_10_RLAST                | output    |         |             |
| AXI_10_RRESP                | output    | [1:0]   |             |
| AXI_10_RVALID               | output    |         |             |
| AXI_10_WREADY               | output    |         |             |
| AXI_11_ARREADY              | output    |         |             |
| AXI_11_AWREADY              | output    |         |             |
| AXI_11_BID                  | output    | [5:0]   |             |
| AXI_11_BRESP                | output    | [1:0]   |             |
| AXI_11_BVALID               | output    |         |             |
| AXI_11_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_11_DFI_CLK_BUF          | output    |         |             |
| AXI_11_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_11_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_11_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_11_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_11_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_11_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_11_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_11_DFI_RST_N_BUF        | output    |         |             |
| AXI_11_RDATA                | output    | [255:0] |             |
| AXI_11_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_11_RID                  | output    | [5:0]   |             |
| AXI_11_RLAST                | output    |         |             |
| AXI_11_RRESP                | output    | [1:0]   |             |
| AXI_11_RVALID               | output    |         |             |
| AXI_11_WREADY               | output    |         |             |
| AXI_12_ARREADY              | output    |         |             |
| AXI_12_AWREADY              | output    |         |             |
| AXI_12_BID                  | output    | [5:0]   |             |
| AXI_12_BRESP                | output    | [1:0]   |             |
| AXI_12_BVALID               | output    |         |             |
| AXI_12_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_12_DFI_CLK_BUF          | output    |         |             |
| AXI_12_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_12_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_12_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_12_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_12_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_12_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_12_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_12_DFI_RST_N_BUF        | output    |         |             |
| AXI_12_MC_STATUS            | output    | [5:0]   |             |
| AXI_12_PHY_STATUS           | output    | [7:0]   |             |
| AXI_12_RDATA                | output    | [255:0] |             |
| AXI_12_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_12_RID                  | output    | [5:0]   |             |
| AXI_12_RLAST                | output    |         |             |
| AXI_12_RRESP                | output    | [1:0]   |             |
| AXI_12_RVALID               | output    |         |             |
| AXI_12_WREADY               | output    |         |             |
| AXI_13_ARREADY              | output    |         |             |
| AXI_13_AWREADY              | output    |         |             |
| AXI_13_BID                  | output    | [5:0]   |             |
| AXI_13_BRESP                | output    | [1:0]   |             |
| AXI_13_BVALID               | output    |         |             |
| AXI_13_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_13_DFI_CLK_BUF          | output    |         |             |
| AXI_13_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_13_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_13_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_13_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_13_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_13_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_13_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_13_DFI_RST_N_BUF        | output    |         |             |
| AXI_13_RDATA                | output    | [255:0] |             |
| AXI_13_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_13_RID                  | output    | [5:0]   |             |
| AXI_13_RLAST                | output    |         |             |
| AXI_13_RRESP                | output    | [1:0]   |             |
| AXI_13_RVALID               | output    |         |             |
| AXI_13_WREADY               | output    |         |             |
| AXI_14_ARREADY              | output    |         |             |
| AXI_14_AWREADY              | output    |         |             |
| AXI_14_BID                  | output    | [5:0]   |             |
| AXI_14_BRESP                | output    | [1:0]   |             |
| AXI_14_BVALID               | output    |         |             |
| AXI_14_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_14_DFI_CLK_BUF          | output    |         |             |
| AXI_14_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_14_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_14_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_14_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_14_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_14_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_14_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_14_DFI_RST_N_BUF        | output    |         |             |
| AXI_14_MC_STATUS            | output    | [5:0]   |             |
| AXI_14_PHY_STATUS           | output    | [7:0]   |             |
| AXI_14_RDATA                | output    | [255:0] |             |
| AXI_14_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_14_RID                  | output    | [5:0]   |             |
| AXI_14_RLAST                | output    |         |             |
| AXI_14_RRESP                | output    | [1:0]   |             |
| AXI_14_RVALID               | output    |         |             |
| AXI_14_WREADY               | output    |         |             |
| AXI_15_ARREADY              | output    |         |             |
| AXI_15_AWREADY              | output    |         |             |
| AXI_15_BID                  | output    | [5:0]   |             |
| AXI_15_BRESP                | output    | [1:0]   |             |
| AXI_15_BVALID               | output    |         |             |
| AXI_15_DFI_AW_AERR_N        | output    | [1:0]   |             |
| AXI_15_DFI_CLK_BUF          | output    |         |             |
| AXI_15_DFI_DBI_BYTE_DISABLE | output    | [7:0]   |             |
| AXI_15_DFI_DW_RDDATA_DBI    | output    | [20:0]  |             |
| AXI_15_DFI_DW_RDDATA_DERR   | output    | [7:0]   |             |
| AXI_15_DFI_DW_RDDATA_VALID  | output    | [1:0]   |             |
| AXI_15_DFI_INIT_COMPLETE    | output    |         |             |
| AXI_15_DFI_PHYUPD_REQ       | output    |         |             |
| AXI_15_DFI_PHY_LP_STATE     | output    |         |             |
| AXI_15_DFI_RST_N_BUF        | output    |         |             |
| AXI_15_RDATA                | output    | [255:0] |             |
| AXI_15_RDATA_PARITY         | output    | [31:0]  |             |
| AXI_15_RID                  | output    | [5:0]   |             |
| AXI_15_RLAST                | output    |         |             |
| AXI_15_RRESP                | output    | [1:0]   |             |
| AXI_15_RVALID               | output    |         |             |
| AXI_15_WREADY               | output    |         |             |
| DRAM_0_STAT_CATTRIP         | output    |         |             |
| DRAM_0_STAT_TEMP            | output    | [2:0]   |             |
| APB_0_PADDR                 | input     | [21:0]  |             |
| APB_0_PCLK                  | input     |         |             |
| APB_0_PENABLE               | input     |         |             |
| APB_0_PRESET_N              | input     |         |             |
| APB_0_PSEL                  | input     |         |             |
| APB_0_PWDATA                | input     | [31:0]  |             |
| APB_0_PWRITE                | input     |         |             |
| AXI_00_ACLK                 | input     |         |             |
| AXI_00_ARADDR               | input     | [36:0]  |             |
| AXI_00_ARBURST              | input     | [1:0]   |             |
| AXI_00_ARESET_N             | input     |         |             |
| AXI_00_ARID                 | input     | [5:0]   |             |
| AXI_00_ARLEN                | input     | [3:0]   |             |
| AXI_00_ARSIZE               | input     | [2:0]   |             |
| AXI_00_ARVALID              | input     |         |             |
| AXI_00_AWADDR               | input     | [36:0]  |             |
| AXI_00_AWBURST              | input     | [1:0]   |             |
| AXI_00_AWID                 | input     | [5:0]   |             |
| AXI_00_AWLEN                | input     | [3:0]   |             |
| AXI_00_AWSIZE               | input     | [2:0]   |             |
| AXI_00_AWVALID              | input     |         |             |
| AXI_00_BREADY               | input     |         |             |
| AXI_00_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_00_RREADY               | input     |         |             |
| AXI_00_WDATA                | input     | [255:0] |             |
| AXI_00_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_00_WLAST                | input     |         |             |
| AXI_00_WSTRB                | input     | [31:0]  |             |
| AXI_00_WVALID               | input     |         |             |
| AXI_01_ACLK                 | input     |         |             |
| AXI_01_ARADDR               | input     | [36:0]  |             |
| AXI_01_ARBURST              | input     | [1:0]   |             |
| AXI_01_ARESET_N             | input     |         |             |
| AXI_01_ARID                 | input     | [5:0]   |             |
| AXI_01_ARLEN                | input     | [3:0]   |             |
| AXI_01_ARSIZE               | input     | [2:0]   |             |
| AXI_01_ARVALID              | input     |         |             |
| AXI_01_AWADDR               | input     | [36:0]  |             |
| AXI_01_AWBURST              | input     | [1:0]   |             |
| AXI_01_AWID                 | input     | [5:0]   |             |
| AXI_01_AWLEN                | input     | [3:0]   |             |
| AXI_01_AWSIZE               | input     | [2:0]   |             |
| AXI_01_AWVALID              | input     |         |             |
| AXI_01_BREADY               | input     |         |             |
| AXI_01_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_01_RREADY               | input     |         |             |
| AXI_01_WDATA                | input     | [255:0] |             |
| AXI_01_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_01_WLAST                | input     |         |             |
| AXI_01_WSTRB                | input     | [31:0]  |             |
| AXI_01_WVALID               | input     |         |             |
| AXI_02_ACLK                 | input     |         |             |
| AXI_02_ARADDR               | input     | [36:0]  |             |
| AXI_02_ARBURST              | input     | [1:0]   |             |
| AXI_02_ARESET_N             | input     |         |             |
| AXI_02_ARID                 | input     | [5:0]   |             |
| AXI_02_ARLEN                | input     | [3:0]   |             |
| AXI_02_ARSIZE               | input     | [2:0]   |             |
| AXI_02_ARVALID              | input     |         |             |
| AXI_02_AWADDR               | input     | [36:0]  |             |
| AXI_02_AWBURST              | input     | [1:0]   |             |
| AXI_02_AWID                 | input     | [5:0]   |             |
| AXI_02_AWLEN                | input     | [3:0]   |             |
| AXI_02_AWSIZE               | input     | [2:0]   |             |
| AXI_02_AWVALID              | input     |         |             |
| AXI_02_BREADY               | input     |         |             |
| AXI_02_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_02_RREADY               | input     |         |             |
| AXI_02_WDATA                | input     | [255:0] |             |
| AXI_02_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_02_WLAST                | input     |         |             |
| AXI_02_WSTRB                | input     | [31:0]  |             |
| AXI_02_WVALID               | input     |         |             |
| AXI_03_ACLK                 | input     |         |             |
| AXI_03_ARADDR               | input     | [36:0]  |             |
| AXI_03_ARBURST              | input     | [1:0]   |             |
| AXI_03_ARESET_N             | input     |         |             |
| AXI_03_ARID                 | input     | [5:0]   |             |
| AXI_03_ARLEN                | input     | [3:0]   |             |
| AXI_03_ARSIZE               | input     | [2:0]   |             |
| AXI_03_ARVALID              | input     |         |             |
| AXI_03_AWADDR               | input     | [36:0]  |             |
| AXI_03_AWBURST              | input     | [1:0]   |             |
| AXI_03_AWID                 | input     | [5:0]   |             |
| AXI_03_AWLEN                | input     | [3:0]   |             |
| AXI_03_AWSIZE               | input     | [2:0]   |             |
| AXI_03_AWVALID              | input     |         |             |
| AXI_03_BREADY               | input     |         |             |
| AXI_03_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_03_RREADY               | input     |         |             |
| AXI_03_WDATA                | input     | [255:0] |             |
| AXI_03_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_03_WLAST                | input     |         |             |
| AXI_03_WSTRB                | input     | [31:0]  |             |
| AXI_03_WVALID               | input     |         |             |
| AXI_04_ACLK                 | input     |         |             |
| AXI_04_ARADDR               | input     | [36:0]  |             |
| AXI_04_ARBURST              | input     | [1:0]   |             |
| AXI_04_ARESET_N             | input     |         |             |
| AXI_04_ARID                 | input     | [5:0]   |             |
| AXI_04_ARLEN                | input     | [3:0]   |             |
| AXI_04_ARSIZE               | input     | [2:0]   |             |
| AXI_04_ARVALID              | input     |         |             |
| AXI_04_AWADDR               | input     | [36:0]  |             |
| AXI_04_AWBURST              | input     | [1:0]   |             |
| AXI_04_AWID                 | input     | [5:0]   |             |
| AXI_04_AWLEN                | input     | [3:0]   |             |
| AXI_04_AWSIZE               | input     | [2:0]   |             |
| AXI_04_AWVALID              | input     |         |             |
| AXI_04_BREADY               | input     |         |             |
| AXI_04_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_04_RREADY               | input     |         |             |
| AXI_04_WDATA                | input     | [255:0] |             |
| AXI_04_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_04_WLAST                | input     |         |             |
| AXI_04_WSTRB                | input     | [31:0]  |             |
| AXI_04_WVALID               | input     |         |             |
| AXI_05_ACLK                 | input     |         |             |
| AXI_05_ARADDR               | input     | [36:0]  |             |
| AXI_05_ARBURST              | input     | [1:0]   |             |
| AXI_05_ARESET_N             | input     |         |             |
| AXI_05_ARID                 | input     | [5:0]   |             |
| AXI_05_ARLEN                | input     | [3:0]   |             |
| AXI_05_ARSIZE               | input     | [2:0]   |             |
| AXI_05_ARVALID              | input     |         |             |
| AXI_05_AWADDR               | input     | [36:0]  |             |
| AXI_05_AWBURST              | input     | [1:0]   |             |
| AXI_05_AWID                 | input     | [5:0]   |             |
| AXI_05_AWLEN                | input     | [3:0]   |             |
| AXI_05_AWSIZE               | input     | [2:0]   |             |
| AXI_05_AWVALID              | input     |         |             |
| AXI_05_BREADY               | input     |         |             |
| AXI_05_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_05_RREADY               | input     |         |             |
| AXI_05_WDATA                | input     | [255:0] |             |
| AXI_05_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_05_WLAST                | input     |         |             |
| AXI_05_WSTRB                | input     | [31:0]  |             |
| AXI_05_WVALID               | input     |         |             |
| AXI_06_ACLK                 | input     |         |             |
| AXI_06_ARADDR               | input     | [36:0]  |             |
| AXI_06_ARBURST              | input     | [1:0]   |             |
| AXI_06_ARESET_N             | input     |         |             |
| AXI_06_ARID                 | input     | [5:0]   |             |
| AXI_06_ARLEN                | input     | [3:0]   |             |
| AXI_06_ARSIZE               | input     | [2:0]   |             |
| AXI_06_ARVALID              | input     |         |             |
| AXI_06_AWADDR               | input     | [36:0]  |             |
| AXI_06_AWBURST              | input     | [1:0]   |             |
| AXI_06_AWID                 | input     | [5:0]   |             |
| AXI_06_AWLEN                | input     | [3:0]   |             |
| AXI_06_AWSIZE               | input     | [2:0]   |             |
| AXI_06_AWVALID              | input     |         |             |
| AXI_06_BREADY               | input     |         |             |
| AXI_06_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_06_RREADY               | input     |         |             |
| AXI_06_WDATA                | input     | [255:0] |             |
| AXI_06_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_06_WLAST                | input     |         |             |
| AXI_06_WSTRB                | input     | [31:0]  |             |
| AXI_06_WVALID               | input     |         |             |
| AXI_07_ACLK                 | input     |         |             |
| AXI_07_ARADDR               | input     | [36:0]  |             |
| AXI_07_ARBURST              | input     | [1:0]   |             |
| AXI_07_ARESET_N             | input     |         |             |
| AXI_07_ARID                 | input     | [5:0]   |             |
| AXI_07_ARLEN                | input     | [3:0]   |             |
| AXI_07_ARSIZE               | input     | [2:0]   |             |
| AXI_07_ARVALID              | input     |         |             |
| AXI_07_AWADDR               | input     | [36:0]  |             |
| AXI_07_AWBURST              | input     | [1:0]   |             |
| AXI_07_AWID                 | input     | [5:0]   |             |
| AXI_07_AWLEN                | input     | [3:0]   |             |
| AXI_07_AWSIZE               | input     | [2:0]   |             |
| AXI_07_AWVALID              | input     |         |             |
| AXI_07_BREADY               | input     |         |             |
| AXI_07_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_07_RREADY               | input     |         |             |
| AXI_07_WDATA                | input     | [255:0] |             |
| AXI_07_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_07_WLAST                | input     |         |             |
| AXI_07_WSTRB                | input     | [31:0]  |             |
| AXI_07_WVALID               | input     |         |             |
| AXI_08_ACLK                 | input     |         |             |
| AXI_08_ARADDR               | input     | [36:0]  |             |
| AXI_08_ARBURST              | input     | [1:0]   |             |
| AXI_08_ARESET_N             | input     |         |             |
| AXI_08_ARID                 | input     | [5:0]   |             |
| AXI_08_ARLEN                | input     | [3:0]   |             |
| AXI_08_ARSIZE               | input     | [2:0]   |             |
| AXI_08_ARVALID              | input     |         |             |
| AXI_08_AWADDR               | input     | [36:0]  |             |
| AXI_08_AWBURST              | input     | [1:0]   |             |
| AXI_08_AWID                 | input     | [5:0]   |             |
| AXI_08_AWLEN                | input     | [3:0]   |             |
| AXI_08_AWSIZE               | input     | [2:0]   |             |
| AXI_08_AWVALID              | input     |         |             |
| AXI_08_BREADY               | input     |         |             |
| AXI_08_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_08_RREADY               | input     |         |             |
| AXI_08_WDATA                | input     | [255:0] |             |
| AXI_08_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_08_WLAST                | input     |         |             |
| AXI_08_WSTRB                | input     | [31:0]  |             |
| AXI_08_WVALID               | input     |         |             |
| AXI_09_ACLK                 | input     |         |             |
| AXI_09_ARADDR               | input     | [36:0]  |             |
| AXI_09_ARBURST              | input     | [1:0]   |             |
| AXI_09_ARESET_N             | input     |         |             |
| AXI_09_ARID                 | input     | [5:0]   |             |
| AXI_09_ARLEN                | input     | [3:0]   |             |
| AXI_09_ARSIZE               | input     | [2:0]   |             |
| AXI_09_ARVALID              | input     |         |             |
| AXI_09_AWADDR               | input     | [36:0]  |             |
| AXI_09_AWBURST              | input     | [1:0]   |             |
| AXI_09_AWID                 | input     | [5:0]   |             |
| AXI_09_AWLEN                | input     | [3:0]   |             |
| AXI_09_AWSIZE               | input     | [2:0]   |             |
| AXI_09_AWVALID              | input     |         |             |
| AXI_09_BREADY               | input     |         |             |
| AXI_09_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_09_RREADY               | input     |         |             |
| AXI_09_WDATA                | input     | [255:0] |             |
| AXI_09_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_09_WLAST                | input     |         |             |
| AXI_09_WSTRB                | input     | [31:0]  |             |
| AXI_09_WVALID               | input     |         |             |
| AXI_10_ACLK                 | input     |         |             |
| AXI_10_ARADDR               | input     | [36:0]  |             |
| AXI_10_ARBURST              | input     | [1:0]   |             |
| AXI_10_ARESET_N             | input     |         |             |
| AXI_10_ARID                 | input     | [5:0]   |             |
| AXI_10_ARLEN                | input     | [3:0]   |             |
| AXI_10_ARSIZE               | input     | [2:0]   |             |
| AXI_10_ARVALID              | input     |         |             |
| AXI_10_AWADDR               | input     | [36:0]  |             |
| AXI_10_AWBURST              | input     | [1:0]   |             |
| AXI_10_AWID                 | input     | [5:0]   |             |
| AXI_10_AWLEN                | input     | [3:0]   |             |
| AXI_10_AWSIZE               | input     | [2:0]   |             |
| AXI_10_AWVALID              | input     |         |             |
| AXI_10_BREADY               | input     |         |             |
| AXI_10_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_10_RREADY               | input     |         |             |
| AXI_10_WDATA                | input     | [255:0] |             |
| AXI_10_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_10_WLAST                | input     |         |             |
| AXI_10_WSTRB                | input     | [31:0]  |             |
| AXI_10_WVALID               | input     |         |             |
| AXI_11_ACLK                 | input     |         |             |
| AXI_11_ARADDR               | input     | [36:0]  |             |
| AXI_11_ARBURST              | input     | [1:0]   |             |
| AXI_11_ARESET_N             | input     |         |             |
| AXI_11_ARID                 | input     | [5:0]   |             |
| AXI_11_ARLEN                | input     | [3:0]   |             |
| AXI_11_ARSIZE               | input     | [2:0]   |             |
| AXI_11_ARVALID              | input     |         |             |
| AXI_11_AWADDR               | input     | [36:0]  |             |
| AXI_11_AWBURST              | input     | [1:0]   |             |
| AXI_11_AWID                 | input     | [5:0]   |             |
| AXI_11_AWLEN                | input     | [3:0]   |             |
| AXI_11_AWSIZE               | input     | [2:0]   |             |
| AXI_11_AWVALID              | input     |         |             |
| AXI_11_BREADY               | input     |         |             |
| AXI_11_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_11_RREADY               | input     |         |             |
| AXI_11_WDATA                | input     | [255:0] |             |
| AXI_11_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_11_WLAST                | input     |         |             |
| AXI_11_WSTRB                | input     | [31:0]  |             |
| AXI_11_WVALID               | input     |         |             |
| AXI_12_ACLK                 | input     |         |             |
| AXI_12_ARADDR               | input     | [36:0]  |             |
| AXI_12_ARBURST              | input     | [1:0]   |             |
| AXI_12_ARESET_N             | input     |         |             |
| AXI_12_ARID                 | input     | [5:0]   |             |
| AXI_12_ARLEN                | input     | [3:0]   |             |
| AXI_12_ARSIZE               | input     | [2:0]   |             |
| AXI_12_ARVALID              | input     |         |             |
| AXI_12_AWADDR               | input     | [36:0]  |             |
| AXI_12_AWBURST              | input     | [1:0]   |             |
| AXI_12_AWID                 | input     | [5:0]   |             |
| AXI_12_AWLEN                | input     | [3:0]   |             |
| AXI_12_AWSIZE               | input     | [2:0]   |             |
| AXI_12_AWVALID              | input     |         |             |
| AXI_12_BREADY               | input     |         |             |
| AXI_12_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_12_RREADY               | input     |         |             |
| AXI_12_WDATA                | input     | [255:0] |             |
| AXI_12_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_12_WLAST                | input     |         |             |
| AXI_12_WSTRB                | input     | [31:0]  |             |
| AXI_12_WVALID               | input     |         |             |
| AXI_13_ACLK                 | input     |         |             |
| AXI_13_ARADDR               | input     | [36:0]  |             |
| AXI_13_ARBURST              | input     | [1:0]   |             |
| AXI_13_ARESET_N             | input     |         |             |
| AXI_13_ARID                 | input     | [5:0]   |             |
| AXI_13_ARLEN                | input     | [3:0]   |             |
| AXI_13_ARSIZE               | input     | [2:0]   |             |
| AXI_13_ARVALID              | input     |         |             |
| AXI_13_AWADDR               | input     | [36:0]  |             |
| AXI_13_AWBURST              | input     | [1:0]   |             |
| AXI_13_AWID                 | input     | [5:0]   |             |
| AXI_13_AWLEN                | input     | [3:0]   |             |
| AXI_13_AWSIZE               | input     | [2:0]   |             |
| AXI_13_AWVALID              | input     |         |             |
| AXI_13_BREADY               | input     |         |             |
| AXI_13_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_13_RREADY               | input     |         |             |
| AXI_13_WDATA                | input     | [255:0] |             |
| AXI_13_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_13_WLAST                | input     |         |             |
| AXI_13_WSTRB                | input     | [31:0]  |             |
| AXI_13_WVALID               | input     |         |             |
| AXI_14_ACLK                 | input     |         |             |
| AXI_14_ARADDR               | input     | [36:0]  |             |
| AXI_14_ARBURST              | input     | [1:0]   |             |
| AXI_14_ARESET_N             | input     |         |             |
| AXI_14_ARID                 | input     | [5:0]   |             |
| AXI_14_ARLEN                | input     | [3:0]   |             |
| AXI_14_ARSIZE               | input     | [2:0]   |             |
| AXI_14_ARVALID              | input     |         |             |
| AXI_14_AWADDR               | input     | [36:0]  |             |
| AXI_14_AWBURST              | input     | [1:0]   |             |
| AXI_14_AWID                 | input     | [5:0]   |             |
| AXI_14_AWLEN                | input     | [3:0]   |             |
| AXI_14_AWSIZE               | input     | [2:0]   |             |
| AXI_14_AWVALID              | input     |         |             |
| AXI_14_BREADY               | input     |         |             |
| AXI_14_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_14_RREADY               | input     |         |             |
| AXI_14_WDATA                | input     | [255:0] |             |
| AXI_14_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_14_WLAST                | input     |         |             |
| AXI_14_WSTRB                | input     | [31:0]  |             |
| AXI_14_WVALID               | input     |         |             |
| AXI_15_ACLK                 | input     |         |             |
| AXI_15_ARADDR               | input     | [36:0]  |             |
| AXI_15_ARBURST              | input     | [1:0]   |             |
| AXI_15_ARESET_N             | input     |         |             |
| AXI_15_ARID                 | input     | [5:0]   |             |
| AXI_15_ARLEN                | input     | [3:0]   |             |
| AXI_15_ARSIZE               | input     | [2:0]   |             |
| AXI_15_ARVALID              | input     |         |             |
| AXI_15_AWADDR               | input     | [36:0]  |             |
| AXI_15_AWBURST              | input     | [1:0]   |             |
| AXI_15_AWID                 | input     | [5:0]   |             |
| AXI_15_AWLEN                | input     | [3:0]   |             |
| AXI_15_AWSIZE               | input     | [2:0]   |             |
| AXI_15_AWVALID              | input     |         |             |
| AXI_15_BREADY               | input     |         |             |
| AXI_15_DFI_LP_PWR_X_REQ     | input     |         |             |
| AXI_15_RREADY               | input     |         |             |
| AXI_15_WDATA                | input     | [255:0] |             |
| AXI_15_WDATA_PARITY         | input     | [31:0]  |             |
| AXI_15_WLAST                | input     |         |             |
| AXI_15_WSTRB                | input     | [31:0]  |             |
| AXI_15_WVALID               | input     |         |             |
| BSCAN_DRCK                  | input     |         |             |
| BSCAN_TCK                   | input     |         |             |
| HBM_REF_CLK                 | input     |         |             |
| MBIST_EN_00                 | input     |         |             |
| MBIST_EN_01                 | input     |         |             |
| MBIST_EN_02                 | input     |         |             |
| MBIST_EN_03                 | input     |         |             |
| MBIST_EN_04                 | input     |         |             |
| MBIST_EN_05                 | input     |         |             |
| MBIST_EN_06                 | input     |         |             |
| MBIST_EN_07                 | input     |         |             |
## Signals

| Name                            | Type         | Description |
| ------------------------------- | ------------ | ----------- |
| trig_attr                       | reg          |             |
| PHY_PCLK_INVERT_01_BIN          | wire         |             |
| PHY_PCLK_INVERT_01_BIN          | reg          |             |
| attr_test                       | reg          |             |
| attr_err                        | reg          |             |
| glblGSR                         | tri0         |             |
| APB_0_PREADY_out                | wire         |             |
| APB_0_PSLVERR_out               | wire         |             |
| AXI_00_ARREADY_out              | wire         |             |
| AXI_00_AWREADY_out              | wire         |             |
| AXI_00_BVALID_out               | wire         |             |
| AXI_00_DFI_CLK_BUF_out          | wire         |             |
| AXI_00_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_00_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_00_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_00_DFI_RST_N_BUF_out        | wire         |             |
| AXI_00_RLAST_out                | wire         |             |
| AXI_00_RVALID_out               | wire         |             |
| AXI_00_WREADY_out               | wire         |             |
| AXI_01_ARREADY_out              | wire         |             |
| AXI_01_AWREADY_out              | wire         |             |
| AXI_01_BVALID_out               | wire         |             |
| AXI_01_DFI_CLK_BUF_out          | wire         |             |
| AXI_01_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_01_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_01_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_01_DFI_RST_N_BUF_out        | wire         |             |
| AXI_01_RLAST_out                | wire         |             |
| AXI_01_RVALID_out               | wire         |             |
| AXI_01_WREADY_out               | wire         |             |
| AXI_02_ARREADY_out              | wire         |             |
| AXI_02_AWREADY_out              | wire         |             |
| AXI_02_BVALID_out               | wire         |             |
| AXI_02_DFI_CLK_BUF_out          | wire         |             |
| AXI_02_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_02_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_02_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_02_DFI_RST_N_BUF_out        | wire         |             |
| AXI_02_RLAST_out                | wire         |             |
| AXI_02_RVALID_out               | wire         |             |
| AXI_02_WREADY_out               | wire         |             |
| AXI_03_ARREADY_out              | wire         |             |
| AXI_03_AWREADY_out              | wire         |             |
| AXI_03_BVALID_out               | wire         |             |
| AXI_03_DFI_CLK_BUF_out          | wire         |             |
| AXI_03_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_03_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_03_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_03_DFI_RST_N_BUF_out        | wire         |             |
| AXI_03_RLAST_out                | wire         |             |
| AXI_03_RVALID_out               | wire         |             |
| AXI_03_WREADY_out               | wire         |             |
| AXI_04_ARREADY_out              | wire         |             |
| AXI_04_AWREADY_out              | wire         |             |
| AXI_04_BVALID_out               | wire         |             |
| AXI_04_DFI_CLK_BUF_out          | wire         |             |
| AXI_04_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_04_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_04_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_04_DFI_RST_N_BUF_out        | wire         |             |
| AXI_04_RLAST_out                | wire         |             |
| AXI_04_RVALID_out               | wire         |             |
| AXI_04_WREADY_out               | wire         |             |
| AXI_05_ARREADY_out              | wire         |             |
| AXI_05_AWREADY_out              | wire         |             |
| AXI_05_BVALID_out               | wire         |             |
| AXI_05_DFI_CLK_BUF_out          | wire         |             |
| AXI_05_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_05_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_05_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_05_DFI_RST_N_BUF_out        | wire         |             |
| AXI_05_RLAST_out                | wire         |             |
| AXI_05_RVALID_out               | wire         |             |
| AXI_05_WREADY_out               | wire         |             |
| AXI_06_ARREADY_out              | wire         |             |
| AXI_06_AWREADY_out              | wire         |             |
| AXI_06_BVALID_out               | wire         |             |
| AXI_06_DFI_CLK_BUF_out          | wire         |             |
| AXI_06_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_06_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_06_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_06_DFI_RST_N_BUF_out        | wire         |             |
| AXI_06_RLAST_out                | wire         |             |
| AXI_06_RVALID_out               | wire         |             |
| AXI_06_WREADY_out               | wire         |             |
| AXI_07_ARREADY_out              | wire         |             |
| AXI_07_AWREADY_out              | wire         |             |
| AXI_07_BVALID_out               | wire         |             |
| AXI_07_DFI_CLK_BUF_out          | wire         |             |
| AXI_07_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_07_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_07_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_07_DFI_RST_N_BUF_out        | wire         |             |
| AXI_07_RLAST_out                | wire         |             |
| AXI_07_RVALID_out               | wire         |             |
| AXI_07_WREADY_out               | wire         |             |
| AXI_08_ARREADY_out              | wire         |             |
| AXI_08_AWREADY_out              | wire         |             |
| AXI_08_BVALID_out               | wire         |             |
| AXI_08_DFI_CLK_BUF_out          | wire         |             |
| AXI_08_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_08_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_08_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_08_DFI_RST_N_BUF_out        | wire         |             |
| AXI_08_RLAST_out                | wire         |             |
| AXI_08_RVALID_out               | wire         |             |
| AXI_08_WREADY_out               | wire         |             |
| AXI_09_ARREADY_out              | wire         |             |
| AXI_09_AWREADY_out              | wire         |             |
| AXI_09_BVALID_out               | wire         |             |
| AXI_09_DFI_CLK_BUF_out          | wire         |             |
| AXI_09_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_09_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_09_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_09_DFI_RST_N_BUF_out        | wire         |             |
| AXI_09_RLAST_out                | wire         |             |
| AXI_09_RVALID_out               | wire         |             |
| AXI_09_WREADY_out               | wire         |             |
| AXI_10_ARREADY_out              | wire         |             |
| AXI_10_AWREADY_out              | wire         |             |
| AXI_10_BVALID_out               | wire         |             |
| AXI_10_DFI_CLK_BUF_out          | wire         |             |
| AXI_10_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_10_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_10_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_10_DFI_RST_N_BUF_out        | wire         |             |
| AXI_10_RLAST_out                | wire         |             |
| AXI_10_RVALID_out               | wire         |             |
| AXI_10_WREADY_out               | wire         |             |
| AXI_11_ARREADY_out              | wire         |             |
| AXI_11_AWREADY_out              | wire         |             |
| AXI_11_BVALID_out               | wire         |             |
| AXI_11_DFI_CLK_BUF_out          | wire         |             |
| AXI_11_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_11_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_11_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_11_DFI_RST_N_BUF_out        | wire         |             |
| AXI_11_RLAST_out                | wire         |             |
| AXI_11_RVALID_out               | wire         |             |
| AXI_11_WREADY_out               | wire         |             |
| AXI_12_ARREADY_out              | wire         |             |
| AXI_12_AWREADY_out              | wire         |             |
| AXI_12_BVALID_out               | wire         |             |
| AXI_12_DFI_CLK_BUF_out          | wire         |             |
| AXI_12_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_12_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_12_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_12_DFI_RST_N_BUF_out        | wire         |             |
| AXI_12_RLAST_out                | wire         |             |
| AXI_12_RVALID_out               | wire         |             |
| AXI_12_WREADY_out               | wire         |             |
| AXI_13_ARREADY_out              | wire         |             |
| AXI_13_AWREADY_out              | wire         |             |
| AXI_13_BVALID_out               | wire         |             |
| AXI_13_DFI_CLK_BUF_out          | wire         |             |
| AXI_13_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_13_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_13_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_13_DFI_RST_N_BUF_out        | wire         |             |
| AXI_13_RLAST_out                | wire         |             |
| AXI_13_RVALID_out               | wire         |             |
| AXI_13_WREADY_out               | wire         |             |
| AXI_14_ARREADY_out              | wire         |             |
| AXI_14_AWREADY_out              | wire         |             |
| AXI_14_BVALID_out               | wire         |             |
| AXI_14_DFI_CLK_BUF_out          | wire         |             |
| AXI_14_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_14_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_14_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_14_DFI_RST_N_BUF_out        | wire         |             |
| AXI_14_RLAST_out                | wire         |             |
| AXI_14_RVALID_out               | wire         |             |
| AXI_14_WREADY_out               | wire         |             |
| AXI_15_ARREADY_out              | wire         |             |
| AXI_15_AWREADY_out              | wire         |             |
| AXI_15_BVALID_out               | wire         |             |
| AXI_15_DFI_CLK_BUF_out          | wire         |             |
| AXI_15_DFI_INIT_COMPLETE_out    | wire         |             |
| AXI_15_DFI_PHYUPD_REQ_out       | wire         |             |
| AXI_15_DFI_PHY_LP_STATE_out     | wire         |             |
| AXI_15_DFI_RST_N_BUF_out        | wire         |             |
| AXI_15_RLAST_out                | wire         |             |
| AXI_15_RVALID_out               | wire         |             |
| AXI_15_WREADY_out               | wire         |             |
| DRAM_0_STAT_CATTRIP_out         | wire         |             |
| DBG_OUT_00_out                  | wire [17:0]  |             |
| DBG_OUT_01_out                  | wire [17:0]  |             |
| DBG_OUT_02_out                  | wire [17:0]  |             |
| DBG_OUT_03_out                  | wire [17:0]  |             |
| DBG_OUT_04_out                  | wire [17:0]  |             |
| DBG_OUT_05_out                  | wire [17:0]  |             |
| DBG_OUT_06_out                  | wire [17:0]  |             |
| DBG_OUT_07_out                  | wire [17:0]  |             |
| DBG_OUT_08_out                  | wire [17:0]  |             |
| DBG_OUT_09_out                  | wire [17:0]  |             |
| DBG_OUT_10_out                  | wire [17:0]  |             |
| DBG_OUT_11_out                  | wire [17:0]  |             |
| DBG_OUT_12_out                  | wire [17:0]  |             |
| DBG_OUT_13_out                  | wire [17:0]  |             |
| DBG_OUT_14_out                  | wire [17:0]  |             |
| DBG_OUT_15_out                  | wire [17:0]  |             |
| AXI_00_BRESP_out                | wire [1:0]   |             |
| AXI_00_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_00_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_00_RRESP_out                | wire [1:0]   |             |
| AXI_01_BRESP_out                | wire [1:0]   |             |
| AXI_01_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_01_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_01_RRESP_out                | wire [1:0]   |             |
| AXI_02_BRESP_out                | wire [1:0]   |             |
| AXI_02_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_02_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_02_RRESP_out                | wire [1:0]   |             |
| AXI_03_BRESP_out                | wire [1:0]   |             |
| AXI_03_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_03_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_03_RRESP_out                | wire [1:0]   |             |
| AXI_04_BRESP_out                | wire [1:0]   |             |
| AXI_04_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_04_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_04_RRESP_out                | wire [1:0]   |             |
| AXI_05_BRESP_out                | wire [1:0]   |             |
| AXI_05_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_05_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_05_RRESP_out                | wire [1:0]   |             |
| AXI_06_BRESP_out                | wire [1:0]   |             |
| AXI_06_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_06_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_06_RRESP_out                | wire [1:0]   |             |
| AXI_07_BRESP_out                | wire [1:0]   |             |
| AXI_07_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_07_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_07_RRESP_out                | wire [1:0]   |             |
| AXI_08_BRESP_out                | wire [1:0]   |             |
| AXI_08_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_08_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_08_RRESP_out                | wire [1:0]   |             |
| AXI_09_BRESP_out                | wire [1:0]   |             |
| AXI_09_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_09_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_09_RRESP_out                | wire [1:0]   |             |
| AXI_10_BRESP_out                | wire [1:0]   |             |
| AXI_10_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_10_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_10_RRESP_out                | wire [1:0]   |             |
| AXI_11_BRESP_out                | wire [1:0]   |             |
| AXI_11_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_11_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_11_RRESP_out                | wire [1:0]   |             |
| AXI_12_BRESP_out                | wire [1:0]   |             |
| AXI_12_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_12_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_12_RRESP_out                | wire [1:0]   |             |
| AXI_13_BRESP_out                | wire [1:0]   |             |
| AXI_13_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_13_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_13_RRESP_out                | wire [1:0]   |             |
| AXI_14_BRESP_out                | wire [1:0]   |             |
| AXI_14_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_14_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_14_RRESP_out                | wire [1:0]   |             |
| AXI_15_BRESP_out                | wire [1:0]   |             |
| AXI_15_DFI_AW_AERR_N_out        | wire [1:0]   |             |
| AXI_15_DFI_DW_RDDATA_VALID_out  | wire [1:0]   |             |
| AXI_15_RRESP_out                | wire [1:0]   |             |
| DLL_SCAN_OUT_00_out             | wire [1:0]   |             |
| IO_SCAN_OUT_00_out              | wire [1:0]   |             |
| MC_SCAN_OUT_00_out              | wire [1:0]   |             |
| MC_SCAN_OUT_01_out              | wire [1:0]   |             |
| MC_SCAN_OUT_02_out              | wire [1:0]   |             |
| MC_SCAN_OUT_03_out              | wire [1:0]   |             |
| MC_SCAN_OUT_04_out              | wire [1:0]   |             |
| MC_SCAN_OUT_05_out              | wire [1:0]   |             |
| MC_SCAN_OUT_06_out              | wire [1:0]   |             |
| MC_SCAN_OUT_07_out              | wire [1:0]   |             |
| PHY_SCAN_OUT_00_out             | wire [1:0]   |             |
| STATUS_00_out                   | wire [1:0]   |             |
| STATUS_01_out                   | wire [1:0]   |             |
| STATUS_02_out                   | wire [1:0]   |             |
| STATUS_03_out                   | wire [1:0]   |             |
| STATUS_04_out                   | wire [1:0]   |             |
| STATUS_05_out                   | wire [1:0]   |             |
| STATUS_06_out                   | wire [1:0]   |             |
| STATUS_07_out                   | wire [1:0]   |             |
| SW_SCAN_OUT_00_out              | wire [1:0]   |             |
| SW_SCAN_OUT_01_out              | wire [1:0]   |             |
| SW_SCAN_OUT_02_out              | wire [1:0]   |             |
| SW_SCAN_OUT_03_out              | wire [1:0]   |             |
| AXI_00_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_01_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_02_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_03_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_04_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_05_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_06_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_07_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_08_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_09_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_10_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_11_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_12_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_13_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_14_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_15_DFI_DW_RDDATA_DBI_out    | wire [20:0]  |             |
| AXI_00_RDATA_out                | wire [255:0] |             |
| AXI_01_RDATA_out                | wire [255:0] |             |
| AXI_02_RDATA_out                | wire [255:0] |             |
| AXI_03_RDATA_out                | wire [255:0] |             |
| AXI_04_RDATA_out                | wire [255:0] |             |
| AXI_05_RDATA_out                | wire [255:0] |             |
| AXI_06_RDATA_out                | wire [255:0] |             |
| AXI_07_RDATA_out                | wire [255:0] |             |
| AXI_08_RDATA_out                | wire [255:0] |             |
| AXI_09_RDATA_out                | wire [255:0] |             |
| AXI_10_RDATA_out                | wire [255:0] |             |
| AXI_11_RDATA_out                | wire [255:0] |             |
| AXI_12_RDATA_out                | wire [255:0] |             |
| AXI_13_RDATA_out                | wire [255:0] |             |
| AXI_14_RDATA_out                | wire [255:0] |             |
| AXI_15_RDATA_out                | wire [255:0] |             |
| DRAM_0_STAT_TEMP_out            | wire [2:0]   |             |
| APB_0_PRDATA_out                | wire [31:0]  |             |
| AXI_00_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_01_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_02_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_03_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_04_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_05_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_06_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_07_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_08_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_09_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_10_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_11_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_12_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_13_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_14_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_15_RDATA_PARITY_out         | wire [31:0]  |             |
| AXI_00_BID_out                  | wire [5:0]   |             |
| AXI_00_MC_STATUS_out            | wire [5:0]   |             |
| AXI_00_RID_out                  | wire [5:0]   |             |
| AXI_01_BID_out                  | wire [5:0]   |             |
| AXI_01_RID_out                  | wire [5:0]   |             |
| AXI_02_BID_out                  | wire [5:0]   |             |
| AXI_02_MC_STATUS_out            | wire [5:0]   |             |
| AXI_02_RID_out                  | wire [5:0]   |             |
| AXI_03_BID_out                  | wire [5:0]   |             |
| AXI_03_RID_out                  | wire [5:0]   |             |
| AXI_04_BID_out                  | wire [5:0]   |             |
| AXI_04_MC_STATUS_out            | wire [5:0]   |             |
| AXI_04_RID_out                  | wire [5:0]   |             |
| AXI_05_BID_out                  | wire [5:0]   |             |
| AXI_05_RID_out                  | wire [5:0]   |             |
| AXI_06_BID_out                  | wire [5:0]   |             |
| AXI_06_MC_STATUS_out            | wire [5:0]   |             |
| AXI_06_RID_out                  | wire [5:0]   |             |
| AXI_07_BID_out                  | wire [5:0]   |             |
| AXI_07_RID_out                  | wire [5:0]   |             |
| AXI_08_BID_out                  | wire [5:0]   |             |
| AXI_08_MC_STATUS_out            | wire [5:0]   |             |
| AXI_08_RID_out                  | wire [5:0]   |             |
| AXI_09_BID_out                  | wire [5:0]   |             |
| AXI_09_RID_out                  | wire [5:0]   |             |
| AXI_10_BID_out                  | wire [5:0]   |             |
| AXI_10_MC_STATUS_out            | wire [5:0]   |             |
| AXI_10_RID_out                  | wire [5:0]   |             |
| AXI_11_BID_out                  | wire [5:0]   |             |
| AXI_11_RID_out                  | wire [5:0]   |             |
| AXI_12_BID_out                  | wire [5:0]   |             |
| AXI_12_MC_STATUS_out            | wire [5:0]   |             |
| AXI_12_RID_out                  | wire [5:0]   |             |
| AXI_13_BID_out                  | wire [5:0]   |             |
| AXI_13_RID_out                  | wire [5:0]   |             |
| AXI_14_BID_out                  | wire [5:0]   |             |
| AXI_14_MC_STATUS_out            | wire [5:0]   |             |
| AXI_14_RID_out                  | wire [5:0]   |             |
| AXI_15_BID_out                  | wire [5:0]   |             |
| AXI_15_RID_out                  | wire [5:0]   |             |
| AXI_00_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_00_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_00_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_01_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_01_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_02_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_02_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_02_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_03_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_03_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_04_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_04_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_04_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_05_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_05_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_06_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_06_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_06_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_07_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_07_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_08_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_08_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_08_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_09_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_09_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_10_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_10_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_10_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_11_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_11_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_12_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_12_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_12_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_13_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_13_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_14_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_14_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| AXI_14_PHY_STATUS_out           | wire [7:0]   |             |
| AXI_15_DFI_DBI_BYTE_DISABLE_out | wire [7:0]   |             |
| AXI_15_DFI_DW_RDDATA_DERR_out   | wire [7:0]   |             |
| BLI_SCAN_OUT_00_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_01_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_02_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_03_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_04_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_05_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_06_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_07_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_08_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_09_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_10_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_11_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_12_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_13_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_14_out             | wire [7:0]   |             |
| BLI_SCAN_OUT_15_out             | wire [7:0]   |             |
| ANALOG_HBM_SEL_00_in            | wire         |             |
| APB_0_PCLK_in                   | wire         |             |
| APB_0_PENABLE_in                | wire         |             |
| APB_0_PRESET_N_in               | wire         |             |
| APB_0_PSEL_in                   | wire         |             |
| APB_0_PWRITE_in                 | wire         |             |
| AXI_00_ACLK_in                  | wire         |             |
| AXI_00_ARESET_N_in              | wire         |             |
| AXI_00_ARVALID_in               | wire         |             |
| AXI_00_AWVALID_in               | wire         |             |
| AXI_00_BREADY_in                | wire         |             |
| AXI_00_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_00_RREADY_in                | wire         |             |
| AXI_00_WLAST_in                 | wire         |             |
| AXI_00_WVALID_in                | wire         |             |
| AXI_01_ACLK_in                  | wire         |             |
| AXI_01_ARESET_N_in              | wire         |             |
| AXI_01_ARVALID_in               | wire         |             |
| AXI_01_AWVALID_in               | wire         |             |
| AXI_01_BREADY_in                | wire         |             |
| AXI_01_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_01_RREADY_in                | wire         |             |
| AXI_01_WLAST_in                 | wire         |             |
| AXI_01_WVALID_in                | wire         |             |
| AXI_02_ACLK_in                  | wire         |             |
| AXI_02_ARESET_N_in              | wire         |             |
| AXI_02_ARVALID_in               | wire         |             |
| AXI_02_AWVALID_in               | wire         |             |
| AXI_02_BREADY_in                | wire         |             |
| AXI_02_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_02_RREADY_in                | wire         |             |
| AXI_02_WLAST_in                 | wire         |             |
| AXI_02_WVALID_in                | wire         |             |
| AXI_03_ACLK_in                  | wire         |             |
| AXI_03_ARESET_N_in              | wire         |             |
| AXI_03_ARVALID_in               | wire         |             |
| AXI_03_AWVALID_in               | wire         |             |
| AXI_03_BREADY_in                | wire         |             |
| AXI_03_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_03_RREADY_in                | wire         |             |
| AXI_03_WLAST_in                 | wire         |             |
| AXI_03_WVALID_in                | wire         |             |
| AXI_04_ACLK_in                  | wire         |             |
| AXI_04_ARESET_N_in              | wire         |             |
| AXI_04_ARVALID_in               | wire         |             |
| AXI_04_AWVALID_in               | wire         |             |
| AXI_04_BREADY_in                | wire         |             |
| AXI_04_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_04_RREADY_in                | wire         |             |
| AXI_04_WLAST_in                 | wire         |             |
| AXI_04_WVALID_in                | wire         |             |
| AXI_05_ACLK_in                  | wire         |             |
| AXI_05_ARESET_N_in              | wire         |             |
| AXI_05_ARVALID_in               | wire         |             |
| AXI_05_AWVALID_in               | wire         |             |
| AXI_05_BREADY_in                | wire         |             |
| AXI_05_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_05_RREADY_in                | wire         |             |
| AXI_05_WLAST_in                 | wire         |             |
| AXI_05_WVALID_in                | wire         |             |
| AXI_06_ACLK_in                  | wire         |             |
| AXI_06_ARESET_N_in              | wire         |             |
| AXI_06_ARVALID_in               | wire         |             |
| AXI_06_AWVALID_in               | wire         |             |
| AXI_06_BREADY_in                | wire         |             |
| AXI_06_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_06_RREADY_in                | wire         |             |
| AXI_06_WLAST_in                 | wire         |             |
| AXI_06_WVALID_in                | wire         |             |
| AXI_07_ACLK_in                  | wire         |             |
| AXI_07_ARESET_N_in              | wire         |             |
| AXI_07_ARVALID_in               | wire         |             |
| AXI_07_AWVALID_in               | wire         |             |
| AXI_07_BREADY_in                | wire         |             |
| AXI_07_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_07_RREADY_in                | wire         |             |
| AXI_07_WLAST_in                 | wire         |             |
| AXI_07_WVALID_in                | wire         |             |
| AXI_08_ACLK_in                  | wire         |             |
| AXI_08_ARESET_N_in              | wire         |             |
| AXI_08_ARVALID_in               | wire         |             |
| AXI_08_AWVALID_in               | wire         |             |
| AXI_08_BREADY_in                | wire         |             |
| AXI_08_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_08_RREADY_in                | wire         |             |
| AXI_08_WLAST_in                 | wire         |             |
| AXI_08_WVALID_in                | wire         |             |
| AXI_09_ACLK_in                  | wire         |             |
| AXI_09_ARESET_N_in              | wire         |             |
| AXI_09_ARVALID_in               | wire         |             |
| AXI_09_AWVALID_in               | wire         |             |
| AXI_09_BREADY_in                | wire         |             |
| AXI_09_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_09_RREADY_in                | wire         |             |
| AXI_09_WLAST_in                 | wire         |             |
| AXI_09_WVALID_in                | wire         |             |
| AXI_10_ACLK_in                  | wire         |             |
| AXI_10_ARESET_N_in              | wire         |             |
| AXI_10_ARVALID_in               | wire         |             |
| AXI_10_AWVALID_in               | wire         |             |
| AXI_10_BREADY_in                | wire         |             |
| AXI_10_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_10_RREADY_in                | wire         |             |
| AXI_10_WLAST_in                 | wire         |             |
| AXI_10_WVALID_in                | wire         |             |
| AXI_11_ACLK_in                  | wire         |             |
| AXI_11_ARESET_N_in              | wire         |             |
| AXI_11_ARVALID_in               | wire         |             |
| AXI_11_AWVALID_in               | wire         |             |
| AXI_11_BREADY_in                | wire         |             |
| AXI_11_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_11_RREADY_in                | wire         |             |
| AXI_11_WLAST_in                 | wire         |             |
| AXI_11_WVALID_in                | wire         |             |
| AXI_12_ACLK_in                  | wire         |             |
| AXI_12_ARESET_N_in              | wire         |             |
| AXI_12_ARVALID_in               | wire         |             |
| AXI_12_AWVALID_in               | wire         |             |
| AXI_12_BREADY_in                | wire         |             |
| AXI_12_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_12_RREADY_in                | wire         |             |
| AXI_12_WLAST_in                 | wire         |             |
| AXI_12_WVALID_in                | wire         |             |
| AXI_13_ACLK_in                  | wire         |             |
| AXI_13_ARESET_N_in              | wire         |             |
| AXI_13_ARVALID_in               | wire         |             |
| AXI_13_AWVALID_in               | wire         |             |
| AXI_13_BREADY_in                | wire         |             |
| AXI_13_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_13_RREADY_in                | wire         |             |
| AXI_13_WLAST_in                 | wire         |             |
| AXI_13_WVALID_in                | wire         |             |
| AXI_14_ACLK_in                  | wire         |             |
| AXI_14_ARESET_N_in              | wire         |             |
| AXI_14_ARVALID_in               | wire         |             |
| AXI_14_AWVALID_in               | wire         |             |
| AXI_14_BREADY_in                | wire         |             |
| AXI_14_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_14_RREADY_in                | wire         |             |
| AXI_14_WLAST_in                 | wire         |             |
| AXI_14_WVALID_in                | wire         |             |
| AXI_15_ACLK_in                  | wire         |             |
| AXI_15_ARESET_N_in              | wire         |             |
| AXI_15_ARVALID_in               | wire         |             |
| AXI_15_AWVALID_in               | wire         |             |
| AXI_15_BREADY_in                | wire         |             |
| AXI_15_DFI_LP_PWR_X_REQ_in      | wire         |             |
| AXI_15_RREADY_in                | wire         |             |
| AXI_15_WLAST_in                 | wire         |             |
| AXI_15_WVALID_in                | wire         |             |
| BLI_SCAN_ENABLE_00_in           | wire         |             |
| BLI_SCAN_ENABLE_01_in           | wire         |             |
| BLI_SCAN_ENABLE_02_in           | wire         |             |
| BLI_SCAN_ENABLE_03_in           | wire         |             |
| BLI_SCAN_ENABLE_04_in           | wire         |             |
| BLI_SCAN_ENABLE_05_in           | wire         |             |
| BLI_SCAN_ENABLE_06_in           | wire         |             |
| BLI_SCAN_ENABLE_07_in           | wire         |             |
| BLI_SCAN_ENABLE_08_in           | wire         |             |
| BLI_SCAN_ENABLE_09_in           | wire         |             |
| BLI_SCAN_ENABLE_10_in           | wire         |             |
| BLI_SCAN_ENABLE_11_in           | wire         |             |
| BLI_SCAN_ENABLE_12_in           | wire         |             |
| BLI_SCAN_ENABLE_13_in           | wire         |             |
| BLI_SCAN_ENABLE_14_in           | wire         |             |
| BLI_SCAN_ENABLE_15_in           | wire         |             |
| BSCAN_DRCK_in                   | wire         |             |
| BSCAN_TCK_in                    | wire         |             |
| DLL_SCAN_CK_00_in               | wire         |             |
| DLL_SCAN_ENABLE_00_in           | wire         |             |
| DLL_SCAN_MODE_00_in             | wire         |             |
| DLL_SCAN_RST_N_00_in            | wire         |             |
| HBM_REF_CLK_in                  | wire         |             |
| IO_SCAN_CK_00_in                | wire         |             |
| IO_SCAN_ENABLE_00_in            | wire         |             |
| IO_SCAN_MODE_00_in              | wire         |             |
| IO_SCAN_RST_N_00_in             | wire         |             |
| MBIST_EN_00_in                  | wire         |             |
| MBIST_EN_01_in                  | wire         |             |
| MBIST_EN_02_in                  | wire         |             |
| MBIST_EN_03_in                  | wire         |             |
| MBIST_EN_04_in                  | wire         |             |
| MBIST_EN_05_in                  | wire         |             |
| MBIST_EN_06_in                  | wire         |             |
| MBIST_EN_07_in                  | wire         |             |
| MC_SCAN_CK_00_in                | wire         |             |
| MC_SCAN_CK_01_in                | wire         |             |
| MC_SCAN_CK_02_in                | wire         |             |
| MC_SCAN_CK_03_in                | wire         |             |
| MC_SCAN_CK_04_in                | wire         |             |
| MC_SCAN_CK_05_in                | wire         |             |
| MC_SCAN_CK_06_in                | wire         |             |
| MC_SCAN_CK_07_in                | wire         |             |
| MC_SCAN_ENABLE_00_in            | wire         |             |
| MC_SCAN_ENABLE_01_in            | wire         |             |
| MC_SCAN_ENABLE_02_in            | wire         |             |
| MC_SCAN_ENABLE_03_in            | wire         |             |
| MC_SCAN_ENABLE_04_in            | wire         |             |
| MC_SCAN_ENABLE_05_in            | wire         |             |
| MC_SCAN_ENABLE_06_in            | wire         |             |
| MC_SCAN_ENABLE_07_in            | wire         |             |
| MC_SCAN_MODE_00_in              | wire         |             |
| MC_SCAN_MODE_01_in              | wire         |             |
| MC_SCAN_MODE_02_in              | wire         |             |
| MC_SCAN_MODE_03_in              | wire         |             |
| MC_SCAN_MODE_04_in              | wire         |             |
| MC_SCAN_MODE_05_in              | wire         |             |
| MC_SCAN_MODE_06_in              | wire         |             |
| MC_SCAN_MODE_07_in              | wire         |             |
| MC_SCAN_RST_N_00_in             | wire         |             |
| MC_SCAN_RST_N_01_in             | wire         |             |
| MC_SCAN_RST_N_02_in             | wire         |             |
| MC_SCAN_RST_N_03_in             | wire         |             |
| MC_SCAN_RST_N_04_in             | wire         |             |
| MC_SCAN_RST_N_05_in             | wire         |             |
| MC_SCAN_RST_N_06_in             | wire         |             |
| MC_SCAN_RST_N_07_in             | wire         |             |
| PHY_SCAN_CK_00_in               | wire         |             |
| PHY_SCAN_ENABLE_00_in           | wire         |             |
| PHY_SCAN_MODE_00_in             | wire         |             |
| PHY_SCAN_RST_N_00_in            | wire         |             |
| SW_SCAN_CK_00_in                | wire         |             |
| SW_SCAN_ENABLE_00_in            | wire         |             |
| SW_SCAN_MODE_00_in              | wire         |             |
| SW_SCAN_RST_N_00_in             | wire         |             |
| AXI_00_ARBURST_in               | wire [1:0]   |             |
| AXI_00_AWBURST_in               | wire [1:0]   |             |
| AXI_01_ARBURST_in               | wire [1:0]   |             |
| AXI_01_AWBURST_in               | wire [1:0]   |             |
| AXI_02_ARBURST_in               | wire [1:0]   |             |
| AXI_02_AWBURST_in               | wire [1:0]   |             |
| AXI_03_ARBURST_in               | wire [1:0]   |             |
| AXI_03_AWBURST_in               | wire [1:0]   |             |
| AXI_04_ARBURST_in               | wire [1:0]   |             |
| AXI_04_AWBURST_in               | wire [1:0]   |             |
| AXI_05_ARBURST_in               | wire [1:0]   |             |
| AXI_05_AWBURST_in               | wire [1:0]   |             |
| AXI_06_ARBURST_in               | wire [1:0]   |             |
| AXI_06_AWBURST_in               | wire [1:0]   |             |
| AXI_07_ARBURST_in               | wire [1:0]   |             |
| AXI_07_AWBURST_in               | wire [1:0]   |             |
| AXI_08_ARBURST_in               | wire [1:0]   |             |
| AXI_08_AWBURST_in               | wire [1:0]   |             |
| AXI_09_ARBURST_in               | wire [1:0]   |             |
| AXI_09_AWBURST_in               | wire [1:0]   |             |
| AXI_10_ARBURST_in               | wire [1:0]   |             |
| AXI_10_AWBURST_in               | wire [1:0]   |             |
| AXI_11_ARBURST_in               | wire [1:0]   |             |
| AXI_11_AWBURST_in               | wire [1:0]   |             |
| AXI_12_ARBURST_in               | wire [1:0]   |             |
| AXI_12_AWBURST_in               | wire [1:0]   |             |
| AXI_13_ARBURST_in               | wire [1:0]   |             |
| AXI_13_AWBURST_in               | wire [1:0]   |             |
| AXI_14_ARBURST_in               | wire [1:0]   |             |
| AXI_14_AWBURST_in               | wire [1:0]   |             |
| AXI_15_ARBURST_in               | wire [1:0]   |             |
| AXI_15_AWBURST_in               | wire [1:0]   |             |
| DLL_SCAN_IN_00_in               | wire [1:0]   |             |
| IO_SCAN_IN_00_in                | wire [1:0]   |             |
| MC_SCAN_IN_00_in                | wire [1:0]   |             |
| MC_SCAN_IN_01_in                | wire [1:0]   |             |
| MC_SCAN_IN_02_in                | wire [1:0]   |             |
| MC_SCAN_IN_03_in                | wire [1:0]   |             |
| MC_SCAN_IN_04_in                | wire [1:0]   |             |
| MC_SCAN_IN_05_in                | wire [1:0]   |             |
| MC_SCAN_IN_06_in                | wire [1:0]   |             |
| MC_SCAN_IN_07_in                | wire [1:0]   |             |
| PHY_SCAN_IN_00_in               | wire [1:0]   |             |
| SW_SCAN_IN_00_in                | wire [1:0]   |             |
| SW_SCAN_IN_01_in                | wire [1:0]   |             |
| SW_SCAN_IN_02_in                | wire [1:0]   |             |
| SW_SCAN_IN_03_in                | wire [1:0]   |             |
| APB_0_PADDR_in                  | wire [21:0]  |             |
| DBG_IN_00_in                    | wire [23:0]  |             |
| DBG_IN_01_in                    | wire [23:0]  |             |
| DBG_IN_02_in                    | wire [23:0]  |             |
| DBG_IN_03_in                    | wire [23:0]  |             |
| DBG_IN_04_in                    | wire [23:0]  |             |
| DBG_IN_05_in                    | wire [23:0]  |             |
| DBG_IN_06_in                    | wire [23:0]  |             |
| DBG_IN_07_in                    | wire [23:0]  |             |
| DBG_IN_08_in                    | wire [23:0]  |             |
| DBG_IN_09_in                    | wire [23:0]  |             |
| DBG_IN_10_in                    | wire [23:0]  |             |
| DBG_IN_11_in                    | wire [23:0]  |             |
| DBG_IN_12_in                    | wire [23:0]  |             |
| DBG_IN_13_in                    | wire [23:0]  |             |
| DBG_IN_14_in                    | wire [23:0]  |             |
| DBG_IN_15_in                    | wire [23:0]  |             |
| AXI_00_WDATA_in                 | wire [255:0] |             |
| AXI_01_WDATA_in                 | wire [255:0] |             |
| AXI_02_WDATA_in                 | wire [255:0] |             |
| AXI_03_WDATA_in                 | wire [255:0] |             |
| AXI_04_WDATA_in                 | wire [255:0] |             |
| AXI_05_WDATA_in                 | wire [255:0] |             |
| AXI_06_WDATA_in                 | wire [255:0] |             |
| AXI_07_WDATA_in                 | wire [255:0] |             |
| AXI_08_WDATA_in                 | wire [255:0] |             |
| AXI_09_WDATA_in                 | wire [255:0] |             |
| AXI_10_WDATA_in                 | wire [255:0] |             |
| AXI_11_WDATA_in                 | wire [255:0] |             |
| AXI_12_WDATA_in                 | wire [255:0] |             |
| AXI_13_WDATA_in                 | wire [255:0] |             |
| AXI_14_WDATA_in                 | wire [255:0] |             |
| AXI_15_WDATA_in                 | wire [255:0] |             |
| AXI_00_ARSIZE_in                | wire [2:0]   |             |
| AXI_00_AWSIZE_in                | wire [2:0]   |             |
| AXI_01_ARSIZE_in                | wire [2:0]   |             |
| AXI_01_AWSIZE_in                | wire [2:0]   |             |
| AXI_02_ARSIZE_in                | wire [2:0]   |             |
| AXI_02_AWSIZE_in                | wire [2:0]   |             |
| AXI_03_ARSIZE_in                | wire [2:0]   |             |
| AXI_03_AWSIZE_in                | wire [2:0]   |             |
| AXI_04_ARSIZE_in                | wire [2:0]   |             |
| AXI_04_AWSIZE_in                | wire [2:0]   |             |
| AXI_05_ARSIZE_in                | wire [2:0]   |             |
| AXI_05_AWSIZE_in                | wire [2:0]   |             |
| AXI_06_ARSIZE_in                | wire [2:0]   |             |
| AXI_06_AWSIZE_in                | wire [2:0]   |             |
| AXI_07_ARSIZE_in                | wire [2:0]   |             |
| AXI_07_AWSIZE_in                | wire [2:0]   |             |
| AXI_08_ARSIZE_in                | wire [2:0]   |             |
| AXI_08_AWSIZE_in                | wire [2:0]   |             |
| AXI_09_ARSIZE_in                | wire [2:0]   |             |
| AXI_09_AWSIZE_in                | wire [2:0]   |             |
| AXI_10_ARSIZE_in                | wire [2:0]   |             |
| AXI_10_AWSIZE_in                | wire [2:0]   |             |
| AXI_11_ARSIZE_in                | wire [2:0]   |             |
| AXI_11_AWSIZE_in                | wire [2:0]   |             |
| AXI_12_ARSIZE_in                | wire [2:0]   |             |
| AXI_12_AWSIZE_in                | wire [2:0]   |             |
| AXI_13_ARSIZE_in                | wire [2:0]   |             |
| AXI_13_AWSIZE_in                | wire [2:0]   |             |
| AXI_14_ARSIZE_in                | wire [2:0]   |             |
| AXI_14_AWSIZE_in                | wire [2:0]   |             |
| AXI_15_ARSIZE_in                | wire [2:0]   |             |
| AXI_15_AWSIZE_in                | wire [2:0]   |             |
| APB_0_PWDATA_in                 | wire [31:0]  |             |
| AXI_00_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_00_WSTRB_in                 | wire [31:0]  |             |
| AXI_01_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_01_WSTRB_in                 | wire [31:0]  |             |
| AXI_02_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_02_WSTRB_in                 | wire [31:0]  |             |
| AXI_03_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_03_WSTRB_in                 | wire [31:0]  |             |
| AXI_04_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_04_WSTRB_in                 | wire [31:0]  |             |
| AXI_05_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_05_WSTRB_in                 | wire [31:0]  |             |
| AXI_06_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_06_WSTRB_in                 | wire [31:0]  |             |
| AXI_07_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_07_WSTRB_in                 | wire [31:0]  |             |
| AXI_08_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_08_WSTRB_in                 | wire [31:0]  |             |
| AXI_09_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_09_WSTRB_in                 | wire [31:0]  |             |
| AXI_10_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_10_WSTRB_in                 | wire [31:0]  |             |
| AXI_11_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_11_WSTRB_in                 | wire [31:0]  |             |
| AXI_12_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_12_WSTRB_in                 | wire [31:0]  |             |
| AXI_13_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_13_WSTRB_in                 | wire [31:0]  |             |
| AXI_14_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_14_WSTRB_in                 | wire [31:0]  |             |
| AXI_15_WDATA_PARITY_in          | wire [31:0]  |             |
| AXI_15_WSTRB_in                 | wire [31:0]  |             |
| AXI_00_ARADDR_in                | wire [36:0]  |             |
| AXI_00_AWADDR_in                | wire [36:0]  |             |
| AXI_01_ARADDR_in                | wire [36:0]  |             |
| AXI_01_AWADDR_in                | wire [36:0]  |             |
| AXI_02_ARADDR_in                | wire [36:0]  |             |
| AXI_02_AWADDR_in                | wire [36:0]  |             |
| AXI_03_ARADDR_in                | wire [36:0]  |             |
| AXI_03_AWADDR_in                | wire [36:0]  |             |
| AXI_04_ARADDR_in                | wire [36:0]  |             |
| AXI_04_AWADDR_in                | wire [36:0]  |             |
| AXI_05_ARADDR_in                | wire [36:0]  |             |
| AXI_05_AWADDR_in                | wire [36:0]  |             |
| AXI_06_ARADDR_in                | wire [36:0]  |             |
| AXI_06_AWADDR_in                | wire [36:0]  |             |
| AXI_07_ARADDR_in                | wire [36:0]  |             |
| AXI_07_AWADDR_in                | wire [36:0]  |             |
| AXI_08_ARADDR_in                | wire [36:0]  |             |
| AXI_08_AWADDR_in                | wire [36:0]  |             |
| AXI_09_ARADDR_in                | wire [36:0]  |             |
| AXI_09_AWADDR_in                | wire [36:0]  |             |
| AXI_10_ARADDR_in                | wire [36:0]  |             |
| AXI_10_AWADDR_in                | wire [36:0]  |             |
| AXI_11_ARADDR_in                | wire [36:0]  |             |
| AXI_11_AWADDR_in                | wire [36:0]  |             |
| AXI_12_ARADDR_in                | wire [36:0]  |             |
| AXI_12_AWADDR_in                | wire [36:0]  |             |
| AXI_13_ARADDR_in                | wire [36:0]  |             |
| AXI_13_AWADDR_in                | wire [36:0]  |             |
| AXI_14_ARADDR_in                | wire [36:0]  |             |
| AXI_14_AWADDR_in                | wire [36:0]  |             |
| AXI_15_ARADDR_in                | wire [36:0]  |             |
| AXI_15_AWADDR_in                | wire [36:0]  |             |
| AXI_00_ARLEN_in                 | wire [3:0]   |             |
| AXI_00_AWLEN_in                 | wire [3:0]   |             |
| AXI_01_ARLEN_in                 | wire [3:0]   |             |
| AXI_01_AWLEN_in                 | wire [3:0]   |             |
| AXI_02_ARLEN_in                 | wire [3:0]   |             |
| AXI_02_AWLEN_in                 | wire [3:0]   |             |
| AXI_03_ARLEN_in                 | wire [3:0]   |             |
| AXI_03_AWLEN_in                 | wire [3:0]   |             |
| AXI_04_ARLEN_in                 | wire [3:0]   |             |
| AXI_04_AWLEN_in                 | wire [3:0]   |             |
| AXI_05_ARLEN_in                 | wire [3:0]   |             |
| AXI_05_AWLEN_in                 | wire [3:0]   |             |
| AXI_06_ARLEN_in                 | wire [3:0]   |             |
| AXI_06_AWLEN_in                 | wire [3:0]   |             |
| AXI_07_ARLEN_in                 | wire [3:0]   |             |
| AXI_07_AWLEN_in                 | wire [3:0]   |             |
| AXI_08_ARLEN_in                 | wire [3:0]   |             |
| AXI_08_AWLEN_in                 | wire [3:0]   |             |
| AXI_09_ARLEN_in                 | wire [3:0]   |             |
| AXI_09_AWLEN_in                 | wire [3:0]   |             |
| AXI_10_ARLEN_in                 | wire [3:0]   |             |
| AXI_10_AWLEN_in                 | wire [3:0]   |             |
| AXI_11_ARLEN_in                 | wire [3:0]   |             |
| AXI_11_AWLEN_in                 | wire [3:0]   |             |
| AXI_12_ARLEN_in                 | wire [3:0]   |             |
| AXI_12_AWLEN_in                 | wire [3:0]   |             |
| AXI_13_ARLEN_in                 | wire [3:0]   |             |
| AXI_13_AWLEN_in                 | wire [3:0]   |             |
| AXI_14_ARLEN_in                 | wire [3:0]   |             |
| AXI_14_AWLEN_in                 | wire [3:0]   |             |
| AXI_15_ARLEN_in                 | wire [3:0]   |             |
| AXI_15_AWLEN_in                 | wire [3:0]   |             |
| AXI_00_ARID_in                  | wire [5:0]   |             |
| AXI_00_AWID_in                  | wire [5:0]   |             |
| AXI_01_ARID_in                  | wire [5:0]   |             |
| AXI_01_AWID_in                  | wire [5:0]   |             |
| AXI_02_ARID_in                  | wire [5:0]   |             |
| AXI_02_AWID_in                  | wire [5:0]   |             |
| AXI_03_ARID_in                  | wire [5:0]   |             |
| AXI_03_AWID_in                  | wire [5:0]   |             |
| AXI_04_ARID_in                  | wire [5:0]   |             |
| AXI_04_AWID_in                  | wire [5:0]   |             |
| AXI_05_ARID_in                  | wire [5:0]   |             |
| AXI_05_AWID_in                  | wire [5:0]   |             |
| AXI_06_ARID_in                  | wire [5:0]   |             |
| AXI_06_AWID_in                  | wire [5:0]   |             |
| AXI_07_ARID_in                  | wire [5:0]   |             |
| AXI_07_AWID_in                  | wire [5:0]   |             |
| AXI_08_ARID_in                  | wire [5:0]   |             |
| AXI_08_AWID_in                  | wire [5:0]   |             |
| AXI_09_ARID_in                  | wire [5:0]   |             |
| AXI_09_AWID_in                  | wire [5:0]   |             |
| AXI_10_ARID_in                  | wire [5:0]   |             |
| AXI_10_AWID_in                  | wire [5:0]   |             |
| AXI_11_ARID_in                  | wire [5:0]   |             |
| AXI_11_AWID_in                  | wire [5:0]   |             |
| AXI_12_ARID_in                  | wire [5:0]   |             |
| AXI_12_AWID_in                  | wire [5:0]   |             |
| AXI_13_ARID_in                  | wire [5:0]   |             |
| AXI_13_AWID_in                  | wire [5:0]   |             |
| AXI_14_ARID_in                  | wire [5:0]   |             |
| AXI_14_AWID_in                  | wire [5:0]   |             |
| AXI_15_ARID_in                  | wire [5:0]   |             |
| AXI_15_AWID_in                  | wire [5:0]   |             |
| BLI_SCAN_IN_00_in               | wire [7:0]   |             |
| BLI_SCAN_IN_01_in               | wire [7:0]   |             |
| BLI_SCAN_IN_02_in               | wire [7:0]   |             |
| BLI_SCAN_IN_03_in               | wire [7:0]   |             |
| BLI_SCAN_IN_04_in               | wire [7:0]   |             |
| BLI_SCAN_IN_05_in               | wire [7:0]   |             |
| BLI_SCAN_IN_06_in               | wire [7:0]   |             |
| BLI_SCAN_IN_07_in               | wire [7:0]   |             |
| BLI_SCAN_IN_08_in               | wire [7:0]   |             |
| BLI_SCAN_IN_09_in               | wire [7:0]   |             |
| BLI_SCAN_IN_10_in               | wire [7:0]   |             |
| BLI_SCAN_IN_11_in               | wire [7:0]   |             |
| BLI_SCAN_IN_12_in               | wire [7:0]   |             |
| BLI_SCAN_IN_13_in               | wire [7:0]   |             |
| BLI_SCAN_IN_14_in               | wire [7:0]   |             |
| BLI_SCAN_IN_15_in               | wire [7:0]   |             |
## Constants

| Name                            | Type    | Value                       | Description                        |
| ------------------------------- | ------- | --------------------------- | ---------------------------------- |
| MODULE_NAME                     |         | "HBM_ONE_STACK_INTF"        | define constants                   |
| PHY_PCLK_INVERT_01_FALSE        |         | 0                           | Parameter encodings and registers  |
| PHY_PCLK_INVERT_01_TRUE         |         | 1                           |                                    |
| CLK_SEL_00_REG                  | [40:1]  | CLK_SEL_00                  |                                    |
| CLK_SEL_01_REG                  | [40:1]  | CLK_SEL_01                  |                                    |
| CLK_SEL_02_REG                  | [40:1]  | CLK_SEL_02                  |                                    |
| CLK_SEL_03_REG                  | [40:1]  | CLK_SEL_03                  |                                    |
| CLK_SEL_04_REG                  | [40:1]  | CLK_SEL_04                  |                                    |
| CLK_SEL_05_REG                  | [40:1]  | CLK_SEL_05                  |                                    |
| CLK_SEL_06_REG                  | [40:1]  | CLK_SEL_06                  |                                    |
| CLK_SEL_07_REG                  | [40:1]  | CLK_SEL_07                  |                                    |
| CLK_SEL_08_REG                  | [40:1]  | CLK_SEL_08                  |                                    |
| CLK_SEL_09_REG                  | [40:1]  | CLK_SEL_09                  |                                    |
| CLK_SEL_10_REG                  | [40:1]  | CLK_SEL_10                  |                                    |
| CLK_SEL_11_REG                  | [40:1]  | CLK_SEL_11                  |                                    |
| CLK_SEL_12_REG                  | [40:1]  | CLK_SEL_12                  |                                    |
| CLK_SEL_13_REG                  | [40:1]  | CLK_SEL_13                  |                                    |
| CLK_SEL_14_REG                  | [40:1]  | CLK_SEL_14                  |                                    |
| CLK_SEL_15_REG                  | [40:1]  | CLK_SEL_15                  |                                    |
| DATARATE_00_REG                 | [10:0]  | DATARATE_00                 |                                    |
| DATARATE_01_REG                 | [10:0]  | DATARATE_01                 |                                    |
| DATARATE_02_REG                 | [10:0]  | DATARATE_02                 |                                    |
| DATARATE_03_REG                 | [10:0]  | DATARATE_03                 |                                    |
| DATARATE_04_REG                 | [10:0]  | DATARATE_04                 |                                    |
| DATARATE_05_REG                 | [10:0]  | DATARATE_05                 |                                    |
| DATARATE_06_REG                 | [10:0]  | DATARATE_06                 |                                    |
| DATARATE_07_REG                 | [10:0]  | DATARATE_07                 |                                    |
| DA_LOCKOUT_REG                  | [40:1]  | DA_LOCKOUT                  |                                    |
| IS_APB_0_PCLK_INVERTED_REG      | [0:0]   | IS_APB_0_PCLK_INVERTED      |                                    |
| IS_APB_0_PRESET_N_INVERTED_REG  | [0:0]   | IS_APB_0_PRESET_N_INVERTED  |                                    |
| IS_AXI_00_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_00_ACLK_INVERTED     |                                    |
| IS_AXI_00_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_00_ARESET_N_INVERTED |                                    |
| IS_AXI_01_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_01_ACLK_INVERTED     |                                    |
| IS_AXI_01_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_01_ARESET_N_INVERTED |                                    |
| IS_AXI_02_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_02_ACLK_INVERTED     |                                    |
| IS_AXI_02_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_02_ARESET_N_INVERTED |                                    |
| IS_AXI_03_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_03_ACLK_INVERTED     |                                    |
| IS_AXI_03_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_03_ARESET_N_INVERTED |                                    |
| IS_AXI_04_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_04_ACLK_INVERTED     |                                    |
| IS_AXI_04_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_04_ARESET_N_INVERTED |                                    |
| IS_AXI_05_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_05_ACLK_INVERTED     |                                    |
| IS_AXI_05_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_05_ARESET_N_INVERTED |                                    |
| IS_AXI_06_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_06_ACLK_INVERTED     |                                    |
| IS_AXI_06_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_06_ARESET_N_INVERTED |                                    |
| IS_AXI_07_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_07_ACLK_INVERTED     |                                    |
| IS_AXI_07_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_07_ARESET_N_INVERTED |                                    |
| IS_AXI_08_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_08_ACLK_INVERTED     |                                    |
| IS_AXI_08_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_08_ARESET_N_INVERTED |                                    |
| IS_AXI_09_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_09_ACLK_INVERTED     |                                    |
| IS_AXI_09_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_09_ARESET_N_INVERTED |                                    |
| IS_AXI_10_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_10_ACLK_INVERTED     |                                    |
| IS_AXI_10_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_10_ARESET_N_INVERTED |                                    |
| IS_AXI_11_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_11_ACLK_INVERTED     |                                    |
| IS_AXI_11_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_11_ARESET_N_INVERTED |                                    |
| IS_AXI_12_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_12_ACLK_INVERTED     |                                    |
| IS_AXI_12_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_12_ARESET_N_INVERTED |                                    |
| IS_AXI_13_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_13_ACLK_INVERTED     |                                    |
| IS_AXI_13_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_13_ARESET_N_INVERTED |                                    |
| IS_AXI_14_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_14_ACLK_INVERTED     |                                    |
| IS_AXI_14_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_14_ARESET_N_INVERTED |                                    |
| IS_AXI_15_ACLK_INVERTED_REG     | [0:0]   | IS_AXI_15_ACLK_INVERTED     |                                    |
| IS_AXI_15_ARESET_N_INVERTED_REG | [0:0]   | IS_AXI_15_ARESET_N_INVERTED |                                    |
| MC_ENABLE_0_REG                 | [40:1]  | MC_ENABLE_0                 |                                    |
| MC_ENABLE_1_REG                 | [40:1]  | MC_ENABLE_1                 |                                    |
| MC_ENABLE_2_REG                 | [40:1]  | MC_ENABLE_2                 |                                    |
| MC_ENABLE_3_REG                 | [40:1]  | MC_ENABLE_3                 |                                    |
| MC_ENABLE_4_REG                 | [40:1]  | MC_ENABLE_4                 |                                    |
| MC_ENABLE_5_REG                 | [40:1]  | MC_ENABLE_5                 |                                    |
| MC_ENABLE_6_REG                 | [40:1]  | MC_ENABLE_6                 |                                    |
| MC_ENABLE_7_REG                 | [40:1]  | MC_ENABLE_7                 |                                    |
| MC_ENABLE_APB_REG               | [40:1]  | MC_ENABLE_APB               |                                    |
| PAGEHIT_PERCENT_00_REG          | [6:0]   | PAGEHIT_PERCENT_00          |                                    |
| PHY_ENABLE_00_REG               | [40:1]  | PHY_ENABLE_00               |                                    |
| PHY_ENABLE_01_REG               | [40:1]  | PHY_ENABLE_01               |                                    |
| PHY_ENABLE_02_REG               | [40:1]  | PHY_ENABLE_02               |                                    |
| PHY_ENABLE_03_REG               | [40:1]  | PHY_ENABLE_03               |                                    |
| PHY_ENABLE_04_REG               | [40:1]  | PHY_ENABLE_04               |                                    |
| PHY_ENABLE_05_REG               | [40:1]  | PHY_ENABLE_05               |                                    |
| PHY_ENABLE_06_REG               | [40:1]  | PHY_ENABLE_06               |                                    |
| PHY_ENABLE_07_REG               | [40:1]  | PHY_ENABLE_07               |                                    |
| PHY_ENABLE_08_REG               | [40:1]  | PHY_ENABLE_08               |                                    |
| PHY_ENABLE_09_REG               | [40:1]  | PHY_ENABLE_09               |                                    |
| PHY_ENABLE_10_REG               | [40:1]  | PHY_ENABLE_10               |                                    |
| PHY_ENABLE_11_REG               | [40:1]  | PHY_ENABLE_11               |                                    |
| PHY_ENABLE_12_REG               | [40:1]  | PHY_ENABLE_12               |                                    |
| PHY_ENABLE_13_REG               | [40:1]  | PHY_ENABLE_13               |                                    |
| PHY_ENABLE_14_REG               | [40:1]  | PHY_ENABLE_14               |                                    |
| PHY_ENABLE_15_REG               | [40:1]  | PHY_ENABLE_15               |                                    |
| PHY_ENABLE_APB_REG              | [40:1]  | PHY_ENABLE_APB              |                                    |
| PHY_PCLK_INVERT_01_REG          | [40:1]  | PHY_PCLK_INVERT_01          |                                    |
| READ_PERCENT_00_REG             | [6:0]   | READ_PERCENT_00             |                                    |
| READ_PERCENT_01_REG             | [6:0]   | READ_PERCENT_01             |                                    |
| READ_PERCENT_02_REG             | [6:0]   | READ_PERCENT_02             |                                    |
| READ_PERCENT_03_REG             | [6:0]   | READ_PERCENT_03             |                                    |
| READ_PERCENT_04_REG             | [6:0]   | READ_PERCENT_04             |                                    |
| READ_PERCENT_05_REG             | [6:0]   | READ_PERCENT_05             |                                    |
| READ_PERCENT_06_REG             | [6:0]   | READ_PERCENT_06             |                                    |
| READ_PERCENT_07_REG             | [6:0]   | READ_PERCENT_07             |                                    |
| READ_PERCENT_08_REG             | [6:0]   | READ_PERCENT_08             |                                    |
| READ_PERCENT_09_REG             | [6:0]   | READ_PERCENT_09             |                                    |
| READ_PERCENT_10_REG             | [6:0]   | READ_PERCENT_10             |                                    |
| READ_PERCENT_11_REG             | [6:0]   | READ_PERCENT_11             |                                    |
| READ_PERCENT_12_REG             | [6:0]   | READ_PERCENT_12             |                                    |
| READ_PERCENT_13_REG             | [6:0]   | READ_PERCENT_13             |                                    |
| READ_PERCENT_14_REG             | [6:0]   | READ_PERCENT_14             |                                    |
| READ_PERCENT_15_REG             | [6:0]   | READ_PERCENT_15             |                                    |
| SIM_DEVICE_REG                  | [152:1] | SIM_DEVICE                  |                                    |
| STACK_LOCATION_REG              | [0:0]   | STACK_LOCATION              |                                    |
| SWITCH_ENABLE_REG               | [40:1]  | SWITCH_ENABLE               |                                    |
| WRITE_PERCENT_00_REG            | [6:0]   | WRITE_PERCENT_00            |                                    |
| WRITE_PERCENT_01_REG            | [6:0]   | WRITE_PERCENT_01            |                                    |
| WRITE_PERCENT_02_REG            | [6:0]   | WRITE_PERCENT_02            |                                    |
| WRITE_PERCENT_03_REG            | [6:0]   | WRITE_PERCENT_03            |                                    |
| WRITE_PERCENT_04_REG            | [6:0]   | WRITE_PERCENT_04            |                                    |
| WRITE_PERCENT_05_REG            | [6:0]   | WRITE_PERCENT_05            |                                    |
| WRITE_PERCENT_06_REG            | [6:0]   | WRITE_PERCENT_06            |                                    |
| WRITE_PERCENT_07_REG            | [6:0]   | WRITE_PERCENT_07            |                                    |
| WRITE_PERCENT_08_REG            | [6:0]   | WRITE_PERCENT_08            |                                    |
| WRITE_PERCENT_09_REG            | [6:0]   | WRITE_PERCENT_09            |                                    |
| WRITE_PERCENT_10_REG            | [6:0]   | WRITE_PERCENT_10            |                                    |
| WRITE_PERCENT_11_REG            | [6:0]   | WRITE_PERCENT_11            |                                    |
| WRITE_PERCENT_12_REG            | [6:0]   | WRITE_PERCENT_12            |                                    |
| WRITE_PERCENT_13_REG            | [6:0]   | WRITE_PERCENT_13            |                                    |
| WRITE_PERCENT_14_REG            | [6:0]   | WRITE_PERCENT_14            |                                    |
| WRITE_PERCENT_15_REG            | [6:0]   | WRITE_PERCENT_15            |                                    |
| ANALOG_MUX_SEL_0_REG            | [7:0]   | 8'h00                       |                                    |
| APB_BYPASS_EN_REG               | [40:1]  | "FALSE"                     |                                    |
| AXI_BYPASS_EN_REG               | [40:1]  | "FALSE"                     |                                    |
| BLI_TESTMODE_SEL_REG            | [40:1]  | "FALSE"                     |                                    |
| DBG_BYPASS_VAL_REG              | [51:0]  | 52'hFFFFFFFFFFFFF           |                                    |
| DEBUG_MODE_REG                  | [40:1]  | "FALSE"                     |                                    |
| DFI_BYPASS_VAL_REG              | [51:0]  | 52'h0000000000000           |                                    |
| DLL_TESTMODE_SEL_0_REG          | [40:1]  | "FALSE"                     |                                    |
| IO_TESTMODE_SEL_0_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_0_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_1_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_2_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_3_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_4_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_5_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_6_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_CSSD_SEL_7_REG               | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_0_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_1_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_2_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_3_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_4_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_5_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_6_REG           | [40:1]  | "FALSE"                     |                                    |
| MC_TESTMODE_SEL_7_REG           | [40:1]  | "FALSE"                     |                                    |
| PHY_CSSD_SEL_0_REG              | [40:1]  | "FALSE"                     |                                    |
| PHY_TESTMODE_SEL_0_REG          | [40:1]  | "FALSE"                     |                                    |
| SW_TESTMODE_SEL_0_REG           | [40:1]  | "FALSE"                     |                                    |
## Processes
- unnamed: ( @ (trig_attr) )
## Instantiations

- SIP_HBM_ONE_STACK_INTF_INST: SIP_HBM_ONE_STACK_INTF
**Description**
tie off

