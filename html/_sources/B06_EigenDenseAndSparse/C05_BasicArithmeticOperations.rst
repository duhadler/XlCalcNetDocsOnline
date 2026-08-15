
.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}


.. |spacingend| raw:: latex

   \end{spacing}


.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />



Basic arithmetic operations
===============================================================================



Matrix deep copy (unary plus)
-------------------------------------------------------------------------------

Returns the matrix multiplied with +1. This results in a deep copy of the matrix.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = A
    >>> C = +A
    >>> A[1,1] = 99
    >>> B.show("B")
    B: 
    11, 12, 13, 14, 15, 16, 
    21, 99, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> C.show("C")
    C: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 






Matrix negation (unary minus)
-------------------------------------------------------------------------------

Returns the matrix multiplied with -1.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = -A
    >>> B.show("B")
    B: 
    -11, -12, -13, -14, -15, -16, 
    -21, -99, -23, -24, -25, -26, 
    -31, -32, -33, -34, -35, -36, 
    -41, -42, -43, -44, -45, -46, 
    -51, -52, -53, -54, -55, -56, 
    -61, -62, -63, -64, -65, -66, 






General matrix addition
-------------------------------------------------------------------------------

Returns the sum of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have the same dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 
    >>> C = A + B; C.show("C")
    C: 
     922,  924,  926,  928,  930,  932, 
     942,  944,  946,  948,  950,  952, 
     962,  964,  966,  968,  970,  972, 
     982,  984,  986,  988,  990,  992, 
    1002, 1004, 1006, 1008, 1010, 1012, 
    1022, 1024, 1026, 1028, 1030, 1032, 





Matrix addition of a vector as diagonal matrix 
-------------------------------------------------------------------------------


Returns the matrix product of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have compatible dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> # read the first column from the matrix
    >>> d = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", "").col(0); d.show("d")
    d: 
    911, 
    921, 
    931, 
    941, 
    951, 
    961, 

    >>> # creates a square matrix with the coefficents of d1 on the diagonal.
    >>> D = d.as_diagonal(); D.show("D")
    D: 
    911,   0,   0,   0,   0,   0, 
      0, 921,   0,   0,   0,   0, 
      0,   0, 931,   0,   0,   0, 
      0,   0,   0, 941,   0,   0, 
      0,   0,   0,   0, 951,   0, 
      0,   0,   0,   0,   0, 961, 

    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> C = A + D; C.show("C")    # same as D + A()
    C: 
     922,   12,   13,   14,   15,   16, 
      21,  943,   23,   24,   25,   26, 
      31,   32,  964,   34,   35,   36, 
      41,   42,   43,  985,   45,   46, 
      51,   52,   53,   54, 1006,   56, 
      61,   62,   63,   64,   65, 1027, 

    >>> C = A + d.diagonal_view(); C.show("C")    # same as d.diagonal_view + A()
    C: 
     922,   12,   13,   14,   15,   16, 
      21,  943,   23,   24,   25,   26, 
      31,   32,  964,   34,   35,   36, 
      41,   42,   43,  985,   45,   46, 
      51,   52,   53,   54, 1006,   56, 
      61,   62,   63,   64,   65, 1027, 



Matrix: addition of a scalar
-------------------------------------------------------------------------------

Returns the sum of matrix ?matA and scalar `b`, applied to each coefficient of ?matA. The coefficients of ?matA and `b` need to be of the same type. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices and real and complex scalars.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = A + 15;  B.show("B")
    B: 
    26, 27, 28, 29, 30, 31, 
    36, 37, 38, 39, 40, 41, 
    46, 47, 48, 49, 50, 51, 
    56, 57, 58, 59, 60, 61, 
    66, 67, 68, 69, 70, 71, 
    76, 77, 78, 79, 80, 81, 




General matrix subtraction
-------------------------------------------------------------------------------


Returns the difference of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have the same dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 
    >>> C = A - B; C.show("C")
    C: 
    -900, -900, -900, -900, -900, -900, 
    -900, -900, -900, -900, -900, -900, 
    -900, -900, -900, -900, -900, -900, 
    -900, -900, -900, -900, -900, -900, 
    -900, -900, -900, -900, -900, -900, 
    -900, -900, -900, -900, -900, -900, 





Matrix: subtraction of a scalar
-------------------------------------------------------------------------------


Returns the difference of matrix ?matA and scalar `b`, applied to each coefficient of ?matA. The coefficients of ?matA and `b` need to be of the same type. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices and real and complex scalars.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = A - 15;  B.show("B")
    B: 
    -4, -3, -2, -1,  0,  1, 
     6,  7,  8,  9, 10, 11, 
    16, 17, 18, 19, 20, 21, 
    26, 27, 28, 29, 30, 31, 
    36, 37, 38, 39, 40, 41, 
    46, 47, 48, 49, 50, 51, 





General matrix multiplication ("gemm")
-------------------------------------------------------------------------------

See also Eigen :cite:p:`EigenMat100`.


In its general form, matrix multiplication takes the form `\boldsymbol{C} = \boldsymbol{A} \boldsymbol{B}`, where `\boldsymbol{A}` is a `m`-by-`k` matrix, `\boldsymbol{B}` is a `k`-by-`n` matrix, and `\boldsymbol{C}` is a `m`-by-`n` matrix. Also, the transposed or adjoined matrices of  `\boldsymbol{A}` and/or `\boldsymbol{B}` are often directly used.

In the general form, no information regarding special properties of `\boldsymbol{A}` and/or `\boldsymbol{B}` is used. If such information is available, specialized forms of multiplication are often signifantly faster:

* if `\boldsymbol{A}` or `\boldsymbol{B}` is a triangular or diagonal matrix, or 
* if the multiplication with the inverse of a square, triangular or diagonal matrix is desired, or
* if `\boldsymbol{B}` is the transpose of `\boldsymbol{A}`.


In the canonical FORTRAN package BLAS, the BLAS Level 3 function `\mathrm{?gemm}` and the BLAS Level 2 function `\mathrm{?gemv}` handle this kind of expression, with the scalars `\alpha` `\beta` and the indicator variables `\textsf{TransA}` and `\textsf{TransB}` as additional parameters:


.. math:: 
    \mathrm{?gemm}=\begin{cases}
        \alpha \boldsymbol{A} \boldsymbol{B} + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'N', TransB = 'N'},\\
        \alpha \boldsymbol{A} \boldsymbol{B}^T + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'N', TransB = 'T'},\\        
        \alpha \boldsymbol{A} \boldsymbol{B}^H + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'N', TransB = 'C'},\\
        \alpha \boldsymbol{A}^T \boldsymbol{B} + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'T', TransB = 'N'},\\
        \alpha \boldsymbol{A}^T \boldsymbol{B}^T + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'T', TransB = 'T'},\\
        \alpha \boldsymbol{A}^T \boldsymbol{B}^H + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'T', TransB = 'C'},\\
        \alpha \boldsymbol{A}^H \boldsymbol{B} + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'C', TransB = 'N'},\\
        \alpha \boldsymbol{A}^H \boldsymbol{B}^T + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'C', TransB = 'T'},\\
        \alpha \boldsymbol{A}^H \boldsymbol{B}^H + \beta \boldsymbol{C}, & \text{for } \textsf{TransA = 'C', TransB = 'C'},\\
    \end{cases}


.. math:: 
    \mathrm{?gemv}=\begin{cases}
        \alpha \boldsymbol{A} \boldsymbol{x} + \beta \boldsymbol{y}, & \text{for } \textsf{TransA = 'N'},\\
        \alpha \boldsymbol{A}^T \boldsymbol{x} + \beta \boldsymbol{y}, & \text{for } \textsf{TransA = 'T'},\\
        \alpha \boldsymbol{A}^H \boldsymbol{x} + \beta \boldsymbol{y}, & \text{for } \textsf{TransA = 'C'}.
    \end{cases}


We use the ``transpose()`` and ``adjoint()`` properties to compute these expressions efficiently.
Here are some examples with real matrices:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 
    >>> C = A * B; C.show("C")
    C: 
     75991,  76072,  76153,  76234,  76315,  76396, 
    132151, 132292, 132433, 132574, 132715, 132856, 
    188311, 188512, 188713, 188914, 189115, 189316, 
    244471, 244732, 244993, 245254, 245515, 245776, 
    300631, 300952, 301273, 301594, 301915, 302236, 
    356791, 357172, 357553, 357934, 358315, 358696, 

    >>> C = A.transpose() * B;  C.show("C")
    C: 
    203926, 204142, 204358, 204574, 204790, 205006, 
    209542, 209764, 209986, 210208, 210430, 210652, 
    215158, 215386, 215614, 215842, 216070, 216298, 
    220774, 221008, 221242, 221476, 221710, 221944, 
    226390, 226630, 226870, 227110, 227350, 227590, 
    232006, 232252, 232498, 232744, 232990, 233236, 

    >>> C = A * B.transpose();  C.show("C")
    C: 
     74011,  74821,  75631,  76441,  77251,  78061, 
    128821, 130231, 131641, 133051, 134461, 135871, 
    183631, 185641, 187651, 189661, 191671, 193681, 
    238441, 241051, 243661, 246271, 248881, 251491, 
    293251, 296461, 299671, 302881, 306091, 309301, 
    348061, 351871, 355681, 359491, 363301, 367111, 



Here are some examples with complex matrices:

