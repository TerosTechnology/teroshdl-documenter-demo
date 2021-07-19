# Entity: AxiLiteWriteFilter

- **File**: AxiLiteWriteFilter.vhd
## Diagram

![Diagram](AxiLiteWriteFilter.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: Module for filtering write access
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name  | Type       | Value              | Description                |
| ------------- | ---------- | ------------------ | -------------------------- |
| TPD_G         | time       | 1 ns               |                            |
| FILTER_SIZE_G | positive   | 1                  | Number of filter addresses |
| FILTER_ADDR_G | Slv32Array | (0 => x"00000000") |                            |
## Ports

| Port name        | Direction | Type                   | Description                                     |
| ---------------- | --------- | ---------------------- | ----------------------------------------------- |
| axilClk          | in        | sl                     | Clock and reset                                 |
| axilRst          | in        | sl                     |                                                 |
| enFilter         | in        | sl                     |                                                 |
| blockAll         | in        | sl                     | overrides enFilter, '1' blocks all transactions |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType | AXI-Lite Slave Interface                        |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType  |                                                 |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType | AXI-Lite Master Interface                       |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType  |                                                 |
## Signals

| Name | Type    | Description |
| ---- | ------- | ----------- |
| r    | RegType |             |
| rin  | RegType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       validAddress     => '1',<br><span style="padding-left:20px">       idx              => 0,<br><span style="padding-left:20px">       sAxilWriteSlave  => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       mAxilWriteMaster => AXI_LITE_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       state            => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                       | Description |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> LOOP_ARRAY_S,<br><span style="padding-left:20px"> CHECK_FLAG_S,<br><span style="padding-left:20px"> MOVE_S,<br><span style="padding-left:20px"> BUS_RESP_S)  |             |
| RegType   |                                                                                                                                                                                                            |             |
## Processes
- comb: ( axilRst, blockAll, enFilter, mAxilWriteSlave, r,
                   sAxilWriteMaster )
- seq: ( axilClk )
