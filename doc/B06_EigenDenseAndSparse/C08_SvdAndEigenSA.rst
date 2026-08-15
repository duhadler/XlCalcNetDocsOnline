

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />




|newpage|

Singular Value and Eigen (selfadjoint) decompositions
===============================================================================================


Singular Value Decomposition, only singular values
-----------------------------------------------------------------------------------------------

.. method:: mat.JacobiSVD(Query, , matB=None, threshold=0, preconditioner="ColPivQR")

    Returns the two-sided Jacobi SVD decomposition of a rectangular matrix.

    See also:  Wikipedia :cite:p:`WikipediaMat109`.




**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:matB:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`

:threshold:   Optional. The threshold that will be used by certain methods such as rank(). A value of 0 means that the default value (which is determined internally) will be used.

:preconditioner:   Optional. A string specifying the the type of QR decomposition that will be used internally for the R-SVD step for non-square matrices. See discussion of possible values below.


 

**Results:**

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:rank:     An integer. The rank of `A` (equal to the number of non-zero singular values)

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:pseudoInverse:     A square matrix of the same type and dimension as `A`. The pseudo-inverse of `A, A^{-1}`.


:SV:     A vector of the same type`A`. The singular values `A` (see below).

:thinU:     A square matrix of the same type and dimension as `A`. The thin singular vectors `U` (see below).

:thinV:     A square matrix of the same type and dimension as `A`. The thin singular vectors `V` (see below).

:fullU:     A square matrix of the same type and dimension as `A`. The full singular vectors `U` (see below).

:fullV:     A square matrix of the same type and dimension as `A`. The full singular vectors `V` (see below).


The singular value decomposition of an `m\times n` complex matrix `\mathbf {M}` is a factorization of the form `\mathbf {M} = \mathbf {U\Sigma V^{*}}`, where `\mathbf {U}` is an `m\times m` complex unitary matrix, `\mathbf {\Sigma}` is an `m\times n` rectangular diagonal matrix with non-negative real numbers on the diagonal, and `\mathbf {V}` is an `n\times n` complex unitary matrix. If `\mathbf {M}` is real, `\mathbf {U}` and `\mathbf {V} ^{\textsf {T}}=\mathbf {V^{*}}` are real orthogonal matrices.

The diagonal entries `\sigma _{i}=\Sigma _{ii}` of `\mathbf{\Sigma}` are known as the singular values of `\mathbf {M}`. The number of non-zero singular values is equal to the rank of `\mathbf {M}`. The columns of `\mathbf {U}` and the columns of `\mathbf {V}` are called the left-singular vectors and right-singular vectors of `\mathbf {M}`, respectively. These vectors are related by

.. math:: \mathbf {Mv} =\sigma \mathbf {u} \,{\text{ and }}\mathbf {M} ^{*}\mathbf {u} =\sigma \mathbf {v} .


The singular values are the square roots of non-negative eigenvalues of `\mathbf {M} ^{*}\mathbf {M}`.

Matrix transpose and conjugate do not alter singular values.

.. math:: \sigma _{i}(A)=\sigma _{i}\left(A^{\textsf {T}}\right)=\sigma _{i}\left(A^{*}\right)=\sigma _{i}\left({\bar {A}}\right).


For any unitary `U\in \mathbb {C} ^{m\times m},V\in \mathbb {C} ^{n\times n}.`

.. math:: \sigma _{i}(A)=\sigma _{i}(UAV).


Relation to eigenvalues:

.. math:: \sigma _{i}^{2}(A)=\lambda _{i}\left(AA^{*}\right)=\lambda _{i}\left(A^{*}A\right).



The singular value decomposition is very general in the sense that it can be applied to any `m \times n` matrix, whereas the eigenvalue decomposition can only be applied to diagonalizable matrices. Nevertheless, the two decompositions are related.

Given an SVD of M, as described above, the following two relations hold:


.. math:: \mathbf {M} ^{*}\mathbf {M} = \mathbf {V} {\boldsymbol {\Sigma }}^{*}\mathbf {U} ^{*}\,\mathbf {U} {\boldsymbol {\Sigma }}\mathbf {V} ^{*} = \mathbf {V} ({\boldsymbol {\Sigma }}^{*}{\boldsymbol {\Sigma }})\mathbf {V} ^{*}


.. math:: \mathbf {M} \mathbf {M} ^{*} = \mathbf {U} {\boldsymbol {\Sigma }}\mathbf {V} ^{*}\,\mathbf {V} {\boldsymbol {\Sigma }}^{*}\mathbf {U} ^{*} = \mathbf {U} ({\boldsymbol {\Sigma }}{\boldsymbol {\Sigma }}^{*})\mathbf {U} ^{*}


The right-hand sides of these relations describe the eigenvalue decompositions of the left-hand sides. Consequently:

The columns of `\mathbf {V}` (right-singular vectors) are eigenvectors of `\mathbf {M} ^{*}\mathbf {M}`.

The columns of `\mathbf {U}` (left-singular vectors) are eigenvectors of `\mathbf {M} \mathbf {M} ^{*}`.

The non-zero elements of  `\mathbf{\Sigma}` (non-zero singular values) are the square roots of the non-zero eigenvalues of `\mathbf {M} ^{*}\mathbf {M}` or `\mathbf {M} \mathbf {M} ^{*}`.







Example for a real matrix: only singular values
............................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")
    A: 
      48,   43,   31,   19,   14,   24, 
      46,   10,   20,  4.6,   14,   10, 
      27,   39,   13,   34,   29,   37, 
     7.1,   42,   15,  2.8,   35,   23, 
      23,   50,   42, 0.44,   42,   23, 
      12,   50,  1.2,   46,   36,   47, 

    >>> Query = "rank, nonzeros, absdet, logabsdet, S, SPlus"
    >>> Res = A.eigen_jacobiSvd2(Query)

    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeros     : ", Res["nonzeros"])
    nonzeropivots:  6

    print("absdet   : ", Res["absdet"])
    absdet   :  48772174.2080000000000000000000000149
    print("logabsdet: ", Res["logabsdet"])
    logabsdet:  17.7026705075414213350761102045531518
    print()
    
    print("rcond   : ", Res["rcond"])  # TBD
    print("isinvertible: ", Res["isinvertible"])  # TBD
    print()

    >>> Res["S"].show("Singular values")
    Singular values: 
      169, 
     58.6, 
     44.1, 
     15.2, 
     7.75, 
    0.950, 

    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00593, 
     0.0171, 
     0.0227, 
     0.0657, 
      0.129, 
       1.05, 





Example for a complex matrix: only singular values
............................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(6,4); A.show("A")
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 
    23.0 + 43.0j, 15.0 + 11.0j, 28.0 + 19.0j, 35.0 + 32.0j, 
    33.0 + 49.0j, 42.0 + 48.0j, 47.0 + 32.0j, 34.0 + 25.0j, 

    >>> Query = "rank, nonzeros, S, SPlus"
    >>> Res = A.eigen_jacobiSvd2(Query)

    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeros     : ", Res["nonzeros"])
    nonzeropivots:  4

    >>> Res["S"].show("Singular values")
    Singular values: 
     208 + 0j, 
    62.1 + 0j, 
    45.6 + 0j, 
    18.6 + 0j, 

    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00480 + 0j, 
     0.0161 + 0j, 
     0.0219 + 0j, 
     0.0536 + 0j, 





|newpage|


Singular Value Decomposition, singular values and thin singular vectors
-----------------------------------------------------------------------------------------------

.. method:: mat.JacobiThinSVD(Query, , matB=None, threshold=0, preconditioner="ColPivQR")


    Returns the two-sided Jacobi SVD decomposition of a rectangular matrix.

    See also:  Wikipedia :cite:p:`WikipediaMat109`,  Wikipedia :cite:p:`WikipediaMat104a`.




**Parameters:**


:Query:     Required. A string specifying which items of the result section should be computed.

:matB:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`

:threshold:   Optional. The threshold that will be used by certain methods such as rank(). A value of 0 means that the default value (which is determined internally) will be used.

:preconditioner:   Optional. A string specifying the the type of QR decomposition that will be used internally for the R-SVD step for non-square matrices. See discussion of possible values below.


 

**Results:**

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:rank:     An integer. The rank of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:pseudoInverse:     A square matrix of the same type and dimension as `A`. The pseudo-inverse of `A, A^{-1}`.


:SV:     A vector of the same type`A`. The singular values `A` (see below).

:thinU:     A square matrix of the same type and dimension as `A`. The thin singular vectors `U` (see below).

:thinV:     A square matrix of the same type and dimension as `A`. The thin singular vectors `V` (see below).

:fullU:     A square matrix of the same type and dimension as `A`. The full singular vectors `U` (see below).

:fullV:     A square matrix of the same type and dimension as `A`. The full singular vectors `V` (see below).







Example for a real matrix: the singular values, pseudoinverse and thin singular vectors
...........................................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

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

    >>> Query = "rank, nonzeros, S, U, V, X, PseudoInverse, SPlus"
    >>> Res = A.eigen_jacobiSvdThin(Query, B)

    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeros: ", Res["nonzeros"])
    nonzeropivots:  6

    >>> Res["S"].show("Singular values")
    Singular values: 
      169, 
     58.6, 
     44.1, 
     15.2, 
     7.75, 
    0.950, 

    >>> Res["U"].show("U")
    U: 
      0.435,  -0.390,   0.336,  -0.697,  -0.243, -0.0356, 
      0.238,  -0.526,   0.374,   0.680,  -0.132,  -0.220, 
      0.439,   0.204,   0.280,   0.153,   0.296,   0.759, 
      0.337,  0.0890,  -0.509,   0.161,  -0.737,   0.224, 
      0.460,  -0.310,  -0.610, -0.0138,   0.541,  -0.165, 
      0.486,   0.653,   0.194,  0.0550,  0.0143,  -0.544, 

    >>> Res["V"].show("V")
    V: 
       0.370,   -0.615,    0.580,    0.226,   -0.303,  -0.0706, 
       0.591,    0.117,   -0.297,   -0.551,   -0.442,   -0.223, 
       0.290,   -0.527,   -0.261,   -0.271,    0.692,    0.135, 
       0.283,    0.466,    0.563,   -0.127,    0.473,   -0.382, 
       0.419,    0.114,   -0.418,    0.737,   0.0986,   -0.288, 
       0.416,    0.317,    0.125,    0.112, -0.00594,    0.836, 


    >>> # Checking the properties of the decomposition
    >>> (Res["U"] * Res["S"].D * Res["V"].H).show("U * S.D * V.H (should be equal to A)")
    U * S.D * V.H (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> CheckResult = (A - Res["U"] * Res["S"].D * Res["V"].H).norm()
    >>> print("||A - U * S.D * V.H|| (should be zero): ", CheckResult)
    ||A - U * S.D * V.H|| (should be zero):  8.10412857745976288505205302405511259E-33


    >>> # Checking the properties of the pseudoinverse
    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00593, 
     0.0171, 
     0.0227, 
     0.0657, 
      0.129, 
       1.05, 

    >>> Pinv = Res["V"] * Res["SPlus"].D * Res["U"].H; Pinv.show("Pinv = V * SPlus.D * U.H")
    Pinv = V * SPlus.D * U.H: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> CheckResult = (Pinv - Res["PseudoInverse"]).norm()
    >>> print("||Pinv - PseudoInverse|| (should be zero): ", CheckResult)
    ||Pinv - PseudoInverse|| (should be zero):  2.28256434739527113292893309427326250E-36

    >>> CheckResult = (A - A * Pinv * A).norm()
    >>> print("||A - A * Pinv * A|| (should be zero): ", CheckResult)
    ||A - A * Pinv * A|| (should be zero):  8.98434059906457464441658519736727490E-33



    >>> # Checking the properties of the solution x
    >>> XPlus = Pinv * B; XPlus.show("XPlus")
    XPlus: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> CheckResult = (XPlus - Res["X"]).norm()
    >>> print("||XPlus - X]|| (should be zero): ", CheckResult)
    ||XPlus - X]|| (should be zero):  5.95971475827492938580034754683669071E-33

    >>> CheckResult = (B - A * Res["X"]).norm()
    >>> print("||B - A * X|| (should be zero): ", CheckResult)
    ||B - A * X|| (should be zero):  4.85901224530253679417394342131061588E-32



    >>> # Checking the relationship to the eigenvalues of A * A.H 
    >>> C = A * A.H if (A.rows > A.cols) else A.H * A
    >>> D = C.eigen_SelfAdjointEigenSystem2("eval")["eval"]; D.show("D: Eigenvalues of A * A.H")
    D: Eigenvalues of A * A.H: 
      0.902, 
       60.0, 
        232, 
    1.94E+3, 
    3.43E+3, 
    2.85E+4, 

    >>> E = (Res["S"].cwiseProduct(Res["S"])).reverse_full()
    >>> E.show("E: Squared singular values, in ascending order")
    E: Squared singular values, in ascending order: 
      0.902, 
       60.0, 
        232, 
    1.94E+3, 
    3.43E+3, 
    2.85E+4, 

    >>> (D - E).show("D-E (should be a zero vector)")
    D-E (should be a zero vector): 
    -1.48E-32, 
    -3.34E-32, 
     -5.4E-32, 
     -1.3E-31, 
     -4.1E-31, 
        4E-31, 