.. code-block:: pycon


    >>> TName = "DecCplxTableA6x6"; Query = "where row<4 and col<4"
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), TName, Query); A.show("A")
    A: 
    11 + 31j, 12 + 32j, 13 + 33j, 14 + 34j, 
    21 + 41j, 22 + 42j, 23 + 43j, 24 + 44j, 
    31 + 51j, 32 + 52j, 33 + 53j, 34 + 54j, 
    41 + 61j, 42 + 62j, 43 + 63j, 44 + 64j, 


    >>> TName = "DecCplxTableB6x6"; Query = "where row<4 and col<4"
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), TName, Query); B.show("B")
    B: 
    45 + 7.5j, 2.9 + 36j,  11 + 13j,  37 + 37j, 
     13 + 29j,  38 + 41j,  22 + 44j,  28 + 20j, 
    32 + 9.0j,  42 + 49j,  47 + 11j,  32 + 49j, 
     34 + 42j, 6.0 + 16j,  20 + 38j,  22 + 17j, 

    >>> C = A.adjoint() * B;  C.show("C")
    C: 
    7596.5 - 2941.5j,  8649.9 - 723.9j,     7946 - 1894j,     8392 - 2226j, 
    7808.0 - 2978.0j,  8880.8 - 670.8j,     8152 - 1888j,     8634 - 2222j, 
    8019.5 - 3014.5j,  9111.7 - 617.7j,     8358 - 1882j,     8876 - 2218j, 
    8231.0 - 3051.0j,  9342.6 - 564.6j,     8564 - 1876j,     9118 - 2214j, 

    >>> C = B.adjoint() * A;  C.show("C")
    C: 
    7596.5 + 2941.5j, 7808.0 + 2978.0j, 8019.5 + 3014.5j, 8231.0 + 3051.0j, 
     8649.9 + 723.9j,  8880.8 + 670.8j,  9111.7 + 617.7j,  9342.6 + 564.6j, 
        7946 + 1894j,     8152 + 1888j,     8358 + 1882j,     8564 + 1876j, 
        8392 + 2226j,     8634 + 2222j,     8876 + 2218j,     9118 + 2214j, 


    >>> C = A * B.adjoint();  C.show("C")
    C: 
     4262.3 + 1907.3j,      5620 + 1634j,  5791.0 + 3459.0j,  4660.0 + 1268.0j, 
     6156.3 + 1931.3j,      7970 + 1304j,  8501.0 + 3809.0j,   6610.0 + 958.0j, 
     8050.3 + 1955.3j,      10320 + 974j, 11211.0 + 4159.0j,   8560.0 + 648.0j, 
     9944.3 + 1979.3j,      12670 + 644j, 13921.0 + 4509.0j,  10510.0 + 338.0j, 

    >>> C = B * A.adjoint();  C.show("C")
    C: 
     4262.3 - 1907.3j,  6156.3 - 1931.3j,  8050.3 - 1955.3j,  9944.3 - 1979.3j, 
         5620 - 1634j,      7970 - 1304j,      10320 - 974j,      12670 - 644j, 
     5791.0 - 3459.0j,  8501.0 - 3809.0j, 11211.0 - 4159.0j, 13921.0 - 4509.0j, 
     4660.0 - 1268.0j,   6610.0 - 958.0j,   8560.0 - 648.0j,  10510.0 - 338.0j, 










Rank-k update  ("syrk", "herk")
------------------------------------------------------------------------------------------

.. method:: mat.RankKUpdate()

    Returns the products matrix of the matrix

    See also Eigen :cite:p:`EigenMat100`.


    If we calculate `C = A^T A`, with `A` being a general real or complex `n`-by-`m` matrix, then `C` is a self-adjoint (i.e. symmetric real or complex hermitian) `m`-by-`m` matrix. Therefore, only the lower triangular or uppper triangular submatrix of `C` need to be computed explicitly, which reduces the number of coefficients of `C`, which need to computed explicitly from `m^2` to `m(m+1)/2`.

    The result of this computation is known in statistics as the matrix of sums of squares and cross-products of the data, or more tersely as the cross-products matrix. Note that this is a different etymology than that for the cross-product of two vectors in linear algebra. In BLAS, this computation is implemented (in slightly different form) by the functions `\textsf{syrk}`, `\textsf{syr}`, `\textsf{herk}` and `\textsf{her}` (see below).

    If the columns of `\boldsymbol{A}` are centered (i.e. their means are zero), then this function computes the covariance matrix, times a constant factor `m-1`. 
    If the columns of `\boldsymbol{A}` are standardized (i.e. their means are zero and their variances are 1), then this function computes the correlation matrix, times a constant factor `\sqrt{m-1}`. 



    For real scalars `\alpha` and `\beta`, parameter `\textsf{Trans}`, real symmetric matrix `\boldsymbol{C}`, and real general matrix `\boldsymbol{A}`, the function is equivalent to the BLAS Level 3 function  `\textsf{syrk}` which computes a so-called rank-k update of the real matrix `\boldsymbol{C}`, defined as 

    .. math:: 
        \textsf{syrk}=\begin{cases}
            \alpha \boldsymbol{A} \boldsymbol{A}^T + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'N'} \\
            \alpha \boldsymbol{A}^T \boldsymbol{A} + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'T'} \\
        \end{cases}


    For real scalar `\alpha`, real vector `\boldsymbol{x}` (instead of `\boldsymbol{A}`), and real symmetric matrix `\boldsymbol{C}`, the function is equivalent to the BLAS Level 2 function  `\textsf{syr}`, which computes the symmetric rank-1 update of the matrix `\boldsymbol{C}`, defined as

    .. math:: \textsf{syr}= \alpha \boldsymbol{x}  \boldsymbol{x}^T +\boldsymbol{C} .




    For complex scalars `\alpha` and `\beta`, complex symmetric matrix `\boldsymbol{C}`, and complex general matrix `\boldsymbol{A}`, the function is equivalent to the BLAS Level 3 function  `\textsf{herk}` and computes a rank-k update of the complex matrix `\boldsymbol{C}`, defined as 

    .. math:: 
        \textsf{herk}=\begin{cases}
            \alpha \boldsymbol{A} \boldsymbol{A}^H + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'N'} \\
            \alpha \boldsymbol{A}^H \boldsymbol{A} + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'C'} \\
        \end{cases}


    For complex scalar `\alpha`, the complex vector `\boldsymbol{x}` (instead of `\boldsymbol{A}`), and complex hermitian matrix `\boldsymbol{A}`, the function is equivalent to the BLAS Level 2 function  `\textsf{her}` and computes the hermitian rank-1 update of the matrix `\boldsymbol{A}`, defined as

    .. math:: \textsf{her}= \alpha \boldsymbol{x}  \boldsymbol{x}^H +\boldsymbol{A} .




    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf(); mp14.setdps(15)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> Res = A.T * A; Res.show("Res")
        Res: 
         9526,  9742,  9958, 10174, 10390, 10606, 
         9742,  9964, 10186, 10408, 10630, 10852, 
         9958, 10186, 10414, 10642, 10870, 11098, 
        10174, 10408, 10642, 10876, 11110, 11344, 
        10390, 10630, 10870, 11110, 11350, 11590, 
        10606, 10852, 11098, 11344, 11590, 11836, 


        >>> C = A.rank_k_update(); C.show("C")
        Res: 
         9526,  9742,  9958, 10174, 10390, 10606, 
         9742,  9964, 10186, 10408, 10630, 10852, 
         9958, 10186, 10414, 10642, 10870, 11098, 
        10174, 10408, 10642, 10876, 11110, 11344, 
        10390, 10630, 10870, 11110, 11350, 11590, 
        10606, 10852, 11098, 11344, 11590, 11836, 








Rank-2k update  ("syr2k", "her2k")
------------------------------------------------------------------------------------------


