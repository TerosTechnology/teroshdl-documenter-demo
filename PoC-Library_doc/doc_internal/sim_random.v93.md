# Package: sim_random

- **File**: sim_random.v93.vhdl
## Functions
- randomInitializeSeed <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
 procedural interface

- randomInitializeSeed <font id="function_arguments">(Seed : T_SIM_SEED) </font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(Seed1 : integer;<br><span style="padding-left:20px"> Seed2 : integer) </font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(SeedVector : T_INTVEC) </font> <font id="function_return">return ()</font>
- randomInitializeSeed <font id="function_arguments">(SeedVector : string) </font> <font id="function_return">return ()</font>
- randomUniformDistributedValue <font id="function_arguments">(Value : out REAL) </font> <font id="function_return">return ()</font>
</br>**Description**
 Uniform distributed random values
 ===========================================================================

- randomUniformDistributedValue <font id="function_arguments">(Value : out integer;<br><span style="padding-left:20px"> Minimum : in integer;<br><span style="padding-left:20px"> Maximum : in integer) </font> <font id="function_return">return ()</font>
- randomUniformDistributedValue <font id="function_arguments">(Value : out REAL;<br><span style="padding-left:20px"> Minimum : in REAL;<br><span style="padding-left:20px"> Maximum : in REAL) </font> <font id="function_return">return ()</font>
- randomNormalDistributedValue <font id="function_arguments">(Value : out REAL;<br><span style="padding-left:20px"> StandardDeviation : in REAL := 1.0;<br><span style="padding-left:20px"> Mean : in REAL := 0.0) </font> <font id="function_return">return ()</font>
</br>**Description**
 Normal / Gaussian distributed random values
 ===========================================================================

- randomNormalDistributedValue <font id="function_arguments">(Value : out integer;<br><span style="padding-left:20px"> StandardDeviation : in REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in integer;<br><span style="padding-left:20px"> Maximum : in integer) </font> <font id="function_return">return ()</font>
- randomNormalDistributedValue <font id="function_arguments">(Value : out REAL;<br><span style="padding-left:20px"> StandardDeviation : in REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in REAL;<br><span style="padding-left:20px"> Maximum : in REAL) </font> <font id="function_return">return ()</font>
- randomPoissonDistributedValue <font id="function_arguments">(Value : out REAL;<br><span style="padding-left:20px"> Mean : in REAL) </font> <font id="function_return">return ()</font>
</br>**Description**
 Poisson distributed random values
 ===========================================================================

- randomPoissonDistributedValue <font id="function_arguments">(Value : out integer;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in integer;<br><span style="padding-left:20px"> Maximum : in integer) </font> <font id="function_return">return ()</font>
- randomPoissonDistributedValue <font id="function_arguments">(Value : out REAL;<br><span style="padding-left:20px"> Mean : in REAL;<br><span style="padding-left:20px"> Minimum : in REAL;<br><span style="padding-left:20px"> Maximum : in REAL) </font> <font id="function_return">return ()</font>
