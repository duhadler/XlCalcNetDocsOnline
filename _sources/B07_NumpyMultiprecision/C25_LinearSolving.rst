




.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />










|newpage|


Standard decompositions and linear solving
=====================================================================================================


Returns the Cholesky decomposition of the symmetric matrix *matA* `=A = PLU`, without pivoting. Here *matA* is an instance of one of the above classes.

See also Eigen :cite:p:`EigenMat106`, Wikipedia :cite:p:`WikipediaMat106`, Wikipedia :cite:p:`WikipediaMat130`.



.. _rst_mpm_cholesky: 

Cholesky decomposition
---------------------------------------------------------------------------------

.. method:: ctx.cholesky(A, tol=None)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Cholesky decomposition of a symmetric positive-definite matrix `A`.
    Returns a lower triangular matrix `L` such that `A = L \times L^T`.
    More generally, for a complex Hermitian positive-definite matrix,
    a Cholesky decomposition satisfying `A = L \times L^H` is returned.

    The Cholesky decomposition can be used to solve linear equation
    systems twice as efficiently as LU decomposition, or to
    test whether `A` is positive-definite.

    The optional parameter ``tol`` determines the tolerance for
    verifying positive-definiteness.

    **Examples**

    Cholesky decomposition of a positive-definite symmetric matrix::

        >>> from mpmath import *
        >>> mp.dps = 25; mp.pretty = True
        >>> A = eye(3) + hilbert(3)
        >>> nprint(A)
        [     2.0      0.5  0.333333]
        [     0.5  1.33333      0.25]
        [0.333333     0.25       1.2]
        >>> L = cholesky(A)
        >>> nprint(L)
        [ 1.41421      0.0      0.0]
        [0.353553  1.09924      0.0]
        [0.235702  0.15162  1.05899]
        >>> chop(A - L*L.T)
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    Cholesky decomposition of a Hermitian matrix::

        >>> A = eye(3) + matrix([[0,0.25j,-0.5j],[-0.25j,0,0],[0.5j,0,0]])
        >>> L = cholesky(A)
        >>> nprint(L)
        [          1.0                0.0                0.0]
        [(0.0 - 0.25j)  (0.968246 + 0.0j)                0.0]
        [ (0.0 + 0.5j)  (0.129099 + 0.0j)  (0.856349 + 0.0j)]
        >>> chop(A - L*L.H)
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    Attempted Cholesky decomposition of a matrix that is not positive
    definite::

        >>> A = -eye(3) + hilbert(3)
        >>> L = cholesky(A)
        Traceback (most recent call last):
            ...
        ValueError: matrix is not positive-definite

    **References**

    1. Wikipedia: http://en.wikipedia.org/wiki/Cholesky_decomposition




.. _rst_mpm_cholesky_solve: 

Cholesky decomposition, solve
---------------------------------------------------------------------------------

