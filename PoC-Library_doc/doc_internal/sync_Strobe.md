# Entity: sync_Strobe

## Diagram

![Diagram](sync_Strobe.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:         Patrick Lehmann
                 Steffen Koehler
Entity:          Synchronizes a strobe signal across clock-domain boundaries
Description:
-------------------------------------
This module synchronizes multiple high-active bits from clock-domain
``Clock1`` to clock-domain ``Clock2``. The clock-domain boundary crossing is
done by a T-FF, two synchronizer D-FFs and a reconstructive XOR. A busy
flag is additionally calculated and can be used to block new inputs. All
bits are independent from each other. Multiple consecutive strobes are
suppressed by a rising edge detection.
.. ATTENTION::
   Use this synchronizer only for one-cycle high-active signals (strobes).
.. image:: /_static/misc/sync/sync_Strobe.*
   :target: ../../../_static/misc/sync/sync_Strobe.svg
Constraints:
  This module uses sub modules which need to be constrained. Please
  attend to the notes of the instantiated sub modules.
License:
=============================================================================
Copyright 2007-2015 Technische Universitaet Dresden - Germany
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

| Generic name        | Type              | Value                 | Description                                 |
| ------------------- | ----------------- | --------------------- | ------------------------------------------- |
| BITS                | positive          | 1                     | number of bit to be synchronized            |
| GATED_INPUT_BY_BUSY | boolean           | TRUE                  | use gated input (by busy signal)            |
| SYNC_DEPTH          | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low | generate SYNC_DEPTH many stages, at least 2 |
## Ports

| Port name | Direction | Type                                | Description                  |
| --------- | --------- | ----------------------------------- | ---------------------------- |
| Clock1    | in        | std_logic                           | <Clock>  input clock domain  |
| Clock2    | in        | std_logic                           | <Clock>  output clock domain |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) | @Clock1:  input bits         |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) | @Clock2:  output bits        |
| Busy      | out       | std_logic_vector(BITS - 1 downto 0) | @Clock1:  busy bits          |
## Signals

| Name         | Type                                | Description |
| ------------ | ----------------------------------- | ----------- |
| syncClk1_In  | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk1_Out | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk2_In  | std_logic_vector(BITS - 1 downto 0) |             |
| syncClk2_Out | std_logic_vector(BITS - 1 downto 0) |             |
## Instantiations

- syncClk2: PoC.sync_Bits
- syncClk1: PoC.sync_Bits
