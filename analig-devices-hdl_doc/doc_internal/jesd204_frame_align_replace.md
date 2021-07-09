# Entity: jesd204_frame_align_replace

## Diagram

![Diagram](jesd204_frame_align_replace.svg "Diagram")
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
   DATA_PATH_WIDTH = 4, 8
   F=1,2,3,4,6, and multiples of DATA_PATH_WIDTH
 
## Generics

| Generic name    | Type | Value | Description |
| --------------- | ---- | ----- | ----------- |
| DATA_PATH_WIDTH |      | 4     |             |
| IS_RX           |      | 1'b1  |             |
| ENABLED         |      | 1'b1  |             |
## Ports

| Port name                    | Direction | Type                    | Description |
| ---------------------------- | --------- | ----------------------- | ----------- |
| clk                          | input     |                         |             |
| reset                        | input     |                         |             |
| cfg_octets_per_frame         | input     | [7:0]                   |             |
| cfg_disable_char_replacement | input     |                         |             |
| cfg_disable_scrambler        | input     |                         |             |
| data                         | input     | [DATA_PATH_WIDTH*8-1:0] |             |
| eof                          | input     | [DATA_PATH_WIDTH-1:0]   |             |
| rx_char_is_a                 | input     | [DATA_PATH_WIDTH-1:0]   |             |
| rx_char_is_f                 | input     | [DATA_PATH_WIDTH-1:0]   |             |
| tx_eomf                      | input     | [DATA_PATH_WIDTH-1:0]   |             |
| data_out                     | output    | [DATA_PATH_WIDTH*8-1:0] |             |
| charisk_out                  | output    | [DATA_PATH_WIDTH-1:0]   |             |
## Signals

| Name                      | Type                                 | Description |
| ------------------------- | ------------------------------------ | ----------- |
| single_eof                | wire                                 |             |
| data_d1                   | reg  [DATA_PATH_WIDTH*8-1:0]         |             |
| data_d2                   | reg  [DATA_PATH_WIDTH*8-1:0]         |             |
| char_is_align             | wire [DATA_PATH_WIDTH-1:0]           |             |
| char_is_align_d1          | reg  [DATA_PATH_WIDTH-1:0]           |             |
| char_is_align_d2          | reg  [DATA_PATH_WIDTH-1:0]           |             |
| saved_data                | wire [((DATA_PATH_WIDTH*2)+4)*8-1:0] |             |
| saved_char_is_align       | wire [((DATA_PATH_WIDTH*2)+4)-1:0]   |             |
| data_replaced             | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| data_prev_eof             | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| data_prev_prev_eof        | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| data_prev_eof_single      | reg  [7:0]                           |             |
| data_prev_eof_single_int  | reg  [7:0]                           |             |
| char_is_align_prev_single | reg                                  |             |
| prev_data_1               | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data_1          | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align_1      | wire [DATA_PATH_WIDTH-1:0]           |             |
| prev_data_2               | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data_2          | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align_2      | wire [DATA_PATH_WIDTH-1:0]           |             |
| prev_data_3               | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data_3          | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align_3      | wire [DATA_PATH_WIDTH-1:0]           |             |
| prev_data_4               | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data_4          | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align_4      | wire [DATA_PATH_WIDTH-1:0]           |             |
| prev_data_6               | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data_6          | wire [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align_6      | wire [DATA_PATH_WIDTH-1:0]           |             |
| prev_data                 | reg  [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_prev_data            | reg  [DATA_PATH_WIDTH*8-1:0]         |             |
| prev_char_is_align        | reg  [DATA_PATH_WIDTH-1:0]           |             |
| jj                        | reg  [DPW_LOG2:0]                    |             |
| ll                        | reg  [DPW_LOG2:0]                    |             |
## Constants

| Name     | Type | Value                                                   | Description |
| -------- | ---- | ------------------------------------------------------- | ----------- |
| DPW_LOG2 |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(eof, data) )
**Description**
Capture single EOF in current cycle

- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