.. method:: mat.Rank2KUpdate()


    Returns the products matrix of the matrix

    If we calculate `C = A B^T + B A^T`, with `A` and `B` being general real or complex `n`-by-`m` matrices, then `C` is a self-adjoint (i.e. symmetric real or complex hermitian) `m`-by-`m` matrix. Therefore, only the lower triangular or uppper triangular submatrix of `C` need to be computed explicitly, which reduces the number of coefficients of `C`, which need to computed explicitly from `m^2` to `m(m+1)/2`.


    For the real scalars `\alpha` and `\beta`, the real symmetric matrix `\boldsymbol{C}`, and the real general matrices `\boldsymbol{A}` and `\boldsymbol{B}`, the function is equivalent to the BLAS Level 3 function  `\textsf{syr2k}` and computes a rank-2k update of the real matrix `\boldsymbol{C}`, defined as 

    .. math:: 
        \textsf{syr2k}=\begin{cases}
            \alpha (\boldsymbol{A} \boldsymbol{B}^T+ \boldsymbol{B} \boldsymbol{A}^T ) + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'N'} \\
            \alpha (\boldsymbol{A}^T \boldsymbol{B} + \boldsymbol{B}^T \boldsymbol{A} ) + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'T'} \\
        \end{cases}


    For the real scalar `\alpha`, the real vectors `\boldsymbol{x}` and `\boldsymbol{y}`, and the real symmetric matrix `\boldsymbol{A}`, the function is equivalent to the BLAS Level 2 function  `\textsf{syr2}` and computes the symmetric rank-2 update of the matrix `\boldsymbol{A}`, defined as

    .. math:: 
        \textsf{syr2}= \alpha \boldsymbol{x} \boldsymbol{y}^T +  \alpha \boldsymbol{y} \boldsymbol{x}^T +\boldsymbol{A}.



    For the complex scalars `\alpha` and `\beta`, the complex hermitian matrix `\boldsymbol{C}`, and the complex general matrices `\boldsymbol{A}` and `\boldsymbol{B}`, the function is equivalent to the BLAS Level 3 function  `\textsf{her2k}` and computes a rank-2k update of the hermitian matrix `\boldsymbol{C}`, defined as 

    .. math:: 
        \textsf{her2k}=\begin{cases}
            \alpha (\boldsymbol{A} \boldsymbol{B}^H+ \boldsymbol{B} \boldsymbol{A}^H) + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'N'} \\
            \alpha (\boldsymbol{A}^H \boldsymbol{B} + \boldsymbol{B}^H \boldsymbol{A}) + \beta \boldsymbol{C}, & \text{for } \textsf{Trans = 'C'} \\
        \end{cases}


    For the complex scalar `\alpha`, the complex vectors `\boldsymbol{x}` and `\boldsymbol{y}`, and the complex hermitian matrix `\boldsymbol{A}`, the function is equivalent to the BLAS Level 2 function  `\textsf{her2}` and computes the hermitian rank-2 update of the matrix `\boldsymbol{A}`, defined as

    .. math:: 
        \textsf{her2}=  \alpha \boldsymbol{x} \boldsymbol{y}^H +  \alpha^* \boldsymbol{y} \boldsymbol{x}^H +\boldsymbol{A}.




    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf(); mp14.setdps(15)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 


        >>> Res = A * B.T + B * A.T; Res.show("Res")
        Res: 
        148022, 203642, 259262, 314882, 370502, 426122, 
        203642, 260462, 317282, 374102, 430922, 487742, 
        259262, 317282, 375302, 433322, 491342, 549362, 
        314882, 374102, 433322, 492542, 551762, 610982, 
        370502, 430922, 491342, 551762, 612182, 672602, 
        426122, 487742, 549362, 610982, 672602, 734222, 


        >>> C = A.rank_2k_update(B); C.show("C")
        C: 
        148022, 203642, 259262, 314882, 370502, 426122, 
        203642, 260462, 317282, 374102, 430922, 487742, 
        259262, 317282, 375302, 433322, 491342, 549362, 
        314882, 374102, 433322, 492542, 551762, 610982, 
        370502, 430922, 491342, 551762, 612182, 672602, 
        426122, 487742, 549362, 610982, 672602, 734222, 





Quadratic forms (statistics), and related expressions
------------------------------------------------------------------------------------------

.. method:: mat.QuadraticForm(matX)

    In multivariate statistics, if `x` is a vector of  n random variables, and `A` is an  n-dimensional symmetric matrix, then the scalar quantity `x^T A x` is known as a quadratic form in `x`. See also:  Wikipedia :cite:p:`WikipediaMat14`.


    In general, this calculates expressions of the form `X^T A X`.


    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf(); mp14.setdps(15)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
        A: 
        44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
        25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
        50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
        47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
        26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
        62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

        >>> X = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); X.show("X")
        X: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 


        >>> Res = X * A * X.T; Res.show("Res")
        Res: 
        1473703456.6, 1489834996.6, 1505966536.6, 1522098076.6, 1538229616.6, 1554361156.6, 
        1489834996.6, 1506143116.6, 1522451236.6, 1538759356.6, 1555067476.6, 1571375596.6, 
        1505966536.6, 1522451236.6, 1538935936.6, 1555420636.6, 1571905336.6, 1588390036.6, 
        1522098076.6, 1538759356.6, 1555420636.6, 1572081916.6, 1588743196.6, 1605404476.6, 
        1538229616.6, 1555067476.6, 1571905336.6, 1588743196.6, 1605581056.6, 1622418916.6, 
        1554361156.6, 1571375596.6, 1588390036.6, 1605404476.6, 1622418916.6, 1639433356.6, 


        >>> C = A.quadratic_form(X); C.show("C")
        C: 
        1473703456.6, 1489834996.6, 1505966536.6, 1522098076.6, 1538229616.6, 1554361156.6, 
        1489834996.6, 1506143116.6, 1522451236.6, 1538759356.6, 1555067476.6, 1571375596.6, 
        1505966536.6, 1522451236.6, 1538935936.6, 1555420636.6, 1571905336.6, 1588390036.6, 
        1522098076.6, 1538759356.6, 1555420636.6, 1572081916.6, 1588743196.6, 1605404476.6, 
        1538229616.6, 1555067476.6, 1571905336.6, 1588743196.6, 1605581056.6, 1622418916.6, 
        1554361156.6, 1571375596.6, 1588390036.6, 1605404476.6, 1622418916.6, 1639433356.6, 







Matrix Multiplication with a selfadjoint matrix ("symm", "hemm")
------------------------------------------------------------------------------------------------


Particularly when dealing with covariance and correlation matrices, we encounter expressions like

`\boldsymbol{C} = \boldsymbol{A} \boldsymbol{B}` or `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}`, 

where `\boldsymbol{B}` and `\boldsymbol{C}` are general `m` by `n` matrices, and `\boldsymbol{A}` is a selfadjoint matrix. The dimension of `\boldsymbol{A}` is `m` by `m` for `\boldsymbol{C} = \boldsymbol{A} \boldsymbol{B}` and `n` by `n` for `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}`.


In the canonical FORTRAN package BLAS, the BLAS Level 3 functions `\mathrm{?symm, ?hemm}` and the BLAS Level 2 function `\mathrm{?symv, ?hemv}` handle this kind of expression, with the scalars `\alpha` and `\beta`, and the indicator variables `\textsf{Side}` and `\textsf{Uplo}` (which determines whether the upper or lower triangle and diagonal of `\boldsymbol{A}` will be used, and is omitted in the equations below) as additional parameters:


.. math:: 
    \textsf{?symm, ?hemm}=\begin{cases}
        \alpha \boldsymbol{A} \boldsymbol{B} + \beta \boldsymbol{C}, & \text{for } \textsf{Side = 'L'} \\
        \alpha \boldsymbol{B} \boldsymbol{A} + \beta \boldsymbol{C}, & \text{for } \textsf{Side = 'R'} \\        
    \end{cases}


.. math:: 
    \textsf{?symv, ?hemv}= \alpha \boldsymbol{A} \boldsymbol{x} + \beta \boldsymbol{y}.



We use the ``selfadjointview()`` property compute these expressions efficiently:



.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
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

    >>> C = A * B; C.show("C")
    C: 
    240701.7, 240958.4, 241215.1, 241471.8, 241728.5, 241985.2, 
    253079.5, 253349.0, 253618.5, 253888.0, 254157.5, 254427.0, 
    289368.7, 289678.4, 289988.1, 290297.8, 290607.5, 290917.2, 
    391682.4, 392100.8, 392519.2, 392937.6, 393356.0, 393774.4, 
    178935.4, 179126.8, 179318.2, 179509.6, 179701.0, 179892.4, 
    299978.1, 300298.2, 300618.3, 300938.4, 301258.5, 301578.6, 

    >>> # same as A.selfadjoint_lower_view() * B, if A is a full matrix
    >>> C = A.selfadjoint_upper_view() * B; C.show("C")
    C: 
    240701.7, 240958.4, 241215.1, 241471.8, 241728.5, 241985.2, 
    253079.5, 253349.0, 253618.5, 253888.0, 254157.5, 254427.0, 
    289368.7, 289678.4, 289988.1, 290297.8, 290607.5, 290917.2, 
    391682.4, 392100.8, 392519.2, 392937.6, 393356.0, 393774.4, 
    178935.4, 179126.8, 179318.2, 179509.6, 179701.0, 179892.4, 
    299978.1, 300298.2, 300618.3, 300938.4, 301258.5, 301578.6, 

    >>> C = B * A; C.show("C")  # same as (A * B.T).T
    C: 
    234538.5, 246271.0, 282859.9, 382214.4, 174822.4, 292447.8, 
    237105.5, 248966.0, 285956.9, 386398.4, 176736.4, 295648.8, 
    239672.5, 251661.0, 289053.9, 390582.4, 178650.4, 298849.8, 
    242239.5, 254356.0, 292150.9, 394766.4, 180564.4, 302050.8, 
    244806.5, 257051.0, 295247.9, 398950.4, 182478.4, 305251.8, 
    247373.5, 259746.0, 298344.9, 403134.4, 184392.4, 308452.8, 

    >>> # same as B * A.selfadjoint_lower_view(), if A is a full matrix
    >>> C = B * A.selfadjoint_upper_view(); C.show("C")
    C: 
    240701.7, 240958.4, 241215.1, 241471.8, 241728.5, 241985.2, 
    253079.5, 253349.0, 253618.5, 253888.0, 254157.5, 254427.0, 
    289368.7, 289678.4, 289988.1, 290297.8, 290607.5, 290917.2, 
    391682.4, 392100.8, 392519.2, 392937.6, 393356.0, 393774.4, 
    178935.4, 179126.8, 179318.2, 179509.6, 179701.0, 179892.4, 
    299978.1, 300298.2, 300618.3, 300938.4, 301258.5, 301578.6, 







Matrix Multiplication with a triangular matrix ("trmm")
-------------------------------------------------------------------------------


Particularly when dealing with matrix decompositions, we encounter expressions like

`\boldsymbol{C} = \boldsymbol{A} \boldsymbol{B}` or `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}`, 

where `\boldsymbol{B}` and `\boldsymbol{C}` are general `m` by `n` matrices, and `\boldsymbol{A}` is a triangular matrix. The dimension of `\boldsymbol{A}` is `m` by `m` for `\boldsymbol{C} = \boldsymbol{A} \boldsymbol{B}` and `n` by `n` for `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}`. Instead of `\boldsymbol{A}`, `\boldsymbol{A}^T` or `\boldsymbol{A}^H` or also used.


