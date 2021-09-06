# Entity: AxiLiteCrossbarI2cMux

- **File**: AxiLiteCrossbarI2cMux.vhd
## Diagram

![Diagram](AxiLiteCrossbarI2cMux.svg "Diagram")
## Description

-----------------------------------------------------------------------------
 Company    : SLAC National Accelerator Laboratory
-----------------------------------------------------------------------------
 Description: Sets the I2C MUX path before sending the TXN to the AXI-Lite XBAR
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

| Generic name       | Type                             | Value                        | Description                 |
| ------------------ | -------------------------------- | ---------------------------- | --------------------------- |
| TPD_G              | time                             | 1 ns                         |                             |
| AXIL_PROXY_G       | boolean                          | false                        |                             |
| MUX_DECODE_MAP_G   | Slv8Array                        | I2C_MUX_DECODE_MAP_TCA9548_C | I2C MUX Generics            |
| I2C_MUX_ADDR_G     | slv(6 downto 0)                  | b"1110_000"                  |                             |
| I2C_SCL_FREQ_G     | real                             | 400.0E+3                     |  units of Hz                |
| I2C_MIN_PULSE_G    | real                             | 100.0E-9                     |  units of seconds           |
| AXIL_CLK_FREQ_G    | real                             | 156.25E+6                    |  units of Hz                |
| NUM_MASTER_SLOTS_G | natural range 1 to 64            | 4                            | AXI-Lite Crossbar Generics  |
| DEC_ERROR_RESP_G   | slv(1 downto 0)                  | AXI_RESP_DECERR_C            |                             |
| MASTERS_CONFIG_G   | AxiLiteCrossbarMasterConfigArray | AXIL_XBAR_CFG_DEFAULT_C      |                             |
| DEBUG_G            | boolean                          | false                        |                             |
## Ports

| Port name         | Direction | Type                                                   | Description                |
| ----------------- | --------- | ------------------------------------------------------ | -------------------------- |
| axilClk           | in        | sl                                                     | Clocks and Resets          |
| axilRst           | in        | sl                                                     |                            |
| sAxilReadMaster   | in        | AxiLiteReadMasterType                                  | Slave AXI-Lite Interface   |
| sAxilReadSlave    | out       | AxiLiteReadSlaveType                                   |                            |
| sAxilWriteMaster  | in        | AxiLiteWriteMasterType                                 |                            |
| sAxilWriteSlave   | out       | AxiLiteWriteSlaveType                                  |                            |
| mAxilWriteMasters | out       | AxiLiteWriteMasterArray(NUM_MASTER_SLOTS_G-1 downto 0) | Master AXI-Lite Interfaces |
| mAxilWriteSlaves  | in        | AxiLiteWriteSlaveArray(NUM_MASTER_SLOTS_G-1 downto 0)  |                            |
| mAxilReadMasters  | out       | AxiLiteReadMasterArray(NUM_MASTER_SLOTS_G-1 downto 0)  |                            |
| mAxilReadSlaves   | in        | AxiLiteReadSlaveArray(NUM_MASTER_SLOTS_G-1 downto 0)   |                            |
| i2ci              | in        | i2c_in_type                                            | I2C MUX Ports              |
| i2co              | out       | i2c_out_type                                           |                            |
## Signals

| Name            | Type                   | Description |
| --------------- | ---------------------- | ----------- |
| r               | RegType                |             |
| rin             | RegType                |             |
| axilReadMaster  | AxiLiteReadMasterType  |             |
| axilReadSlave   | AxiLiteReadSlaveType   |             |
| axilWriteMaster | AxiLiteWriteMasterType |             |
| axilWriteSlave  | AxiLiteWriteSlaveType  |             |
| i2cRegMasterOut | I2cRegMasterOutType    |             |
| ack             | AxiLiteAckType         |             |
| xbarReadMaster  | AxiLiteReadMasterType  |             |
| xbarReadSlave   | AxiLiteReadSlaveType   |             |
| xbarWriteMaster | AxiLiteWriteMasterType |             |
| xbarWriteSlave  | AxiLiteWriteSlaveType  |             |
## Constants

| Name             | Type               | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description    |
| ---------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| I2C_SCL_5xFREQ_C | real               |  5.0 * I2C_SCL_FREQ_G                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                |
| PRESCALE_C       | natural            |  (getTimeRatio(AXIL_CLK_FREQ_G,<br><span style="padding-left:20px"> I2C_SCL_5xFREQ_C)) - 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                |
| FILTER_C         | natural            |  natural(AXIL_CLK_FREQ_G * I2C_MIN_PULSE_G) + 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                |
| DEVICE_MAP_C     | I2cAxiLiteDevType  |  (       MakeI2cAxiLiteDevType(          i2cAddress  => I2C_MUX_ADDR_G,<br><span style="padding-left:20px">          dataSize    => 8,<br><span style="padding-left:20px">              -- in units of bits          addrSize    => 0,<br><span style="padding-left:20px">              -- in units of bits          endianness  => '0',<br><span style="padding-left:20px">            -- Little endian          repeatStart => '0'))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                |
| I2C_MUX_INIT_C   | I2cRegMasterInType |  (       i2cAddr     => DEVICE_MAP_C.i2cAddress,<br><span style="padding-left:20px">       tenbit      => DEVICE_MAP_C.i2cTenbit,<br><span style="padding-left:20px">       regAddr     => (others => '0'),<br><span style="padding-left:20px">       regWrData   => (others => '0'),<br><span style="padding-left:20px">       regOp       => '1',<br><span style="padding-left:20px">               -- 1 for write,<br><span style="padding-left:20px"> 0 for read       regAddrSkip => '1',<br><span style="padding-left:20px">               -- No memory address in the MUX       regAddrSize => (others => '0'),<br><span style="padding-left:20px">       regDataSize => (others => '0'),<br><span style="padding-left:20px">       regReq      => '0',<br><span style="padding-left:20px">       busReq      => '0',<br><span style="padding-left:20px">       endianness  => DEVICE_MAP_C.endianness,<br><span style="padding-left:20px">       repeatStart => DEVICE_MAP_C.repeatStart) |  Repeat Start  |
| REG_INIT_C       | RegType            |  (       rnw            => '0',<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       i2cRegMasterIn => I2C_MUX_INIT_C,<br><span style="padding-left:20px">       req            => AXI_LITE_REQ_INIT_C,<br><span style="padding-left:20px">       state          => IDLE_S)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                |
## Types

| Name      | Type                                                                                              | Description |
| --------- | ------------------------------------------------------------------------------------------------- | ----------- |
| StateType | ( IDLE_S,<br><span style="padding-left:20px"> MUX_S,<br><span style="padding-left:20px"> XBAR_S)  |             |
| RegType   |                                                                                                   |             |
## Processes
- comb: ( ack, axilReadMaster, axilRst, axilWriteMaster,
                   i2cRegMasterOut, r )
- seq: ( axilClk )
## Instantiations

- U_I2cRegMaster: surf.I2cRegMaster
- U_XbarAxilMaster: surf.AxiLiteMaster
- U_XBAR: surf.AxiLiteCrossbar
