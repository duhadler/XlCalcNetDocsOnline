

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />



|newpage|

Standard decompositions and linear solving
===================================================================



Cholesky Decomposition with Pivoting
--------------------------------------------------


.. method:: mat.CholeskyLDLT(Query, matB)


    Returns the Cholesky decomposition of the symmetric matrix *matA* `=A = A = P^TLDLP`, with partial pivoting.
    See also Eigen :cite:p:`EigenMat117`,  Wikipedia :cite:p:`WikipediaMat117`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`





**Results:**

:info:     An integer indicating whether the decomposition was successful (=0) or not(=1).

:ispos:     An integer indicating whether the matrix A is semidefinit positve (=0) or not(=1).

:isneg:     An integer indicating whether the matrix A is semidefinit negative (=0) or not(=1).

:det:     A scalar of a return type matching `A`. The determinant of `A`.

:rcond:     A scalar of the same return type as det. The condition number of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.

:P:     A square matrix of the same type and dimension as `A`. The permutation matrix `P` in the decomposition `A = P^TLDLP`.

:L:     A square matrix of the same type and dimension as `A`, containing the matrix `L` in the decomposition `A = P^TLDLP`.

:D:     A square matrix of the same type and dimension as `A`, containing the matrix `D` in the decomposition `A = P^TLDLP`.




Perform a robust Cholesky decomposition of a positive semidefinite or negative semidefinite matrix such that
`A = P^TLDLP`, where P is a permutation matrix, L is lower triangular with a unit diagonal and D is a diagonal
matrix.
The decomposition uses pivoting to ensure stability, so that L will have zeros in the bottom right rank(A) - n
submatrix. Avoiding the square root on D also stabilizes the computation.
Remember that Cholesky decompositions are not rank-revealing. Also, do not use a Cholesky decomposition to
determine whether a system of equations has a solution

rankUpdate: Update the LDLT decomposition: given `A = LDLT` , efficiently compute the decomposition of `A + \sigma w w^T.`  
Parameters: `w` a vector to be incorporated into the decomposition. `\sigma` a scalar, +1 for updates and -1 for
"downdates", which correspond to removing previously-added column vectors. Optional; default value is +1.

solve: Returns a solution x of `Ax = b` using the current decomposition of `A`. This function also supports in-place solves using the syntax x = decompositionObject.solve(x) .

This method just tries to find as good a solution as possible. If you want to check whether a solution exists
or if it is accurate, just call this function to get a result and then compute the error of this result, or use
MatrixBase::isApprox() directly, for instance like this:

bool a solution exists = (A*result).isApprox(b, precision);

This method avoids dividing by zero, so that the non-existence of a solution does not by itself mean that you will get inf or nan values.

More precisely, this method solves `Ax = b` using the decomposition `A = P^TLDL*P` by solving the systems 

`P^T y1 = b, LY2 = y1, Dy3 = y2, L*y4 = y3` and `Px = y4` in succession. 

If the matrix A is singular, then D will also be singular (all the other matrices are invertible). In that case, the least-square solution of `Dy3 = y2` is computed. This does not mean that this function computes the least-square solution of `Ax = b` if A is singular.



Example for a real symmetric matrix
........................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")

    >>> # This needs to be a positive definite matrix
    A: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "ispos, isneg, info, rcond, L, U, D, P, X, Inverse"
    >>> Res = A.eigen_ldlt2(Query, B)
    >>> print("Info : ", Res["Info"])
    Info :  0
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.00736220456231950672450648838163673064
    >>> print("Ispos: ", Res["Ispos"])
    Ispos:  False
    >>> print("Isneg: ", Res["Isneg"])
    Isneg:  False

    >>> Res["X"].show("X")
    X: 
     -7.46,  -7.47,  -7.48,  -7.48,  -7.49,  -7.50, 
     -4.07,  -4.07,  -4.08,  -4.08,  -4.09,  -4.09, 
     -25.5,  -25.5,  -25.6,  -25.6,  -25.6,  -25.6, 
    -0.158, -0.158, -0.158, -0.158, -0.158, -0.158, 
      54.5,   54.5,   54.6,   54.6,   54.7,   54.7, 
      19.3,   19.3,   19.3,   19.3,   19.4,   19.4, 

    >>> (A * Res["X"]).show("A * X")
    A * X: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["x"]).show("B - A * X")
    B - A * X: 
           0,        0,   -2E-32,   -1E-32,   -1E-32,    1E-32, 
     1.6E-32,    4E-33,    9E-33,   -9E-33,  2.0E-32,  2.4E-32, 
     1.7E-32,  1.3E-32,    6E-33, -1.0E-32,  2.5E-32,    8E-33, 
      -2E-32,   -1E-32,   -3E-32,   -3E-32,   -1E-32,   -2E-32, 
      -2E-33,   -3E-33,        0,   -8E-33,    6E-33,    4E-33, 
       2E-33,  1.4E-32, -1.4E-32,   -9E-33,  1.1E-32,    5E-33, 

    >>> Res["P"].T.show("P^T")
    P^T: 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 0, 1, 
    0, 0, 1, 0, 0, 0, 
    0, 1, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    1, 0, 0, 0, 0, 0, 

    >>> Res["L"].show("L")
    L: 
          1,       0,       0,       0,       0,       0, 
       1.03,       1,       0,       0,       0,       0, 
      0.314,   -2.21,       1,       0,       0,       0, 
      0.729,   0.623, -0.0271,       1,       0,       0, 
      0.145,   -1.05,   0.580,   0.362,       1,       0, 
      0.548,   -1.84,   0.805,   -3.59,   0.514,       1, 

    >>> Res["D"].show("D")
    D: 
     85.0,     0,     0,     0,     0,     0, 
        0, -25.6,     0,     0,     0,     0, 
        0,     0,   172,     0,     0,     0, 
        0,     0,     0,  9.46,     0,     0, 
        0,     0,     0,     0,  6.99,     0, 
        0,     0,     0,     0,     0,  -150, 

    >>> Res["U"].show("U")
    U: 
          1,    1.03,   0.314,   0.729,   0.145,   0.548, 
          0,       1,   -2.21,   0.623,   -1.05,   -1.84, 
          0,       0,       1, -0.0271,   0.580,   0.805, 
          0,       0,       0,       1,   0.362,   -3.59, 
          0,       0,       0,       0,       1,   0.514, 
          0,       0,       0,       0,       0,       1, 

    >>> Res["P"].show("P")
    P: 
    0, 0, 0, 0, 0, 1, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 1, 0, 0, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 1, 0, 0, 0, 0, 

    >>> (A - Res["P"].T * Res["L"]  * Res["D"] * Res["U"] * Res["P"]).show("A - P^T * L * D * U * P")
    A - P^T * L * D * U * P: 
         0,      0,      0,      0,      0,      0, 
         0,      0, -1E-34, -1E-34, -1E-34,      0, 
         0,      0,      0, -1E-34,  1E-34,      0, 
         0, -1E-34, -1E-34,      0,      0,  3E-34, 
         0,      0,  2E-34,      0,      0,      0, 
         0,      0,      0,  3E-34,      0,      0, 

    >>> Res["Inverse"].show("Inverse")
    Inverse: 
      0.0293,  -0.0252,   0.0436, -0.00894,  -0.0389, -0.00643, 
     -0.0252, -0.00666,  0.00269,   0.0130,  0.00342,  0.00733, 
      0.0436,  0.00269,   0.0547,  0.00851,  -0.0859,  -0.0468, 
    -0.00894,   0.0130,  0.00851, -0.00235,  -0.0109, 0.000736, 
     -0.0389,  0.00342,  -0.0859,  -0.0109,    0.141,   0.0442, 
    -0.00643,  0.00733,  -0.0468, 0.000736,   0.0442,   0.0200, 

    >>> (A * Res["Inverse"]).show("A * Inverse")
    A * Inverse: 
         1.00,    -5E-36,     1E-35,   1.1E-36,     2E-35,    -1E-35, 
      1.1E-35,      1.00,     2E-35,  -4.9E-36,    -6E-35,   1.1E-35, 
      3.9E-35,    -1E-36,      1.00,  -2.1E-36,  -1.0E-34,  -2.1E-35, 
     -2.8E-35,    -1E-36,    -2E-35,      1.00,     5E-35,     1E-35, 
     2.16E-35,   1.6E-36,   2.5E-35, -5.17E-36,      1.00,  -1.2E-35, 
       -1E-36,     5E-36,         0,  -1.6E-36,    -1E-35,      1.00, 





Example for a hermitian matrix
........................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be a self-adjoint, positive definite matrix
    A: 
       91.0 + 0j, 12.0 - 3.60j, 22.0 - 7.40j, 14.0 + 1.10j, 
    12.0 + 3.60j,    77.0 + 0j, 2.50 - 2.00j, 3.40 - 7.60j, 
    22.0 + 7.40j, 2.50 + 2.00j,    91.0 + 0j, 17.0 + 3.70j, 
    14.0 - 1.10j, 3.40 + 7.60j, 17.0 - 3.70j,    74.0 + 0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Query = "ispos, isneg, info, rcond, L, U, D, P, X, Inverse"
    >>> Res = A.eigen_ldlt2(Query, B)
    >>> print("Info : ", Res["Info"])
    Info :  0 + 0j
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.415203875955925693806099488262499569 + 0j
    >>> print("Ispos: ", Res["Ispos"])
    Ispos:  False
    >>> print("Isneg: ", Res["Isneg"])
    Isneg:  False

    >>> Res["X"].show("X")
    X: 
        0.376 - 0.0288j,     -0.222 + 0.281j,   -0.0865 + 0.0417j,      0.229 + 0.303j, 
        0.0290 + 0.383j,      0.511 + 0.498j,      0.227 + 0.583j,      0.309 + 0.210j, 
        0.219 - 0.0602j,      0.535 + 0.463j,    0.527 - 0.00173j,      0.288 + 0.417j, 
         0.379 + 0.583j, 0.000510 + 0.00479j,      0.214 + 0.481j,     0.170 + 0.0528j, 

    >>> (A * Res["X"]).show("A * X")
    A * X: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> (B - A * Res["x"]).show("B - A * X")
    B - A * X: 
            0 - 5.00E-35j,        -1.80E-34 + 0j,                0 + 0j,                0 + 0j, 
                   0 + 0j, -1.00E-34 - 1.00E-34j,         0 - 2.00E-34j,         0 - 1.00E-34j, 
                   0 + 0j,         0 - 1.00E-34j,                0 + 0j,                0 + 0j, 
    -1.00E-34 + 1.00E-34j,        -1.00E-35 + 0j,         0 - 1.00E-34j, -1.00E-34 - 1.00E-34j, 

    >>> Res["P"].T.show("P^T")
    P^T: 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 

    >>> Res["L"].show("L")
    L: 
             1.00 + 0j,             0 + 0j,             0 + 0j,             0 + 0j, 
       0.242 + 0.0813j,          1.00 + 0j,             0 + 0j,             0 + 0j, 
       0.132 + 0.0396j, -0.00815 - 0.0223j,          1.00 + 0j,             0 + 0j, 
       0.154 - 0.0121j,    0.161 - 0.0270j,    0.0220 + 0.106j,          1.00 + 0j, 

    >>> Res["D"].show("D")
    D: 
    91.0 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j, 85.1 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j, 75.2 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 68.7 + 0j, 

    >>> Res["U"].show("U")
    U: 
             1.00 + 0j,    0.242 - 0.0813j,    0.132 - 0.0396j,    0.154 + 0.0121j, 
                0 + 0j,          1.00 + 0j, -0.00815 + 0.0223j,    0.161 + 0.0270j, 
                0 + 0j,             0 + 0j,          1.00 + 0j,    0.0220 - 0.106j, 
                0 + 0j,             0 + 0j,             0 + 0j,          1.00 + 0j, 

    >>> Res["P"].show("P")
    P: 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 

    >>> (A - Res["P"].T * Res["L"]  * Res["D"] * Res["U"] * Res["P"]).show("A - P^T * L * D * U * P")
    A - P^T * L * D * U * P: 
           0 + 0j,        0 + 0j,        0 + 0j,        0 + 0j, 
           0 + 0j,        0 + 0j, 0 + 1.00E-35j, 0 + 2.00E-35j, 
           0 + 0j,        0 + 0j,        0 + 0j,        0 + 0j, 
           0 + 0j, 0 - 2.00E-35j,        0 + 0j,        0 + 0j, 

    >>> Res["Inverse"].show("Inverse")
    Inverse: 
       0.0122 - 1.00E-39j,  -0.00177 + 0.000794j,  -0.00259 + 0.000957j,  -0.00167 - 0.000490j, 
     -0.00177 - 0.000794j,    0.0135 - 1.00E-40j, 0.000120 + 0.0000425j,  -0.000321 + 0.00154j, 
     -0.00259 - 0.000957j, 0.000120 - 0.0000425j,    0.0121 + 2.60E-40j,  -0.00231 - 0.000373j, 
     -0.00167 + 0.000490j,  -0.000321 - 0.00154j,  -0.00231 + 0.000373j,           0.0146 + 0j, 

    >>> (A * Res["Inverse"]).show("A * Inverse")
    A * Inverse: 
         1.00 - 1.20E-37j,  1.03E-36 - 2.00E-37j, -8.00E-37 + 1.30E-37j,                0 + 0j, 
           -3.90E-37 + 0j,             1.00 + 0j,         6.00E-38 + 0j, -2.00E-37 + 1.00E-36j, 
    -8.00E-37 - 1.00E-38j,  7.00E-38 - 1.00E-37j,      1.00 + 6.00E-38j,         1.00E-36 + 0j, 
     1.00E-36 + 1.00E-37j,         0 + 1.00E-36j,         1.00E-36 + 0j,      1.00 - 5.00E-38j, 






|newpage|


LU Decomposition with partial Pivoting
----------------------------------------------


.. method:: mat.PartialPivLU(Query, matB)


    Returns the LU decomposition of the general square matrix *matA* `= A = PLU`, with partial pivoting.

    See also Eigen :cite:p:`EigenMat107`,  Wikipedia :cite:p:`WikipediaMat107`,  Wikipedia :cite:p:`WikipediaMat130`.





**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`





