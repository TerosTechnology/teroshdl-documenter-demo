# Package: simulation

- **File**: sim_simulation.v93.vhdl
## Types

| Name        | Type                            | Description |
| ----------- | ------------------------------- | ----------- |
| TIME_VECTOR | array(natural range<>) of time  |             |
## Functions
- simInitialize <font id="function_arguments">(MaxAssertFailures : natural := natural'high;<br><span style="padding-left:20px"> MaxSimulationRuntime : TIME := TIME'high) </font> <font id="function_return">return ()</font>
**Description**
Testbench Status Management===========================================================================alias simInitialize					is work.sim_unprotected.initialize[NATURAL, TIME];
- simStopAllClocks <font id="function_arguments">()</font> <font id="function_return">return ()</font>
