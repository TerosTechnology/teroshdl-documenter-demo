# Entity: Jesd204bRx

- **File**: Jesd204bRx.vhd
## Diagram

![Diagram](Jesd204bRx.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: JESD204b multi-lane receiver module
             Receiver JESD204b module.
             Supports a subset of features from JESD204b standard.
             Supports sub-class 1 deterministic latency.
             Supports sub-class 0 non deterministic latency.
             Features:
             - Synchronization of LMFC to SYSREF
             - Multi-lane operation (L_G: 1-16)
             - Lane alignment using RX buffers
             - Serial lane error check
             - Alignment character replacement and alignment check
         Note: sampleDataArr_o is little endian and not byte-swapped
               First sample in time:  sampleData_o(15 downto 0)
               Second sample in time: sampleData_o(31 downto 16)
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name | Type                   | Value | Description                                          |
| ------------ | ---------------------- | ----- | ---------------------------------------------------- |
| TPD_G        | time                   | 1 ns  |                                                      |
| GEN_ASYNC_G  | boolean                | false | default false don't add synchronizer                 |
| TEST_G       | boolean                | false | Test tx module instead of GTX                        |
| F_G          | positive               | 2     | JESD generics Number of bytes in a frame (1,2,or 4)  |
| K_G          | positive               | 32    | Number of frames in a multi frame (32)               |
| L_G          | positive range 1 to 32 | 2     | Number of RX lanes (1 to 32)                         |
## Ports

| Port name       | Direction | Type                                  | Description                                                            |
| --------------- | --------- | ------------------------------------- | ---------------------------------------------------------------------- |
| axiClk          | in        | sl                                    | AXI interfaceClocks and Resets                                         |
| axiRst          | in        | sl                                    |                                                                        |
| axilReadMaster  | in        | AxiLiteReadMasterType                 | AXI-Lite Register Interface                                            |
| axilReadSlave   | out       | AxiLiteReadSlaveType                  |                                                                        |
| axilWriteMaster | in        | AxiLiteWriteMasterType                |                                                                        |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                 |                                                                        |
| sampleDataArr_o | out       | sampleDataArray(L_G-1 downto 0)       | Sample data output (Use if external data acquisition core is attached) |
| dataValidVec_o  | out       | slv(L_G-1 downto 0)                   |                                                                        |
| devClk_i        | in        | sl                                    | JESDClocks and Resets                                                  |
| devRst_i        | in        | sl                                    |                                                                        |
| sysRef_i        | in        | sl                                    | SYSREF for subclass 1 fixed latency                                    |
| sysRefDbg_o     | out       | sl                                    | SYSREF output for debug                                                |
| r_jesdGtRxArr   | in        | jesdGtRxLaneTypeArray(L_G-1 downto 0) | Data and character inputs from GT (transceivers)                       |
| gtRxReset_o     | out       | slv(L_G-1 downto 0)                   |                                                                        |
| rxPowerDown     | out       | slv(L_G-1 downto 0)                   |                                                                        |
| rxPolarity      | out       | slv(L_G-1 downto 0)                   |                                                                        |
| nSync_o         | out       | sl                                    | Synchronization output combined from all receivers                     |
| pulse_o         | out       | slv(L_G-1 downto 0)                   | Debug signals                                                          |
| leds_o          | out       | slv(1 downto 0)                       |                                                                        |
## Signals

| Name              | Type                                  | Description                                      |
| ----------------- | ------------------------------------- | ------------------------------------------------ |
| r                 | RegType                               |                                                  |
| rin               | RegType                               |                                                  |
| s_lmfc            | sl                                    | Internal signalsLocal Multi Frame Clock          |
| s_nSyncVec        | slv(L_G-1 downto 0)                   | Synchronization output generation                |
| s_nSyncVecEn      | slv(L_G-1 downto 0)                   |                                                  |
| s_dataValidVec    | slv(L_G-1 downto 0)                   |                                                  |
| s_nSyncAll        | sl                                    |                                                  |
| s_nSyncAny        | sl                                    |                                                  |
| s_sysrefDlyRx     | slv(SYSRF_DLY_WIDTH_C-1 downto 0)     |                                                  |
| s_enableRx        | slv(L_G-1 downto 0)                   |                                                  |
| s_replEnable      | sl                                    |                                                  |
| s_scrEnable       | sl                                    |                                                  |
| s_invertData      | slv(L_G-1 downto 0)                   |                                                  |
| s_subClass        | sl                                    | JESD subclass selection (from AXI lite register) |
| s_gtReset         | sl                                    | User reset (from AXI lite register)              |
| s_invertSync      | sl                                    |                                                  |
| s_clearErr        | sl                                    |                                                  |
| s_statusRxArr     | rxStatuRegisterArray(L_G-1 downto 0)  |                                                  |
| s_thresoldHighArr | Slv16Array(L_G-1 downto 0)            |                                                  |
| s_thresoldLowArr  | Slv16Array(L_G-1 downto 0)            |                                                  |
| s_dlyTxArr        | Slv4Array(L_G-1 downto 0)             | Testing registers                                |
| s_alignTxArr      | alignTxArray(L_G-1 downto 0)          |                                                  |
| s_sampleDataArr   | sampleDataArray(L_G-1 downto 0)       |                                                  |
| s_sysrefSync      | sl                                    | Sysref conditioning                              |
| s_sysrefD         | sl                                    |                                                  |
| s_sysrefRe        | sl                                    |                                                  |
| s_jesdGtRxArr     | jesdGtRxLaneTypeArray(L_G-1 downto 0) | Record containing GT signals                     |
| s_rawData         | slv32Array(L_G-1 downto 0)            |                                                  |
| s_linkErrMask     | slv(5 downto 0)                       | Generate pause signal logic OR                   |
## Constants

| Name       | Type    | Value                              | Description |
| ---------- | ------- | ---------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       nSyncAnyD1 => '0'       ) |             |
## Types

| Name    | Type | Description |
| ------- | ---- | ----------- |
| RegType |      |             |
## Processes
- comb: ( devRst_i, s_nSyncAny )
**Description**
DFF

- seq: ( devClk_i )
## Instantiations

- U_Reg: surf.JesdRxReg
**Description**
axiLite register interface

- U_SysrefDly: surf.SlvDelay
**Description**
Delay SYSREF input (for 1 to 256 c-c)

- LmfcGen_INST: surf.JesdLmfcGen
**Description**
LMFC period generator aligned to SYSREF input

