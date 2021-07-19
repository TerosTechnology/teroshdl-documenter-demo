# Entity: AxiRateGen

- **File**: AxiRateGen.vhd
## Diagram

![Diagram](AxiRateGen.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: General Purpose AXI4 memory rate generator
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type          | Value | Description |
| ------------ | ------------- | ----- | ----------- |
| TPD_G        | time          | 1 ns  |             |
| COMMON_CLK_G | boolean       | false |             |
| AXI_CONFIG_G | AxiConfigType |       |             |
## Ports

| Port name        | Direction | Type                   | Description           |
| ---------------- | --------- | ---------------------- | --------------------- |
| axiClk           | in        | sl                     | AXI4 Memory Interface |
| axiRst           | in        | sl                     |                       |
| axiWriteMaster   | out       | AxiWriteMasterType     |                       |
| axiWriteSlave    | in        | AxiWriteSlaveType      |                       |
| axiReadMaster    | out       | AxiReadMasterType      |                       |
| axiReadSlave     | in        | AxiReadSlaveType       |                       |
| axilClk          | in        | sl                     | AXI-Lite Interface    |
| axilRst          | in        | sl                     |                       |
| sAxilReadMaster  | in        | AxiLiteReadMasterType  |                       |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType   |                       |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType |                       |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType  |                       |
## Signals

| Name            | Type                   | Description |
| --------------- | ---------------------- | ----------- |
| r               | RegType                |             |
| rin             | RegType                |             |
| axilReadMaster  | AxiLiteReadMasterType  |             |
| axilReadSlave   | AxiLiteReadSlaveType   |             |
| axilWriteMaster | AxiLiteWriteMasterType |             |
| axilWriteSlave  | AxiLiteWriteSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       wrState        => WRITE_ADDR_S,<br><span style="padding-left:20px">       rdState        => READ_ADDR_S,<br><span style="padding-left:20px">       awlen          => x"00",<br><span style="padding-left:20px">       writeSize      => x"FFF",<br><span style="padding-left:20px">       wrTimer        => x"0000_0000",<br><span style="padding-left:20px">       rdTimer        => x"0000_0000",<br><span style="padding-left:20px">       -- Registers       wrEnable       => '0',<br><span style="padding-left:20px">       rdEnable       => '0',<br><span style="padding-left:20px">       wrSize         => x"FFF",<br><span style="padding-left:20px">       rdSize         => x"FFF",<br><span style="padding-left:20px">       wrPeriod       => x"0000_FFFF",<br><span style="padding-left:20px">       rdPeriod       => x"0000_FFFF",<br><span style="padding-left:20px">       awburst        => "01",<br><span style="padding-left:20px">       awcache        => "1111",<br><span style="padding-left:20px">       arburst        => "01",<br><span style="padding-left:20px">       arcache        => "1111",<br><span style="padding-left:20px">       -- AXI4       axiWriteMaster => axiWriteMasterInit(AXI_CONFIG_G),<br><span style="padding-left:20px">       axiReadMaster  => axiReadMasterInit(AXI_CONFIG_G),<br><span style="padding-left:20px">       -- AXI-Lite       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
## Types

| Name        | Type                                                                                                                 | Description |
| ----------- | -------------------------------------------------------------------------------------------------------------------- | ----------- |
| WrStateType | ( WRITE_ADDR_S,<br><span style="padding-left:20px"> WRITE_DATA_S,<br><span style="padding-left:20px"> WRITE_RESP_S)  |             |
| RdStateType | ( READ_ADDR_S,<br><span style="padding-left:20px"> READ_DATA_S)                                                      |             |
| RegType     |                                                                                                                      |             |
## Processes
- comb: ( axiReadSlave, axiRst, axiWriteSlave, axilReadMaster,
                   axilWriteMaster, r )
- seq: ( axiClk )
## Instantiations

- U_AxiLiteAsync: surf.AxiLiteAsync
