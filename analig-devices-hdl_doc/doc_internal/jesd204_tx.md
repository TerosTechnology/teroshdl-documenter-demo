# Entity: jesd204_tx

- **File**: jesd204_tx.v
## Diagram

![Diagram](jesd204_tx.svg "Diagram")
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

| Generic name        | Type | Value                | Description                                                    |
| ------------------- | ---- | -------------------- | -------------------------------------------------------------- |
| NUM_LANES           |      | 1                    |                                                                |
| NUM_LINKS           |      | 1                    |                                                                |
| NUM_OUTPUT_PIPELINE |      | 0                    |                                                                |
| LINK_MODE           |      | 1                    | 2 - 64B/66B;  1 - 8B/10B                                       |
| DATA_PATH_WIDTH     |      | LINK_MODE[1] ? 8 : 4 | Only 4 is supported at the moment for 8b/10b and 8 for 64b */  |
| TPL_DATA_PATH_WIDTH |      | LINK_MODE[1] ? 8 : 4 |                                                                |
| ENABLE_CHAR_REPLACE |      | 1'b0                 |                                                                |
| ASYNC_CLK           |      | 1                    |                                                                |
## Ports

| Port name                           | Direction | Type                                  | Description |
| ----------------------------------- | --------- | ------------------------------------- | ----------- |
| clk                                 | input     |                                       |             |
| reset                               | input     |                                       |             |
| device_clk                          | input     |                                       |             |
| device_reset                        | input     |                                       |             |
| phy_data                            | output    | [DATA_PATH_WIDTH*8*NUM_LANES-1:0]     |             |
| phy_charisk                         | output    | [DATA_PATH_WIDTH*NUM_LANES-1:0]       |             |
| phy_header                          | output    | [2*NUM_LANES-1:0]                     |             |
| sysref                              | input     |                                       |             |
| lmfc_edge                           | output    |                                       |             |
| lmfc_clk                            | output    |                                       |             |
| sync                                | input     | [NUM_LINKS-1:0]                       |             |
| tx_data                             | input     | [TPL_DATA_PATH_WIDTH*8*NUM_LANES-1:0] |             |
| tx_ready                            | output    |                                       |             |
| tx_eof                              | output    | [TPL_DATA_PATH_WIDTH-1:0]             |             |
| tx_sof                              | output    | [TPL_DATA_PATH_WIDTH-1:0]             |             |
| tx_somf                             | output    | [TPL_DATA_PATH_WIDTH-1:0]             |             |
| tx_eomf                             | output    | [TPL_DATA_PATH_WIDTH-1:0]             |             |
| tx_valid                            | input     |                                       |             |
| cfg_lanes_disable                   | input     | [NUM_LANES-1:0]                       |             |
| cfg_links_disable                   | input     | [NUM_LINKS-1:0]                       |             |
| cfg_octets_per_multiframe           | input     | [9:0]                                 |             |
| cfg_octets_per_frame                | input     | [7:0]                                 |             |
| cfg_continuous_cgs                  | input     |                                       |             |
| cfg_continuous_ilas                 | input     |                                       |             |
| cfg_skip_ilas                       | input     |                                       |             |
| cfg_mframes_per_ilas                | input     | [7:0]                                 |             |
| cfg_disable_char_replacement        | input     |                                       |             |
| cfg_disable_scrambler               | input     |                                       |             |
| device_cfg_octets_per_multiframe    | input     | [9:0]                                 |             |
| device_cfg_octets_per_frame         | input     | [7:0]                                 |             |
| device_cfg_beats_per_multiframe     | input     | [7:0]                                 |             |
| device_cfg_lmfc_offset              | input     | [7:0]                                 |             |
| device_cfg_sysref_oneshot           | input     |                                       |             |
| device_cfg_sysref_disable           | input     |                                       |             |
| ilas_config_rd                      | output    |                                       |             |
| ilas_config_addr                    | output    | [1:0]                                 |             |
| ilas_config_data                    | input     | [NUM_LANES*DATA_PATH_WIDTH*8-1:0]     |             |
| ctrl_manual_sync_request            | input     |                                       |             |
| device_event_sysref_edge            | output    |                                       |             |
| device_event_sysref_alignment_error | output    |                                       |             |
| status_sync                         | output    | [NUM_LINKS-1:0]                       |             |
| status_state                        | output    | [1:0]                                 |             |
| status_synth_params0                | output    | [31:0]                                |             |
| status_synth_params1                | output    | [31:0]                                |             |
| status_synth_params2                | output    | [31:0]                                |             |
## Signals

