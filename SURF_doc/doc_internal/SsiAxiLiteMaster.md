# Entity: SsiAxiLiteMaster

## Diagram

![Diagram](SsiAxiLiteMaster.svg "Diagram")
## Description

Title      : SSI Protocol: https://confluence.slac.stanford.edu/x/0oyfD
Company    : SLAC National Accelerator Laboratory
Description:
Block for Register protocol.
Packet is a minimum of 4 x 32-bits
Incoming Request:
Word 0   Data[31:0]  = TID[31:0] (echoed)
Word 1   Data[29:0]  = Address[31:2] (only 26-bits if EN_32BIT_G = false)
Word 1   Data[31:30] = Opcode, 0x0=Read, 0x1=Write, 0x2=Set, 0x3=Clear
                       (bit set and bit clear not supported)
Word 2   Data[31:0]  = WriteData[31:0] or ReadCount[8:0]
Word N-1 Data[31:0]  = WriteData[31:0]
Word N   Data[31:2]  = Don't Care
Outgoing Response:
Word 0   Data[1:0]   = VC (legacy, echoed)
Word 0   Data[7:2]   = Dest_ID (legacy, echoed)
Word 0   Data[31:8]  = TID[31:0] (legacy, echoed)
Word 1   Data[29:0]  = Address[31:2]
Word 1   Data[31:30] = OpCode, 0x0=Read, 0x1=Write, 0x2=Set, 0x3=Clear
Word 2   Data[31:0]  = ReadData[31:0]/WriteData[31:0]
Word N-1 Data[31:0]  = ReadData[31:0]/WriteData[31:0]
Word N   Data[31:18] = Don't Care
Word N   Data[17]    = Timeout Flag (response data)
Word N   Data[16]    = Fail Flag (response data)
Word N   Data[15:00] = Don't Care
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name        | Type                       | Value   | Description           |
| ------------------- | -------------------------- | ------- | --------------------- |
| TPD_G               | time                       | 1 ns    | General Config        |
| RESP_THOLD_G        | integer range 0 to (2**24) | 1       | =1 = normal operation |
| SLAVE_READY_EN_G    | boolean                    | false   |                       |
| EN_32BIT_ADDR_G     | boolean                    | false   |                       |
| MEMORY_TYPE_G       | string                     | "block" |                       |
| GEN_SYNC_FIFO_G     | boolean                    | false   |                       |
| FIFO_ADDR_WIDTH_G   | integer range 4 to 48      | 9       |                       |
| FIFO_PAUSE_THRESH_G | integer range 1 to (2**24) | 2**8    |                       |
| AXI_STREAM_CONFIG_G | AxiStreamConfigType        |         | AXI Stream IO Config  |
## Ports

| Port name           | Direction | Type                   | Description                                            |
| ------------------- | --------- | ---------------------- | ------------------------------------------------------ |
| sAxisClk            | in        | sl                     | Streaming Slave (Rx) Interface (sAxisClk domain)       |
| sAxisRst            | in        | sl                     |                                                        |
| sAxisMaster         | in        | AxiStreamMasterType    |                                                        |
| sAxisSlave          | out       | AxiStreamSlaveType     |                                                        |
| sAxisCtrl           | out       | AxiStreamCtrlType      |                                                        |
| mAxisClk            | in        | sl                     | Streaming Master (Tx) Data Interface (mAxisClk domain) |
| mAxisRst            | in        | sl                     |                                                        |
| mAxisMaster         | out       | AxiStreamMasterType    |                                                        |
| mAxisSlave          | in        | AxiStreamSlaveType     |                                                        |
| axiLiteClk          | in        | sl                     | AXI Lite Bus (axiLiteClk domain)                       |
| axiLiteRst          | in        | sl                     |                                                        |
| mAxiLiteWriteMaster | out       | AxiLiteWriteMasterType |                                                        |
| mAxiLiteWriteSlave  | in        | AxiLiteWriteSlaveType  |                                                        |
| mAxiLiteReadMaster  | out       | AxiLiteReadMasterType  |                                                        |
| mAxiLiteReadSlave   | in        | AxiLiteReadSlaveType   |                                                        |
## Signals

| Name            | Type                | Description |
| --------------- | ------------------- | ----------- |
| sFifoAxisMaster | AxiStreamMasterType |             |
| sFifoAxisSlave  | AxiStreamSlaveType  |             |
| mFifoAxisMaster | AxiStreamMasterType |             |
| mFifoAxisSlave  | AxiStreamSlaveType  |             |
| mFifoAxisCtrl   | AxiStreamCtrlType   |             |
| r               | RegType             |             |
| rin             | RegType             |             |
## Constants

| Name                     | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ------------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SLAVE_FIFO_SSI_CONFIG_C  | AxiStreamConfigType |  ssiAxiStreamConfig(4,<br><span style="padding-left:20px"> TKEEP_COMP_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| MASTER_FIFO_SSI_CONFIG_C | AxiStreamConfigType |  ssiAxiStreamConfig(4,<br><span style="padding-left:20px"> TKEEP_COMP_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| REG_INIT_C               | RegType             |  (       echo                => (others => '0'),<br><span style="padding-left:20px">       address             => (others => '0'),<br><span style="padding-left:20px">       rdSize              => (others => '0'),<br><span style="padding-left:20px">       rdCount             => (others => '0'),<br><span style="padding-left:20px">       timer               => (others => '1'),<br><span style="padding-left:20px">       state               => S_IDLE_C,<br><span style="padding-left:20px">       timeout             => '0',<br><span style="padding-left:20px">       fail                => '0',<br><span style="padding-left:20px">       mAxiLiteWriteMaster => AXI_LITE_WRITE_MASTER_INIT_C,<br><span style="padding-left:20px">       mAxiLiteReadMaster  => AXI_LITE_READ_MASTER_INIT_C,<br><span style="padding-left:20px">       sFifoAxisSlave      => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       mFifoAxisMaster     => AXI_STREAM_MASTER_INIT_C) |             |
## Types

| Name      | Type                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | (S_IDLE_C,<br><span style="padding-left:20px"> S_ADDR_C,<br><span style="padding-left:20px"> S_WRITE_C,<br><span style="padding-left:20px"> S_WRITE_AXI_C,<br><span style="padding-left:20px"> S_READ_SIZE_C,<br><span style="padding-left:20px"> S_READ_C,<br><span style="padding-left:20px"> S_READ_AXI_C,<br><span style="padding-left:20px"> S_STATUS_C,<br><span style="padding-left:20px"> S_DUMP_C)  |             |
| RegType   |                                                                                                                                                                                                                                                                                                                                                                                                              |             |
## Processes
- comb: ( axiLiteRst, mAxiLiteReadSlave, mAxiLiteWriteSlave, mFifoAxisCtrl, r, sFifoAxisMaster )
**Description**
Master State Machine

- seq: ( axiLiteClk )
## Instantiations

- SlaveAxiStreamFifo: surf.AxiStreamFifoV2
- MasterAxiStreamFifo: surf.AxiStreamFifoV2
**Description**
Output FIFO