Example for a complex matrix: the singular values, pseudoinverse and thin singular vectors
...........................................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")
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

    >>> Query = "rank, nonzeros, S, U, V, X, PseudoInverse, SPlus"
    >>> Res = A.eigen_jacobiSvdThin(Query, B)

    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeros: ", Res["nonzeros"])
    nonzeropivots:  4

    >>> Res["S"].show("Singular values")
    Singular values: 
     163 + 0j, 
    54.2 + 0j, 
    39.9 + 0j, 
    3.63 + 0j, 

    >>> Res["U"].show("U")
    U: 
     -0.430 - 0.102j,   0.409 - 0.250j,  0.585 - 0.0708j,  -0.324 + 0.348j, 
     -0.476 - 0.153j, -0.582 + 0.0348j,  -0.170 - 0.215j,  -0.546 - 0.190j, 
    -0.617 - 0.0410j,  0.0954 - 0.293j,  -0.386 + 0.495j,  0.359 - 0.0131j, 
     -0.375 - 0.176j, -0.0724 + 0.574j,   0.349 - 0.247j,   0.534 - 0.159j, 

    >>> Res["V"].show("V")
    V: 
      -0.437 + 0.150j,    0.592 + 0.283j,    0.274 - 0.230j, -0.478 + 0.00322j, 
      -0.383 + 0.383j,  -0.556 - 0.0490j,   -0.250 + 0.254j,  -0.513 + 0.0673j, 
      -0.411 + 0.231j,    0.214 + 0.327j,  -0.572 + 0.0914j,   0.537 - 0.0308j, 
      -0.425 + 0.300j,   -0.237 - 0.221j,   0.634 - 0.0880j,   0.463 - 0.0218j, 


    >>> # Checking the properties of the decomposition
    >>> (Res["U"] * Res["S"].D * Res["V"].H).show("U * S.D * V.H (should be equal to A)")
    U * S.D * V.H (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> CheckResult = (A - Res["U"] * Res["S"].D * Res["V"].H).norm()
    >>> print("||A - U * S.D * V.H|| (should be zero): ", CheckResult)
    ||A - U * S.D * V.H|| (should be zero):  7.23797623649041832083182110841296889E-33 + 0j


    >>> # Checking the properties of the pseudoinverse
    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00615 + 0j, 
     0.0185 + 0j, 
     0.0250 + 0j, 
      0.275 + 0j, 

    >>> Pinv = Res["V"] * Res["SPlus"].D * Res["U"].H; Pinv.show("Pinv = V * SPlus.D * U.H")
    Pinv = V * SPlus.D * U.H: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> CheckResult = (Pinv - Res["PseudoInverse"]).norm()
    >>> print("||Pinv - PseudoInverse|| (should be zero): ", CheckResult)
    ||Pinv - PseudoInverse|| (should be zero):  6.32060123722419305732811075240482494E-37 + 0j

    >>> CheckResult = (A - A * Pinv * A).norm()
    >>> print("||A - A * Pinv * A|| (should be zero): ", CheckResult)
    ||A - A * Pinv * A|| (should be zero):  4.78955112719344504545703109417795418E-33 + 0j



    >>> # Checking the properties of the solution x
    >>> XPlus = Pinv * B; XPlus.show("XPlus")
    XPlus: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> CheckResult = (XPlus - Res["X"]).norm()
    >>> print("||XPlus - X]|| (should be zero): ", CheckResult)
    ||XPlus - X]|| (should be zero):  8.35763124336076459797867686951053026E-35 + 0j

    >>> CheckResult = (B - A * Res["X"]).norm()
    >>> print("||B - A * X|| (should be zero): ", CheckResult)
    ||B - A * X|| (should be zero):  8.25590697622011727085329191499069154E-33 + 0j



    >>> # Checking the relationship to the eigenvalues of A * A.H 
    >>> C = A * A.H if (A.rows > A.cols) else A.H * A
    >>> D = C.eigen_SelfAdjointEigenSystem2("eval")["eval"]; D.show("D: Eigenvalues of A * A.H")
    D: Eigenvalues of A * A.H: 
       13.2 + 0j, 
    1.60E+3 + 0j, 
    2.93E+3 + 0j, 
    2.65E+4 + 0j, 

    >>> E = (Res["S"].cwiseProduct(Res["S"])).reverse_full(); 
    >>> E.show("E: Squared singular values, in ascending order")
    E: Squared singular values, in ascending order: 
       13.2 + 0j, 
    1.60E+3 + 0j, 
    2.93E+3 + 0j, 
    2.65E+4 + 0j, 

    >>> (D - E).show("D-E (should be a zero vector)")
    D-E (should be a zero vector): 
    -5.10E-33 + 0j, 
    -1.40E-31 + 0j, 
     2.40E-31 + 0j, 
     7.00E-31 + 0j, 







|newpage|


Singular Value Decomposition, singular values and full singular vectors
-----------------------------------------------------------------------------------------------

.. method:: mat.JacobiFullSVD(Query, matB=None, threshold=0, preconditioner="ColPivQR")


    Returns the two-sided Jacobi SVD decomposition of a rectangular matrix.

    See also Eigen :cite:p:`EigenMat109`,  Wikipedia :cite:p:`WikipediaMat109`,  Wikipedia :cite:p:`WikipediaMat104a`,  Wikipedia :cite:p:`WikipediaMat130`.




**Parameters:**


:Query:     Required. A string specifying which items of the result section should be computed.

:matB:   Optional. A general n-by-m matrix of the same type as `A`. You need to specify `B` only if you want to solve the linear equation `AX = B`

:threshold:   Optional. The threshold that will be used by certain methods such as rank(). A value of 0 means that the default value (which is determined internally) will be used.

:preconditioner:   Optional. A string specifying the the type of QR decomposition that will be used internally for the R-SVD step for non-square matrices. See discussion of possible values below.




**Results:**

:absdet:     A scalar of a return type matching `A`. The absolute value of the determinant of `A`.

:rank:     An integer. The rank of `A`.

:X:     A general matrix of the same type and dimension as `B`. The solution to `AX = B`.

:pseudoInverse:     A square matrix of the same type and dimension as `A`. The pseudo-inverse of `A, A^{-1}`.


:SV:     A vector of the same type`A`. The singular values `A` (see below).

:thinU:     A square matrix of the same type and dimension as `A`. The thin singular vectors `U` (see below).

:thinV:     A square matrix of the same type and dimension as `A`. The thin singular vectors `V` (see below).

:fullU:     A square matrix of the same type and dimension as `A`. The full singular vectors `U` (see below).

:fullV:     A square matrix of the same type and dimension as `A`. The full singular vectors `V` (see below).




SVD decomposition consists in decomposing any n-by-p matrix A as a product

`A = USV*`

where U is a n-by-n unitary, V is a p-by-p unitary, and S is a n-by-p real positive matrix which is zero outside of its main diagonal; the diagonal entries of S are known as the singular values of A and the columns of U and V are known as the left and right singular vectors of A respectively. Singular values are always sorted in decreasing order.

This JacobiSVD decomposition computes only singular values by default. If you want U or V , you need to
ask for them explicitly.

You can ask for only thin U or V to be computed, meaning the following. In case of a rectangular n-by-p matrix,
letting m be the smaller value among n and p, there are only m singular vectors; the remaining columns of U
and V do not correspond to actual singular vectors. Asking for thin U or V means asking for only their m first
columns to be formed. So U is then a n-by-m matrix, and V is then a p-by-m matrix. Notice that thin U and V
are all you need for (least squares) solving.

This JacobiSVD class is a two-sided Jacobi R-SVD decomposition, ensuring optimal reliability and accuracy. The downside is that it’s slower than bidiagonalizing SVD algorithms for large square matrices; however its complexity is still where n is the smaller dimension and p is the greater dimension, meaning that it is still of the same order of complexity as the faster bidiagonalizing R-SVD algorithms. In particular, like any R-SVD, it takes advantage of non-squareness in that its complexity is only linear in the greater dimension.

If the input matrix has inf or nan coefficients, the result of the computation is undefined, but the computation is guaranteed to terminate in finite (and reasonable) time.

The possible values for QRPreconditioner are:


• ColPivHouseholderQRPreconditioner is the default. In practice it’s very safe. It uses column-pivoting QR.

• FullPivHouseholderQRPreconditioner, is the safest and slowest. It uses full-pivoting QR. Contrary to other QRs, it doesn’t allow computing thin unitaries.

• HouseholderQRPreconditioner is the fastest, and less safe and accurate than the pivoting variants. It uses non-pivoting QR. This is very similar in safety and accuracy to the bidiagonalization process used by bidiagonalizing SVD algorithms (since bidiagonalization is inherently non-pivoting). However the resulting SVD is still more reliable than bidiagonalizing SVDs because the Jacobi-based iterarive process is more reliable than the optimized bidiagonal SVD iterations.

• NoQRPreconditioner allows not to use a QR preconditioner at all. This is useful if you know that you will only be computing JacobiSVD decompositions of square matrices. Non-square matrices require a QR preconditioner. Using this option will result in faster compilation and smaller executable code. It won’t significantly speed up computation, since JacobiSVD is always checking if QR preconditioning is needed before applying it anyway.

const internal::solve retval¡JacobiSVD, Rhs¿ solve ( const MatrixBase¡ Rhs ¿ & b) const
Returns a (least squares) solution of using the current SVD decomposition of A. Parameters: b the right-hand-side of the equation to solve.

Note: Solving requires both U and V to be computed. Thin U and V are enough, there is no need for full U or V. SVD solving is implicitly least-squares. Thus, this method serves both purposes of exact solving and least-squaressolving. In other words, the returned solution is guaranteed to minimize the Euclidean norm `||Ax - b||.`






