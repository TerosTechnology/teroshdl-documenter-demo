# Package: MATH_COMPLEX

- **File**: math_complex.vhdl
## Constants

| Name            | Type    | Value                                                   | Description                 |
| --------------- | ------- | ------------------------------------------------------- | --------------------------- |
| CopyRightNotice | STRING  |  "Copyright 2008 IEEE. All rights reserved."            |                             |
| MATH_CBASE_1    | COMPLEX |  COMPLEX'(1.0,<br><span style="padding-left:20px"> 0.0) |   Constant Definitions<br>  |
| MATH_CBASE_J    | COMPLEX |  COMPLEX'(0.0,<br><span style="padding-left:20px"> 1.0) |                             |
| MATH_CZERO      | COMPLEX |  COMPLEX'(0.0,<br><span style="padding-left:20px"> 0.0) |                             |
## Types

| Name          | Type | Description             |
| ------------- | ---- | ----------------------- |
| COMPLEX       |      |   Type Definitions<br>  |
| COMPLEX_POLAR |      |                         |
## Functions
- CMPLX <font id="function_arguments">(X : in REAL;<br><span style="padding-left:20px"> Y : in REAL := 0.0) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns TRUE if L is not equal to R and returns FALSE
         otherwise
 Special values:
         COMPLEX_POLAR'(0.0, X) /= COMPLEX_POLAR'(0.0, Y) returns
         FALSE regardless of the value of X and Y.
 Domain:
         L in COMPLEX_POLAR and L.ARG /= -MATH_PI
         R in COMPLEX_POLAR and R.ARG /= -MATH_PI
 Error conditions:
         Error if L.ARG = -MATH_PI
         Error if R.ARG = -MATH_PI
 Range:
         "/="(L,R) is either TRUE or FALSE
 Notes:
         None

 Function Declarations


- GET_PRINCIPAL_VALUE <font id="function_arguments">(X : in REAL) </font> <font id="function_return">return PRINCIPAL_VALUE </font>
**Description**
 Purpose:
         Returns COMPLEX number X + iY
 Special values:
         None
 Domain:
         X in REAL
         Y in REAL
 Error conditions:
         None
 Range:
         CMPLX(X,Y) is mathematically unbounded
 Notes:
         None

- COMPLEX_TO_POLAR <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns principal value of angle X; X in radians
 Special values:
         None
 Domain:
         X in REAL
 Error conditions:
         None
 Range:
         -MATH_PI < GET_PRINCIPAL_VALUE(X) <= MATH_PI
 Notes:
         None

- POLAR_TO_COMPLEX <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value COMPLEX_POLAR of Z
 Special values:
         COMPLEX_TO_POLAR(MATH_CZERO) = COMPLEX_POLAR'(0.0, 0.0)
         COMPLEX_TO_POLAR(Z) = COMPLEX_POLAR'(ABS(Z.IM),
                              SIGN(Z.IM)*MATH_PI_OVER_2) if Z.RE = 0.0
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- ARG <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return PRINCIPAL_VALUE </font>
**Description**
 Purpose:
         Returns absolute value (magnitude) of Z
 Special values:
         None
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         ABS(Z) >= 0.0
 Notes:
         ABS(Z) = Z.MAG

- ARG <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return PRINCIPAL_VALUE </font>
**Description**
 Purpose:
         Returns argument (angle) in radians of the principal
         value of Z
 Special values:
         ARG(Z) = 0.0 if Z.RE >= 0.0 and Z.IM = 0.0
         ARG(Z) = SIGN(Z.IM)*MATH_PI_OVER_2 if Z.RE = 0.0
         ARG(Z) = MATH_PI if Z.RE < 0.0        and Z.IM = 0.0
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         -MATH_PI < ARG(Z) <= MATH_PI
 Notes:
         ARG(Z) = ARCTAN(Z.IM, Z.RE)

