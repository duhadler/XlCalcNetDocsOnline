


.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






Flint/Functions for matrices
============================================================




Matrix multiplication: special options for FMPQ, ARB, ACB
-------------------------------------------------------------------------------

.. method:: ArbMatTimes(C, A, B)

   Sets res to the matrix product of mat1 and mat2. The operands must have compatible dimensions for matrix multiplication.

See also: :cite:t:`Johansson2018`, :cite:t:`Johansson2019`.


**Options FMPZ**


FMPZ: This function automatically switches between classical and multimodular multiplication, based on a heuristic comparison of the dimensions and entry sizes.



fmpz_mat_mul_classical(C, A, B)

Sets C to the matrix product C = AB computed using classical matrix algorithm.
The matrices must have compatible dimensions for matrix multiplication. No aliasing is
allowed.



fmpz_mat_mul_strassen(C, A, B)

Sets C = AB. Dimensions must be compatible for matrix multiplication. C is not
allowed to be aliased with A or B. Uses Strassen multiplication (the Strassen-Winograd
variant).


fmpz_mat_mul_multi_mod(C, A, B)

Sets C to the matrix product C = AB computed using a multimodular algorithm. C
is computed modulo several small prime numbers and reconstructed using the Chinese
Remainder Theorem. This generally becomes more efficient than classical multiplication
for large matrices.

The bits parameter is a bound for the bit size of largest element of C, or twice the
absolute value of the largest element if any elements of C are negative. The function
fmpz_mat_mul_multi_mod calculates a rigorous bound automatically. If the default
bound is too pessimistic, _fmpz_mat_mul_multi_mod can be used with a custom bound.
The matrices must have compatible dimensions for matrix multiplication. No aliasing is
allowed.


fmpz_mat_sqr(C, A, B)

Sets B to the square of the matrix A, which must be a square matrix. Aliasing is allowed.
The function calls fmpz_mat_mul for dimensions less than 12 and calls fmpz_mat_sqr_bodrato
for cases in which the latter is faster.


fmpz_mat_sqr_bodrato(C, A, B)

Sets B to the square of the matrix A, which must be a square matrix. Aliasing is allowed.
The bodrato algorithm is described in [6]. It is highly efficient for squaring matrices
which satisfy both the following conditions : (a) large elements (b) dimensions less than
150.



**Options FMPQ**


Sets C to the matrix product AB, computed by clearing denominators and multiplying over the integers.
Same options as FMPZ.



**Options Arb**


arb_mat_mul_classical(C, A, B)

The classical version performs matrix multiplication in the trivial way.


arb_mat_mul_block(C, A, B)

The block version decomposes the input matrices into one or several blocks of uniformly
scaled matrices and multiplies large blocks via fmpz_mat_mul. It also invokes
_arb_mat_addmul_rad_mag_fast() for the radius matrix multiplications.


arb_mat_mul_threaded(C, A, B)

The threaded version performs classical multiplication but splits the computation over the number
of threads returned by flint_get_num_threads().




**Options ACB**


acb_mat_mul_classical(C, A, B)

The classical version performs matrix multiplication in the trivial way.



acb_mat_mul_threaded(C, A, B)

The threaded version performs classical multiplication but splits the computation over the number
of threads returned by flint_get_num_threads().


acb_mat_mul_reorder(C, A, B)

The reorder version reorders the data and performs one to four real matrix multiplications via
arb_mat_mul() .





|newpage|


Determinant (incl. special options for FMPQ, ARB, ACB)
-------------------------------------------------------------------------------

.. method:: mat.Det()

   returns the determinant of the matrix `A`.

See also:  Wikipedia :cite:p:`WikipediaMat102`.



Sets det to the determinant of the square matrix A. The matrix of dimension `0 \times 0` is defined to have determinant 1.
   
FMPZ: This function automatically chooses between fmpz_mat_det_cofactor, fmpz_mat_det_bareiss, fmpz_mat_det_modular and fmpz_mat_det_modular_accelerated (with proved = 1), depending on the size of the matrix and its entries.

The default version automatically selects between the lu and precond versions and additionally handles small or triangular matrices by direct formulas.



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

    >>> print(A.eigen_det())
    48772174.207998




**Options FMPZ**


fmpz_mat_det_cofactor(det, A)

Sets det to the determinant of the square matrix A computed using direct cofactor
expansion. This function only supports matrices up to size `4 \times 4`.


fmpz_mat_det_bareiss(det, A)

