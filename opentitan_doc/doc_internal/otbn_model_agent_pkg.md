# Package: otbn_model_agent_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Signals

| Name                 | Type       | Description |
| -------------------- | ---------- | ----------- |
| insn_addr            | bit [31:0] |             |
| output               | bit [31:0] |             |
| mnemonic             | string     |             |
| otbn_model_agent_pkg | endpackage |             |
## Types

| Name                   | Type                                                                                                                                                                            | Description                                                                                                                                                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| otbn_model_item_type_e | enum {<br><span style="padding-left:20px">     OtbnModelStart,<br><span style="padding-left:20px">     OtbnModelDone,<br><span style="padding-left:20px">     OtbnModelInsn   } |                                                                                                                                                                                                                                                    |
| otbn_model_item        | undefined                                                                                                                                                                       |                                                                                                                                                                                                                                                    |
| otbn_model_agent_cfg   | undefined                                                                                                                                                                       |                                                                                                                                                                                                                                                    |
| otbn_dummy_sequencer   | dv_base_sequencer #(otbn_model_item,<br><span style="padding-left:20px"> otbn_model_agent_cfg)                                                                                  | driver and sequencer are not used in this agent. Create these dummy components to avoid compile error due to the TLM connection between monitor and sequencer in dv_base_*. Both TLM fifo/port need to use the same item object (otbn_model_item)  |
| otbn_dummy_driver      | dv_base_driver #(otbn_model_item,<br><span style="padding-left:20px"> otbn_model_agent_cfg)                                                                                     |                                                                                                                                                                                                                                                    |