Example for a real matrix: the singular values, pseudoinverse and full singular vectors


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

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

    >>> Query = "rank, nonzeros, S, U, V, X, PseudoInverse, SPlus"
    >>> Res = A.eigen_jacobiSvdFull(Query, B)

    >>> print("rank         : ", Res["rank"])
    rank         :  6
    >>> print("nonzeros: ", Res["nonzeros"])
    nonzeropivots:  6

    >>> Res["S"].show("Singular values")
    Singular values: 
      169, 
     58.6, 
     44.1, 
     15.2, 
     7.75, 
    0.950, 

    >>> Res["U"].show("U")
    U: 
      0.435,  -0.390,   0.336,  -0.697,  -0.243, -0.0356, 
      0.238,  -0.526,   0.374,   0.680,  -0.132,  -0.220, 
      0.439,   0.204,   0.280,   0.153,   0.296,   0.759, 
      0.337,  0.0890,  -0.509,   0.161,  -0.737,   0.224, 
      0.460,  -0.310,  -0.610, -0.0138,   0.541,  -0.165, 
      0.486,   0.653,   0.194,  0.0550,  0.0143,  -0.544, 

    >>> Res["V"].show("V")
    V: 
       0.370,   -0.615,    0.580,    0.226,   -0.303,  -0.0706, 
       0.591,    0.117,   -0.297,   -0.551,   -0.442,   -0.223, 
       0.290,   -0.527,   -0.261,   -0.271,    0.692,    0.135, 
       0.283,    0.466,    0.563,   -0.127,    0.473,   -0.382, 
       0.419,    0.114,   -0.418,    0.737,   0.0986,   -0.288, 
       0.416,    0.317,    0.125,    0.112, -0.00594,    0.836, 


    >>> # Checking the properties of the decomposition
    >>> (Res["U"] * Res["S"].D * Res["V"].H).show("U * S.D * V.H (should be equal to A)")
    U * S.D * V.H (should be equal to A): 
     48.0,  43.0,  31.0,  19.0,  14.0,  24.0, 
     46.0,  10.0,  20.0,  4.60,  14.0,  10.0, 
     27.0,  39.0,  13.0,  34.0,  29.0,  37.0, 
     7.10,  42.0,  15.0,  2.80,  35.0,  23.0, 
     23.0,  50.0,  42.0, 0.440,  42.0,  23.0, 
     12.0,  50.0,  1.20,  46.0,  36.0,  47.0, 

    >>> CheckResult = (A - Res["U"] * Res["S"].D * Res["V"].H).norm()
    >>> print("||A - U * S.D * V.H|| (should be zero): ", CheckResult)
    ||A - U * S.D * V.H|| (should be zero):  8.10412857745976288505205302405511259E-33


    >>> # Checking the properties of the pseudoinverse
    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00593, 
     0.0171, 
     0.0227, 
     0.0657, 
      0.129, 
       1.05, 

    >>> Pinv = Res["V"] * Res["SPlus"].D * Res["U"].H; Pinv.show("Pinv = V * SPlus.D * U.H")
    Pinv = V * SPlus.D * U.H: 
     0.0113,  0.0426, -0.0633, 0.00768, -0.0128,  0.0375, 
     0.0459,  0.0319,  -0.201, -0.0115,  0.0136,   0.127, 
    -0.0121, -0.0523,   0.129, -0.0340,  0.0322, -0.0835, 
    0.00719,  0.0757,  -0.283,  -0.141,  0.0901,   0.228, 
    -0.0289,  0.0940,  -0.220, -0.0636,  0.0627,   0.169, 
    -0.0363,  -0.190,   0.672,   0.198,  -0.148,  -0.473, 

    >>> CheckResult = (Pinv - Res["PseudoInverse"]).norm()
    >>> print("||Pinv - PseudoInverse|| (should be zero): ", CheckResult)
    ||Pinv - PseudoInverse|| (should be zero):  2.28256434739527113292893309427326250E-36

    >>> CheckResult = (A - A * Pinv * A).norm()
    >>> print("||A - A * Pinv * A|| (should be zero): ", CheckResult)
    ||A - A * Pinv * A|| (should be zero):  8.98434059906457464441658519736727490E-33



    >>> # Checking the properties of the solution x
    >>> XPlus = Pinv * B; XPlus.show("XPlus")
    XPlus: 
     21.6,  21.7,  21.7,  21.7,  21.7,  21.8, 
     8.21,  8.22,  8.22,  8.23,  8.23,  8.24, 
    -20.5, -20.6, -20.6, -20.6, -20.6, -20.6, 
    -15.3, -15.3, -15.4, -15.4, -15.4, -15.4, 
     16.9,  16.9,  17.0,  17.0,  17.0,  17.0, 
     8.73,  8.76,  8.78,  8.80,  8.82,  8.85, 

    >>> CheckResult = (XPlus - Res["X"]).norm()
    >>> print("||XPlus - X]|| (should be zero): ", CheckResult)
    ||XPlus - X]|| (should be zero):  5.95971475827492938580034754683669071E-33

    >>> CheckResult = (B - A * Res["X"]).norm()
    >>> print("||B - A * X|| (should be zero): ", CheckResult)
    ||B - A * X|| (should be zero):  4.85901224530253679417394342131061588E-32



    >>> # Checking the relationship to the eigenvalues of A * A.H 
    >>> C = A * A.H if (A.rows > A.cols) else A.H * A
    >>> D = C.eigen_SelfAdjointEigenSystem2("eval")["eval"]; D.show("D: Eigenvalues of A * A.H")
    D: Eigenvalues of A * A.H: 
      0.902, 
       60.0, 
        232, 
    1.94E+3, 
    3.43E+3, 
    2.85E+4, 

    >>> E = (Res["S"].cwiseProduct(Res["S"])).reverse_full()
    >>> E.show("E: Squared singular values, in ascending order")
    E: Squared singular values, in ascending order: 
      0.902, 
       60.0, 
        232, 
    1.94E+3, 
    3.43E+3, 
    2.85E+4, 

    >>> (D - E).show("D-E (should be a zero vector)")
    D-E (should be a zero vector): 
    -1.48E-32, 
    -3.34E-32, 
     -5.4E-32, 
     -1.3E-31, 
     -4.1E-31, 
        4E-31, 







Example for a complex matrix: the singular values, pseudoinverse and full singular vectors
............................................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")
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

    >>> Query = "rank, nonzeros, S, U, V, X, PseudoInverse, SPlus"
    >>> Res = A.eigen_jacobiSvdThin(Query, B)

    >>> print("rank         : ", Res["rank"])
    rank         :  4
    >>> print("nonzeros: ", Res["nonzeros"])
    nonzeropivots:  4

    >>> Res["S"].show("Singular values")
    Singular values: 
     163 + 0j, 
    54.2 + 0j, 
    39.9 + 0j, 
    3.63 + 0j, 

    >>> Res["U"].show("U")
    U: 
     -0.430 - 0.102j,   0.409 - 0.250j,  0.585 - 0.0708j,  -0.324 + 0.348j, 
     -0.476 - 0.153j, -0.582 + 0.0348j,  -0.170 - 0.215j,  -0.546 - 0.190j, 
    -0.617 - 0.0410j,  0.0954 - 0.293j,  -0.386 + 0.495j,  0.359 - 0.0131j, 
     -0.375 - 0.176j, -0.0724 + 0.574j,   0.349 - 0.247j,   0.534 - 0.159j, 

    >>> Res["V"].show("V")
    V: 
      -0.437 + 0.150j,    0.592 + 0.283j,    0.274 - 0.230j, -0.478 + 0.00322j, 
      -0.383 + 0.383j,  -0.556 - 0.0490j,   -0.250 + 0.254j,  -0.513 + 0.0673j, 
      -0.411 + 0.231j,    0.214 + 0.327j,  -0.572 + 0.0914j,   0.537 - 0.0308j, 
      -0.425 + 0.300j,   -0.237 - 0.221j,   0.634 - 0.0880j,   0.463 - 0.0218j, 


    >>> # Checking the properties of the decomposition
    >>> (Res["U"] * Res["S"].D * Res["V"].H).show("U * S.D * V.H (should be equal to A)")
    U * S.D * V.H (should be equal to A): 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 

    >>> CheckResult = (A - Res["U"] * Res["S"].D * Res["V"].H).norm()
    >>> print("||A - U * S.D * V.H|| (should be zero): ", CheckResult)
    ||A - U * S.D * V.H|| (should be zero):  7.23797623649041832083182110841296889E-33 + 0j


    >>> # Checking the properties of the pseudoinverse
    >>> Res["SPlus"].show("SPlus")
    SPlus: 
    0.00615 + 0j, 
     0.0185 + 0j, 
     0.0250 + 0j, 
      0.275 + 0j, 

    >>> Pinv = Res["V"] * Res["SPlus"].D * Res["U"].H; Pinv.show("Pinv = V * SPlus.D * U.H")
    Pinv = V * SPlus.D * U.H: 
       0.0516 + 0.0468j,    0.0667 - 0.0273j, -0.0516 + 0.000462j,   -0.0635 - 0.0282j, 
       0.0449 + 0.0423j,    0.0801 - 0.0400j, -0.0447 + 0.000795j,  -0.0814 - 0.00721j, 
      -0.0583 - 0.0458j,   -0.0783 + 0.0245j,   0.0599 + 0.00584j,    0.0786 + 0.0125j, 
      -0.0338 - 0.0465j,   -0.0674 + 0.0325j,    0.0409 - 0.0104j,    0.0738 + 0.0219j, 

    >>> CheckResult = (Pinv - Res["PseudoInverse"]).norm()
    >>> print("||Pinv - PseudoInverse|| (should be zero): ", CheckResult)
    ||Pinv - PseudoInverse|| (should be zero):  6.32060123722419305732811075240482494E-37 + 0j

    >>> CheckResult = (A - A * Pinv * A).norm()
    >>> print("||A - A * Pinv * A|| (should be zero): ", CheckResult)
    ||A - A * Pinv * A|| (should be zero):  4.78955112719344504545703109417795418E-33 + 0j



    >>> # Checking the properties of the solution x
    >>> XPlus = Pinv * B; XPlus.show("XPlus")
    XPlus: 
    -0.869 - 3.37j, -0.858 - 3.37j, -0.846 - 3.38j, -0.835 - 3.38j, 
     -1.82 - 3.22j,  -1.82 - 3.22j,  -1.82 - 3.23j,  -1.81 - 3.23j, 
      2.15 + 3.53j,   2.15 + 3.53j,   2.16 + 3.53j,   2.16 + 3.53j, 
      1.81 + 3.52j,   1.82 + 3.53j,   1.84 + 3.54j,   1.86 + 3.55j, 

    >>> CheckResult = (XPlus - Res["X"]).norm()
    >>> print("||XPlus - X]|| (should be zero): ", CheckResult)
    ||XPlus - X]|| (should be zero):  8.35763124336076459797867686951053026E-35 + 0j

    >>> CheckResult = (B - A * Res["X"]).norm()
    >>> print("||B - A * X|| (should be zero): ", CheckResult)
    ||B - A * X|| (should be zero):  8.25590697622011727085329191499069154E-33 + 0j



    >>> # Checking the relationship to the eigenvalues of A * A.H 
    >>> C = A * A.H if (A.rows > A.cols) else A.H * A
    >>> D = C.eigen_SelfAdjointEigenSystem2("eval")["eval"]; D.show("D: Eigenvalues of A * A.H")
    D: Eigenvalues of A * A.H: 
       13.2 + 0j, 
    1.60E+3 + 0j, 
    2.93E+3 + 0j, 
    2.65E+4 + 0j, 

    >>> E = (Res["S"].cwiseProduct(Res["S"])).reverse_full(); 
    >>> E.show("E: Squared singular values, in ascending order")
    E: Squared singular values, in ascending order: 
       13.2 + 0j, 
    1.60E+3 + 0j, 
    2.93E+3 + 0j, 
    2.65E+4 + 0j, 

    >>> (D - E).show("D-E (should be a zero vector)")
    D-E (should be a zero vector): 
    -5.10E-33 + 0j, 
    -1.40E-31 + 0j, 
     2.40E-31 + 0j, 
     7.00E-31 + 0j, 









|newpage|


Symmetric/Hermitian Eigensystem, only eigen values
------------------------------------------------------------

.. method:: mat.SelfAdjointEigenValues(Query)


    Returns the eigendecomposition of the symmetric/hermitian matrix *matA* `=A`.


    See also Eigen :cite:p:`EigenMat110`,  Wikipedia :cite:p:`WikipediaMat112`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.





**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**


:info:   Reports whether previous computation was successful.


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.


:sqrt:   Returns the positive-definite square root of the matrix

:inversesqrt:   Returns the inverse square root of the matrix



A matrix A is selfadjoint if it equals its adjoint. For real matrices, this means that the matrix is symmetric: it equals its transpose. This class computes the eigenvalues and eigenvectors of a selfadjoint matrix. These are the scalars `\lambda` and vectors `v` such that `Av = \lambda v.` The eigenvalues of a selfadjoint matrix are always real. If `D` is a diagonal matrix with the eigenvalues on the diagonal, and `V` is a matrix with the eigenvectors as its columns, then `A = V DV^{-1}` (for selfadjoint matrices, the matrix `V` is always invertible). This is called the eigendecomposition. The algorithm exploits the fact that the matrix is selfadjoint, making it faster and more accurate than the general purpose eigenvalue algorithms implemented in EigenSolver and ComplexEigenSolver. Only the lower triangular part of the input matrix is referenced.