Sets det to the determinant of the square matrix A computed using the Bareiss algorithm.
A copy of the input matrix is row reduced using fraction-free Gaussian elimination,
and the determinant is read of from the last element on the main diagonal.


fmpz_mat_det_modular(det, A, proved=1)

Sets det to the determinant of the square matrix A (if proved = 1), or a probabilistic
value for the determinant (proved = 0), computed using a multimodular algorithm.
The determinant is computed modulo several small primes and reconstructed using the
Chinese Remainder Theorem. With proved = 1, sufficiently many primes are chosen
to satisfy the bound computed by fmpz_mat_det_bound. With proved = 0, the determinant
is considered determined if it remains unchanged modulo several consecutive
primes (currently if their product exceeds `2^100`).



fmpz_mat_det_modular_accelerated(det, A, proved=1)

Sets det to the determinant of the square matrix A (if proved = 1), or a probabilistic
value for the determinant (proved = 0), computed using a multimodular algorithm.
This function uses the same basic algorithm as fmpz_mat_det_modular, but instead
of computing det(A) directly, it generates a divisor d of det(A) and then computes
x = det(A)=d modulo several small primes not dividing d. This typically accelerates the
computation by requiring fewer primes for large matrices, since d with high probability
will be nearly as large as the determinant. This trick is described in [1].




**Options FMPQ**


Sets det to the determinant of mat. In the general case, the determinant is computed by clearing denominators and computing a determinant over the integers. Matrices of size 0, 1 or 2 are handled directly.
Same options as FMPZ.



**Options Arb**


Sets det to the determinant of the matrix A. The default version automatically selects between the lu and precond versions and additionally handles small or triangular matrices by direct formulas.

arb_mat_det_lu(A)

The lu version uses Gaussian elimination with partial pivoting. If at some point an invertible pivot
element cannot be found, the elimination is stopped and the magnitude of the determinant of the
remaining submatrix is bounded using Hadamard's inequality.

arb_mat_det_precond(A)

The precond version computes an approximate LU factorization of A and multiplies by the inverse
L and U matrices as preconditioners to obtain a matrix close to the identity matrix :cite:t:`Rump2010`.
An enclosure for this determinant is computed using Gershgorin circles. This is about four times
slower than direct Gaussian elimination, but much more numerically stable.





**Options ACB**


acb_mat_det_lu(A)

The lu version uses Gaussian elimination with partial pivoting. If at some point an invertible pivot
element cannot be found, the elimination is stopped and the magnitude of the determinant of the
remaining submatrix is bounded using Hadamard's inequality.

acb_mat_det_precond(A)

The precond version computes an approximate LU factorization of A and multiplies by the inverse
L and U matrices as preconditioners to obtain a matrix close to the identity matrix :cite:t:`Rump2010`.
An enclosure for this determinant is computed using Gershgorin circles. This is about four times
slower than direct Gaussian elimination, but much more numerically stable.



*Example: hilbert_matrix.c*


Given an input integer *n*, this program accurately computes the
determinant of the *n* by *n* Hilbert matrix.
Hilbert matrices are notoriously ill-conditioned: although the
entries are close to unit magnitude, the determinant `h_n`
decreases superexponentially (nearly as `1/4^{n^2}`) as
a function of *n*.
This program automatically doubles the working precision
until the ball computed for `h_n` by :func:`arb_mat_det`
does not contain zero.

Sample output::

    $ build/examples/hilbert_matrix 200
    prec=20: [+/- 1.32e-335]
    prec=40: [+/- 1.63e-545]
    prec=80: [+/- 1.30e-933]
    prec=160: [+/- 3.62e-1926]
    prec=320: [+/- 1.81e-4129]
    prec=640: [+/- 3.84e-8838]
    prec=1280: [2.955454297e-23924 +/- 8.29e-23935]
    success!
    cpu/wall(s): 8.494 8.513
    virt/peak/res/peak(MB): 134.98 134.98 111.57 111.57

Called with ``-eig n``, instead of computing the determinant,
the program computes the smallest eigenvalue of the Hilbert matrix
(in fact, it isolates all eigenvalues and prints the smallest eigenvalue)::

    $ build/examples/hilbert_matrix -eig 50
    prec=20: nan
    prec=40: nan
    prec=80: nan
    prec=160: nan
    prec=320: nan
    prec=640: [1.459157797e-74 +/- 2.49e-84]
    success!
    cpu/wall(s): 1.84 1.841
    virt/peak/res/peak(MB): 33.97 33.97 10.51 10.51









|newpage|

