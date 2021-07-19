# Entity: AxiRssiTxFsm

- **File**: AxiRssiTxFsm.vhd
## Diagram

![Diagram](AxiRssiTxFsm.svg "Diagram")
## Description

Title      : RSSI Protocol: https://confluence.slac.stanford.edu/x/1IyfD
Company    : SLAC National Accelerator Laboratory
Description: Transmitter FSM
             Transmitter has the following functionality:
             Handle buffer addresses and buffer window (firstUnackAddr,nextSentAddr,lastSentAddr, bufferFull, bufferEmpty)
             Application side FSM. Receive SSI frame and store into TX data buffer.
                  - IDLE Waits until buffer window is free (not bufferFull),
                  - Waits for Application side SOF,
                  - Save the segment to Rx buffer at nextSentAddr. Disable sending of NULL segments with appBusy flag,
                  - When EOF received save segment length and keep flags. Check length error,
                  - Request data send at Transport side FSM and increment nextSentAddr
                  - Wait until the data is processed and data segment sent by Transport side FSM
                  - Release appBusy flag and go back to INIT.
             Acknowledgment FSM.
                  - IDLE Waits for ack_i (ack request) and ackN_i(ack number)(from RxFSM),
                  - Increments firstUnackAddr until the ackN_i is found in Window buffer,
                  - If it does not find the SEQ number it reports Ack Error,
                  - Goes back to IDLE.
             Transport side FSM. Send and resend various segments to Transport side.
                  - INIT Initializes seqN to initSeqN. Waits until new connection requested. ConnFSM goin out od Closed state.
                  - DISS_CONN allows sending SYN, ACK, or RST segments. Goes to CONN when connection becomes active.
                  - CONN allows sending DATA, NULL, ACK, or RST segments.
                    In Resend procedure the FSM resends all the unacknowledged (DATA, NULL, RST) segments in the buffer window.
             Note:Sequence number is incremented with sending SYN, DATA, NULL, and RST segments.
             Note:Only the following segments are saved into Tx buffer DATA, NULL, and RST.
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name        | Type          | Value | Description                                              |
| ------------------- | ------------- | ----- | -------------------------------------------------------- |
| TPD_G               | time          | 1 ns  |                                                          |
| AXI_CONFIG_G        | AxiConfigType |       |                                                          |
| BURST_BYTES_G       | positive      | 1024  |                                                          |
| WINDOW_ADDR_SIZE_G  | positive      | 3     | 2^WINDOW_ADDR_SIZE_G  = Number of segments               |
| SEGMENT_ADDR_SIZE_G | positive      | 7     | 2^SEGMENT_ADDR_SIZE_G = Number of 64 bit wide data words |
| HEADER_CHKSUM_EN_G  | boolean       | true  |                                                          |
## Ports

