# Entity: otbn_tracer
## Diagram
![Diagram](otbn_tracer.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 
## Generics
| Generic name      | Type   | Value | Description                                                                               |
| ----------------- | ------ | ----- | ----------------------------------------------------------------------------------------- |
| InsnExecutePrefix | string | "E"   | Prefixes used in trace lines. Formats are documented in `hw/ip/otbn/dv/tracer/README.md`  |
| InsnStallPrefix   | string | "S"   |                                                                                           |
| RegReadPrefix     | string | "<"   |                                                                                           |
| RegWritePrefix    | string | ">"   |                                                                                           |
| MemWritePrefix    | string | "W"   |                                                                                           |
| MemReadPrefix     | string | "R"   |                                                                                           |
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
## Processes
- unnamed: _( @(posedge clk_i or negedge rst_ni) )_