**Results:**

:det:     A scalar of a return type matching `A`. The determinant of `A`.

:rcond:     A scalar of the same return type as det. The condition number of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.

:P:     A square matrix of the same type and dimension as `A`. The permutation matrix `P` in the decomposition `A = PLU`.

:LU:     A square matrix of the same type and dimension as `A`, containing the matrices `L` and `U` in the decomposition `A = PLU`.




This class represents a LU decomposition of a square invertible matrix, with partial pivoting: the matrix A is
decomposed as A = PLU where L is unit-lower-triangular, U is upper-triangular, and P is a permutation matrix.

Typically, partial pivoting LU decomposition is only considered numerically stable for square invertible matrices.
Thus LAPACK's dgesv and dgesvx require the matrix to be square and invertible. The present class does the
same. It will assert that the matrix is square, but it won’t (actually it cannot) check that the matrix is invertible:
it is your task to check that you only use this decomposition on invertible matrices.
The guaranteed safe alternative, working for all matrices, is the full pivoting LU decomposition, provided by class
FullPivLU.

This is not a rank-revealing LU decomposition. Many features are intentionally absent from this class, such as
rank computation. If you need these features, use class FullPivLU.

This LU decomposition is suitable to invert invertible matrices. It is what MatrixBase::inverse() uses in the general
case. On the other hand, it is not suitable to determine whether a given matrix is invertible.
The data of the LU decomposition can be directly accessed through the methods matrixLU(), permutationP().




