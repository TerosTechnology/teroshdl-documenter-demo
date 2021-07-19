# Entity: T80pa

- **File**: T80pa.vhd
## Diagram

![Diagram](T80pa.svg "Diagram")
## Description

Z80 compatible microprocessor core, preudo-asynchronous top level (by Sorgelig)
Copyright (c) 2001-2002 Daniel Wallner (jesus@opencores.org)
All rights reserved
Redistribution and use in source and synthezised forms, with or without
modification, are permitted provided that the following conditions are met:
Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
Redistributions in synthesized form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
Neither the name of the author nor the names of other contributors may
be used to endorse or promote products derived from this software without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
Please report bugs to the author, but before you do so, please
make sure that this is not a derivative work and that
you have the latest version of this file.
The latest version of this file can be found at:
 http://www.opencores.org/cvsweb.shtml/t80/
File history :
v1.0: convert to preudo-asynchronous model with original Z80 timings.
v2.0: rewritten for more precise timings.
      support for both CEN_n and CEN_p set to 1. Effective clock will be CLK/2.
v2.1: Output Address 0 during non-bus MCycle (fix ZX contention)
v2.2: Interrupt acknowledge cycle has been corrected
      WAIT_n is broken in T80.vhd. Simulate correct WAIT_n locally.
v2.3: Output last used Address during non-bus MCycle seems more correct.
## Generics

| Generic name | Type    | Value | Description                                 |
| ------------ | ------- | ----- | ------------------------------------------- |
| Mode         | integer | 0     | 0 => Z80, 1 => Fast Z80, 2 => 8080, 3 => GB |
## Ports

| Port name | Direction | Type                           | Description                                                                   |
| --------- | --------- | ------------------------------ | ----------------------------------------------------------------------------- |
| RESET_n   | in        | std_logic                      |                                                                               |
| CLK       | in        | std_logic                      |                                                                               |
| CEN_p     | in        | std_logic                      |                                                                               |
| CEN_n     | in        | std_logic                      |                                                                               |
| WAIT_n    | in        | std_logic                      |                                                                               |
| INT_n     | in        | std_logic                      |                                                                               |
| NMI_n     | in        | std_logic                      |                                                                               |
| BUSRQ_n   | in        | std_logic                      |                                                                               |
| M1_n      | out       | std_logic                      |                                                                               |
| MREQ_n    | out       | std_logic                      |                                                                               |
| IORQ_n    | out       | std_logic                      |                                                                               |
| RD_n      | out       | std_logic                      |                                                                               |
| WR_n      | out       | std_logic                      |                                                                               |
| RFSH_n    | out       | std_logic                      |                                                                               |
| HALT_n    | out       | std_logic                      |                                                                               |
| BUSAK_n   | out       | std_logic                      |                                                                               |
| OUT0      | in        | std_logic                      | 0 => OUT(C),0, 1 => OUT(C),255                                                |
| A         | out       | std_logic_vector(15 downto 0)  |                                                                               |
| DI        | in        | std_logic_vector(7 downto 0)   |                                                                               |
| DO        | out       | std_logic_vector(7 downto 0)   |                                                                               |
| REG       | out       | std_logic_vector(211 downto 0) | IFF2, IFF1, IM, IY, HL', DE', BC', IX, HL, DE, BC, PC, SP, R, I, F', A', F, A |
| DIRSet    | in        | std_logic                      |                                                                               |
| DIR       | in        | std_logic_vector(211 downto 0) | IFF2, IFF1, IM, IY, HL', DE', BC', IX, HL, DE, BC, PC, SP, R, I, F', A', F, A |
## Signals

| Name        | Type                          | Description        |
| ----------- | ----------------------------- | ------------------ |
| IntCycle_n  | std_logic                     |                    |
| IntCycleD_n | std_logic_vector(1 downto 0)  |                    |
| IORQ        | std_logic                     |                    |
| NoRead      | std_logic                     |                    |
| Write       | std_logic                     |                    |
| BUSAK       | std_logic                     |                    |
| DI_Reg      | std_logic_vector (7 downto 0) | Input synchroniser |
| MCycle      | std_logic_vector(2 downto 0)  |                    |
| TState      | std_logic_vector(2 downto 0)  |                    |
| CEN_pol     | std_logic                     |                    |
| CEN         | std_logic                     |                    |
## Processes
- unnamed: ( CLK )
## Instantiations

- u0: T80
