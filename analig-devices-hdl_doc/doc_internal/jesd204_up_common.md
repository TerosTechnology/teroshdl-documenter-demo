# Entity: jesd204_up_common

- **File**: jesd204_up_common.v
## Diagram

![Diagram](jesd204_up_common.svg "Diagram")
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

| Generic name         | Type | Value | Description |
| -------------------- | ---- | ----- | ----------- |
| PCORE_VERSION        |      | 0     |             |
| PCORE_MAGIC          |      | 0     |             |
| ID                   |      | 0     |             |
| NUM_LANES            |      | 1     |             |
| NUM_LINKS            |      | 1     |             |
| DATA_PATH_WIDTH_LOG2 |      | 2     |             |
| NUM_IRQS             |      | 1     |             |
| EXTRA_CFG_WIDTH      |      | 1     |             |
| DEV_EXTRA_CFG_WIDTH  |      | 1     |             |
| ENABLE_LINK_STATS    |      | 0     |             |
## Ports

| Port name                         | Direction | Type                          | Description |
| --------------------------------- | --------- | ----------------------------- | ----------- |
| up_clk                            | input     |                               |             |
| ext_resetn                        | input     |                               |             |
| up_reset                          | output    |                               |             |
| up_reset_synchronizer             | output    |                               |             |
| core_clk                          | input     |                               |             |
| core_reset_ext                    | input     |                               |             |
| core_reset                        | output    |                               |             |
| device_clk                        | input     |                               |             |
| device_reset                      | output    |                               |             |
| up_raddr                          | input     | [11:0]                        |             |
| up_rdata                          | output    | [31:0]                        |             |
| up_wreq                           | input     |                               |             |
| up_waddr                          | input     | [11:0]                        |             |
| up_wdata                          | input     | [31:0]                        |             |
| up_extra_cfg                      | input     | [EXTRA_CFG_WIDTH-1:0]         |             |
| up_dev_extra_cfg                  | input     | [DEV_EXTRA_CFG_WIDTH-1:0]     |             |
| up_irq_trigger                    | input     | [NUM_IRQS-1:0]                |             |
| irq                               | output    |                               |             |
| up_cfg_is_writeable               | output    |                               |             |
| core_cfg_lanes_disable            | output    | [NUM_LANES-1:0]               |             |
| core_cfg_links_disable            | output    | [NUM_LINKS-1:0]               |             |
| core_cfg_octets_per_multiframe    | output    | reg [9:0]                     |             |
| core_cfg_octets_per_frame         | output    | reg [7:0]                     |             |
| core_cfg_disable_scrambler        | output    | reg                           |             |
| core_cfg_disable_char_replacement | output    | reg                           |             |
| core_extra_cfg                    | output    | reg [EXTRA_CFG_WIDTH-1:0]     |             |
| device_extra_cfg                  | output    | reg [DEV_EXTRA_CFG_WIDTH-1:0] |             |
| device_cfg_octets_per_multiframe  | output    | reg [9:0]                     |             |
| device_cfg_octets_per_frame       | output    | reg [7:0]                     |             |
| device_cfg_beats_per_multiframe   | output    | reg [7:0]                     |             |
| status_synth_params0              | input     | [31:0]                        |             |
| status_synth_params1              | input     | [31:0]                        |             |
| status_synth_params2              | input     | [31:0]                        |             |
## Signals

| Name                                  | Type                | Description                                                                                                                                                                                                |
| ------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| up_scratch                            | reg [31:0]          |                                                                                                                                                                                                            |
| up_cfg_octets_per_frame               | reg [7:0]           |                                                                                                                                                                                                            |
| up_cfg_octets_per_multiframe          | reg [9:0]           |                                                                                                                                                                                                            |
| up_cfg_beats_per_multiframe           | reg [7:0]           |                                                                                                                                                                                                            |
| up_cfg_lanes_disable                  | reg [NUM_LANES-1:0] |                                                                                                                                                                                                            |
| up_cfg_links_disable                  | reg [NUM_LINKS-1:0] |                                                                                                                                                                                                            |
| up_cfg_disable_char_replacement       | reg                 |                                                                                                                                                                                                            |
| up_cfg_disable_scrambler              | reg                 |                                                                                                                                                                                                            |
| up_reset_vector                       | reg [2:0]           |  Reset for the register map */                                                                                                                                                                             |
| core_reset_vector                     | reg [4:0]           |  Reset signal generation for the JESD core */                                                                                                                                                              |
| device_reset_vector                   | reg [4:0]           |                                                                                                                                                                                                            |
| up_reset_synchronizer_vector          | reg [1:0]           |  Transfer the reset signal back to the up domain, used to keep the  * synchronizers in reset until the core is ready. This is done in order to  * prevent bogus data to propagate to the register map. */  |
| up_core_reset_ext_synchronizer_vector | reg [1:0]           |   * Synchronize the external core reset to the register map domain so the status  * can be shown in the register map. This is useful for debugging.  */                                                    |
| up_core_reset_ext                     | wire                |                                                                                                                                                                                                            |
| core_cfg_transfer_en                  | wire                |  Transfer two cycles before the core comes out of reset */                                                                                                                                                 |
| device_cfg_transfer_en                | wire                |                                                                                                                                                                                                            |
| up_reset_core                         | reg                 |                                                                                                                                                                                                            |
| core_reset_all                        | wire                |                                                                                                                                                                                                            |
| up_irq_enable                         | reg [NUM_IRQS-1:0]  |  Interupt handling */                                                                                                                                                                                      |
| up_irq_source                         | reg [NUM_IRQS-1:0]  |                                                                                                                                                                                                            |
| up_irq_clear                          | reg [NUM_IRQS-1:0]  |                                                                                                                                                                                                            |
| up_irq_pending                        | wire [NUM_IRQS-1:0] |                                                                                                                                                                                                            |
| up_irq_event_cnt_bus                  | wire [8*16-1:0]     |  Count link enable */                                                                                                                                                                                      |
| up_link_enable_cnt_s                  | wire [15:0]         |                                                                                                                                                                                                            |
| clk_mon_count                         | wire [20:0]         |                                                                                                                                                                                                            |
| device_clk_mon_count                  | wire [20:0]         |                                                                                                                                                                                                            |
## Processes
- unnamed: ( @(posedge up_clk or negedge ext_resetn) )
  - **Type:** always
- unnamed: ( @(posedge core_clk or posedge core_reset_all) )
  - **Type:** always
- unnamed: ( @(posedge device_clk or posedge core_reset_all) )
  - **Type:** always
- unnamed: ( @(posedge up_clk or posedge core_reset) )
  - **Type:** always
- unnamed: ( @(posedge up_clk or posedge core_reset_ext) )
  - **Type:** always
- unnamed: ( @(posedge core_clk) )
  - **Type:** always
- unnamed: ( @(posedge device_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
</br>**Description**
 IRQ pending register is write-1-to-clear */ 
- unnamed: ( @(posedge up_clk) )
  - **Type:** always
## Instantiations

- i_clock_mon: up_clock_mon
- i_dev_clock_mon: up_clock_mon
