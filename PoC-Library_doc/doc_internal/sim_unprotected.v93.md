# Package: sim_unprotected
## Functions
- initialize <font id="function_arguments">(MaxAssertFailures : natural := natural'high; MaxSimulationRuntime : TIME := TIME'high)</font> <font id="function_return">return ()</font>
- finalize <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- fail <font id="function_arguments">(Message : string := "")</font> <font id="function_return">return ()</font>
**Description**
Assertions
- assertion <font id="function_arguments">(Condition : boolean; Message : string := "")</font> <font id="function_return">return ()</font>
- writeMessage <font id="function_arguments">(Message : string)</font> <font id="function_return">return ()</font>
- writeReport <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- deactivateProcess <font id="function_arguments">(procID : T_SIM_PROCESS_ID)</font> <font id="function_return">return ()</font>
- stopAllProcesses <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- stopProcesses <font id="function_arguments">(TestID	: T_SIM_TEST_ID := C_SIM_DEFAULT_TEST_ID)</font> <font id="function_return">return ()</font>
- createDefaultTest <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Test Management
- activateDefaultTest <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- finalizeTest <font id="function_arguments">(TestID : T_SIM_TEST_ID)</font> <font id="function_return">return ()</font>
- stopAllClocks <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
Clock Management
- stopClocks <font id="function_arguments">(TestID		: T_SIM_TEST_ID := C_SIM_DEFAULT_TEST_ID)</font> <font id="function_return">return ()</font>
