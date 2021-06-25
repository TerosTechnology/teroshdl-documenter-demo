# Entity: prim_multibit_sync
## Diagram
![Diagram](prim_multibit_sync.svg "Diagram")
## Description
Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 WARNING: DO NOT USE THIS MODULE IF YOU DO NOT HAVE A GOOD REASON TO DO SO.
 This module is only meant to be used in special cases where a handshake synchronizer
 is not viable (this is for instance the case for the multibit life cycle signals).
 For handshake-based synchronization, consider using prim_sync_reqack_data.
 Description:
 This module implements a multibit synchronizer that employs a data consistency check to
 decide whether the synchronized multibit signal is stable and can be output or not.
 The number of consistency checkers can be controlled via NumChecks. Each check adds another
 delay register after the 2-flop synchronizer, and corresponding comparator that checks whether
 the register input is equal to the output of the last register in the chain. If all checks are
 successful, the output register is enabled such that the data can propagate to the output.
 This is illustrated bellow for NumChecks = 1:
                  /--------\        /--------\        /--------\
                  |        |        |        |        |        |
    data_i --/--> |  flop  | --x--> |  flop  | --x--> |  flop  | --/--> data_o
           Width  | 2 sync |   |    |        |   |    |        |
                  |        |   |    |        |   |    |   en   |
                  \--------/   |    \--------/   |    \--------/
                               |                 v        ^
                               |               /----\     |
                               \-------------> | == | ----/
                                               \----/
 Note: CDC tools will likely flag this module due to re-convergent logic.
 
## Generics
| Generic name | Type              | Value | Description                                                                                                                                                              |
| ------------ | ----------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Width        | int               | 8     | Width of the multibit signal.                                                                                                                                            |
| NumChecks    | int               | 1     | Number of cycles the synchronized multi-bit signal needs to be stable until it is relased to the output. Each check adds a comparator and an additional delay register.  |
| Width        | logic [Width-1:0] | '0    | Reset value of the multibit signal.                                                                                                                                      |
## Ports
| Port name | Direction | Type        | Description |
| --------- | --------- | ----------- | ----------- |
| clk_i     | input     |             |             |
| rst_ni    | input     |             |             |
| data_i    | input     | [Width-1:0] |             |
| data_o    | output    | [Width-1:0] |             |
## Signals
| Name          | Type                             | Description                                                            |
| ------------- | -------------------------------- | ---------------------------------------------------------------------- |
| data_check_d  | logic [NumChecks:0][Width-1:0]   | First, synchronize the input data to this clock domain.                |
| data_check_q  | logic [NumChecks-1:0][Width-1:0] |                                                                        |
| checks        | logic [NumChecks-1:0]            | Consistency check. Always compare to the output of the last register.  |
| data_synced_d | logic [Width-1:0]                | Only propagate to output register if all checks have passed.           |
| data_synced_q | logic [Width-1:0]                | Only propagate to output register if all checks have passed.           |
## Processes
- p_regs: _( @(posedge clk_i or negedge rst_ni) )_

## Instantiations
- i_prim_flop_2sync: prim_flop_2sync
