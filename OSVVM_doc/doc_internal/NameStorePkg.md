# Package: NameStorePkg

- **File**: NameStorePkg.vhd
## Constants

| Name         | Type       | Value       | Description |
| ------------ | ---------- | ----------- | ----------- |
| ID_NOT_FOUND | NameIDType |  (ID => -1) |             |
## Types

| Name            | Type                                    | Description |
| --------------- | --------------------------------------- | ----------- |
| NameIDType      |                                         |             |
| NameIDArrayType | array (integer range <>) of NameIDType  |             |
| NameStorePType  |                                         |             |
## Functions
- Set <font id="function_arguments">(ID : NameIDType ;<br><span style="padding-left:20px"> NameIn : String) </font> <font id="function_return">return ()</font>
**Description**
 impure function NewID     (NameIn : String ; Size : positive ) return NameStoreIDArrayType ;
- Clear <font id="function_arguments">(ID : NameIDType) </font> <font id="function_return">return ()</font>
**Description**
clear name
- Deallocate <font id="function_arguments">(ID : NameIDType) </font> <font id="function_return">return ()</font>
**Description**
effectively alias to clear name