Inverse (incl. special options for FMPQ, ARB, ACB)
-------------------------------------------------------------------------------

.. method:: mat.Inverse()

   returns the inverse of the matrix `A`.

    See also:  Wikipedia :cite:p:`WikipediaMat104`.




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




**FMPZ: Options**

Sets (Ainv, den) to the inverse matrix of A. Returns 1 if A is nonsingular and 0 if A is singular. Aliasing of Ainv and A is allowed. The denominator is not guaranteed to be minimal, but is guaranteed to be a divisor of the determinant of A. This function uses a direct formula for matrices of size two or less, and otherwise solves for the identity matrix using fraction-free LU decomposition.



**FMPQ: Options**

Sets B to the inverse matrix of A and returns nonzero. Returns zero if A is singular. A must be a square matrix.




**Options**

If `A` cannot be inverted numerically (indicating either that `A` is singular or that the precision is insufficient), the values in the output matrix are left undefined and zero is returned. A nonzero return value guarantees that the matrix is invertible and that the exact inverse is contained in the output.


arb_mat_inverse_lu(X, A, B)

The lu version performs LU decomposition directly in ball arithmetic. This is fast, but the
bounds typically blow up exponentially with n, even if the system is well-conditioned. This
algorithm is usually the best choice at very high precision.

arb_mat_inverse_precond(X, A, B)

The precond version computes an approximate inverse to precondition the system :cite:t:`HS1967`.
This is usually several times slower than direct LU decomposition, but the bounds do not
blow up with n if the system is well-conditioned. This algorithm is usually the best choice for
large systems at low to moderate precision.



**Options**

If `A` cannot be inverted numerically (indicating either that `A` is singular or that the precision is insufficient), the values in the output matrix are left undefined and zero is returned. A nonzero return value guarantees that the matrix is invertible and that the exact inverse is contained in the output.


acb_mat_inverse_lu(X, A, B)

The lu version performs LU decomposition directly in ball arithmetic. This is fast, but the
bounds typically blow up exponentially with n, even if the system is well-conditioned. This
algorithm is usually the best choice at very high precision.

acb_mat_inverse_precond(X, A, B)

The precond version computes an approximate inverse to precondition the system :cite:t:`HS1967`.
This is usually several times slower than direct LU decomposition, but the bounds do not
blow up with n if the system is well-conditioned. This algorithm is usually the best choice for
large systems at low to moderate precision.








|newpage|

Solve (incl. special options for FMPQ, ARB, ACB)
-------------------------------------------------------------------------------

.. method:: mat.Solve(B)

   returns a solution x to the equation Ax=b.

See also:  Wikipedia :cite:p:`WikipediaMat105`.

The parameter b is the right-hand-side of the equation to solve. Can be a vector or a matrix, the only requirement in order for the equation to make sense is that b.rows()==A.rows().

This method just tries to find as good a solution as possible. If you want to check whether a solution exists or if it is accurate, just call this function to get a result and then compute the error of this result, or use 


This method avoids dividing by zero, so that the non-existence of a solution doesn't by itself mean that you'll get inf or nan values. If there exists more than one solution, this method will arbitrarily choose one. If you need a complete analysis of the space of solutions, take the one solution obtained by this method and add to it elements of the kernel, as determined by kernel().



.. method:: mat.ArbSolve(matB)

    Solves `AX = B` given a nonsingular square matrix A and a matrix B of compatible dimensions

    Returns a solution `x` to the equation `Ax=b`.


    See also  Wikipedia :cite:p:`WikipediaMat105`.


The parameter `b` is the right-hand-side of the equation to solve. Can be a vector or a matrix, the only requirement in order for the equation to make sense is that b.rows()==A.rows().

This method just tries to find as good a solution as possible. If you want to check whether a solution exists or if it is accurate, just call this function to get a result and then compute the error of this result, or use 

MatrixBase::isApprox() directly, for instance like this:

bool a_solution_exists = (A*result).isApprox(b, precision); 

