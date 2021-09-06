# Entity: fftstage

- **File**: ifftstage.v
## Diagram

![Diagram](ifftstage.svg "Diagram")
## Description

//////////////////////////////////////////////////////////////////////////////

 Filename:	fftstage.v

 Project:	A General Purpose Pipelined FFT Implementation

 Purpose:	This file is (almost) a Verilog source file.  It is meant to
		be used by a FFT core compiler to generate FFTs which may be
	used as part of an FFT core.  Specifically, this file encapsulates
	the options of an FFT-stage.  For any 2^N length FFT, there shall be
	(N-1) of these stages.


 Operation:
 	Given a stream of values, operate upon them as though they were
 	value pairs, x[n] and x[n+N/2].  The stream begins when n=0, and ends
 	when n=N/2-1 (i.e. there's a full set of N values).  When the value
 	x[0] enters, the synchronization input, i_sync, must be true as well.

 	For this stream, produce outputs
 	y[n    ] = x[n] + x[n+N/2], and
 	y[n+N/2] = (x[n] - x[n+N/2]) * c[n],
 			where c[n] is a complex coefficient found in the
 			external memory file COEFFILE.
 	When y[0] is output, a synchronization bit o_sync will be true as
 	well, otherwise it will be zero.

 	Most of the work to do this is done within the butterfly, whether the
 	hardware accelerated butterfly (uses a DSP) or not.

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

| Generic name | Type  | Value         | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------ | ----- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IWIDTH       |       | 16            |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LGSPAN       |       | 5             |  LGWIDTH=6                                                                                                                                                                                                                                                                                                                                                                                                                             |
| OPT_HWMPY    | [0:0] | 1             |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CKPCE        |       | 1             |  Clocks per CE.  If your incoming data rate is less than 50% of your  clock speed, you can set CKPCE to 2'b10, make sure there's at least  one clock between cycles when i_ce is high, and then use two  multiplies instead of three.  Setting CKPCE to 2'b11, and insisting  on at least two clocks with i_ce low between cycles with i_ce high,  then the hardware optimized butterfly code will used one multiply  instead of two.  |
| COEFFILE     |       | "cmem_64.hex" |  The COEFFILE parameter contains the name of the file containing the  FFT twiddle factors                                                                                                                                                                                                                                                                                                                                              |
| ZERO_ON_IDLE | [0:0] | 1'b0          |                                                                                                                                                                                                                                                                                                                                                                                                                                        |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| i_clk     | input     | wire                  |  VERILATOR  |
|  i_reset  | input     | wire                  |  VERILATOR  |
|  i_ce     | input     | wire                  |  VERILATOR  |
|  i_sync   | input     | wire                  |  VERILATOR  |
| i_data    | input     | wire	[(2*IWIDTH-1):0] |             |
| o_data    | output    | [(2*OWIDTH-1):0]      |             |
| o_sync    | output    |                       |             |
## Signals

| Name            | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| wait_for_sync   | reg                   |  I am using the prefixes  	ib_*	to reference the inputs to the butterfly, and  	ob_*	to reference the outputs from the butterfly                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ib_a            | reg	[(2*IWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ib_b            | reg	[(2*IWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ib_c            | reg	[(2*CWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ib_sync         | reg                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| b_started       | reg                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ob_sync         | wire                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ob_a            | wire [(2*OWIDTH-1):0] |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ob_b            | wire [(2*OWIDTH-1):0] |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| cmem            | reg	[(2*CWIDTH-1):0]  |  cmem is defined as an array of real and complex values,  where the top CWIDTH bits are the real value and the bottom  CWIDTH bits are the imaginary value.<br>  cmem[i] = { (2^(CWIDTH-2)) * cos(2*pi*i/(2^LGWIDTH)), 		(2^(CWIDTH-2)) * sin(2*pi*i/(2^LGWIDTH)) };<br>                                                                                                                                                                                                                                                                                                                                                       |
| iaddr           | reg	[(LGSPAN):0]      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| imem            | reg	[(2*IWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| oaddr           | reg	[LGSPAN:0]        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| omem            | reg	[(2*OWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| idle            | reg                   |  The idle register is designed to keep track of when an input  to the butterfly is important and going to be used.  It's used  in a flag following, so that when useful values are placed  into the butterfly they'll be non-zero (idle=0), otherwise when  the inputs to the butterfly are irrelevant and will be ignored,  then (idle=1) those inputs will be set to zero.  This  functionality is not designed to be used in operation, but only  within a Verilator simulation context when chasing a bug.  In this limited environment, the non-zero answers will stand  in a trace making it easier to highlight a bug.  |
| nxt_oaddr       | reg	[(LGSPAN-1):0]    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| pre_ovalue      | reg	[(2*OWIDTH-1):0]  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_mpydelay      | reg	[LGSPAN:0]        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_past_valid    | reg                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_addr          | reg	[LGSPAN:0]        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_left          | reg	[2*IWIDTH-1:0]    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_right         | reg	[2*IWIDTH-1:0]    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_next_addr     | wire [LGSPAN:0]       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_last_addr     | wire [LGSPAN:0]       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_oleft         | reg	[2*OWIDTH-1:0]    | ///////////////////////////////////////<br>  Formally verify the output half, from the output of the butterfly  to the outputs of this module<br> ///////////////////////////////////////                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| f_oright        | reg	[2*OWIDTH-1:0]    | ///////////////////////////////////////<br>  Formally verify the output half, from the output of the butterfly  to the outputs of this module<br> ///////////////////////////////////////                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| f_oaddr         | reg	[LGSPAN:0]        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_oaddr_m1      | wire [LGSPAN:0]       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| f_output_active | reg                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
## Constants

| Name         | Type  | Value | Description |
| ------------ | ----- | ----- | ----------- |
| ZERO_ON_IDLE | [0:0] | 1'b0  |             |
## Processes
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
</br>**Description**
Need to make certain here that we don't read 
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
</br>**Description**
 Read the values from our input memory, and use them to feed first of two  butterfly inputs 
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
</br>**Description**
 Only write to the memory on the first half of the outputs  We'll use the memory value on the second half of the outputs 
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
- unnamed: ( @(*) )
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
- unnamed: ( @(*) )
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
- unnamed: ( @(posedge i_clk) )
  - **Type:** always
