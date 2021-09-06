# Entity: flash_mp_data_region_sel

- **File**: flash_mp_data_region_sel.sv
## Diagram

![Diagram](flash_mp_data_region_sel.svg "Diagram")
## Description

 Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0

 Flash Memory Properties


## Generics

| Generic name | Type | Value | Description |
| ------------ | ---- | ----- | ----------- |
| Regions      | int  | 4     |             |
## Ports

| Port name      | Direction | Type                | Description |
| -------------- | --------- | ------------------- | ----------- |
| req_i          | input     |                     |             |
| phase_i        | input     | flash_lcmgr_phase_e |             |
| addr_i         | input     | [AllPagesW-1:0]     |             |
| region_attrs_i | input     | data_region_attr_t  |             |
| sel_cfg_o      | output    | mp_region_cfg_t     |             |
## Signals

| Name         | Type                | Description                                                                                        |
| ------------ | ------------------- | -------------------------------------------------------------------------------------------------- |
| region_end   | logic [AllPagesW:0] |  There could be multiple region matches due to region overlap  Lower indices always have priority  |
| region_match | logic [Regions-1:0] |                                                                                                    |
| region_sel   | logic [Regions-1:0] |                                                                                                    |
## Processes
- unnamed: (  )
  - **Type:** always_comb
</br>**Description**
 check for region match 
- unnamed: (  )
  - **Type:** always_comb
</br>**Description**
 select appropriate region configuration 
