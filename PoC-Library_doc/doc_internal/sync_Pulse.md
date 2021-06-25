# Entity: sync_Pulse
## Diagram
![Diagram](sync_Pulse.svg "Diagram")
## Description
EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:         Patrick Lehmann
Entity:          Synchronizes a very short pulse across clock-domain boundaries
Description:
-------------------------------------
This module synchronizes multiple pulsed bits into the clock-domain ``Clock``.
The clock-domain boundary crossing is done by two synchronizer D-FFs. All bits
are independent from each other. If a known vendor like Altera or Xilinx are
recognized, a vendor specific implementation is chosen.
.. ATTENTION::
   Use this synchronizer for very short signals (pulse).
Constraints:
  General:
    Please add constraints for meta stability to all '_meta' signals and
    timing ignore constraints to all '_async' signals.
  Xilinx:
    In case of a Xilinx device, this module will instantiate the optimized
    module PoC.xil.sync.Pulse. Please attend to the notes of sync_Bits.vhdl.
  Altera sdc file:
    TODO
SeeAlso:
:doc:`PoC.misc.sync.Bits </IPCores/misc/sync/sync_Bits>`
  For a common 2 D-FF synchronizer for *flag*-signals.
:doc:`PoC.misc.sync.Reset </IPCores/misc/sync/sync_Reset>`
  For a special 2 D-FF synchronizer for *reset*-signals.
:doc:`PoC.misc.sync.Strobe </IPCores/misc/sync/sync_Strobe>`
  For a synchronizer for *strobe*-signals.
:doc:`PoC.misc.sync.Vector </IPCores/misc/sync/sync_Vector>`
  For a multiple bits capable synchronizer.
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
| Generic name | Type              | Value                 | Description                                 |
| ------------ | ----------------- | --------------------- | ------------------------------------------- |
| BITS         | positive          | 1                     | number of bit to be synchronized            |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low | generate SYNC_DEPTH many stages, at least 2 |
## Ports
| Port name | Direction | Type                                | Description                  |
| --------- | --------- | ----------------------------------- | ---------------------------- |
| Clock     | in        | std_logic                           | <Clock>  output clock domain |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) | @async:  input bits          |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) | @Clock:  output bits         |
## Constants
| Name     | Type          | Value        | Description |
| -------- | ------------- | ------------ | ----------- |
| DEV_INFO | T_DEVICE_INFO |  DEVICE_INFO |             |
