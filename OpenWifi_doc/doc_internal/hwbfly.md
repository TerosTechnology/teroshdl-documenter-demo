# Entity: hwbfly

## Diagram

![Diagram](hwbfly.svg "Diagram")
## Description

Filename:	hwbfly.v
 Project:	A General Purpose Pipelined FFT Implementation
 Purpose:	This routine is identical to the butterfly.v routine found
 Operation:
 Creator:	Dan Gisselquist, Ph.D.
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
 
## Generics

| Generic name | Type  | Value | Description                                         |
| ------------ | ----- | ----- | --------------------------------------------------- |
| IWIDTH       |       | 16    |                                                     |
| SHIFT        |       | 0     | Drop an additional bit on the output?               |
| CKPCE        | [1:0] | 1     | The number of clocks per clock enable, 1, 2, or 3.  |
## Ports

| Port name | Direction | Type                  | Description |
| --------- | --------- | --------------------- | ----------- |
| i_clk     | input     | wire                  |             |
|  i_reset  | input     | wire                  |             |
|  i_ce     | input     | wire                  |             |
| i_coef    | input     | wire	[(2*CWIDTH-1):0] |             |
| i_left    | input     | wire	[(2*IWIDTH-1):0] |             |
|  i_right  | input     | wire	[(2*IWIDTH-1):0] |             |
| i_aux     | input     | wire                  |             |
| o_left    | output    | wire	[(2*OWIDTH-1):0] |             |
|  o_right  | output    | wire	[(2*OWIDTH-1):0] |             |
| o_aux     | output    |                       |             |
## Signals

| Name              | Type                               | Description                                                                                                                                                                                                                                                                                          |
| ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| r_left            | reg	[(2*IWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_right           | reg	[(2*IWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_aux             | reg                                |                                                                                                                                                                                                                                                                                                      |
| r_aux_2           | reg                                |                                                                                                                                                                                                                                                                                                      |
| r_coef            | reg	[(2*CWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_left_r          | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_left_i          | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_right_r         | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_right_i         | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| ir_coef_r         | reg	signed	[(CWIDTH-1):0]          |                                                                                                                                                                                                                                                                                                      |
| ir_coef_i         | reg	signed	[(CWIDTH-1):0]          |                                                                                                                                                                                                                                                                                                      |
| r_sum_r           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_sum_i           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_dif_r           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_dif_i           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| leftv             | reg	[(2*IWIDTH+2):0]               |                                                                                                                                                                                                                                                                                                      |
| leftvv            | reg	[(2*IWIDTH+2):0]               |                                                                                                                                                                                                                                                                                                      |
| p_one             | wire [((IWIDTH+1)+(CWIDTH)-1):0]   | See comments in the butterfly.v source file for a discussion of these operations and the appropriate bit widths.                                                                                                                                                                                     |
| p_two             | wire [((IWIDTH+1)+(CWIDTH)-1):0]   | See comments in the butterfly.v source file for a discussion of these operations and the appropriate bit widths.                                                                                                                                                                                     |
| p_three           | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| w_one             | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| w_two             | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| aux_s             | wire                               | These values are held in memory and delayed during the multiply.  Here, we recover them.  During the multiply, values were multiplied by 2^(CWIDTH-2)*exp{-j*2*pi*...}, therefore, the left_x values need to be right shifted by CWIDTH-2 as well.  The additional bits come from a sign extension.  |
| left_si           | wire [(IWIDTH+CWIDTH):0]           |                                                                                                                                                                                                                                                                                                      |
| left_sr           | wire [(IWIDTH+CWIDTH):0]           |                                                                                                                                                                                                                                                                                                      |
| left_saved        | reg		[(2*IWIDTH+2):0]              |                                                                                                                                                                                                                                                                                                      |
| mpy_r             | reg	signed	[(CWIDTH+IWIDTH+3-1):0] |                                                                                                                                                                                                                                                                                                      |
| mpy_i             | reg	signed	[(CWIDTH+IWIDTH+3-1):0] |                                                                                                                                                                                                                                                                                                      |
| rnd_left_r        | wire [(OWIDTH-1):0]                | Round the results                                                                                                                                                                                                                                                                                    |
| rnd_left_i        | wire [(OWIDTH-1):0]                | Round the results                                                                                                                                                                                                                                                                                    |
| rnd_right_r       | wire [(OWIDTH-1):0]                | Round the results                                                                                                                                                                                                                                                                                    |
| rnd_right_i       | wire [(OWIDTH-1):0]                | Round the results                                                                                                                                                                                                                                                                                    |
| f_dlyleft_r       | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyleft_i       | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyright_r      | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyright_i      | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlycoeff_r      | reg	signed	[CWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlycoeff_i      | reg	signed	[CWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyaux          | reg	signed	[F_DEPTH-1:0]           |                                                                                                                                                                                                                                                                                                      |
| f_startup_counter | reg	[F_LGDEPTH-1:0]                |                                                                                                                                                                                                                                                                                                      |
| f_sumr            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumi            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumrx           | wire [IWIDTH+CWIDTH:0]             |                                                                                                                                                                                                                                                                                                      |
| f_sumix           | wire [IWIDTH+CWIDTH:0]             |                                                                                                                                                                                                                                                                                                      |
| f_difr            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_difi            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_difrx           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_difix           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_widecoeff_r     | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_widecoeff_i     | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_predifr         | wire [IWIDTH:0]                    | Let's see if we can improve our performance at all by moving our test one clock earlier.  If nothing else, it should help induction finish one (or more) clocks ealier than otherwise                                                                                                                |
| f_predifi         | wire [IWIDTH:0]                    | Let's see if we can improve our performance at all by moving our test one clock earlier.  If nothing else, it should help induction finish one (or more) clocks ealier than otherwise                                                                                                                |
| f_predifrx        | wire [IWIDTH+CWIDTH+1-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_predifix        | wire [IWIDTH+CWIDTH+1-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_sumcoef         | wire [CWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumdiff         | wire [IWIDTH+1:0]                  |                                                                                                                                                                                                                                                                                                      |
## Constants

| Name      | Type            | Value     | Description |
| --------- | --------------- | --------- | ----------- |
| F_LGDEPTH |                 | 3         |             |
| F_DEPTH   |                 | 5         |             |
| F_D       | [F_LGDEPTH-1:0] | F_DEPTH-1 |             |
## Processes
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge i_clk) )
**Description**
Induction helpers

## Instantiations

- do_rnd_left_r: convround
- do_rnd_left_i: convround
- do_rnd_right_r: convround
- do_rnd_right_i: convround
