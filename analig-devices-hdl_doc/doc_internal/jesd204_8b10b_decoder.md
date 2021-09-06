# Entity: jesd204_8b10b_decoder

- **File**: jesd204_8b10b_decoder.v
## Diagram

![Diagram](jesd204_8b10b_decoder.svg "Diagram")
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

| Port name      | Direction | Type  | Description |
| -------------- | --------- | ----- | ----------- |
| in_disparity   | input     |       |             |
| in_char        | input     | [9:0] |             |
| out_char       | output    | [7:0] |             |
| out_charisk    | output    |       |             |
| out_notintable | output    |       |             |
| out_disperr    | output    |       |             |
| out_disparity  | output    |       |             |
## Signals

| Name                 | Type      | Description                                                                                                                                      |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| data5b               | reg [4:0] |   * Only supports the subset of 8b10b that is used by JESD204.  * If non-supported control characters are supplied the output is undefined.  */  |
| notintable5b         | reg       |                                                                                                                                                  |
| disparity5b          | reg [1:0] |                                                                                                                                                  |
| ignore5b             | reg       |                                                                                                                                                  |
| data3b               | reg [2:0] |                                                                                                                                                  |
| notintable3b         | reg       |                                                                                                                                                  |
| disparity3b          | reg [1:0] |                                                                                                                                                  |
| ignore3b             | reg       |                                                                                                                                                  |
| total_disparity      | reg [1:0] |                                                                                                                                                  |
| notintable_disparity | reg       |                                                                                                                                                  |
| charisk              | wire      |  Only detect K28.X                                                                                                                               |
## Processes
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
- unnamed: ( @(*) )
  - **Type:** always
