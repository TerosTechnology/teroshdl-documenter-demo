# Entity: hvvc_to_vvc_bridge
## Diagram
![Diagram](hvvc_to_vvc_bridge.svg "Diagram")
## Generics
| Generic name           | Type                                  | Value           | Description |
| ---------------------- | ------------------------------------- | --------------- | ----------- |
| GC_INSTANCE_IDX        | integer                               |                 |             |
| GC_DUT_IF_FIELD_CONFIG | t_dut_if_field_config_direction_array |                 |             |
| GC_MAX_NUM_WORDS       | positive                              |                 |             |
| GC_PHY_MAX_ACCESS_TIME | time                                  |                 |             |
| GC_SCOPE               | string                                |                 |             |
| GC_WORD_ENDIANNESS     | t_word_endianness                     | LOWER_WORD_LEFT |             |
## Ports
| Port name      | Direction | Type             | Description |
| -------------- | --------- | ---------------- | ----------- |
| hvvc_to_bridge | in        | t_hvvc_to_bridge |             |
| bridge_to_hvvc | out       | t_bridge_to_hvvc |             |