Example for a real general square matrix (Python)
....................................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "rcond, det, LU, P, X, Inverse"
    >>> Res = A.eigen_partialPivLu2(Query, B)
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.00272489624557829438421888621186348891
    >>> print("Det  : ", Res["Det"])
    Det  :  48772174.2080000000000000000000000005

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
       2E-33,   -4E-33, -1.3E-32,    1E-33,   -1E-33,   -3E-33, 
       3E-33,   -1E-33,   -2E-33,    4E-33,   -4E-33, -1.1E-32, 
       3E-33,   -4E-33,   -3E-33,   -1E-33,   -2E-33,   -4E-33, 
       1E-33,    0E-33,   -1E-33,   -1E-33,    1E-33,   -1E-33, 
       2E-33,   -6E-33,   -2E-33,   -2E-33,    0E-33,   -5E-33, 
       0E-33,   -2E-33,   -3E-33,   -1E-33,   -1E-33,   -2E-33, 

    >>> Res["P"].show("P")
    P: 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 1, 0, 0, 0, 0, 
    0, 0, 1, 0, 0, 0, 

    >>> L = Res["LU"].unit_lower_triangle(); L.show("L")
    L: 
          1,       0,       0,       0,       0,       0, 
       0.25,       1,       0,       0,       0,       0, 
      0.479,   0.749,       1,       0,       0,       0, 
      0.148,   0.908,   0.510,       1,       0,       0, 
      0.958,  -0.795,  -0.465, -0.0452,       1,       0, 
      0.563,   0.377, -0.0613,  -0.308,   0.282,       1, 

    >>> U = Res["LU"].upper_triangle(); U.show("U")
    U: 
       48,    43,    31,    19,    14,    24, 
        0,  39.3, -6.55,  41.3,  32.5,  41.0, 
        0,     0,  32.1, -39.6,  11.0, -19.2, 
        0,     0,     0, -17.3, -2.17, -7.97, 
        0,     0,     0,     0,  31.4,  10.3, 
        0,     0,     0,     0,     0,  1.49, 

    >>> (Res["P"] * L * U).show("P * L * U (should be equal to A)")
    P * L * U (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
        1.00,    0E-35,    0E-34,    0E-35,    0E-35,    0E-34, 
      -8E-36,     1.00, -1.2E-34,    1E-35,   -1E-35,   -2E-35, 
       0E-35,   -1E-35,     1.00,    0E-35,    0E-35,    1E-34, 
       3E-36,    0E-35,    0E-34,     1.00,    2E-35,    1E-34, 
       3E-36,   -1E-35,    0E-34,    0E-35,     1.00,    1E-34, 
       1E-35,    1E-35,    0E-34,   -1E-35,    0E-35,     1.00, 






Example for a complex matrix
...............................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> Query = "rcond, det, LU, P, X, Inverse"
    >>> Res = A.eigen_partialPivLu2(Query, B)
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.0187124480364562114562726704652022526 + 0j
    >>> print("Det  : ", Res["Det"])
    Det  :  1083952.90000000000000000000000000002 - 676519.300000000000000000000000000002j

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
           -1.00E-34 + 0j, -2.00E-34 - 2.00E-33j,         1.00E-33 + 0j,  1.20E-33 - 2.00E-33j, 
     3.50E-33 - 1.00E-33j,        -1.20E-33 + 0j, -6.00E-34 - 2.00E-33j,  6.00E-34 - 2.00E-33j, 
     1.00E-33 - 1.00E-33j, -1.00E-33 - 1.00E-33j,         0 - 3.00E-33j,         0 - 1.00E-33j, 
     1.40E-33 - 1.00E-33j,        -1.00E-34 + 0j,                0 + 0j,         3.00E-34 + 0j, 

    >>> Res["P"].show("P")
    P: 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 

    >>> L = Res["LU"].unit_lower_triangle(); L.show("L")
    L: 
          1.00 + 0j,          0 + 0j,          0 + 0j,          0 + 0j, 
     0.502 - 0.355j,       1.00 + 0j,          0 + 0j,          0 + 0j, 
     0.632 - 0.560j,  0.314 + 0.471j,       1.00 + 0j,          0 + 0j, 
     0.568 + 0.151j,  0.866 - 0.190j, -0.137 - 0.755j,       1.00 + 0j, 

    >>> U = Res["LU"].upper_triangle(); U.show("U")
    U: 
     34.0 + 42.0j,  6.00 + 16.0j,  20.0 + 38.0j,  22.0 + 17.0j, 
           0 + 0j,  33.3 + 43.1j, 23.4 - 0.968j,  14.9 + 48.3j, 
           0 + 0j,        0 + 0j, -30.7 - 10.6j,  31.7 + 16.4j, 
           0 + 0j,        0 + 0j,        0 + 0j, -12.0 - 5.80j, 

    >>> (Res["P"] * L * U).show("P * L * U (should be equal to A)")
    P * L * U (should be equal to A): 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
         1.00 - 1.00E-35j, -2.00E-35 + 2.00E-35j,  1.00E-35 + 1.00E-35j,  1.00E-35 + 1.00E-35j, 
    -2.60E-35 - 3.00E-35j,      1.00 + 1.00E-36j,         0 - 1.10E-35j,                0 + 0j, 
    -2.00E-35 - 2.00E-35j, -1.00E-35 + 4.00E-35j,      1.00 - 1.00E-35j,  1.00E-35 + 1.00E-35j, 
     3.00E-36 - 1.00E-35j, -1.00E-35 - 1.10E-35j,         0 + 2.00E-36j,      1.00 + 1.00E-35j, 






|newpage|


LU Decomposition with full Pivoting
---------------------------------------------


.. method:: mat.FullPivLU(Query, matB)


    Returns the LU decomposition of the general square matrix *matA* `= A = PLUQ`, with full pivoting.
    See also Eigen :cite:p:`EigenMat118`,  Wikipedia :cite:p:`WikipediaMat118`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`




**Results:**

:isinjective:     An boolean value indicating whether `A` is injective.

:isinvertible:     An boolean value indicating whether `A` is invertible.

:issurjective:     An boolean value indicating whether `A` is surjective.

:rank:     An integer. The rank of `A`.

:det:     A scalar of a return type matching `A`. The determinant of `A`.

:rcond:     A scalar of the same return type as det. The condition number of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.

:P:     A square matrix of the same type and dimension as `A`. The permutation matrix `P` in the decomposition `A = PLUQ`.

:Q:     A square matrix of the same type and dimension as `A`. The permutation matrix `Q` in the decomposition `A = PLUQ`.

:LU:     A square matrix of the same type and dimension as `A`, containing the matrices `L` and `U` in the decomposition `A = PLUQ`.


This class represents a LU decomposition of any matrix, with complete pivoting: the matrix A is decomposed as
`A = PLUQ` where `L` is unit-lower-triangular, `U` is upper-triangular, and `P` and `Q` are permutation matrices. This is a rank-revealing LU decomposition. The eigenvalues (diagonal coefficients) of `U` are sorted in such a way that any zeros are at the end.

This decomposition provides the generic approach to solving systems of linear equations, computing the rank,
invertibility, inverse, kernel, and determinant. This LU decomposition is very stable and well tested with large
matrices. However there are use cases where the SVD decomposition is inherently more stable and/or flexible.
For example, when computing the kernel of a matrix, working with the SVD allows to select the smallest singular
values of the matrix, something that the LU decomposition doesn’t see.





Example for a real matrix
..................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "isinjective, isinvertible, issurjective, rcond, det, LU, P, Q, X, Inverse"
    >>> Res = A.eigen_fullPivLu2(Query, B)
    >>> print("isinjective : ", Res["isinjective"])
    isinjective :  True
    >>> print("isinvertible: ", Res["isinvertible"])
    isinvertible:  True
    >>> print("issurjective: ", Res["issurjective"])
    issurjective:  True
    >>> print("rcond: ", Res["rcond"])
    rcond:  0.00272489624557829438421888621186348884
    >>> print("det  : ", Res["det"])
    det  :  48772174.2079999999999999999999999991

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
     8E-33, -6E-33, -5E-33, -2E-33, -8E-33,  9E-33, 
     1E-33, -8E-33, -4E-33,  1E-33, -8E-33, -1E-33, 
     6E-33,  4E-33,  3E-33,  3E-33, -2E-33,  4E-33, 
     1E-33,  0E-33,  2E-33, -2E-33, -1E-33,  3E-33, 
     3E-33, -1E-33, -1E-33, -2E-33, -3E-33,  1E-33, 
     5E-33,  6E-33,  5E-33,  1E-33, -3E-33,  5E-33, 

    >>> P1 = Res["P"].eigen_inverse(); P1.show("P^-1")
    P^-1: 
    0, 0, 0, 1, 0, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 
    0, 0, 0, 0, 1, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 1, 0, 0, 0, 0, 

    >>> L = Res["LU"].unit_lower_triangle(); L.show("L")
    L: 
          1,       0,       0,       0,       0,       0, 
          1,       1,       0,       0,       0,       0, 
        0.2,  0.0990,       1,       0,       0,       0, 
       0.86,   0.409,   0.770,       1,       0,       0, 
       0.84,  0.0533,  -0.274, -0.0710,       1,       0, 
       0.78,   0.739,   0.404,  0.0750,  -0.295,       1, 

    >>> U = Res["LU"].upper_triangle(); U.show("U")
    U: 
        50,   0.44,     23,     42,     42,     23, 
         0,   45.6,    -11,     -6,  -40.8,     24, 
         0,      0,   42.5,   6.19,   15.6,   3.02, 
         0,      0,      0,  -24.4, -0.487,  -7.92, 
         0,      0,      0,      0,  -13.9,   2.67, 
         0,      0,      0,      0,      0,   1.49, 

    >>> Q1 = Res["Q"].eigen_inverse(); Q1.show("Q^-1")
    Q^-1: 
    0, 1, 0, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 

    >>> (P1 * L * U * Q1).show("A = P^-1 * L * U * Q^-1 (should be equal to A)")
    A = P^-1 * L * U * Q^-1 (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
      1.00,  2E-35, -2E-34, -1E-35,  0E-35,  1E-34, 
    -1E-36,   1.00, -2E-35,  0E-35,  0E-35,  3E-35, 
     0E-35,  1E-35,   1.00, -1E-35,  0E-35,  1E-34, 
    -3E-36,  2E-35,  0E-34,   1.00,  0E-35,  0E-34, 
    -3E-36,  0E-35,  0E-34,  0E-35,   1.00,  0E-34, 
     1E-35,  2E-35,  0E-34,  0E-35,  1E-35,   1.00, 







Example for a complex matrix
..................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> Query = "isinjective, isinvertible, issurjective, rcond, det, LU, P, Q, X, Inverse"
    >>> Res = A.eigen_fullPivLu2(Query, B)
    >>> print("isinjective : ", Res["isinjective"])
    isinjective :  True
    >>> print("isinvertible: ", Res["isinvertible"])
    isinvertible:  True
    >>> print("issurjective: ", Res["issurjective"])
    issurjective:  True
    >>> print("rcond: ", Res["rcond"])
    rcond:  0.0187124480364562114562726704652022524 + 0j
    >>> print("det  : ", Res["det"])
    det  :  1083952.89999999999999999999999999999 - 676519.300000000000000000000000000006j

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
    -2.50E-33 + 1.00E-33j,        -3.00E-34 + 0j, -1.00E-33 + 1.00E-33j,  5.00E-34 + 2.00E-33j, 
     6.00E-34 + 2.00E-33j, -1.00E-34 + 1.00E-33j,        -6.00E-34 + 0j,  3.00E-34 + 2.00E-33j, 
           -1.00E-33 + 0j,         0 - 1.00E-33j, -1.00E-33 - 1.00E-33j,        -1.00E-33 + 0j, 
           -1.10E-33 + 0j,        -1.00E-34 + 0j,  1.00E-34 - 1.00E-33j,  9.00E-34 + 2.00E-33j, 

    >>> P1 = Res["P"].eigen_inverse(); P1.show("P^-1")
    P^-1: 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 

    >>> L = Res["LU"].unit_lower_triangle(); L.show("L")
    L: 
          1.00 + 0j,          0 + 0j,          0 + 0j,          0 + 0j, 
    0.249 + 0.0907j,       1.00 + 0j,          0 + 0j,          0 + 0j, 
     0.453 + 0.329j,  0.306 - 0.685j,       1.00 + 0j,          0 + 0j, 
    0.865 - 0.0336j,  0.201 + 0.554j, -0.512 - 0.745j,       1.00 + 0j, 

    >>> U = Res["LU"].upper_triangle(); U.show("U")
    U: 
     42.0 + 49.0j,  32.0 + 9.00j,  32.0 + 49.0j,  47.0 + 11.0j, 
           0 + 0j,  26.9 + 36.9j,  18.5 + 1.91j,  9.31 + 31.0j, 
           0 + 0j,        0 + 0j,  31.7 + 16.4j, -30.7 - 10.6j, 
           0 + 0j,        0 + 0j,        0 + 0j, -11.6 - 3.64j, 

    >>> Q1 = Res["Q"].eigen_inverse(); Q1.show("Q^-1")
    Q^-1: 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 

    >>> (P1 * L * U * Q1).show("A = P^-1 * L * U * Q^-1 (should be equal to A)")
    A = P^-1 * L * U * Q^-1 (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
         1.00 + 1.00E-35j,         0 + 2.00E-35j,         0 + 1.00E-35j,         1.00E-35 + 0j, 
            0 + 3.00E-35j,      1.00 + 1.30E-35j,  1.00E-35 - 2.00E-35j,         0 - 2.00E-35j, 
           -1.00E-35 + 0j, -2.00E-35 + 1.00E-35j,      1.00 - 2.00E-35j,  2.00E-35 - 1.00E-35j, 
            1.30E-35 + 0j,         0 - 8.00E-36j,         0 - 3.00E-36j,      1.00 - 1.00E-35j, 










|newpage|

Cholesky Decomposition without Pivoting
---------------------------------------------------------------

.. method:: mat.CholeskyLLT(Query, matB)


    Returns the Cholesky decomposition of the symmetric matrix *matA* `= A = LL^T = U^TU`, without pivoting. 

    See also Eigen :cite:p:`EigenMat106`,  Wikipedia :cite:p:`WikipediaMat106`,  Wikipedia :cite:p:`WikipediaMat130`.




**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`



**Results:**

:det:     A scalar of a return type matching `A`. The determinant of `A`.

:rcond:     A scalar of the same return type as det. The condition number of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.

:L:     A square matrix of the same type and dimension as `A`, containing the matrix `L` in the decomposition `A = LL^T = U^TU`.

:U:     A square matrix of the same type and dimension as `A`, containing the matrix `U` in the decomposition `A = LL^T = U^TU`.




These functions perform a `LL^T` Cholesky decomposition of a symmetric, positive definite matrix `A` such that `A = LL^T = U^TU`, where `L` is lower triangular. While the Cholesky decomposition is particularly useful to solve selfadjoint problems like `D^T D x = b`, for that purpose, we recommend the Cholesky decomposition without square root which is more stable and even faster. Nevertheless, this standard Cholesky decomposition remains useful in many other situations like generalised eigen problems with hermitian matrices. Remember that Cholesky decompositions are not rank-revealing. This `LL^T` decomposition is only stable on positive definite matrices, use `LDL^T` instead for the semidefinite case. Also, do not use a Cholesky decomposition to determine whether a system of equations has a solution.


Example for a real symmetric matrix
........................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAPosDefA6x6", ""); A.show("A")

    >>> # This needs to be a self-adjoint, positive definite matrix
    A: 
    248,  40,  38,  43,  33,  35, 
     40, 240,  25,  38,  28,  35, 
     38,  25, 245,  40,  33,  17, 
     43,  38,  40, 250,  30,  33, 
     33,  28,  33,  30, 240,  22, 
     35,  35,  17,  33,  22, 243, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "info, rcond, X, L, U, Inverse"
    >>> Res = A.eigen_llt2(Query, B)
    >>> print("Info : ", Res["Info"])
    Info :  0
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.387103744149799746293987557343114309

    >>> Res["X"].show("X")
    X: 
    1.86, 1.86, 1.86, 1.87, 1.87, 1.87, 
    2.26, 2.26, 2.26, 2.26, 2.27, 2.27, 
    2.41, 2.41, 2.41, 2.42, 2.42, 2.42, 
    2.05, 2.05, 2.05, 2.06, 2.06, 2.06, 
    2.61, 2.61, 2.62, 2.62, 2.62, 2.62, 
    2.68, 2.68, 2.68, 2.69, 2.69, 2.69, 

    >>> (A * Res["X"]).show("A * X")
    A * X: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["x"]).show("B - A * X")
    B - A * X: 
    -3E-33, -3E-33,      0, -1E-33, -4E-33, -2E-33, 
    -3E-33, -5E-33, -1E-33, -2E-33, -5E-33, -2E-33, 
         0,  1E-33,      0,      0,  2E-33,      0, 
    -2E-33, -3E-33, -2E-33, -1E-33, -3E-33, -3E-33, 
     3E-33,  3E-33,  4E-33,  1E-33, -1E-33,  1E-33, 
    -1E-33, -2E-33, -3E-33, -1E-33, -4E-33, -2E-33, 

    >>> Res["L"].show("L")
    L: 
     15.7,     0,     0,     0,     0,     0, 
     2.54,  15.3,     0,     0,     0,     0, 
     2.41,  1.23,  15.4,     0,     0,     0, 
     2.73,  2.03,  2.00,  15.3,     0,     0, 
     2.10,  1.48,  1.69,  1.17,  15.1,     0, 
     2.22,  1.92, 0.601,  1.43, 0.780,  15.2, 

    >>> Res["U"].show("U")
    U: 
     15.7,  2.54,  2.41,  2.73,  2.10,  2.22, 
        0,  15.3,  1.23,  2.03,  1.48,  1.92, 
        0,     0,  15.4,  2.00,  1.69, 0.601, 
        0,     0,     0,  15.3,  1.17,  1.43, 
        0,     0,     0,     0,  15.1, 0.780, 
        0,     0,     0,     0,     0,  15.2, 

    >>> (A - Res["L"] * Res["U"]).show("A - L * U")
    A - L * U: 
     1E-33,      0,  1E-34,      0, -1E-34,  1E-34, 
         0,      0,      0,      0, -1E-34,      0, 
     1E-34,      0,      0,      0, -1E-34,      0, 
         0,      0,      0,      0,      0,  1E-34, 
    -1E-34, -1E-34, -1E-34,      0,      0,      0, 
     1E-34,      0,      0,  1E-34,      0,  1E-33, 

    >>> Res["Inverse"].show("Inverse")
    Inverse: 
       0.00438,  -0.000496,  -0.000466,  -0.000502,  -0.000379,  -0.000424, 
     -0.000496,    0.00445,  -0.000228,  -0.000455,  -0.000320,  -0.000463, 
     -0.000466,  -0.000228,    0.00433,  -0.000513,  -0.000431, -0.0000939, 
     -0.000502,  -0.000455,  -0.000513,    0.00433,  -0.000313,  -0.000385, 
     -0.000379,  -0.000320,  -0.000431,  -0.000313,    0.00437,  -0.000223, 
     -0.000424,  -0.000463, -0.0000939,  -0.000385,  -0.000223,    0.00432, 

    >>> (A * Res["Inverse"]).show("A * Inverse")
    A * Inverse: 
         1.00,    -7E-37,   6.3E-37,         0, -1.35E-36,    -1E-36, 
       -3E-37,      1.00,  -4.7E-37,    -6E-37,  -3.5E-37,    -1E-36, 
      9.7E-37,   1.6E-37,      1.00,   3.6E-37,  -3.7E-37,         0, 
        8E-37,  -1.3E-36,  -7.2E-37,      1.00,  -1.3E-37,     1E-36, 
     1.25E-36,     3E-37,  -3.5E-37,   8.2E-37,      1.00,     2E-37, 
        1E-36,    -2E-36,         0,   1.1E-36,    -3E-37,      1.00, 





