# Entity: i2cmst_gen

## Diagram

![Diagram](i2cmst_gen.svg "Diagram")
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
Entity:      i2cmst_gen
File:        i2cmst_gen.vhd
Author:      Jan Andersson - Aeroflex Gaisler
Contact:     support@gaisler.com
Description: Generic I2CMST, see i2cmst.vhd
## Generics

| Generic name | Type                   | Value | Description            |
| ------------ | ---------------------- | ----- | ---------------------- |
| oepol        | integer range 0 to 1   | 0     | output enable polarity |
| filter       | integer range 2 to 512 | 2     | filter bit size        |
| dynfilt      | integer range 0 to 1   | 0     |                        |
## Ports

| Port name   | Direction | Type                          | Description |
| ----------- | --------- | ----------------------------- | ----------- |
| rstn        | in        | std_ulogic                    |             |
| clk         | in        | std_ulogic                    |             |
| psel        | in        | std_ulogic                    | APB signals |
| penable     | in        | std_ulogic                    |             |
| paddr       | in        | std_logic_vector(31 downto 0) |             |
| pwrite      | in        | std_ulogic                    |             |
| pwdata      | in        | std_logic_vector(31 downto 0) |             |
| prdata      | out       | std_logic_vector(31 downto 0) |             |
| irq         | out       | std_logic                     |             |
| i2ci_scl    | in        | std_ulogic                    | I2C signals |
| i2ci_sda    | in        | std_ulogic                    |             |
| i2co_scl    | out       | std_ulogic                    |             |
| i2co_scloen | out       | std_ulogic                    |             |
| i2co_sda    | out       | std_ulogic                    |             |
| i2co_sdaoen | out       | std_ulogic                    |             |
| i2co_enable | out       | std_ulogic                    |             |
## Signals

| Name | Type             | Description |
| ---- | ---------------- | ----------- |
| apbi | apb_slv_in_type  |             |
| apbo | apb_slv_out_type |             |
| i2ci | i2c_in_type      | I2C signals |
| i2co | i2c_out_type     |             |
## Instantiations

- i2c0: i2cmst
