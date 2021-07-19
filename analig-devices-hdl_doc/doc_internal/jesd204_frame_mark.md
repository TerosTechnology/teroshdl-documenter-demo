# Entity: jesd204_frame_mark

- **File**: jesd204_frame_mark.v
## Diagram

![Diagram](jesd204_frame_mark.svg "Diagram")
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
 Limitations:
  for DATA_PATH_WIDTH = 4, 8
    F*K=4, multiples of DATA_PATH_WIDTH
    F=1,2,3,4,6, and multiples of DATA_PATH_WIDTH
  for DATA_PATH_WIDTH = 6
    F=3,6
  for DATA_PATH_WIDTH = 12
    F=3,6,12
 
## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| DATA_PATH_WIDTH |      | 4     |             |
## Ports

| Port name                 | Direction | Type                  | Description |
| ------------------------- | --------- | --------------------- | ----------- |
| clk                       | input     |                       |             |
| reset                     | input     |                       |             |
| cfg_octets_per_multiframe | input     | [9:0]                 |             |
| cfg_beats_per_multiframe  | input     | [7:0]                 |             |
| cfg_octets_per_frame      | input     | [7:0]                 |             |
| sof                       | output    | [DATA_PATH_WIDTH-1:0] |             |
| eof                       | output    | [DATA_PATH_WIDTH-1:0] |             |
| somf                      | output    | [DATA_PATH_WIDTH-1:0] |             |
| eomf                      | output    | [DATA_PATH_WIDTH-1:0] |             |
## Signals

| Name                     | Type                             | Description                                       |
| ------------------------ | -------------------------------- | ------------------------------------------------- |
| octets_per_mf_4_mod_8    | wire                             | For DATA_PATH_WIDTH = 8, special case if F*K%8=4  |
| cur_beats_per_multiframe | reg [BEATS_PER_MF_WIDTH-1:0]     |                                                   |
| mf_phase                 | reg                              |                                                   |
| beat_cnt_mod_3           | reg [1:0]                        |                                                   |
| beat_cnt_frame           | reg [BEATS_PER_FRAME_WIDTH-1:0]  |                                                   |
| cur_sof                  | wire                             |                                                   |
| cur_eof                  | wire                             |                                                   |
| beat_cnt_mf              | reg [BEATS_PER_MF_WIDTH-1:0]     |                                                   |
| cur_somf                 | wire                             |                                                   |
| cur_eomf                 | wire                             |                                                   |
| default_sof              | wire [DATA_PATH_WIDTH-1:0]       |                                                   |
| default_eof              | wire [DATA_PATH_WIDTH-1:0]       |                                                   |
| cfg_beats_per_frame      | wire [BEATS_PER_FRAME_WIDTH-1:0] |                                                   |
| sof_f_3                  | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
| eof_f_3                  | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
| sof_f_6                  | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
| eof_f_6                  | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
| sof_f_12                 | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
| eof_f_12                 | reg [DATA_PATH_WIDTH-1:0]        |                                                   |
## Constants

| Name                  | Type | Value                                                   | Description |
| --------------------- | ---- | ------------------------------------------------------- | ----------- |
| MAX_OCTETS_PER_FRAME  |      | 32                                                      |             |
| DPW_LOG2              |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |             |
| CW                    |      | MAX_OCTETS_PER_FRA                                      |             |
| BEATS_PER_FRAME_WIDTH |      | CW-DPW_LOG2                                             |             |
| BEATS_PER_MF_WIDTH    |      | 10-DPW_LOG2                                             |             |