This method avoids dividing by zero, so that the non-existence of a solution doesn't by itself mean that you'll get inf or nan values. If there exists more than one solution, this method will arbitrarily choose one. If you need a complete analysis of the space of solutions, take the one solution obtained by this method and add to it elements of the kernel, as determined by kernel().


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

    >>> # This is the same as A^-1 * B = A.solve(B)
    >>> X = A.lu_solve(B); mp14.setdps(5); X.show("X"); mp14.setdps(15)
    X: 
     21.65,  21.67,  21.69,  21.72,  21.74,  21.76, 
     8.210,  8.216,  8.222,  8.228,  8.234,  8.240, 
    -20.54, -20.56, -20.58, -20.60, -20.62, -20.64, 
    -15.32, -15.34, -15.36, -15.39, -15.41, -15.43, 
     16.93,  16.94,  16.96,  16.97,  16.98,  16.99, 
     8.733,  8.756,  8.778,  8.801,  8.824,  8.847, 

    >>> B2 = A * X; mp14.setdps(5); B2.show("B2"); mp14.setdps(15)
    B2: 
    911.0, 912.0, 913.0, 914.0, 915.0, 916.0, 
    921.0, 922.0, 923.0, 924.0, 925.0, 926.0, 
    931.0, 932.0, 933.0, 934.0, 935.0, 936.0, 
    941.0, 942.0, 943.0, 944.0, 945.0, 946.0, 
    951.0, 952.0, 953.0, 954.0, 955.0, 956.0, 
    961.0, 962.0, 963.0, 964.0, 965.0, 966.0, 




**FMPZ: Options**


The following functions allow solving matrix-matrix equations AX = B where the system matrix A is square and has full rank. The solving is implicitly done over the field of rational numbers: except where otherwise noted, an integer matrix X and a separate denominator d (den) are computed such that `A(X/d) = b`, equivalently such that `A X =bd` holds over the integers.

No guarantee is made that the numerators and denominator are reduced to lowest terms, but the denominator is always guaranteed to be a divisor of the determinant of A. If A is singular, den will be set to zero and the elements of the solution vector or matrix will have undefined values. No aliasing is allowed between arguments.


.. method:: mat.FmpzSolve(X, den, A, B)

   Solves the equation `AX = B` for nonsingular `A`. More precisely, computes (X, den) such that `AX = B \times den`. Returns 1 if A is nonsingular and 0 if A is singular. The computed denominator will not generally be minimal. This function uses Cramer's rule for small systems and fraction-free LU decomposition followed by fraction-free forward and back substitution for larger systems. Note that for very large systems, it is faster to compute a modular solution using fmpz_mat_solve_dixon.


.. method:: mat.FmpzSolveFflu(X, den, A, B)

    Solves the equation AX = B for nonsingular A. More precisely, computes (X, den) such that `AX = B \times den`. Returns 1 if A is nonsingular and 0 if A is singular. The computed denominator will not generally be minimal. Uses fraction-free LU decomposition followed by fraction-free forward and back substitution.



.. method:: mat.FmpzSolveCramer(X, den, A, B)

    Solves the equation AX = B for nonsingular A. More precisely, computes (X, den) such that `AX = B \times den`. Returns 1 if A is nonsingular and 0 if A is singular. Uses Cramer's rule. Only systems of size up to `3 \times 3` are allowed.



.. method:: mat.FmpzSolveDixon(X, den, A, B)

    Solves `AX = B` given a nonsingular square matrix A and a matrix B of compatible dimensions, using a modular algorithm. In particular, Dixon's p-adic lifting algorithm is used (currently a non-adaptive version). This is generally the preferred method for large dimensions.

    More precisely, this function computes an integer `M` and an integer matrix `X` such that `AX = B \mod M` and such that all the reduced numerators and denominators of the elements `x = p/q` in the full solution satisfy `2|p|q \le M`. As such, the explicit rational solution matrix can be recovered uniquely by passing the output of this function to fmpq_mat_set_fmpz_mat_mod.

    A nonzero value is returned if A is nonsingular. If A is singular, zero is returned and the values of the output variables will be undefined. Aliasing between input and output matrices is allowed.





**FMPQ: Options**

Solves `AX = B` for nonsingular A by clearing denominators and solving the rescaled system over the integers using a fraction-free algorithm. This is usually the fastest algorithm for small systems. Returns nonzero if `X` is nonsingular or if the right hand side is empty, and zero otherwise.


fmpq_mat_solve_fraction_free(X, A, B)

Solves AX = B for nonsingular A by clearing denominators and solving the rescaled system
over the integers using Dixon's algorithm. The rational solution matrix is generated using
rational reconstruction. This is usually the fastest algorithm for large systems. Returns
nonzero if X is nonsingular or if the right hand side is empty, and zero otherwise.

fmpq_mat_solve_fmpz_mat(X, A, B)

Solves AX = B for integer matrices A and B with A nonsingular by choosing between
fmpz_mat_solve and fmpz_mat_solve_dixon and restoring the solution X from the
output of these functions. Returns nonzero if X is nonsingular or if the right hand side
is empty, and zero otherwise.




