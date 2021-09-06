# Package: AlertLogPkg

- **File**: AlertLogPkg.vhd
## Constants

| Name                         | Type           | Value                 | Description                                                                                     |
| ---------------------------- | -------------- | --------------------- | ----------------------------------------------------------------------------------------------- |
| ALERTLOG_BASE_ID             | AlertLogIDType |  0                    |  Careful as some code may assume this is 0.                                                    |
| ALERTLOG_DEFAULT_ID          | AlertLogIDType |  ALERTLOG_BASE_ID + 1 |                                                                                                 |
| OSVVM_ALERTLOG_ID            | AlertLogIDType |  ALERTLOG_BASE_ID + 2 |  reporting for packages                                                                        |
| REQUIREMENT_ALERTLOG_ID      | AlertLogIDType |  ALERTLOG_BASE_ID + 3 |                                                                                                 |
| OSVVM_SCOREBOARD_ALERTLOG_ID | AlertLogIDType |  OSVVM_ALERTLOG_ID    |  May have its own ID or OSVVM_ALERTLOG_ID as default - most scoreboards allocate their own ID  |
| ALERT_DEFAULT_ID             | AlertLogIDType |  ALERTLOG_DEFAULT_ID  |  Same as ALERTLOG_DEFAULT_ID                                                                   |
| LOG_DEFAULT_ID               | AlertLogIDType |  ALERTLOG_DEFAULT_ID  |                                                                                                 |
| ALERTLOG_ID_NOT_FOUND        | AlertLogIDType |  -1                   |  alternately integer'right                                                                     |
| ALERTLOG_ID_NOT_ASSIGNED     | AlertLogIDType |  -1                   |                                                                                                 |
| MIN_NUM_AL_IDS               | AlertLogIDType |  32                   |  Number IDs initially allocated                                                                |
## Types

