# Entity: butterfly

## Diagram

![Diagram](butterfly.svg "Diagram")
## Description

Filename:	butterfly.v
 Project:	A General Purpose Pipelined FFT Implementation
 Purpose:	This routine caculates a butterfly for a decimation
 Notes:
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

| Generic name | Type | Value        | Description                                                                                                                                                                                                                                                  |
| ------------ | ---- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IWIDTH       |      | 16           | Public changeable parameters ...                                                                                                                                                                                                                             |
| SHIFT        |      | 0            |                                                                                                                                                                                                                                                              |
| CKPCE        |      | 1            | The number of clocks per each i_ce.  The actual number can be more, but the algorithm depends upon at least this many for extra internal processing.                                                                                                         |
| F_CHECK      |      | MPYREMAINDER | F_CHECK will be set externally by the solver, so that we can double check that the solver is actually testing what we think it is testing.  We'll set it here to MPYREMAINDER, which will essentially eliminate the check--unless overridden by the solver.  |
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
| f_dlyleft_r       | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyleft_i       | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyright_r      | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyright_i      | reg	signed	[IWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlycoeff_r      | reg	signed	[CWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlycoeff_i      | reg	signed	[CWIDTH-1:0]            |                                                                                                                                                                                                                                                                                                      |
| f_dlyaux          | reg	signed	[F_DEPTH-1:0]           |                                                                                                                                                                                                                                                                                                      |
| f_predifr         | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_predifi         | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_predifrx        | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_predifix        | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_sumcoef         | wire [CWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumdiff         | wire [IWIDTH+1:0]                  |                                                                                                                                                                                                                                                                                                      |
| f_sumr            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumi            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_sumrx           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_sumix           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_difr            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_difi            | wire [IWIDTH:0]                    |                                                                                                                                                                                                                                                                                                      |
| f_difrx           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_difix           | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_widecoeff_r     | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| f_widecoeff_i     | wire [IWIDTH+CWIDTH+3-1:0]         |                                                                                                                                                                                                                                                                                                      |
| fp_one_ic         | wire [(CWIDTH):0]                  |                                                                                                                                                                                                                                                                                                      |
| fp_two_ic         | wire [(CWIDTH):0]                  |                                                                                                                                                                                                                                                                                                      |
| fp_three_ic       | wire [(CWIDTH):0]                  |                                                                                                                                                                                                                                                                                                      |
| f_p3c_in          | wire [(CWIDTH):0]                  |                                                                                                                                                                                                                                                                                                      |
| fp_one_id         | wire [(IWIDTH+1):0]                |                                                                                                                                                                                                                                                                                                      |
| fp_two_id         | wire [(IWIDTH+1):0]                |                                                                                                                                                                                                                                                                                                      |
| fp_three_id       | wire [(IWIDTH+1):0]                |                                                                                                                                                                                                                                                                                                      |
| f_p3d_in          | wire [(IWIDTH+1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_left            | reg	[(2*IWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_right           | reg	[(2*IWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_coef            | reg	[(2*CWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_coef_2          | reg	[(2*CWIDTH-1):0]               |                                                                                                                                                                                                                                                                                                      |
| r_left_r          | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_left_i          | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_right_r         | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_right_i         | wire [(IWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| r_sum_r           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_sum_i           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_dif_r           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| r_dif_i           | reg	signed	[(IWIDTH):0]            |                                                                                                                                                                                                                                                                                                      |
| fifo_addr         | reg	[(LGDELAY-1):0]                |                                                                                                                                                                                                                                                                                                      |
| fifo_read_addr    | wire [(LGDELAY-1):0]               |                                                                                                                                                                                                                                                                                                      |
| fifo_left         | reg	[(2*IWIDTH+1):0]               |                                                                                                                                                                                                                                                                                                      |
| ir_coef_r         | wire [(CWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| ir_coef_i         | wire [(CWIDTH-1):0]                |                                                                                                                                                                                                                                                                                                      |
| p_one             | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| p_two             | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| p_three           | wire [((IWIDTH+2)+(CWIDTH+1)-1):0] |                                                                                                                                                                                                                                                                                                      |
| fifo_i            | wire [(IWIDTH+CWIDTH):0]           | These values are held in memory and delayed during the multiply.  Here, we recover them.  During the multiply, values were multiplied by 2^(CWIDTH-2)*exp{-j*2*pi*...}, therefore, the left_x values need to be right shifted by CWIDTH-2 as well.  The additional bits come from a sign extension.  |
| fifo_r            | wire [(IWIDTH+CWIDTH):0]           | These values are held in memory and delayed during the multiply.  Here, we recover them.  During the multiply, values were multiplied by 2^(CWIDTH-2)*exp{-j*2*pi*...}, therefore, the left_x values need to be right shifted by CWIDTH-2 as well.  The additional bits come from a sign extension.  |
| fifo_read         | reg		[(2*IWIDTH+1):0]              |                                                                                                                                                                                                                                                                                                      |
| mpy_r             | reg	signed	[(CWIDTH+IWIDTH+3-1):0] |                                                                                                                                                                                                                                                                                                      |
| mpy_i             | reg	signed	[(CWIDTH+IWIDTH+3-1):0] |                                                                                                                                                                                                                                                                                                      |
| rnd_left_r        | wire [(OWIDTH-1):0]                | Now, if the user wants to keep any extras of these (via OWIDTH), or if he wishes to arbitrarily shift some of these off (via SHIFT) we accomplish that here.                                                                                                                                         |
| rnd_left_i        | wire [(OWIDTH-1):0]                | Now, if the user wants to keep any extras of these (via OWIDTH), or if he wishes to arbitrarily shift some of these off (via SHIFT) we accomplish that here.                                                                                                                                         |
| rnd_right_r       | wire [(OWIDTH-1):0]                | Now, if the user wants to keep any extras of these (via OWIDTH), or if he wishes to arbitrarily shift some of these off (via SHIFT) we accomplish that here.                                                                                                                                         |
| rnd_right_i       | wire [(OWIDTH-1):0]                | Now, if the user wants to keep any extras of these (via OWIDTH), or if he wishes to arbitrarily shift some of these off (via SHIFT) we accomplish that here.                                                                                                                                         |
| left_sr           | wire [(CWIDTH+IWIDTH+3-1):0]       |                                                                                                                                                                                                                                                                                                      |
| left_si           | wire [(CWIDTH+IWIDTH+3-1):0]       |                                                                                                                                                                                                                                                                                                      |
| aux_pipeline      | reg	[(AUXLEN-1):0]                 |                                                                                                                                                                                                                                                                                                      |
| f_startup_counter | reg	[F_LGDEPTH:0]                  |                                                                                                                                                                                                                                                                                                      |
## Constants

| Name         | Type            | Value            | Description                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | --------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MXMPYBITS    |                 | +2               | The first step is to calculate how many clocks it takes our multiply to come back with an answer within.  The time in the multiply depends upon the input value with the fewest number of bits--to keep the pipeline depth short.  So, let's find the fewest number of bits here.                                                                                                                |
| LCLDELAY     |                 | MPYDELAY         | In an environment when CKPCE > 1, the multiply delay isn't necessarily the delay felt by this algorithm--measured in i_ce's.  In particular, if the multiply can operate with more operations per clock, it can appear to finish "faster". Since most of the logic in this core operates on the slower clock, we'll need to map that speed into the number of slower clock ticks that it takes.  |
| LGDELAY      |                 |                  |                                                                                                                                                                                                                                                                                                                                                                                                  |
| AUXLEN       |                 | undefined        |                                                                                                                                                                                                                                                                                                                                                                                                  |
| MPYREMAINDER |                 | MPYDELAY - CKPCE |                                                                                                                                                                                                                                                                                                                                                                                                  |
| F_LGDEPTH    |                 |                  |                                                                                                                                                                                                                                                                                                                                                                                                  |
| F_DEPTH      |                 | AUXLEN           |                                                                                                                                                                                                                                                                                                                                                                                                  |
| F_D          | [F_LGDEPTH-1:0] | -1               |                                                                                                                                                                                                                                                                                                                                                                                                  |
## Processes
- unnamed: ( @(posedge i_clk) )
**Description**
Set up the input to the multiply

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
**Description**
Let's see if we can improve our performance at all by
moving our test one clock earlier.  If nothing else, it should
help induction finish one (or more) clocks ealier than
otherwise

- unnamed: ( @(*) )
- unnamed: ( @(posedge i_clk) )
**Description**
Induction helpers

- unnamed: ( @(*) )
## Instantiations

- do_rnd_left_r: convround
- do_rnd_left_i: convround
- do_rnd_right_r: convround
- do_rnd_right_i: convround
