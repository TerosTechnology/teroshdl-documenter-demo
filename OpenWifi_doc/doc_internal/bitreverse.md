# Entity: bitreverse

- **File**: bitreverse.v
## Diagram

![Diagram](bitreverse.svg "Diagram")
## Description

//////////////////////////////////////////////////////////////////////////////

 Filename:	bitreverse.v

 Project:	A General Purpose Pipelined FFT Implementation

 Purpose:	This module bitreverses a pipelined FFT input.  It differes
		from the dblreverse module in that this is just a simple and
	straightforward bitreverse, rather than one written to handle two
	words at once.


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
| LGSIZE       |      | 5     |             |
## Ports

| Port name | Direction | Type                 | Description |
| --------- | --------- | -------------------- | ----------- |
| i_clk     | input     | wire                 |             |
|  i_reset  | input     | wire                 |             |
|  i_ce     | input     | wire                 |             |
| i_in      | input     | wire	[(2*WIDTH-1):0] |             |
| o_out     | output    | [(2*WIDTH-1):0]      |             |
| o_sync    | output    |                      |             |
## Signals

| Name            | Type                | Description |
| --------------- | ------------------- | ----------- |
| wraddr          | reg	[(LGSIZE):0]    |             |
| rdaddr          | wire [(LGSIZE):0]   |             |
| brmem           | reg	[(2*WIDTH-1):0] |             |
| in_reset        | reg                 |             |
| f_past_valid    | reg                 |             |
| f_const_addr    | reg	[LGSIZE:0]      |             |
| f_reversed_addr | wire [LGSIZE:0]     |             |
| f_addr_loaded   | reg                 |             |
| f_addr_value    | reg	[(2*WIDTH-1):0] |             |
## Processes
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