In the canonical FORTRAN package BLAS, the BLAS Level 3 function `\mathrm{?trmm}` and the BLAS Level 2 function `\mathrm{?trmv}` handle this kind of expression, with the scalar `\alpha` and the indicator variables `\textsf{Uplo}`, `\textsf{Diag}`, `\textsf{Side}` and `\textsf{TransA}` as additional parameters. The indicator variable `\textsf{Uplo}` (which determines whether the upper or lower triangular is used) and `\textsf{Diag}` (which determines how the information on the diagonal is used) are omitted from the equations below, but are discussed in the examples in Python: 

.. math:: 
    \mathrm{?trmm}=\begin{cases}
        \alpha \boldsymbol{A} \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'N'},\\
        \alpha \boldsymbol{B} \boldsymbol{A}, & \text{for } \textsf{Side = 'R', TransA = 'N'},\\
        \alpha \boldsymbol{A}^T \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'T'},\\
        \alpha \boldsymbol{B} \boldsymbol{A}^T, & \text{for } \textsf{Side = 'R', TransA = 'T'},\\
        \alpha \boldsymbol{A}^H \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'C'},\\
        \alpha \boldsymbol{B} \boldsymbol{A}^H, & \text{for } \textsf{Side = 'R', TransA = 'C'},\\
    \end{cases}


.. math:: 
    \textsf{?trmv}=\begin{cases}
        \boldsymbol{A} \boldsymbol{x}, & \text{for } \textsf{TransA = 'N'},\\
        \boldsymbol{A}^T \boldsymbol{x}, & \text{for } \textsf{TransA = 'T'},\\
        \boldsymbol{A}^H \boldsymbol{x}, & \text{for } \textsf{TransA = 'C'}.
    \end{cases}



We use the ``?triangularview`` property  to compute these expressions efficiently:


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> mpm.dps = 40;
    >>> A = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableA4x4", "")
    >>> B = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableB4x4", "")

    >>> C = A.upper_triangularview() * B
    >>> C = A.lower_triangularview() * B

    >>> C = A.strictly_upper_triangularview() * B
    >>> C = A.strictly_lower_triangularview() * B

    >>> C = A.unit_upper_triangularview() * B
    >>> C = A.unit_lower_triangularview() * B


    >>> C = B * A.upper_triangularview()
    >>> C = B * A.lower_triangularview()

    >>> C = B * A.strictly_upper_triangularview()
    >>> C = B * A.strictly_lower_triangularview()

    >>> C = B * A.unit_upper_triangularview()
    >>> C = B * A.unit_lower_triangularview()


An example with a lower triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.lower_triangle(); B1.show("B1")
    B1: 
    911,   0,   0,   0,   0,   0, 
    921, 922,   0,   0,   0,   0, 
    931, 932, 933,   0,   0,   0, 
    941, 942, 943, 944,   0,   0, 
    951, 952, 953, 954, 955,   0, 
    961, 962, 963, 964, 965, 966, 

    >>> C = B1 * A; C.show("C")
    C: 
     10021,  10932,  11843,  12754,  13665,  14576, 
     29493,  31336,  33179,  35022,  36865,  38708, 
     58736,  61532,  64328,  67124,  69920,  72716, 
     98070, 101840, 105610, 109380, 113150, 116920, 
    147815, 152580, 157345, 162110, 166875, 171640, 
    208291, 214072, 219853, 225634, 231415, 237196, 

    >>> C = B.lower_triangle_view() * A; C.show("C")
    C: 
     10021,  10932,  11843,  12754,  13665,  14576, 
     29493,  31336,  33179,  35022,  36865,  38708, 
     58736,  61532,  64328,  67124,  69920,  72716, 
     98070, 101840, 105610, 109380, 113150, 116920, 
    147815, 152580, 157345, 162110, 166875, 171640, 
    208291, 214072, 219853, 225634, 231415, 237196, 


    >>> C = A * B1; C.show("C")
    C: 
     75991,  66040,  55034,  42950,  29765,  15456, 
    132151, 113140,  92954,  71570,  48965,  25116, 
    188311, 160240, 130874, 100190,  68165,  34776, 
    244471, 207340, 168794, 128810,  87365,  44436, 
    300631, 254440, 206714, 157430, 106565,  54096, 
    356791, 301540, 244634, 186050, 125765,  63756, 

    >>> C = A * B.lower_triangle_view(); C.show("C")
    C: 
     75991,  66040,  55034,  42950,  29765,  15456, 
    132151, 113140,  92954,  71570,  48965,  25116, 
    188311, 160240, 130874, 100190,  68165,  34776, 
    244471, 207340, 168794, 128810,  87365,  44436, 
    300631, 254440, 206714, 157430, 106565,  54096, 
    356791, 301540, 244634, 186050, 125765,  63756, 



An example with an upper triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.upper_triangle(); B1.show("B1")
    B1: 
    911, 912, 913, 914, 915, 916, 
      0, 922, 923, 924, 925, 926, 
      0,   0, 933, 934, 935, 936, 
      0,   0,   0, 944, 945, 946, 
      0,   0,   0,   0, 955, 956, 
      0,   0,   0,   0,   0, 966, 

    >>> C = B1 * A; C.show("C")
    C: 
    197491, 202972, 208453, 213934, 219415, 224896, 
    189520, 194140, 198760, 203380, 208000, 212620, 
    171998, 175736, 179474, 183212, 186950, 190688, 
    144605, 147440, 150275, 153110, 155945, 158780, 
    107021, 108932, 110843, 112754, 114665, 116576, 
     58926,  59892,  60858,  61824,  62790,  63756, 

    >>> C = B.upper_triangle_view() * A; C.show("C")
    C: 
    197491, 202972, 208453, 213934, 219415, 224896, 
    189520, 194140, 198760, 203380, 208000, 212620, 
    171998, 175736, 179474, 183212, 186950, 190688, 
    144605, 147440, 150275, 153110, 155945, 158780, 
    107021, 108932, 110843, 112754, 114665, 116576, 
     58926,  59892,  60858,  61824,  62790,  63756, 


    >>> C = A * B1; C.show("C")
    C: 
     10021,  21096,  33248,  46500,  60875,  76396, 
     19131,  39436,  60938,  83660, 107625, 132856, 
     28241,  57776,  88628, 120820, 154375, 189316, 
     37351,  76116, 116318, 157980, 201125, 245776, 
     46461,  94456, 144008, 195140, 247875, 302236, 
     55571, 112796, 171698, 232300, 294625, 358696, 

    >>> C = A * B.upper_triangle_view(); C.show("C")
    C: 
     10021,  21096,  33248,  46500,  60875,  76396, 
     19131,  39436,  60938,  83660, 107625, 132856, 
     28241,  57776,  88628, 120820, 154375, 189316, 
     37351,  76116, 116318, 157980, 201125, 245776, 
     46461,  94456, 144008, 195140, 247875, 302236, 
     55571, 112796, 171698, 232300, 294625, 358696, 




An example with a strictly lower triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.strictly_lower_triangle(); B1.show("B1")
    B1: 
      0,   0,   0,   0,   0,   0, 
    921,   0,   0,   0,   0,   0, 
    931, 932,   0,   0,   0,   0, 
    941, 942, 943,   0,   0,   0, 
    951, 952, 953, 954,   0,   0, 
    961, 962, 963, 964, 965,   0, 

    >>> C = B1 * A; C.show("C")
    C: 
         0,      0,      0,      0,      0,      0, 
     10131,  11052,  11973,  12894,  13815,  14736, 
     29813,  31676,  33539,  35402,  37265,  39128, 
     59366,  62192,  65018,  67844,  70670,  73496, 
     99110, 102920, 106730, 110540, 114350, 118160, 
    149365, 154180, 158995, 163810, 168625, 173440, 

    >>> C = B.strictly_lower_triangle_view() * A; C.show("C")
    C: 
         0,      0,      0,      0,      0,      0, 
     10131,  11052,  11973,  12894,  13815,  14736, 
     29813,  31676,  33539,  35402,  37265,  39128, 
     59366,  62192,  65018,  67844,  70670,  73496, 
     99110, 102920, 106730, 110540, 114350, 118160, 
    149365, 154180, 158995, 163810, 168625, 173440, 


    >>> C = A * B1; C.show("C")
    C: 
     65970,  54976,  42905,  29734,  15440,      0, 
    113020,  92856,  71495,  48914,  25090,      0, 
    160070, 130736, 100085,  68094,  34740,      0, 
    207120, 168616, 128675,  87274,  44390,      0, 
    254170, 206496, 157265, 106454,  54040,      0, 
    301220, 244376, 185855, 125634,  63690,      0, 

    >>> C = A * B.strictly_lower_triangle_view(); C.show("C")
    C: 
     65970,  54976,  42905,  29734,  15440,      0, 
    113020,  92856,  71495,  48914,  25090,      0, 
    160070, 130736, 100085,  68094,  34740,      0, 
    207120, 168616, 128675,  87274,  44390,      0, 
    254170, 206496, 157265, 106454,  54040,      0, 
    301220, 244376, 185855, 125634,  63690,      0, 