.. method:: ctx.cholesky_solve(A, b, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Solves a symmetric positive-definite linear equation system.
    This is twice as efficient as lu_solve.


    Returns the LU decomposition of the general square matrix *matA* `= A = PLU`, with partial pivoting.

    See also Eigen :cite:p:`EigenMat107`, Wikipedia :cite:p:`WikipediaMat107`, Wikipedia :cite:p:`WikipediaMat130`.







.. _rst_mpm_lu: 

Matrix LU factorization
---------------------------------------------------------------------------------

.. method:: ctx.lu(A)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    A -> P, L, U

    LU factorisation of a square matrix A. L is the lower, U the upper part.
    P is the permutation matrix indicating the row swaps.

    P*A = L*U

    If you need efficiency, use the low-level method LU_decomp instead, it's
    much more memory efficient.


    The function ``lu`` computes an explicit LU factorization of a matrix::

        >>> P, L, U = lu(matrix([[0,2,3],[4,5,6],[7,8,9]]))
        >>> print(P)
        [0.0  0.0  1.0]
        [1.0  0.0  0.0]
        [0.0  1.0  0.0]
        >>> print(L)
        [              1.0                0.0  0.0]
        [              0.0                1.0  0.0]
        [0.571428571428571  0.214285714285714  1.0]
        >>> print(U)
        [7.0  8.0                9.0]
        [0.0  2.0                3.0]
        [0.0  0.0  0.214285714285714]
        >>> print(P.T*L*U)
        [0.0  2.0  3.0]
        [4.0  5.0  6.0]
        [7.0  8.0  9.0]




.. _rst_mpm_det: 

Determinant of a matrix, using LU decomposition
---------------------------------------------------------------------------------

.. method:: ctx.det(A)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Calculates the determinant of a matrix, using the LU factorization.



.. _rst_mpm_inverse: 

Inverse of a matrix, using the LU factorization
---------------------------------------------------------------------------------

.. method:: ctx.inverse(A, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Calculates the inverse of a matrix, using the LU factorization.

    If you want to solve an equation system Ax = b, it's recommended to use
    solve(A, b) instead, it's about 3 times more efficient.




.. _rst_mpm_lu_solve: 

Linear equations: LU solve
---------------------------------------------------------------------------------

.. method:: ctx.lu_solve(A, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Basic linear algebra is implemented; you can for example solve the linear
    equation system::

          x + 2*y = -10
        3*x + 4*y =  10

    using ``lu_solve``::

        >>> from mpmath import *
        >>> mp.pretty = False
        >>> A = matrix([[1, 2], [3, 4]])
        >>> b = matrix([-10, 10])
        >>> x = lu_solve(A, b)
        >>> x
        matrix(
        [['30.0'],
         ['-20.0']])




.. _rst_mpm_residual: 

Linear equations: residual of LU solve
---------------------------------------------------------------------------------

.. method:: ctx.residual(A, x, b, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Calculate the residual of a solution to a linear equation system.

    r = A*x - b for A*x = b

    If you don't trust the result, use ``residual`` to calculate the residual ||A*x-b||::

        >>> residual(A, x, b)
        matrix(
        [['3.46944695195361e-18'],
         ['3.46944695195361e-18']])
        >>> str(eps)
        '2.22044604925031e-16'

    As you can see, the solution is quite accurate. The error is caused by the
    inaccuracy of the internal floating point arithmetic. Though, it's even smaller
    than the current machine epsilon, which basically means you can trust the
    result.


    ``lu_solve`` accepts overdetermined systems. It is usually not possible to solve
    such systems, so the residual is minimized instead. Internally this is done
    using Cholesky decomposition to compute a least squares approximation. This means
    that ``lu_solve`` will square the errors. If you can't afford this, use
    ``qr_solve`` instead. It is twice as slow but more accurate, and it calculates
    the residual automatically.




??? LU improve solution
---------------------------------------------------------------------------------

.. method:: improve_solution(ctx, A, x, b, maxsteps=1)

    Improve a solution to a linear equation system iteratively.

    This re-uses the LU decomposition and is thus cheap.
    Usually 3 up to 4 iterations are giving the maximal improvement.






.. _rst_mpm_cond: 

mpmath: LU condition number
---------------------------------------------------------------------------------

.. method:: ctx.cond(A, norm=None)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Calculates the condition number of a matrix using a specified matrix norm.

    The condition number estimates the sensitivity of a matrix to errors.
    Example: small input errors for ill-conditioned coefficient matrices
    alter the solution of the system dramatically.

    For ill-conditioned matrices it's recommended to use qr_solve() instead
    of lu_solve(). This does not help with input errors however, it just avoids
    to add additional errors.

    Definition:    cond(A) = ||A|| * ||A**-1||



    Returns the QR decomposition of the symmetric matrix *matA* `=A = QR`, without pivoting.

    See also Eigen :cite:p:`EigenMat108`, Wikipedia :cite:p:`WikipediaMat121`, Wikipedia :cite:p:`WikipediaMat130`.






.. _rst_mpm_qr: 

QR factorization
---------------------------------------------------------------------------------

.. method:: ctx.qr(A, mode = 'full', edps = 10)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Compute a QR factorization $A = QR$ where
    A is an m x n matrix of real or complex numbers where m >= n

    mode has following meanings:
    (1) mode = 'raw' returns two matrixes (A, tau) in the internal format used by LAPACK
    (2) mode = 'skinny' returns the leading n columns of Q and n rows of R
    (3) Any other value returns the leading m columns of Q and m rows of R

    edps is the increase in mp precision used for calculations

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 15
        >>> mp.pretty = True
        >>> A = matrix([[1, 2], [3, 4], [1, 1]])
        >>> Q, R = qr(A)
        >>> Q
        [-0.301511344577764   0.861640436855329   0.408248290463863]
        [-0.904534033733291  -0.123091490979333  -0.408248290463863]
        [-0.301511344577764  -0.492365963917331   0.816496580927726]
        >>> R
        [-3.3166247903554  -4.52267016866645]
        [             0.0  0.738548945875996]
        [             0.0                0.0]
        >>> Q * R
        [1.0  2.0]
        [3.0  4.0]
        [1.0  1.0]
        >>> chop(Q.T * Q)
        [1.0  0.0  0.0]
        [0.0  1.0  0.0]
        [0.0  0.0  1.0]
        >>> B = matrix([[1+0j, 2-3j], [3+j, 4+5j]])
        >>> Q, R = qr(B)
        >>> nprint(Q)
        [     (-0.301511 + 0.0j)   (0.0695795 - 0.95092j)]
        [(-0.904534 - 0.301511j)  (-0.115966 + 0.278318j)]
        >>> nprint(R)
        [(-3.31662 + 0.0j)  (-5.72872 - 2.41209j)]
        [              0.0       (3.91965 + 0.0j)]
        >>> Q * R
        [(1.0 + 0.0j)  (2.0 - 3.0j)]
        [(3.0 + 1.0j)  (4.0 + 5.0j)]
        >>> chop(Q.T * Q.conjugate())
        [1.0  0.0]
        [0.0  1.0]




.. _rst_mpm_qr_solve: 

QR solve
---------------------------------------------------------------------------------

.. method:: ctx.qr_solve(A, b, norm=None, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Ax = b => x, ||Ax - b||

    Solve a determined or overdetermined linear equations system and
    calculate the norm of the residual (error).
    QR decomposition using Householder factorization is applied, which gives very
    accurate results even for ill-conditioned matrices. lu_solve is twice as
    efficient.




