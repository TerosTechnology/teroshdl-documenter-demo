# Entity: bimpy

## Diagram

![Diagram](bimpy.svg "Diagram")
## Description

Filename:	../../ifft64/bimpy.v
 Project:	A General Purpose Pipelined FFT Implementation
 Purpose:	A simple 2-bit multiply based upon the fact that LUT's allow
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

| Generic name | Type | Value | Description           |
| ------------ | ---- | ----- | --------------------- |
| BW           |      | 18    | Number of bits in i_b |
## Ports

| Port name | Direction | Type              | Description |
| --------- | --------- | ----------------- | ----------- |
| i_clk     | input     | wire              |             |
|  i_ce     | input     | wire              |             |
| i_a       | input     | wire	[(LUTB-1):0] |             |
| i_b       | input     | wire	[(BW-1):0]   |             |
| o_r       | output    | [(BW+LUTB-1):0]   |             |
## Signals

| Name         | Type                 | Description |
| ------------ | -------------------- | ----------- |
| w_r          | wire [(BW+LUTB-2):0] |             |
| c            | wire [(BW+LUTB-3):1] |             |
| f_past_valid | reg                  |             |
## Constants

| Name | Type | Value | Description                                |
| ---- | ---- | ----- | ------------------------------------------ |
| LUTB |      | 2     | Number of bits in i_a for our LUT multiply |
## Processes
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
- unnamed: ( @(posedge i_clk) )
