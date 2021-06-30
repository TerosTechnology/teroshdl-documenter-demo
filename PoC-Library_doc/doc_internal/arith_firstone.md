# Entity: arith_firstone

## Diagram

![Diagram](arith_firstone.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					TODO
Description:
-------------------------------------
Computes from an input word, a word of the same size that has, at most,
one bit set. The output contains a set bit at the position of the rightmost
set bit of the input if and only if such a set bit exists in the input.
A typical use case for this computation would be an arbitration over
requests with a fixed and strictly ordered priority. The terminology of
the interface assumes this use case and provides some useful extras:
* Set tin <= '0' (no input token) to disallow grants altogether.
* Read tout (unused token) to see whether or any grant was issued.
* Read bin to obtain the binary index of the rightmost detected one bit.
  The index starts at zero (0) in the rightmost bit position.
This implementation uses carry chains for wider implementations.
License:
=============================================================================
Copyright 2007-2015 Technische Universität Dresden - Germany
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
=============================================================================
## Generics

| Generic name | Type     | Value | Description           |
| ------------ | -------- | ----- | --------------------- |
| N            | positive |       | Length of Token Chain |
## Ports

| Port name | Direction | Type                                     | Description              |
| --------- | --------- | ---------------------------------------- | ------------------------ |
| tin       | in        | std_logic                                | Enable:   Fed Token      |
| rqst      | in        | std_logic_vector(N-1 downto 0)           | Request:  Token Requests |
| grnt      | out       | std_logic_vector(N-1 downto 0)           | Grant:    Token Output   |
| tout      | out       | std_logic                                | Inactive: Unused Token   |
| bin       | out       | std_logic_vector(log2ceil(N)-1 downto 0) | Binary Grant Index       |
