# Package: prim_alert_pkg

- **File**: prim_alert_pkg.sv
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 

## Constants

| Name             | Type       | Value          | Description |
| ---------------- | ---------- | -------------- | ----------- |
| alert_tx_t       | alert_tx_t | undefined      |             |
| ALERT_RX_DEFAULT | alert_rx_t | prim_alert_pkg |             |
## Types

| Name       | Type                                                                                                                                                                                                                                                                          | Description |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| alert_tx_t | struct packed {<br><span style="padding-left:20px">     logic alert_p;<br><span style="padding-left:20px">     logic alert_n;<br><span style="padding-left:20px">   }                                                                                                         |             |
| alert_rx_t | struct packed {<br><span style="padding-left:20px">     logic ping_p;<br><span style="padding-left:20px">     logic ping_n;<br><span style="padding-left:20px">     logic ack_p;<br><span style="padding-left:20px">     logic ack_n;<br><span style="padding-left:20px">   } |             |
