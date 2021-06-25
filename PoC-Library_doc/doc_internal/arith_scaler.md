# Entity: arith_scaler
## Diagram
![Diagram](arith_scaler.svg "Diagram")
## Generics
| Generic name | Type     | Value    | Description |
| ------------ | -------- | -------- | ----------- |
| MULS         | T_POSVEC | (0 => 1) |             |
| DIVS         | T_POSVEC | (0 => 1) |             |
## Ports
| Port name | Direction | Type                                               | Description |
| --------- | --------- | -------------------------------------------------- | ----------- |
| clk       | in        | std_logic                                          |             |
| rst       | in        | std_logic                                          |             |
| start     | in        | std_logic                                          |             |
| arg       | in        | std_logic_vector                                   |             |
| msel      | in        | std_logic_vector(log2ceil(MULS'length)-1 downto 0) |             |
| dsel      | in        | std_logic_vector(log2ceil(DIVS'length)-1 downto 0) |             |
| done      | out       | std_logic                                          |             |
| res       | out       | std_logic_vector                                   |             |
## Signals
| Name       | Type                                         | Description |
| ---------- | -------------------------------------------- | ----------- |
| muloffset  | unsigned(X-1 downto 0)                       |             |
| multiplier | unsigned(X	 downto 0)                        |             |
| divisor    | unsigned(R-1 downto 0)                       |             |
| divcini    | unsigned(log2ceil(MAX_ANY_STEPS)-1 downto 0) |             |
| divmask    | tResMask                                     |             |
## Constants
| Name          | Type                  | Value                                       | Description |
| ------------- | --------------------- | ------------------------------------------- | ----------- |
| N             | positive              |  arg'length                                 |             |
| X             | positive              |  log2ceil(imax(imax(MULS), imax(DIVS)/2+1)) |             |
| R             | positive              |  log2ceil(imax(DIVS)+1)                     |             |
| DIV_PROPS     | tDivProps             |  computeProps                               |             |
| MAX_MUL_STEPS | positive              |  N                                          |             |
| MAX_DIV_STEPS | positive              |  imax(DIV_PROPS.steps)                      |             |
| MAX_ANY_STEPS | positive              |  imax(MAX_MUL_STEPS, MAX_DIV_STEPS)         |             |
| RES_MASKS     | tResMasks(DIVS'range) |  computeMasks                               |             |
## Types
| Name      | Type | Description |
| --------- | ---- | ----------- |
| tDivProps |      |             |
| tResMasks |      |             |
## Functions
- computeProps <font id="function_arguments">()</font> <font id="function_return">return tDivProps</font>
- computeMasks <font id="function_arguments">()</font> <font id="function_return">return tResMasks</font>