Call the function compute() to compute the eigenvalues and eigenvectors of a given matrix. Alternatively, you can use the SelfAdjointEigenSolver(const MatrixType, int) constructor which computes the eigenvalues and eigenvectors at construction time. Once the eigenvalue and eigenvectors are computed, they can be retrieved with the eigenvalues() and eigenvectors() functions. The documentation for SelfAdjointEigenSolver(const MatrixType, int) contains an example of the typical use of this class.

To solve the generalized eigenvalue problem `Av = \lambda B v` and the likes, see the class GeneralizedSelfAdjointEigenSolver. This implementation uses a symmetric QR algorithm. The matrix is first reduced to tridiagonal form using the Tridiagonalization class. The tridiagonal matrix is then brought to diagonal form with implicit symmetric QR steps with Wilkinson shift. Details can be found in Section 8.3 of Golub & Van Loan (1996). The cost of the computation is about 9n3 if the eigenvectors are required and 4n3/3 if they are not required.



Example for a real symmetric matrix: only eigenvalues
...............................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
    A: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> Query = "Eval"
    >>> Res = A.eigen_SelfAdjointEigenValues2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i   L[i]  
    0: -61.7, 
    1: -27.7, 
    2:  4.34, 
    3:  25.8, 
    4:  62.5, 
    5:   311, 

    >>> X = +A; #X.show("X")
    >>> AD = X.diagonal(); #AD.show("AD")
    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X.set_diagonal(0, AD - L[i])
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - I * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - I * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - I * L[i]) should be zero): 
    i   L[i]  Det(A - I * L[i])  
    0: -61.7,          3.71E-23, 
    1: -27.7,          7.41E-25, 
    2:  4.34,         -1.22E-25, 
    3:  25.8,          2.76E-25, 
    4:  62.5,         -2.13E-23, 
    5:   311,          1.24E-20, 




Example for a hermitian matrix: only eigenvalues
...............................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")
    A: 
       80.0 + 0j, 50.0 - 23.0j, 85.0 + 5.00j, 36.0 - 4.30j, 
    50.0 + 23.0j,    30.0 + 0j, 43.0 + 9.50j, 27.0 + 11.0j, 
    85.0 - 5.00j, 43.0 - 9.50j,    85.0 + 0j, 55.0 - 7.00j, 
    36.0 + 4.30j, 27.0 - 11.0j, 55.0 + 7.00j,    23.0 + 0j, 

    Query = "Eval"
    Res = A.eigen_SelfAdjointEigenValues2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i        L[i]  
    0: -21.6 + 0j, 
    1:  3.50 + 0j, 
    2:  14.1 + 0j, 
    3:   222 + 0j, 

    >>> X = +A; #X.show("X")
    >>> AD = X.diagonal(); #AD.show("AD")
    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X.set_diagonal(0, AD - L[i])
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - I * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - I * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - I * L[i]) should be zero): 
    i        L[i]      Det(A - I * L[i])  
    0: -21.6 + 0j,  5.65E-29 + 4.39E-30j, 
    1:  3.50 + 0j,  1.82E-29 - 2.71E-30j, 
    2:  14.1 + 0j, -1.40E-29 - 2.14E-30j, 
    3:   222 + 0j,  2.52E-26 - 5.79E-28j, 





|newpage|


Symmetric/Hermitian Eigensystem, eigenvalues and eigenvectors
-----------------------------------------------------------------

.. method:: mat.SelfAdjointEigenSystem(Query)


    Returns the eigendecomposition of the symmetric/hermitian matrix *matA* `=A`.


    See also Eigen :cite:p:`EigenMat110`,  Wikipedia :cite:p:`WikipediaMat112`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.





**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**


:info:   Reports whether previous computation was successful.


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.


:sqrt:   Returns the positive-definite square root of the matrix

:inversesqrt:   Returns the inverse square root of the matrix




