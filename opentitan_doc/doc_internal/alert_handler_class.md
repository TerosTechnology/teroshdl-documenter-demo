# Entity: alert_handler_class

- **File**: alert_handler_class.sv
## Diagram

![Diagram](alert_handler_class.svg "Diagram")
## Description

Copyright lowRISC contributors.
 Licensed under the Apache License, Version 2.0, see LICENSE for details.
 SPDX-License-Identifier: Apache-2.0
 This module gates the alert triggers with their enable bits, and correctly bins
 the enabled alerts into the class that they have been assigned to. The module
 produces the alert cause and class trigger signals.
 
## Ports

| Port name         | Direction | Type                            | Description      |
| ----------------- | --------- | ------------------------------- | ---------------- |
| alert_trig_i      | input     | [NAlerts-1:0]                   | alert trigger    |
| loc_alert_trig_i  | input     | [N_LOC_ALERT-1:0]               | alert trigger    |
| alert_en_i        | input     | [NAlerts-1:0]                   | alert enable     |
| loc_alert_en_i    | input     | [N_LOC_ALERT-1:0]               | alert enable     |
| alert_class_i     | input     | [NAlerts-1:0]    [CLASS_DW-1:0] | class assignment |
| loc_alert_class_i | input     | [N_LOC_ALERT-1:0][CLASS_DW-1:0] | class assignment |
| alert_cause_o     | output    | [NAlerts-1:0]                   | alert cause      |
| loc_alert_cause_o | output    | [N_LOC_ALERT-1:0]               | alert cause      |
| class_trig_o      | output    | [N_CLASSES-1:0]                 | class triggered  |
## Signals

| Name            | Type                                   | Description             |
| --------------- | -------------------------------------- | ----------------------- |
| class_masks     | logic [N_CLASSES-1:0][NAlerts-1:0]     | classification mapping  |
| loc_class_masks | logic [N_CLASSES-1:0][N_LOC_ALERT-1:0] |                         |
## Processes
- p_class_mask: (  )
**Description**
this is basically an address to onehot0 decoder

