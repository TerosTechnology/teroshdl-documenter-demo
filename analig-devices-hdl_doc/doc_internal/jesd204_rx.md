# Entity: jesd204_rx

- **File**: jesd204_rx.v
## Diagram

![Diagram](jesd204_rx.svg "Diagram")
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

| Generic name                 | Type | Value                  | Description                                                     |
| ---------------------------- | ---- | ---------------------- | --------------------------------------------------------------- |
| NUM_LANES                    |      | 1                      |                                                                 |
| NUM_LINKS                    |      | 1                      |                                                                 |
| NUM_INPUT_PIPELINE           |      | 1                      |                                                                 |
| NUM_OUTPUT_PIPELINE          |      | 1                      |                                                                 |
| LINK_MODE                    |      | 1                      |  2 - 64B/66B;  1 - 8B/10B                                       |
| DATA_PATH_WIDTH              |      | LINK_MODE == 2 ? 8 : 4 |  Only 4 is supported at the moment for 8b/10b and 8 for 64b */  |
| ENABLE_FRAME_ALIGN_CHECK     |      | 1                      |                                                                 |
| ENABLE_FRAME_ALIGN_ERR_RESET |      | 0                      |                                                                 |
| ENABLE_CHAR_REPLACE          |      | 0                      |                                                                 |
| ASYNC_CLK                    |      | 1                      |                                                                 |
| TPL_DATA_PATH_WIDTH          |      | LINK_MODE == 2 ? 8 : 4 |                                                                 |
## Ports

| Port name                           | Direction | Type                                  | Description                                                    |
| ----------------------------------- | --------- | ------------------------------------- | -------------------------------------------------------------- |
| clk                                 | input     |                                       | Link clock, lane rate / 40 or lane rate / 20 or lane rate / 66 |
| reset                               | input     |                                       |                                                                |
| device_clk                          | input     |                                       | Integer multiple of frame clock                                |
| device_reset                        | input     |                                       |                                                                |
| phy_data                            | input     | [DATA_PATH_WIDTH*8*NUM_LANES-1:0]     |                                                                |
| phy_header                          | input     | [2*NUM_LANES-1:0]                     |                                                                |
| phy_charisk                         | input     | [DATA_PATH_WIDTH*NUM_LANES-1:0]       |                                                                |
| phy_notintable                      | input     | [DATA_PATH_WIDTH*NUM_LANES-1:0]       |                                                                |
| phy_disperr                         | input     | [DATA_PATH_WIDTH*NUM_LANES-1:0]       |                                                                |
| phy_block_sync                      | input     | [NUM_LANES-1:0]                       |                                                                |
| sysref                              | input     |                                       |                                                                |
| lmfc_edge                           | output    |                                       |                                                                |
| lmfc_clk                            | output    |                                       |                                                                |
| device_event_sysref_alignment_error | output    |                                       |                                                                |
| device_event_sysref_edge            | output    |                                       |                                                                |
| event_frame_alignment_error         | output    |                                       |                                                                |
| event_unexpected_lane_state_error   | output    |                                       |                                                                |
| sync                                | output    | [NUM_LINKS-1:0]                       |                                                                |
| phy_en_char_align                   | output    |                                       |                                                                |
| rx_data                             | output    | [TPL_DATA_PATH_WIDTH*8*NUM_LANES-1:0] |                                                                |
| rx_valid                            | output    |                                       |                                                                |
| rx_eof                              | output    | [TPL_DATA_PATH_WIDTH-1:0]             |                                                                |
| rx_sof                              | output    | [TPL_DATA_PATH_WIDTH-1:0]             |                                                                |
| rx_eomf                             | output    | [TPL_DATA_PATH_WIDTH-1:0]             |                                                                |
| rx_somf                             | output    | [TPL_DATA_PATH_WIDTH-1:0]             |                                                                |
| cfg_lanes_disable                   | input     | [NUM_LANES-1:0]                       |                                                                |
| cfg_links_disable                   | input     | [NUM_LINKS-1:0]                       |                                                                |
| cfg_octets_per_multiframe           | input     | [9:0]                                 |                                                                |
| cfg_octets_per_frame                | input     | [7:0]                                 |                                                                |
| cfg_disable_scrambler               | input     |                                       |                                                                |
| cfg_disable_char_replacement        | input     |                                       |                                                                |
| cfg_frame_align_err_threshold       | input     | [7:0]                                 |                                                                |
| device_cfg_octets_per_multiframe    | input     | [9:0]                                 |                                                                |
| device_cfg_octets_per_frame         | input     | [7:0]                                 |                                                                |
| device_cfg_beats_per_multiframe     | input     | [7:0]                                 |                                                                |
| device_cfg_lmfc_offset              | input     | [7:0]                                 |                                                                |
| device_cfg_sysref_oneshot           | input     |                                       |                                                                |
| device_cfg_sysref_disable           | input     |                                       |                                                                |
| device_cfg_buffer_early_release     | input     |                                       |                                                                |
| device_cfg_buffer_delay             | input     | [7:0]                                 |                                                                |
| ctrl_err_statistics_reset           | input     |                                       |                                                                |
| ctrl_err_statistics_mask            | input     | [6:0]                                 |                                                                |
| status_err_statistics_cnt           | output    | [32*NUM_LANES-1:0]                    |                                                                |
| ilas_config_valid                   | output    | [NUM_LANES-1:0]                       |                                                                |
| ilas_config_addr                    | output    | [NUM_LANES*2-1:0]                     |                                                                |
| ilas_config_data                    | output    | [NUM_LANES*DATA_PATH_WIDTH*8-1:0]     |                                                                |
| status_ctrl_state                   | output    | [1:0]                                 |                                                                |
| status_lane_cgs_state               | output    | [2*NUM_LANES-1:0]                     |                                                                |
| status_lane_ifs_ready               | output    | [NUM_LANES-1:0]                       |                                                                |
| status_lane_latency                 | output    | [14*NUM_LANES-1:0]                    |                                                                |
| status_lane_emb_state               | output    | [3*NUM_LANES-1:0]                     |                                                                |
| status_lane_frame_align_err_cnt     | output    | [8*NUM_LANES-1:0]                     |                                                                |
| status_synth_params0                | output    | [31:0]                                |                                                                |
| status_synth_params1                | output    | [31:0]                                |                                                                |
| status_synth_params2                | output    | [31:0]                                |                                                                |
## Signals

