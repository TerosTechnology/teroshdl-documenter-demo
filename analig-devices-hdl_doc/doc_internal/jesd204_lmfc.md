# Entity: jesd204_lmfc

- **File**: jesd204_lmfc.v
## Diagram

![Diagram](jesd204_lmfc.svg "Diagram")
## Description

The ADI JESD204 Core is released under the following license, which is
 different than all other HDL cores in this repository.
 Please read this, and understand the freedoms and responsibilities you have
 by using this source code/core.
 The JESD204 HDL, is copyright © 2016-2017 Analog Devices Inc.
 This core is free software, you can use run, copy, study, change, ask
 questions about and improve this core. Distribution of source, or resulting
 binaries (including those inside an FPGA or ASIC) require you to release the
 source of the entire project (excluding the system libraries provide by the
 tools/compiler/FPGA vendor). These are the terms of the GNU General Public
 License version 2 as published by the Free Software Foundation.
 This core  is distributed in the hope that it will be useful, but WITHOUT ANY
 WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
 A PARTICULAR PURPOSE. See the GNU General Public License for more details.
 You should have received a copy of the GNU General Public License version 2
 along with this source code, and binary.  If not, see
 <http://www.gnu.org/licenses/>.
 Commercial licenses (with commercial support) of this JESD204 core are also
 available under terms different than the General Public License. (e.g. they
 do not require you to accompany any image (FPGA or ASIC) using the JESD204
 core with any corresponding source code.) For these alternate terms you must
 purchase a license from Analog Devices Technology Licensing Office. Users
 interested in such a license should contact jesd204-licensing@analog.com for
 more information. This commercial license is sub-licensable (if you purchase
 chips from Analog Devices, incorporate them into your PCB level product, and
 purchase a JESD204 license, end users of your product will also have a
 license to use this core in a commercial setting without releasing their
 source code).
 In addition, we kindly ask you to acknowledge ADI in any program, application
 or publication in which you use this JESD204 HDL core. (You are not required
 to do so; it is up to your common sense to decide whether you want to comply
 with this request or not.) For general publications, we suggest referencing :
 “The design and implementation of the JESD204 HDL Core used in this project
 is copyright © 2016-2017, Analog Devices, Inc.”
 
## Generics

| Generic name    | Type | Value | Description              |
| --------------- | ---- | ----- | ------------------------ |
| LINK_MODE       |      | 1     | 2 - 64B/66B;  1 - 8B/10B |
| DATA_PATH_WIDTH |      | 4     |                          |
## Ports

| Port name                 | Direction | Type  | Description                 |
| ------------------------- | --------- | ----- | --------------------------- |
| clk                       | input     |       |                             |
| reset                     | input     |       |                             |
| sysref                    | input     |       |                             |
| cfg_octets_per_multiframe | input     | [9:0] |                             |
| cfg_beats_per_multiframe  | input     | [7:0] |                             |
| cfg_lmfc_offset           | input     | [7:0] |                             |
| cfg_sysref_oneshot        | input     |       |                             |
| cfg_sysref_disable        | input     |       |                             |
| lmfc_edge                 | output    |       |                             |
| lmfc_clk                  | output    |       |                             |
| lmfc_counter              | output    | [7:0] |                             |
| lmc_edge                  | output    |       | Local MultiBlock clock edge |
| lmc_quarter_edge          | output    |       |                             |
| eoemb                     | output    |       | End of Extended MultiBlock  |
| sysref_edge               | output    |       |                             |
| sysref_alignment_error    | output    |       |                             |
## Signals

| Name                           | Type                        | Description                                                                   |
| ------------------------------ | --------------------------- | ----------------------------------------------------------------------------- |
| cfg_whole_beats_per_multiframe | reg  [BEATS_PER_MF_WIDTH:0] |                                                                               |
| sysref_r                       | reg                         |                                                                               |
| sysref_d1                      | reg                         |                                                                               |
| sysref_d2                      | reg                         |                                                                               |
| sysref_d3                      | reg                         |                                                                               |
| sysref_captured                | reg                         |                                                                               |
| lmfc_counter_next              | reg [7:0]                   | lmfc_octet_counter = lmfc_counter * (char_clock_rate / device_clock_rate) */  |
| lmfc_clk_p1                    | reg                         |                                                                               |
| lmfc_active                    | reg                         |                                                                               |
## Constants

| Name               | Type | Value                                                   | Description |
| ------------------ | ---- | ------------------------------------------------------- | ----------- |
| DPW_LOG2           |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |             |
| BEATS_PER_MF_WIDTH |      | 10-DPW_LOG2                                             |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
1 MultiBlock = 32 blocks

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
End of Extended MultiBlock

- unnamed: ( @(posedge clk) )
