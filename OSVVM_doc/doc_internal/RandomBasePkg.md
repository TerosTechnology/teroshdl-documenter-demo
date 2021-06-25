# Package: RandomBasePkg
## Types
| Name           | Type | Description |
| -------------- | ---- | ----------- |
| RandomSeedType |      |             |
## Functions
- Uniform <font id="function_arguments">(Result : out real ;  Seed : inout RandomSeedType)</font> <font id="function_return">return ()</font>
- to_string <font id="function_arguments">(A : RandomSeedType)</font> <font id="function_return">return string</font>
- write <font id="function_arguments">(variable L: inout line ; A : RandomSeedType )</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ; A : out RandomSeedType ; good : out boolean )</font> <font id="function_return">return ()</font>
- read <font id="function_arguments">(variable L: inout line ; A : out RandomSeedType )</font> <font id="function_return">return ()</font>