| Port name         | Direction | Type                                          | Description                                                      |
| ----------------- | --------- | --------------------------------------------- | ---------------------------------------------------------------- |
| clk_i             | in        | sl                                            |                                                                  |
| rst_i             | in        | sl                                            |                                                                  |
| axiOffset_i       | in        | slv(63 downto 0)                              | AXI Segment Buffer Interface                                     |
| mAxiWriteMaster_o | out       | AxiWriteMasterType                            |                                                                  |
| mAxiWriteSlave_i  | in        | AxiWriteSlaveType                             |                                                                  |
| mAxiReadMaster_o  | out       | AxiReadMasterType                             |                                                                  |
| mAxiReadSlave_i   | in        | AxiReadSlaveType                              |                                                                  |
| appMaster_i       | in        | AxiStreamMasterType                           | Inbound Application Interface                                    |
| appSlave_o        | out       | AxiStreamSlaveType                            |                                                                  |
| tspMaster_o       | out       | AxiStreamMasterType                           | Outbound Transport Interface                                     |
| tspSlave_i        | in        | AxiStreamSlaveType                            |                                                                  |
| connActive_i      | in        | sl                                            | Connection FSM indicating active connection                      |
| closed_i          | in        | sl                                            | Closed state in connFSM (initialize seqN)                        |
| injectFault_i     | in        | sl                                            | Fault injection corrupts header checksum                         |
| sndSyn_i          | in        | sl                                            | Various segment requests                                         |
| sndAck_i          | in        | sl                                            |                                                                  |
| sndRst_i          | in        | sl                                            |                                                                  |
| sndResend_i       | in        | sl                                            |                                                                  |
| sndNull_i         | in        | sl                                            |                                                                  |
| windowSize_i      | in        | integer range 1 to 2 ** (WINDOW_ADDR_SIZE_G)  | Window buff size (Depends on the number of outstanding segments) |
| bufferSize_i      | in        | integer range 1 to 2 ** (SEGMENT_ADDR_SIZE_G) |                                                                  |
| rdHeaderAddr_o    | out       | slv(7 downto 0)                               | Header read                                                      |
| rdHeaderData_i    | in        | slv(RSSI_WORD_WIDTH_C*8-1 downto 0)           |                                                                  |
| initSeqN_i        | in        | slv(7 downto 0)                               | Initial sequence number                                          |
| txSeqN_o          | out       | slv(7 downto 0)                               | Tx data (input to header decoder module)                         |
| synHeadSt_o       | out       | sl                                            | FSM outs for header and data flow control                        |
| ackHeadSt_o       | out       | sl                                            |                                                                  |
| dataHeadSt_o      | out       | sl                                            |                                                                  |
| dataSt_o          | out       | sl                                            |                                                                  |
| rstHeadSt_o       | out       | sl                                            |                                                                  |
| nullHeadSt_o      | out       | sl                                            |                                                                  |
| lastAckN_o        | out       | slv(7 downto 0)                               | Last acked number (Used in Rx FSM to determine if AcnN is valid) |
| ack_i             | in        | sl                                            | From receiver module when a segment with valid ACK is received   |
| ackN_i            | in        | slv(7 downto 0)                               | Number being ACKed                                               |
| lenErr_o          | out       | sl                                            | Errors (1 cc pulse)                                              |
| ackErr_o          | out       | sl                                            |                                                                  |
| bufferEmpty_o     | out       | sl                                            | Segment buffer indicator                                         |
## Signals

