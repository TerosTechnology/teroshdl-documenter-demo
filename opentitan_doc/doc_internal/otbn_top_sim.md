# Entity: otbn_top_sim
## Diagram
![Diagram](otbn_top_sim.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics
| Generic name  | Type | Value                        | Description                                 |
| ------------- | ---- | ---------------------------- | ------------------------------------------- |
| ImemSizeByte  | int  | otbn_reg_pkg::OTBN_IMEM_SIZE | Size of the instruction memory, in bytes    |
| DmemSizeByte  | int  | otbn_reg_pkg::OTBN_DMEM_SIZE | Size of the data memory, in bytes           |
| ImemStartAddr | int  | 32'h0                        | Start address of first instruction in IMem  |
## Ports
| Port name | Direction | Type | Description |
| --------- | --------- | ---- | ----------- |
| IO_CLK    | input     |      |             |
| IO_RST_N  | input     |      |             |
## Signals
| Name                      | Type                                     | Description                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| otbn_done_d               | logic                                    |                                                                                                                                                                                                  |
| otbn_done_q               | logic                                    |                                                                                                                                                                                                  |
| otbn_err_bits_d           | err_bits_t                               |                                                                                                                                                                                                  |
| otbn_err_bits_q           | err_bits_t                               |                                                                                                                                                                                                  |
| otbn_start                | logic                                    |                                                                                                                                                                                                  |
| otbn_start_done           | logic                                    | Intialise otbn_start_done to 1 so that we only signal otbn_start after we have seen a reset. If you don't do this, we start OTBN before the reset, which can generate confusing trace messages.  |
| imem_req                  | logic                                    | Instruction memory (IMEM) signals                                                                                                                                                                |
| imem_addr                 | logic [ImemAddrWidth-1:0]                |                                                                                                                                                                                                  |
| imem_rdata                | logic [38:0]                             |                                                                                                                                                                                                  |
| imem_rvalid               | logic                                    |                                                                                                                                                                                                  |
| imem_rerror               | logic                                    |                                                                                                                                                                                                  |
| dmem_req                  | logic                                    | Data memory (DMEM) signals                                                                                                                                                                       |
| dmem_write                | logic                                    |                                                                                                                                                                                                  |
| dmem_addr                 | logic [DmemAddrWidth-1:0]                |                                                                                                                                                                                                  |
| dmem_wdata                | logic [ExtWLEN-1:0]                      |                                                                                                                                                                                                  |
| dmem_wmask                | logic [ExtWLEN-1:0]                      |                                                                                                                                                                                                  |
| dmem_rdata                | logic [ExtWLEN-1:0]                      |                                                                                                                                                                                                  |
| dmem_rvalid               | logic                                    |                                                                                                                                                                                                  |
| dmem_rerror               | logic                                    |                                                                                                                                                                                                  |
| edn_rnd_req               | logic                                    | Entropy Distribution Network (EDN)                                                                                                                                                               |
| edn_urnd_req              | logic                                    | Entropy Distribution Network (EDN)                                                                                                                                                               |
| edn_rnd_ack               | logic                                    |                                                                                                                                                                                                  |
| edn_urnd_ack              | logic                                    |                                                                                                                                                                                                  |
| edn_rnd_data              | logic [EdnDataWidth-1:0]                 |                                                                                                                                                                                                  |
| edn_urnd_data             | logic [EdnDataWidth-1:0]                 |                                                                                                                                                                                                  |
| edn_rnd_data_valid        | logic                                    |                                                                                                                                                                                                  |
| edn_urnd_data_valid       | logic                                    |                                                                                                                                                                                                  |
| insn_cnt                  | logic [31:0]                             | Instruction counter (feeds into otbn.INSN_CNT in full block)                                                                                                                                     |
| unused_imem_top_rdata     | logic                                    | The top bits of IMEM rdata aren't currently used (they will eventually be used for integrity checks both on the bus and within the core)                                                         |
| dmem_index                | logic [DmemIndexWidth-1:0]               |                                                                                                                                                                                                  |
| unused_dmem_addr          | logic [DmemAddrWidth-DmemIndexWidth-1:0] |                                                                                                                                                                                                  |
| imem_index                | logic [ImemIndexWidth-1:0]               |                                                                                                                                                                                                  |
| unused_imem_addr          | logic [1:0]                              |                                                                                                                                                                                                  |
| finish_counter            | logic [1:0]                              | When OTBN is done let a few more cycles run then finish simulation                                                                                                                               |
| otbn_model_done           | logic                                    |                                                                                                                                                                                                  |
| otbn_model_err_bits       | err_bits_t                               |                                                                                                                                                                                                  |
| otbn_model_insn_cnt       | bit [31:0]                               |                                                                                                                                                                                                  |
| otbn_model_err            | bit                                      |                                                                                                                                                                                                  |
| done_mismatch_latched     | bit                                      |                                                                                                                                                                                                  |
| err_bits_mismatch_latched | bit                                      |                                                                                                                                                                                                  |
| cnt_mismatch_latched      | bit                                      |                                                                                                                                                                                                  |
| model_err_latched         | bit                                      |                                                                                                                                                                                                  |
## Constants
| Name              | Type             | Value                                                                 | Description                                                                               |
| ----------------- | ---------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| ImemAddrWidth     | int              | prim_util_pkg::vbits(ImemSizeByte)                                    |                                                                                           |
| DmemAddrWidth     | int              | prim_util_pkg::vbits(DmemSizeByte)                                    |                                                                                           |
| TestScrambleKey   | logic [127:0]    | 128'h48ecf6c738f0f108a5b08620695ffd4d                                 | Fixed key and nonce for scrambling in verilator environment                               |
| TestScrambleNonce | logic [319:0]    | 320'h19286173144131c12c2607f5e72aca1fb72adea0a4ff82b9f88c2578fa4cd123 | 320-bit nonce has 0s in top bits as nonce from OTP is only 256-bit for now                |
| FixedEdnVal       | logic [WLEN-1:0] | undefined                                                             |                                                                                           |
| DmemSizeWords     | int              | DmemSizeByte                                                          |                                                                                           |
| DmemIndexWidth    | int              | prim_util_pkg::vbits(DmemSizeWords)                                   |                                                                                           |
| ImemSizeWords     | int              | ImemSizeByte / 4                                                      |                                                                                           |
| ImemIndexWidth    | int              | prim_util_pkg::vbits(ImemSizeWords)                                   |                                                                                           |
| DesignScope       | string           | "..u_otbn_core"                                                       | This runs in parallel with the real core above, with consistency checks between the two.  |
## Processes
- unnamed: _( @(posedge IO_CLK or negedge IO_RST_N) )_

- unnamed: _( @(posedge IO_CLK or negedge IO_RST_N) )_

- unnamed: _( @(posedge IO_CLK or negedge IO_RST_N) )_

## Instantiations
- u_otbn_core: otbn_core
- u_mock_rnd_edn: otbn_mock_edn
- u_mock_urnd_edn: otbn_mock_edn
- u_dmem: prim_ram_1p_scr
- u_imem: prim_ram_1p_scr
- u_otbn_core_model: otbn_core_model
