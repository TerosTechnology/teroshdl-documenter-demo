# Package: MATH_REAL

## Constants

| Name               | Type | Value                       | Description |
| ------------------ | ---- | --------------------------- | ----------- |
| math_e             | real |  2.71828_18284_59045_23536  |             |
| math_1_over_e      | real |  0.36787_94411_71442_321596 |             |
| math_pi            | real |  3.14159_26535_89793_23846  |             |
| math_2_pi          | real |  6.28318_53071_79586_47693  |             |
| math_pi_over_2     | real |  1.57079_63267_94896_61923  |             |
| math_pi_over_3     | real |  1.04719_75511_96597_74615  |             |
| math_pi_over_4     | real |  0.78539_81633_97448_30962  |             |
| math_3_pi_over_2   | real |  4.71238_89803_84689_85769  |             |
| math_log_of_2      | real |  0.69314_71805_59945_30942  |             |
| math_log_of_10     | real |  2.30258_50929_94045_68402  |             |
| math_log2_of_e     | real |  1.44269_50408_88963_40736  |             |
| math_log10_of_e    | real |  0.43429_44819_03251_82765  |             |
| math_sqrt_2        | real |  1.41421_35623_73095_04880  |             |
| math_1_over_sqrt_2 | real |  0.70710_67811_86547_52440  |             |
| math_sqrt_pi       | real |  1.77245_38509_05516_02730  |             |
| math_deg_to_rad    | real |  0.01745_32925_19943_29577  |             |
| math_rad_to_deg    | real |  57.29577_95130_82320_87680 |             |
## Functions
- SIGN <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- CEIL <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- FLOOR <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ROUND <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- TRUNC <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- REALMAX <font id="function_arguments">(X,<br><span style="padding-left:20px"> Y : REAL) </font> <font id="function_return">return REAL </font>
**Description**
 Contrary to fmod, the sign of the result is the sign of Y.
- REALMIN <font id="function_arguments">(X,<br><span style="padding-left:20px"> Y : REAL) </font> <font id="function_return">return REAL </font>
- UNIFORM <font id="function_arguments">(SEED1,<br><span style="padding-left:20px"> SEED2 : inout POSITIVE;<br><span style="padding-left:20px"> X : out REAL) </font> <font id="function_return">return ()</font>
- SQRT <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
**Description**
 Algorithm from: Pierre L'Ecuyer, CACM June 1988 Volume 31 Number 6 page 747 figure 3.
- CBRT <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- EXP <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- LOG <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- LOG2 <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- LOG10 <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- LOG <font id="function_arguments">(X : REAL;<br><span style="padding-left:20px"> BASE : REAL) </font> <font id="function_return">return REAL </font>
- SIN <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- COS <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- TAN <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCSIN <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCCOS <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCTAN <font id="function_arguments">(Y : REAL) </font> <font id="function_return">return REAL </font>
- ARCTAN <font id="function_arguments">(Y,<br><span style="padding-left:20px"> X : REAL) </font> <font id="function_return">return REAL </font>
- SINH <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- COSH <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- TANH <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCSINH <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCCOSH <font id="function_arguments">(X : REAL) </font> <font id="function_return">return REAL </font>
- ARCTANH <font id="function_arguments">(Y : REAL) </font> <font id="function_return">return REAL </font>
