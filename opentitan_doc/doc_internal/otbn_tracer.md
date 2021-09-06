# Entity: otbn_tracer

- **File**: otbn_tracer.sv
## Diagram

![Diagram](otbn_tracer.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
*

## Generics

| Generic name      | Type   | Value | Description                                                                                |
| ----------------- | ------ | ----- | ------------------------------------------------------------------------------------------ |
| InsnExecutePrefix | string | "E"   |  Prefixes used in trace lines. Formats are documented in `hw/ip/otbn/dv/tracer/README.md`  |
| InsnStallPrefix   | string | "S"   |                                                                                            |
| RegReadPrefix     | string | "<"   |                                                                                            |
| RegWritePrefix    | string | ">"   |                                                                                            |
| MemWritePrefix    | string | "W"   |                                                                                            |
| MemReadPrefix     | string | "R"   |                                                                                            |
## Ports

| Port name  | Direction | Type          | Description |
| ---------- | --------- | ------------- | ----------- |
| clk_i      | input     |               |             |
| rst_ni     | input     |               |             |
| otbn_trace | input     | otbn_trace_if |             |
## Signals

| Name                | Type         | Description |
| ------------------- | ------------ | ----------- |
| trace_output_buffer | string       |             |
| cycle_count         | logic [31:0] |             |
| trace               | string       |             |
| int                 | string       |             |
| cycle_count         | unsigned     |             |
## Functions
- otbn_wlen_data_str <font id="function_arguments">(logic [WLEN-1:0])</font> <font id="function_return">return (string)</font>
</br>**Description**
 Given a WLEN size word output a hex string with the data split into 32-bit chunks separated
 with '_'. WLEN must be a multiple of 32.

- otbn_dmem_write_str <font id="function_arguments">(logic [31:0] add)</font> <font id="function_return">return (string)</font>
</br>**Description**
 Produce trace output string for dmem writes. For a 256-bit write, the address and full data is
 output. For 32-bit writes (determined by looking at the mask) only the relevant 32-bit chunk is
 output along with the address modified so it refers to that chunk.

- otbn_ispr_name_str <font id="function_arguments">(ispr_e)</font> <font id="function_return">return (string)</font>
</br>**Description**
 Determine name for an ISPR

- otbn_flags_str <font id="function_arguments">(flags_t)</font> <font id="function_return">return (string)</font>
</br>**Description**
 Format flag information into a string

- output_trace <font id="function_arguments">(string prefix,<br><span style="padding-left:20px"> string trace_line)</font> <font id="function_return">return (void)</font>
</br>**Description**
 Called by other trace functions to append their trace lines to the output buffer

- trace_base_rf <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- trace_bignum_rf <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- trace_bignum_mem <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- trace_ispr_accesses <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- trace_insn <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
- do_trace <font id="function_arguments">()</font> <font id="function_return">return (void)</font>
## Processes
- unnamed: ( @(posedge clk_i or negedge rst_ni) )
  - **Type:** always
