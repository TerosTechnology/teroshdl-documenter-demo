# Entity: arith_scaler

- **File**: arith_scaler.vhdl
## Diagram

![Diagram](arith_scaler.svg "Diagram")
## Description

 EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:					Thomas B. Preusser

 Entity:					A flexible scaler for fixed-point values.

 Description:
 -------------------------------------
 A flexible scaler for fixed-point values. The scaler is implemented for a set
 of multiplier and divider values. Each individual scaling operation can
 arbitrarily select one value from each these sets.

 The computation calculates: ``unsigned(arg) * MULS(msel) / DIVS(dsel)``
 rounded to the nearest (tie upwards) fixed-point result of the same precision
 as ``arg``.

 The computation is started by asserting ``start`` to high for one cycle. If a
 computation is running, it will be restarted. The completion of a calculation
 is signaled via ``done``. ``done`` is high when no computation is in progress.
 The result of the last scaling operation is stable and can be read from
 ``res``. The weight of the LSB of ``res`` is the same as the LSB of ``arg``.
 Make sure to tap a sufficient number of result bits in accordance to the
 highest scaling ratio to be used in order to avoid a truncation overflow.

 License:
 =============================================================================
 Copyright 2007-2016 Technische Universitaet Dresden - Germany
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

| Generic name | Type     | Value    | Description                                                   |
| ------------ | -------- | -------- | ------------------------------------------------------------- |
| MULS         | T_POSVEC | (0 => 1) |  The set of multipliers to choose from in scaling operations. |
| DIVS         | T_POSVEC | (0 => 1) |  The set of divisors to choose from in scaling operations.    |
## Ports

| Port name | Direction | Type                                               | Description                     |
| --------- | --------- | -------------------------------------------------- | ------------------------------- |
| clk       | in        | std_logic                                          |                                 |
| rst       | in        | std_logic                                          |                                 |
| start     | in        | std_logic                                          |  Start of Computation           |
| arg       | in        | std_logic_vector                                   |  Fixed-point value to be scaled |
| msel      | in        | std_logic_vector(log2ceil(MULS'length)-1 downto 0) |                                 |
| dsel      | in        | std_logic_vector(log2ceil(DIVS'length)-1 downto 0) |                                 |
| done      | out       | std_logic                                          |  Completion                     |
| res       | out       | std_logic_vector                                   |  Result                         |
## Signals

| Name       | Type                                         | Description                   |
| ---------- | -------------------------------------------- | ----------------------------- |
| muloffset  | unsigned(X-1 downto 0)                       |  Offset for correct rounding. |
| multiplier | unsigned(X	 downto 0)                        |  The actual multiplier value. |
| divisor    | unsigned(R-1 downto 0)                       |  The actual divisor value.    |
| divcini    | unsigned(log2ceil(MAX_ANY_STEPS)-1 downto 0) |  Count for division steps.    |
| divmask    | tResMask                                     |                               |
## Constants

| Name          | Type                  | Value                                                                           | Description |
| ------------- | --------------------- | ------------------------------------------------------------------------------- | ----------- |
| N             | positive              |  arg'length                                                                     |             |
| X             | positive              |  log2ceil(imax(imax(MULS),<br><span style="padding-left:20px"> imax(DIVS)/2+1)) |             |
| R             | positive              |  log2ceil(imax(DIVS)+1)                                                         |             |
| DIV_PROPS     | tDivProps             |  computeProps                                                                   |             |
| MAX_MUL_STEPS | positive              |  N                                                                              |             |
| MAX_DIV_STEPS | positive              |  imax(DIV_PROPS.steps)                                                          |             |
| MAX_ANY_STEPS | positive              |  imax(MAX_MUL_STEPS,<br><span style="padding-left:20px"> MAX_DIV_STEPS)         |             |
| RES_MASKS     | tResMasks(DIVS'range) |  computeMasks                                                                   |             |
## Types

| Name      | Type                                | Description           |
| --------- | ----------------------------------- | --------------------- |
| tDivProps |                                     |  Division Properties  |
| tResMasks | array(natural range<>) of tResMask  |                       |
## Functions
- computeProps <font id="function_arguments">()</font> <font id="function_return">return tDivProps </font>
- computeMasks <font id="function_arguments">()</font> <font id="function_return">return tResMasks </font>
