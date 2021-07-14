# Package: keymgr_pkg

## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This struct contains three fields:
 - valid
 - key_share0
 - key_share1
 share0 and share1 are only driven when `valid` is 1.
 

## Signals

| Name         | Type                     | Description                                                           |
| ------------ | ------------------------ | --------------------------------------------------------------------- |
| sideload_key | keymgr_pkg::hw_key_req_t | This struct contains three fields: - valid - key_share0 - key_share1  |
| path         | string                   |                                                                       |
