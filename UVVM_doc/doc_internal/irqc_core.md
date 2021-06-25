# Entity: irqc_core
## Diagram
![Diagram](irqc_core.svg "Diagram")
## Ports
| Port name   | Direction | Type                                       | Description |
| ----------- | --------- | ------------------------------------------ | ----------- |
| clk         | in        | std_logic                                  |             |
| arst        | in        | std_logic                                  |             |
| p2c         | in        | t_p2c                                      |             |
| c2p         | out       | t_c2p                                      |             |
| irq_source  | in        | std_logic_vector(C_NUM_SOURCES-1 downto 0) |             |
| irq2cpu     | out       | std_logic                                  |             |
| irq2cpu_ack | in        | std_logic                                  |             |
## Signals
| Name  | Type      | Description |
| ----- | --------- | ----------- |
| c2p_i | t_c2p     |             |
| igr   | std_logic |             |
## Functions
- or_reduce <font id="function_arguments">(    constant value : std_logic_vector
    )</font> <font id="function_return">return std_logic</font>
## Processes
- p_irr: _( clk, arst )_

- p_irq2cpu: _( clk, arst )_

