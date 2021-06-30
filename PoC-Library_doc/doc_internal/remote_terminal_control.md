# Entity: remote_terminal_control

## Diagram

![Diagram](remote_terminal_control.svg "Diagram")
## Description

EMACS settings: -*-  tab-width:2  -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
Description:  Simple terminal interface to monitor and manipulate
              basic IO components such as buttons, slide switches, LED
              and hexadecimal displays.
A typical transport would be a UART connection using a terminal application.
A command line starts with a single letter identifying the addressed
resource type:
   R .. Reset  - strobed input to the design
   P .. Pulse  - strobed input to the design
   S .. Switch - stateful input to the design
   L .. Light  - (bit) output from the design
   D .. Digit  - (hex) output from the design
This letter may be followed by a hexadecimal input vector, which triggers
   R - a strobe on the corresponding inputs,
   P - a strobe on the corresponding inputs, and
   S - a state toggle of the corresponding inputs.
The input vector is ignored for outputs from the design.
The command line may contain an arbitrary amount of spaces.
The terminal interface will echo with:
  <resource character>[<bit count>'<hex output vector>]
The <bit count> and <hex output vector> will only be present if, at least,
a single instance of the addressed resource type is available.
In particular, the resource characters of lines starting with other than
the listed resource types will simply be echoed.
The <bit count> describes how many bits of the addressed resource are
available, which may be used to explore the resources using a command line
with no or a zero input argument. The <bit count> is typically provided in
decimal (default) but may be changed to hexadecimal through the generic
parameter COUNT_DECIMAL.
The <hex output vector> acknowledges the input (R and P) and informs about
the current state (S, L and D).
Example:
 > L
   L10'21D
 > D
   D8'5E
 > A
   A
 > S
   S6'00
 > S3A
   S6'3A
 > S 1
   S6'3B
 > P8
   P4'8
 > P
   P4'0
Authors:      Thomas B. Preußer <thomas.preusser@utexas.edu>
Copyright 2007-2014 Technische Universität Dresden - Germany
                    Chair of VLSI-Design, Diagnostics and Architecture
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
## Generics

| Generic name  | Type    | Value | Description |
| ------------- | ------- | ----- | ----------- |
| RESET_COUNT   | natural |       |             |
| PULSE_COUNT   | natural |       |             |
| SWITCH_COUNT  | natural |       |             |
| LIGHT_COUNT   | natural |       |             |
| DIGIT_COUNT   | natural |       |             |
| COUNT_DECIMAL | boolean | true  |             |
## Ports

| Port name | Direction | Type                                                | Description       |
| --------- | --------- | --------------------------------------------------- | ----------------- |
| clk       | in        | std_logic                                           | Global Control    |
| rst       | in        | std_logic                                           |                   |
| idat      | in        | std_logic_vector(6 downto 0)                        | UART Connectivity |
| istb      | in        | std_logic                                           |                   |
| odat      | out       | std_logic_vector(6 downto 0)                        |                   |
| ordy      | in        | std_logic                                           |                   |
| oput      | out       | std_logic                                           |                   |
| resets    | out       | std_logic_vector(imax(RESET_COUNT -1, 0) downto 0)  | Control Outputs   |
| pulses    | out       | std_logic_vector(imax(PULSE_COUNT -1, 0) downto 0)  |                   |
| switches  | out       | std_logic_vector(imax(SWITCH_COUNT-1, 0) downto 0)  |                   |
| lights    | in        | std_logic_vector(imax(  LIGHT_COUNT-1, 0) downto 0) | Monitor Inputs    |
| digits    | in        | std_logic_vector(imax(4*DIGIT_COUNT-1, 0) downto 0) |                   |
## Signals

| Name   | Type                              | Description |
| ------ | --------------------------------- | ----------- |
| BufVld | std_logic                         |             |
| BufCmd | std_logic_vector(4 downto 0)      |             |
| BufCnt | unsigned(CNT_BITS-1 downto 0)     |             |
| BufEco | std_logic_vector(0 to ECO_BITS-1) |             |
| BufAck | std_logic                         |             |
## Constants

| Name       | Type                     | Value                                                                                                                                        | Description |
| ---------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| COUNTS     | tCounts                  |  (0,                                  RESET_COUNT,   PULSE_COUNT, SWITCH_COUNT,                                  LIGHT_COUNT, 4*DIGIT_COUNT) |             |
| PAR_BITS   | natural                  |  max_count(COUNTS(tInput))                                                                                                                   |             |
| RES_BITS   | natural                  |  max_count(COUNTS(tActual))                                                                                                                  |             |
| ECO_BITS   | natural                  |  4*((RES_BITS+3)/4)                                                                                                                          |             |
| CNT_BITS   | positive                 |  makeCntBits                                                                                                                                 |             |
| OUT_COUNTS | tOutCounts(COUNTS'range) |  makeOutCounts                                                                                                                               |             |
| CODES      | tCodes(tActual)          |  ("10010", "10000", "10011", "01100", "00100")                                                                                               |             |
| STROBES    | tStrobes(tInput)         |  (true, true, false)                                                                                                                         |             |
## Types

| Name       | Type                                                                      | Description |
| ---------- | ------------------------------------------------------------------------- | ----------- |
| tKind      | (KIND_NONE, KIND_RESET, KIND_PULSE, KIND_SWITCH, KIND_LIGHT, KIND_DIGIT)  |             |
| tCounts    |                                                                           | Counts      |
| tOutCounts |                                                                           |             |
| tCodes     |                                                                           |             |
| tStrobes   |                                                                           |             |
## Functions
- max_count <font id="function_arguments">(arr : tCounts) </font> <font id="function_return">return natural </font>
- log10ceil <font id="function_arguments">(x : natural) </font> <font id="function_return">return positive </font>
- makeCntBits <font id="function_arguments">()</font> <font id="function_return">return positive </font>
- makeOutCounts <font id="function_arguments">()</font> <font id="function_return">return tOutCounts </font>
