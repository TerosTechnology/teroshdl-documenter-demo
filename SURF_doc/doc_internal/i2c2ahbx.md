# Entity: i2c2ahbx

- **File**: i2c2ahbx.vhd
## Diagram

![Diagram](i2c2ahbx.svg "Diagram")
## Description

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
Entity:      i2c2ahbx
File:        i2c2ahbx.vhd
Author:      Jan Andersson - Aeroflex Gaisler AB
Contact:     support@gaisler.com
Description: Simple I2C-slave providing a bridge to AMBA AHB
             This entity is typically wrapped with i2c2ahb or i2c2ahb_apb
             before use.
Short core documentation, for additional information see the GRLIB IP
Library User's Manual (GRIP):
The core functions as a I2C memory device. To write to the core, issue the
following I2C bus sequence:
0. START condition
1. Send core's I2C address with direction = write
2. Send 32-bit address to be used for AMBA bus
3. Send data to be written
The core will expect 32-bits of data and write these as a word. This can be
changed by writing to the core's control register. See documentation further
down. When the core's internal FIFO is full, the core will use clock
stretching to stall the transfer.
To write to the core, issue the following I2C bus sequence:
0. START condition
1. Send core's I2C address with direction = write
2. Send 32-bit address to be used for AMBA bus
3. Send repeated start condition
4. Send core's I2C address with direction = read
5. Read bytes
The core will perform 32-bit data accesses to fill its internal buffer. This
can be changed by writing to the core's control register (see documentation
further down). When the buffer is empty the core will use clock stretching
to stall the transfer.
The cores control/status register is accessed via address i2caddr + 1. The
register has the following layout:
+--------+-----------------------------------------------------------------+
| Bit(s) | Description                                                     |
+--------+-----------------------------------------------------------------+
|  7:6   | Reserved, always zero (RO)                                      |
|   5    | PROT: Memory protection triggered. Last access was outside      |
|        | range. Updated after each AMBA access (RO)                      |
|   4    | MEXC: Memory exception. Gets set if core receives AMBA ERROR    |
|        | response. Updated after each AMBA access. (RO)                  |
|   3    | DMAACT: Core is currently performing DMA (RO)                   |
|   2    | NACK: NACK instead of using clock stretching (RW)               |
|  1:0   | HSIZE: Controls the access size core will use for AMBA accesses |
|        | Default is HSIZE = WORD. HSIZE 11 is illegal (RW)               |
+--------+-----------------------------------------------------------------+
Documentation of generics:
[hindex]  AHB master index
[oepol]   Output enable polarity
[filter]  Length of filters used on SCL and SDA
## Generics

| Generic name | Type                   | Value | Description        |
| ------------ | ---------------------- | ----- | ------------------ |
| hindex       | integer                | 0     | AHB configuration  |
| oepol        | integer range 0 to 1   | 0     |                    |
| filter       | integer range 2 to 512 | 2     |                    |
## Ports

| Port name | Direction | Type             | Description          |
| --------- | --------- | ---------------- | -------------------- |
| rstn      | in        | std_ulogic       |                      |
| clk       | in        | std_ulogic       |                      |
| ahbi      | in        | ahb_mst_in_type  | AHB master interface |
| ahbo      | out       | ahb_mst_out_type |                      |
| i2ci      | in        | i2c_in_type      | I2C signals          |
| i2co      | out       | i2c_out_type     |                      |
| i2c2ahbi  | in        | i2c2ahb_in_type  |                      |
| i2c2ahbo  | out       | i2c2ahb_out_type |                      |
## Signals

| Name | Type             | Description |
| ---- | ---------------- | ----------- |
| ami  | ahb_dma_in_type  |             |
| amo  | ahb_dma_out_type |             |
| r    | i2c2ahb_reg_type |             |
|  rin | i2c2ahb_reg_type |             |
## Constants

| Name        | Type       | Value                      | Description |
| ----------- | ---------- | -------------------------- | ----------- |
| OEPOL_LEVEL | std_ulogic |  conv_std_logic(oepol = 1) |             |
| I2C_LOW     | std_ulogic |  OEPOL_LEVEL               | OE          |
| I2C_HIZ     | std_ulogic |  not OEPOL_LEVEL           |             |
| I2C_ACK     | std_ulogic |  '0'                       |             |
## Types

| Name             | Type                                                                                                                                                                                             | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| i2c_in_array     |                                                                                                                                                                                                  |             |
| state_type       | (idle,<br><span style="padding-left:20px"> checkaddr,<br><span style="padding-left:20px"> sclhold,<br><span style="padding-left:20px"> movebyte,<br><span style="padding-left:20px"> handshake)  |             |
| i2c2ahb_reg_type |                                                                                                                                                                                                  |             |
## Processes
- comb: ( r, rstn, i2ci, amo, i2c2ahbi )
- reg: ( clk )
## Instantiations

- ahbmst0: ahbmst
- bootmsg: report_version
**Description**
Boot message
pragma translate_off