Example for a real symmetric matrix: eigenvalues and eigenvectors
......................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
    A: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    Query = "Eval, Evec"
    Res = A.eigen_SelfAdjointEigenSystem2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i   L[i]  
    0: -61.7, 
    1: -27.7, 
    2:  4.34, 
    3:  25.8, 
    4:  62.5, 
    5:   311, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors (V0, ... , V5): 
          V0       V1       V2      V3      V4     V5  
      0.0719,  -0.497,  -0.271,  0.730, -0.157, 0.343, 
      -0.550,  -0.562,  0.0403, -0.473, 0.0957, 0.382, 
      -0.277,   0.514,  -0.515, 0.0931,  0.464, 0.412, 
       0.744, -0.0396, -0.0409, -0.370, 0.0252, 0.553, 
    0.000270,  0.0462,   0.760,  0.310,  0.515, 0.243, 
      -0.249,   0.410,   0.284, 0.0486, -0.697, 0.449, 

    >>> CheckResult = (A - V * L.D * V.eigen_inverse()).norm()
    >>> print("||A - V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
        ||A - V * diag(L) * V^-1|| (should be zero):  7.70E-33

    >>> X = +A; #X.show("X")
    >>> AD = X.diagonal(); #AD.show("AD")
    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X.set_diagonal(0, AD - L[i])
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - I * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - I * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - I * L[i]) should be zero): 
    i   L[i]  Det(A - I * L[i])  
    0: -61.7,            -0E-34, 
    1: -27.7,            -0E-34, 
    2:  4.34,             0E-35, 
    3:  25.8,             0E-34, 
    4:  62.5,             0E-34, 
    5:   311,             0E-33, 


    >>> for i in range(V.rows):
    >>>     AV = AC * V.col(i); VL = V.col(i) * L[i]; X = AV - VL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(VL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - VL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "VL = " + Vi + " * " + Li, "AV - VL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  -61.7
    Checking the properties of eigenvector V0 (AV - VL should be a zero vector): 
    Eigenvector V0  AV = A * V0  VL = V0 * L[0]   AV - VL  
            0.0719,       -4.44,          -4.44,  3.7E-34, 
            -0.550,        33.9,           33.9, -2.2E-33, 
            -0.277,        17.1,           17.1,    3E-34, 
             0.744,       -45.9,          -45.9,  2.9E-33, 
          0.000270,     -0.0166,        -0.0166, 6.52E-34, 
            -0.249,        15.4,           15.4, -1.5E-33, 

    Eigenvalue L[1]:  -27.7
    Checking the properties of eigenvector V1 (AV - VL should be a zero vector): 
    Eigenvector V1  AV = A * V1  VL = V1 * L[1]   AV - VL  
            -0.497,        13.8,           13.8,    0E-34, 
            -0.562,        15.6,           15.6,    0E-34, 
             0.514,       -14.3,          -14.3,   -2E-34, 
           -0.0396,        1.10,           1.10, -3.4E-34, 
            0.0462,       -1.28,          -1.28,    7E-35, 
             0.410,       -11.4,          -11.4,   -6E-34, 

    Eigenvalue L[2]:  4.34
    Checking the properties of eigenvector V2 (AV - VL should be a zero vector): 
    Eigenvector V2  AV = A * V2  VL = V2 * L[2]    AV - VL  
            -0.271,       -1.17,          -1.17,    -4E-35, 
            0.0403,       0.175,          0.175,   9.9E-35, 
            -0.515,       -2.23,          -2.23,   2.4E-34, 
           -0.0409,      -0.177,         -0.177, -4.07E-34, 
             0.760,        3.30,           3.30,    -7E-35, 
             0.284,        1.23,           1.23,     4E-35, 

    Eigenvalue L[3]:  25.8
    Checking the properties of eigenvector V3 (AV - VL should be a zero vector): 
    Eigenvector V3  AV = A * V3  VL = V3 * L[3]  AV - VL  
             0.730,        18.8,           18.8,   1E-34, 
            -0.473,       -12.2,          -12.2,   6E-34, 
            0.0931,        2.40,           2.40, 2.8E-34, 
            -0.370,       -9.54,          -9.54, 7.1E-34, 
             0.310,        7.99,           7.99, 2.6E-34, 
            0.0486,        1.25,           1.25,   2E-35, 

    Eigenvalue L[4]:  62.5
    Checking the properties of eigenvector V4 (AV - VL should be a zero vector): 
    Eigenvector V4  AV = A * V4  VL = V4 * L[4]   AV - VL  
            -0.157,       -9.78,          -9.78, 1.05E-33, 
            0.0957,        5.98,           5.98, -6.2E-34, 
             0.464,        29.0,           29.0, -1.6E-33, 
            0.0252,        1.58,           1.58,  1.5E-34, 
             0.515,        32.2,           32.2, -1.8E-33, 
            -0.697,       -43.5,          -43.5,  2.6E-33, 

    Eigenvalue L[5]:  311
    Checking the properties of eigenvector V5 (AV - VL should be a zero vector): 
    Eigenvector V5  AV = A * V5  VL = V5 * L[5]   AV - VL  
             0.343,         106,            106,   -1E-33, 
             0.382,         119,            119,   -3E-33, 
             0.412,         128,            128,   -2E-33, 
             0.553,         172,            172,   -4E-33, 
             0.243,        75.5,           75.5, -1.8E-33, 
             0.449,         140,            140,   -1E-33, 





Example for a hermitian matrix: eigenvalues and eigenvectors
...............................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A")
    A: 
       80.0 + 0j, 50.0 - 23.0j, 85.0 + 5.00j, 36.0 - 4.30j, 
    50.0 + 23.0j,    30.0 + 0j, 43.0 + 9.50j, 27.0 + 11.0j, 
    85.0 - 5.00j, 43.0 - 9.50j,    85.0 + 0j, 55.0 - 7.00j, 
    36.0 + 4.30j, 27.0 - 11.0j, 55.0 + 7.00j,    23.0 + 0j, 

    Query = "Eval, Evec"
    Res = A.eigen_SelfAdjointEigenSystem2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i        L[i]  
    0: -21.6 + 0j, 
    1:  3.50 + 0j, 
    2:  14.1 + 0j, 
    3:   222 + 0j, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors (V0, ... , V3): 
                 V0                V1               V2               V3  
         0.458 + 0j,      -0.419 + 0j,     -0.502 + 0j,      0.602 + 0j, 
    -0.305 - 0.364j,   0.473 + 0.350j, -0.262 - 0.476j,  0.343 + 0.124j, 
    -0.472 + 0.234j, -0.225 + 0.0826j,  0.506 + 0.130j, 0.626 - 0.0122j, 
     0.523 - 0.113j,   0.586 - 0.278j,  0.390 + 0.164j, 0.336 + 0.0294j, 

    >>> AC = +A
    >>> CheckResult = (AC - V * L.D * V.eigen_inverse()).norm().real
    >>> print("||A - V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - V * diag(L) * V^-1|| (should be zero):  3.35E-33

    >>> X = +A; #X.show("X")
    >>> AD = X.diagonal(); #AD.show("AD")
    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X.set_diagonal(0, AD - L[i])
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - I * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - I * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - I * L[i]) should be zero): 
    i        L[i]      Det(A - I * L[i])  
    0: -21.6 + 0j,  5.65E-29 + 4.39E-30j, 
    1:  3.50 + 0j,  1.82E-29 - 2.71E-30j, 
    2:  14.1 + 0j, -1.40E-29 - 2.14E-30j, 
    3:   222 + 0j,  2.52E-26 - 5.79E-28j, 


    >>> for i in range(V.rows):
    >>>     AV = AC * V.col(i); VL = V.col(i) * L[i]; X = AV - VL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(VL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - VL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "VL = " + Vi + " * " + Li, "AV - VL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  -21.6 + 0j
    Checking the properties of eigenvector V0 (AV - VL should be a zero vector): 
     Eigenvector V0        AV = A * V0  VL = V0 * L[0]                AV - VL  
         0.458 + 0j, -9.92 + 5.00E-35j,     -9.92 + 0j, -1.90E-34 + 5.00E-35j, 
    -0.305 - 0.364j,      6.61 + 7.88j,   6.61 + 7.88j, -7.00E-34 - 3.60E-34j, 
    -0.472 + 0.234j,      10.2 - 5.06j,   10.2 - 5.06j, -2.00E-34 + 1.40E-34j, 
     0.523 - 0.113j,     -11.3 + 2.45j,  -11.3 + 2.45j,  5.00E-34 + 1.00E-34j, 

    Eigenvalue L[1]:  3.50 + 0j
    Checking the properties of eigenvector V1 (AV - VL should be a zero vector): 
      Eigenvector V1      AV = A * V1   VL = V1 * L[1]                AV - VL  
         -0.419 + 0j,      -1.47 + 0j,      -1.47 + 0j,         2.90E-34 + 0j, 
      0.473 + 0.350j,    1.66 + 1.23j,    1.66 + 1.23j,  1.00E-35 + 2.50E-34j, 
    -0.225 + 0.0826j, -0.789 + 0.290j, -0.789 + 0.290j,  6.30E-35 + 1.43E-34j, 
      0.586 - 0.278j,   2.06 - 0.974j,   2.06 - 0.974j, -3.70E-34 + 1.53E-34j, 

    Eigenvalue L[2]:  14.1 + 0j
    Checking the properties of eigenvector V2 (AV - VL should be a zero vector): 
     Eigenvector V2        AV = A * V2  VL = V2 * L[2]                AV - VL  
        -0.502 + 0j, -7.10 - 3.20E-34j,     -7.10 + 0j,  2.30E-34 - 3.20E-34j, 
    -0.262 - 0.476j,     -3.70 - 6.73j,  -3.70 - 6.73j, -1.70E-34 - 6.20E-34j, 
     0.506 + 0.130j,      7.16 + 1.83j,   7.16 + 1.83j, -3.10E-34 - 5.00E-34j, 
     0.390 + 0.164j,      5.52 + 2.32j,   5.52 + 2.32j, -1.20E-34 - 1.90E-34j, 

    Eigenvalue L[3]:  222 + 0j
    Checking the properties of eigenvector V3 (AV - VL should be a zero vector): 
     Eigenvector V3      AV = A * V3  VL = V3 * L[3]                AV - VL  
         0.602 + 0j, 134 + 1.40E-34j,       134 + 0j,         0 + 1.40E-34j, 
     0.343 + 0.124j,    76.1 + 27.4j,   76.1 + 27.4j, -1.20E-33 - 8.00E-34j, 
    0.626 - 0.0122j,     139 - 2.72j,    139 - 2.72j, -1.00E-33 + 7.00E-35j, 
    0.336 + 0.0294j,    74.5 + 6.54j,   74.5 + 6.54j, -1.20E-33 + 1.10E-34j, 




|newpage|


Generalized Selfadjoint Eigensystem, only eigenvalues
--------------------------------------------------------

.. method:: mat.GeneralizedSelfAdjointEigenValues(Query)


    Returns the eigendecomposition of a generalized selfadjoint eigensystem.


    See also Eigen :cite:p:`EigenMat122`,  Wikipedia :cite:p:`WikipediaMat123`,  Wikipedia :cite:p:`WikipediaMat130`,  Wikipedia :cite:p:`WikipediaMat112b`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.



**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.



The generalized eigenvalues and eigenvectors of a matrix pair `A` and `B` are scalars `\lambda` and vectors `v` such that `Av = \lambda Bv`. If `D` is a diagonal matrix with the eigenvalues on the diagonal, and `V` is a matrix with the eigenvectors as its columns, then `AV = BV D`. The matrix `V` is almost always invertible, in which case we have `A = BV DV^{-1}`. This is called the generalized eigen-decomposition.



This class solves the generalized eigenvalue problem `Av =  \lambda Bv`. In this case, the matrix `A` should be selfadjoint and the matrix `B` should be positive definite. Only the lower triangular part of the input matrix is referenced.

Parameters:
[in] matA Selfadjoint matrix in matrix pencil. Only the lower triangular part of the matrix is referenced.
[in] matB Positive-definite matrix in matrix pencil. Only the lower triangular part of the matrix is referenced.
[in] options A or-ed set of flags ComputeEigenvectors,EigenvaluesOnly - ``Ax_lBx,ABx_lx,BAx_lx``. Default is
ComputeEigenvectors ``Ax_lBx``.

Computes the eigenvalues and (if requested) the eigenvectors of the generalized eigenproblem `Ax = \lambda Bx` with
matA the selfadjoint matrix A and matB the positive definite matrix B. Each eigenvector x satisfies the property
`x^T B x = 1`. The eigenvectors are computed if options contains ComputeEigenvectors. In addition, the two following variants can be solved via options:

``ABx_lx``: `ABx =  \lambda x`

``BAx_lx``: `BAx =  \lambda x`

Computes generalized eigendecomposition of given matrix pencil. 
Parameters [in] matA Selfadjoint matrix in matrix pencil. Only the lower triangular part of the matrix is referenced. 
[in] matB Positive-definite matrix in matrix pencil. Only the lower triangular part of the matrix is referenced.
[in] options A or-ed set of flags

ComputeEigenvectors,EigenvaluesOnly  ``Ax_lBx,ABx_lx,BAx_lx``. Default is ComputeEigenvectors ``Ax_lBx``.
According to options, this function computes eigenvalues and (if requested) the eigenvectors of one of the following three generalized eigenproblems:

``Ax_lBx``: `Ax = \lambda Bx`

``ABx_lx``: `ABx = \lambda x`

``BAx_lx``: `BAx = \lambda x`

with matA the selfadjoint matrix A and matB the positive definite matrix B. In addition, each eigenvector satisfies the property `x*Bx = 1`.The eigenvalues() function can be used to retrieve the eigenvalues. If options contains ComputeEigenvectors, then the eigenvectors are also computed and can be retrieved by calling eigenvectors().

The implementation uses LLT to compute the Cholesky decomposition `B = LL^T` and computes the classical eigendecomposition of the selfadjoint matrix L^{-1} A(L*)^{-1} if options contains ``Ax_lBx`` and of `L*AL` otherwise. This solves the generalized eigenproblem, because any solution of the generalized eigenproblem Ax =  \lambda Bx corresponds to a solution `L^{-1} A(L*)^{-1} (L*x) =  \lambda (L*x)` of the eigenproblem for `L^{-1} A(L*)^{-1}.` Similar statements can be made for the two other variants.







Example for a real symmetric matrix: eigenvalues only
.................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAPosDefB6x6", "")
    >>> A.show("A (real symmetric)")
    A (real symmetric): 
    60, 58, 65, 68, 23, 45, 
    58, 63, 65, 70, 20, 48, 
    65, 65, 88, 85, 33, 50, 
    68, 70, 85, 95, 35, 58, 
    23, 20, 33, 35, 25, 17, 
    45, 48, 50, 58, 17, 45, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAPosDefA6x6", "")
    >>> B.show("B (real symmetric positive definite)")
    B (real symmetric positive definite): 
    248,  40,  38,  43,  33,  35, 
     40, 240,  25,  38,  28,  35, 
     38,  25, 245,  40,  33,  17, 
     43,  38,  40, 250,  30,  33, 
     33,  28,  33,  30, 240,  22, 
     35,  35,  17,  33,  22, 243, 

    >>> Query = "Eval"
    >>> Res = A.eigen_GeneralizedSelfAdjointEigenValues2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i    L[i]  
    0: 0.0114, 
    1: 0.0163, 
    2: 0.0282, 
    3: 0.0455, 
    4: 0.0952, 
    5:  0.850, 
    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = A - B * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i    L[i]  Det(A - B * L[i])  
    0: 0.0114,         -3.12E-29, 
    1: 0.0163,         -1.30E-30, 
    2: 0.0282,         -6.39E-29, 
    3: 0.0455,          2.67E-28, 
    4: 0.0952,         -7.75E-27, 
    5:  0.850,          1.43E-21, 





Example for a hermitian matrix: eigenvalues only
.................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A (hermitian)")
    A (hermitian): 
       91.0 + 0j, 12.0 - 3.60j, 22.0 - 7.40j, 14.0 + 1.10j, 
    12.0 + 3.60j,    77.0 + 0j, 2.50 - 2.00j, 3.40 - 7.60j, 
    22.0 + 7.40j, 2.50 + 2.00j,    91.0 + 0j, 17.0 + 3.70j, 
    14.0 - 1.10j, 3.40 + 7.60j, 17.0 - 3.70j,    74.0 + 0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefB6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B (hermitian positive definite)")
    B (hermitian positive definite): 
       85.0 + 0j, 7.30 + 1.40j, 9.20 + 2.30j, 3.10 + 1.80j, 
    7.30 - 1.40j,    73.0 + 0j, 19.0 - 1.80j, 3.70 + 2.00j, 
    9.20 - 2.30j, 19.0 + 1.80j,    89.0 + 0j, 13.0 - 8.30j, 
    3.10 - 1.80j, 3.70 - 2.00j, 13.0 + 8.30j,    84.0 + 0j, 

    >>> Query = "Eval"
    >>> Res = A.eigen_GeneralizedSelfAdjointEigenValues2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    i       L[i]  
    0: 57.8 + 0j, 
    1: 67.0 + 0j, 
    2: 81.6 + 0j, 
    3:  127 + 0j, 

    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = A - B * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i       L[i]     Det(A - B * L[i])  
    0: 57.8 + 0j, 4.30E+14 + 2.49E-23j, 
    1: 67.0 + 0j, 7.87E+14 + 5.51E-23j, 
    2: 81.6 + 0j, 1.75E+15 + 5.75E-23j, 
    3:  127 + 0j, 1.03E+16 + 1.19E-21j, 





|newpage|


Generalized Selfadjoint Eigensystem: eigenvalues and eigenvectors
------------------------------------------------------------------------------

.. method:: mat.GeneralizedSelfAdjointEigenSystem(Query)


    Returns the eigendecomposition of a generalized selfadjoint eigensystem.


    See also Eigen :cite:p:`EigenMat122`,  Wikipedia :cite:p:`WikipediaMat123`,  Wikipedia :cite:p:`WikipediaMat130`,  Wikipedia :cite:p:`WikipediaMat112b`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.



**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.




Example for a real symmetric matrix: eigenvalues and eigenvectors
.................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAPosDefB6x6", "")
    >>> A.show("A (real symmetric)")
    A (real symmetric): 
    60, 58, 65, 68, 23, 45, 
    58, 63, 65, 70, 20, 48, 
    65, 65, 88, 85, 33, 50, 
    68, 70, 85, 95, 35, 58, 
    23, 20, 33, 35, 25, 17, 
    45, 48, 50, 58, 17, 45, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAPosDefA6x6", "")
    >>> B.show("B (real symmetric positive definite)")
    B (real symmetric positive definite): 
    248,  40,  38,  43,  33,  35, 
     40, 240,  25,  38,  28,  35, 
     38,  25, 245,  40,  33,  17, 
     43,  38,  40, 250,  30,  33, 
     33,  28,  33,  30, 240,  22, 
     35,  35,  17,  33,  22, 243, 

    >>> Query = "Eval, Evec"
    >>> Res = A.eigen_GeneralizedSelfAdjointEigenSolver2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i    L[i]  
    0: 0.0114, 
    1: 0.0163, 
    2: 0.0282, 
    3: 0.0455, 
    4: 0.0952, 
    5:  0.850, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors (V0, ... , V5): 
          V0       V1        V2       V3       V4       V5  
      0.0347, 0.00906,  -0.0464,  0.0197, -0.0160,  0.0172, 
     -0.0472, -0.0274, -0.00784, 0.00953, -0.0293,  0.0215, 
    -0.00569,  0.0245,   0.0310,  0.0386,  0.0196,  0.0292, 
      0.0276, -0.0386,   0.0178, -0.0275,  0.0143,  0.0282, 
     -0.0247, 0.00690,  -0.0328, -0.0181,  0.0481, 0.00121, 
    -0.00467,  0.0434,   0.0104, -0.0400, -0.0216,  0.0157, 

    >>> # Vinv = V^-1 = V.H
    >>> Vinv = V.eigen_inverse(); Vinv.show(" V^-1")
    >>> CheckResult = (A - V * L.D * Vinv).norm()
    >>> print("||A - B * V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - V * diag(L) * V^-1|| (should be zero):  4.59E-33

    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = A - B * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i    L[i]  Det(A - B * L[i])  
    0: 0.0114,         -3.12E-29, 
    1: 0.0163,         -1.30E-30, 
    2: 0.0282,         -6.39E-29, 
    3: 0.0455,          2.67E-28, 
    4: 0.0952,         -7.75E-27, 
    5:  0.850,          1.43E-21, 


    >>> for i in range(V.rows):
    >>>     AV = A * V.col(i); BVL = (B * L[i]) * V.col(i); X = AV - BVL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(BVL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - BVL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "BVL = B * " + Vi + " * " + Li, "   AV - BVL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  0.0114
    Checking the properties of eigenvector V0 (AV - BVL should be a zero vector): 
    Eigenvector V0  AV = A * V0  BVL = B * V0 * L[0]     AV - BVL  
            0.0347,      0.0769,              0.0769,    1.89E-35, 
           -0.0472,      -0.113,              -0.113,     3.6E-35, 
          -0.00569,     -0.0120,             -0.0120,    6.23E-35, 
            0.0276,      0.0627,              0.0627,    4.16E-35, 
           -0.0247,     -0.0637,             -0.0637,    1.67E-35, 
          -0.00467,     -0.0149,             -0.0149,    2.83E-35, 

    Eigenvalue L[1]:  0.0163
    Checking the properties of eigenvector V1 (AV - BVL should be a zero vector): 
    Eigenvector V1  AV = A * V1  BVL = B * V1 * L[1]     AV - BVL  
           0.00906,      0.0354,              0.0354,   -2.30E-35, 
           -0.0274,     -0.0876,             -0.0876,   -1.54E-35, 
            0.0245,      0.0832,              0.0832,     2.3E-36, 
           -0.0386,      -0.125,              -0.125,      -6E-36, 
           0.00690,      0.0293,              0.0293,    -1.1E-36, 
            0.0434,       0.150,               0.150,      -7E-36, 

    Eigenvalue L[2]:  0.0282
    Checking the properties of eigenvector V2 (AV - BVL should be a zero vector): 
    Eigenvector V2  AV = A * V2  BVL = B * V2 * L[2]     AV - BVL  
           -0.0464,      -0.299,              -0.299,     1.5E-35, 
          -0.00784,     -0.0802,             -0.0802,   -1.53E-35, 
            0.0310,       0.154,               0.154,    -3.0E-35, 
            0.0178,      0.0776,              0.0776,   -2.38E-35, 
           -0.0328,      -0.221,              -0.221,     1.1E-35, 
            0.0104,      0.0289,              0.0289,     2.2E-36, 

    Eigenvalue L[3]:  0.0455
    Checking the properties of eigenvector V3 (AV - BVL should be a zero vector): 
    Eigenvector V3  AV = A * V3  BVL = B * V3 * L[3]     AV - BVL  
            0.0197,       0.162,               0.162,    -1.0E-35, 
           0.00953,      0.0497,              0.0497,     3.7E-36, 
            0.0386,       0.368,               0.368,    -2.2E-35, 
           -0.0275,      -0.272,              -0.272,     2.7E-35, 
           -0.0181,      -0.175,              -0.175,     1.0E-35, 
           -0.0400,      -0.425,              -0.425,     1.4E-35, 

    Eigenvalue L[4]:  0.0952
    Checking the properties of eigenvector V4 (AV - BVL should be a zero vector): 
    Eigenvector V4  AV = A * V4  BVL = B * V4 * L[4]     AV - BVL  
           -0.0160,      -0.281,              -0.281,       6E-36, 
           -0.0293,      -0.576,              -0.576,       7E-36, 
            0.0196,       0.500,               0.500,    -4.9E-35, 
            0.0143,       0.313,               0.313,    -1.8E-35, 
            0.0481,        1.03,                1.03,      -4E-35, 
           -0.0216,      -0.473,              -0.473,      -5E-36, 

    Eigenvalue L[5]:  0.850
    Checking the properties of eigenvector V5 (AV - BVL should be a zero vector): 
    Eigenvector V5  AV = A * V5  BVL = B * V5 * L[5]     AV - BVL  
            0.0172,        6.83,                6.83,    -1.5E-34, 
            0.0215,        7.00,                7.00,    -2.1E-34, 
            0.0292,        8.30,                8.30,    -2.5E-34, 
            0.0282,        8.79,                8.79,    -2.2E-34, 
           0.00121,        3.07,                3.07,      -9E-35, 
            0.0157,        5.63,                5.63,    -1.9E-34, 






Example for a hermitian matrix: eigenvalues and eigenvectors
.................................................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A (hermitian)")
    A (hermitian): 
       91.0 + 0j, 12.0 - 3.60j, 22.0 - 7.40j, 14.0 + 1.10j, 
    12.0 + 3.60j,    77.0 + 0j, 2.50 - 2.00j, 3.40 - 7.60j, 
    22.0 + 7.40j, 2.50 + 2.00j,    91.0 + 0j, 17.0 + 3.70j, 
    14.0 - 1.10j, 3.40 + 7.60j, 17.0 - 3.70j,    74.0 + 0j, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAPosDefB6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B (hermitian positive definite)")
    B (hermitian positive definite): 
       85.0 + 0j, 7.30 + 1.40j, 9.20 + 2.30j, 3.10 + 1.80j, 
    7.30 - 1.40j,    73.0 + 0j, 19.0 - 1.80j, 3.70 + 2.00j, 
    9.20 - 2.30j, 19.0 + 1.80j,    89.0 + 0j, 13.0 - 8.30j, 
    3.10 - 1.80j, 3.70 - 2.00j, 13.0 + 8.30j,    84.0 + 0j, 

    >>> Query = "Eval, Evec"
    >>> Res = A.eigen_GeneralizedSelfAdjointEigenSolver2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i        L[i]  
    0: 0.731 + 0j, 
    1: 0.779 + 0j, 
    2:  1.15 + 0j, 
    3:  1.47 + 0j, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors (V0, ... , V3): 
                   V0                   V1                   V2                 V3  
    0.0609 + 0.00995j, -0.0160 - 0.000497j,  -0.0833 + 0.00552j, 0.0307 - 0.00215j, 
    -0.0321 - 0.0508j,   0.00344 - 0.0182j,   -0.0405 - 0.0520j, -0.0529 - 0.0594j, 
    -0.0290 - 0.0350j,    0.0579 - 0.0201j, -0.00730 + 0.00466j,  0.0488 + 0.0641j, 
    -0.0469 + 0.0140j,   -0.0206 + 0.0834j,   -0.0120 - 0.0120j,  0.0395 - 0.0268j, 

    >>> # Vinv = V^-1 = V.H
    >>> Vinv = V.eigen_inverse(); Vinv.show(" V^-1")
    >>> CheckResult = (A - V * L.D * Vinv).norm()
    >>> print("||A - B * V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - V * diag(L) * V^-1|| (should be zero):  4.59E-33 + 0j

    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = A - B * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i        L[i]      Det(A - B * L[i])  
    0: 0.731 + 0j, -1.97E-29 + 2.21E-32j, 
    1: 0.779 + 0j,         7.30E-30 + 0j, 
    2:  1.15 + 0j,  3.23E-30 - 1.27E-31j, 
    3:  1.47 + 0j,  2.56E-28 + 1.89E-31j, 


    >>> for i in range(V.rows):
    >>>     AV = A * V.col(i); BVL = (B * L[i]) * V.col(i); X = AV - BVL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(BVL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - BVL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "BVL = B * " + Vi + " * " + Li, "   AV - BVL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  0.731 + 0j
    Checking the properties of eigenvector V0 (AV - BVL should be a zero vector): 
       Eigenvector V0       AV = A * V0  BVL = B * V0 * L[0]               AV - BVL  
    0.0609 + 0.00995j, 3.40 + 1.10E-35j,    3.40 + 2.10E-36j, -1.30E-34 + 8.90E-36j, 
    -0.0321 - 0.0508j,    -1.98 - 3.20j,       -1.98 - 3.20j,  8.00E-35 + 1.00E-34j, 
    -0.0290 - 0.0350j,    -2.20 - 2.64j,       -2.20 - 2.64j,  1.10E-34 + 1.50E-34j, 
    -0.0469 + 0.0140j,   -2.95 + 0.201j,      -2.95 + 0.201j,  1.50E-34 + 1.30E-35j, 

    Eigenvalue L[1]:  0.779 + 0j
    Checking the properties of eigenvector V1 (AV - BVL should be a zero vector): 
         Eigenvector V1     AV = A * V1  BVL = B * V1 * L[1]               AV - BVL  
    -0.0160 - 0.000497j,    -0.738 + 0j,         -0.738 + 0j,         2.40E-35 + 0j, 
      0.00344 - 0.0182j,  0.743 - 1.19j,       0.743 - 1.19j, -1.10E-35 + 2.00E-35j, 
       0.0579 - 0.0201j,  4.30 - 0.652j,       4.30 - 0.652j, -1.00E-34 + 5.00E-36j, 
      -0.0206 + 0.0834j, -0.688 + 5.59j,      -0.688 + 5.59j,  2.00E-36 - 9.00E-35j, 

    Eigenvalue L[2]:  1.15 + 0j
    Checking the properties of eigenvector V2 (AV - BVL should be a zero vector): 
         Eigenvector V2        AV = A * V2  BVL = B * V2 * L[2]               AV - BVL  
     -0.0833 + 0.00552j, -8.53 - 1.00E-36j,   -8.53 + 1.80E-36j,  1.00E-35 - 2.80E-36j, 
      -0.0405 - 0.0520j,     -4.28 - 4.16j,       -4.28 - 4.16j, -4.00E-35 - 5.00E-35j, 
    -0.00730 + 0.00466j,    -2.70 - 0.530j,      -2.70 - 0.530j,  2.00E-35 + 6.20E-35j, 
      -0.0120 - 0.0120j,     -1.90 - 1.09j,       -1.90 - 1.09j,         4.00E-35 + 0j, 

    Eigenvalue L[3]:  1.47 + 0j
    Checking the properties of eigenvector V3 (AV - BVL should be a zero vector): 
       Eigenvector V3       AV = A * V3  BVL = B * V3 * L[3]               AV - BVL  
    0.0307 - 0.00215j, 4.08 - 5.00E-36j,    4.08 + 2.00E-36j, -1.60E-34 - 7.00E-36j, 
    -0.0529 - 0.0594j,    -3.51 - 4.82j,       -3.51 - 4.82j,  1.00E-35 + 9.00E-35j, 
     0.0488 + 0.0641j,     5.89 + 5.45j,        5.89 + 5.45j, -2.40E-34 - 1.30E-34j, 
     0.0395 - 0.0268j,     4.69 - 1.74j,        4.69 - 1.74j, -1.90E-34 + 6.00E-35j, 








|newpage|


Tridiagonalization
-----------------------------

.. method:: mat.Tridiagonalization(Query)


    Returns the tridiagonal decomposition of a selfadjoint matrix.

    See also Eigen :cite:p:`EigenMat111`,  Wikipedia :cite:p:`WikipediaMat111`,  Wikipedia :cite:p:`WikipediaMat111a`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.


**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**

:Q:     Returns the unitary matrix Q in the decomposition.

:T:     Returns an expression of the tridiagonal matrix T in the decomposition..

:packed:     Returns the internal representation of the decomposition.

:hcoeff:     Returns the Householder coefficients..

:diag:     Returns the diagonal of the tridiagonal matrix T in the decomposition.

:subdiag:     Returns the subdiagonal of the tridiagonal matrix T in the decomposition.


This class performs a tridiagonal decomposition of a selfadjoint matrix `A` such that: `A = QTQ^*` where `Q` is unitary and T a real symmetric tridiagonal matrix. A tridiagonal matrix is a matrix which has nonzero elements only on the main diagonal and the first diagonal below and above it. The Hessenberg decomposition of a selfadjoint matrix is in fact a tridiagonal decomposition. This class is used in SelfAdjointEigenSolver to compute the eigenvalues and eigenvectors of a selfadjoint matrix.





Example for a real matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
    A: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> Query = "Q, T, Packed, Hcoeff, Diag, Subdiag"
    >>> Res = A.eigen_tridiag2(Query)

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
    1,      0,        0,      0,      0,      0, 
    0, -0.255,    0.648,  0.267,  0.628,  0.220, 
    0, -0.500,   -0.254,  0.734, -0.127, -0.361, 
    0, -0.479,    0.538, -0.386, -0.470, -0.332, 
    0, -0.264, -0.00888,  0.149, -0.455,  0.837, 
    0, -0.620,   -0.474, -0.468,  0.401,  0.101, 

    >>> T = Res["T"]; T.show("T")
    T: 
     44.9, -99.9,     0,     0,     0,     0, 
    -99.9,   255, -73.7,     0,     0,     0, 
        0, -73.7,  11.5,  21.7,     0,     0, 
        0,     0,  21.7,  20.2, -49.4,     0, 
        0,     0,     0, -49.4, -18.5, -24.2, 
        0,     0,     0,     0, -24.2, 0.966, 

    >>> Res["Packed"].show("Packed")
    Packed: 
     44.9,   25.5,    50.0,   47.9,  26.4,  62.0, 
    -99.9,    255,    49.1,   95.0,  29.0,  46.6, 
    0.399,  -73.7,    11.5,   84.0,  44.4,  26.7, 
    0.382, -0.192,    21.7,   20.2,  39.5,  87.5, 
    0.210, 0.0961, -0.0240,  -49.4, -18.5,  12.3, 
    0.494,  0.526,   0.680, -0.524, -24.2, 0.966, 

    >>> # Check that Q is unitary, i.e. that QQ^H = I
    >>> CheckResult = (Q.I - Q * Q.H).norm()
    >>> print("||I - Q * Q.H|| (should be zero): ", CheckResult.s())
        ||I - Q * Q.H|| (should be zero):  1.44E-35

    >>> # Check the defining property of the decomposition, i.e. A = QTQ^H
    >>> CheckResult = (A - Q * T * Q.H).norm()
    >>> print("||A - Q * T * Q^H|| (should be zero): ", CheckResult.s())
        ||A - Q * T * Q^H|| (should be zero):  3.96E-33

    >>> diag = Res["Diag"]; subdiag = Res["Subdiag"]
    >>> Query = "eval, evec"
    >>> evaltridiag = diag.eigen_SelfAdjointEigenSystemFromTridiag2(Query, subdiag)

    >>> L = evaltridiag["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues of T", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues of T: 
    i   L[i]  
    0: -61.7, 
    1: -27.7, 
    2:  4.34, 
    3:  25.8, 
    4:  62.5, 
    5:   311, 

    >>> V =  evaltridiag["Evec"]; mt = "Matrix V of eigenvectors of T (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors of T (V0, ... , V5): 
        V0      V1        V2      V3      V4        V5  
    0.0719, -0.497,   -0.271,  0.730, -0.157,    0.343, 
    0.0767, -0.361,   -0.110,  0.139, 0.0275,   -0.912, 
     0.232, -0.711, -0.00659, -0.555,  0.284,    0.226, 
    -0.521, 0.0579,   -0.370,  0.108,  0.759,   0.0173, 
    -0.760, -0.257,   -0.122, -0.257, -0.525, -0.00262, 
    -0.293, -0.216,    0.873,  0.249,  0.206, 0.000204, 

    >>> CheckResult = (T - V * L.D * V.T).norm()
    >>> print("||T - V * diag(L) * V^T|| (should be zero): ", (CheckResult).s())
        ||T - V * diag(L) * V^T|| (should be zero):  6.70E-33

    >>> XA = +A; AD = XA.diagonal(); DetA = L * 0
    >>> XT = +T; TD = XT.diagonal(); DetT = L * 0

    >>> for i in range(A.rows):
    >>>     XA.set_diagonal(0, AD - L[i]); DetA[i] = XA.eigen_det()
    >>>     XT.set_diagonal(0, TD - L[i]); DetT[i] = XT.eigen_det()

    >>> Result = L.concat_horizontal(DetA).concat_horizontal(DetT)
    >>> mt = "Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero"
    >>> ct = ["L[i]", "Det(A - I * L[i])", "Det(T - I * L[i])"]
    >>> rt = ["i"] + [x for x in range(L.rows)]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero: 
    i   L[i]  Det(A - I * L[i])  Det(T - I * L[i])  
    0: -61.7,          8.41E-24,          8.69E-24, 
    1: -27.7,         -4.36E-25,         -5.06E-25, 
    2:  4.34,          3.49E-26,          4.32E-26, 
    3:  25.8,          4.92E-25,          2.75E-25, 
    4:  62.5,         -1.13E-23,         -1.08E-23, 
    5:   311,         -6.62E-21,         -8.92E-21, 




Example for a complex matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAA6x6", "")
    >>> A = A.top_left_corner(5,5); A.show("A")
    A: 
       80.0 + 0j, 50.0 - 23.0j, 85.0 + 5.00j, 36.0 - 4.30j, 16.0 - 18.0j, 
    50.0 + 23.0j,    30.0 + 0j, 43.0 + 9.50j, 27.0 + 11.0j, 50.0 - 24.0j, 
    85.0 - 5.00j, 43.0 - 9.50j,    85.0 + 0j, 55.0 - 7.00j, 34.0 + 8.50j, 
    36.0 + 4.30j, 27.0 - 11.0j, 55.0 + 7.00j,    23.0 + 0j, 49.0 + 40.0j, 
    16.0 + 18.0j, 50.0 + 24.0j, 34.0 - 8.50j, 49.0 - 40.0j,    85.0 + 0j, 

    >>> Query = "Q, T, Packed, Hcoeff, Diag, Subdiag"
    >>> Res = A.eigen_tridiag2(Query)

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
    1.00 + 0j,           0 + 0j,           0 + 0j,            0 + 0j,           0 + 0j, 
       0 + 0j,  -0.453 - 0.208j, -0.0465 - 0.186j,    0.480 - 0.389j,   0.144 + 0.558j, 
       0 + 0j, -0.770 + 0.0453j,  -0.158 + 0.243j, 0.00105 + 0.0880j,  -0.417 - 0.372j, 
       0 + 0j, -0.326 - 0.0390j,   0.258 + 0.207j,   -0.228 + 0.640j,   0.456 + 0.336j, 
       0 + 0j,  -0.145 - 0.163j,   0.864 - 0.153j,   -0.224 - 0.314j, -0.0891 - 0.162j, 

    >>> T = Res["T"]; T.show("T")
    T: 
    80.0 + 0j,  -110 + 0j,     0 + 0j,     0 + 0j,     0 + 0j, 
    -110 + 0j,   153 + 0j, -59.2 + 0j,     0 + 0j,     0 + 0j, 
       0 + 0j, -59.2 + 0j,   104 + 0j,  24.4 + 0j,     0 + 0j, 
       0 + 0j,     0 + 0j,  24.4 + 0j, -30.1 + 0j, -19.0 + 0j, 
       0 + 0j,     0 + 0j,     0 + 0j, -19.0 + 0j, -4.47 + 0j, 

    >>> Res["Packed"].show("Packed")
    Packed: 
           80.0 + 0j,    50.0 - 23.0j,   85.0 + 5.00j, 36.0 - 4.30j, 16.0 - 18.0j, 
           -110 + 0j,        153 + 0j,   43.0 + 9.50j, 27.0 + 11.0j, 50.0 - 24.0j, 
      0.515 - 0.105j,      -59.2 + 0j,       104 + 0j, 55.0 - 7.00j, 34.0 + 8.50j, 
    0.224 - 0.00528j, -0.161 - 0.271j,      24.4 + 0j,   -30.1 + 0j, 49.0 + 40.0j, 
     0.114 + 0.0960j, -0.732 - 0.105j, 0.251 + 0.187j,   -19.0 + 0j,   -4.47 + 0j, 

    >>> # Check that Q is unitary, i.e. that QQ^H = I
    >>> CheckResult = (Q.I - Q * Q.H).norm()
    >>> print("||I - Q * Q.H|| (should be zero): ", CheckResult.s())
        ||I - Q * Q.H|| (should be zero):  1.46E-35 + 0j

    >>> # Check the defining property of the decomposition, i.e. A = QTQ^H
    >>> CheckResult = (A - Q * T * Q.H).norm()
    >>> print("||A - Q * T * Q^H|| (should be zero): ", CheckResult.s())
        ||A - Q * T * Q^H|| (should be zero):  2.51E-33 + 0j

    >>> diag = Res["Diag"]; subdiag = Res["Subdiag"]; T = Res["T"]
    >>> Query = "eval, evec"
    >>> evaltridiag = diag.eigen_SelfAdjointEigenSystemFromTridiag2(Query, subdiag)

    >>> L = evaltridiag["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues of T", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues of T: 
    i        L[i]  
    0: -44.4 + 0j, 
    1: -10.3 + 0j, 
    2:  5.28 + 0j, 
    3:   103 + 0j, 
    4:   250 + 0j, 

    >>> V =  evaltridiag["Evec"]; mt = "Matrix V of eigenvectors of T (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors of T (V0, ... , V4): 
              V0            V1            V2            V3             V4  
    -0.0991 + 0j,  -0.708 + 0j,   0.190 + 0j,  -0.432 + 0j,    0.515 + 0j, 
     -0.112 + 0j,  -0.580 + 0j,   0.129 + 0j,  0.0896 + 0j,   -0.792 + 0j, 
     -0.189 + 0j,  -0.282 + 0j, -0.0325 + 0j,   0.881 + 0j,    0.327 + 0j, 
      0.876 + 0j, -0.0839 + 0j,   0.443 + 0j,   0.166 + 0j,   0.0288 + 0j, 
      0.418 + 0j,  -0.274 + 0j,  -0.866 + 0j, -0.0295 + 0j, -0.00216 + 0j, 

    >>> CheckResult = (T - V * L.D * V.T).norm()
    >>> print("||T - V * diag(L) * V^T|| (should be zero): ", (CheckResult).s())
        ||T - V * diag(L) * V^T|| (should be zero):  9.71E-33 + 0j

    >>> XA = +A; AD = XA.diagonal(); DetA = L * 0
    >>> XT = +T; TD = XT.diagonal(); DetT = L * 0

    >>> for i in range(A.rows):
    >>>     XA.set_diagonal(0, AD - L[i]); DetA[i] = XA.eigen_det()
    >>>     XT.set_diagonal(0, TD - L[i]); DetT[i] = XT.eigen_det()

    >>> Result = L.concat_horizontal(DetA).concat_horizontal(DetT)
    >>> mt = "Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero"
    >>> ct = ["L[i]", "Det(A - I * L[i])", "Det(T - I * L[i])"]
    >>> rt = ["i"] + [x for x in range(L.rows)]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero: 
    i        L[i]      Det(A - I * L[i])  Det(T - I * L[i])  
    0: -44.4 + 0j, -5.09E-26 - 2.12E-27j,    -2.15E-26 + 0j, 
    1: -10.3 + 0j,  5.47E-27 + 2.47E-28j,     8.81E-28 + 0j, 
    2:  5.28 + 0j, -6.37E-29 + 1.87E-27j,     9.68E-28 + 0j, 
    3:   103 + 0j, -5.10E-25 - 1.96E-26j,    -4.86E-25 + 0j, 
    4:   250 + 0j,  1.12E-23 + 3.03E-26j,     1.19E-23 + 0j, 






|newpage|


Square root of a selfadjoint matrix
-----------------------------------------

.. method:: mat.MatrixSquareRootSA(Query)


    Returns the tridiagonal decomposition of a selfadjoint matrix.

    See also Eigen :cite:p:`EigenMat111`,  Wikipedia :cite:p:`WikipediaMat111`,  Wikipedia :cite:p:`WikipediaMat111a`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.


**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**

:Q:     Returns the unitary matrix Q in the decomposition.

:T:     Returns an expression of the tridiagonal matrix T in the decomposition..

:packed:     Returns the internal representation of the decomposition.

:hcoeff:     Returns the Householder coefficients..

:diag:     Returns the diagonal of the tridiagonal matrix T in the decomposition.

:subdiag:     Returns the subdiagonal of the tridiagonal matrix T in the decomposition.


This class performs a tridiagonal decomposition of a selfadjoint matrix `A` such that: `A = QTQ^*` where `Q` is unitary and T a real symmetric tridiagonal matrix. A tridiagonal matrix is a matrix which has nonzero elements only on the main diagonal and the first diagonal below and above it. The Hessenberg decomposition of a selfadjoint matrix is in fact a tridiagonal decomposition. This class is used in SelfAdjointEigenSolver to compute the eigenvalues and eigenvectors of a selfadjoint matrix.





Example for a real matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
    A: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> Query = "Q, T, Packed, Hcoeff, Diag, Subdiag"
    >>> Res = A.eigen_tridiag2(Query)

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
    1,      0,        0,      0,      0,      0, 
    0, -0.255,    0.648,  0.267,  0.628,  0.220, 
    0, -0.500,   -0.254,  0.734, -0.127, -0.361, 
    0, -0.479,    0.538, -0.386, -0.470, -0.332, 
    0, -0.264, -0.00888,  0.149, -0.455,  0.837, 
    0, -0.620,   -0.474, -0.468,  0.401,  0.101, 

    >>> T = Res["T"]; T.show("T")
    T: 
     44.9, -99.9,     0,     0,     0,     0, 
    -99.9,   255, -73.7,     0,     0,     0, 
        0, -73.7,  11.5,  21.7,     0,     0, 
        0,     0,  21.7,  20.2, -49.4,     0, 
        0,     0,     0, -49.4, -18.5, -24.2, 
        0,     0,     0,     0, -24.2, 0.966, 

    >>> Res["Packed"].show("Packed")
    Packed: 
     44.9,   25.5,    50.0,   47.9,  26.4,  62.0, 
    -99.9,    255,    49.1,   95.0,  29.0,  46.6, 
    0.399,  -73.7,    11.5,   84.0,  44.4,  26.7, 
    0.382, -0.192,    21.7,   20.2,  39.5,  87.5, 
    0.210, 0.0961, -0.0240,  -49.4, -18.5,  12.3, 
    0.494,  0.526,   0.680, -0.524, -24.2, 0.966, 

    >>> # Check that Q is unitary, i.e. that QQ^H = I
    >>> CheckResult = (Q.I - Q * Q.H).norm()
    >>> print("||I - Q * Q.H|| (should be zero): ", CheckResult.s())
        ||I - Q * Q.H|| (should be zero):  1.44E-35

    >>> # Check the defining property of the decomposition, i.e. A = QTQ^H
    >>> CheckResult = (A - Q * T * Q.H).norm()
    >>> print("||A - Q * T * Q^H|| (should be zero): ", CheckResult.s())
        ||A - Q * T * Q^H|| (should be zero):  3.96E-33

    >>> diag = Res["Diag"]; subdiag = Res["Subdiag"]
    >>> Query = "eval, evec"
    >>> evaltridiag = diag.eigen_SelfAdjointEigenSystemFromTridiag2(Query, subdiag)

    >>> L = evaltridiag["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues of T", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues of T: 
    i   L[i]  
    0: -61.7, 
    1: -27.7, 
    2:  4.34, 
    3:  25.8, 
    4:  62.5, 
    5:   311, 

    >>> V =  evaltridiag["Evec"]; mt = "Matrix V of eigenvectors of T (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors of T (V0, ... , V5): 
        V0      V1        V2      V3      V4        V5  
    0.0719, -0.497,   -0.271,  0.730, -0.157,    0.343, 
    0.0767, -0.361,   -0.110,  0.139, 0.0275,   -0.912, 
     0.232, -0.711, -0.00659, -0.555,  0.284,    0.226, 
    -0.521, 0.0579,   -0.370,  0.108,  0.759,   0.0173, 
    -0.760, -0.257,   -0.122, -0.257, -0.525, -0.00262, 
    -0.293, -0.216,    0.873,  0.249,  0.206, 0.000204, 

    >>> CheckResult = (T - V * L.D * V.T).norm()
    >>> print("||T - V * diag(L) * V^T|| (should be zero): ", (CheckResult).s())
        ||T - V * diag(L) * V^T|| (should be zero):  6.70E-33

    >>> XA = +A; AD = XA.diagonal(); DetA = L * 0
    >>> XT = +T; TD = XT.diagonal(); DetT = L * 0

    >>> for i in range(A.rows):
    >>>     XA.set_diagonal(0, AD - L[i]); DetA[i] = XA.eigen_det()
    >>>     XT.set_diagonal(0, TD - L[i]); DetT[i] = XT.eigen_det()

    >>> Result = L.concat_horizontal(DetA).concat_horizontal(DetT)
    >>> mt = "Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero"
    >>> ct = ["L[i]", "Det(A - I * L[i])", "Det(T - I * L[i])"]
    >>> rt = ["i"] + [x for x in range(L.rows)]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero: 
    i   L[i]  Det(A - I * L[i])  Det(T - I * L[i])  
    0: -61.7,          8.41E-24,          8.69E-24, 
    1: -27.7,         -4.36E-25,         -5.06E-25, 
    2:  4.34,          3.49E-26,          4.32E-26, 
    3:  25.8,          4.92E-25,          2.75E-25, 
    4:  62.5,         -1.13E-23,         -1.08E-23, 
    5:   311,         -6.62E-21,         -8.92E-21, 




Example for a complex matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableRandomSAA6x6", "")
    >>> A = A.top_left_corner(5,5); A.show("A")
    A: 
       80.0 + 0j, 50.0 - 23.0j, 85.0 + 5.00j, 36.0 - 4.30j, 16.0 - 18.0j, 
    50.0 + 23.0j,    30.0 + 0j, 43.0 + 9.50j, 27.0 + 11.0j, 50.0 - 24.0j, 
    85.0 - 5.00j, 43.0 - 9.50j,    85.0 + 0j, 55.0 - 7.00j, 34.0 + 8.50j, 
    36.0 + 4.30j, 27.0 - 11.0j, 55.0 + 7.00j,    23.0 + 0j, 49.0 + 40.0j, 
    16.0 + 18.0j, 50.0 + 24.0j, 34.0 - 8.50j, 49.0 - 40.0j,    85.0 + 0j, 

    >>> Query = "Q, T, Packed, Hcoeff, Diag, Subdiag"
    >>> Res = A.eigen_tridiag2(Query)

    >>> Q = Res["Q"]; Q.show("Q")
    Q: 
    1.00 + 0j,           0 + 0j,           0 + 0j,            0 + 0j,           0 + 0j, 
       0 + 0j,  -0.453 - 0.208j, -0.0465 - 0.186j,    0.480 - 0.389j,   0.144 + 0.558j, 
       0 + 0j, -0.770 + 0.0453j,  -0.158 + 0.243j, 0.00105 + 0.0880j,  -0.417 - 0.372j, 
       0 + 0j, -0.326 - 0.0390j,   0.258 + 0.207j,   -0.228 + 0.640j,   0.456 + 0.336j, 
       0 + 0j,  -0.145 - 0.163j,   0.864 - 0.153j,   -0.224 - 0.314j, -0.0891 - 0.162j, 

    >>> T = Res["T"]; T.show("T")
    T: 
    80.0 + 0j,  -110 + 0j,     0 + 0j,     0 + 0j,     0 + 0j, 
    -110 + 0j,   153 + 0j, -59.2 + 0j,     0 + 0j,     0 + 0j, 
       0 + 0j, -59.2 + 0j,   104 + 0j,  24.4 + 0j,     0 + 0j, 
       0 + 0j,     0 + 0j,  24.4 + 0j, -30.1 + 0j, -19.0 + 0j, 
       0 + 0j,     0 + 0j,     0 + 0j, -19.0 + 0j, -4.47 + 0j, 

    >>> Res["Packed"].show("Packed")
    Packed: 
           80.0 + 0j,    50.0 - 23.0j,   85.0 + 5.00j, 36.0 - 4.30j, 16.0 - 18.0j, 
           -110 + 0j,        153 + 0j,   43.0 + 9.50j, 27.0 + 11.0j, 50.0 - 24.0j, 
      0.515 - 0.105j,      -59.2 + 0j,       104 + 0j, 55.0 - 7.00j, 34.0 + 8.50j, 
    0.224 - 0.00528j, -0.161 - 0.271j,      24.4 + 0j,   -30.1 + 0j, 49.0 + 40.0j, 
     0.114 + 0.0960j, -0.732 - 0.105j, 0.251 + 0.187j,   -19.0 + 0j,   -4.47 + 0j, 

    >>> # Check that Q is unitary, i.e. that QQ^H = I
    >>> CheckResult = (Q.I - Q * Q.H).norm()
    >>> print("||I - Q * Q.H|| (should be zero): ", CheckResult.s())
        ||I - Q * Q.H|| (should be zero):  1.46E-35 + 0j

    >>> # Check the defining property of the decomposition, i.e. A = QTQ^H
    >>> CheckResult = (A - Q * T * Q.H).norm()
    >>> print("||A - Q * T * Q^H|| (should be zero): ", CheckResult.s())
        ||A - Q * T * Q^H|| (should be zero):  2.51E-33 + 0j

    >>> diag = Res["Diag"]; subdiag = Res["Subdiag"]; T = Res["T"]
    >>> Query = "eval, evec"
    >>> evaltridiag = diag.eigen_SelfAdjointEigenSystemFromTridiag2(Query, subdiag)

    >>> L = evaltridiag["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues of T", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues of T: 
    i        L[i]  
    0: -44.4 + 0j, 
    1: -10.3 + 0j, 
    2:  5.28 + 0j, 
    3:   103 + 0j, 
    4:   250 + 0j, 

    >>> V =  evaltridiag["Evec"]; mt = "Matrix V of eigenvectors of T (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors of T (V0, ... , V4): 
              V0            V1            V2            V3             V4  
    -0.0991 + 0j,  -0.708 + 0j,   0.190 + 0j,  -0.432 + 0j,    0.515 + 0j, 
     -0.112 + 0j,  -0.580 + 0j,   0.129 + 0j,  0.0896 + 0j,   -0.792 + 0j, 
     -0.189 + 0j,  -0.282 + 0j, -0.0325 + 0j,   0.881 + 0j,    0.327 + 0j, 
      0.876 + 0j, -0.0839 + 0j,   0.443 + 0j,   0.166 + 0j,   0.0288 + 0j, 
      0.418 + 0j,  -0.274 + 0j,  -0.866 + 0j, -0.0295 + 0j, -0.00216 + 0j, 

    >>> CheckResult = (T - V * L.D * V.T).norm()
    >>> print("||T - V * diag(L) * V^T|| (should be zero): ", (CheckResult).s())
        ||T - V * diag(L) * V^T|| (should be zero):  9.71E-33 + 0j

    >>> XA = +A; AD = XA.diagonal(); DetA = L * 0
    >>> XT = +T; TD = XT.diagonal(); DetT = L * 0

    >>> for i in range(A.rows):
    >>>     XA.set_diagonal(0, AD - L[i]); DetA[i] = XA.eigen_det()
    >>>     XT.set_diagonal(0, TD - L[i]); DetT[i] = XT.eigen_det()

    >>> Result = L.concat_horizontal(DetA).concat_horizontal(DetT)
    >>> mt = "Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero"
    >>> ct = ["L[i]", "Det(A - I * L[i])", "Det(T - I * L[i])"]
    >>> rt = ["i"] + [x for x in range(L.rows)]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues: Det(A - I * L[i]) and Det(T - I * L[i]) should be zero: 
    i        L[i]      Det(A - I * L[i])  Det(T - I * L[i])  
    0: -44.4 + 0j, -5.09E-26 - 2.12E-27j,    -2.15E-26 + 0j, 
    1: -10.3 + 0j,  5.47E-27 + 2.47E-28j,     8.81E-28 + 0j, 
    2:  5.28 + 0j, -6.37E-29 + 1.87E-27j,     9.68E-28 + 0j, 
    3:   103 + 0j, -5.10E-25 - 1.96E-26j,    -4.86E-25 + 0j, 
    4:   250 + 0j,  1.12E-23 + 3.03E-26j,     1.19E-23 + 0j, 







