## Standard types

### int
Integer value.
```freefem
int i = 0;
```

### bool
Boolean value.
```freefem
bool b = true;
```

### real
Real value (C double precision).
```freefem
real r = 0.;
```

### complex
Complex value (two C double precision).
```freefem
complex c = 0.+1i;
```
The imaginary number $i$ is defined as `1i`

### string
String value.
```freefem
string s = "this is a string";
```


## Mesh design

### border
Border type.
```freefem
border b(t=0., 1.){x=cos(2.*pi*t); y=sin(2.*pi*t); label=1;};
```
Define the 2D geometrical border in parametric coordinates.

### mesh
2D Mesh type
```freefem
mesh Th;
```

### mesh3
3D mesh type
```freefem
mesh3 Th;
```


## Finite element space design

### fespace
Finite element space type.
```freefem
fespace Uh(Th, P1);
fespace UPh(Th, [P2, P2, P1]);
```
A finite element space is based on a mesh (`Th`) with an element definition, scalar (`P1`) or vector (`[P2, P2, P1]`).


**Available finite element space:**

Generic:

 - P0 / P03d
 - P0Edge
 - P1 / P13d
 - P1dc
 - P1b / P1b3d
 - P1bl / P1bl3d
 - P1nc
 - P2 / P23d
 - P2b
 - P2dc
 - RT0 / RT03d
 - RT0Ortho
 - Edge03d

Using _Element_P3_:

 - P3

Using _Element_P3dc_:

 - P3d

Using _Element_P4_:

 - P4

Using _Element_P4dc_:

 - P4dc

Using _Element_PkEdge_:

 - P1Edge
 - P2Edge
 - P3Edge
 - P4Edge
 - P5Edge

Using _Morlay_:

 - P2Morley

Using _HCT_:

 - HCT

Using _BernardiRaugel_:

 - P2BR

Using _Element_Mixte_:

 - RT1
 - RT1Ortho
 - BDM1
 - BDM1Ortho

Using _Element_Mixte3d_:

 - Edge13D
 - Edge23D

Using _Element_QF_:

 - FEQF

A finite element variable is defined as follow:
```freefem
fespace Uh(Th, P1);
Uh u;

fespace UPh(Th, [P2, P2, P1]);
UPh [Ux, Uy, p];
```

## Macro design

### macro
Macro type.
```freefem
macro grad(u) [dx(u), dy(u)] //
```
Macro ends with `//`.

You can use the C concatenation operator ## inside a macro using #.
> If Ux and Uy are defined:
```freefem
macro Grad(U) [grad(U#x), grad(U#y)] //
```


## Functions design

### func
Function type.

Function without parameters ($x$, $y$ and $z$ are implicitly considered):
```freefem
func f = x^2 + y^2;
```

Function with parameters:
```freefem
func real f (real var){
	return x^2 + y^2 + var^2;
}
```


## Problem design

### problem
Problem type.
```freefem
problem Laplacian (u, uh) = ...
```
FreeFem++ needs the variational form in the problem definition.

In order to solve the problem, just call:
```freefem
Laplacian;
```

### solve
Solve type.

Identical to problem but automatically solved.

### varf
Variational form type.
```freefem
varf vLaplacian (u, uh) = ...
```
This is the other way to define a problem in order to directly manage matrix and right hang side.


## Array

Array can be defined using types: int, bool, real, complex, string, ...

### Array index
Array index can be int or string:
```freefem
real[int] Ai = [1, 1, 0, 0];
real[string] As = [1, 1, 0, 0];
```

### Array size
The size of an array is obtained using the keyword `n`:
```freefem
int ArraySize = Ai.n;
```

### Double array
A double array (matrix) can be defined using two indexes:
```freefem
real[int, int] Aii = [[1, 1], [0, 0]];
```
The two sizes are obtained using the keywords `n` and `m`:
```freefem
int ArraySize1 = Aii.n;
int ArraySize2 = Aii.m;
```


## Matrix
Matrices can be defined using a variational form type:
```freefem
matrix Laplacian = vLaplacian(Uh, Uh);
```
Matrices are designed using templates, so they can be real or complex:
```freefem
matrix<real> A = ...
matrix<complex> Ai = ...
```

The diagonal of the matrix is obtained using:
```freefem
real[int] Aii = A.diag;
```