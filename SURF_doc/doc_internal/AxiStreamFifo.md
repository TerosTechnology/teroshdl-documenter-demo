# Entity: AxiStreamFifo

- **File**: AxiStreamFifo.vhd
## Diagram

![Diagram](AxiStreamFifo.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 Block to serve as an async FIFO for AXI Streams. This block also allows the
 bus to be compress/expanded, allowing different standard sizes on each side
 of the FIFO. Re-sizing is always little endian.
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

| Generic name           | Type                       | Value   | Description                                                                                                                                                                                           |
| ---------------------- | -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TPD_G                  | time                       | 1 ns    | General Configurations                                                                                                                                                                                |
| INT_PIPE_STAGES_G      | natural range 0 to 16      | 0       |  Internal FIFO setting                                                                                                                                                                                |
| PIPE_STAGES_G          | natural range 0 to 16      | 1       |                                                                                                                                                                                                       |
| SLAVE_READY_EN_G       | boolean                    | true    |                                                                                                                                                                                                       |
| VALID_THOLD_G          | integer range 0 to (2**24) | 1       |  =1 = normal operation                                                                                                                                                                                |
| MEMORY_TYPE_G          | string                     | "block" | =0 = only when frame ready >1 = only when frame ready or # entries FIFO configurations                                                                                                                |
| GEN_SYNC_FIFO_G        | boolean                    | false   |                                                                                                                                                                                                       |
| CASCADE_SIZE_G         | integer range 1 to (2**24) | 1       |                                                                                                                                                                                                       |
| FIFO_ADDR_WIDTH_G      | integer range 4 to 48      | 9       |                                                                                                                                                                                                       |
| FIFO_FIXED_THRESH_G    | boolean                    | true    |                                                                                                                                                                                                       |
| FIFO_PAUSE_THRESH_G    | integer range 1 to (2**24) | 1       |                                                                                                                                                                                                       |
| LAST_FIFO_ADDR_WIDTH_G | integer range 0 to 48      | 0       | If VALID_THOLD_G /=1, FIFO that stores on tLast txns can be smaller. Set to 0 for same size as primary fifo (default) Set >4 for custom size. Use at own risk. Overflow of tLast fifo is not checked  |
| CASCADE_PAUSE_SEL_G    | integer range 0 to (2**24) | 0       | Index = 0 is output, index = n is input                                                                                                                                                               |
| SLAVE_AXI_CONFIG_G     | AxiStreamConfigType        |         | AXI Stream Port Configurations                                                                                                                                                                        |
| MASTER_AXI_CONFIG_G    | AxiStreamConfigType        |         |                                                                                                                                                                                                       |
## Ports

| Port name       | Direction | Type                                         | Description                                    |
| --------------- | --------- | -------------------------------------------- | ---------------------------------------------- |
| sAxisClk        | in        | sl                                           | Slave Port                                     |
| sAxisRst        | in        | sl                                           |                                                |
| sAxisMaster     | in        | AxiStreamMasterType                          |                                                |
| sAxisSlave      | out       | AxiStreamSlaveType                           |                                                |
| sAxisCtrl       | out       | AxiStreamCtrlType                            |                                                |
| fifoPauseThresh | in        | slv(FIFO_ADDR_WIDTH_G-1 downto 0)            | FIFO status & config , synchronous to sAxisClk |
| mAxisClk        | in        | sl                                           | Master Port                                    |
| mAxisRst        | in        | sl                                           |                                                |
| mAxisMaster     | out       | AxiStreamMasterType                          |                                                |
| mAxisSlave      | in        | AxiStreamSlaveType                           |                                                |
| mTLastTUser     | out       | slv(AXI_STREAM_MAX_TDATA_WIDTH_C-1 downto 0) |                                                |
## Signals

| Name          | Type                              | Description                                  |
| ------------- | --------------------------------- | -------------------------------------------- |
| wrR           | WrRegType                         |                                              |
| wrRin         | WrRegType                         |                                              |
| fifoDin       | slv(FIFO_BITS_C-1 downto 0)       | --------------  FIFO Signals --------------  |
| fifoWrite     | sl                                |                                              |
| fifoWriteLast | sl                                |                                              |
| fifoWriteUser | slv(FIFO_USER_TOT_C-1 downto 0)   |                                              |
| fifoWrCount   | slv(FIFO_ADDR_WIDTH_G-1 downto 0) |                                              |
| fifoRdCount   | slv(FIFO_ADDR_WIDTH_G-1 downto 0) |                                              |
| fifoAFull     | sl                                |                                              |
| fifoReady     | sl                                |                                              |
| fifoPFull     | sl                                |                                              |
| fifoPFullVec  | slv(CASCADE_SIZE_G-1 downto 0)    |                                              |
| fifoDout      | slv(FIFO_BITS_C-1 downto 0)       |                                              |
| fifoRead      | sl                                |                                              |
| fifoReadLast  | sl                                |                                              |
| fifoReadUser  | slv(FIFO_USER_TOT_C-1 downto 0)   |                                              |
| fifoValidInt  | sl                                |                                              |
| fifoValid     | sl                                |                                              |
| fifoValidLast | sl                                |                                              |
| fifoInFrame   | sl                                |                                              |
| rdR           | RdRegType                         |                                              |
| rdRin         | RdRegType                         |                                              |
| axisMaster    | AxiStreamMasterType               | -------------  Sync Signals -------------    |
| axisSlave     | AxiStreamSlaveType                |                                              |
## Constants

| Name                   | Type                  | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                 |
| ---------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| FIFO_AXIS_CONFIG_C     | AxiStreamConfigType   |  ite(SLAVE_AXI_CONFIG_G.TDATA_BYTES_C > MASTER_AXI_CONFIG_G.TDATA_BYTES_C,<br><span style="padding-left:20px"> SLAVE_AXI_CONFIG_G,<br><span style="padding-left:20px"> MASTER_AXI_CONFIG_G)                                                                                                                                                                                                                                                                                                                                                                     |                                                             |
| LAST_FIFO_ADDR_WIDTH_C | integer range 4 to 48 |        ite(LAST_FIFO_ADDR_WIDTH_G < 4,<br><span style="padding-left:20px"> FIFO_ADDR_WIDTH_G,<br><span style="padding-left:20px"> LAST_FIFO_ADDR_WIDTH_G)                                                                                                                                                                                                                                                                                                                                                                                                       |                                                             |
| WR_BYTES_C             | integer               |  SLAVE_AXI_CONFIG_G.TDATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                             |
| RD_BYTES_C             | integer               |  MASTER_AXI_CONFIG_G.TDATA_BYTES_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                             |
| DATA_BYTES_C           | integer               |  maximum(SLAVE_AXI_CONFIG_G.TDATA_BYTES_C,<br><span style="padding-left:20px"> MASTER_AXI_CONFIG_G.TDATA_BYTES_C)                                                                                                                                                                                                                                                                                                                                                                                                                                               |  Use wider of two interfaces                                |
| DATA_BITS_C            | integer               |  (DATA_BYTES_C * 8)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                             |
| KEEP_MODE_C            | TKeepModeType         |  SLAVE_AXI_CONFIG_G.TKEEP_MODE_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  Use SLAVE TKEEP Mode                                       |
| KEEP_BITS_C            | integer               |  ite(KEEP_MODE_C = TKEEP_NORMAL_C,<br><span style="padding-left:20px"> DATA_BYTES_C,<br><span style="padding-left:20px">                                          ite(KEEP_MODE_C = TKEEP_COMP_C,<br><span style="padding-left:20px"> bitSize(DATA_BYTES_C-1),<br><span style="padding-left:20px"> 0))                                                                                                                                                                                                                                                          |                                                             |
| USER_MODE_C            | TUserModeType         |  ite(((WR_BYTES_C = 1) or (RD_BYTES_C = 1)),<br><span style="padding-left:20px"> TUSER_NORMAL_C,<br><span style="padding-left:20px"> SLAVE_AXI_CONFIG_G.TUSER_MODE_C)                                                                                                                                                                                                                                                                                                                                                                                           |  User user bit mode of slave                                |
| SLAVE_USER_BITS_C      | integer               |  SLAVE_AXI_CONFIG_G.TUSER_BITS_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  Use whichever interface has the least number of user bits  |
| MASTER_USER_BITS_C     | integer               |  MASTER_AXI_CONFIG_G.TUSER_BITS_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                             |
| FIFO_USER_BITS_C       | integer               |  minimum(SLAVE_USER_BITS_C,<br><span style="padding-left:20px"> MASTER_USER_BITS_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                                             |
| FIFO_USER_TOT_C        | integer               |  ite(USER_MODE_C = TUSER_FIRST_LAST_C,<br><span style="padding-left:20px"> FIFO_USER_BITS_C*2,<br><span style="padding-left:20px">                                              ite(USER_MODE_C = TUSER_LAST_C,<br><span style="padding-left:20px"> FIFO_USER_BITS_C,<br><span style="padding-left:20px">                                                  ite(USER_MODE_C = TUSER_NORMAL_C,<br><span style="padding-left:20px"> DATA_BYTES_C * FIFO_USER_BITS_C,<br><span style="padding-left:20px">                                                      1))) |                                                             |
| STRB_BITS_C            | integer               |  ite(SLAVE_AXI_CONFIG_G.TSTRB_EN_C,<br><span style="padding-left:20px"> DATA_BYTES_C,<br><span style="padding-left:20px"> 0)                                                                                                                                                                                                                                                                                                                                                                                                                                    |  Use SLAVE settings for strobe, dest and ID bit values      |
| DEST_BITS_C            | integer               |  SLAVE_AXI_CONFIG_G.TDEST_BITS_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                             |
| ID_BITS_C              | integer               |  SLAVE_AXI_CONFIG_G.TID_BITS_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                             |
| FIFO_BITS_C            | integer               |  1 + DATA_BITS_C + KEEP_BITS_C + FIFO_USER_TOT_C + STRB_BITS_C + DEST_BITS_C + ID_BITS_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                             |
| WR_LOGIC_EN_C          | boolean               |  (WR_BYTES_C < RD_BYTES_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | --------------  Write Signals --------------                |
| WR_SIZE_C              | integer               |  ite(WR_LOGIC_EN_C,<br><span style="padding-left:20px"> RD_BYTES_C / WR_BYTES_C,<br><span style="padding-left:20px"> 1)                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                             |
| WR_REG_INIT_C          | WrRegType             |  (       count    => (others => '0'),<br><span style="padding-left:20px">       wrMaster => axiStreamMasterInit(SLAVE_AXI_CONFIG_G)       )                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                             |
| RD_LOGIC_EN_C          | boolean               |  (RD_BYTES_C < WR_BYTES_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | -------------  Read Signals -------------                   |
| RD_SIZE_C              | integer               |  ite(RD_LOGIC_EN_C,<br><span style="padding-left:20px"> WR_BYTES_C / RD_BYTES_C,<br><span style="padding-left:20px"> 1)                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                             |
| RD_REG_INIT_C          | RdRegType             |  (       count    => (others => '0'),<br><span style="padding-left:20px">       bytes    => conv_std_logic_vector(RD_BYTES_C,<br><span style="padding-left:20px"> bitSize(DATA_BYTES_C)),<br><span style="padding-left:20px">       rdMaster => axiStreamMasterInit(MASTER_AXI_CONFIG_G),<br><span style="padding-left:20px">       ready    => '0'       )                                                                                                                                                                                                     |                                                             |
## Types

| Name      | Type | Description |
| --------- | ---- | ----------- |
| WrRegType |      |             |
| RdRegType |      |             |
## Functions
- iAxiToSlv <font id="function_arguments">(din : AxiStreamMasterType) </font> <font id="function_return">return slv </font>
</br>**Description**
 Convert record to slv

- iSlvToAxi <font id="function_arguments">(din     : in    slv(FIFO_BITS_C-1 downto 0);<br><span style="padding-left:20px"> valid   : in    sl;<br><span style="padding-left:20px"> master  : inout AxiStreamMasterType;<br><span style="padding-left:20px"> byteCnt : inout integer) </font> <font id="function_return">return ()</font>
</br>**Description**
 Convert slv to record

## Processes
- wrComb: ( fifoReady, sAxisMaster, wrR )
</br>**Description**
-----------------------  Write Logic ----------------------- 
- wrSeq: ( sAxisClk )
- unnamed: ( fifoPFullVec, sAxisClk )
</br>**Description**
-----------------------  FIFO -----------------------  Pause generation 
- rdComb: ( axisSlave, fifoDout, fifoValid, rdR )
</br>**Description**
-----------------------  Read Logic ----------------------- 
- rdSeq: ( mAxisClk )
</br>**Description**
 If fifo is asynchronous, must use async reset on rd side. 
## Instantiations

- U_Fifo: surf.FifoCascade
- Synchronizer_1: surf.Synchronizer
</br>**Description**
 Synchronize master side tvalid back to slave side ctrl.idle
 This is a total hack

- U_Pipe: surf.AxiStreamPipeline
</br>**Description**
-----------------------
 Pipeline Logic
-----------------------

