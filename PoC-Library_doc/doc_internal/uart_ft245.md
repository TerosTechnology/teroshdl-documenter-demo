# Entity: uart_ft245

- **File**: uart_ft245.vhdl
## Diagram

![Diagram](uart_ft245.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:     Peter Reichel
              Jan Schirok
              Steffen Koehler

 Entity:      UART controller for FTDI FT245M UART-over-USB converter.

 Description:
 ------------
 .. TODO:: No documentation available.

 License:
 =============================================================================
 Copyright 2008-2015 Technische Universitaet Dresden - Germany
										 Chair of VLSI-Design, Diagnostics and Architecture

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 =============================================================================
## Generics

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| CLK_FREQ     | positive |       |             |
## Ports

| Port name    | Direction | Type                         | Description         |
| ------------ | --------- | ---------------------------- | ------------------- |
| clk          | in        | std_logic                    | common signals      |
| rst          | in        | std_logic                    |                     |
| snd_ready    | out       | std_logic                    | send data           |
| snd_strobe   | in        | std_logic                    |                     |
| snd_data     | in        | std_logic_vector(7 downto 0) |                     |
| rec_strobe   | out       | std_logic                    | receive data        |
| rec_data     | out       | std_logic_vector(7 downto 0) |                     |
| ft245_data   | inout     | std_logic_vector(7 downto 0) | connection to ft245 |
| ft245_rdn    | out       | std_logic                    |                     |
| ft245_wrn    | out       | std_logic                    |                     |
| ft245_rxfn   | in        | std_logic                    |                     |
| ft245_txen   | in        | std_logic                    |                     |
| ft245_pwrenn | in        | std_logic                    |                     |
## Signals

| Name          | Type                             | Description       |
| ------------- | -------------------------------- | ----------------- |
| reg_delay     | unsigned(DELAY_WIDTH-1 downto 0) |  delay register   |
| fsm_state     | tState                           |                   |
| fsm_nextstate | tState                           |                   |
| reg_data_snd  | std_logic_vector(7 downto 0)     |  registers        |
| reg_data_rec  | std_logic_vector(7 downto 0)     |                   |
| reg_ld_rec    | std_logic                        |                   |
| reg_dto_b     | std_logic                        |  low-active       |
| reg_wr_b      | std_logic                        |  low-active       |
| reg_rd_b      | std_logic                        |  low-active       |
| ff_susp       | std_logic                        |  low-active       |
| ff_rxf        | std_logic                        |  low-active       |
| ff_txe        | std_logic                        |  low-active       |
| ctrl_ld_rec   | std_logic                        |  control signals  |
| ctrl_delay    | std_logic                        |                   |
| ctrl_rd       | std_logic                        |                   |
| ctrl_wr       | std_logic                        |                   |
| ctrl_dto      | std_logic                        |                   |
| data_in       | std_logic_vector(7 downto 0)     |                   |
## Constants

| Name         | Type                             | Value                                                                             | Description                                                           |
| ------------ | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| CLK_FREQ_MHZ | integer                          |  CLK_FREQ / 1000000                                                               |                                                                       |
| DELAY_CYCLES | integer                          |  CLK_FREQ_MHZ / 20                                                                |  FT245 communication delay cycles (minimum delay is 50 ns = 1/20 us)  |
| DELAY_WIDTH  | integer                          |  log2ceilnz(DELAY_CYCLES + 1)                                                     |  delay register width                                                 |
| DELAY_LOAD   | unsigned(DELAY_WIDTH-1 downto 0) |        to_unsigned(DELAY_CYCLES,<br><span style="padding-left:20px"> DELAY_WIDTH) |  delay register load value                                            |
## Types

| Name   | Type                                                                                                                                                                                                                                                                                                                                              | Description |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| tState | ( IDLE,<br><span style="padding-left:20px"> RD1,<br><span style="padding-left:20px"> RD2,<br><span style="padding-left:20px"> RD3,<br><span style="padding-left:20px"> RD4,<br><span style="padding-left:20px"> WR1,<br><span style="padding-left:20px"> WR2,<br><span style="padding-left:20px"> WR3,<br><span style="padding-left:20px"> WR4 )  |  FSM        |
## Processes
- unnamed: ( clk )
- unnamed: ( fsm_state, snd_strobe, reg_delay, ff_susp, ff_rxf, ff_txe )
- unnamed: ( clk )
**Description**
--------------------------------------------  registers 