An example with an strictly upper triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.strictly_upper_triangle(); B1.show("B1")
    B1: 
      0, 912, 913, 914, 915, 916, 
      0,   0, 923, 924, 925, 926, 
      0,   0,   0, 934, 935, 936, 
      0,   0,   0,   0, 945, 946, 
      0,   0,   0,   0,   0, 956, 
      0,   0,   0,   0,   0,   0, 

    >>> C = B1 * A; C.show("C")
    C: 
    187470, 192040, 196610, 201180, 205750, 210320, 
    170158, 173856, 177554, 181252, 184950, 188648, 
    143075, 145880, 148685, 151490, 154295, 157100, 
    105901, 107792, 109683, 111574, 113465, 115356, 
     58316,  59272,  60228,  61184,  62140,  63096, 
         0,      0,      0,      0,      0,      0, 


    >>> C = B.strictly_upper_triangle_view() * A; C.show("C")
    C: 
    187470, 192040, 196610, 201180, 205750, 210320, 
    170158, 173856, 177554, 181252, 184950, 188648, 
    143075, 145880, 148685, 151490, 154295, 157100, 
    105901, 107792, 109683, 111574, 113465, 115356, 
     58316,  59272,  60228,  61184,  62140,  63096, 
         0,      0,      0,      0,      0,      0, 


    >>> C = A * B1; C.show("C")
    C: 
    0,  10032,  21119,  33284,  46550,  60940, 
    0,  19152,  39479,  61004,  83750, 107740, 
    0,  28272,  57839,  88724, 120950, 154540, 
    0,  37392,  76199, 116444, 158150, 201340, 
    0,  46512,  94559, 144164, 195350, 248140, 
    0,  55632, 112919, 171884, 232550, 294940, 

    >>> C = A * B.strictly_upper_triangle_view(); C.show("C")
    C: 
    0,  10032,  21119,  33284,  46550,  60940, 
    0,  19152,  39479,  61004,  83750, 107740, 
    0,  28272,  57839,  88724, 120950, 154540, 
    0,  37392,  76199, 116444, 158150, 201340, 
    0,  46512,  94559, 144164, 195350, 248140, 
    0,  55632, 112919, 171884, 232550, 294940, 





An example with a unit lower triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.unit_lower_triangle(); B1.show("B1")
    B1: 
      1,   0,   0,   0,   0,   0, 
    921,   1,   0,   0,   0,   0, 
    931, 932,   1,   0,   0,   0, 
    941, 942, 943,   1,   0,   0, 
    951, 952, 953, 954,   1,   0, 
    961, 962, 963, 964, 965,   1, 

    >>> C = B1 * A; C.show("C")
    C: 
        11,     12,     13,     14,     15,     16, 
     10152,  11074,  11996,  12918,  13840,  14762, 
     29844,  31708,  33572,  35436,  37300,  39164, 
     59407,  62234,  65061,  67888,  70715,  73542, 
     99161, 102972, 106783, 110594, 114405, 118216, 
    149426, 154242, 159058, 163874, 168690, 173506, 

    >>> C = B.unit_lower_triangle_view() * A; C.show("C")
    C: 
        11,     12,     13,     14,     15,     16, 
     10152,  11074,  11996,  12918,  13840,  14762, 
     29844,  31708,  33572,  35436,  37300,  39164, 
     59407,  62234,  65061,  67888,  70715,  73542, 
     99161, 102972, 106783, 110594, 114405, 118216, 
    149426, 154242, 159058, 163874, 168690, 173506, 

    >>> C = A * B1; C.show("C")
    C: 
     65981,  54988,  42918,  29748,  15455,     16, 
    113041,  92878,  71518,  48938,  25115,     26, 
    160101, 130768, 100118,  68128,  34775,     36, 
    207161, 168658, 128718,  87318,  44435,     46, 
    254221, 206548, 157318, 106508,  54095,     56, 
    301281, 244438, 185918, 125698,  63755,     66, 

    >>> C = A * B.unit_lower_triangle_view(); C.show("C")
    C: 
     65981,  54988,  42918,  29748,  15455,     16, 
    113041,  92878,  71518,  48938,  25115,     26, 
    160101, 130768, 100118,  68128,  34775,     36, 
    207161, 168658, 128718,  87318,  44435,     46, 
    254221, 206548, 157318, 106508,  54095,     56, 
    301281, 244438, 185918, 125698,  63755,     66, 



An example with an unit upper triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 

    >>> B1 = B.unit_upper_triangle(); B1.show("B1")
    B1: 
      1, 912, 913, 914, 915, 916, 
      0,   1, 923, 924, 925, 926, 
      0,   0,   1, 934, 935, 936, 
      0,   0,   0,   1, 945, 946, 
      0,   0,   0,   0,   1, 956, 
      0,   0,   0,   0,   0,   1, 

    >>> C = B1 * A; C.show("C")
    C: 
    187481, 192052, 196623, 201194, 205765, 210336, 
    170179, 173878, 177577, 181276, 184975, 188674, 
    143106, 145912, 148718, 151524, 154330, 157136, 
    105942, 107834, 109726, 111618, 113510, 115402, 
     58367,  59324,  60281,  61238,  62195,  63152, 
        61,     62,     63,     64,     65,     66, 

    >>> C = B.unit_upper_triangle_view() * A; C.show("C")
    C: 
    187481, 192052, 196623, 201194, 205765, 210336, 
    170179, 173878, 177577, 181276, 184975, 188674, 
    143106, 145912, 148718, 151524, 154330, 157136, 
    105942, 107834, 109726, 111618, 113510, 115402, 
     58367,  59324,  60281,  61238,  62195,  63152, 
        61,     62,     63,     64,     65,     66, 


    >>> C = A * B1; C.show("C")
    C: 
        11,  10044,  21132,  33298,  46565,  60956, 
        21,  19174,  39502,  61028,  83775, 107766, 
        31,  28304,  57872,  88758, 120985, 154576, 
        41,  37434,  76242, 116488, 158195, 201386, 
        51,  46564,  94612, 144218, 195405, 248196, 
        61,  55694, 112982, 171948, 232615, 295006, 

    >>> C = A * B.unit_upper_triangle_view(); C.show("C")
    C: 
        11,  10044,  21132,  33298,  46565,  60956, 
        21,  19174,  39502,  61028,  83775, 107766, 
        31,  28304,  57872,  88758, 120985, 154576, 
        41,  37434,  76242, 116488, 158195, 201386, 
        51,  46564,  94612, 144218, 195405, 248196, 
        61,  55694, 112982, 171948, 232615, 295006, 








Matrix multiplication with  a vector as diagonal matrix 
-------------------------------------------------------------------------------


Returns the matrix product of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have compatible dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> # read the first column from the matrix
    >>> d = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", "").col(0); d.show("d")
    d: 
    911, 
    921, 
    931, 
    941, 
    951, 
    961, 

    >>> # creates a square matrix with the coefficents of d1 on the diagonal.
    >>> D = d.as_diagonal(); D.show("D")
    D: 
    911,   0,   0,   0,   0,   0, 
      0, 921,   0,   0,   0,   0, 
      0,   0, 931,   0,   0,   0, 
      0,   0,   0, 941,   0,   0, 
      0,   0,   0,   0, 951,   0, 
      0,   0,   0,   0,   0, 961, 

    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> C = A * D; C.show("C")    # same as D * A()
    C: 
    10021, 11052, 12103, 13174, 14265, 15376, 
    19131, 20262, 21413, 22584, 23775, 24986, 
    28241, 29472, 30723, 31994, 33285, 34596, 
    37351, 38682, 40033, 41404, 42795, 44206, 
    46461, 47892, 49343, 50814, 52305, 53816, 
    55571, 57102, 58653, 60224, 61815, 63426, 

    >>> C = A * d.diagonal_view(); C.show("C")    # same as d.diagonal_view * A()
    C: 
    10021, 11052, 12103, 13174, 14265, 15376, 
    19131, 20262, 21413, 22584, 23775, 24986, 
    28241, 29472, 30723, 31994, 33285, 34596, 
    37351, 38682, 40033, 41404, 42795, 44206, 
    46461, 47892, 49343, 50814, 52305, 53816, 
    55571, 57102, 58653, 60224, 61815, 63426, 





Matrix coefficient-wise multiplication (array multiplication)
-------------------------------------------------------------------------------

Returns the coefficient-wise product of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have the same dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 
    >>> C = A.array_view() * B; C.show("C")
    C: 
    10021, 10944, 11869, 12796, 13725, 14656, 
    19341, 20284, 21229, 22176, 23125, 24076, 
    28861, 29824, 30789, 31756, 32725, 33696, 
    38581, 39564, 40549, 41536, 42525, 43516, 
    48501, 49504, 50509, 51516, 52525, 53536, 
    58621, 59644, 60669, 61696, 62725, 63756, 




Matrix Multiplication with scalar
-------------------------------------------------------------------------------


Returns the product of matrix ?matA and scalar `b`, applied to each coefficient of ?matA. The coefficients of ?matA and `b` need to be of the same type. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices and real and complex scalars.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = 2*A;  B.show("B")
    B: 
     22,  24,  26,  28,  30,  32, 
     42,  44,  46,  48,  50,  52, 
     62,  64,  66,  68,  70,  72, 
     82,  84,  86,  88,  90,  92, 
    102, 104, 106, 108, 110, 112, 
    122, 124, 126, 128, 130, 132, 









Matrix multiplication with the inverse of a general invertible matrix ("matrix division")
------------------------------------------------------------------------------------------------


Returns the matrix product of the multiplicative inverse of matrix `A`, `A^{-1}`, with the  matrix `B`, when only `A` but not `A^{-1}` is explicitly given. `A` and `B` need to be of the same type and need to have compatible dimensions with regard to matrix multiplication, and `A` needs to be invertible. Special rules apply for mixing real and complex matrices.