| Name                 | Type                                                                                                                                                                                  | Description                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| AlertLogIDVectorType | array (integer range <>) of AlertLogIDType                                                                                                                                            |                                          |
| AlertType            | (FAILURE,<br><span style="padding-left:20px"> ERROR,<br><span style="padding-left:20px"> WARNING)                                                                                     |  NEVER                                  |
| AlertCountType       |                                                                                                                                                                                       |                                          |
| AlertEnableType      |                                                                                                                                                                                       |                                          |
| LogType              | (ALWAYS,<br><span style="padding-left:20px"> DEBUG,<br><span style="padding-left:20px"> FINAL,<br><span style="padding-left:20px"> INFO,<br><span style="padding-left:20px"> PASSED)  |  NEVER  -- See function IsLogEnableType |
| LogEnableType        |                                                                                                                                                                                       |                                          |
## Functions
- Alert <font id="function_arguments">( AlertLogID   : AlertLogIDType ;<br><span style="padding-left:20px"> Message      : string ;<br><span style="padding-left:20px"> Level        : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
  Alert always goes to the transcript file

- Alert <font id="function_arguments">( Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- IncAlertCount <font id="function_arguments">(   -- A silent form of alert AlertLogID   : AlertLogIDType ;<br><span style="padding-left:20px"> Level        : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- IncAlertCount <font id="function_arguments">( Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIf <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 Similar to assert, except condition is positive

- AlertIf <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 Direct replacement for assert

- AlertIfNot <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : std_logic ;<br><span style="padding-left:20px">         Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 overloading for common functionality

- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : std_logic_vector ;<br><span style="padding-left:20px">  Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : unsigned ;<br><span style="padding-left:20px">          Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : signed ;<br><span style="padding-left:20px">            Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : integer ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : real ;<br><span style="padding-left:20px">              Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : character ;<br><span style="padding-left:20px">         Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : string ;<br><span style="padding-left:20px">            Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : time ;<br><span style="padding-left:20px">              Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : std_logic ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : std_logic_vector ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : unsigned ;<br><span style="padding-left:20px">         Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : signed ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : integer ;<br><span style="padding-left:20px">          Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : real ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : character ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : string ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : time ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : std_logic ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : std_logic_vector ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : unsigned ;<br><span style="padding-left:20px">         Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : signed ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : integer ;<br><span style="padding-left:20px">          Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : real ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : character ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : string ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  L,<br><span style="padding-left:20px"> R : time ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : std_logic ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : std_logic_vector ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : unsigned ;<br><span style="padding-left:20px">         Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : signed ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : integer ;<br><span style="padding-left:20px">          Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : real ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : character ;<br><span style="padding-left:20px">        Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : string ;<br><span style="padding-left:20px">           Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L,<br><span style="padding-left:20px"> R : time ;<br><span style="padding-left:20px">             Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Name1,<br><span style="padding-left:20px"> Name2 : string;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 Simple Diff for file comparisons

- AlertIfDiff <font id="function_arguments">(Name1,<br><span style="padding-left:20px"> Name2 : string;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> file File1,<br><span style="padding-left:20px"> File2 : text;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(file File1,<br><span style="padding-left:20px"> File2 : text;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">( AlertLogID       : AlertLogIDType ;<br><span style="padding-left:20px"> condition        : boolean ;<br><span style="padding-left:20px"> ReceivedMessage  : string ;<br><span style="padding-left:20px"> ExpectedMessage  : string ;<br><span style="padding-left:20px"> Enable           : boolean  := FALSE   -- override internal enable ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------

- AffirmIf <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> ReceivedMessage,<br><span style="padding-left:20px"> ExpectedMessage : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">( AlertLogID   : AlertLogIDType ;<br><span style="padding-left:20px"> condition    : boolean ;<br><span style="padding-left:20px"> Message      : string ;<br><span style="padding-left:20px"> Enable       : boolean := FALSE -- override internal enable ) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px">  Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> ReceivedMessage,<br><span style="padding-left:20px"> ExpectedMessage : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- AffirmIfNot <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> ReceivedMessage,<br><span style="padding-left:20px"> ExpectedMessage : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- AffirmIfNot <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmPassed <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- AffirmPassed <font id="function_arguments">( Message : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmError <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Message : string ) </font> <font id="function_return">return ()</font>
- AffirmError <font id="function_arguments">( Message : string ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : boolean ;<br><span style="padding-left:20px">  Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : std_logic ;<br><span style="padding-left:20px">  Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : std_logic_vector ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : unsigned ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : signed ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : integer ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : real ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : character ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : string ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Received,<br><span style="padding-left:20px"> Expected : time ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : boolean ;<br><span style="padding-left:20px">  Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
 Without AlertLogID
----------------------------------------------------------

- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : std_logic ;<br><span style="padding-left:20px">  Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : std_logic_vector ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : unsigned ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : signed ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : integer ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : real ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : character ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : string ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received,<br><span style="padding-left:20px"> Expected : time ;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Name1,<br><span style="padding-left:20px"> Name2 : string;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- AffirmIfDiff <font id="function_arguments">(Name1,<br><span style="padding-left:20px"> Name2 : string;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> file File1,<br><span style="padding-left:20px"> File2 : text;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(file File1,<br><span style="padding-left:20px"> File2 : text;<br><span style="padding-left:20px"> Message : string := "" ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">( RequirementsIDName : string ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> ReceivedMessage,<br><span style="padding-left:20px"> ExpectedMessage : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 Support for Specification / Requirements Tracking

- AffirmIf <font id="function_arguments">( RequirementsIDName : string ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Enable : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- SetAlertLogJustify <font id="function_arguments">(Enable : boolean := TRUE) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- ReportAlerts <font id="function_arguments">( Name : String ;<br><span style="padding-left:20px"> AlertCount : AlertCountType ) </font> <font id="function_return">return ()</font>
- ReportRequirements <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ReportAlerts <font id="function_arguments">( Name : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID ;<br><span style="padding-left:20px"> ExternalErrors : AlertCountType := (others => 0) ) </font> <font id="function_return">return ()</font>
- ReportNonZeroAlerts <font id="function_arguments">( Name : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID ;<br><span style="padding-left:20px"> ExternalErrors : AlertCountType := (others => 0) ) </font> <font id="function_return">return ()</font>
- WriteTestSummary <font id="function_arguments">( FileName : string ;<br><span style="padding-left:20px"> OpenKind : File_Open_Kind := APPEND_MODE ) </font> <font id="function_return">return ()</font>
- WriteTestSummaries <font id="function_arguments">( FileName : string ;<br><span style="padding-left:20px"> OpenKind : File_Open_Kind := WRITE_MODE ) </font> <font id="function_return">return ()</font>
- ReportTestSummaries <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- WriteAlerts <font id="function_arguments">( FileName    : string ;<br><span style="padding-left:20px"> AlertLogID  : AlertLogIDType := ALERTLOG_BASE_ID ;<br><span style="padding-left:20px"> OpenKind    : File_Open_Kind := WRITE_MODE ) </font> <font id="function_return">return ()</font>
- WriteRequirements <font id="function_arguments">( FileName        : string ;<br><span style="padding-left:20px"> AlertLogID      : AlertLogIDType := REQUIREMENT_ALERTLOG_ID ;<br><span style="padding-left:20px"> OpenKind        : File_Open_Kind := WRITE_MODE ) </font> <font id="function_return">return ()</font>
- ReadSpecification <font id="function_arguments">(FileName : string ;<br><span style="padding-left:20px"> PassedGoal : integer := -1) </font> <font id="function_return">return ()</font>
- ReadRequirements <font id="function_arguments">( FileName        : string ;<br><span style="padding-left:20px"> ThresholdPassed : boolean := FALSE ) </font> <font id="function_return">return ()</font>
- ReadTestSummaries <font id="function_arguments">(FileName : string) </font> <font id="function_return">return ()</font>
- ClearAlerts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ClearAlertStopCounts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ClearAlertCounts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- Log <font id="function_arguments">( AlertLogID   : AlertLogIDType ;<br><span style="padding-left:20px"> Message      : string ;<br><span style="padding-left:20px"> Level        : LogType := ALWAYS ;<br><span style="padding-left:20px"> Enable       : boolean := FALSE    -- override internal enable ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
  log filtering for verbosity control, optionally has a separate file parameter

- Log <font id="function_arguments">( Message : string ;<br><span style="padding-left:20px"> Level : LogType := ALWAYS ;<br><span style="padding-left:20px"> Enable : boolean := FALSE) </font> <font id="function_return">return ()</font>
- SetAlertEnable <font id="function_arguments">(Level : AlertType ;<br><span style="padding-left:20px">  Enable : boolean) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------
 Alert Enables

- SetAlertEnable <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  Level : AlertType ;<br><span style="padding-left:20px">  Enable : boolean ;<br><span style="padding-left:20px"> DescendHierarchy : boolean := TRUE) </font> <font id="function_return">return ()</font>
- SetLogEnable <font id="function_arguments">(Level : LogType ;<br><span style="padding-left:20px">  Enable : boolean) </font> <font id="function_return">return ()</font>
</br>**Description**
 Log Enables

- SetLogEnable <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  Level : LogType ;<br><span style="padding-left:20px">  Enable : boolean ;<br><span style="padding-left:20px"> DescendHierarchy : boolean := TRUE) </font> <font id="function_return">return ()</font>
- ReportLogEnables <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
 same as GetLogEnable

- SetAlertLogName <font id="function_arguments">(Name : string ) </font> <font id="function_return">return ()</font>
- DeallocateAlertLogStruct <font id="function_arguments">()</font> <font id="function_return">return ()</font>
</br>**Description**
 synthesis translate_on

- InitializeAlertLogStruct <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- SetPassedGoal <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> PassedGoal : integer ) </font> <font id="function_return">return ()</font>
- SetAlertLogPrefix <font id="function_arguments">(AlertLogID : AlertLogIDType;<br><span style="padding-left:20px"> Name : string ) </font> <font id="function_return">return ()</font>
- UnSetAlertLogPrefix <font id="function_arguments">(AlertLogID : AlertLogIDType) </font> <font id="function_return">return ()</font>
- SetAlertLogSuffix <font id="function_arguments">(AlertLogID : AlertLogIDType;<br><span style="padding-left:20px"> Name : string ) </font> <font id="function_return">return ()</font>
</br>**Description**
 synthesis translate_on

- UnSetAlertLogSuffix <font id="function_arguments">(AlertLogID : AlertLogIDType) </font> <font id="function_return">return ()</font>
- SetGlobalAlertEnable <font id="function_arguments">(A : boolean := TRUE) </font> <font id="function_return">return ()</font>
</br>**Description**
 synthesis translate_on
----------------------------------------------------------
 Accessor Methods

- IncAffirmCount <font id="function_arguments">(AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID) </font> <font id="function_return">return ()</font>
- IncAffirmPassedCount <font id="function_arguments">(AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID) </font> <font id="function_return">return ()</font>
- SetAlertStopCount <font id="function_arguments">(AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px">  Level : AlertType ;<br><span style="padding-left:20px">  Count : integer) </font> <font id="function_return">return ()</font>
- SetAlertStopCount <font id="function_arguments">(Level : AlertType ;<br><span style="padding-left:20px">  Count : integer) </font> <font id="function_return">return ()</font>
- SetAlertLogOptions <font id="function_arguments">( FailOnWarning            : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> FailOnDisabledErrors     : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> FailOnRequirementErrors  : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> ReportHierarchy          : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteAlertErrorCount     : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteAlertLevel          : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteAlertName           : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteAlertTime           : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteLogErrorCount       : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteLogLevel            : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteLogName             : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> WriteLogTime             : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PrintPassed              : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PrintAffirmations        : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PrintDisabledAlerts      : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PrintRequirements        : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PrintIfHaveRequirements  : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> DefaultPassedGoal        : integer             := integer'left ;<br><span style="padding-left:20px"> AlertPrefix              : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> LogPrefix                : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> ReportPrefix             : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> DoneName                 : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> PassName                 : string := OSVVM_STRING_INIT_PARM_DETECT ;<br><span style="padding-left:20px"> FailName                 : string := OSVVM_STRING_INIT_PARM_DETECT ) </font> <font id="function_return">return ()</font>
</br>**Description**
----------------------------------------------------------

- ReportAlertLogOptions <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- IsLogEnableType <font id="function_arguments">(Name : String) </font> <font id="function_return">return boolean </font>
</br>**Description**
 File Reading Utilities

- ReadLogEnables <font id="function_arguments">(file AlertLogInitFile : text) </font> <font id="function_return">return ()</font>
- ReadLogEnables <font id="function_arguments">(FileName : string) </font> <font id="function_return">return ()</font>
- PathTail <font id="function_arguments">(A : string) </font> <font id="function_return">return string </font>
</br>**Description**
 String Helper Functions -- This should be in a more general string package

- MetaMatch <font id="function_arguments">(l,<br><span style="padding-left:20px"> r : std_ulogic) </font> <font id="function_return">return boolean </font>
</br>**Description**
----------------------------------------------------------
 MetaMatch
   Similar to STD_MATCH, except 
   it returns TRUE for U=U, X=X, Z=Z, and W=W 
   All other values are consistent with STD_MATCH
   MetaMatch, BooleanTableType, and MetaMatchTable are derivatives
   of STD_MATCH from IEEE.Numeric_Std copyright by IEEE.
   Numeric_Std is also released under the Apache License, Version 2.0.
   Coding Styles were updated to match OSVVM
----------------------------------------------------------

- MetaMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : std_ulogic_vector) </font> <font id="function_return">return boolean </font>
- MetaMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : unresolved_unsigned) </font> <font id="function_return">return boolean </font>
- MetaMatch <font id="function_arguments">(L,<br><span style="padding-left:20px"> R : unresolved_signed) </font> <font id="function_return">return boolean </font>
- AlertIf <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
 synthesis translate_on
  ------------------------------------------------------------
 Deprecated

 deprecated

- AlertIfNot <font id="function_arguments">( condition : boolean ;<br><span style="padding-left:20px"> AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> Level : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
 deprecated

- AffirmIf <font id="function_arguments">( AlertLogID   : AlertLogIDType ;<br><span style="padding-left:20px"> condition    : boolean ;<br><span style="padding-left:20px"> Message      : string ;<br><span style="padding-left:20px"> LogLevel     : LogType  ;<br><span style="padding-left:20px">  -- := PASSED AlertLevel   : AlertType := ERROR ) </font> <font id="function_return">return ()</font>
</br>**Description**
 deprecated

- AffirmIf <font id="function_arguments">( AlertLogID : AlertLogIDType ;<br><span style="padding-left:20px"> condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px"> AlertLevel : AlertType ) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px">  LogLevel : LogType  ;<br><span style="padding-left:20px"> AlertLevel : AlertType := ERROR) </font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ;<br><span style="padding-left:20px"> Message : string ;<br><span style="padding-left:20px">  AlertLevel : AlertType ) </font> <font id="function_return">return ()</font>