Example for a hermitian matrix
..................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be a self-adjoint, positive definite matrix
    A: 
       91.0 + 0j, 12.0 - 3.60j, 22.0 - 7.40j, 14.0 + 1.10j, 
    12.0 + 3.60j,    77.0 + 0j, 2.50 - 2.00j, 3.40 - 7.60j, 
    22.0 + 7.40j, 2.50 + 2.00j,    91.0 + 0j, 17.0 + 3.70j, 
    14.0 - 1.10j, 3.40 + 7.60j, 17.0 - 3.70j,    74.0 + 0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Query = "info, rcond, X, L, U, Inverse"
    >>> Res = A.eigen_llt2(Query, B)
    >>> print("Info : ", Res["Info"])
    Info :  0 + 0j
    >>> print("Rcond: ", Res["Rcond"])
    Rcond:  0.415203875955925693806099488262499571 + 0j

    >>> Res["X"].show("X")
    X: 
        0.376 - 0.0288j,     -0.222 + 0.281j,   -0.0865 + 0.0417j,      0.229 + 0.303j, 
        0.0290 + 0.383j,      0.511 + 0.498j,      0.227 + 0.583j,      0.309 + 0.210j, 
        0.219 - 0.0602j,      0.535 + 0.463j,    0.527 - 0.00173j,      0.288 + 0.417j, 
         0.379 + 0.583j, 0.000510 + 0.00479j,      0.214 + 0.481j,     0.170 + 0.0528j, 

    >>> (A * Res["X"]).show("A * X")
    A * X: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> (B - A * Res["x"]).show("B - A * X")
    B - A * X: 
    -1.00E-34 + 4.00E-35j, -7.00E-35 - 2.00E-34j,                0 + 0j, -2.00E-34 - 1.00E-34j, 
            0 + 1.00E-34j,         1.00E-34 + 0j,  1.00E-34 + 1.00E-34j,                0 + 0j, 
    -3.00E-34 + 3.00E-35j, -3.00E-34 - 3.00E-34j,        -3.00E-34 + 0j, -2.00E-34 - 2.00E-34j, 
     2.00E-34 + 4.00E-34j, -3.00E-35 - 1.00E-34j,  1.00E-34 + 1.00E-34j,  1.00E-34 + 1.00E-34j, 

    >>> Res["L"].show("L")
    L: 
           9.54 + 0j,           0 + 0j,           0 + 0j,           0 + 0j, 
       1.26 + 0.377j,        8.68 + 0j,           0 + 0j,           0 + 0j, 
       2.31 + 0.776j, -0.0800 + 0.218j,        9.22 + 0j,           0 + 0j, 
       1.47 - 0.115j,   0.184 + 0.956j,    1.47 - 0.236j,        8.29 + 0j, 

    >>> Res["U"].show("U")
    U: 
           9.54 + 0j,    1.26 - 0.377j,    2.31 - 0.776j,    1.47 + 0.115j, 
              0 + 0j,        8.68 + 0j, -0.0800 - 0.218j,   0.184 - 0.956j, 
              0 + 0j,           0 + 0j,        9.22 + 0j,    1.47 + 0.236j, 
              0 + 0j,           0 + 0j,           0 + 0j,        8.29 + 0j, 

    >>> (A - Res["L"] * Res["U"]).show("A - L * U")
    A - L * U: 
            0 + 0j,         0 + 0j,         0 + 0j,         0 + 0j, 
            0 + 0j, -2.00E-34 + 0j,         0 + 0j,         0 + 0j, 
            0 + 0j,         0 + 0j,         0 + 0j,  1.00E-34 + 0j, 
            0 + 0j,         0 + 0j,  1.00E-34 + 0j, -1.00E-34 + 0j, 

    >>> Res["Inverse"].show("Inverse")
    Inverse: 
       0.0122 + 1.36E-39j,  -0.00177 + 0.000794j,  -0.00259 + 0.000957j,  -0.00167 - 0.000490j, 
     -0.00177 - 0.000794j,    0.0135 + 1.96E-40j, 0.000120 + 0.0000425j,  -0.000321 + 0.00154j, 
     -0.00259 - 0.000957j, 0.000120 - 0.0000425j,    0.0121 + 2.17E-40j,  -0.00231 - 0.000373j, 
     -0.00167 + 0.000490j,  -0.000321 - 0.00154j,  -0.00231 + 0.000373j,           0.0146 + 0j, 

    >>> (A * Res["Inverse"]).show("A * Inverse")
    A * Inverse: 
         1.00 + 8.00E-38j, -8.40E-37 + 2.00E-37j, -8.00E-37 + 2.30E-37j, -1.00E-36 - 1.00E-37j, 
     1.56E-36 + 4.00E-37j,      1.00 - 4.00E-38j,  1.60E-37 - 1.00E-37j,  1.00E-37 + 1.00E-36j, 
     1.20E-36 + 4.00E-38j, -4.00E-38 - 3.00E-37j,      1.00 + 6.00E-38j, -1.00E-36 - 3.00E-37j, 
     1.00E-36 - 4.00E-37j,         0 + 1.00E-36j,         1.00E-36 + 0j,      1.00 - 2.00E-38j, 





|newpage|


QR Decomposition without Pivoting
-------------------------------------------



.. method:: mat.HouseholderQR(Query, matB)



    Returns the QR decomposition of the symmetric matrix *matA* `=A = QR`, without pivoting.

    See also Eigen :cite:p:`EigenMat108`,  Wikipedia :cite:p:`WikipediaMat121`,  Wikipedia :cite:p:`WikipediaMat130`.




