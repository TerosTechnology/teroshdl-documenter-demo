# Entity: tx_interrupt_selection

- **File**: tx_interrupt_selection.v
## Diagram

![Diagram](tx_interrupt_selection.svg "Diagram")
## Description

Xianjun jiao. putaoshu@msn.com; xianjun.jiao@imec.be;
 
## Ports

| Port name         | Direction | Type       | Description     |
| ----------------- | --------- | ---------- | --------------- |
| src_sel           | input     | wire [2:0] | selection       |
| s00_axis_tlast    | input     | wire       | src             |
| phy_tx_start      | input     | wire       |                 |
| tx_start_from_acc | input     | wire       |                 |
| tx_end_from_acc   | input     | wire       |                 |
| tx_try_complete   | input     | wire       |                 |
| tx_itrpt          | output    |            | to ps interrupt |
## Processes
- unnamed: ( @( src_sel, s00_axis_tlast,phy_tx_start, tx_start_from_acc, tx_end_from_acc,tx_try_complete) )