**Options**

The default version selects between lu and precomp automatically.

arb_mat_solve_lu(X, A, B)

The lu version performs LU decomposition directly in ball arithmetic. This is fast, but the
bounds typically blow up exponentially with n, even if the system is well-conditioned. This
algorithm is usually the best choice at very high precision.

arb_mat_solve_precond(X, A, B)

The precond version computes an approximate inverse to precondition the system :cite:t:`HS1967`.
This is usually several times slower than direct LU decomposition, but the bounds do not
blow up with n if the system is well-conditioned. This algorithm is usually the best choice for
large systems at low to moderate precision.




**Options**

The default version selects between lu and precomp automatically.

acb_mat_solve_lu(X, A, B)

The lu version performs LU decomposition directly in ball arithmetic. This is fast, but the
bounds typically blow up exponentially with n, even if the system is well-conditioned. This
algorithm is usually the best choice at very high precision.

acb_mat_solve_precond(X, A, B)

The precond version computes an approximate inverse to precondition the system :cite:t:`HS1967`.
This is usually several times slower than direct LU decomposition, but the bounds do not
blow up with n if the system is well-conditioned. This algorithm is usually the best choice for
large systems at low to moderate precision.






.. _rst_arb_expm: 

Matrix Exponential
------------------------------------------------------------------------------------------------------------

