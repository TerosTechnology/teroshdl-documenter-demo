# Entity: I2cMaster

- **File**: I2cMaster.vhd
## Diagram

![Diagram](I2cMaster.svg "Diagram")
## Description

----------------------------------------------------------------------------
  This file is a part of the GRLIB VHDL IP LIBRARY
  Copyright (C) 2003 - 2008, Gaisler Research
  Copyright (C) 2008 - 2012, Aeroflex Gaisler

  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
-----------------------------------------------------------------------------
 Entity:      I2cMaster
 Author:      Jan Andersson - Gaisler Research
 Contact:     support@gaisler.com
 Description:

         Generic interface to OpenCores I2C-master. This is a wrapper
         that instantiates the byte- and bit-controller of the OpenCores I2C
         master (OC core developed by Richard Herveille, richard@asics.ws).

 Modifications:
   10/2012 - Ben Reese <bareese@slac.stanford.edu>
     Removed AMBA bus register based interfaced and replaced with generic
     IO interface for use anywhere within a firmware design.
     Interface based on transactions consisting of a i2c device address
     followed by up to 4 byte-reads or 4 byte-writes.

     Dynamic filter and bus speed adjustment have been left in as features,
     though they will probably be rarely used.
## Generics

| Generic name         | Type                      | Value | Description                  |
| -------------------- | ------------------------- | ----- | ---------------------------- |
| TPD_G                | time                      | 1 ns  |  Simulated propagation delay |
| OUTPUT_EN_POLARITY_G | integer range 0 to 1      | 0     |  output enable polarity      |
| PRESCALE_G           | integer range 0 to 655535 | 62    |                              |
| FILTER_G             | integer range 2 to 512    | 126   |  filter bit size             |
| DYNAMIC_FILTER_G     | integer range 0 to 1      | 0     |                              |
## Ports

| Port name    | Direction | Type             | Description |
| ------------ | --------- | ---------------- | ----------- |
| clk          | in        | sl               |             |
| srst         | in        | sl               |             |
| arst         | in        | sl               |             |
| i2cMasterIn  | in        | I2cMasterInType  | Front End   |
| i2cMasterOut | out       | I2cMasterOutType |             |
| i2ci         | in        | i2c_in_type      | I2C signals |
| i2co         | out       | i2c_out_type     |             |
## Signals

| Name        | Type                                        | Description                                                                                                                                                                                                                     |
| ----------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| r           | RegType                                     | ------------------------------------------------------------------------------------------------  Signals ------------------------------------------------------------------------------------------------  Register interface  |
| rin         | RegType                                     |                                                                                                                                                                                                                                 |
| byteCtrlOut | ByteCtrlOutType                             |  Outputs from byte_ctrl block                                                                                                                                                                                                   |
| iSclOEn     | sl                                          |  Internal SCL output enable                                                                                                                                                                                                     |
| iSdaOEn     | sl                                          |  Internal SDA output enablee                                                                                                                                                                                                    |
| filter      | slv((FILTER_G-1)*DYNAMIC_FILTER_G downto 0) |  filt input to byte_ctrl                                                                                                                                                                                                        |
| arstL       | sl                                          |                                                                                                                                                                                                                                 |
| coreRst     | sl                                          |                                                                                                                                                                                                                                 |
## Constants

| Name       | Type    | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description |
| ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TIMEOUT_C  | integer |  (PRESCALE_G+1)*5*500                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |             |
| REG_INIT_C | RegType |  (       timer        => 0,<br><span style="padding-left:20px">       coreRst      => '0',<br><span style="padding-left:20px">       byteCtrlIn   => (          start     => '0',<br><span style="padding-left:20px">          stop      => '0',<br><span style="padding-left:20px">          read      => '0',<br><span style="padding-left:20px">          write     => '0',<br><span style="padding-left:20px">          ackIn     => '0',<br><span style="padding-left:20px">          din       => (others => '0')),<br><span style="padding-left:20px">       state        => WAIT_TXN_REQ_S,<br><span style="padding-left:20px">       tenbit       => '0',<br><span style="padding-left:20px">       i2cMasterOut => (          busAck    => '0',<br><span style="padding-left:20px">          txnError  => '0',<br><span style="padding-left:20px">          wrAck     => '0',<br><span style="padding-left:20px">          rdValid   => '0',<br><span style="padding-left:20px">          rdData    => (others => '0'))) |             |
## Types

| Name            | Type                                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ByteCtrlInType  |                                                                                                                                                                                                                                                                                                                          | ---------------------------------------------------------------------------  Types ---------------------------------------------------------------------------  i2c_master_byte_ctrl IO  |
| ByteCtrlOutType |                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                          |
| StateType       | ( WAIT_TXN_REQ_S,<br><span style="padding-left:20px"> ADDR_S,<br><span style="padding-left:20px"> WAIT_ADDR_ACK_S,<br><span style="padding-left:20px"> READ_S,<br><span style="padding-left:20px"> WAIT_READ_DATA_S,<br><span style="padding-left:20px"> WRITE_S,<br><span style="padding-left:20px"> WAIT_WRITE_ACK_S)  |                                                                                                                                                                                          |
| RegType         |                                                                                                                                                                                                                                                                                                                          |  Module Registers                                                                                                                                                                        |
## Processes
- comb: ( r, byteCtrlOut, i2cMasterIn, srst )
- reg: ( clk, arst )
## Instantiations

- byte_ctrl: i2c_master_byte_ctrl
**Description**
 Byte Controller from OpenCores I2C master,
 by Richard Herveille (richard@asics.ws). The asynchronous
 reset is tied to '1'. Only the synchronous reset is used.
 OC I2C logic has active high reset.

