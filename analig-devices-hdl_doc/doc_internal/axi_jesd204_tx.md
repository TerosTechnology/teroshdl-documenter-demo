# Entity: axi_jesd204_tx

- **File**: axi_jesd204_tx.v
## Diagram

![Diagram](axi_jesd204_tx.svg "Diagram")
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

| Generic name      | Type | Value                  | Description              |
| ----------------- | ---- | ---------------------- | ------------------------ |
| ID                |      | 0                      |                          |
| NUM_LANES         |      | 1                      |                          |
| NUM_LINKS         |      | 1                      |                          |
| LINK_MODE         |      | 1                      | 2 - 64B/66B;  1 - 8B/10B |
| ENABLE_LINK_STATS |      | 0                      |                          |
| DATA_PATH_WIDTH   |      | LINK_MODE == 2 ? 8 : 4 |                          |
## Ports

| Port name                           | Direction | Type                              | Description |
| ----------------------------------- | --------- | --------------------------------- | ----------- |
| s_axi_aclk                          | input     |                                   |             |
| s_axi_aresetn                       | input     |                                   |             |
| s_axi_awvalid                       | input     |                                   |             |
| s_axi_awaddr                        | input     | [13:0]                            |             |
| s_axi_awready                       | output    |                                   |             |
| s_axi_awprot                        | input     | [2:0]                             |             |
| s_axi_wvalid                        | input     |                                   |             |
| s_axi_wdata                         | input     | [31:0]                            |             |
| s_axi_wstrb                         | input     | [3:0]                             |             |
| s_axi_wready                        | output    |                                   |             |
| s_axi_bvalid                        | output    |                                   |             |
| s_axi_bresp                         | output    | [1:0]                             |             |
| s_axi_bready                        | input     |                                   |             |
| s_axi_arvalid                       | input     |                                   |             |
| s_axi_araddr                        | input     | [13:0]                            |             |
| s_axi_arready                       | output    |                                   |             |
| s_axi_arprot                        | input     | [2:0]                             |             |
| s_axi_rvalid                        | output    |                                   |             |
| s_axi_rready                        | input     |                                   |             |
| s_axi_rresp                         | output    | [1:0]                             |             |
| s_axi_rdata                         | output    | [31:0]                            |             |
| irq                                 | output    |                                   |             |
| core_clk                            | input     |                                   |             |
| core_reset_ext                      | input     |                                   |             |
| core_reset                          | output    |                                   |             |
| device_clk                          | input     |                                   |             |
| device_reset                        | output    |                                   |             |
| core_cfg_lanes_disable              | output    | [NUM_LANES-1:0]                   |             |
| core_cfg_links_disable              | output    | [NUM_LINKS-1:0]                   |             |
| core_cfg_octets_per_multiframe      | output    | [9:0]                             |             |
| core_cfg_octets_per_frame           | output    | [7:0]                             |             |
| core_cfg_continuous_cgs             | output    |                                   |             |
| core_cfg_continuous_ilas            | output    |                                   |             |
| core_cfg_skip_ilas                  | output    |                                   |             |
| core_cfg_mframes_per_ilas           | output    | [7:0]                             |             |
| core_cfg_disable_char_replacement   | output    |                                   |             |
| core_cfg_disable_scrambler          | output    |                                   |             |
| device_cfg_octets_per_multiframe    | output    | [7:0]                             |             |
| device_cfg_octets_per_frame         | output    | [7:0]                             |             |
| device_cfg_beats_per_multiframe     | output    | [7:0]                             |             |
| device_cfg_lmfc_offset              | output    | [7:0]                             |             |
| device_cfg_sysref_oneshot           | output    |                                   |             |
| device_cfg_sysref_disable           | output    |                                   |             |
| core_ilas_config_rd                 | input     |                                   |             |
| core_ilas_config_addr               | input     | [1:0]                             |             |
| core_ilas_config_data               | output    | [DATA_PATH_WIDTH*8*NUM_LANES-1:0] |             |
| device_event_sysref_alignment_error | input     |                                   |             |
| device_event_sysref_edge            | input     |                                   |             |
| core_ctrl_manual_sync_request       | output    |                                   |             |
| core_status_state                   | input     | [1:0]                             |             |
| core_status_sync                    | input     | [NUM_LINKS-1:0]                   |             |
| status_synth_params0                | input     | [31:0]                            |             |
| status_synth_params1                | input     | [31:0]                            |             |
| status_synth_params2                | input     | [31:0]                            |             |
## Signals

| Name                    | Type        | Description                    |
| ----------------------- | ----------- | ------------------------------ |
| up_reset                | wire        |                                |
| up_rdata                | reg [31:0]  | Register interface signals */  |
| up_wack                 | reg         |                                |
| up_rack                 | reg         |                                |
| up_wreq                 | wire        |                                |
| up_rreq                 | wire        |                                |
| up_wdata                | wire [31:0] |                                |
| up_waddr                | wire [11:0] |                                |
| up_raddr                | wire [11:0] |                                |
| up_rdata_common         | wire [31:0] |                                |
| up_rdata_sysref         | wire [31:0] |                                |
| up_rdata_tx             | wire [31:0] |                                |
| up_cfg_skip_ilas        | wire        |                                |
| up_cfg_continuous_ilas  | wire        |                                |
| up_cfg_continuous_cgs   | wire        |                                |
| up_cfg_mframes_per_ilas | wire [7:0]  |                                |
| up_cfg_lmfc_offset      | wire [7:0]  |                                |
| up_cfg_sysref_oneshot   | wire        |                                |
| up_cfg_sysref_disable   | wire        |                                |
| up_cfg_is_writeable     | wire        |                                |
| up_irq_trigger          | wire [4:0]  |                                |
## Constants

| Name                 | Type | Value        | Description |
| -------------------- | ---- | ------------ | ----------- |
| PCORE_VERSION        |      | 32'h00010661 | 1.06.a      |
| PCORE_MAGIC          |      | 32'h32303454 | 204T        |
| DATA_PATH_WIDTH_LOG2 |      | 3            |             |
## Processes
- unnamed: ( @(posedge s_axi_aclk) )
## Instantiations

- i_up_axi: up_axi
- i_up_common: jesd204_up_common
- i_up_sysref: jesd204_up_sysref
- i_up_tx: jesd204_up_tx
