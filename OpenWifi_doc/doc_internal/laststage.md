# Entity: laststage

- **File**: laststage.v
## Diagram

![Diagram](laststage.svg "Diagram")
## Description

//////////////////////////////////////////////////////////////////////////////

 Filename:	laststage.v

 Project:	A General Purpose Pipelined FFT Implementation

 Purpose:	This is part of an FPGA implementation that will process
		the final stage of a decimate-in-frequency FFT, running
	through the data at one sample per clock.


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
| IWIDTH       |      | 16    |             |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| i_clk     | input     | wire                  |             |
|  i_reset  | input     | wire                  |             |
|  i_ce     | input     | wire                  |             |
|  i_sync   | input     | wire                  |             |
| i_val     | input     | wire	[(2*IWIDTH-1):0] |             |
| o_val     | output    | wire	[(2*OWIDTH-1):0] |             |
| o_sync    | output    |                       |             |
## Signals

| Name          | Type                      | Description                                                                                                                                              |
| ------------- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| m_r           | reg	signed	[(IWIDTH-1):0] |                                                                                                                                                          |
| m_i           | reg	signed	[(IWIDTH-1):0] |                                                                                                                                                          |
| i_r           | wire [(IWIDTH-1):0]       |                                                                                                                                                          |
| i_i           | wire [(IWIDTH-1):0]       |                                                                                                                                                          |
| rnd_r         | reg	signed	[(IWIDTH):0]   |  Don't forget that we accumulate a bit by adding two values  together. Therefore our intermediate value must have one more  bit than the two originals.  |
| rnd_i         | reg	signed	[(IWIDTH):0]   |  Don't forget that we accumulate a bit by adding two values  together. Therefore our intermediate value must have one more  bit than the two originals.  |
| sto_r         | reg	signed	[(IWIDTH):0]   |  Don't forget that we accumulate a bit by adding two values  together. Therefore our intermediate value must have one more  bit than the two originals.  |
| sto_i         | reg	signed	[(IWIDTH):0]   |  Don't forget that we accumulate a bit by adding two values  together. Therefore our intermediate value must have one more  bit than the two originals.  |
| wait_for_sync | reg                       |                                                                                                                                                          |
| stage         | reg                       |                                                                                                                                                          |
| sync_pipe     | reg		[1:0]                |                                                                                                                                                          |
| o_r           | wire [(OWIDTH-1):0]       |  Now that we have our results, let's round them and report them                                                                                          |
| o_i           | wire [(OWIDTH-1):0]       |  Now that we have our results, let's round them and report them                                                                                          |
| f_past_valid  | reg                       |                                                                                                                                                          |
| f_piped_real  | reg	signed	[IWIDTH-1:0]   |                                                                                                                                                          |
| f_piped_imag  | reg	signed	[IWIDTH-1:0]   |                                                                                                                                                          |
| f_syncd       | wire                      |                                                                                                                                                          |
| f_rsyncd      | reg                       |                                                                                                                                                          |
| f_state       | reg                       |                                                                                                                                                          |
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
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
## Instantiations

- do_rnd_r: convround
- do_rnd_i: convround
