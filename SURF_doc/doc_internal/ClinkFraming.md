# Entity: ClinkFraming

- **File**: ClinkFraming.vhd
## Diagram

![Diagram](ClinkFraming.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description:
 CameraLink framing module
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

| Generic name       | Type                | Value | Description             |
| ------------------ | ------------------- | ----- | ----------------------- |
| TPD_G              | time                | 1 ns  |                         |
| COMMON_DATA_CLK_G  | boolean             | false |  true if dataClk=sysClk |
| DATA_AXIS_CONFIG_G | AxiStreamConfigType |       |                         |
## Ports

| Port name  | Direction | Type                          | Description            |
| ---------- | --------- | ----------------------------- | ---------------------- |
| sysClk     | in        | sl                            | System clock and reset |
| sysRst     | in        | sl                            |                        |
| chanConfig | in        | ClChanConfigType              | Config and status      |
| chanStatus | out       | ClChanStatusType              |                        |
| linkStatus | in        | ClLinkStatusArray(2 downto 0) |                        |
| parData    | in        | Slv28Array(2 downto 0)        | Data interface         |
| parValid   | in        | slv(2 downto 0)               |                        |
| parReady   | out       | sl                            |                        |
| dataClk    | in        | sl                            | Camera data            |
| dataRst    | in        | sl                            |                        |
| dataMaster | out       | AxiStreamMasterType           |                        |
| dataSlave  | in        | AxiStreamSlaveType            |                        |
## Signals

| Name       | Type                | Description |
| ---------- | ------------------- | ----------- |
| r          | RegType             |             |
| rin        | RegType             |             |
| intCtrl    | AxiStreamCtrlType   |             |
| packMaster | AxiStreamMasterType |             |
## Constants

| Name         | Type                | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| SLV_CONFIG_C | AxiStreamConfigType |  ssiAxiStreamConfig(dataBytes => 16,<br><span style="padding-left:20px"> tDestBits => 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| MST_CONFIG_C | AxiStreamConfigType |  ssiAxiStreamConfig(dataBytes => 16,<br><span style="padding-left:20px"> tDestBits => 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |             |
| REG_INIT_C   | RegType             |  (       ready    => '1',<br><span style="padding-left:20px">       portData => CL_DATA_INIT_C,<br><span style="padding-left:20px">       byteData => CL_DATA_INIT_C,<br><span style="padding-left:20px">       bytes    => 1,<br><span style="padding-left:20px">       inFrame  => '0',<br><span style="padding-left:20px">       dump     => '0',<br><span style="padding-left:20px">       status   => CL_CHAN_STATUS_INIT_C,<br><span style="padding-left:20px">       master   => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       pipeline => (others => AXI_STREAM_MASTER_INIT_C)) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( chanConfig, intCtrl, linkStatus, parData, parValid, r,
                   sysRst )
- seq: ( sysClk )
## Instantiations

- U_Pack: surf.AxiStreamBytePacker
**Description**
-------------------------------
 Frame Packing
-------------------------------

- U_DataFifo: surf.AxiStreamFifoV2
**Description**
-------------------------------
 Data FIFO
-------------------------------

