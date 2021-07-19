# Package: simulation

- **File**: sim_simulation.v08.vhdl
## Functions
- simInitialize <font id="function_arguments">(MaxAssertFailures : natural := natural'high;<br><span style="padding-left:20px"> MaxSimulationRuntime : TIME := TIME'high) </font> <font id="function_return">return ()</font>
- simFinalize <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- simFinalizeTest <font id="function_arguments">(constant TestID : T_SIM_TEST_ID) </font> <font id="function_return">return ()</font>
- simDeactivateProcess <font id="function_arguments">(ProcID : T_SIM_PROCESS_ID) </font> <font id="function_return">return ()</font>
- simAssertion <font id="function_arguments">(cond : in boolean;<br><span style="padding-left:20px"> Message : in string := "") </font> <font id="function_return">return ()</font>
- simFail <font id="function_arguments">(Message : in string := "") </font> <font id="function_return">return ()</font>
- simWriteMessage <font id="function_arguments">(Message : in string := "") </font> <font id="function_return">return ()</font>