**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`





**Results:**

:signdet:     A scalar of a return type matching `A`. The sign of the determinant of `A`.

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:logabsdet:     A scalar of a return type matching `A`. The logarithm of the absolute value of the determinant of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.

:QR:     A square matrix of the same type and dimension as `A`, containing the matrices `Q` and `R` in the decomposition `A = QR`.


This class performs a  QR decomposition of a matrix `A` into matrices `Q` and `R` such that `A = QR` by using Householder transformations. Here, `Q` a unitary matrix and `R` an upper triangular matrix. The result
is stored in a compact way compatible with LAPACK. Note that no pivoting is performed. 

This is not a rankrevealing decomposition. If you want that feature, use FullPivHouseholderQR or ColPivHouseholderQR instead.

This Householder QR decomposition is faster, but less numerically stable and less feature-rich than FullPivHouseholderQR or ColPivHouseholderQR





Example for a real general square matrix (Python)
......................................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "absdet, logabsdet, householderq, QR, X, Inverse"
    >>> Res = A.eigen_householderQr2(Query, B)
    >>> print("absdet     : ", Res["absdet"])
    absdet     :  48772174.2079999999999999999999999994
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  17.7026705075414213350761102045531515

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
      -5E-33,    8E-33,   -4E-33,    2E-33, -1.3E-32,    2E-33, 
    -1.0E-32,   -7E-33,   -5E-33,    2E-33, -1.3E-32,    0E-33, 
       4E-33,  1.0E-32,    5E-33,  1.0E-32,    5E-33,    5E-33, 
       5E-33,    8E-33,    4E-33,    9E-33,    5E-33,    3E-33, 
      -2E-33,    4E-33,   -2E-33,    3E-33,   -3E-33,   -2E-33, 
       4E-33,    7E-33,    3E-33,    8E-33,    4E-33,    3E-33, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
    -76.6, -73.4, -50.2, -34.2, -48.9, -50.5, 
        0,  69.6,  16.5,  30.4,  52.5,  47.9, 
        0,     0,  27.0, -36.2,  3.91, -19.6, 
        0,     0,     0,  15.9, -2.42,  6.43, 
        0,     0,     0,     0, -18.7, -6.45, 
        0,     0,     0,     0,     0, -1.14, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
     -0.626, -0.0428, 0.00995, -0.0493,   0.776,  0.0413, 
     -0.600,  -0.489, -0.0766,  -0.243,  -0.538,   0.215, 
     -0.352,   0.189,  -0.288,   0.362,  -0.207,  -0.764, 
    -0.0927,   0.506,  0.0749,  -0.819, -0.0880,  -0.225, 
     -0.300,   0.402,   0.752,   0.328,  -0.218,   0.169, 
     -0.157,   0.553,  -0.583,   0.169,  -0.106,   0.538, 

    >>> (Q.T * Q).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
        1.00,   -8E-37,    1E-37,   -3E-37,   -8E-37, -1.4E-36, 
      -8E-37,     1.00,   -1E-36,   -9E-37, -7.7E-36,    0E-36, 
       1E-37,   -1E-36,     1.00, -2.1E-36,    0E-37,    2E-36, 
      -3E-37,   -9E-37, -2.1E-36,     1.00, -2.0E-36,   -6E-37, 
      -8E-37, -7.7E-36,    0E-37, -2.0E-36,     1.00,    1E-37, 
    -1.4E-36,    0E-36,    2E-36,   -6E-37,    1E-37,     1.00, 

    >>> (Q * R).show("Q * R (should be equal to A)")
    Q * R (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
        1.00,   -5E-35,    0E-34,    4E-35,   -1E-35,    0E-34, 
     4.1E-35,     1.00, -2.4E-34,   -2E-35,    3E-35,  1.3E-34, 
      -1E-35,   -2E-35,     1.00,   -1E-35,    1E-35,    0E-34, 
      -7E-36,   -1E-35,    1E-34,     1.00,   -1E-35,    0E-34, 
       3E-36,   -2E-35,    0E-34,    4E-35,     1.00,    0E-34, 
       0E-35,   -1E-35,    0E-34,    1E-35,    0E-35,     1.00, 






Example for a complex matrix
......................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> Query = "absdet, logabsdet, householderq, QR, X, Inverse"
    >>> Res = A.eigen_householderQr2(Query, B)
    >>> print("absdet     : ", Res["absdet"])
    absdet     :  1277744.98734720145252248645737252879 + 0j
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  14.0606073535918791833794443624280812 + 0j

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["x"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
    -2.00E-34 - 1.00E-33j,  1.00E-34 - 1.00E-33j,        -1.10E-33 + 0j,  2.00E-34 + 1.00E-33j, 
           -2.00E-34 + 0j, -2.80E-33 - 1.00E-33j,        -1.80E-33 + 0j,         0 - 2.00E-33j, 
            1.00E-33 + 0j,         0 + 1.00E-33j,        -1.00E-33 + 0j,         1.00E-33 + 0j, 
    -1.00E-34 - 1.00E-33j, -1.50E-33 + 1.00E-33j,         1.30E-33 + 0j, -1.00E-34 + 1.00E-33j, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
        -84.3 + 0j,  -56.2 - 29.8j,  -71.5 - 9.69j,  -68.9 - 21.0j, 
            0 + 0j,     -69.5 + 0j, -29.8 - 0.903j,  -42.7 + 7.20j, 
            0 + 0j,         0 + 0j,     -28.1 + 0j,  31.5 - 0.339j, 
            0 + 0j,         0 + 0j,         0 + 0j,     -7.76 + 0j, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
    -0.533 - 0.0889j,   0.352 - 0.217j,   0.557 + 0.167j,   0.262 - 0.361j, 
     -0.154 - 0.344j,  -0.569 - 0.246j,  0.0855 - 0.360j,   0.523 + 0.252j, 
     -0.379 - 0.107j,  -0.343 - 0.456j,  -0.396 + 0.505j, -0.318 - 0.0806j, 
     -0.403 - 0.498j,  0.0266 + 0.345j,   0.125 - 0.313j,  -0.572 + 0.170j, 

    >>> (Q.T * Q.conjugate()).show("Q.T * Q.conjugate() (should be an identity matrix)")
    Q.T * Q.conjugate() (should be an identity matrix): 
               1.00 + 0j, 1.00E-36 - 1.00E-36j,        0 + 1.00E-36j, 1.00E-36 + 2.00E-36j, 
    1.00E-36 + 1.00E-36j,            1.00 + 0j, 3.00E-36 - 1.10E-36j,        1.60E-36 + 0j, 
           0 - 1.00E-36j, 3.00E-36 + 1.10E-36j,            1.00 + 0j, 1.00E-36 - 1.00E-36j, 
    1.00E-36 - 2.00E-36j,        1.60E-36 + 0j, 1.00E-36 + 1.00E-36j,            1.00 + 0j, 

    >>> (Q * R).show("Q * R (should be equal to A)")
    Q * R (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
         1.00 - 1.00E-35j,  1.00E-35 + 2.00E-35j,  1.00E-35 + 1.00E-35j,         0 - 1.00E-35j, 
    -1.10E-35 + 1.00E-35j,      1.00 + 3.10E-35j,  2.00E-35 - 2.50E-35j,  3.00E-35 - 1.00E-35j, 
            0 + 1.00E-35j,  2.00E-35 + 1.00E-35j,             1.00 + 0j,        -2.00E-35 + 0j, 
     1.20E-35 + 2.00E-35j,  3.00E-35 + 9.00E-36j, -1.00E-35 - 4.00E-36j,             1.00 + 0j, 






|newpage|


QR Decomposition with column Pivoting
----------------------------------------------

.. method:: mat.ColPivHouseholderQR(Query, matB, threshold)


    Returns the QR decomposition of the symmetric matrix *matA* `=A = QR`, with column pivoting.
    See also: Eigen :cite:p:`EigenMat119`,  Wikipedia :cite:p:`WikipediaMat120`,  Wikipedia :cite:p:`WikipediaMat130`.






**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:matB:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`

:threshold:   Optional. The threshold that will be used by certain methods such as rank().






**Results:**

:info:     An integer indicating whether the decompsition was successful(=0) or not(=1).

:dimofkernel:     An integer returning the dimension of the kernel of `A`.

:rank:     An integer returning the rank of `A`, which need to determine when pivots are to be considered nonzero. This is not used for the QR decomposition itself.

:nonzeropivots:     An integer returning the number of non-zero ivots in the decomposition.


:isinjective:     A boolean indicating whether `A` is injective.

:isinvertible:     A boolean indicating whether `A` is invertible.

:issurjective:     A boolean indicating whether `A` is surjective.


:signdet:     A scalar of a return type matching `A`. The sign of the determinant of `A`.

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:logabsdet:     A scalar of a return type matching `A`. The logarithm of the absolute value of the determinant of `A`.

:maxpivot:     A scalar of the same return type as det. The absolute value of the biggest pivot, i.e. the biggest diagonal coefficient of `R`. 



:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.


:P:     A square matrix of the same type and dimension as `A`. The matrix `P` contains the column permutation matrix.



:Q:     A square matrix of the same type and dimension as `A`. The matrix `Q` as a sequence of householder transformations. 


:R:     A square matrix of the same type and dimension as `A`, containing the matrix `R`.

:QR:     A square matrix of the same type and dimension as `A`, containing the matrix `QR`.


This class performs a rank-revealing QR decomposition of a matrix A into matrices P, Q and R such that

AP = QR 

by using Householder transformations. Here, P is a permutation matrix, Q a unitary matrix and R an upper
triangular matrix.

This decomposition performs column pivoting in order to be rank-revealing and improve numerical stability.
It is slower than HouseholderQR, and faster than FullPivHouseholderQR.

solve: This method finds a solution x to the equation Ax=b, where A is the matrix of which this is the QR decomposition, if any exists. 

Parameters: b the right-hand-side of the equation to solve.

Returns a solution. Note: The case where b is a matrix is not yet implemented. Also, this code is space
inefficient.This method just tries to find as good a solution as possible. If you want to check whether a solution exists or if it is accurate, just call this function to get a result and then compute the error of this result, or use

MatrixBase::isApprox() directly, for instance like this:

bool a\_solution\_exists = (A*result).isApprox(b, precision);

This method avoids dividing by zero, so that the non-existence of a solution doesn’t by itself mean that you’ll get inf or nan values. If there exists more than one solution, this method will arbitrarily choose one.