| Name                              | Type                                   | Description |
| --------------------------------- | -------------------------------------- | ----------- |
| phy_data_r                        | wire [DW-1:0]                          |             |
| phy_charisk_r                     | wire [CW-1:0]                          |             |
| phy_header_r                      | wire [HW-1:0]                          |             |
| eof_gen_reset                     | wire                                   |             |
| tx_ready_64b_next                 | wire                                   |             |
| tx_ready_64b                      | reg                                    |             |
| frame_mark_reset                  | wire                                   |             |
| tx_sof_fm                         | wire [DATA_PATH_WIDTH-1:0]             |             |
| tx_eof_fm                         | wire [DATA_PATH_WIDTH-1:0]             |             |
| tx_somf_fm                        | wire [DATA_PATH_WIDTH-1:0]             |             |
| tx_eomf_fm                        | wire [DATA_PATH_WIDTH-1:0]             |             |
| tx_sof_fm_d1                      | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_eof_fm_d1                      | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_somf_fm_d1                     | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_eomf_fm_d1                     | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_sof_fm_d2                      | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_eof_fm_d2                      | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_somf_fm_d2                     | reg [DATA_PATH_WIDTH-1:0]              |             |
| tx_eomf_fm_d2                     | reg [DATA_PATH_WIDTH-1:0]              |             |
| lmfc_edge_synced                  | wire                                   |             |
| lmc_edge                          | wire                                   |             |
| lmc_quarter_edge                  | wire                                   |             |
| eoemb                             | wire                                   |             |
| gearbox_data                      | wire [DATA_PATH_WIDTH*8*NUM_LANES-1:0] |             |
| tx_ready_nx                       | wire                                   |             |
| link_lmfc_edge                    | wire                                   |             |
| link_lmfc_clk                     | wire                                   |             |
| device_lmfc_edge                  | wire                                   |             |
| device_lmfc_clk                   | wire                                   |             |
| device_lmc_edge                   | wire                                   |             |
| device_lmc_quarter_edge           | wire                                   |             |
| device_eoemb                      | wire                                   |             |
| tx_next_mf_ready                  | wire                                   |             |
| link_tx_ready                     | wire                                   |             |
| cfg_beats_per_multiframe          | wire [7:0]                             |             |
| device_cfg_beats_per_multiframe_s | wire [7:0]                             |             |
## Constants

| Name                      | Type | Value                                                   | Description |
| ------------------------- | ---- | ------------------------------------------------------- | ----------- |
| MAX_OCTETS_PER_FRAME      |      | 32                                                      |             |
| MAX_OCTETS_PER_MULTIFRAME |      | 1024                                                    |             |
| MAX_BEATS_PER_MULTIFRAME  |      | MAX_OCTETS_PER_MULTIFRAME / DATA_PATH_WIDTH             |             |
| DPW_LOG2                  |      | DATA_PATH_WIDTH == 8 ? 3 : DATA_PATH_WIDTH == 4 ? 2 : 1 |             |
| LMFC_COUNTER_WIDTH        |      | MAX_BE                                                  |             |
| DW                        |      | DATA_PATH_WIDTH * 8 * NUM_LANES                         |             |
| CW                        |      | DATA_PATH_WIDTH * NUM_LANES                             |             |
| HW                        |      | 2 * NUM_LANES                                           |             |
## Processes
- unnamed: ( @(posedge clk) )
## Instantiations

- i_lmfc: jesd204_lmfc
- i_frame_mark: jesd204_frame_mark
- i_output_pipeline_stage: pipeline_stage
