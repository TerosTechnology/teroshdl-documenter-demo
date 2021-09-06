# Entity: AxiStreamDma

- **File**: AxiStreamDma.vhd
## Diagram

![Diagram](AxiStreamDma.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Generic AXI Stream DMA block for frame at a time transfers.
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

| Generic name      | Type                 | Value       | Description |
| ----------------- | -------------------- | ----------- | ----------- |
| TPD_G             | time                 | 1 ns        |             |
| FREE_ADDR_WIDTH_G | integer              | 9           |             |
| AXIL_COUNT_G      | integer range 1 to 2 | 1           |             |
| AXIL_BASE_ADDR_G  | slv(31 downto 0)     | x"00000000" |             |
| AXI_READY_EN_G    | boolean              | false       |             |
| AXIS_READY_EN_G   | boolean              | false       |             |
| AXIS_CONFIG_G     | AxiStreamConfigType  |             |             |
| AXI_CONFIG_G      | AxiConfigType        |             |             |
| AXI_BURST_G       | slv(1 downto 0)      | "01"        |             |
| AXI_CACHE_G       | slv(3 downto 0)      | "1111"      |             |
| PEND_THRESH_G     | natural              | 0           |             |
| BYP_SHIFT_G       | boolean              | false       |             |
## Ports

| Port name       | Direction | Type                                             | Description                 |
| --------------- | --------- | ------------------------------------------------ | --------------------------- |
| axiClk          | in        | sl                                               | Clock/Reset                 |
| axiRst          | in        | sl                                               |                             |
| axilReadMaster  | in        | AxiLiteReadMasterArray(AXIL_COUNT_G-1 downto 0)  | Register Access & Interrupt |
| axilReadSlave   | out       | AxiLiteReadSlaveArray(AXIL_COUNT_G-1 downto 0)   |                             |
| axilWriteMaster | in        | AxiLiteWriteMasterArray(AXIL_COUNT_G-1 downto 0) |                             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveArray(AXIL_COUNT_G-1 downto 0)  |                             |
| interrupt       | out       | sl                                               |                             |
| online          | out       | sl                                               |                             |
| acknowledge     | out       | sl                                               |                             |
| sAxisMaster     | in        | AxiStreamMasterType                              | AXI Stream Interface        |
| sAxisSlave      | out       | AxiStreamSlaveType                               |                             |
| mAxisMaster     | out       | AxiStreamMasterType                              |                             |
| mAxisSlave      | in        | AxiStreamSlaveType                               |                             |
| mAxisCtrl       | in        | AxiStreamCtrlType                                |                             |
| axiReadMaster   | out       | AxiReadMasterType                                | AXI Interface               |
| axiReadSlave    | in        | AxiReadSlaveType                                 |                             |
| axiWriteMaster  | out       | AxiWriteMasterType                               |                             |
| axiWriteSlave   | in        | AxiWriteSlaveType                                |                             |
| axiWriteCtrl    | in        | AxiCtrlType                                      |                             |
## Signals

| Name            | Type                                     | Description |
| --------------- | ---------------------------------------- | ----------- |
| r               | RegType                                  |             |
| rin             | RegType                                  |             |
| ib              | IbType                                   |             |
| ibin            | IbType                                   |             |
| ob              | ObType                                   |             |
| obin            | ObType                                   |             |
| intReadMasters  | AxiLiteReadMasterArray(1 downto 0)       |             |
| intReadSlaves   | AxiLiteReadSlaveArray(1 downto 0)        |             |
| intWriteMasters | AxiLiteWriteMasterArray(1 downto 0)      |             |
| intWriteSlaves  | AxiLiteWriteSlaveArray(1 downto 0)       |             |
| popFifoClk      | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| popFifoRst      | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| popFifoValid    | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| popFifoWrite    | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| popFifoPFull    | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| popFifoDin      | Slv32Array(POP_FIFO_COUNT_C-1 downto 0)  |             |
| pushFifoClk     | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| pushFifoRst     | slv(POP_FIFO_COUNT_C-1 downto 0)         |             |
| pushFifoValid   | slv(PUSH_FIFO_COUNT_C-1 downto 0)        |             |
| pushFifoDout    | Slv36Array(PUSH_FIFO_COUNT_C-1 downto 0) |             |
| pushFifoRead    | slv(PUSH_FIFO_COUNT_C-1 downto 0)        |             |
| obAck           | AxiReadDmaAckType                        |             |
| obReq           | AxiReadDmaReqType                        |             |
| ibAck           | AxiWriteDmaAckType                       |             |
| ibReq           | AxiWriteDmaReqType                       |             |
## Constants

| Name                          | Type                                         | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description |
| ----------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PUSH_ADDR_WIDTH_C             | integer                                      |  FREE_ADDR_WIDTH_G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| POP_ADDR_WIDTH_C              | integer                                      |  FREE_ADDR_WIDTH_G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| POP_FIFO_PFULL_C              | integer                                      |  (2**POP_ADDR_WIDTH_C) - 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| POP_FIFO_COUNT_C              | integer                                      |  2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| PUSH_FIFO_COUNT_C             | integer                                      |  2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| IB_FIFO_C                     | integer                                      |  0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| OB_FIFO_C                     | integer                                      |  1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| CROSSBAR_CONN_C               | slv(15 downto 0)                             |  x"FFFF"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| LOC_INDEX_C                   | natural                                      |  0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| LOC_BASE_ADDR_C               | slv(31 downto 0)                             |  AXIL_BASE_ADDR_G(31 downto 12) & x"000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| LOC_NUM_BITS_C                | natural                                      |  10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| FIFO_INDEX_C                  | natural                                      |  1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |             |
| FIFO_BASE_ADDR_C              | slv(31 downto 0)                             |  AXIL_BASE_ADDR_G(31 downto 12) & x"400"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |             |
| FIFO_NUM_BITS_C               | natural                                      |  10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |             |
| AXI_CROSSBAR_MASTERS_CONFIG_C | AxiLiteCrossbarMasterConfigArray(1 downto 0) |  (       LOC_INDEX_C     => (          baseAddr     => LOC_BASE_ADDR_C,<br><span style="padding-left:20px">          addrBits     => LOC_NUM_BITS_C,<br><span style="padding-left:20px">          connectivity => CROSSBAR_CONN_C),<br><span style="padding-left:20px">       FIFO_INDEX_C    => (          baseAddr     => FIFO_BASE_ADDR_C,<br><span style="padding-left:20px">          addrBits     => FIFO_NUM_BITS_C,<br><span style="padding-left:20px">          connectivity => CROSSBAR_CONN_C))                                                                                                                                                                                                                                                                                                                        |             |
| REG_INIT_C                    | RegType                                      |  (       maxRxSize     => (others => '0'),<br><span style="padding-left:20px">       interrupt     => '0',<br><span style="padding-left:20px">       intEnable     => '0',<br><span style="padding-left:20px">       intAck        => '0',<br><span style="padding-left:20px">       acknowledge   => '0',<br><span style="padding-left:20px">       online        => '0',<br><span style="padding-left:20px">       rxEnable      => '0',<br><span style="padding-left:20px">       txEnable      => '0',<br><span style="padding-left:20px">       fifoClear     => '1',<br><span style="padding-left:20px">       swCache       => AXI_CACHE_G,<br><span style="padding-left:20px">       axiReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axiWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C) |             |
| IB_INIT_C                     | IbType                                       |  (       state        => IDLE_S,<br><span style="padding-left:20px">       intPending   => '0',<br><span style="padding-left:20px">       ibReq        => AXI_WRITE_DMA_REQ_INIT_C,<br><span style="padding-left:20px">       popFifoWrite => '0',<br><span style="padding-left:20px">       popFifoDin   => (others => '0'),<br><span style="padding-left:20px">       pushFifoRead => '0')                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| OB_INIT_C                     | ObType                                       |  (       state        => IDLE_S,<br><span style="padding-left:20px">       intPending   => '0',<br><span style="padding-left:20px">       obReq        => AXI_READ_DMA_REQ_INIT_C,<br><span style="padding-left:20px">       popFifoWrite => '0',<br><span style="padding-left:20px">       popFifoDin   => (others => '0'),<br><span style="padding-left:20px">       pushFifoRead => '0')                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
## Types

| Name      | Type                                                                                                                                               | Description |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_S,<br><span style="padding-left:20px"> FIFO_0_S,<br><span style="padding-left:20px"> FIFO_1_S)  |             |
| RegType   |                                                                                                                                                    |             |
| IbType    |                                                                                                                                                    |             |
| ObType    |                                                                                                                                                    |             |
## Processes
- unnamed: ( axiClk )
- unnamed: ( axiRst, ib, intReadMasters, intWriteMasters, ob, popFifoValid, r )
**Description**
-----------------------------------  Local Register Space ----------------------------------- 
- unnamed: ( axiRst, ib, ibAck, popFifoPFull, pushFifoDout, pushFifoValid, r )
- unnamed: ( axiRst, ob, obAck, pushFifoDout, pushFifoValid, r )
## Instantiations

- U_SwFifos: surf.AxiLiteFifoPushPop
- U_IbDma: surf.AxiStreamDmaWrite
**Description**
-----------------------------------
 Inbound Controller
-----------------------------------

- U_ObDma: surf.AxiStreamDmaRead
**Description**
-----------------------------------
 Outbound Controller
-----------------------------------

