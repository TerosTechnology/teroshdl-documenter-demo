# Entity: irqc
## Diagram
![Diagram](irqc.svg "Diagram")
## Ports
| Port name   | Direction | Type                                       | Description |
| ----------- | --------- | ------------------------------------------ | ----------- |
| clk         | in        | std_logic                                  |             |
| arst        | in        | std_logic                                  |             |
| cs          | in        | std_logic                                  |             |
| addr        | in        | unsigned(2 downto 0)                       |             |
| wr          | in        | std_logic                                  |             |
| rd          | in        | std_logic                                  |             |
| din         | in        | std_logic_vector(7 downto 0)               |             |
| dout        | out       | std_logic_vector(7 downto 0)               |             |
| irq_source  | in        | std_logic_vector(C_NUM_SOURCES-1 downto 0) |             |
| irq2cpu     | out       | std_logic                                  |             |
| irq2cpu_ack | in        | std_logic                                  |             |
## Signals
| Name | Type  | Description |
| ---- | ----- | ----------- |
| p2c  | t_p2c |             |
| c2p  | t_c2p |             |
## Instantiations
- i_irqc_pif: work.irqc_pif
- i_irqc_core: work.irqc_core
