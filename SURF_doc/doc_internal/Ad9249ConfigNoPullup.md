# Entity: Ad9249ConfigNoPullup

- **File**: Ad9249ConfigNoPullup.vhd
## Diagram

![Diagram](Ad9249ConfigNoPullup.svg "Diagram")
## Description

Company    : SLAC National Accelerator Laboratory
Description: AD9249 Configuration/Status Module (no pullup version)
This file is part of 'SLAC Firmware Standard Library'.
It is subject to the license terms in the LICENSE.txt file found in the
top-level directory of this distribution and at:
   https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
No part of 'SLAC Firmware Standard Library', including this file,
may be copied, modified, propagated, or distributed except according to
the terms contained in the LICENSE.txt file.
## Generics

| Generic name    | Type     | Value   | Description |
| --------------- | -------- | ------- | ----------- |
| TPD_G           | time     | 1 ns    |             |
| DEN_POLARITY_G  | sl       | '1'     |             |
| CLK_PERIOD_G    | real     | 8.0e-9  |             |
| CLK_EN_PERIOD_G | real     | 16.0e-9 |             |
| NUM_CHIPS_G     | positive | 1       |             |
## Ports

| Port name       | Direction | Type                                       | Description      |
| --------------- | --------- | ------------------------------------------ | ---------------- |
| axilClk         | in        | sl                                         |                  |
| axilRst         | in        | sl                                         |                  |
| axilReadMaster  | in        | AxiLiteReadMasterType                      |                  |
| axilReadSlave   | out       | AxiLiteReadSlaveType                       |                  |
| axilWriteMaster | in        | AxiLiteWriteMasterType                     |                  |
| axilWriteSlave  | out       | AxiLiteWriteSlaveType                      |                  |
| adcSClk         | out       | std_logic                                  | Interface To ADC |
| adcSDin         | in        | std_logic                                  |                  |
| adcSDout        | out       | std_logic                                  |                  |
| adcSDEn         | out       | std_logic                                  |                  |
| adcCsb          | out       | std_logic_vector(NUM_CHIPS_G*2-1 downto 0) |                  |
| adcPdwn         | out       | std_logic_vector(NUM_CHIPS_G-1 downto 0)   |                  |
## Signals

| Name        | Type                                             | Description   |
| ----------- | ------------------------------------------------ | ------------- |
| intShift    | std_logic_vector(23 downto 0)                    | Local Signals |
| nextClk     | std_logic                                        |               |
| nextAck     | std_logic                                        |               |
| shiftCnt    | std_logic_vector(12 downto 0)                    |               |
| shiftCntEn  | std_logic                                        |               |
| shiftEn     | std_logic                                        |               |
| locSDout    | std_logic                                        |               |
| adcSDir     | std_logic                                        |               |
| axilClkEn   | std_logic                                        |               |
| sclkCounter | std_logic_vector(SCLK_COUNTER_SIZE_C-1 downto 0) |               |
| curState    | std_logic_vector(1 downto 0)                     |               |
| nxtState    | std_logic_vector(1 downto 0)                     |               |
| adcWrData   | std_logic_vector(7 downto 0)                     |               |
| adcRdData   | std_logic_vector(7 downto 0)                     |               |
| adcAddr     | std_logic_vector(12 downto 0)                    |               |
| adcWrReq    | std_logic                                        |               |
| adcRdReq    | std_logic                                        |               |
| adcAck      | std_logic                                        |               |
| r           | RegType                                          |               |
| rin         | RegType                                          |               |
## Constants

| Name                         | Type                          | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description   |
| ---------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| SPI_CLK_PERIOD_DIV2_CYCLES_C | integer                       |  integer(CLK_EN_PERIOD_G / CLK_PERIOD_G) / 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |               |
| SCLK_COUNTER_SIZE_C          | integer                       |  bitSize(SPI_CLK_PERIOD_DIV2_CYCLES_C)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |               |
| ST_IDLE                      | std_logic_vector(1 downto 0)  |  "01"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | State Machine |
| ST_SHIFT                     | std_logic_vector(1 downto 0)  |  "10"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |               |
| ST_DONE                      | std_logic_vector(1 downto 0)  |  "11"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |               |
| CHIP_SEL_WIDTH_C             | integer                       |  log2(NUM_CHIPS_G*2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |               |
| PWDN_ADDR_BIT_C              | integer                       |  11 + CHIP_SEL_WIDTH_C                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |               |
| PWDN_ADDR_C                  | slv(PWDN_ADDR_BIT_C downto 0) |  toSlv(2**PWDN_ADDR_BIT_C,<br><span style="padding-left:20px"> PWDN_ADDR_BIT_C+1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |               |
| REG_INIT_C                   | RegType                       |  (       state          => ADC_IDLE_S,<br><span style="padding-left:20px">       axilReadSlave  => AXI_LITE_READ_SLAVE_INIT_C,<br><span style="padding-left:20px">       axilWriteSlave => AXI_LITE_WRITE_SLAVE_INIT_C,<br><span style="padding-left:20px">       chipSel        => (others => '0'),<br><span style="padding-left:20px">       wrData         => (others => '0'),<br><span style="padding-left:20px">       adcWrReq       => '0',<br><span style="padding-left:20px">       adcRdReq       => '0',<br><span style="padding-left:20px">       pdwn           => (others => '0')) |               |
## Types

| Name      | Type                                                                                                           | Description |
| --------- | -------------------------------------------------------------------------------------------------------------- | ----------- |
| StateType | (ADC_IDLE_S,<br><span style="padding-left:20px"> ADC_READ_S,<br><span style="padding-left:20px"> ADC_WRITE_S)  |             |
| RegType   |                                                                                                                | Registers   |
## Processes
- comb: ( adcAck, adcRdData, axilReadMaster, axilRst, axilWriteMaster, r )
- seq: ( axilClk )
- unnamed: ( axilClk )
**Description**
Generate clock enable for state machine

- unnamed: ( axilClk )
**Description**
Control shift memory register

- unnamed: ( curState, adcWrReq, adcRdReq, shiftCntEn )
**Description**
State machine control

