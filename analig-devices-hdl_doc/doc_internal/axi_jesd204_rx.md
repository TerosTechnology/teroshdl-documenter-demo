# Entity: axi_jesd204_rx

- **File**: axi_jesd204_rx.v
## Diagram

![Diagram](axi_jesd204_rx.svg "Diagram")
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

| Generic name      | Type | Value                  | Description                |
| ----------------- | ---- | ---------------------- | -------------------------- |
| ID                |      | 0                      |                            |
| NUM_LANES         |      | 1                      |                            |
| NUM_LINKS         |      | 1                      |                            |
| LINK_MODE         |      | 1                      |  2 - 64B/66B;  1 - 8B/10B  |
| ENABLE_LINK_STATS |      | 0                      |                            |
| DATA_PATH_WIDTH   |      | LINK_MODE == 2 ? 8 : 4 |                            |
## Ports

| Port name                              | Direction | Type                              | Description |
| -------------------------------------- | --------- | --------------------------------- | ----------- |
| s_axi_aclk                             | input     |                                   |             |
| s_axi_aresetn                          | input     |                                   |             |
| s_axi_awvalid                          | input     |                                   |             |
| s_axi_awaddr                           | input     | [13:0]                            |             |
| s_axi_awready                          | output    |                                   |             |
| s_axi_awprot                           | input     | [2:0]                             |             |
| s_axi_wvalid                           | input     |                                   |             |
| s_axi_wdata                            | input     | [31:0]                            |             |
| s_axi_wstrb                            | input     | [3:0]                             |             |
| s_axi_wready                           | output    |                                   |             |
| s_axi_bvalid                           | output    |                                   |             |
| s_axi_bresp                            | output    | [1:0]                             |             |
| s_axi_bready                           | input     |                                   |             |
| s_axi_arvalid                          | input     |                                   |             |
| s_axi_araddr                           | input     | [13:0]                            |             |
| s_axi_arready                          | output    |                                   |             |
| s_axi_arprot                           | input     | [2:0]                             |             |
| s_axi_rvalid                           | output    |                                   |             |
| s_axi_rready                           | input     |                                   |             |
| s_axi_rresp                            | output    | [ 1:0]                            |             |
| s_axi_rdata                            | output    | [31:0]                            |             |
| irq                                    | output    |                                   |             |
| core_clk                               | input     |                                   |             |
| core_reset_ext                         | input     |                                   |             |
| core_reset                             | output    |                                   |             |
| device_clk                             | input     |                                   |             |
| device_reset                           | output    |                                   |             |
| core_cfg_lanes_disable                 | output    | [NUM_LANES-1:0]                   |             |
| core_cfg_links_disable                 | output    | [NUM_LINKS-1:0]                   |             |
| core_cfg_octets_per_multiframe         | output    | [9:0]                             |             |
| core_cfg_octets_per_frame              | output    | [7:0]                             |             |
| core_cfg_disable_scrambler             | output    |                                   |             |
| core_cfg_disable_char_replacement      | output    |                                   |             |
| core_cfg_frame_align_err_threshold     | output    | [7:0]                             |             |
| device_cfg_octets_per_multiframe       | output    | [9:0]                             |             |
| device_cfg_octets_per_frame            | output    | [7:0]                             |             |
| device_cfg_beats_per_multiframe        | output    | [7:0]                             |             |
| device_cfg_lmfc_offset                 | output    | [7:0]                             |             |
| device_cfg_sysref_oneshot              | output    |                                   |             |
| device_cfg_sysref_disable              | output    |                                   |             |
| device_cfg_buffer_early_release        | output    |                                   |             |
| device_cfg_buffer_delay                | output    | [7:0]                             |             |
| core_ilas_config_valid                 | input     | [NUM_LANES-1:0]                   |             |
| core_ilas_config_addr                  | input     | [2*NUM_LANES-1:0]                 |             |
| core_ilas_config_data                  | input     | [NUM_LANES*DATA_PATH_WIDTH*8-1:0] |             |
| device_event_sysref_alignment_error    | input     |                                   |             |
| device_event_sysref_edge               | input     |                                   |             |
| core_event_frame_alignment_error       | input     |                                   |             |
| core_event_unexpected_lane_state_error | input     |                                   |             |
| core_ctrl_err_statistics_mask          | output    | [6:0]                             |             |
| core_ctrl_err_statistics_reset         | output    |                                   |             |
| core_status_err_statistics_cnt         | input     | [32*NUM_LANES-1:0]                |             |
| core_status_ctrl_state                 | input     | [1:0]                             |             |
| core_status_lane_cgs_state             | input     | [2*NUM_LANES-1:0]                 |             |
| core_status_lane_emb_state             | input     | [3*NUM_LANES-1:0]                 |             |
| core_status_lane_ifs_ready             | input     | [NUM_LANES-1:0]                   |             |
| core_status_lane_latency               | input     | [14*NUM_LANES-1:0]                |             |
| core_status_lane_frame_align_err_cnt   | input     | [8*NUM_LANES-1:0]                 |             |
| status_synth_params0                   | input     | [31:0]                            |             |
| status_synth_params1                   | input     | [31:0]                            |             |
| status_synth_params2                   | input     | [31:0]                            |             |
## Signals

| Name                                 | Type        | Description                     |
| ------------------------------------ | ----------- | ------------------------------- |
| up_rdata                             | reg [31:0]  |  Register interface signals */  |
| up_wack                              | reg         |                                 |
| up_rack                              | reg         |                                 |
| up_rreq_d1                           | reg         |                                 |
| up_wreq                              | wire        |                                 |
| up_rreq                              | wire        |                                 |
| up_wdata                             | wire [31:0] |                                 |
| up_waddr                             | wire [11:0] |                                 |
| up_raddr                             | wire [11:0] |                                 |
| up_rdata_common                      | wire [31:0] |                                 |
| up_rdata_sysref                      | wire [31:0] |                                 |
| up_rdata_rx                          | wire [31:0] |                                 |
| up_irq_trigger                       | wire [4:0]  |                                 |
| up_cfg_is_writeable                  | wire        |                                 |
| up_cfg_sysref_oneshot                | wire        |                                 |
| up_cfg_sysref_disable                | wire        |                                 |
| up_cfg_buffer_early_release          | wire        |                                 |
| up_cfg_buffer_delay                  | wire [7:0]  |                                 |
| up_cfg_lmfc_offset                   | wire [7:0]  |                                 |
| up_cfg_frame_align_err_threshold     | wire [7:0]  |                                 |
| up_reset                             | wire        |                                 |
| up_reset_synchronizer                | wire        |                                 |
| up_event_frame_alignment_error       | wire        |                                 |
| up_event_unexpected_lane_state_error | wire        |                                 |
## Constants

| Name                 | Type | Value        | Description |
| -------------------- | ---- | ------------ | ----------- |
| PCORE_VERSION        |      | 32'h00010761 | 1.07.a      |
| PCORE_MAGIC          |      | 32'h32303452 | 204R        |
| DATA_PATH_WIDTH_LOG2 |      | 3            |             |
## Processes
- unnamed: ( @(posedge s_axi_aclk) )
  - **Type:** always
## Instantiations

- i_sync_frame_align_err: sync_event
- i_up_axi: up_axi
- i_up_common: jesd204_up_common
- i_up_sysref: jesd204_up_sysref
- i_up_rx: jesd204_up_rx