Example for a real matrix
..............................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "isinjective, isinvertible, issurjective, info, dimofkernel, rank, nonzeropivots, "
    >>> Query += " absdet, logabsdet, maxpivot, QR, R, Householderq, Hqnonzeros, Permcols, X, Inverse"

    >>> Res = A.eigen_colPivHouseholderQr2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("info         : ", Res["info"])
    info         :  0
    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  6

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  48772174.2080000000000000000000000014
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  17.7026705075414213350761102045531516
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  101.163234428323810884390632615959908

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
      -3E-33, -1.6E-32,   -5E-33, -1.7E-32,    4E-33,   -9E-33, 
       7E-33,    6E-33,   -3E-33,   -5E-33,    7E-33,    9E-33, 
       3E-33,   -4E-33,   -2E-33,   -8E-33,    2E-33,   -5E-33, 
      -4E-33,   -7E-33,   -4E-33,   -8E-33,    2E-33, -1.3E-32, 
      -8E-33, -1.2E-32, -1.1E-32, -1.8E-32,   -2E-33, -1.2E-32, 
      -7E-33, -1.0E-32,   -6E-33, -1.0E-32,   -4E-33, -1.3E-32, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
    0, 1, 0, 0, 0, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
      -101,  -55.6,  -45.8,  -71.6,  -47.7,  -69.6, 
         0,  -52.7,  -1.51,   4.47,  -22.6, 0.0539, 
         0,      0,  -39.6,   4.55,   24.8,  -20.5, 
         0,      0,      0,  -18.7,  0.371,  -6.51, 
         0,      0,      0,      0,  -10.8,   1.75, 
         0,      0,      0,      0,      0,  -1.14, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
     -0.425,  -0.462,  0.0289,   0.774,  0.0677,  0.0413, 
    -0.0989,  -0.768,  0.0273,  -0.546,   0.234,   0.215, 
     -0.386,  -0.106,  -0.409,  -0.199,  -0.223,  -0.764, 
     -0.415,   0.303,   0.398,  -0.113,   0.717,  -0.225, 
     -0.494,  0.0850,   0.557,  -0.197,  -0.609,   0.169, 
     -0.494,   0.294,  -0.602,  -0.109,  0.0756,   0.538, 

    >>> Res["Hqnonzeros"].show("Hqnonzeros")
    Hqnonzeros: 
     -0.425,  -0.462,  0.0289,   0.774,  0.0677,  0.0413, 
    -0.0989,  -0.768,  0.0273,  -0.546,   0.234,   0.215, 
     -0.386,  -0.106,  -0.409,  -0.199,  -0.223,  -0.764, 
     -0.415,   0.303,   0.398,  -0.113,   0.717,  -0.225, 
     -0.494,  0.0850,   0.557,  -0.197,  -0.609,   0.169, 
     -0.494,   0.294,  -0.602,  -0.109,  0.0756,   0.538, 

    >>> (Q.T * Q).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
         1.00,    -2E-36,    -1E-36,   3.3E-36,   1.6E-36,     1E-36, 
       -2E-36,      1.00,    -2E-36,     3E-37,   2.0E-36,     2E-36, 
       -1E-36,    -2E-36,      1.00,  -1.1E-36,    -2E-37,     0E-36, 
      3.3E-36,     3E-37,  -1.1E-36,      1.00, -1.10E-36,    -6E-37, 
      1.6E-36,   2.0E-36,    -2E-37, -1.10E-36,      1.00,    -9E-37, 
        1E-36,     2E-36,     0E-36,    -6E-37,    -9E-37,      1.00, 

    >>> (Q * R * P2).show("Q * R * P2 (should be equal to A)") 
    Q * R * P2 (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
       1.00,  -2E-35,   1E-34,  -1E-35,  -3E-35,  -1E-34, 
      0E-36,    1.00,   0E-35,  -2E-35,   0E-35,  -1E-35, 
      0E-35,   0E-35,    1.00,  -1E-35,  -1E-35,   0E-34, 
     -7E-36,   0E-35,   0E-34,    1.00,  -1E-35,   0E-34, 
    1.3E-35,  -1E-35,   1E-34,  -3E-35,    1.00,   0E-34, 
      0E-35,   1E-35,   0E-34,  -2E-35,  -2E-35,    1.00, 




Example for a complex matrix
..............................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix, `A^{-1}`
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> Query = "isinjective, isinvertible, issurjective, info, dimofkernel, rank, nonzeropivots, "
    >>> Query += " absdet, logabsdet, maxpivot, QR, R, Householderq, Hqnonzeros, Permcols, X, Inverse"

    >>> Res = A.eigen_colPivHouseholderQr2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("info         : ", Res["info"])
    info         :  0
    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  4

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  1277744.98734720145252248645737252874
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  14.0606073535918791833794443624280812
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  94.2677569479617988433310533758539450

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
     9.00E-34 + 1.00E-33j,  8.00E-34 - 1.00E-33j,         2.00E-34 + 0j,  1.10E-33 - 1.00E-33j, 
     6.00E-34 - 1.00E-33j,  2.00E-34 - 1.00E-33j, -5.00E-34 - 3.00E-33j,  4.00E-34 - 1.00E-33j, 
     1.00E-33 - 4.00E-33j,  1.00E-33 - 3.00E-33j,  1.00E-33 - 2.00E-33j,  1.00E-33 - 3.00E-33j, 
     3.00E-34 + 1.00E-33j,         5.00E-34 + 0j,        -6.00E-34 + 0j,        -5.00E-34 + 0j, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
        -94.3 + 0j,  -50.3 + 26.6j,  -79.3 + 14.6j,  -67.7 + 16.1j, 
            0 + 0j,      62.2 + 0j,   23.1 + 6.28j,   35.3 - 2.79j, 
            0 + 0j,         0 + 0j,      32.4 + 0j, -27.3 - 0.294j, 
            0 + 0j,         0 + 0j,         0 + 0j,     -6.71 + 0j, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
     -0.0308 - 0.382j,    0.535 - 0.175j,    0.480 + 0.242j,    0.392 - 0.307j, 
      -0.403 - 0.435j,   -0.303 + 0.287j,  -0.0459 - 0.410j,    0.526 + 0.164j, 
      -0.445 - 0.520j, -0.0686 - 0.0850j,   -0.303 + 0.514j,  -0.402 + 0.0392j, 
     -0.0636 - 0.170j,    0.422 + 0.565j,    0.255 - 0.345j,  -0.527 + 0.0840j, 

    >>> Res["Hqnonzeros"].show("Hqnonzeros")
    Hqnonzeros: 
     -0.0308 - 0.382j,    0.535 - 0.175j,    0.480 + 0.242j,    0.392 - 0.307j, 
      -0.403 - 0.435j,   -0.303 + 0.287j,  -0.0459 - 0.410j,    0.526 + 0.164j, 
      -0.445 - 0.520j, -0.0686 - 0.0850j,   -0.303 + 0.514j,  -0.402 + 0.0392j, 
     -0.0636 - 0.170j,    0.422 + 0.565j,    0.255 - 0.345j,  -0.527 + 0.0840j, 

    >>> (Q.T * Q.conjugate()).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
                1.00 + 0j,         0 + 1.40E-36j,        -1.60E-36 + 0j,  1.10E-36 + 7.00E-37j, 
            0 - 1.40E-36j,             1.00 + 0j,  1.40E-36 - 2.00E-36j, -4.00E-36 + 3.00E-36j, 
           -1.60E-36 + 0j,  1.40E-36 + 2.00E-36j,             1.00 + 0j, -3.00E-36 - 1.00E-36j, 
     1.10E-36 - 7.00E-37j, -4.00E-36 - 3.00E-36j, -3.00E-36 + 1.00E-36j,             1.00 + 0j, 

    >>> (Q * R * P2).show("Q * R * P2 (should be equal to A)") 
    Q * R * P2 (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
         1.00 - 2.00E-35j, -2.00E-35 - 2.00E-35j,  1.00E-35 + 2.00E-35j,         1.00E-35 + 0j, 
     1.00E-36 - 1.00E-35j,      1.00 + 2.00E-36j,  2.00E-35 + 1.30E-35j, -1.00E-35 + 1.00E-35j, 
            0 - 5.00E-35j, -4.00E-35 - 1.00E-35j,      1.00 + 2.00E-35j,         0 + 2.00E-35j, 
    -8.00E-36 - 1.00E-35j, -1.00E-35 + 8.00E-36j,         0 - 1.80E-35j,      1.00 - 1.00E-35j, 












|newpage|


QR Decomposition with full Pivoting
-----------------------------------------------


.. method:: mat.FullPivHouseholderQR(Query, matB, threshold)


    Returns the QR decomposition (with full pivoting) of the general matrix *matA* such that`PAP'` = QR` by using Householder transformations. Here, `P` and `P'` are permutation matrices, `Q` is a unitary matrix and `R` is an upper triangular matrix.

    See also Eigen :cite:p:`EigenMat120`,  Wikipedia :cite:p:`WikipediaMat120`,  Wikipedia :cite:p:`WikipediaMat130`.





**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`

:threshold:   Optional. The threshold that will be used by certain methods such as rank().




**Results:**


:info:     An integer indicating whether the decompsition was successful(=0) or not(=1).

:dimofkernel:     An integer returning the dimension of the kernel of `A`.

:rank:     An integer returning the rank of `A`, which need to determine when pivots are to be considered nonzero. This is not used for the QR decomposition itself.

:nonzeropivots:     An integer returning the number of non-zero ivots in the decomposition.


:isinjective:     A boolean indicating whether `A` is injective.

:isinvertible:     A boolean indicating whether `A` is invertible.

:issurjective:     A boolean indicating whether `A` is surjective.


:signdet:     A scalar of a return type matching `A`. The sign of the determinant of `A`.

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:logabsdet:     A scalar of a return type matching `A`. The logarithm of the absolute value of the determinant of `A`.

:maxpivot:     A scalar of the same return type as det. The absolute value of the biggest pivot, i.e. the biggest diagonal coefficient of `R`. 



:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:Inv:     A square matrix of the same type and dimension as `A`. The inverse of `A, A^{-1}`.


:P:     A square matrix of the same type and dimension as `A`. The matrix `P` contains the column permutation matrix.


:P':     A square matrix of the same type and dimension as `A`. The matrix `P'` contains the rows transpositions matrix.


:Q:     A square matrix of the same type and dimension as `A`. The matrix `Q` as a sequence of householder transformations. 


:R:     A square matrix of the same type and dimension as `A`, containing the matrix `R`.

:QR:     A square matrix of the same type and dimension as `A`, containing the matrix `QR`.



This class performs a rank-revealing QR decomposition of a matrix `A` into matrices `P`, `P'`, `Q` and `R` such that`PAP'` = QR` by using Householder transformations. Here, `P` and `P'` is a permutation matrices, `Q` a unitary matrix and `R` an upper triangular matrix.

This decomposition performs full pivoting in order to be rank-revealing and achieve optimal numerical stability.
The trade-off is that it is slower than HouseholderQR and ColPivHouseholderQR.

solve: This method finds a solution x to the equation Ax=b, where A is the matrix of which this is the QR decomposition, if any exists. 

Parameters: b the right-hand-side of the equation to solve.

Returns the exact or least-square solution if the rank is greater or equal to the number of columns of A, and an
arbitrary solution otherwise. Note: The case where b is a matrix is not yet implemented. Also, this code is space inefficient.This method just tries to find as good a solution as possible. If you want to check whether a solution exists or if it is accurate, just call this function to get a result and then compute the error of this result, or use MatrixBase::isApprox() directly, for instance like this:

bool a\_solution\_exists = (A*result).isApprox(b, precision);

This method avoids dividing by zero, so that the non-existence of a solution doesn’t by itself mean that you’ll get inf or nan values. If there exists more than one solution, this method will arbitrarily choose one.



Example for a real matrix
..................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "isinjective, isinvertible, issurjective, dimofkernel, rank, nonzeropivots, "
    >>> Query += "absdet, logabsdet, maxpivot, QR, Q, Permcols, X, Inverse"

    >>> Res = A.eigen_fullPivHouseholderQr2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  6

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  48772174.2079999999999999999999999990
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  17.7026705075414213350761102045531515
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  101.163234428323810884390632615959908

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
      -6E-33,    2E-33,    5E-33,   -1E-33, -1.3E-32,   -4E-33, 
      -6E-33,   -1E-33,   -1E-33,   -5E-33, -1.7E-32,   -1E-33, 
       9E-33,    4E-33,  1.0E-32,    9E-33,    1E-33,  1.0E-32, 
       3E-33,   -1E-33,    1E-33,   -4E-33,   -5E-33,    3E-33, 
       5E-33,   -2E-33,    6E-33,   -3E-33,   -8E-33,    7E-33, 
     1.3E-32,    6E-33,  1.5E-32,  1.0E-32,    5E-33,  1.6E-32, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
    0, 1, 0, 0, 0, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
      -101,  -55.6,  -45.8,  -71.6,  -47.7,  -69.6, 
         0,  -52.7,  -1.51,   4.47,  -22.6, 0.0539, 
         0,      0,  -39.6,   4.55,   24.8,  -20.5, 
         0,      0,      0,   18.7, -0.371,   6.51, 
         0,      0,      0,      0,   10.8,  -1.75, 
         0,      0,      0,      0,      0,   1.14, 

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
     -0.425,  -0.462,  0.0289,   0.774,  0.0677,  0.0413, 
    -0.0989,  -0.768,  0.0273,  -0.546,   0.234,   0.215, 
     -0.386,  -0.106,  -0.409,  -0.199,  -0.223,  -0.764, 
     -0.415,   0.303,   0.398,  -0.113,   0.717,  -0.225, 
     -0.494,  0.0850,   0.557,  -0.197,  -0.609,   0.169, 
     -0.494,   0.294,  -0.602,  -0.109,  0.0756,   0.538, 

    >>> (Q.T * Q).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
         1.00,     0E-36,    -2E-36,  -1.8E-36,  -1.5E-36,     0E-36, 
        0E-36,      1.00,     2E-36,  -1.9E-36,   2.5E-36,    -1E-36, 
       -2E-36,     2E-36,      1.00,     7E-37,   3.1E-36,     0E-36, 
     -1.8E-36,  -1.9E-36,     7E-37,      1.00, -2.09E-36,     0E-37, 
     -1.5E-36,   2.5E-36,   3.1E-36, -2.09E-36,      1.00,  -2.2E-36, 
        0E-36,    -1E-36,     0E-36,     0E-37,  -2.2E-36,      1.00, 

    >>> (Q * R * P2).show("Q * R * P2 (should be equal to A, except possible permutation of rows)")
    Q * R * P2 (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
       1.00,   2E-35,   1E-34,   0E-35,   1E-35,   0E-34, 
      9E-36,    1.00,  -3E-35,   0E-35,  -1E-35,   1E-35, 
      1E-35,   3E-35,    1.00,  -3E-35,   3E-35,   0E-34, 
      3E-36,   2E-35,   1E-34,    1.00,  -1E-35,   0E-34, 
    1.3E-35,   4E-35,   0E-34,   1E-35,    1.00,   1E-34, 
      2E-35,   4E-35,  -2E-34,  -3E-35,   4E-35,    1.00, 






Example for a complex matrix
..................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix, `A^{-1}`
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 
    
    >>> Query = "isinjective, isinvertible, issurjective, dimofkernel, rank, nonzeropivots, "
    >>> Query += "absdet, logabsdet, maxpivot, QR, Q, Permcols, X, Inverse"

    >>> Res = A.eigen_fullPivHouseholderQr2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  4

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  1277744.98734720145252248645737252872
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  14.0606073535918791833794443624280811
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  101.163234428323810884390632615959908

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
     9.00E-34 - 1.00E-33j,  1.50E-33 - 1.00E-33j,  2.00E-34 + 2.00E-33j,  9.00E-34 + 1.00E-33j, 
    -4.00E-34 - 3.00E-33j,  6.00E-34 - 2.00E-33j,  4.00E-34 - 3.00E-33j,                0 + 0j, 
     1.00E-33 - 4.00E-33j,         0 - 5.00E-33j,  1.00E-33 - 4.00E-33j,  2.00E-33 - 4.00E-33j, 
            6.00E-34 + 0j,         3.00E-34 + 0j, -1.00E-34 + 1.00E-33j,        -6.00E-34 + 0j, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 

    >>> R = Res["QR"].upper_triangle(); R.show("R")
    R: 
       -94.3 + 0j, -50.3 + 26.6j, -79.3 + 14.6j, -67.7 + 16.1j, 
           0 + 0j,    -62.2 + 0j, -23.1 - 6.28j, -35.3 + 2.79j, 
           0 + 0j,        0 + 0j,    -32.4 + 0j, 27.3 + 0.294j, 
           0 + 0j,        0 + 0j,        0 + 0j,     6.71 + 0j, 

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
    -0.0308 - 0.382j,  -0.535 + 0.175j,  -0.480 - 0.242j,  -0.392 + 0.307j, 
     -0.403 - 0.435j,   0.303 - 0.287j,  0.0459 + 0.410j,  -0.526 - 0.164j, 
     -0.445 - 0.520j, 0.0686 + 0.0850j,   0.303 - 0.514j,  0.402 - 0.0392j, 
    -0.0636 - 0.170j,  -0.422 - 0.565j,  -0.255 + 0.345j,  0.527 - 0.0840j, 

    >>> (Q.T * Q.conjugate()).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
                1.00 + 0j,  1.00E-36 - 9.00E-37j,  1.80E-36 + 4.00E-37j,  6.00E-37 - 2.00E-37j, 
     1.00E-36 + 9.00E-37j,             1.00 + 0j, -1.50E-36 + 1.00E-36j,                0 + 0j, 
     1.80E-36 - 4.00E-37j, -1.50E-36 - 1.00E-36j,             1.00 + 0j, -1.00E-36 - 2.00E-36j, 
     6.00E-37 + 2.00E-37j,                0 + 0j, -1.00E-36 + 2.00E-36j,             1.00 + 0j, 

    >>> (Q * R * P2).show("Q * R * P2 (should be equal to A, except possible permutation of rows)")
    Q * R * P2 (should be equal to A, except possible permutation of rows): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Res["Inverse"].show("Inverse of A")
    Inverse of A: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["Inverse"]).show("A * Inverse (should be an identity matrix)")
    A * Inverse (should be an identity matrix): 
         1.00 + 1.00E-35j,         0 - 3.00E-35j, -1.00E-35 + 2.00E-35j, -2.00E-35 + 4.00E-35j, 
     1.10E-35 - 2.00E-35j,      1.00 - 3.20E-35j,  3.00E-35 + 1.00E-35j,  4.00E-35 + 5.00E-35j, 
     1.00E-35 - 7.00E-35j, -1.10E-34 - 5.00E-35j,      1.00 + 3.00E-35j,  5.00E-35 + 9.00E-35j, 
     7.00E-36 - 1.00E-35j, -1.00E-35 - 1.80E-35j,  1.00E-35 - 9.00E-36j,      1.00 + 1.00E-35j, 











|newpage|


Complete orthogonal decomposition (COD)
-----------------------------------------------


.. method:: mat.CODHouseholderQR(results, matB)


    Returns a rank-revealing complete orthogonal decomposition (COD) of the general matrix *matA* `=A`  into matrices `P`, `Q`, `T`, and `Z` such that 

    .. math::  \mathbf{A} \, \mathbf{P} = \mathbf{Q} \, 
                \begin{bmatrix} 
                    \mathbf{T} & \mathbf{0} \\ 
                    \mathbf{0} & \mathbf{0} 
                \end{bmatrix} \, 
                \mathbf{Z} 

    by using Householder transformations. Here, `P` is a permutation matrix, `Q` and `Z` are unitary matrices and `T` an upper triangular matrix of size rank-by-rank. `A` may be rank deficient.

    See also Eigen :cite:p:`EigenMat121`,  Wikipedia :cite:p:`WikipediaMat121`,  Wikipedia :cite:p:`WikipediaMat130`.







**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`




**Results:**


:info:     An integer indicating whether the decompsition was successful(=0) or not(=1).

:dimofkernel:     An integer returning the dimension of the kernel of `A`.

:rank:     An integer returning the rank of `A`, which need to determine when pivots are to be considered nonzero. This is not used for the QR decomposition itself.

:nonzeropivots:     An integer returning the number of non-zero ivots in the decomposition.


:isinjective:     A boolean indicating whether `A` is injective.

:isinvertible:     A boolean indicating whether `A` is invertible.

:issurjective:     A boolean indicating whether `A` is surjective.


:signdet:     A scalar of a return type matching `A`. The sign of the determinant of `A`.

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:logabsdet:     A scalar of a return type matching `A`. The logarithm of the absolute value of the determinant of `A`.

:maxpivot:     A scalar of the same return type as det. The absolute value of the biggest pivot, i.e. the biggest diagonal coefficient of `R`. 



:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:pseudoInverse:     A square matrix of the same type and dimension as `A`. The pseudo-inverse of `A, A^{-1}`.


:P:     A square matrix of the same type and dimension as `A`. The matrix `P` contains the column permutation matrix.


:P':     A square matrix of the same type and dimension as `A`. The matrix `P'` contains the rows transpositions matrix.


:T:     A square matrix of the same type and dimension as `A`., containing the matrix `Z`.


:Z:     A square matrix of the same type and dimension as `A`, containing the matrix `R`.

:QTZ:     A square matrix of the same type and dimension as `A`, containing the matrix `QTZ`.



This class performs a  a rank-revealing complete orthogonal decomposition (COD) of the general matrix *matA* `=A`  into matrices `P`, `Q`, `T`, and `Z` such that 

.. math::  \mathbf{A} \, \mathbf{P} = \mathbf{Q} \, 
            \begin{bmatrix} 
                \mathbf{T} & \mathbf{0} \\ 
                \mathbf{0} & \mathbf{0} 
            \end{bmatrix} \, 
            \mathbf{Z} 

by using Householder transformations. Here, `P` is a permutation matrix, `Q` and `Z` are unitary matrices and `T` an upper triangular matrix of size rank-by-rank. `A` may be rank deficient.


solve: This method finds a solution x to the equation Ax=b, where A is the matrix of which this is the QR decomposition, if any exists. 

Parameters: b the right-hand-side of the equation to solve.

Returns the exact or least-square solution if the rank is greater or equal to the number of columns of A, and an
arbitrary solution otherwise. Note: The case where b is a matrix is not yet implemented. Also, this code is space inefficient.This method just tries to find as good a solution as possible. If you want to check whether a solution exists or if it is accurate, just call this function to get a result and then compute the error of this result, or use MatrixBase::isApprox() directly, for instance like this:

bool a\_solution\_exists = (A*result).isApprox(b, precision);

This method avoids dividing by zero, so that the non-existence of a solution doesn’t by itself mean that you’ll get inf or nan values. If there exists more than one solution, this method will arbitrarily choose one.




Example for a real matrix
..................................

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # This needs to be a square matrix
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> Query = "isinjective, isinvertible, issurjective, info, dimofkernel, rank, nonzeropivots, absdet, "
    >>> Query += "logabsdet, maxpivot, QTZ, T, Z, Householderq, Hqnonzeros, Permcols, X, PseudoInverse"

    >>> Res = A.eigen_COD2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("info         : ", Res["info"])
    dimofkernel  :  0
    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  6

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  48772174.2080000000000000000000000014
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  17.7026705075414213350761102045531516
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  101.163234428323810884390632615959908

    >>> Res["X"].show("X")
    X: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
      -3E-33, -1.6E-32,   -5E-33, -1.7E-32,    4E-33,   -9E-33, 
       7E-33,    6E-33,   -3E-33,   -5E-33,    7E-33,    9E-33, 
       3E-33,   -4E-33,   -2E-33,   -8E-33,    2E-33,   -5E-33, 
      -4E-33,   -7E-33,   -4E-33,   -8E-33,    2E-33, -1.3E-32, 
      -8E-33, -1.2E-32, -1.1E-32, -1.8E-32,   -2E-33, -1.2E-32, 
      -7E-33, -1.0E-32,   -6E-33, -1.0E-32,   -4E-33, -1.3E-32, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
    0, 1, 0, 0, 0, 0, 
    1, 0, 0, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 0, 0, 1, 

    >>> Res["QTZ"].show("QTZ")
    QTZ: 
       -101,   -55.6,   -45.8,   -71.6,   -47.7,   -69.6, 
     0.0694,   -52.7,   -1.51,    4.47,   -22.6,  0.0539, 
      0.271, -0.0112,   -39.6,    4.55,    24.8,   -20.5, 
      0.291,  -0.252,  -0.279,   -18.7,   0.371,   -6.51, 
      0.347,  -0.141,  -0.389,   0.443,   -10.8,    1.75, 
      0.347,  -0.261,   0.427,   0.222, -0.0306,   -1.14, 

    >>> T = Res["T"].upper_triangle(); T.show("T")
    T: 
      -101,  -55.6,  -45.8,  -71.6,  -47.7,  -69.6, 
         0,  -52.7,  -1.51,   4.47,  -22.6, 0.0539, 
         0,      0,  -39.6,   4.55,   24.8,  -20.5, 
         0,      0,      0,  -18.7,  0.371,  -6.51, 
         0,      0,      0,      0,  -10.8,   1.75, 
         0,      0,      0,      0,      0,  -1.14, 

    >>> Z = Res["Z"]; Z.show("Z")
    Z: 
    1, 0, 0, 0, 0, 0, 
    0, 1, 0, 0, 0, 0, 
    0, 0, 1, 0, 0, 0, 
    0, 0, 0, 1, 0, 0, 
    0, 0, 0, 0, 1, 0, 
    0, 0, 0, 0, 0, 1, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
     -0.425,  -0.462,  0.0289,   0.774,  0.0677,  0.0413, 
    -0.0989,  -0.768,  0.0273,  -0.546,   0.234,   0.215, 
     -0.386,  -0.106,  -0.409,  -0.199,  -0.223,  -0.764, 
     -0.415,   0.303,   0.398,  -0.113,   0.717,  -0.225, 
     -0.494,  0.0850,   0.557,  -0.197,  -0.609,   0.169, 
     -0.494,   0.294,  -0.602,  -0.109,  0.0756,   0.538, 

    >>> Res["Hqnonzeros"].show("Hqnonzeros")
    Hqnonzeros: 
     -0.425,  -0.462,  0.0289,   0.774,  0.0677,  0.0413, 
    -0.0989,  -0.768,  0.0273,  -0.546,   0.234,   0.215, 
     -0.386,  -0.106,  -0.409,  -0.199,  -0.223,  -0.764, 
     -0.415,   0.303,   0.398,  -0.113,   0.717,  -0.225, 
     -0.494,  0.0850,   0.557,  -0.197,  -0.609,   0.169, 
     -0.494,   0.294,  -0.602,  -0.109,  0.0756,   0.538, 

    >>> (Q.T * Q).show("Q.T * Q (should be an identity matrix)")
    Q.T * Q (should be an identity matrix): 
         1.00,    -2E-36,    -1E-36,   3.3E-36,   1.6E-36,     1E-36, 
       -2E-36,      1.00,    -2E-36,     3E-37,   2.0E-36,     2E-36, 
       -1E-36,    -2E-36,      1.00,  -1.1E-36,    -2E-37,     0E-36, 
      3.3E-36,     3E-37,  -1.1E-36,      1.00, -1.10E-36,    -6E-37, 
      1.6E-36,   2.0E-36,    -2E-37, -1.10E-36,      1.00,    -9E-37, 
        1E-36,     2E-36,     0E-36,    -6E-37,    -9E-37,      1.00, 

    >>> (Q * T * Z* P2).show("Q * T * Z * P2 (should be equal to A)")
    Q * T * Z * P2 (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> Res["PseudoInverse"].show("PseudoInverse")
    PseudoInverse: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> (A * Res["PseudoInverse"]).show("A * PseudoInverse")
    A * PseudoInverse: 
       1.00,  -2E-35,   1E-34,  -1E-35,  -3E-35,  -1E-34, 
      0E-36,    1.00,   0E-35,  -2E-35,   0E-35,  -1E-35, 
      0E-35,   0E-35,    1.00,  -1E-35,  -1E-35,   0E-34, 
     -7E-36,   0E-35,   0E-34,    1.00,  -1E-35,   0E-34, 
    1.3E-35,  -1E-35,   1E-34,  -3E-35,    1.00,   0E-34, 
      0E-35,   1E-35,   0E-34,  -2E-35,  -2E-35,    1.00, 








Example for a complex matrix
..................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")

    >>> # This needs to be an invertible matrix, `A^{-1}`
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> Query = "isinjective, isinvertible, issurjective, info, dimofkernel, rank, nonzeropivots, absdet, "
    >>> Query += "logabsdet, maxpivot, QTZ, T, Z, Householderq, Hqnonzeros, Permcols, X, PseudoInverse"

    >>> Res = A.eigen_COD2(Query, B)

    >>> print("isinjective  : ", Res["isinjective"])
    isinjective  :  True
    >>> print("isinvertible : ", Res["isinvertible"])
    isinvertible :  True
    >>> print("issurjective : ", Res["issurjective"])
    issurjective :  True

    >>> print("info         : ", Res["info"])
    dimofkernel  :  0
    >>> print("dimofkernel  : ", Res["dimofkernel"])
    dimofkernel  :  0
    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeropivots: ", Res["nonzeropivots"])
    nonzeropivots:  4

    >>> print("absdet     : ", Res["absdet"])
    absdet     :  1277744.98734720145252248645737252874
    >>> print("logabsdet  : ", Res["logabsdet"])
    logabsdet  :  14.0606073535918791833794443624280812
    >>> print("maxpivot  : ", Res["maxpivot"])
    maxpivot  :  94.2677569479617988433310533758539450

    >>> Res["X"].show("X")
    X: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> (A * Res["X"]).show("A * X (should be equal to B)")
    A * X (should be equal to B): 
    11.0 + 31.0j, 12.0 + 32.0j, 13.0 + 33.0j, 14.0 + 34.0j, 
    21.0 + 41.0j, 22.0 + 42.0j, 23.0 + 43.0j, 24.0 + 44.0j, 
    31.0 + 51.0j, 32.0 + 52.0j, 33.0 + 53.0j, 34.0 + 54.0j, 
    41.0 + 61.0j, 42.0 + 62.0j, 43.0 + 63.0j, 44.0 + 64.0j, 

    >>> (B - A * Res["X"]).show("B - A * X (should be a zero matrix)")
    B - A * X (should be a zero matrix): 
     9.00E-34 + 1.00E-33j,  8.00E-34 - 1.00E-33j,         2.00E-34 + 0j,  1.10E-33 - 1.00E-33j, 
     6.00E-34 - 1.00E-33j,  2.00E-34 - 1.00E-33j, -5.00E-34 - 3.00E-33j,  4.00E-34 - 1.00E-33j, 
     1.00E-33 - 4.00E-33j,  1.00E-33 - 3.00E-33j,  1.00E-33 - 2.00E-33j,  1.00E-33 - 3.00E-33j, 
     3.00E-34 + 1.00E-33j,         5.00E-34 + 0j,        -6.00E-34 + 0j,        -5.00E-34 + 0j, 

    >>> P2 = Res["Permcols"].eigen_inverse(); P2.show("P2^-1")
    P2^-1: 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 

    >>> Res["QTZ"].show("QTZ")
    QTZ: 
         -94.3 + 0j,   -50.3 + 26.6j,   -79.3 + 14.6j,   -67.7 + 16.1j, 
     0.481 + 0.244j,       62.2 + 0j,    23.1 + 6.28j,    35.3 - 2.79j, 
     0.544 + 0.303j,  0.238 + 0.130j,       32.4 + 0j,  -27.3 - 0.294j, 
     0.108 + 0.125j, -0.162 - 0.347j, -0.360 + 0.302j,      -6.71 + 0j, 

    >>> T = Res["T"].upper_triangle(); T.show("T")
    T: 
        -94.3 + 0j,  -50.3 + 26.6j,  -79.3 + 14.6j,  -67.7 + 16.1j, 
            0 + 0j,      62.2 + 0j,   23.1 + 6.28j,   35.3 - 2.79j, 
            0 + 0j,         0 + 0j,      32.4 + 0j, -27.3 - 0.294j, 
            0 + 0j,         0 + 0j,         0 + 0j,     -6.71 + 0j, 

    >>> Z = Res["Z"]; Z.show("Z")
    Z: 
    1.00 + 0j,    0 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j, 1.00 + 0j,    0 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j, 1.00 + 0j,    0 + 0j, 
       0 + 0j,    0 + 0j,    0 + 0j, 1.00 + 0j, 

    >>> Q = Res["Householderq"]; Q.show("Q")
    Q: 
     -0.0308 - 0.382j,    0.535 - 0.175j,    0.480 + 0.242j,    0.392 - 0.307j, 
      -0.403 - 0.435j,   -0.303 + 0.287j,  -0.0459 - 0.410j,    0.526 + 0.164j, 
      -0.445 - 0.520j, -0.0686 - 0.0850j,   -0.303 + 0.514j,  -0.402 + 0.0392j, 
     -0.0636 - 0.170j,    0.422 + 0.565j,    0.255 - 0.345j,  -0.527 + 0.0840j, 

    >>> Res["Hqnonzeros"].show("Hqnonzeros")
    Hqnonzeros: 
     -0.0308 - 0.382j,    0.535 - 0.175j,    0.480 + 0.242j,    0.392 - 0.307j, 
      -0.403 - 0.435j,   -0.303 + 0.287j,  -0.0459 - 0.410j,    0.526 + 0.164j, 
      -0.445 - 0.520j, -0.0686 - 0.0850j,   -0.303 + 0.514j,  -0.402 + 0.0392j, 
     -0.0636 - 0.170j,    0.422 + 0.565j,    0.255 - 0.345j,  -0.527 + 0.0840j, 

    >>> (Q.T * Q.conjugate()).show("Q.T * Q.conjugate() (should be an identity matrix)")
    Q.T * Q.conjugate() (should be an identity matrix): 
                1.00 + 0j,         0 + 1.40E-36j,        -1.60E-36 + 0j,  1.10E-36 + 7.00E-37j, 
            0 - 1.40E-36j,             1.00 + 0j,  1.40E-36 - 2.00E-36j, -4.00E-36 + 3.00E-36j, 
           -1.60E-36 + 0j,  1.40E-36 + 2.00E-36j,             1.00 + 0j, -3.00E-36 - 1.00E-36j, 
     1.10E-36 - 7.00E-37j, -4.00E-36 - 3.00E-36j, -3.00E-36 + 1.00E-36j,             1.00 + 0j, 

    >>> (Q * T * Z* P2).show("Q * T * Z * P2 (should be equal to A)")
    Q * T * Z * P2 (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> Res["PseudoInverse"].show("PseudoInverse")
    PseudoInverse: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> (A * Res["PseudoInverse"]).show("A * PseudoInverse")
    A * PseudoInverse: 
         1.00 - 2.00E-35j, -2.00E-35 - 2.00E-35j,  1.00E-35 + 2.00E-35j,         1.00E-35 + 0j, 
     1.00E-36 - 1.00E-35j,      1.00 + 2.00E-36j,  2.00E-35 + 1.30E-35j, -1.00E-35 + 1.00E-35j, 
            0 - 5.00E-35j, -4.00E-35 - 1.00E-35j,      1.00 + 2.00E-35j,         0 + 2.00E-35j, 
    -8.00E-36 - 1.00E-35j, -1.00E-35 + 8.00E-36j,         0 - 1.80E-35j,      1.00 - 1.00E-35j, 











