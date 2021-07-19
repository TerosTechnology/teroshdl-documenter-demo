# Entity: jesd204_rx_frame_align

- **File**: jesd204_rx_frame_align.v
## Diagram

![Diagram](jesd204_rx_frame_align.svg "Diagram")
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

| Generic name        | Type | Value | Description |
| ------------------- | ---- | ----- | ----------- |
| DATA_PATH_WIDTH     |      | 4     |             |
| ENABLE_CHAR_REPLACE |      | 0     |             |
## Ports

| Port name                    | Direction | Type                    | Description |
| ---------------------------- | --------- | ----------------------- | ----------- |
| clk                          | input     |                         |             |
| reset                        | input     |                         |             |
| cfg_octets_per_multiframe    | input     | [9:0]                   |             |
| cfg_octets_per_frame         | input     | [7:0]                   |             |
| cfg_disable_char_replacement | input     |                         |             |
| cfg_disable_scrambler        | input     |                         |             |
| charisk28                    | input     | [DATA_PATH_WIDTH-1:0]   |             |
| data                         | input     | [DATA_PATH_WIDTH*8-1:0] |             |
| data_replaced                | output    | [DATA_PATH_WIDTH*8-1:0] |             |
| align_err_cnt                | output    | [7:0]                   |             |
## Signals

| Name                     | Type                       | Description |
| ------------------------ | -------------------------- | ----------- |
| char_is_a                | reg  [DATA_PATH_WIDTH-1:0] |             |
| char_is_f                | reg  [DATA_PATH_WIDTH-1:0] |             |
| eof                      | wire [DATA_PATH_WIDTH-1:0] |             |
| eomf                     | wire [DATA_PATH_WIDTH-1:0] |             |
| eof_err                  | reg  [DATA_PATH_WIDTH-1:0] |             |
| eof_good                 | reg  [DATA_PATH_WIDTH-1:0] |             |
| eomf_err                 | reg  [DATA_PATH_WIDTH-1:0] |             |
| eomf_good                | reg  [DATA_PATH_WIDTH-1:0] |             |
| align_good               | reg                        |             |
| align_err                | reg                        |             |
| cur_align_err_cnt        | reg  [DPW_LOG2*2:0]        |             |
| align_err_cnt_next       | wire [8:0]                 |             |
| cfg_beats_per_multiframe | wire [7:0]                 |             |
## Constants

| Name                   | Type | Value    | Description                                                                                                                                                                                                                                               |
| ---------------------- | ---- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RESET_COUNT_ON_MF_ONLY |      | 1'b1     | Reset alignment error count on good multiframe alignment, or on good frame or multiframe alignment If disabled, misalignments could me masked if due to cfg_octets_per_multiframe mismatch or due to a slip of a multiple of cfg_octets_per_frame octets  |
| DPW_LOG2               |      | DATA_PAT |                                                                                                                                                                                                                                                           |
## Functions
- count_ones <font id="function_arguments">(input [DATA_PATH_WIDTH*2-1:0])</font> <font id="function_return">return ([DPW_LOG2*2:0])</font>
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
Alignment error counter
Resets upon good alignment

## Instantiations

- i_frame_mark: jesd204_frame_mark
- i_align_replace: jesd204_frame_align_replace
