# Entity: arith_trng

- **File**: arith_trng.vhdl
## Diagram

![Diagram](arith_trng.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:					Thomas B. Preusser
Entity:					TRNG - True Random Number Generator.
Description:
------------
This module implements a true random number generator based on sampling
combinational loops of interleaved X(N)OR gates.
Always verify the randomness of this TRNG implementation for your concrete
target platform, for instance, using the dieharder test by Robert G. Brown
[http://www.phy.duke.edu/~rgb/General/dieharder.php], which is also
directly available for many GNU/Linux distributions, e.g. Debian. Ideally,
randomness would be verified for varying operating conditions.
This design involves fast-switching combinational loops on purpose so as
to serve as sources of entropoy. This implies a relevant local power
consumption. Do not cramp large parts of a chip with these TRNGs without
ensuring appropriate heat dissipation. It often requires special
constraints or directives to enforce the proper synthesis of these
combinational loops by the tools.
License:
=============================================================================
Copyright 2007-2017 Technische Universitaet Dresden - Germany
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
=============================================================================
## Generics

| Generic name | Type     | Value | Description                  |
| ------------ | -------- | ----- | ---------------------------- |
| BITS         | positive |       | Width: Number of Oscillators |
## Ports

| Port name | Direction | Type                              | Description               |
| --------- | --------- | --------------------------------- | ------------------------- |
| clk       | in        | std_logic                         | Clock                     |
| rnd       | out       | std_logic_vector(BITS-1 downto 0) | Random Oscillator Samples |
## Signals

| Name | Type                              | Description |
| ---- | --------------------------------- | ----------- |
| osc  | std_logic_vector(BITS-1 downto 0) | Oscillators |
## Instantiations

- sync_i: sync_Bits
