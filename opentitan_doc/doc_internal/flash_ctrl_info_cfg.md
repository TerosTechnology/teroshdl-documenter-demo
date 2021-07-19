# Entity: flash_ctrl_info_cfg

- **File**: flash_ctrl_info_cfg.sv
## Diagram

![Diagram](flash_ctrl_info_cfg.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 Flash info page protection assignment
 This module takes into account seed pages and assigns privileges accordingly.
 
## Generics

| Generic name   | Type                       | Value | Description |
| -------------- | -------------------------- | ----- | ----------- |
| BankW          | logic [BankW-1:0]          | 0     |             |
| InfoTypesWidth | logic [InfoTypesWidth-1:0] | 0     |             |
## Ports

| Port name           | Direction | Type               | Description |
| ------------------- | --------- | ------------------ | ----------- |
| cfgs_i              | input     | [InfosPerBank-1:0] |             |
| creator_seed_priv_i | input     |                    |             |
| owner_seed_priv_i   | input     |                    |             |
| iso_flash_wr_en_i   | input     |                    |             |
| iso_flash_rd_en_i   | input     |                    |             |
| cfgs_o              | output    | [InfosPerBank-1:0] |             |
## Signals

| Name           | Type            | Description |
| -------------- | --------------- | ----------- |
| isolate_pg_cfg | info_page_cfg_t |             |
## Constants

| Name        | Type | Value                  | Description |
| ----------- | ---- | ---------------------- | ----------- |
| CfgBitWidth | int  | $bits(info_page_cfg_t) |             |