.. method:: mat.ApcExpm()

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat141`.

    Computes the matrix exponential of a square matrix `A`, which is defined by the power series  `\displaystyle  \exp(A) = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \ldots`



    Basic examples::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> expm(zeros(3))
        [1.0  0.0  0.0]
        [0.0  1.0  0.0]
        [0.0  0.0  1.0]
        >>> expm(eye(3))
        [2.71828182845905               0.0               0.0]
        [             0.0  2.71828182845905               0.0]
        [             0.0               0.0  2.71828182845905]
        >>> expm([[1,1,0],[1,0,1],[0,1,0]])
        [ 3.86814500615414  2.26812870852145  0.841130841230196]
        [ 2.26812870852145  2.44114713886289   1.42699786729125]
        [0.841130841230196  1.42699786729125    1.6000162976327]
        >>> expm([[1,1,0],[1,0,1],[0,1,0]], method='pade')
        [ 3.86814500615414  2.26812870852145  0.841130841230196]
        [ 2.26812870852145  2.44114713886289   1.42699786729125]
        [0.841130841230196  1.42699786729125    1.6000162976327]
        >>> expm([[1+j, 0], [1+j,1]])
        [(1.46869393991589 + 2.28735528717884j)                        0.0]
        [  (1.03776739863568 + 3.536943175722j)  (2.71828182845905 + 0.0j)]

    Matrices with large entries are allowed::

        >>> expm(matrix([[1,2],[2,3]])**25)
        [5.65024064048415e+2050488462815550  9.14228140091932e+2050488462815550]
        [9.14228140091932e+2050488462815550  1.47925220414035e+2050488462815551]

    The identity `\exp(A+B) = \exp(A) \exp(B)` does not hold for
    noncommuting matrices::

        >>> A = hilbert(3)
        >>> B = A + eye(3)
        >>> chop(mnorm(A*B - B*A))
        0.0
        >>> chop(mnorm(expm(A+B) - expm(A)*expm(B)))
        0.0
        >>> B = A + ones(3)
        >>> mnorm(A*B - B*A)
        1.8
        >>> mnorm(expm(A+B) - expm(A)*expm(B))
        42.0927851137247





|newpage|


.. _rst_arb_sinm: 

Matrix Sine
------------------------------------------------------------------------------------------------------------

.. method:: mat.ApcSinm()


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.


    Calculates the sine function of the matrix.


    The cosine of a square matrix `A` is defined in analogy with the matrix exponential.


    .. math ::     \cos(A) =  \frac{e^{iA} + e^{-iA}}{2}


    .. math ::     \sin(A) =  \frac{e^{iA} - e^{-iA}}{2i}


    .. math ::     \cos^2(A) + \sin^2(A) =  I

    For real `A`, we can write `\cos(A) = \Re ( e^{iA} )` and `\sin(A) = \Im ( e^{iA} )`.


    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}


    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}






|newpage|


.. _rst_arb_cosm: 


Matrix Cosine
------------------------------------------------------------------------------------------------------------


.. method:: mat.ApcCosm()


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.


    Calculates the cosine function of the matrix.

    The cosine of a square matrix `A` is defined in analogy with the matrix exponential.


    .. math ::     \cos(A) =  \frac{e^{iA} + e^{-iA}}{2}


    .. math ::     \sin(A) =  \frac{e^{iA} - e^{-iA}}{2i}


    .. math ::     \cos^2(A) + \sin^2(A) =  I

    For real `A`, we can write `\cos(A) = \Re ( e^{iA} )` and `\sin(A) = \Im ( e^{iA} )`.


    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}


    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}





|newpage|


.. _rst_arb_sinhm: 

Matrix Hyperbolic Sine
------------------------------------------------------------------------------------------------------------

.. method:: mat.ApcSinhm()


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.


    Calculates the hyperbolic sine function of the matrix.



    The hyperbolic sine of a square matrix `A` is defined in analogy with the matrix exponential.


    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}


    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}


    .. math ::     \cosh^2(A) + \sinh^2(A) =  I





|newpage|


.. _rst_arb_coshm: 

Matrix Hyperbolic Cosine
------------------------------------------------------------------------------------------------------------


.. method:: mat.ApcCoshm()


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.


    Calculates the hyperbolic cosine function of the matrix.


    The hyperbolic cosine of a square matrix `A` is defined in analogy with the matrix exponential.


    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}


    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}


    .. math ::     \cosh^2(A) + \sinh^2(A) =  I







Characteristic polynomial
-------------------------------------------------------------------------------

.. method:: mat.ApcCharpoly(cp, A)

   Sets cp to the characteristic polynomial of length `n + 1` of  of `A` which must be a an `n \times n` square matrix.



See also: Johansson (2020).



**FMPZ: Options**


fmpz_mat_charpoly_berkowitz(cp, A)

Computes the characteristic polynomial of length `n+1` of an `n \times n` square matrix. Uses
an `O(n^4)` algorithm based on the method of Berkowitz.


fmpz_mat_charpoly_modular(cp, A)

Computes the characteristic polynomial of length n+1 of an `n \times n` square matrix. Uses
a modular method based on an `O(n^3)`, worst case `O(n^4)` method over `\mathbb{Z}=n\mathbb{Z}`.



**FMPQ: Options**


Set cp to the characteristic polynomial of the given `n \times n` matrix. If `A` is not square, an exception is raised.




**Options**

Employs a division-free algorithm using `O(n^4)` operations.



**Options**


Employs a division-free algorithm using `O(n^4)` operations.







|newpage|

Calculating eigenvalues via characteristic polynomials
-------------------------------------------------------------------------------



.. method::mat.ApcEigenvaluesViaCp(evals, matA, flags)

    The eigenvalues of matrix matA are determined by calculating the characteristic polynomial cp of matA, folllowed by finding the roots of cp.






**Examples**

.. code-block:: vbnet
    
    Sub DemoArbCharPoly()
        Console.WriteLine("Hello DemoArbCharPoly!")
        mp4.setdps(40)        
        Dim digits As Int32 = 5        
        Dim n = 4
        
        Dim matA = arbmatClass.random(n, n)
        matA.Print("Input matrix A: ", digits)        
        
        Dim polyA1 = apm.arb_mat_charpoly(matA)
        polyA1.print("Coefficients of characteristic polynomial:  ")
        
        
        Dim polyA = acb.poly_t(polyA1)
        polyA.print("polyA = acb.poly_t(polyA1): ")
        
        Dim roots = polyA.find_roots()
        roots.print("Roots:  ")
        
        Dim polyD = polyA.evaluate_vec_iter(roots, n)
        polyD.print("polyD = polyA.evaluate_vec_iter(roots, n): ")
    End Sub



.. code-block:: none
    
    Hello DemoArbCharPoly!

    Coefficients of characteristic polynomial:  from within
    0: [0.0004290477699032390004736549330908684056378 +/- 1.16e-39]
    1: [0.1814289677116147743258392370857230215306 +/- 5.01e-40]
    2: [0.01886322926891042893463352416522124196556 +/- 1.83e-42]
    3: [-1.746330149235511317029612143869599094614 +/- 3.87e-40]
    4: 1.000000000000000000000000000000000000000

    polyA = acb.poly_t(polyA1): from within
    0: ([0.0004290477699032390004736549330908684056378 +/- 1.16e-39], 0)
    1: ([0.1814289677116147743258392370857230215306 +/- 5.01e-40], 0)
    2: ([0.01886322926891042893463352416522124196556 +/- 1.83e-42], 0)
    3: ([-1.746330149235511317029612143869599094614 +/- 3.87e-40], 0)
    4: (1.000000000000000000000000000000000000000, 0)

    Roots:  from within
    0: ([1.669878413241797800236331773781105705837 +/- 2.26e-39], [+/- 1.99e-39])
    1: ([-0.002365534438538074439744022733356414276159 +/- 2.56e-38], [+/- 2.56e-38])
    2: ([-0.2925077245552650276472984861466489488210 +/- 1.41e-38], [+/- 1.41e-38])
    3: ([0.3713249949875166188803228789684987518743 +/- 1.70e-38], [+/- 1.70e-38])

    polyD = polyA.evaluate_vec_iter(roots, n): from within
    0: ([-8.416759096120581254796289369072552250922e-41 +/- 1.21e-38], [+/- 1.01e-38])
    1: ([+/- 5.80e-39], [+/- 4.64e-39])
    2: ([-1.134491236717371900619851470631516099885e-41 +/- 6.67e-39], [+/- 5.35e-39])
    3: ([6.367500221891968770277427226469378900538e-42 +/- 8.56e-39], [+/- 7.20e-39])
    4: (0, 0)










Eigenvalue enclosure (Rump)
-------------------------------------------------------------------------------

.. method:: mat.ApcEigEnclosureRump(Lambda0, matR0)


    Given an *n* by *n* matrix  *A* and an approximate eigenvalue-eigenvector pair *lambda_approx* and *R_approx* (where *R_approx* is an *n* by 1 matrix), computes an enclosure *lambda* guaranteed to contain at least one of the eigenvalues of *A*, along with an enclosure *R* for a corresponding right eigenvector.

    More generally, this function can handle clustered (or repeated) eigenvalues. If *R_approx* is an *n* by *k* matrix containing approximate eigenvectors for a presumed cluster of *k* eigenvalues near *lambda_approx*, this function computes an enclosure *lambda* guaranteed to contain at least *k* eigenvalues of *A* along with a matrix *R* guaranteed to contain a basis for the *k*-dimensional invariant subspace associated with these eigenvalues. Note that for multiple eigenvalues, determining the individual eigenvectors is an ill-posed problem; describing an enclosure of the invariant subspace is the best we can hope for.

    For `k = 1`, it is guaranteed that `AR - R \lambda` contains the zero matrix. For `k > 2`, this cannot generally be guaranteed (in particular, *A* might not diagonalizable). In this case, we can still compute an approximately diagonal *k* by *k* interval matrix `J \approx \lambda I` such that `AR - RJ` is guaranteed to contain the zero matrix. This matrix has the property that the Jordan canonical form of (any exact matrix contained in) *A* has a *k* by *k* submatrix equal to the Jordan canonical form of (some exact matrix contained in) *J*. The output *J* is optional (the user can pass *NULL* to omit it).

    The algorithm follows section 13.4 in :cite:t:`Rump2010`, corresponding to the ``verifyeig()`` routine in INTLAB.
    No assumptions are made about the structure of *A* or the quality of the given approximations.


    See also: :cite:t:`Johansson2018a`.



    .. code-block:: vbnet
    
        Sub DemoArbEigEnclosureRump()
            Console.WriteLine("Hello DemoArbEigEnclosureRump!")
            mp4.setdps(40)        
            Dim digits As Int32 = 5        
            Dim n = 4
        
            Dim matA = arbmatClass.random(n, n)
            matA.Print("Input matrix A: ", digits)        
        
            Dim polyA1 = apm.arb_mat_charpoly(matA)
            polyA1.print("Coefficients of characteristic polynomial:  ")
        
        
            Dim polyA = acb.poly_t(polyA1)
            polyA.print("polyA = acb.poly_t(polyA1): ")
        
            Dim roots = polyA.find_roots()
            roots.print("Roots:  ")
        
            Dim polyD = polyA.evaluate_vec_iter(roots, n)
            polyD.print("polyD = polyA.evaluate_vec_iter(roots, n): ")
        End Sub



Eigenvalues, step by setp
-------------------------------------------------------------------------------

.. method:: mat.ApcEigSimple(matE0, matR0)

    Computes all the eigenvalues (and optionally corresponding eigenvectors) of the given *n* by *n* matrix *A*.

    Attempts to prove that *A* has *n* simple (isolated) eigenvalues, returning 1 if successful and 0 otherwise. On success, isolating complex intervals for the eigenvalues are written to the vector *E*, in no particular order. If *L* is not *NULL*, enclosures of the corresponding left eigenvectors are written to the rows of *L*. If *R* is not *NULL*, enclosures of the corresponding right eigenvectors are written to the columns of *R*.

    The left eigenvectors are normalized so that `L = R^{-1}`. This produces a diagonalization `LAR = D` where *D* is the diagonal matrix with the entries in *E* on the diagonal.

    The user supplies approximations *E_approx* and *R_approx* of the eigenvalues and the right eigenvectors. No assumptions are made about the structure of *A* or the quality of the given approximations.

    Two algorithms are implemented:

    * The *rump* version calls :func:`acb_mat_eig_enclosure_rump` repeatedly to certify eigenvalue-eigenvector pairs one by one. The iteration is stopped to return non-success if a new eigenvalue overlaps with previously computed one. Finally, *L* is computed by a matrix inversion. This has complexity `O(n^4)`.

    * The *vdhoeven_mourrain* version uses the algorithm in [vanderHoeven2017` to certify all eigenvalues and eigenvectors in one step. This has complexity `O(n^3)`.

    The default version currently uses *vdhoeven_mourrain*.

    By design, these functions terminate instead of attempting to compute eigenvalue clusters if some eigenvalues cannot be isolated. To compute all eigenvalues of a matrix allowing for overlap,
    :func:`acb_mat_eig_multiple_rump` may be used as a fallback, or :func:`acb_mat_eig_multiple` may be used in the first place.


    .. code-block:: vbnet
    
        Sub DemoArbEigSimple()
            Console.WriteLine("Hello DemoArbEigSimple!")
            mp4.setdps(40)        
            Dim digits As Int32 = 5        
            Dim n = 4
        
            Dim matA = arbmatClass.random(n, n)
            matA.Print("Input matrix A: ", digits)        
        
            Dim polyA1 = apm.arb_mat_charpoly(matA)
            polyA1.print("Coefficients of characteristic polynomial:  ")
        
        
            Dim polyA = acb.poly_t(polyA1)
            polyA.print("polyA = acb.poly_t(polyA1): ")
        
            Dim roots = polyA.find_roots()
            roots.print("Roots:  ")
        
            Dim polyD = polyA.evaluate_vec_iter(roots, n)
            polyD.print("polyD = polyA.evaluate_vec_iter(roots, n): ")
        End Sub



