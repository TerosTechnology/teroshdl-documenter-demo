# Entity: SspLowSpeedDecoder12b14bWrapper

- **File**: SspLowSpeedDecoder12b14bWrapper.vhd
## Diagram

![Diagram](SspLowSpeedDecoder12b14bWrapper.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: SSP Decoder Wrapper
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

| Generic name    | Type                    | Value | Description |
| --------------- | ----------------------- | ----- | ----------- |
| TPD_G           | time                    | 1 ns  |             |
| SIMULATION_G    | boolean                 | false |             |
| DLY_STEP_SIZE_G | positive range 1 to 255 | 1     |             |
| NUM_LANE_G      | positive                | 1     |             |
## Ports

| Port name       | Direction | Type                              | Description                                 |
| --------------- | --------- | --------------------------------- | ------------------------------------------- |
| deserClk        | in        | sl                                | Deserialization Interface (deserClk domain) |
| deserRst        | in        | sl                                |                                             |
| deserData       | in        | Slv8Array(NUM_LANE_G-1 downto 0)  |                                             |
| dlyLoad         | out       | slv(NUM_LANE_G-1 downto 0)        |                                             |
| dlyCfg          | out       | Slv9Array(NUM_LANE_G-1 downto 0)  |                                             |
| rxLinkUp        | out       | slv(NUM_LANE_G-1 downto 0)        | SSP Frame Output                            |
| rxValid         | out       | slv(NUM_LANE_G-1 downto 0)        |                                             |
| rxData          | out       | Slv12Array(NUM_LANE_G-1 downto 0) |                                             |
| rxSof           | out       | slv(NUM_LANE_G-1 downto 0)        |                                             |
| rxEof           | out       | slv(NUM_LANE_G-1 downto 0)        |                                             |
| rxEofe          | out       | slv(NUM_LANE_G-1 downto 0)        |                                             |
| axilClk         | in        | sl                                | AXI-Lite Interface (axilClk domain)         |
| axilRst         | in        | sl                                |                                             |
| axilReadMaster  | in        | AxiLiteReadMasterType             |                                             |
| axilReadSlave   | out       | AxiLiteReadSlaveType              |                                             |
| axilWriteMaster | in        | AxiLiteWriteMasterType            |                                             |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType             |                                             |
## Signals

| Name           | Type                             | Description |
| -------------- | -------------------------------- | ----------- |
| dlyConfig      | Slv9Array(NUM_LANE_G-1 downto 0) |             |
| enUsrDlyCfg    | sl                               |             |
| usrDlyCfg      | slv(8 downto 0)                  |             |
| minEyeWidth    | slv(7 downto 0)                  |             |
| lockingCntCfg  | slv(23 downto 0)                 |             |
| bypFirstBerDet | sl                               |             |
| lockOnIdle     | sl                               |             |
| bitOrder       | slv(1 downto 0)                  |             |
| errorMask      | slv(2 downto 0)                  |             |
| polarity       | slv(NUM_LANE_G-1 downto 0)       |             |
| errorDet       | slv(NUM_LANE_G-1 downto 0)       |             |
| bitSlip        | slv(NUM_LANE_G-1 downto 0)       |             |
| locked         | slv(NUM_LANE_G-1 downto 0)       |             |
| idleCode       | slv(NUM_LANE_G-1 downto 0)       |             |
## Constants

| Name         | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| DATA_WIDTH_C | positive |  12   |             |
## Instantiations

- U_Reg: surf.SspLowSpeedDecoderReg
