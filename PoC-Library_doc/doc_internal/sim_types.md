# Package: sim_types

- **File**: sim_types.vhdl
## Description

 use			PoC.physical.all;

## Constants

| Name                    | Type          | Value           | Description  |
| ----------------------- | ------------- | --------------- | ------------ |
| C_SIM_VERBOSE           | boolean       |  FALSE          |  POC_VERBOSE |
| C_SIM_DEFAULT_TEST_ID   | T_SIM_TEST_ID |  -1             |              |
| C_SIM_DEFAULT_TEST_NAME | string        |  "Default test" |              |
## Types

| Name                    | Type                                                                                                                                                                                                           | Description                                                                                                                                                                                                         |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T_SIM_BOOLVEC           | array(integer range <>) of boolean                                                                                                                                                                             |  ===========================================================================  Simulation Task and Status Management  ===========================================================================                    |
| T_SIM_PROCESS_ID_VECTOR | array(natural range <>) of T_SIM_PROCESS_ID                                                                                                                                                                    |                                                                                                                                                                                                                     |
| T_SIM_TEST_STATUS       | ( SIM_TEST_STATUS_CREATED,<br><span style="padding-left:20px"> SIM_TEST_STATUS_ACTIVE,<br><span style="padding-left:20px"> SIM_TEST_STATUS_ENDED,<br><span style="padding-left:20px"> SIM_TEST_STATUS_ZOMBI )  |                                                                                                                                                                                                                     |
| T_SIM_PROCESS_STATUS    | ( SIM_PROCESS_STATUS_ACTIVE,<br><span style="padding-left:20px"> SIM_PROCESS_STATUS_ENDED )                                                                                                                    |                                                                                                                                                                                                                     |
| T_SIM_TEST              |                                                                                                                                                                                                                |                                                                                                                                                                                                                     |
| T_SIM_TEST_VECTOR       | array(integer range <>) of T_SIM_TEST                                                                                                                                                                          |                                                                                                                                                                                                                     |
| T_SIM_PROCESS           |                                                                                                                                                                                                                |                                                                                                                                                                                                                     |
| T_SIM_PROCESS_VECTOR    | array(natural range <>) of T_SIM_PROCESS                                                                                                                                                                       |                                                                                                                                                                                                                     |
| T_SIM_RAND_SEED         |                                                                                                                                                                                                                |  ===========================================================================  Random Numbers  ===========================================================================                                           |
| T_PERCENT               |                                                                                                                                                                                                                |  ===========================================================================  Clock Generation  ===========================================================================  type T_PERCENT is INTEGER'range units  |
| T_DEGREE                |                                                                                                                                                                                                                |                                                                                                                                                                                                                     |
## Functions
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> SeedValue : in T_SIM_RAND_SEED) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> SeedVector : in T_INTVEC) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> SeedVector : in string) </font> <font id="function_return">return ()</font>
- randInitializeSeed <font id="function_arguments">()</font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedValue : T_SIM_RAND_SEED) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedVector : T_INTVEC) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randInitializeSeed <font id="function_arguments">(SeedVector : string) </font> <font id="function_return">return T_SIM_RAND_SEED </font>
- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL) </font> <font id="function_return">return ()</font>
</br>**Description**
 Uniform distributed random values
 ===========================================================================

- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out integer;<br><span style="padding-left:20px"> Minimum : integer;<br><span style="padding-left:20px"> Maximum : integer) </font> <font id="function_return">return ()</font>
- randUniformDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL;<br><span style="padding-left:20px"> Minimum : REAL;<br><span style="padding-left:20px"> Maximum : REAL) </font> <font id="function_return">return ()</font>
- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL;<br><span style="padding-left:20px"> StandardDeviation : REAL := 1.0;<br><span style="padding-left:20px"> Mean : REAL := 0.0) </font> <font id="function_return">return ()</font>
</br>**Description**
 Normal / Gaussian distributed random values
 ===========================================================================

- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out integer;<br><span style="padding-left:20px"> StandardDeviation : in REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in integer;<br><span style="padding-left:20px"> Maximum : in integer) </font> <font id="function_return">return ()</font>
- randNormalDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL;<br><span style="padding-left:20px"> StandardDeviation : in REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in REAL;<br><span style="padding-left:20px"> Maximum : in REAL) </font> <font id="function_return">return ()</font>
- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL;<br><span style="padding-left:20px"> Mean : in REAL) </font> <font id="function_return">return ()</font>
</br>**Description**
 Poisson distributed random values
 ===========================================================================

- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out integer;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in integer;<br><span style="padding-left:20px"> Maximum : in integer) </font> <font id="function_return">return ()</font>
- randPoissonDistributedValue <font id="function_arguments">(Seed : inout T_SIM_RAND_SEED;<br><span style="padding-left:20px"> Value : out REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in REAL;<br><span style="padding-left:20px"> Maximum : in REAL) </font> <font id="function_return">return ()</font>
- ite <font id="function_arguments">(cond : boolean;<br><span style="padding-left:20px"> value1 : T_DEGREE;<br><span style="padding-left:20px"> value2 : T_DEGREE) </font> <font id="function_return">return T_DEGREE </font>
