# Entity: ei_demo_tb
## Diagram
![Diagram](ei_demo_tb.svg "Diagram")
## Generics
| Generic name | Type    | Value | Description |
| ------------ | ------- | ----- | ----------- |
| GC_TESTCASE  | natural | 0     |             |
## Signals
| Name       | Type                                      | Description |
| ---------- | ----------------------------------------- | ----------- |
| output_sl  | std_logic                                 |             |
| input_sl   | std_logic                                 |             |
| input_slv  | std_logic_vector(C_DATA_WIDTH-1 downto 0) |             |
| output_slv | std_logic_vector(C_DATA_WIDTH-1 downto 0) |             |
## Constants
| Name                 | Type                                      | Value            | Description |
| -------------------- | ----------------------------------------- | ---------------- | ----------- |
| C_SCOPE              | string                                    |  "EI_DEMO_TB"    |             |
| C_SL_EI_IDX          | natural                                   |  1               |             |
| C_SLV_EI_IDX         | natural                                   |  2               |             |
| C_DATA_WIDTH         | natural                                   |  8               |             |
| C_SL_SIGNAL_DEFAULT  | std_logic                                 |  '0'             |             |
| C_SLV_SIGNAL_DEFAULT | std_logic_vector(C_DATA_WIDTH-1 downto 0) |  (others => '0') |             |
| C_PULSE_WIDTH        | time                                      |  20 ns           |             |
## Processes
- p_sequencer: _(  )_

## Instantiations
- i_ti_uvvm_engine: uvvm_vvc_framework.ti_uvvm_engine
- error_injector_sl: work.error_injection_sl
- error_injector_slv: work.error_injection_slv
