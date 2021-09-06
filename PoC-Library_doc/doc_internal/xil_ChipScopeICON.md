# Entity: xil_ChipScopeICON

- **File**: xil_ChipScopeICON.vhdl
## Diagram

![Diagram](xil_ChipScopeICON.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:				 	Patrick Lehmann

 Entity:				 	Generic Xilinx ChipScope ICON wrapper

 Description:
 -------------------------------------
 This module wraps 15 ChipScope ICON IP core netlists generated from ChipScope
 ICON xco files. The generic parameter ``PORTS`` selects the apropriate ICON
 instance with 1 to 15 ICON ``ControlBus`` ports. Each ``ControlBus`` port is
 of type ``T_XIL_CHIPSCOPE_CONTROL`` and of mode ``inout``.

 .. rubric:: Compile required CoreGenerator IP Cores to Netlists with PoC

 Please use the provided Xilinx ISE compile command ``ise`` in PoC to recreate
 the needed source and netlist files on your local machine.

 .. code-block:: PowerShell

    cd PoCRoot
    .\poc.ps1 ise PoC.xil.ChipScopeICON --board=KC705

 SeeAlso:
 :doc:`Using PoC -> Synthesis </UsingPoC/Synthesis>`
   For how to run synthesis with PoC and CoreGenerator.

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

| Generic name | Type     | Value | Description |
| ------------ | -------- | ----- | ----------- |
| PORTS        | positive |       |             |
## Ports

| Port name  | Direction | Type                                               | Description |
| ---------- | --------- | -------------------------------------------------- | ----------- |
| ControlBus | inout     | T_XIL_CHIPSCOPE_CONTROL_VECTOR(PORTS - 1 downto 0) |             |