| Name                                 | Type                   | Description |
| ------------------------------------ | ---------------------- | ----------- |
| cfg_beats_per_multiframe             | wire [7:0]             |             |
| device_cfg_beats_per_multiframe_s    | wire [7:0]             |             |
| cgs_reset                            | wire [NUM_LANES-1:0]   |             |
| cgs_ready                            | wire [NUM_LANES-1:0]   |             |
| ifs_reset                            | wire [NUM_LANES-1:0]   |             |
| buffer_release_n                     | reg                    |             |
| buffer_release_d1                    | reg                    |             |
| buffer_ready_n                       | wire [NUM_LANES-1:0]   |             |
| all_buffer_ready_n                   | wire                   |             |
| dev_all_buffer_ready_n               | wire                   |             |
| eof_reset                            | reg                    |             |
| phy_data_r                           | wire [DW-1:0]          |             |
| phy_header_r                         | wire [HW-1:0]          |             |
| phy_charisk_r                        | wire [CW-1:0]          |             |
| phy_notintable_r                     | wire [CW-1:0]          |             |
| phy_disperr_r                        | wire [CW-1:0]          |             |
| phy_block_sync_r                     | wire [NUM_LANES-1:0]   |             |
| rx_data_s                            | wire [ODW-1:0]         |             |
| rx_valid_s                           | wire                   |             |
| lmfc_counter                         | wire [7:0]             |             |
| latency_monitor_reset                | wire                   |             |
| frame_align                          | wire [3*NUM_LANES-1:0] |             |
| ifs_ready                            | wire [NUM_LANES-1:0]   |             |
| event_data_phase                     | wire                   |             |
| err_statistics_reset                 | wire                   |             |
| lmfc_edge_synced                     | wire                   |             |
| frame_align_err_thresh_met           | reg [NUM_LANES-1:0]    |             |
| event_frame_alignment_error_per_lane | reg [NUM_LANES-1:0]    |             |
| buffer_release_opportunity           | reg                    |             |
## Constants

| Name                      | Type | Value                                                   | Description                                                                                                                       |
| ------------------------- | ---- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| CHAR_INFO_REGISTERED      |      | 0                                                       |   * Can be used to enable additional pipeline stages to ease timing. Usually not  * necessary.  */                                |
| ALIGN_MUX_REGISTERED      |      | 1                                                       |                                                                                                                                   |
| SCRAMBLER_REGISTERED      |      | 0                                                       |                                                                                                                                   |
| MAX_OCTETS_PER_FRAME      |      | 32                                                      |   * Maximum number of octets per multiframe for ADI JESD204 DACs is 256 (Adjust  * as necessary). Divide by data path width.  */  |
| MAX_OCTETS_PER_MULTIFRAME |      | 1024                                                    |                                                                                                                                   |
| MAX_BEATS_PER_MULTIFRAME  |      | MAX_OCTETS_PER_MULTIFRAME / DATA_PATH_WIDTH             |                                                                                                                                   |
| ELASTIC_BUFFER_SIZE       |      | MAX_BEATS_PER_MULTIFRAME                                |                                                                                                                                   |
| DPW_LOG2                  |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |                                                                                                                                   |
| LMFC_COUNTER_WIDTH        |      | MAX_BE                                                  |                                                                                                                                   |
| DW                        |      | 8*DATA_PATH_WIDTH*NUM_LANES                             |  Helper for common expressions */                                                                                                 |
| ODW                       |      | 8*TPL_DATA_PATH_WIDTH*NUM_LANES                         |                                                                                                                                   |
| CW                        |      | DATA_PATH_WIDTH*NUM_LANES                               |                                                                                                                                   |
| HW                        |      | 2*NUM_LANES                                             |                                                                                                                                   |
## Processes
- unnamed: ( @(posedge device_clk) )
  - **Type:** always
- unnamed: ( @(posedge device_clk) )
  - **Type:** always
## Instantiations

- i_all_buffer_ready_cdc: sync_bits
- i_input_pipeline_stage: pipeline_stage
- i_output_pipeline_stage: pipeline_stage
- i_lmfc: jesd204_lmfc
- i_frame_mark: jesd204_frame_mark