- CONJ <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of unary minus of Z
 Special values:
         "-"(Z) = COMPLEX_POLAR'(Z.MAG, MATH_PI) if Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         Returns COMPLEX_POLAR'(Z.MAG, Z.ARG - SIGN(Z.ARG)*MATH_PI) if
                Z.ARG /= 0.0

- CONJ <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns complex conjugate of Z
 Special values:
         None
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         CONJ(Z) is mathematically unbounded
 Notes:
         Returns x -jy for Z= x + jy

- SQRT <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of complex conjugate of Z
 Special values:
         CONJ(Z) = COMPLEX_POLAR'(Z.MAG, MATH_PI) if Z.ARG = MATH_PI
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         Returns COMPLEX_POLAR'(Z.MAG, -Z.ARG) if Z.ARG /= MATH_PI

- SQRT <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns square root of Z with positive real part
         or, if the real part is zero, the one with nonnegative
         imaginary part
 Special values:
         SQRT(MATH_CZERO) = MATH_CZERO
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         SQRT(Z) is mathematically unbounded
 Notes:
         None

- EXP <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns square root of Z with positive real part
         or, if the real part is zero, the one with nonnegative
         imaginary part
 Special values:
         SQRT(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- EXP <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns exponential of Z
 Special values:
         EXP(MATH_CZERO) = MATH_CBASE_1
         EXP(Z) = -MATH_CBASE_1 if Z.RE = 0.0 and ABS(Z.IM) = MATH_PI
         EXP(Z) = SIGN(Z.IM)*MATH_CBASE_J if Z.RE = 0.0 and
                                          ABS(Z.IM) =  MATH_PI_OVER_2
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         EXP(Z) is mathematically unbounded
 Notes:
         None

- LOG <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of exponential of Z
 Special values:
         EXP(Z) = COMPLEX_POLAR'(1.0, 0.0) if Z.MAG =0.0 and
                                                        Z.ARG = 0.0
         EXP(Z) = COMPLEX_POLAR'(1.0, MATH_PI) if Z.MAG = MATH_PI and
                                        ABS(Z.ARG) = MATH_PI_OVER_2
         EXP(Z) = COMPLEX_POLAR'(1.0, MATH_PI_OVER_2) if
                                        Z.MAG = MATH_PI_OVER_2 and
                                        Z.ARG = MATH_PI_OVER_2
         EXP(Z) = COMPLEX_POLAR'(1.0, -MATH_PI_OVER_2) if
                                        Z.MAG = MATH_PI_OVER_2 and
                                        Z.ARG = -MATH_PI_OVER_2
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- LOG2 <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns natural logarithm of Z
 Special values:
         LOG(MATH_CBASE_1) = MATH_CZERO
         LOG(-MATH_CBASE_1) = COMPLEX'(0.0, MATH_PI)
         LOG(MATH_CBASE_J) = COMPLEX'(0.0, MATH_PI_OVER_2)
         LOG(-MATH_CBASE_J) = COMPLEX'(0.0, -MATH_PI_OVER_2)
         LOG(Z) = MATH_CBASE_1 if Z = COMPLEX'(MATH_E, 0.0)
 Domain:
         Z in COMPLEX and ABS(Z) /= 0.0
 Error conditions:
         Error if ABS(Z) = 0.0
 Range:
         LOG(Z) is mathematically unbounded
 Notes:
         None

- LOG10 <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns logarithm base 2 of Z
 Special values:
         LOG2(MATH_CBASE_1) = MATH_CZERO
         LOG2(Z) = MATH_CBASE_1 if Z = COMPLEX'(2.0, 0.0)
 Domain:
         Z in COMPLEX and ABS(Z) /= 0.0
 Error conditions:
         Error if ABS(Z) = 0.0
 Range:
         LOG2(Z) is mathematically unbounded
 Notes:
         None

- LOG <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns logarithm base 10 of Z
 Special values:
         LOG10(MATH_CBASE_1) = MATH_CZERO
         LOG10(Z) = MATH_CBASE_1 if Z = COMPLEX'(10.0, 0.0)
 Domain:
         Z in COMPLEX and ABS(Z) /= 0.0
 Error conditions:
         Error if ABS(Z) = 0.0
 Range:
         LOG10(Z) is mathematically unbounded
 Notes:
         None

- LOG2 <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns principal value of natural logarithm of Z
 Special values:
         LOG(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 1.0 and
                                             Z.ARG = 0.0
         LOG(Z) = COMPLEX_POLAR'(MATH_PI, MATH_PI_OVER_2) if
                              Z.MAG = 1.0 and Z.ARG = MATH_PI
         LOG(Z) = COMPLEX_POLAR'(MATH_PI_OVER_2, MATH_PI_OVER_2) if
                              Z.MAG = 1.0 and  Z.ARG = MATH_PI_OVER_2
         LOG(Z) = COMPLEX_POLAR'(MATH_PI_OVER_2, -MATH_PI_OVER_2) if
                              Z.MAG = 1.0 and  Z.ARG = -MATH_PI_OVER_2
         LOG(Z) = COMPLEX_POLAR'(1.0, 0.0) if Z.MAG = MATH_E and
                                             Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
         Z.MAG /= 0.0
 Error conditions:
         Error if Z.ARG = -MATH_PI
         Error if Z.MAG = 0.0
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- LOG10 <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns principal value of logarithm base 2 of Z
 Special values:
         LOG2(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 1.0 and
                                              Z.ARG = 0.0
         LOG2(Z) = COMPLEX_POLAR'(1.0, 0.0) if Z.MAG = 2.0 and
                                             Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
         Z.MAG /= 0.0
 Error conditions:
         Error if Z.ARG = -MATH_PI
         Error if Z.MAG = 0.0
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
        None

- LOG <font id="function_arguments">(Z : in COMPLEX;<br><span style="padding-left:20px"> BASE : in REAL) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of logarithm base 10 of Z
 Special values:
         LOG10(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 1.0 and
                                               Z.ARG = 0.0
         LOG10(Z) = COMPLEX_POLAR'(1.0, 0.0) if Z.MAG = 10.0 and
                                               Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
         Z.MAG /= 0.0
 Error conditions:
         Error if Z.ARG = -MATH_PI
         Error if Z.MAG = 0.0
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- LOG <font id="function_arguments">(Z : in COMPLEX_POLAR;<br><span style="padding-left:20px"> BASE : in REAL) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns logarithm base BASE of Z
 Special values:
         LOG(MATH_CBASE_1, BASE) = MATH_CZERO
         LOG(Z,BASE) = MATH_CBASE_1 if Z = COMPLEX'(BASE, 0.0)
 Domain:
         Z in COMPLEX and ABS(Z) /= 0.0
         BASE > 0.0
         BASE /= 1.0
 Error conditions:
         Error if ABS(Z) = 0.0
         Error if BASE <= 0.0
         Error if BASE = 1.0
 Range:
         LOG(Z,BASE) is mathematically unbounded
 Notes:
         None

- SIN <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of logarithm base BASE of Z
 Special values:
         LOG(Z, BASE) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 1.0 and
                                                Z.ARG = 0.0
         LOG(Z, BASE) = COMPLEX_POLAR'(1.0, 0.0) if Z.MAG = BASE and
                                                Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
         Z.MAG /= 0.0
         BASE > 0.0
         BASE /= 1.0
 Error conditions:
         Error if Z.ARG = -MATH_PI
         Error if Z.MAG = 0.0
         Error if BASE <= 0.0
         Error if BASE = 1.0
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- SIN <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns sine of Z
 Special values:
         SIN(MATH_CZERO) = MATH_CZERO
         SIN(Z) = MATH_CZERO if Z = COMPLEX'(MATH_PI, 0.0)
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         ABS(SIN(Z)) <= SQRT(SIN(Z.RE)*SIN(Z.RE) +
                                         SINH(Z.IM)*SINH(Z.IM))
 Notes:
         None

- COS <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of sine of Z
 Special values:
         SIN(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 0.0 and
                                            Z.ARG = 0.0
         SIN(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = MATH_PI and
                                            Z.ARG = 0.0
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- COS <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns cosine of Z
 Special values:
         COS(Z) = MATH_CZERO if Z = COMPLEX'(MATH_PI_OVER_2, 0.0)
         COS(Z) = MATH_CZERO if Z = COMPLEX'(-MATH_PI_OVER_2, 0.0)
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         ABS(COS(Z)) <= SQRT(COS(Z.RE)*COS(Z.RE) +
                                         SINH(Z.IM)*SINH(Z.IM))
 Notes:
         None

- SINH <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of cosine of Z
 Special values:
         COS(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = MATH_PI_OVER_2
                                               and Z.ARG = 0.0
         COS(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = MATH_PI_OVER_2
                                               and Z.ARG = MATH_PI
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- SINH <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns hyperbolic sine of Z
 Special values:
         SINH(MATH_CZERO) = MATH_CZERO
         SINH(Z) = MATH_CZERO if Z.RE = 0.0 and Z.IM = MATH_PI
         SINH(Z) = MATH_CBASE_J if Z.RE = 0.0 and
                                               Z.IM = MATH_PI_OVER_2
         SINH(Z) = -MATH_CBASE_J if Z.RE = 0.0 and
                                               Z.IM = -MATH_PI_OVER_2
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         ABS(SINH(Z)) <= SQRT(SINH(Z.RE)*SINH(Z.RE) +
                                         SIN(Z.IM)*SIN(Z.IM))
 Notes:
         None

- COSH <font id="function_arguments">(Z : in COMPLEX) </font> <font id="function_return">return COMPLEX </font>
**Description**
 Purpose:
         Returns principal value of hyperbolic sine of Z
 Special values:
         SINH(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = 0.0 and
                                            Z.ARG = 0.0
         SINH(Z) = COMPLEX_POLAR'(0.0, 0.0) if Z.MAG = MATH_PI and
                                            Z.ARG = MATH_PI_OVER_2
         SINH(Z) = COMPLEX_POLAR'(1.0, MATH_PI_OVER_2) if Z.MAG =
                         MATH_PI_OVER_2 and Z.ARG = MATH_PI_OVER_2
         SINH(Z) = COMPLEX_POLAR'(1.0, -MATH_PI_OVER_2) if Z.MAG =
                         MATH_PI_OVER_2 and Z.ARG = -MATH_PI_OVER_2
 Domain:
         Z in COMPLEX_POLAR and Z.ARG /= -MATH_PI
 Error conditions:
         Error if Z.ARG = -MATH_PI
 Range:
         result.MAG >= 0.0
         -MATH_PI < result.ARG <= MATH_PI
 Notes:
         None

- COSH <font id="function_arguments">(Z : in COMPLEX_POLAR) </font> <font id="function_return">return COMPLEX_POLAR </font>
**Description**
 Purpose:
         Returns hyperbolic cosine of Z
 Special values:
         COSH(MATH_CZERO) = MATH_CBASE_1
         COSH(Z) = -MATH_CBASE_1 if Z.RE = 0.0 and Z.IM = MATH_PI
         COSH(Z) = MATH_CZERO if Z.RE = 0.0 and Z.IM = MATH_PI_OVER_2
         COSH(Z) = MATH_CZERO if Z.RE = 0.0 and Z.IM = -MATH_PI_OVER_2
 Domain:
         Z in COMPLEX
 Error conditions:
         None
 Range:
         ABS(COSH(Z)) <= SQRT(SINH(Z.RE)*SINH(Z.RE) +
                                         COS(Z.IM)*COS(Z.IM))
 Notes:
         None

