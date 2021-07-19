# Entity: jesd204_rx_header

- **File**: jesd204_rx_header.v
## Diagram

![Diagram](jesd204_rx_header.svg "Diagram")
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
 
## Ports

| Port name                | Direction | Type      | Description                                  |
| ------------------------ | --------- | --------- | -------------------------------------------- |
| clk                      | input     |           |                                              |
| reset                    | input     |           |                                              |
| sh_lock                  | input     |           |                                              |
| header                   | input     | [1:0]     |                                              |
| cfg_header_mode          | input     | [1:0]     | 0 - CRC12 ; 1 - CRC3; 2 - FEC; 3 - CMD       |
| cfg_rx_thresh_emb_err    | input     | [4:0]     |                                              |
| cfg_beats_per_multiframe | input     | [7:0]     |                                              |
| emb_lock                 | output    |           |                                              |
| valid_eomb               | output    |           |                                              |
| valid_eoemb              | output    |           |                                              |
| crc12                    | output    | [11:0]    | Received header data qualified by valid_eomb |
| crc3                     | output    | [2:0]     |                                              |
| fec                      | output    | [25:0]    |                                              |
| cmd                      | output    | [18:0]    |                                              |
| sh_count                 | output    | reg [7:0] |                                              |
| status_lane_emb_state    | output    | [2:0]     |                                              |
| event_invalid_header     | output    |           |                                              |
| event_unexpected_eomb    | output    |           |                                              |
| event_unexpected_eoemb   | output    |           |                                              |
## Signals

| Name             | Type        | Description |
| ---------------- | ----------- | ----------- |
| state            | reg [2:0]   |             |
| next_state       | reg [2:0]   |             |
| sync_word        | reg [31:0]  |             |
| header_bit       | wire        |             |
| invalid_sequence | wire        |             |
| invalid_eoemb    | wire        |             |
| invalid_eomb     | wire        |             |
| cmd0             | wire [6:0]  |             |
| cmd1             | wire [6:0]  |             |
| cmd3             | wire [18:0] |             |
| eoemb            | wire        |             |
| eomb             | wire        |             |
| emb_vcount       | reg [1:0]   |             |
| emb_icount       | reg [4:0]   |             |
## Constants

| Name           | Type | Value  | Description |
| -------------- | ---- | ------ | ----------- |
| STATE_EMB_INIT |      | 3'b001 |             |
| STATE_EMB_HUNT |      | 3'b010 |             |
| STATE_EMB_LOCK |      | 3'b100 |             |
| BIT_EMB_INIT   |      | 0      |             |
| BIT_EMB_HUNT   |      | 1      |             |
| BIT_EMB_LOCK   |      | 2      |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(*) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
