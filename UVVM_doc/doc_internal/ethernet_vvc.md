# Entity: ethernet_vvc
## Diagram
![Diagram](ethernet_vvc.svg "Diagram")
## Generics
| Generic name                             | Type                                  | Value                                         | Description |
| ---------------------------------------- | ------------------------------------- | --------------------------------------------- | ----------- |
| GC_INSTANCE_IDX                          | natural                               |                                               |             |
| GC_PHY_INTERFACE                         | t_interface                           |                                               |             |
| GC_PHY_VVC_INSTANCE_IDX                  | natural                               |                                               |             |
| GC_PHY_MAX_ACCESS_TIME                   | time                                  | 1 us                                          |             |
| GC_DUT_IF_FIELD_CONFIG                   | t_dut_if_field_config_direction_array | C_DUT_IF_FIELD_CONFIG_DIRECTION_ARRAY_DEFAULT |             |
| GC_ETHERNET_PROTOCOL_CONFIG              | t_ethernet_protocol_config            | C_ETHERNET_PROTOCOL_CONFIG_DEFAULT            |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural                               | 1000                                          |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural                               | 950                                           |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level                         | WARNING                                       |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural                               | 1000                                          |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural                               | 950                                           |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level                         | WARNING                                       |             |
## Instantiations
- i_ethernet_tx: work.ethernet_tx_vvc
- i_ethernet_rx: work.ethernet_rx_vvc
