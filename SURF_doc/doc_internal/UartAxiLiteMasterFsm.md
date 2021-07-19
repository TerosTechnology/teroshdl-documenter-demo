# Entity: UartAxiLiteMasterFsm

- **File**: UartAxiLiteMasterFsm.vhd
## Diagram

![Diagram](UartAxiLiteMasterFsm.svg "Diagram")
## Description

Title      : UART Memory Protocol: https://confluence.slac.stanford.edu/x/uSDoDQ
Company    : SLAC National Accelerator Laboratory
Description: Finite State Machine (FSM) for UartAxiLiteMaster.vhd
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| TPD_G        | time | 1 ns  |             |
## Ports

| Port name        | Direction | Type                   | Description                      |
| ---------------- | --------- | ---------------------- | -------------------------------- |
| axilClk          | in        | sl                     | Clock and Reset                  |
| axilRst          | in        | sl                     |                                  |
| uartTxValid      | out       | sl                     | UART TX Streaming Byte Interface |
| uartTxData       | out       | slv(7 downto 0)        |                                  |
| uartTxReady      | in        | sl                     |                                  |
| uartRxValid      | in        | sl                     | UART RX Streaming Byte Interface |
| uartRxData       | in        | slv(7 downto 0)        |                                  |
| uartRxReady      | out       | sl                     |                                  |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType | AXI-Lite interface               |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType  |                                  |
| mAxilReadMaster  | out       | AxiLiteReadMasterType  |                                  |
| mAxilReadSlave   | in        | AxiLiteReadSlaveType   |                                  |
## Signals

| Name    | Type           | Description |
| ------- | -------------- | ----------- |
| r       | RegType        |             |
| rin     | RegType        |             |
| axilAck | AxiLiteAckType |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       state       => WAIT_START_S,<br><span style="padding-left:20px">       count       => (others => '0'),<br><span style="padding-left:20px">       axilReq     => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       rdData      => (others => '0'),<br><span style="padding-left:20px">       uartTxData  => (others => '0'),<br><span style="padding-left:20px">       uartTxValid => '0',<br><span style="padding-left:20px">       uartRxReady => '1') |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( WAIT_START_S,<br><span style="padding-left:20px"> SPACE_ADDR_S,<br><span style="padding-left:20px"> ADDR_SPACE_S,<br><span style="padding-left:20px"> WR_DATA_S,<br><span style="padding-left:20px"> WAIT_EOL_S,<br><span style="padding-left:20px"> AXIL_TXN_S,<br><span style="padding-left:20px"> RD_DATA_SPACE_S,<br><span style="padding-left:20px"> RD_DATA_S,<br><span style="padding-left:20px"> DONE_S)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                                                     |             |
## Functions
- hexToSlv <font id="function_arguments">(hex : slv(7 downto 0)) </font> <font id="function_return">return slv </font>
**Description**
translate a hex character 0-9 A-F into an slv
- slvToHex <font id="function_arguments">(nibble : slv(3 downto 0)) </font> <font id="function_return">return slv </font>
## Processes
- comb: ( axilAck, axilRst, r, uartRxData, uartRxValid, uartTxReady )
**Description**
[in]

- seq: ( axilClk )
## Instantiations

- U_AxiLiteMaster_1: surf.AxiLiteMaster