To evaluate the expression `x = A^{-1} * b`, we calculate x as the solution to the linear system `A*x = b`.

To evaluate the expression `x = b * A^{-1}`, we calculate x as the solution to the linear system `A^T*x^T = b^T`.

Particularly if `b` is a vector, this is much more efficient than calculating the inverse explicitely.

For `x = b * A^{-1}`, one can also write `x = b / A`

For `x = A^{-1} * b`, one can also write `x = A.\text{solve}(b)`. This is equivalent to Matlab's `\backslash` operator, like `x = A \backslash b`, which is not available in Python.



.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(15)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", ""); A.show("A")

    >>> # Should be a full random matrix, not SA
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


    >>> Ainv = A.lu_inverse(); mp14.setdps(5); Ainv.show("Ainv"); mp14.setdps(15)
    Ainv: 
     0.01126,  0.04256, -0.06327, 0.007677, -0.01281,  0.03752, 
     0.04592,  0.03192,  -0.2010, -0.01155,  0.01363,   0.1270, 
    -0.01211, -0.05226,   0.1292, -0.03402,  0.03217, -0.08354, 
    0.007192,  0.07568,  -0.2825,  -0.1415,  0.09012,   0.2278, 
    -0.02892,  0.09395,  -0.2203, -0.06359,  0.06268,   0.1686, 
    -0.03631,  -0.1895,   0.6720,   0.1984,  -0.1483,  -0.4734, 


    >>> D1 = A * Ainv; mp14.setdps(5); D1.show("D1"); mp14.setdps(15)
    D1: 
       1.000,        0,   -1E-12,   -1E-13,        0,        0, 
     1.7E-13,    1.000,   -8E-13,   -1E-13,   -1E-13,   -6E-13, 
       1E-13,   -1E-13,    1.000,    1E-13,   -1E-13,        0, 
    -2.1E-13,        0,        0,    1.000,        0,    1E-12, 
       9E-14,    2E-13,        0,        0,    1.000,    1E-12, 
      -1E-13,    1E-13,   -2E-12,        0,        0,    1.000, 

    >>> E1 = Ainv *  B; mp14.setdps(5); E1.show("E1"); mp14.setdps(15)
    E1: 
     21.65,  21.67,  21.69,  21.72,  21.74,  21.76, 
     8.210,  8.216,  8.222,  8.228,  8.234,  8.240, 
    -20.54, -20.56, -20.58, -20.60, -20.62, -20.64, 
    -15.32, -15.34, -15.36, -15.39, -15.41, -15.43, 
     16.93,  16.94,  16.96,  16.97,  16.98,  16.99, 
     8.733,  8.756,  8.778,  8.801,  8.824,  8.847, 

    >>> # This is the same as A^-1 * B = A.solve(B)
    >>> E2 = A.lu_solve(B); mp14.setdps(5); E2.show("E2"); mp14.setdps(15)
    E2: 
     21.65,  21.67,  21.69,  21.72,  21.74,  21.76, 
     8.210,  8.216,  8.222,  8.228,  8.234,  8.240, 
    -20.54, -20.56, -20.58, -20.60, -20.62, -20.64, 
    -15.32, -15.34, -15.36, -15.39, -15.41, -15.43, 
     16.93,  16.94,  16.96,  16.97,  16.98,  16.99, 
     8.733,  8.756,  8.778,  8.801,  8.824,  8.847, 

    >>> E3 = B * Ainv; mp14.setdps(5); E3.show("E3"); mp14.setdps(15)
    E3: 
    -12.06,  1.703,  32.75, -40.39,  34.05,  2.612, 
    -12.19,  1.726,  33.09, -40.83,  34.42,  2.652, 
    -12.32,  1.749,  33.43, -41.28,  34.80,  2.692, 
    -12.45,  1.772,  33.77, -41.72,  35.17,  2.732, 
    -12.58,  1.796,  34.11, -42.17,  35.55,  2.772, 
    -12.71,  1.819,  34.45, -42.61,  35.92,  2.813, 

    >>> # This is the same as B * A^-1
    >>> E4 = (Ainv.T *  B.T).T; mp14.setdps(5); E4.show("E4"); mp14.setdps(15)
    E4: 
    -12.06,  1.703,  32.75, -40.39,  34.05,  2.612, 
    -12.19,  1.726,  33.09, -40.83,  34.42,  2.652, 
    -12.32,  1.749,  33.43, -41.28,  34.80,  2.692, 
    -12.45,  1.772,  33.77, -41.72,  35.17,  2.732, 
    -12.58,  1.796,  34.11, -42.17,  35.55,  2.772, 
    -12.71,  1.819,  34.45, -42.61,  35.92,  2.813, 

    >>> # This is the same as B * A^-1 = B/A.upper_triangle()
    >>> E6 = A.T.lu_solve(B.T).T; mp14.setdps(5); E6.show("E6"); mp14.setdps(15)
    E6: 
    -12.06,  1.703,  32.75, -40.39,  34.05,  2.612, 
    -12.19,  1.726,  33.09, -40.83,  34.42,  2.652, 
    -12.32,  1.749,  33.43, -41.28,  34.80,  2.692, 
    -12.45,  1.772,  33.77, -41.72,  35.17,  2.732, 
    -12.58,  1.796,  34.11, -42.17,  35.55,  2.772, 
    -12.71,  1.819,  34.45, -42.61,  35.92,  2.813, 






Matrix multiplication with the inverse of a self-adjoint matrix ("ldlt solve")
----------------------------------------------------------------------------------------


Returns the matrix product of the multiplicative inverse of matrix `A`, `A^{-1}`, with the  matrix or vector `b`, when only `A` but not `A^{-1}` is explicitly given. `A` and `b` need to be of the same type and need to have compatible dimensions with regard to matrix multiplication, and `A` needs to be invertible. Special rules apply for mixing real and complex matrices.

To evaluate the expression `x = A^{-1} * b`, we calculate x as the solution to the linear system `A*x = b`.

To evaluate the expression `x = b * A^{-1}`, we calculate x as the solution to the linear system `A^T*x^T = b^T`.

Particularly if `b` is a vector, this is much more efficient than calculating the inverse explicitely.

For `x = b * A^{-1}`, one can also write `x = b / A`

For `x = A^{-1} * b`, one can also write `x = A.\text{solve}(b)`. This is equivalent to Matlab's `\backslash` operator, like `x = A \backslash b`, which is not available in Python.



.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(15)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", ""); A.show("A")
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

    >>> # Should be llt
    >>> Ainv = A.lu_inverse(); mp14.setdps(5); Ainv.show("Ainv"); mp14.setdps(15)
    Ainv: 
      0.02928,  -0.02516,   0.04360, -0.008938,  -0.03887, -0.006430, 
     -0.02516, -0.006656,  0.002689,   0.01296,  0.003418,  0.007326, 
      0.04360,  0.002689,   0.05468,  0.008513,  -0.08586,  -0.04679, 
    -0.008938,   0.01296,  0.008513, -0.002346,  -0.01091, 0.0007357, 
     -0.03887,  0.003418,  -0.08586,  -0.01091,    0.1414,   0.04422, 
    -0.006430,  0.007326,  -0.04679, 0.0007357,   0.04422,   0.01998, 


    >>> D1 = A * Ainv; mp14.setdps(5); D1.show("D1"); mp14.setdps(15)
    D1: 
       1.000,   -9E-14,        0, -1.5E-14,   -2E-13,   -1E-13, 
      -6E-14,    1.000,        0,    3E-15,   -1E-13,  1.3E-13, 
       4E-14, -1.7E-13,    1.000,  1.5E-14,   -1E-13, -1.2E-13, 
      -5E-14, -1.4E-13,   -2E-13,    1.000,        0,    1E-13, 
    -3.7E-14, -4.1E-14, -1.6E-13, -1.6E-15,    1.000,    3E-14, 
     1.3E-13,   -4E-14,    1E-13, -2.4E-14,   -1E-13,    1.000, 

    >>> E1 = Ainv *  B; mp14.setdps(5); E1.show("E1"); mp14.setdps(15)
    E1: 
     -7.464,  -7.471,  -7.477,  -7.484,  -7.490,  -7.497, 
     -4.067,  -4.072,  -4.078,  -4.083,  -4.088,  -4.094, 
     -25.51,  -25.53,  -25.56,  -25.58,  -25.60,  -25.63, 
    -0.1580, -0.1580, -0.1580, -0.1580, -0.1580, -0.1580, 
      54.47,   54.52,   54.58,   54.63,   54.68,   54.74, 
      19.27,   19.29,   19.31,   19.33,   19.35,   19.37, 

    >>> # Should be llt
    >>> # This is the same as A^-1 * B = A.solve(B)
    >>> E2 = A.lu_solve(B); mp14.setdps(5); E2.show("E2"); mp14.setdps(15)
    E2: 
     -7.464,  -7.471,  -7.477,  -7.484,  -7.490,  -7.497, 
     -4.067,  -4.072,  -4.078,  -4.083,  -4.088,  -4.094, 
     -25.51,  -25.53,  -25.56,  -25.58,  -25.60,  -25.63, 
    -0.1580, -0.1580, -0.1580, -0.1580, -0.1580, -0.1580, 
      54.47,   54.52,   54.58,   54.63,   54.68,   54.74, 
      19.27,   19.29,   19.31,   19.33,   19.35,   19.37, 

    >>> E3 = B * Ainv; mp14.setdps(5); E3.show("E3"); mp14.setdps(15)
    E3: 
       -6.093,    -4.858,    -21.55, -0.004965,     49.20,     17.54, 
       -6.158,    -4.912,    -21.78, -0.004833,     49.73,     17.73, 
       -6.223,    -4.966,    -22.02, -0.004700,     50.27,     17.92, 
       -6.288,    -5.021,    -22.25, -0.004568,     50.80,     18.11, 
       -6.354,    -5.075,    -22.48, -0.004436,     51.33,     18.30, 
       -6.419,    -5.129,    -22.71, -0.004304,     51.87,     18.49, 

    >>> # This is the same as B * A^-1
    >>> E4 = (Ainv.T *  B.T).T; mp14.setdps(5); E4.show("E4"); mp14.setdps(15)
    E4: 
       -6.093,    -4.858,    -21.55, -0.004965,     49.20,     17.54, 
       -6.158,    -4.912,    -21.78, -0.004833,     49.73,     17.73, 
       -6.223,    -4.966,    -22.02, -0.004700,     50.27,     17.92, 
       -6.288,    -5.021,    -22.25, -0.004568,     50.80,     18.11, 
       -6.354,    -5.075,    -22.48, -0.004436,     51.33,     18.30, 
       -6.419,    -5.129,    -22.71, -0.004304,     51.87,     18.49, 

    >>> # Should be llt
    >>> # This is the same as B * A^-1 = B/A.upper_triangle()
    >>> E6 = A.T.lu_solve(B.T).T; mp14.setdps(5); E6.show("E6"); mp14.setdps(15)
    E6: 
       -6.093,    -4.858,    -21.55, -0.004965,     49.20,     17.54, 
       -6.158,    -4.912,    -21.78, -0.004833,     49.73,     17.73, 
       -6.223,    -4.966,    -22.02, -0.004700,     50.27,     17.92, 
       -6.288,    -5.021,    -22.25, -0.004568,     50.80,     18.11, 
       -6.354,    -5.075,    -22.48, -0.004436,     51.33,     18.30, 
       -6.419,    -5.129,    -22.71, -0.004304,     51.87,     18.49, 






