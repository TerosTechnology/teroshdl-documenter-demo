# Package: simulation

## Types

| Name        | Type | Description |
| ----------- | ---- | ----------- |
| TIME_VECTOR |      |             |
## Functions
- simInitialize <font id="function_arguments">(MaxAssertFailures : natural := natural'high; MaxSimulationRuntime : TIME := TIME'high) </font> <font id="function_return">return ()</font>
**Description**
Testbench Status Management===========================================================================alias simInitialize					is work.sim_unprotected.initialize[NATURAL, TIME];
- simStopAllClocks <font id="function_arguments">()</font> <font id="function_return">return ()</font>
