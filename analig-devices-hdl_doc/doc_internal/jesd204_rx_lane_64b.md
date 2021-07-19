# Entity: jesd204_rx_lane_64b

- **File**: jesd204_rx_lane_64b.v
## Diagram

![Diagram](jesd204_rx_lane_64b.svg "Diagram")
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
| ELASTIC_BUFFER_SIZE |      | 256   |             |
| TPL_DATA_PATH_WIDTH |      | 8     |             |
| ASYNC_CLK           |      | 0     |             |
## Ports

| Port name                 | Direction | Type                        | Description                            |
| ------------------------- | --------- | --------------------------- | -------------------------------------- |
| clk                       | input     |                             |                                        |
| reset                     | input     |                             |                                        |
| device_clk                | input     |                             |                                        |
| device_reset              | input     |                             |                                        |
| phy_data                  | input     | [63:0]                      |                                        |
| phy_header                | input     | [1:0]                       |                                        |
| phy_block_sync            | input     |                             |                                        |
| rx_data                   | output    | [TPL_DATA_PATH_WIDTH*8-1:0] |                                        |
| buffer_ready_n            | output    | reg                         |                                        |
| all_buffer_ready_n        | input     |                             |                                        |
| buffer_release_n          | input     |                             |                                        |
| lmfc_edge                 | input     |                             |                                        |
| emb_lock                  | output    |                             |                                        |
| cfg_disable_scrambler     | input     |                             |                                        |
| cfg_header_mode           | input     | [1:0]                       | 0 - CRC12 ; 1 - CRC3; 2 - FEC; 3 - CMD |
| cfg_rx_thresh_emb_err     | input     | [4:0]                       |                                        |
| cfg_beats_per_multiframe  | input     | [7:0]                       |                                        |
| ctrl_err_statistics_reset | input     |                             |                                        |
| ctrl_err_statistics_mask  | input     | [3:0]                       |                                        |
| status_err_statistics_cnt | output    | [31:0]                      |                                        |
| status_lane_emb_state     | output    | [2:0]                       |                                        |
| status_lane_skew          | output    | [7:0]                       |                                        |
## Signals

| Name                       | Type        | Description |
| -------------------------- | ----------- | ----------- |
| crc12_calculated_prev      | reg [11:0]  |             |
| data_descrambled_s         | wire [63:0] |             |
| data_descrambled           | wire [63:0] |             |
| data_descrambled_reordered | wire [63:0] |             |
| crc12_received             | wire [11:0] |             |
| crc12_calculated           | wire [11:0] |             |
| event_invalid_header       | wire        |             |
| event_unexpected_eomb      | wire        |             |
| event_unexpected_eoemb     | wire        |             |
| event_crc12_mismatch       | wire        |             |
| err_cnt_rst                | wire        |             |
| rx_data_msb_s              | wire [63:0] |             |
| eomb                       | wire        |             |
| eoemb                      | wire        |             |
| sh_count                   | wire [7:0]  |             |
| crc12_on                   | reg         |             |
| crc12_rdy                  | reg         |             |
## Processes
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
- unnamed: ( @(posedge clk) )
**Description**
Control when data is written to the elastic buffer
Start writing to the buffer when current lane is multiblock locked, but if
other lanes are not writing in the next half multiblock period stop
writing.
This limits the supported lane skew to half of the multiframe

- unnamed: ( @(posedge clk) )
**Description**
Measure the delay from the eoemb to the next LMFC edge.

## Instantiations

- i_rx_header: jesd204_rx_header
- i_crc12: jesd204_crc12
- i_error_monitor: error_monitor
- i_descrambler: jesd204_scrambler_64b
- i_pipeline_stage2: pipeline_stage
- i_elastic_buffer: elastic_buffer
