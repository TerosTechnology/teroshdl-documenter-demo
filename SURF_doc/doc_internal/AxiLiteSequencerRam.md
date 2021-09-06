# Entity: AxiLiteSequencerRam

- **File**: AxiLiteSequencerRam.vhd
## Diagram

![Diagram](AxiLiteSequencerRam.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: The slave AXI-Lite interface used to load a sequence of master
              AXI-Lite transactions.  The transactions are stored in
              address=[1:2**ADDR_WIDTH_G-1].  Writing to Address[0] will
              start the transaction sequence and the number of transactions
              to execute.  At the end of the sequence (or if a bus error is
              detected during the sequence) a slave AXI-lite bus response is
              executed.  If there is a bus error, the address/response/data
              is written into address[0] of the RAM for debugging.
-----------------------------------------------------------------------------
 Sequencer's RAM Address mapping:
 sAxil.address[0x00].BIT[ADDR_WIDTH_G-1:0](write) = (r.size) Starts transactions and number of transactions to execute (zero exclusive)
 sAxil.address[0x00].BIT[31:ADDR_WIDTH_G](write)  = Unused
 sAxil.address[0x04].BIT[31:0](write)             = Unused
 sAxil.address[0x00](Read)                        = zero if no error response else mAxil.Data[errorEvent].BIT[31:00]
 sAxil.address[0x04](Read)                        = zero if no error response else mAxil.Address[errorEvent].BIT[31:02] & errorResp
 sAxil.address[0x08] = Ram.Address[0x1].BIT[31:00]: Sequenced mAxil.Data[0].BIT[31:00]
 sAxil.address[0x0C] = Ram.Address[0x1].BIT[63:32]: Sequenced mAxil.Address[0].BIT[31:02] & '0' & RnW
 sAxil.address[0x10] = Ram.Address[0x2].BIT[31:00]: Sequenced mAxil.Data[1][31:00]
 sAxil.address[0x14] = Ram.Address[0x2].BIT[63:32]: Sequenced mAxil.Address[1].BIT[31:02] & '0' & RnW
 sAxil.address[0x18] = Ram.Address[0x3].BIT[31:00]: Sequenced mAxil.Data[2][31:00]
 sAxil.address[0x1C] = Ram.Address[0x3].BIT[63:32]: Sequenced mAxil.Address[2].BIT[31:02] & '0' & RnW
 .....
 .....
 sAxil.address[8*r.size+0x0] = Ram.Address[r.size].BIT[31:00]: Sequenced mAxil.Data[r.size-1][31:00]
 sAxil.address[8*r.size+0x4] = Ram.Address[r.size].BIT[63:32]: Sequenced mAxil.Address[r.size-1].BIT[31:02] & '0' & RnW

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

| Generic name        | Type                 | Value      | Description                                                                                          |
| ------------------- | -------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| TPD_G               | time                 | 1 ns       |                                                                                                      |
| SYNTH_MODE_G        | string               | "inferred" |                                                                                                      |
| MEMORY_TYPE_G       | string               | "block"    |                                                                                                      |
| MEMORY_INIT_FILE_G  | string               | "none"     |  Used for MEMORY_TYPE_G="XPM only                                                                    |
| MEMORY_INIT_PARAM_G | string               | "0"        |  Used for MEMORY_TYPE_G="XPM only                                                                    |
| WAIT_FOR_RESPONSE_G | boolean              | false      |  false: immediately respond back for address[0], true: wait for the end of the transaction sequences |
| READ_LATENCY_G      | natural range 0 to 3 | 2          |                                                                                                      |
| ADDR_WIDTH_G        | positive             | 8          |                                                                                                      |
## Ports

| Port name        | Direction | Type                         | Description                |
| ---------------- | --------- | ---------------------------- | -------------------------- |
| axilClk          | in        | sl                           | Clock and Reset            |
| axilRst          | in        | sl                           |                            |
| extStart         | in        | sl                           | External Control Interface |
| extSize          | in        | slv(ADDR_WIDTH_G-1 downto 0) |                            |
| extBusy          | out       | sl                           |                            |
| extDone          | out       | sl                           |                            |
| sAxilReadMaster  | in        | AxiLiteReadMasterType        | Slave AXI-Lite Interface   |
| sAxilReadSlave   | out       | AxiLiteReadSlaveType         |                            |
| sAxilWriteMaster | in        | AxiLiteWriteMasterType       |                            |
| sAxilWriteSlave  | out       | AxiLiteWriteSlaveType        |                            |
| mAxilReadMaster  | out       | AxiLiteReadMasterType        | Master AXI-Lite Interface  |
| mAxilReadSlave   | in        | AxiLiteReadSlaveType         |                            |
| mAxilWriteMaster | out       | AxiLiteWriteMasterType       |                            |
| mAxilWriteSlave  | in        | AxiLiteWriteSlaveType        |                            |
## Signals

| Name    | Type             | Description |
| ------- | ---------------- | ----------- |
| r       | RegType          |             |
| rin     | RegType          |             |
| seqData | slv(63 downto 0) |             |
| dout    | slv(63 downto 0) |             |
| ack     | AxiLiteAckType   |             |
## Constants

| Name                | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| AXI_RAM_ADDR_HIGH_C | integer |  ADDR_WIDTH_G+AXI_DEC_ADDR_RANGE_C'high                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |             |
| AXI_RAM_ADDR_LOW_C  | integer |  AXI_DEC_ADDR_RANGE_C'high+1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |             |
| REG_INIT_C          | RegType |  (       extBusy         => '0',<br><span style="padding-left:20px">       extDone         => '0',<br><span style="padding-left:20px">       sAxilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       sAxilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       wstrb           => (others => '0'),<br><span style="padding-left:20px">       din             => (others => '0'),<br><span style="padding-left:20px">       addr            => (others => '0'),<br><span style="padding-left:20px">       size            => (others => '0'),<br><span style="padding-left:20px">       cnt             => (others => '0'),<br><span style="padding-left:20px">       seqAddr         => (others => '0'),<br><span style="padding-left:20px">       resp            => (others => '0'),<br><span style="padding-left:20px">       rdLatecy        => 0,<br><span style="padding-left:20px">       req             => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       state           => IDLE_S) |             |
## Types

| Name      | Type                                                                                                                                                                                                         | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> S_AXI_RD_S,<br><span style="padding-left:20px"> M_AXI_REQ_S,<br><span style="padding-left:20px"> M_AXI_ACK_S,<br><span style="padding-left:20px"> SEQ_DONE_S)  |             |
| RegType   |                                                                                                                                                                                                              |             |
## Processes
- comb: ( ack, axilRst, dout, extSize, extStart, r, sAxilReadMaster,
                   sAxilWriteMaster, seqData )
- seq: ( axilClk )
## Instantiations

- U_AxiLiteMaster: surf.AxiLiteMaster
