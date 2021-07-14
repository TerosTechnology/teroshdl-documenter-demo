# Package: spi_device_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Serial Peripheral Interface (SPI) Device module.
 

## Signals

| Name           | Type       | Description |
| -------------- | ---------- | ----------- |
| spi_device_pkg | endpackage |             |
## Constants

| Name              | Type         | Value                                  | Description                           |
| ----------------- | ------------ | -------------------------------------- | ------------------------------------- |
| SramAw            | int unsigned | $clog2(spi_device_reg_pkg::SramDepth)  |                                       |
| SramReadBufferIdx | sram_addr_t  | sram_addr_t'(0)                        | Calculate each space's base and size  |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| SramMailboxIdx    | sram_addr_t  | SramReadBufferIdx + SramReadBufferSize |                                       |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| SramSfdpIdx       | sram_addr_t  | SramMailboxIdx + SramMailboxSize       |                                       |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| SramPayloadIdx    | sram_addr_t  | SramSfdpIdx + SramSfdpSize             |                                       |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| SramCmdFifoIdx    | sram_addr_t  | SramPayloadIdx + SramPayloadSize       |                                       |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| SramAddrFifoIdx   | sram_addr_t  | SramCmdFifoIdx + SramCmdFifoSize       |                                       |
| sram_addr_t       | sram_addr_t  | undefined                              |                                       |
| BitLength         | int unsigned | SramMsgDepth * 32                      | Max BitCount in a transaction         |
| BitCntW           | int unsigned | $clog2(BitLength + 1)                  |                                       |
## Types

| Name              | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| passthrough_req_t | struct packed {<br><span style="padding-left:20px">               logic       passthrough_en;<br><span style="padding-left:20px">                logic       sck;<br><span style="padding-left:20px">     logic       sck_gate_en;<br><span style="padding-left:20px">      logic       sck_en;<br><span style="padding-left:20px">                     logic       csb;<br><span style="padding-left:20px">     logic       csb_en;<br><span style="padding-left:20px">           logic [3:0] s;<br><span style="padding-left:20px">     logic [3:0] s_en;<br><span style="padding-left:20px">   } |                            |
| passthrough_rsp_t | struct packed {<br><span style="padding-left:20px">          logic [3:0] s;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                            |
| sram_addr_t       | logic [SramAw-1:0]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                            |
| sram_data_t       | struct packed {<br><span style="padding-left:20px">     logic [SramDw-1:0]   data;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                            |
| sram_err_t        | struct packed {<br><span style="padding-left:20px">     logic uncorr;<br><span style="padding-left:20px">     logic corr;<br><span style="padding-left:20px">   }                                                                                                                                                                                                                                                                                                                                                                                                                                   |                            |
| scan_mode_e       | enum logic [2:0] {<br><span style="padding-left:20px">     ClkInvSel,<br><span style="padding-left:20px">     CsbRstMuxSel,<br><span style="padding-left:20px">     TxRstMuxSel,<br><span style="padding-left:20px">     RxRstMuxSel,<br><span style="padding-left:20px">     ClkMuxSel,<br><span style="padding-left:20px">     ClkSramSel,<br><span style="padding-left:20px">     RstSramSel,<br><span style="padding-left:20px">     ScanModeUseLast   }                                                                                                                                        | spi device scanmode usage  |
