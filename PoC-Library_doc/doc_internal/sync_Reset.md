# Entity: sync_Reset

## Diagram

![Diagram](sync_Reset.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:         Patrick Lehmann
Entity:          Synchronizes a reset signal across clock-domain boundaries
Description:
-------------------------------------
This module synchronizes an asynchronous reset signal to the clock
``Clock``. The ``Input`` can be asserted and de-asserted at any time.
The ``Output`` is asserted asynchronously and de-asserted synchronously
to the clock.
.. ATTENTION::
   Use this synchronizer only to asynchronously reset your design.
   The 'Output' should be feed by global buffer to the destination FFs, so
   that, it reaches their reset inputs within one clock cycle.
Constraints:
  General:
    Please add constraints for meta stability to all '_meta' signals and
    timing ignore constraints to all '_async' signals.
  Xilinx:
    In case of a Xilinx device, this module will instantiate the optimized
    module xil_SyncReset. Please attend to the notes of xil_SyncReset.
  Altera sdc file:
    TODO
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
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low | generate SYNC_DEPTH many stages, at least 2 |
## Ports

| Port name | Direction | Type      | Description                  |
| --------- | --------- | --------- | ---------------------------- |
| Clock     | in        | std_logic | <Clock>  output clock domain |
| Input     | in        | std_logic | @async:  reset input         |
| Output    | out       | std_logic | @Clock:  reset output        |
