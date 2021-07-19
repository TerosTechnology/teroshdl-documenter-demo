# Package: TestSupportPkg

- **File**: Demo_Rand.vhd
## Types

| Name          | Type                                 | Description |
| ------------- | ------------------------------------ | ----------- |
| integer_array | array (integer range <>) of integer  |             |
## Functions
- TestInit <font id="function_arguments">(TestName : string ;<br><span style="padding-left:20px"> variable Results : inout integer_array ) </font> <font id="function_return">return ()</font>
- TestInit <font id="function_arguments">(TestName : string ;<br><span style="padding-left:20px"> variable Results : inout integer_array ;<br><span style="padding-left:20px"> variable Count : inout natural ) </font> <font id="function_return">return ()</font>
- AccumulateResults <font id="function_arguments">(IntVal : integer ;<br><span style="padding-left:20px"> Num : integer ;<br><span style="padding-left:20px"> variable Results : inout integer_array) </font> <font id="function_return">return ()</font>
- PrintResults <font id="function_arguments">(Results : integer_array) </font> <font id="function_return">return ()</font>
