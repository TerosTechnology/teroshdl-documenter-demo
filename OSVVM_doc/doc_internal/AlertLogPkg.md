# Package: AlertLogPkg
## Constants
| Name                         | Type           | Value                 | Description                                                                                   |
| ---------------------------- | -------------- | --------------------- | --------------------------------------------------------------------------------------------- |
| ALERTLOG_BASE_ID             | AlertLogIDType |  0                    | Careful as some code may assume this is 0.                                                    |
| ALERTLOG_DEFAULT_ID          | AlertLogIDType |  ALERTLOG_BASE_ID + 1 |                                                                                               |
| OSVVM_ALERTLOG_ID            | AlertLogIDType |  ALERTLOG_BASE_ID + 2 | reporting for packages                                                                        |
| REQUIREMENT_ALERTLOG_ID      | AlertLogIDType |  ALERTLOG_BASE_ID + 3 |                                                                                               |
| OSVVM_SCOREBOARD_ALERTLOG_ID | AlertLogIDType |  OSVVM_ALERTLOG_ID    | May have its own ID or OSVVM_ALERTLOG_ID as default - most scoreboards allocate their own ID  |
| ALERT_DEFAULT_ID             | AlertLogIDType |  ALERTLOG_DEFAULT_ID  | Same as ALERTLOG_DEFAULT_ID                                                                   |
| LOG_DEFAULT_ID               | AlertLogIDType |  ALERTLOG_DEFAULT_ID  |                                                                                               |
| ALERTLOG_ID_NOT_FOUND        | AlertLogIDType |  -1                   | alternately integer'right                                                                     |
| ALERTLOG_ID_NOT_ASSIGNED     | AlertLogIDType |  -1                   |                                                                                               |
| MIN_NUM_AL_IDS               | AlertLogIDType |  32                   | Number IDs initially allocated                                                                |
## Types
| Name                 | Type                                 | Description                             |
| -------------------- | ------------------------------------ | --------------------------------------- |
| AlertLogIDVectorType |                                      |                                         |
| AlertType            | (FAILURE, ERROR, WARNING)            | NEVER                                   |
| AlertCountType       |                                      |                                         |
| AlertEnableType      |                                      |                                         |
| LogType              | (ALWAYS, DEBUG, FINAL, INFO, PASSED) | NEVER  -- See function IsLogEnableType  |
| LogEnableType        |                                      |                                         |
## Functions
- Alert <font id="function_arguments">(    AlertLogID   : AlertLogIDType ;
    Message      : string ;
    Level        : AlertType := ERROR
  )</font> <font id="function_return">return ()</font>
**Description**
 Alert always goes to the transcript file
