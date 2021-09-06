# Entity: qtrstage

- **File**: qtrstage.v
## Diagram

![Diagram](qtrstage.svg "Diagram")
## Description

//////////////////////////////////////////////////////////////////////////////

 Filename:	qtrstage.v

 Project:	A General Purpose Pipelined FFT Implementation

 Purpose:	This file encapsulates the 4 point stage of a decimation in
		frequency FFT.  This particular implementation is optimized
	so that all of the multiplies are accomplished by additions and
	multiplexers only.

 Operation:
 	The operation of this stage is identical to the regular stages of
 	the FFT (see them for details), with one additional and critical
 	difference: this stage doesn't require any hardware multiplication.
 	The multiplies within it may all be accomplished using additions and
 	subtractions.

 	Let's see how this is done.  Given x[n] and x[n+2], cause thats the
 	stage we are working on, with i_sync true for x[0] being input,
 	produce the output:

 	y[n  ] = x[n] + x[n+2]
 	y[n+2] = (x[n] - x[n+2]) * e^{-j2pi n/2}	(forward transform)
 	       = (x[n] - x[n+2]) * -j^n

 	y[n].r = x[n].r + x[n+2].r	(This is the easy part)
 	y[n].i = x[n].i + x[n+2].i

 	y[2].r = x[0].r - x[2].r
 	y[2].i = x[0].i - x[2].i

 	y[3].r =   (x[1].i - x[3].i)		(forward transform)
 	y[3].i = - (x[1].r - x[3].r)

 	y[3].r = - (x[1].i - x[3].i)		(inverse transform)
 	y[3].i =   (x[1].r - x[3].r)		(INVERSE = 1)

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
| LGWIDTH      |      | 8     |             |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| i_clk     | input     | wire                  |             |
|  i_reset  | input     | wire                  |             |
|  i_ce     | input     | wire                  |             |
|  i_sync   | input     | wire                  |             |
| i_data    | input     | wire	[(2*IWIDTH-1):0] |             |
| o_data    | output    | [(2*OWIDTH-1):0]      |             |
| o_sync    | output    |                       |             |
## Signals

| Name          | Type                    | Description                                        |
| ------------- | ----------------------- | -------------------------------------------------- |
| wait_for_sync | reg                     |                                                    |
| pipeline      | reg	[2:0]               |                                                    |
| sum_r         | reg	signed [(IWIDTH):0] |                                                    |
| sum_i         | reg	signed [(IWIDTH):0] |                                                    |
| diff_r        | reg	signed [(IWIDTH):0] |                                                    |
| diff_i        | reg	signed [(IWIDTH):0] |                                                    |
| ob_a          | reg	[(2*OWIDTH-1):0]    |                                                    |
| ob_b          | wire [(2*OWIDTH-1):0]   |                                                    |
| ob_b_r        | reg	[(OWIDTH-1):0]      |                                                    |
| ob_b_i        | reg	[(OWIDTH-1):0]      |                                                    |
| iaddr         | reg	[(LGWIDTH-1):0]     |                                                    |
| imem          | reg	[(2*IWIDTH-1):0]    |                                                    |
| imem_r        | wire [(IWIDTH-1):0]     |                                                    |
| imem_i        | wire [(IWIDTH-1):0]     |                                                    |
| omem          | reg	[(2*OWIDTH-1):0]    |                                                    |
| rnd_sum_r     | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| rnd_sum_i     | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| rnd_diff_r    | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| rnd_diff_i    | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| n_rnd_diff_r  | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| n_rnd_diff_i  | wire [(OWIDTH-1):0]     |   Round our output values down to OWIDTH bits<br>  |
| f_past_valid  | reg                     |                                                    |
| f_piped_real  | reg	signed [IWIDTH-1:0] |                                                    |
| f_piped_imag  | reg	signed [IWIDTH-1:0] |                                                    |
| f_rsyncd      | reg                     |                                                    |
| f_syncd       | wire                    |                                                    |
| f_state       | reg	[1:0]               |                                                    |
| f_i_real      | wire [2*IWIDTH-1:0]     |                                                    |
| f_i_imag      | wire [2*IWIDTH-1:0]     |                                                    |
| f_o_real      | wire [OWIDTH-1:0]       |                                                    |
| f_o_imag      | wire [OWIDTH-1:0]       |                                                    |
## Processes
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
</br>**Description**
 This is the pipeline[-1] stage, pipeline[0] will be set next. 
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
</br>**Description**
 pipeline[1] takes sum_x and diff_x and produces rnd_x  Now for pipeline[2].  We can actually do this at all i_ce  clock times, since nothing will listen unless pipeline[3]  on the next clock.  Thus, we simplify this logic and do  it independent of pipeline[2]. 
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
## Instantiations

- do_rnd_sum_r: convround
- do_rnd_sum_i: convround
- do_rnd_diff_r: convround
- do_rnd_diff_i: convround