Eigenvalues, multiple
-------------------------------------------------------------------------------

.. method:: mat.ApcEigMultiple(matE0, matR0)

    Computes all the eigenvalues of the given *n* by *n* matrix *A*. On success, the output vector *E* contains *n* complex intervals, each representing one eigenvalue of *A* with the correct multiplicities in case of overlap. The output intervals are either disjoint or identical, and identical intervals are guaranteed to be grouped consecutively. Each complete run of *k* identical intervals thus represents a cluster of exactly *k* eigenvalues which could not be separated from each other at the current precision, but which could be isolated from the other `n - k` eigenvalues of the matrix.

    The user supplies approximations *E_approx* and *R_approx* of the eigenvalues and the right eigenvectors. No assumptions are made about the structure of *A* or the quality of the given approximations.

    The *rump* algorithm groups approximate eigenvalues that are close and calls :func:`acb_mat_eig_enclosure_rump` repeatedly to validate each cluster. The complexity is `O(m n^3)` for *m* clusters.

    The default version, as currently implemented, first attempts to call :func:`acb_mat_eig_simple_vdhoeven_mourrain` hoping that the eigenvalues are actually simple. It then uses the *rump* algorithm as a fallback.



    .. code-block:: vbnet
    
        Sub DemoArbEigMultiple()
            Console.WriteLine("Hello DemoArbEigMultiple!")
            mp4.setdps(40)        
            Dim digits As Int32 = 5        
            Dim n = 4
        
            Dim matA = arbmatClass.random(n, n)
            matA.Print("Input matrix A: ", digits)        
        
            Dim polyA1 = apm.arb_mat_charpoly(matA)
            polyA1.print("Coefficients of characteristic polynomial:  ")
        
        
            Dim polyA = acb.poly_t(polyA1)
            polyA.print("polyA = acb.poly_t(polyA1): ")
        
            Dim roots = polyA.find_roots()
            roots.print("Roots:  ")
        
            Dim polyD = polyA.evaluate_vec_iter(roots, n)
            polyD.print("polyD = polyA.evaluate_vec_iter(roots, n): ")
        End Sub



    