Matrix multiplication with the inverse of a triangular matrix ("trsm")
-------------------------------------------------------------------------------

Particularly when dealing with matrix decompositions, we encounter expressions like

`\boldsymbol{C} = \boldsymbol{A}^{-1} \boldsymbol{B}` or `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}^{-1}`, 

where `\boldsymbol{B}` and `\boldsymbol{C}` are general `m` by `n` matrices, and `\boldsymbol{A}` is a triangular matrix. The dimension of `\boldsymbol{A}` is `m` by `m` for `\boldsymbol{C} = \boldsymbol{A}^{-1} \boldsymbol{B}` and `n` by `n` for `\boldsymbol{C} = \boldsymbol{B} \boldsymbol{A}^{-1}`. Key to an efficient evaluation of this sort of expression is the insight that it can be considered as the solution of a system of linear equations, without the need to actually invert `\boldsymbol{A}` explicitly.

See also Eigen :cite:p:`EigenMat100`.


In the canonical FORTRAN package BLAS, the BLAS Level 3 function `\mathrm{?trsm}` and the BLAS Level 2 function `\mathrm{?trsv}` handle this kind of expression, with the scalar `\alpha` and the indicator variables `\textsf{Uplo}`, `\textsf{Diag}`, `\textsf{Side}` and `\textsf{TransA}` as additional parameters. The indicator variable `\textsf{Uplo}` (which determines whether the upper or lower triangular is used) and `\textsf{Diag}` (which determines how the information on the diagonal is used) are omitted from the equations below, but are discussed in the examples in Python: 


.. math:: 
    \textsf{?trsm}=\begin{cases}
        \alpha \boldsymbol{A}^{-1} \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'N'},\\
        \alpha \boldsymbol{B} \boldsymbol{A}^{-1}, & \text{for } \textsf{Side = 'R', TransA = 'N'},\\
        \alpha \left(\boldsymbol{A}^T \right)^{-1} \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'T'},\\
        \alpha \boldsymbol{B} \left(\boldsymbol{A}^T \right)^{-1}, & \text{for } \textsf{Side = 'R', TransA = 'T'},\\
        \alpha \left(\boldsymbol{A}^H \right)^{-1} \boldsymbol{B}, & \text{for } \textsf{Side = 'L', TransA = 'C'},\\
        \alpha \boldsymbol{B} \left(\boldsymbol{A}^H \right)^{-1}, & \text{for } \textsf{Side = 'R', TransA = 'C'},\\
    \end{cases}


.. math:: 
    \textsf{?trsv}=\begin{cases}
        \boldsymbol{A}^{-1} \boldsymbol{x} & \text{for } \textsf{TransA = 'N'},\\
        \left(\boldsymbol{A}^T\right)^{-1} \boldsymbol{x}, & \text{for } \textsf{TransA = 'T'},\\
        \left(\boldsymbol{A}^H\right)^{-1} \boldsymbol{x}, & \text{for } \textsf{TransA = 'C'}.
    \end{cases}


We use the ``triangularview()`` property together with the ``solve`` method to compute these expressions efficiently:


Returns the matrix product of the multiplicative inverse of matrix `A`, `A^{-1}`, with the  matrix `B`, when only `A` but not `A^{-1}` is explicitly given. `A` and `B` need to be of the same type and need to have compatible dimensions with regard to matrix multiplication, and `A` needs to be invertible. Special rules apply for mixing real and complex matrices.

To evaluate the expression `x = A^{-1} * b`, we calculate x as the solution to the linear system `A*x = b`.

To evaluate the expression `x = b * A^{-1}`, we calculate x as the solution to the linear system `A^T*x^T = b^T`.

Particularly if `b` is a vector, this is much more efficient than calculating the inverse explicitely.

For `x = b * A^{-1}`, one can also write `x = b / A`

For `x = A^{-1} * b`, one can also write `x = A.\text{solve}(b)`. This is equivalent to Matlab's `\backslash` operator, like `x = A \backslash b`, which is not available in Python.




.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> mpm.dps = 40;
    >>> A = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableA4x4", "")
    >>> B = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableB4x4", "")

    >>> C = A.upper_triangularview().solve(B)
    >>> C = A.lower_triangularview().solve(B)

    >>> C = A.unit_upper_triangularview().solve(B)
    >>> C = A.unit_lower_triangularview().solve(B)




An example with an unit upper triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(15)
    >>> A0 = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A0.show("A0")
    A0: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> A = A0.upper_triangle(); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
     0, 22, 23, 24, 25, 26, 
     0,  0, 33, 34, 35, 36, 
     0,  0,  0, 44, 45, 46, 
     0,  0,  0,  0, 55, 56, 
     0,  0,  0,  0,  0, 66, 


    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 


    >>> Ainv = A.lu_inverse(); mp14.setdps(5); Ainv.show("Ainv"); mp14.setdps(15)
    Ainv: 
        0.09091,    -0.04959,   -0.001252,  -0.0009107,  -0.0007120,  -0.0005825, 
              0,     0.04545,    -0.03168,  -0.0003130,  -0.0002447,  -0.0002002, 
              0,           0,     0.03030,    -0.02342,  -0.0001252,  -0.0001025, 
              0,           0,           0,     0.02273,    -0.01860, -0.00006261, 
              0,           0,           0,           0,     0.01818,    -0.01543, 
              0,           0,           0,           0,           0,     0.01515, 

    >>> D1 = A * Ainv; mp14.setdps(3); D1.show("D1"); mp14.setdps(15)
    D1: 
         1.0,        0,        0,        0,        0,        0, 
           0,      1.0,  1.0E-14,        0,        0,        0, 
           0,        0,      1.0,  2.0E-14,        0,        0, 
           0,        0,        0,      1.0, -1.0E-14,        0, 
           0,        0,        0,        0,      1.0,   -1E-14, 
           0,        0,        0,        0,        0,      1.0, 

    >>> E1 = Ainv *  B; mp14.setdps(5); E1.show("E1"); mp14.setdps(15)
    E1: 
    33.89, 33.93, 33.96, 34.00, 34.04, 34.08, 
    11.65, 11.66, 11.68, 11.69, 11.70, 11.71, 
    5.960, 5.967, 5.973, 5.980, 5.987, 5.993, 
    3.642, 3.646, 3.650, 3.655, 3.659, 3.663, 
    2.466, 2.468, 2.471, 2.474, 2.477, 2.479, 
    14.56, 14.58, 14.59, 14.61, 14.62, 14.64, 

    >>> # This is the same as A^-1 * B = A.solve(B)
    >>> E2 = A.upper_triangle_solve(B); mp14.setdps(5); E2.show("E2"); mp14.setdps(15)
    E2: 
    33.89, 33.93, 33.96, 34.00, 34.04, 34.08, 
    11.65, 11.66, 11.68, 11.69, 11.70, 11.71, 
    5.960, 5.967, 5.973, 5.980, 5.987, 5.993, 
    3.642, 3.646, 3.650, 3.655, 3.659, 3.663, 
    2.466, 2.468, 2.471, 2.474, 2.477, 2.479, 
    14.56, 14.58, 14.59, 14.61, 14.62, 14.64, 

    >>> E3 = B * Ainv; mp14.setdps(5); E3.show("E3"); mp14.setdps(15)
    E3: 
     82.82, -3.719, -2.367, -1.721, -1.346, -1.101, 
     83.73, -3.760, -2.393, -1.740, -1.361, -1.113, 
     84.64, -3.802, -2.419, -1.759, -1.376, -1.125, 
     85.55, -3.843, -2.446, -1.779, -1.391, -1.138, 
     86.45, -3.884, -2.472, -1.798, -1.405, -1.150, 
     87.36, -3.926, -2.498, -1.817, -1.420, -1.162, 

    >>> # This is the same as B * A^-1
    >>> E4 = (Ainv.T *  B.T).T; mp14.setdps(5); E4.show("E4"); mp14.setdps(15)
    E4: 
     82.82, -3.719, -2.367, -1.721, -1.346, -1.101, 
     83.73, -3.760, -2.393, -1.740, -1.361, -1.113, 
     84.64, -3.802, -2.419, -1.759, -1.376, -1.125, 
     85.55, -3.843, -2.446, -1.779, -1.391, -1.138, 
     86.45, -3.884, -2.472, -1.798, -1.405, -1.150, 
     87.36, -3.926, -2.498, -1.817, -1.420, -1.162, 

    >>> # This is the same as B * A^-1 = B/A.upper_triangle()
    >>> E6 = A.T.lower_triangle_solve(B.T).T; mp14.setdps(5); E6.show("E6"); mp14.setdps(15)
    E6: 
     82.82, -3.719, -2.367, -1.721, -1.346, -1.101, 
     83.73, -3.760, -2.393, -1.740, -1.361, -1.113, 
     84.64, -3.802, -2.419, -1.759, -1.376, -1.125, 
     85.55, -3.843, -2.446, -1.779, -1.391, -1.138, 
     86.45, -3.884, -2.472, -1.798, -1.405, -1.150, 
     87.36, -3.926, -2.498, -1.817, -1.420, -1.162, 