- Alert <font id="function_arguments">( Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- IncAlertCount <font id="function_arguments">(    A silent form of alert    AlertLogID   : AlertLogIDType ;
    Level        : AlertType := ERROR
  )</font> <font id="function_return">return ()</font>
- IncAlertCount <font id="function_arguments">( Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIf <font id="function_arguments">( AlertLogID : AlertLogIDType ; condition : boolean ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
Similar to assert, except condition is positive
- AlertIf <font id="function_arguments">( condition : boolean ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ; condition : boolean ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
Direct replacement for assert
- AlertIfNot <font id="function_arguments">( condition : boolean ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : std_logic ;         Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
overloading for common functionality
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : std_logic_vector ;  Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : unsigned ;          Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : signed ;            Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : integer ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : real ;              Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : character ;         Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : string ;            Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : time ;              Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : std_logic ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : std_logic_vector ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : unsigned ;         Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : signed ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : integer ;          Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : real ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : character ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : string ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfEqual <font id="function_arguments">( L, R : time ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : std_logic ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : std_logic_vector ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : unsigned ;         Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : signed ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : integer ;          Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : real ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : character ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : string ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ;  L, R : time ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : std_logic ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : std_logic_vector ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : unsigned ;         Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : signed ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : integer ;          Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : real ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : character ;        Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : string ;           Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfNotEqual <font id="function_arguments">( L, R : time ;             Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ; Name1, Name2 : string; Message : string := "" ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
Simple Diff for file comparisons
- AlertIfDiff <font id="function_arguments">(Name1, Name2 : string; Message : string := "" ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ; file File1, File2 : text; Message : string := "" ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AlertIfDiff <font id="function_arguments">(file File1, File2 : text; Message : string := "" ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(  
    AlertLogID       : AlertLogIDType ;
    condition        : boolean ;
    ReceivedMessage  : string ;
    ExpectedMessage  : string ;
    Enable           : boolean  := FALSE    override internal enable
  )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">( condition : boolean ; ReceivedMessage, ExpectedMessage : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(    AlertLogID   : AlertLogIDType ;
    condition    : boolean ;
    Message      : string ;
    Enable       : boolean := FALSE  override internal enable
  )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ; Message : string ;  Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ; condition : boolean ; ReceivedMessage, ExpectedMessage : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( condition : boolean ; ReceivedMessage, ExpectedMessage : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( AlertLogID : AlertLogIDType ; condition : boolean ; Message : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfNot <font id="function_arguments">( condition : boolean ; Message : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmPassed <font id="function_arguments">( AlertLogID : AlertLogIDType ; Message : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmPassed <font id="function_arguments">( Message : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmError <font id="function_arguments">( AlertLogID : AlertLogIDType ; Message : string )</font> <font id="function_return">return ()</font>
- AffirmError <font id="function_arguments">( Message : string )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : boolean ;  Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : std_logic ;  Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : std_logic_vector ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : unsigned ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : signed ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : integer ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : real ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : character ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : string ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( AlertLogID : AlertLogIDType ; Received, Expected : time ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : boolean ;  Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : std_logic ;  Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : std_logic_vector ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : unsigned ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : signed ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : integer ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : real ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : character ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : string ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfEqual <font id="function_arguments">( Received, Expected : time ; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ; Name1, Name2 : string; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(Name1, Name2 : string; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(AlertLogID : AlertLogIDType ; file File1, File2 : text; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIfDiff <font id="function_arguments">(file File1, File2 : text; Message : string := "" ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">( RequirementsIDName : string ; condition : boolean ; ReceivedMessage, ExpectedMessage : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
**Description**
Support for Specification / Requirements Tracking
- AffirmIf <font id="function_arguments">( RequirementsIDName : string ; condition : boolean ; Message : string ; Enable : boolean := FALSE )</font> <font id="function_return">return ()</font>
- SetAlertLogJustify <font id="function_arguments">(Enable : boolean := TRUE)</font> <font id="function_return">return ()</font>
- ReportAlerts <font id="function_arguments">( Name : String ; AlertCount : AlertCountType )</font> <font id="function_return">return ()</font>
- ReportRequirements <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ReportAlerts <font id="function_arguments">( Name : string := OSVVM_STRING_INIT_PARM_DETECT ; AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID ; ExternalErrors : AlertCountType := (others => 0) )</font> <font id="function_return">return ()</font>
- ReportNonZeroAlerts <font id="function_arguments">( Name : string := OSVVM_STRING_INIT_PARM_DETECT ; AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID ; ExternalErrors : AlertCountType := (others => 0) )</font> <font id="function_return">return ()</font>
- WriteTestSummary <font id="function_arguments">( FileName : string ; OpenKind : File_Open_Kind := APPEND_MODE )</font> <font id="function_return">return ()</font>
- WriteTestSummaries <font id="function_arguments">( FileName : string ; OpenKind : File_Open_Kind := WRITE_MODE )</font> <font id="function_return">return ()</font>
- ReportTestSummaries <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- WriteAlerts <font id="function_arguments">(    FileName    : string ;
    AlertLogID  : AlertLogIDType := ALERTLOG_BASE_ID ;
    OpenKind    : File_Open_Kind := WRITE_MODE
  )</font> <font id="function_return">return ()</font>
- WriteRequirements <font id="function_arguments">(    FileName        : string ;
    AlertLogID      : AlertLogIDType := REQUIREMENT_ALERTLOG_ID ;
    OpenKind        : File_Open_Kind := WRITE_MODE
  )</font> <font id="function_return">return ()</font>
- ReadSpecification <font id="function_arguments">(FileName : string ; PassedGoal : integer := -1)</font> <font id="function_return">return ()</font>
- ReadRequirements <font id="function_arguments">(    FileName        : string ;
    ThresholdPassed : boolean := FALSE 
  )</font> <font id="function_return">return ()</font>
- ReadTestSummaries <font id="function_arguments">(FileName : string)</font> <font id="function_return">return ()</font>
- ClearAlerts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ClearAlertStopCounts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- ClearAlertCounts <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- Log <font id="function_arguments">(    AlertLogID   : AlertLogIDType ;
    Message      : string ;
    Level        : LogType := ALWAYS ;
    Enable       : boolean := FALSE     override internal enable
  )</font> <font id="function_return">return ()</font>
**Description**
 log filtering for verbosity control, optionally has a separate file parameter
- Log <font id="function_arguments">( Message : string ; Level : LogType := ALWAYS ; Enable : boolean := FALSE)</font> <font id="function_return">return ()</font>
- SetAlertEnable <font id="function_arguments">(Level : AlertType ;  Enable : boolean)</font> <font id="function_return">return ()</font>
**Description**
Alert Enables
- SetAlertEnable <font id="function_arguments">(AlertLogID : AlertLogIDType ;  Level : AlertType ;  Enable : boolean ; DescendHierarchy : boolean := TRUE)</font> <font id="function_return">return ()</font>
- SetLogEnable <font id="function_arguments">(Level : LogType ;  Enable : boolean)</font> <font id="function_return">return ()</font>
**Description**
Log Enables
- SetLogEnable <font id="function_arguments">(AlertLogID : AlertLogIDType ;  Level : LogType ;  Enable : boolean ; DescendHierarchy : boolean := TRUE)</font> <font id="function_return">return ()</font>
- ReportLogEnables <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
same as GetLogEnable
- SetAlertLogName <font id="function_arguments">(Name : string )</font> <font id="function_return">return ()</font>
- DeallocateAlertLogStruct <font id="function_arguments">()</font> <font id="function_return">return ()</font>
**Description**
synthesis translate_on
- InitializeAlertLogStruct <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- SetPassedGoal <font id="function_arguments">(AlertLogID : AlertLogIDType ; PassedGoal : integer )</font> <font id="function_return">return ()</font>
- SetAlertLogPrefix <font id="function_arguments">(AlertLogID : AlertLogIDType; Name : string )</font> <font id="function_return">return ()</font>
- UnSetAlertLogPrefix <font id="function_arguments">(AlertLogID : AlertLogIDType)</font> <font id="function_return">return ()</font>
- SetAlertLogSuffix <font id="function_arguments">(AlertLogID : AlertLogIDType; Name : string )</font> <font id="function_return">return ()</font>
**Description**
synthesis translate_on
- UnSetAlertLogSuffix <font id="function_arguments">(AlertLogID : AlertLogIDType)</font> <font id="function_return">return ()</font>
- SetGlobalAlertEnable <font id="function_arguments">(A : boolean := TRUE)</font> <font id="function_return">return ()</font>
**Description**
Accessor Methods
- IncAffirmCount <font id="function_arguments">(AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID)</font> <font id="function_return">return ()</font>
- IncAffirmPassedCount <font id="function_arguments">(AlertLogID : AlertLogIDType := ALERTLOG_BASE_ID)</font> <font id="function_return">return ()</font>
- SetAlertStopCount <font id="function_arguments">(AlertLogID : AlertLogIDType ;  Level : AlertType ;  Count : integer)</font> <font id="function_return">return ()</font>
- SetAlertStopCount <font id="function_arguments">(Level : AlertType ;  Count : integer)</font> <font id="function_return">return ()</font>
- SetAlertLogOptions <font id="function_arguments">(    FailOnWarning            : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    FailOnDisabledErrors     : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    FailOnRequirementErrors  : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    ReportHierarchy          : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteAlertErrorCount     : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteAlertLevel          : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteAlertName           : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteAlertTime           : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteLogErrorCount       : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteLogLevel            : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteLogName             : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    WriteLogTime             : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    PrintPassed              : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    PrintAffirmations        : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    PrintDisabledAlerts      : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    PrintRequirements        : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    PrintIfHaveRequirements  : AlertLogOptionsType := OPT_INIT_PARM_DETECT ;
    DefaultPassedGoal        : integer             := integer'left ;
    AlertPrefix              : string := OSVVM_STRING_INIT_PARM_DETECT ;
    LogPrefix                : string := OSVVM_STRING_INIT_PARM_DETECT ;
    ReportPrefix             : string := OSVVM_STRING_INIT_PARM_DETECT ;
    DoneName                 : string := OSVVM_STRING_INIT_PARM_DETECT ;
    PassName                 : string := OSVVM_STRING_INIT_PARM_DETECT ;
    FailName                 : string := OSVVM_STRING_INIT_PARM_DETECT
  )</font> <font id="function_return">return ()</font>
- ReportAlertLogOptions <font id="function_arguments">()</font> <font id="function_return">return ()</font>
- IsLogEnableType <font id="function_arguments">(Name : String)</font> <font id="function_return">return boolean</font>
**Description**
File Reading Utilities
- ReadLogEnables <font id="function_arguments">(file AlertLogInitFile : text)</font> <font id="function_return">return ()</font>
- ReadLogEnables <font id="function_arguments">(FileName : string)</font> <font id="function_return">return ()</font>
- PathTail <font id="function_arguments">(A : string)</font> <font id="function_return">return string</font>
**Description**
String Helper Functions -- This should be in a more general string package
- MetaMatch <font id="function_arguments">(l, r : std_ulogic)</font> <font id="function_return">return boolean</font>
- MetaMatch <font id="function_arguments">(L, R : std_ulogic_vector)</font> <font id="function_return">return boolean</font>
- MetaMatch <font id="function_arguments">(L, R : unresolved_unsigned)</font> <font id="function_return">return boolean</font>
- MetaMatch <font id="function_arguments">(L, R : unresolved_signed)</font> <font id="function_return">return boolean</font>
- AlertIf <font id="function_arguments">( condition : boolean ; AlertLogID : AlertLogIDType ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
deprecated
- AlertIfNot <font id="function_arguments">( condition : boolean ; AlertLogID : AlertLogIDType ; Message : string ; Level : AlertType := ERROR )</font> <font id="function_return">return ()</font>
**Description**
deprecated
- AffirmIf <font id="function_arguments">(    AlertLogID   : AlertLogIDType ;
    condition    : boolean ;
    Message      : string ;
    LogLevel     : LogType  ;   := PASSED
    AlertLevel   : AlertType := ERROR
  )</font> <font id="function_return">return ()</font>
**Description**
deprecated
- AffirmIf <font id="function_arguments">( AlertLogID : AlertLogIDType ; condition : boolean ; Message : string ; AlertLevel : AlertType )</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ; Message : string ;  LogLevel : LogType  ; AlertLevel : AlertType := ERROR)</font> <font id="function_return">return ()</font>
- AffirmIf <font id="function_arguments">(condition : boolean ; Message : string ;  AlertLevel : AlertType )</font> <font id="function_return">return ()</font>