| Name        | Type                | Description |
| ----------- | ------------------- | ----------- |
| r           | RegType             |             |
| rin         | RegType             |             |
| wrAck       | AxiWriteDmaAckType  |             |
| rdAck       | AxiReadDmaAckType   |             |
| wrDmaMaster | AxiStreamMasterType |             |
| wrDmaSlave  | AxiStreamSlaveType  |             |
| rdDmaMaster | AxiStreamMasterType |             |
| rdDmaSlave  | AxiStreamSlaveType  |             |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| REG_INIT_C | RegType |  (       ----------------------------------------------------       -- Buffer window handling and acknowledgment control       ----------------------------------------------------       -- Window control       firstUnackAddr => (others => '0'),<br><span style="padding-left:20px">       lastSentAddr   => (others => '0'),<br><span style="padding-left:20px">       nextSentAddr   => (others => '0'),<br><span style="padding-left:20px">       lastAckSeqN    => (others => '0'),<br><span style="padding-left:20px">       --eackAddr       => (others => '0'),<br><span style="padding-left:20px">       --eackIndex      => 0,<br><span style="padding-left:20px">       bufferFull     => '0',<br><span style="padding-left:20px">       bufferEmpty    => '1',<br><span style="padding-left:20px">       windowArray    => (0 to 2 ** WINDOW_ADDR_SIZE_G-1 => WINDOW_INIT_C),<br><span style="padding-left:20px">       ackErr         => '0',<br><span style="padding-left:20px">       ackState       => IDLE_S,<br><span style="padding-left:20px">       -----------------------       -- Application side FSM       -----------------------       wrReq          => AXI_WRITE_DMA_REQ_INIT_C,<br><span style="padding-left:20px">       rxSegmentWe    => '0',<br><span style="padding-left:20px">       rxBufferAddr   => (others => '0'),<br><span style="padding-left:20px">       sndData        => '0',<br><span style="padding-left:20px">       lenErr         => '0',<br><span style="padding-left:20px">       appBusy        => '0',<br><span style="padding-left:20px">       appSlave       => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       appState       => IDLE_S,<br><span style="padding-left:20px">       ----------------------       -- Transport side FSM       ----------------------       rdReq          => AXI_READ_DMA_REQ_INIT_C,<br><span style="padding-left:20px">       --       csumAccum      => (others => '0'),<br><span style="padding-left:20px">       chksumOk       => '0',<br><span style="padding-left:20px">       checksum       => (others => '0'),<br><span style="padding-left:20px">       --       nextSeqN       => (others => '0'),<br><span style="padding-left:20px">       seqN           => (others => '0'),<br><span style="padding-left:20px">       txHeaderAddr   => (others => '0'),<br><span style="padding-left:20px">       txBufferAddr   => (others => '0'),<br><span style="padding-left:20px">       --       synH           => '0',<br><span style="padding-left:20px">       ackH           => '0',<br><span style="padding-left:20px">       rstH           => '0',<br><span style="padding-left:20px">       nullH          => '0',<br><span style="padding-left:20px">       dataH          => '0',<br><span style="padding-left:20px">       dataD          => '0',<br><span style="padding-left:20px">       resend         => '0',<br><span style="padding-left:20px">       ackSndData     => '0',<br><span style="padding-left:20px">       hdrAmrmed      => '0',<br><span style="padding-left:20px">       simErrorDet    => '0',<br><span style="padding-left:20px">       --       buffWe         => '0',<br><span style="padding-left:20px">       buffSent       => '0',<br><span style="padding-left:20px">       -- Fault injection       injectFaultD1  => '0',<br><span style="padding-left:20px">       injectFaultReg => '0',<br><span style="padding-left:20px">       -- Transport Interface       rdDmaSlave     => AXI_STREAM_SLAVE_INIT_C,<br><span style="padding-left:20px">       tspMaster      => AXI_STREAM_MASTER_INIT_C,<br><span style="padding-left:20px">       -- State Machine       tspState       => INIT_S) |             |
## Types

| Name         | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TspStateType | ( INIT_S,<br><span style="padding-left:20px"> DISS_CONN_S,<br><span style="padding-left:20px"> CONN_S,<br><span style="padding-left:20px"> SYN_H_S,<br><span style="padding-left:20px"> SYN_XSUM_S,<br><span style="padding-left:20px"> NSYN_H_S,<br><span style="padding-left:20px"> NSYN_XSUM_S,<br><span style="padding-left:20px"> DATA_H_S,<br><span style="padding-left:20px"> DATA_XSUM_S,<br><span style="padding-left:20px"> DATA_S,<br><span style="padding-left:20px"> RESEND_INIT_S,<br><span style="padding-left:20px"> RESEND_H_S,<br><span style="padding-left:20px"> RESEND_XSUM_S,<br><span style="padding-left:20px"> RESEND_PP_S)  |             |
| AppStateType | ( IDLE_S,<br><span style="padding-left:20px"> WAIT_SOF_S,<br><span style="padding-left:20px"> DATA_S,<br><span style="padding-left:20px"> SEG_RDY_S)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |             |
| AckStateType | ( IDLE_S,<br><span style="padding-left:20px"> ERR_S,<br><span style="padding-left:20px"> ACK_S)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
| RegType      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |             |
## Processes
- comb: ( ackN_i, ack_i, appMaster_i, axiOffset_i, bufferSize_i,
                   closed_i, connActive_i, initSeqN_i, injectFault_i, r, rdAck,
                   rdDmaMaster, rdHeaderData_i, rst_i, sndAck_i, sndNull_i,
                   sndResend_i, sndRst_i, sndSyn_i, tspSlave_i, windowSize_i,
                   wrAck, wrDmaSlave )
- seq: ( clk_i )
## Instantiations

- U_DmaWrite: surf.AxiStreamDmaWrite
- U_DmaRead: surf.AxiStreamDmaRead