An example with a lower triangular matrix:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(15)
    >>> A0 = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A0.show("A0")
    A0: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 

    >>> A = A0.lower_triangle(); A.show("A")
    A: 
    11,  0,  0,  0,  0,  0, 
    21, 22,  0,  0,  0,  0, 
    31, 32, 33,  0,  0,  0, 
    41, 42, 43, 44,  0,  0, 
    51, 52, 53, 54, 55,  0, 
    61, 62, 63, 64, 65, 66, 


    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 


    >>> Ainv = A.lu_inverse(); mp14.setdps(5); Ainv.show("Ainv"); mp14.setdps(15)
    Ainv: 
        0.0909,          0,   1.09E-15,  -1.82E-15,   9.09E-16,  -1.64E-15, 
       -0.0868,     0.0455,  -2.68E-15,   1.33E-15,  -1.35E-15,   9.09E-16, 
      -0.00125,    -0.0441,     0.0303,   4.47E-16,   4.47E-16,   1.44E-17, 
     -0.000655,  -0.000313,    -0.0296,     0.0227,          0,   1.42E-17, 
     -0.000405,  -0.000194,  -0.000125,    -0.0223,     0.0182,  -8.95E-16, 
     -0.000276,  -0.000132, -0.0000854, -0.0000626,    -0.0179,     0.0152, 

    >>> D1 = A * Ainv; mp14.setdps(3); D1.show("D1"); mp14.setdps(15)
    D1: 
         1.0,        0,  1.2E-14, -2.0E-14,  1.0E-14, -1.8E-14, 
           0,      1.0, -3.6E-14, -8.8E-15, -1.1E-14, -1.4E-14, 
    -2.8E-14,        0,      1.0,  1.1E-15, -2.2E-16, -2.1E-14, 
     3.3E-14, -1.3E-13, -1.0E-13,      1.0, -1.5E-16, -2.8E-14, 
     9.4E-14, -5.2E-14, -8.2E-14,        0,      1.0, -8.4E-14, 
     6.7E-14, -3.2E-14,  5.2E-15, -4.5E-14,        0,      1.0, 

    >>> E1 = Ainv *  B; mp14.setdps(5); E1.show("E1"); mp14.setdps(15)
    E1: 
     82.82,  82.91,  83.00,  83.09,  83.18,  83.27, 
    -37.19, -37.23, -37.27, -37.31, -37.36, -37.40, 
    -13.52, -13.54, -13.55, -13.57, -13.58, -13.60, 
    -7.069, -7.077, -7.085, -7.093, -7.101, -7.108, 
    -4.370, -4.375, -4.380, -4.385, -4.389, -4.394, 
    -2.980, -2.983, -2.986, -2.990, -2.993, -2.996, 

    >>> # This is the same as A^-1 * B = A.solve(B)
    >>> E2 = A.lower_triangle_solve(B); mp14.setdps(5); E2.show("E2"); mp14.setdps(15)
    E2: 
     82.82,  82.91,  83.00,  83.09,  83.18,  83.27, 
    -37.19, -37.23, -37.27, -37.31, -37.36, -37.40, 
    -13.52, -13.54, -13.55, -13.57, -13.58, -13.60, 
    -7.069, -7.077, -7.085, -7.093, -7.101, -7.108, 
    -4.370, -4.375, -4.380, -4.385, -4.389, -4.394, 
    -2.980, -2.983, -2.986, -2.990, -2.993, -2.996, 

    >>> E3 = B * Ainv; mp14.setdps(5); E3.show("E3"); mp14.setdps(15)
    E3: 
     1.313, 0.6281, 0.4064, 0.2980, 0.2342,  13.88, 
     1.329, 0.6355, 0.4112, 0.3015, 0.2369,  14.03, 
     1.344, 0.6428, 0.4160, 0.3050, 0.2397,  14.18, 
     1.360, 0.6502, 0.4207, 0.3085, 0.2424,  14.33, 
     1.375, 0.6576, 0.4255, 0.3120, 0.2452,  14.48, 
     1.390, 0.6650, 0.4303, 0.3156, 0.2479,  14.64, 

    >>> # This is the same as B * A^-1
    >>> E4 = (Ainv.T *  B.T).T; mp14.setdps(5); E4.show("E4"); mp14.setdps(15)
    E4: 
     1.313, 0.6281, 0.4064, 0.2980, 0.2342,  13.88, 
     1.329, 0.6355, 0.4112, 0.3015, 0.2369,  14.03, 
     1.344, 0.6428, 0.4160, 0.3050, 0.2397,  14.18, 
     1.360, 0.6502, 0.4207, 0.3085, 0.2424,  14.33, 
     1.375, 0.6576, 0.4255, 0.3120, 0.2452,  14.48, 
     1.390, 0.6650, 0.4303, 0.3156, 0.2479,  14.64, 

    >>> # This is the same as B * A^-1 = B/A.upper_triangle()
    >>> E6 = A.T.upper_triangle_solve(B.T).T; mp14.setdps(5); E6.show("E6"); mp14.setdps(15)
    E6: 
     1.313, 0.6281, 0.4064, 0.2980, 0.2342,  13.88, 
     1.329, 0.6355, 0.4112, 0.3015, 0.2369,  14.03, 
     1.344, 0.6428, 0.4160, 0.3050, 0.2397,  14.18, 
     1.360, 0.6502, 0.4207, 0.3085, 0.2424,  14.33, 
     1.375, 0.6576, 0.4255, 0.3120, 0.2452,  14.48, 
     1.390, 0.6650, 0.4303, 0.3156, 0.2479,  14.64, 







Matrix coefficient-wise division (array division)
-------------------------------------------------------------------------------


Returns the coefficient-wise quotient of matrix ?matA and matrix matB. ?matA and matB need to be of the same type and need to have the same dimensions. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
    B: 
    911, 912, 913, 914, 915, 916, 
    921, 922, 923, 924, 925, 926, 
    931, 932, 933, 934, 935, 936, 
    941, 942, 943, 944, 945, 946, 
    951, 952, 953, 954, 955, 956, 
    961, 962, 963, 964, 965, 966, 
    >>> mp14.setdps(5)
    >>> C = A.array_view() / B; C.show("C")
    C: 
    0.01207, 0.01316, 0.01424, 0.01532, 0.01639, 0.01747, 
    0.02280, 0.02386, 0.02492, 0.02597, 0.02703, 0.02808, 
    0.03330, 0.03433, 0.03537, 0.03640, 0.03743, 0.03846, 
    0.04357, 0.04459, 0.04560, 0.04661, 0.04762, 0.04863, 
    0.05363, 0.05462, 0.05561, 0.05660, 0.05759, 0.05858, 
    0.06348, 0.06445, 0.06542, 0.06639, 0.06736, 0.06832, 





Matrix division by scalar
-------------------------------------------------------------------------------


Returns the quotient of matrix ?matA and scalar `b`, applied to each coefficient of ?matA. The coefficients of ?matA and `b` need to be of the same type. The returned matrix is of the same type as ?matA. Special rules apply for mixing real and complex matrices and real and complex scalars.


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
    A: 
    11, 12, 13, 14, 15, 16, 
    21, 22, 23, 24, 25, 26, 
    31, 32, 33, 34, 35, 36, 
    41, 42, 43, 44, 45, 46, 
    51, 52, 53, 54, 55, 56, 
    61, 62, 63, 64, 65, 66, 
    >>> B = A / 2;  B.show("B")
    B: 
     5.5,  6.0,  6.5,  7.0,  7.5,  8.0, 
    10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 
    15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 
    20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 
    25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 
    30.5, 31.0, 31.5, 32.0, 32.5, 33.0, 





Arithmetic comparisons with a scalar or a matrix
-------------------------------------------------------------------------------


.. method:: mat.count(query, comparator)


    Returns the number of coefficients in matrix ?matA which are greater than the corresponding coefficients in matrix matB.

    Queries are: ">, <, >=, <=, !=, ==", For complex matrices, the absolute values are compared 


    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mpm.dps = 40;
        >>> A = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableA4x4", "")
        >>> B = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableB4x4", "")


