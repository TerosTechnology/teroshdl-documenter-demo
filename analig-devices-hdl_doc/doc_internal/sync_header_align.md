# Entity: sync_header_align

- **File**: sync_header_align.v
## Diagram

![Diagram](sync_header_align.svg "Diagram")
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
 The design and implementation of the JESD204 HDL Core used in this project
 is copyright © 2016-2017, Analog Devices, Inc.


## Ports

| Port name    | Direction | Type   | Description |
| ------------ | --------- | ------ | ----------- |
| clk          | input     |        |             |
| reset        | input     |        |             |
| i_data       | input     | [65:0] |             |
| i_slip       | output    |        |             |
| i_slip_done  | input     |        |             |
| o_data       | output    | [63:0] |             |
| o_header     | output    | [1:0]  |             |
| o_block_sync | output    |        |             |
## Signals

| Name         | Type                          | Description |
| ------------ | ----------------------------- | ----------- |
| state        | reg [2:0]                     |             |
| next_state   | reg [2:0]                     |             |
| header_vcnt  | reg [7:0]                     |             |
| header_icnt  | reg [LOG2_RX_THRESH_SH_ERR:0] |             |
| valid_header | wire                          |             |
## Constants

| Name                  | Type | Value                    | Description                |
| --------------------- | ---- | ------------------------ | -------------------------- |
| STATE_SH_HUNT         |      | 3'b001                   |  TODO : Add alignment FSM  |
| STATE_SH_SLIP         |      | 3'b010                   |                            |
| STATE_SH_LOCK         |      | 3'b100                   |                            |
| BIT_SH_HUNT           |      | 0                        |                            |
| BIT_SH_SLIP           |      | 1                        |                            |
| BIT_SH_LOCK           |      | 2                        |                            |
| RX_THRESH_SH_ERR      |      | 16                       |                            |
| LOG2_RX_THRESH_SH_ERR |      | $clog2(RX_THRESH_SH_ERR) |                            |
## Processes
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(posedge clk) )
  - **Type:** always
