# Package: sim_types

## Description

use			PoC.physical.all;

## Constants

| Name                    | Type          | Value           | Description |
| ----------------------- | ------------- | --------------- | ----------- |
| C_SIM_VERBOSE           | boolean       |  FALSE          | POC_VERBOSE |
| C_SIM_DEFAULT_TEST_ID   | T_SIM_TEST_ID |  -1             |             |
| C_SIM_DEFAULT_TEST_NAME | string        |  "Default test" |             |
## Types

| Name                    | Type                                                                                               | Description                                                                                                                                                                                                 |
| ----------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T_SIM_BOOLVEC           |                                                                                                    | ===========================================================================Simulation Task and Status Management===========================================================================                 |
| T_SIM_PROCESS_ID_VECTOR |                                                                                                    |                                                                                                                                                                                                             |
| T_SIM_TEST_STATUS       | ( SIM_TEST_STATUS_CREATED, SIM_TEST_STATUS_ACTIVE, SIM_TEST_STATUS_ENDED, SIM_TEST_STATUS_ZOMBI )  |                                                                                                                                                                                                             |
| T_SIM_PROCESS_STATUS    | ( SIM_PROCESS_STATUS_ACTIVE, SIM_PROCESS_STATUS_ENDED )                                            |                                                                                                                                                                                                             |
| T_SIM_TEST              |                                                                                                    |                                                                                                                                                                                                             |
| T_SIM_TEST_VECTOR       |                                                                                                    |                                                                                                                                                                                                             |
| T_SIM_PROCESS           |                                                                                                    |                                                                                                                                                                                                             |
| T_SIM_PROCESS_VECTOR    |                                                                                                    |                                                                                                                                                                                                             |
| T_SIM_RAND_SEED         |                                                                                                    | ===========================================================================Random Numbers===========================================================================                                        |
| T_PERCENT               |                                                                                                    | ===========================================================================Clock Generation===========================================================================type T_PERCENT is INTEGER'range units |
| T_DEGREE                |                                                                                                    |                                                                                                                                                                                                             |
## Functions
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; SeedValue : in T_SIM_RAND_SEED) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; SeedVector : in T_INTVEC) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; SeedVector : in string) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">()</font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedValue : T_SIM_RAND_SEED) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedVector : T_INTVEC) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedVector : string) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL) </font> <font id="function_return">return ()</font>
**Description**
Uniform distributed random values===========================================================================
- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out integer; Minimum : integer; Maximum : integer) </font> <font id="function_return">return ()</font>
- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL; Minimum : REAL; Maximum : REAL) </font> <font id="function_return">return ()</font>
- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL; StandardDeviation : REAL := 1.0; Mean : REAL := 0.0) </font> <font id="function_return">return ()</font>
**Description**
Normal / Gaussian distributed random values===========================================================================
- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out integer; StandardDeviation : in REAL; Mean : in REAL; Minimum : in integer; Maximum : in integer) </font> <font id="function_return">return ()</font>
- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL; StandardDeviation : in REAL; Mean : in REAL; Minimum : in REAL; Maximum : in REAL) </font> <font id="function_return">return ()</font>
- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL; Mean : in REAL) </font> <font id="function_return">return ()</font>
**Description**
Poisson distributed random values===========================================================================
- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out integer; Mean : in REAL; Minimum : in integer; Maximum : in integer) </font> <font id="function_return">return ()</font>
- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED; Value : out REAL; Mean : in REAL; Minimum : in REAL; Maximum : in REAL) </font> <font id="function_return">return ()</font>
- ite <font id="function_arguments">(cond : boolean; value1 : T_DEGREE; value2 : T_DEGREE) </font> <font id="function_return">return T_DEGREE </font>
