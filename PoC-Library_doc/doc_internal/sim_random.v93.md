# Package: sim_random
## Functions
- randomInitializeSeed <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(Seed : T_SIM_SEED)</font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(Seed1 : integer; Seed2 : integer)</font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(SeedVector : T_INTVEC)</font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(SeedVector : string)</font> <font id="function_return">return ()</font>
- randomUniformDistributedValue <font id="function_arguments">(Value : out REAL)</font> <font id="function_return">return ()</font>
- randomUniformDistributedValue <font id="function_arguments">(Value : out integer; Minimum : in integer; Maximum : in integer)</font> <font id="function_return">return ()</font>
- randomUniformDistributedValue <font id="function_arguments">(Value : out REAL; Minimum : in REAL; Maximum : in REAL)</font> <font id="function_return">return ()</font>
- randomNormalDistributedValue <font id="function_arguments">(Value : out REAL; StandardDeviation : in REAL := 1.0; Mean : in REAL := 0.0)</font> <font id="function_return">return ()</font>
- randomNormalDistributedValue <font id="function_arguments">(Value : out integer; StandardDeviation : in REAL; Mean : in REAL; Minimum : in integer; Maximum : in integer)</font> <font id="function_return">return ()</font>
- randomNormalDistributedValue <font id="function_arguments">(Value : out REAL; StandardDeviation : in REAL; Mean : in REAL; Minimum : in REAL; Maximum : in REAL)</font> <font id="function_return">return ()</font>
- randomPoissonDistributedValue <font id="function_arguments">(Value : out REAL; Mean : in REAL)</font> <font id="function_return">return ()</font>
- randomPoissonDistributedValue <font id="function_arguments">(Value : out integer; Mean : in REAL; Minimum : in integer; Maximum : in integer)</font> <font id="function_return">return ()</font>
- randomPoissonDistributedValue <font id="function_arguments">(Value : out REAL; Mean : in REAL; Minimum : in REAL; Maximum : in REAL)</font> <font id="function_return">return ()</font>
