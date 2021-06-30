# Entity: sync_Reset_Xilinx

## Diagram

![Diagram](sync_Reset_Xilinx.svg "Diagram")
## Description

EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
vim: tabstop=2:shiftwidth=2:noexpandtab
kate: tab-width 2; replace-tabs off; indent-width 2;
=============================================================================
Authors:           Patrick Lehmann
Entity:           sync_Reset_Xilinx
Description:
-------------------------------------
   This is the Xilinx specific implementation of the entity
   'PoC.misc.sync.sync_Reset'. See the description there on how to use this.
   CONSTRAINTS:
     The relative placement of the internal sites is constrained by RLOCs.
     Xilinx ISE UCF or XCF file:
       NET "*_async"    TIG;
       INST "*FF1_METASTABILITY_FFS" TNM = "METASTABILITY_FFS";
       TIMESPEC "TS_MetaStability" = FROM FFS TO "METASTABILITY_FFS" TIG;
     Xilinx Vivado xdc file:
       TODO
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
## Signals

| Name        | Type      | Description |
| ----------- | --------- | ----------- |
| Reset_async | std_logic |             |
| Reset_meta  | std_logic |             |
| Reset_sync  | std_logic |             |
## Instantiations

- FF2_METASTABILITY_FFS: FDP
- FF3_METASTABILITY_FFS: FDP
