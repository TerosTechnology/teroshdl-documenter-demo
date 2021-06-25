# Entity: irqc_demo_tb
## Diagram
![Diagram](irqc_demo_tb.svg "Diagram")
## Signals
| Name        | Type                                                             | Description |
| ----------- | ---------------------------------------------------------------- | ----------- |
| clk         | std_logic                                                        |             |
| arst        | std_logic                                                        |             |
| sbi_if      | t_sbi_if(addr(2 downto 0), wdata(7 downto 0), rdata(7 downto 0)) |             |
| irq_source  | std_logic_vector(C_NUM_SOURCES-1 downto 0)                       |             |
| irq2cpu     | std_logic                                                        |             |
| irq2cpu_ack | std_logic                                                        |             |
| clock_ena   | boolean                                                          |             |
## Constants
| Name         | Type | Value  | Description |
| ------------ | ---- | ------ | ----------- |
| C_CLK_PERIOD | time |  10 ns |             |
## Functions
- trim <font id="function_arguments">(      constant source   : std_logic_vector;
      constant num_bits : positive := C_NUM_SOURCES)</font> <font id="function_return">return t_irq_source</font>
- fit <font id="function_arguments">(      constant source   : std_logic_vector;
      constant num_bits : positive := C_NUM_SOURCES)</font> <font id="function_return">return std_logic_vector</font>
## Processes
- p_main: _(  )_

## Instantiations
- i_irqc: work.irqc
