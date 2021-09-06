# Entity: JesdTxLane

- **File**: JesdTxLane.vhd
## Diagram

![Diagram](JesdTxLane.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: JesdTx transmit single lane module
              Transmitter for JESD204b standard.
              Supports sub-class 1 deterministic latency.
              Supports sub-class 0 non deterministic latency
              Features:
              - Synchronization FSM
              - Comma transmission
              - ILA Sequence generation
              - Control character generation:
                   - A(K28.3) - x"7C" - End of multi-frame
                   - F(K28.7) - x"FC" - Inserted at the end of the frame
             Status register encoding:
                bit 0: GT Reset done
                bit 1: Transmuting valid data
                bit 2: Transmitting ILA sequence
                bit 3: Synchronization input status
                bit 4: TX module enabled status
                bit 5: SysRef detected (active only when the lane is enabled)

          Note: sampleData_i should be big endian and not byte swapped
                First sample in time:  sampleData_i(31 downto 16)
                Second sample in time: sampleData_i(15 downto 0)
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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| TPD_G        | time     | 1 ns  |             |
| F_G          | positive | 2     |             |
| K_G          | positive | 32    |             |
## Ports

| Port name    | Direction | Type                               | Description                                  |
| ------------ | --------- | ---------------------------------- | -------------------------------------------- |
| devClk_i     | in        | sl                                 | JESDClocks and Resets                        |
| devRst_i     | in        | sl                                 |                                              |
| subClass_i   | in        | sl                                 | JESD subclass selection: '0' or '1'(default) |
| enable_i     | in        | sl                                 | Control register                             |
| replEnable_i | in        | sl                                 |                                              |
| scrEnable_i  | in        | sl                                 |                                              |
| inv_i        | in        | sl                                 |                                              |
| lmfc_i       | in        | sl                                 | Local multi frame clock                      |
| nSync_i      | in        | sl                                 | Synchronization request input                |
| gtTxReady_i  | in        | sl                                 | GT is ready to transmit data after reset     |
| sysRef_i     | in        | sl                                 | SYSREF for subclass 1 fixed latency          |
| status_o     | out       | slv(TX_STAT_WIDTH_C-1 downto 0)    | Status of the transmitter                    |
| dacReady_o   | out       | sl                                 |                                              |
| sampleData_i | in        | slv((GT_WORD_SIZE_C*8)-1 downto 0) | Sample data input                            |
| r_jesdGtTx   | out       | jesdGtTxLaneType                   | Data and character output and GT signals     |
## Signals

| Name            | Type                        | Description |
| --------------- | --------------------------- | ----------- |
| s_dataValid     | sl                          |             |
| s_ila           | sl                          |             |
| s_refDetected   | sl                          |             |
| s_sampleDataMux | slv(r_jesdGtTx.data'range)  |  Data-path  |
| s_sampleKMux    | slv(r_jesdGtTx.dataK'range) |             |
| s_ilaDataMux    | slv(r_jesdGtTx.data'range)  |             |
| s_ilaKMux       | slv(r_jesdGtTx.dataK'range) |             |
| s_commaDataMux  | slv(r_jesdGtTx.data'range)  |             |
| s_commaKMux     | slv(r_jesdGtTx.dataK'range) |             |
| s_data_sel      | slv(1 downto 0)             |             |
## Instantiations

- syncFSM_INST: surf.JesdSyncFsmTx
- ilasGen_INST: surf.JesdIlasGen
</br>**Description**
--------------------------------------------------
 Initial Synchronization Data Sequence (ILAS)

- AlignChGen_INST: surf.JesdAlignChGen
</br>**Description**
--------------------------------------------------
 Sample data with added synchronization characters TODO

