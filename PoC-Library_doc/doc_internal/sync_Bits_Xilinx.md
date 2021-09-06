# Entity: sync_Bits_Xilinx

- **File**: sync_Bits_Xilinx.vhdl
## Diagram

![Diagram](sync_Bits_Xilinx.svg "Diagram")
## Description

 EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
 vim: tabstop=2:shiftwidth=2:noexpandtab
 kate: tab-width 2; replace-tabs off; indent-width 2;
 =============================================================================
 Authors:           Patrick Lehmann

 Entity:           sync_Bits_Xilinx

 Description:
 -------------------------------------
 This is a multi-bit clock-domain-crossing circuit optimized for Xilinx FPGAs.
 It utilizes two `FD` instances from `UniSim.vComponents`. If you need a
 platform independent version of this synchronizer, please use
 `PoC.misc.sync.Flag`, which internally instantiates this module if a Xilinx
 FPGA is detected.

 .. ATTENTION:
     Use this synchronizer only for long time stable signals (flags).

 CONSTRAINTS:
    This relative placement of the internal sites are constrained by RLOCs.

   Xilinx ISE UCF or XCF file:
    .. code-block:: VHDL

        NET "*_async"    TIG;
        INST "*FF1_METASTABILITY_FFS" TNM = "METASTABILITY_FFS";
        TIMESPEC "TS_MetaStability" = FROM FFS TO "METASTABILITY_FFS" TIG;

   Xilinx Vivado xdc file:
    The XDC file `sync_Bits_Xilinx.xdc` must be directly applied to all
    instances of sync_Bits_Xilinx. To achieve this, set the property
    `SCOPED_TO_REF` to `sync_Bits_Xilinx` within the Vivado project.
    Load the XDC file defining the clocks before that XDC file by using the
    property `PROCESSING_ORDER`.

    .. literalinclude:: ../../../ucf/misc/sync/sync_Bits_Xilinx.xdc
       :language: xdc
       :tab-width: 2
       :linenos:
       :lines: 4-8

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

| Generic name | Type              | Value                 | Description                                  |
| ------------ | ----------------- | --------------------- | -------------------------------------------- |
| BITS         | positive          | 1                     |  number of bit to be synchronized            |
| INIT         | std_logic_vector  | x"00000000"           |  initialization bits                         |
| SYNC_DEPTH   | T_MISC_SYNC_DEPTH | T_MISC_SYNC_DEPTH'low |  generate SYNC_DEPTH many stages, at least 2 |
## Ports

| Port name | Direction | Type                                | Description                   |
| --------- | --------- | ----------------------------------- | ----------------------------- |
| Clock     | in        | std_logic                           |  <Clock>  output clock domain |
| Input     | in        | std_logic_vector(BITS - 1 downto 0) |  @async:  input bits          |
| Output    | out       | std_logic_vector(BITS - 1 downto 0) |  @Clock:  output bits         |
