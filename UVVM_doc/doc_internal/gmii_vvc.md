# Entity: gmii_vvc
## Diagram
![Diagram](gmii_vvc.svg "Diagram")
## Generics
| Generic name                             | Type              | Value                     | Description |
| ---------------------------------------- | ----------------- | ------------------------- | ----------- |
| GC_INSTANCE_IDX                          | natural           |                           |             |
| GC_GMII_BFM_CONFIG                       | t_gmii_bfm_config | C_GMII_BFM_CONFIG_DEFAULT |             |
| GC_CMD_QUEUE_COUNT_MAX                   | natural           | 1000                      |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD             | natural           | 950                       |             |
| GC_CMD_QUEUE_COUNT_THRESHOLD_SEVERITY    | t_alert_level     | WARNING                   |             |
| GC_RESULT_QUEUE_COUNT_MAX                | natural           | 1000                      |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD          | natural           | 950                       |             |
| GC_RESULT_QUEUE_COUNT_THRESHOLD_SEVERITY | t_alert_level     | WARNING                   |             |
## Ports
| Port name      | Direction | Type         | Description |
| -------------- | --------- | ------------ | ----------- |
| gmii_vvc_tx_if | inout     | t_gmii_tx_if |             |
| gmii_vvc_rx_if | inout     | t_gmii_rx_if |             |
## Instantiations
- i_gmii_tx: work.gmii_tx_vvc
- i_gmii_rx: work.gmii_rx_vvc
