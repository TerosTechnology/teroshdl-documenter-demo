# Entity: convround

- **File**: convround.v
## Diagram

![Diagram](convround.svg "Diagram")
## Description

//////////////////////////////////////////////////////////////////////////////

 Filename: 	convround.v

 Project:	A General Purpose Pipelined FFT Implementation

 Purpose:	A convergent rounding routine, also known as banker's
		rounding, Dutch rounding, Gaussian rounding, unbiased
	rounding, or ... more, at least according to Wikipedia.

	This form of rounding works by rounding, when the direction is in
	question, towards the nearest even value.


 Creator:	Dan Gisselquist, Ph.D.
		Gisselquist Technology, LLC

//////////////////////////////////////////////////////////////////////////////

 Copyright (C) 2015-2019, Gisselquist Technology, LLC

 This file is part of the general purpose pipelined FFT project.

 The pipelined FFT project is free software (firmware): you can redistribute
 it and/or modify it under the terms of the GNU Lesser General Public License
 as published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 The pipelined FFT project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
 General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with this program.  (It's in the $(ROOT)/doc directory.  Run make
 with no target there if the PDF file isn't present.)  If not, see
 <http://www.gnu.org/licenses/> for a copy.

 License:	LGPL, v3, as defined and found on www.gnu.org,
		http://www.gnu.org/licenses/lgpl.html


//////////////////////////////////////////////////////////////////////////////


`default_nettype	none


## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| IWID         |      | 16    |             |
## Ports

| Port name | Direction | Type                     | Description |
| --------- | --------- | ------------------------ | ----------- |
| i_clk     | input     | wire                     |             |
|  i_ce     | input     | wire                     |             |
| i_val     | input     | wire	signed	[(IWID-1):0] |             |
| o_val     | output    | [(OWID-1):0]             |             |
