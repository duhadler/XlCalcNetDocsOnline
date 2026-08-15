




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

Singular Value and Eigen decompositions
===============================================================================================


See: https://math.stackexchange.com/questions/1816364/the-svd-solution-to-linear-least-squares-linear-system-of-equations




Returns the SVD decomposition of a rectangular matrix.

See also Eigen :cite:p:`EigenMat109`, Wikipedia :cite:p:`WikipediaMat109`, Wikipedia :cite:p:`WikipediaMat130`.



.. _rst_mpm_svd_r: 

Real singular value decomposition of a matrix A
---------------------------------------------------------------------------------

.. method:: ctx.svd_r(A, full_matrices = False, compute_uv = True, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.



    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal matrices U and V are calculated such that

            A = U S V        and        U' U = 1         and         V V' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here ' denotes the transpose. The diagonal elements of S are the singular
    values of A, i.e. the positive square roots of the eigenvalues of A' A or A A'.

    input:

        A             : a real matrix of shape (m, n)

        full_matrices : if true, U and V are of shape (m, m) and (n, n).
                        if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).

        compute_uv    : if true, U and V are calculated. if false, only S is calculated.

        overwrite_a   : if true, allows modification of A which may improve
                        performance. if false, A is not modified.

    output:
        U : an orthogonal matrix: U' U = 1. if full_matrices is true, U is of
            shape (m, m). ortherwise it is of shape (m, min(m, n)).

        S : an array of length min(m, n) containing the singular values of A sorted by
            decreasing magnitude.

        V : an orthogonal matrix: V V' = 1. if full_matrices is true, V is of
            shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

    S          if compute_uv is false

    (U, S, V)      if compute_uv is true

    overview of the matrices:

        full_matrices true:

        A           : m*n

        U           : m*m     U' U  = 1

        S as matrix : m*n

        V           : n*n     V  V' = 1

        full_matrices false:

        A           : m*n

        U           : m*min(n,m)             U' U  = 1

        S as matrix : min(m,n)*min(m,n)

        V           : min(m,n)*n             V  V' = 1

    examples:

        >>> from mpmath import mp
        >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
        >>> S = mp.svd_r(A, compute_uv = False)
        >>> print(S)
        [6.0]
        [3.0]
        [1.0]

        >>> U, S, V = mp.svd_r(A)
        >>> print(mp.chop(A - U * mp.diag(S) * V))
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]


    see also: svd, svd_c




.. _rst_mpm_svd_c: 

Complex singular value decomposition of a matrix A
---------------------------------------------------------------------------------

.. method:: ctx.svd_c(A, full_matrices = False, compute_uv = True, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.


    This routine computes the singular value decomposition of a matrix A.
    Given A, two unitary matrices U and V are calculated such that

            A = U S V        and        U' U = 1         and         V V' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here ' denotes the hermitian transpose (i.e. transposition and complex
    conjugation). The diagonal elements of S are the singular values of A,
    i.e. the positive square roots of the eigenvalues of A' A or A A'.

    input:

        A             : a complex matrix of shape (m, n)

        full_matrices : if true, U and V are of shape (m, m) and (n, n).

                        if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).

        compute_uv    : if true, U and V are calculated. if false, only S is calculated.

        overwrite_a   : if true, allows modification of A which may improve
                        performance. if false, A is not modified.

    output:
        U : an unitary matrix: U' U = 1. if full_matrices is true, U is of
            shape (m, m). ortherwise it is of shape (m, min(m, n)).

        S : an array of length min(m, n) containing the singular values of A sorted by
            decreasing magnitude.

        V : an unitary matrix: V V' = 1. if full_matrices is true, V is of
            shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

    S          if compute_uv is false

    (U, S, V)      if compute_uv is true

    overview of the matrices:

        full_matrices true:

        A           : m*n

        U           : m*m     U' U  = 1

        S as matrix : m*n

        V           : n*n     V  V' = 1

        full_matrices false:

        A           : m*n

        U           : m*min(n,m)             U' U  = 1

        S as matrix : min(m,n)*min(m,n)

        V           : min(m,n)*n             V  V' = 1

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[-2j, -1-3j, -2+2j], [2-2j, -1-3j, 1], [-3+1j,-2j,0]])
        >>> S = mp.svd_c(A, compute_uv = False)
        >>> print(mp.chop(S - mp.matrix([mp.sqrt(34), mp.sqrt(15), mp.sqrt(6)])))
        [0.0]
        [0.0]
        [0.0]

        >>> U, S, V = mp.svd_c(A)
        >>> print(mp.chop(A - U * mp.diag(S) * V))
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    see also: svd, svd_r




.. _rst_mpm_svd: 


mpmath: Singular value decomposition of a matrix A (real or complex)
---------------------------------------------------------------------------------

.. method:: ctx.svd(A, full_matrices = False, compute_uv = True, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.


    "svd" is a unified interface for "svd_r" and "svd_c". Depending on
    whether A is real or complex the appropriate function is called.

    This routine computes the singular value decomposition of a matrix A.
    Given A, two orthogonal (A real) or unitary (A complex) matrices U and V
    are calculated such that

            A = U S V        and        U' U = 1         and         V V' = 1

    where S is a suitable shaped matrix whose off-diagonal elements are zero.
    Here ' denotes the hermitian transpose (i.e. transposition and complex
    conjugation). The diagonal elements of S are the singular values of A,
    i.e. the squareroots of the eigenvalues of A' A or A A'.

    input:

        A             : a real or complex matrix of shape (m, n)

        full_matrices : if true, U and V are of shape (m, m) and (n, n).  if false, U and V are of shape (m, min(m, n)) and (min(m, n), n).

        compute_uv    : if true, U and V are calculated. if false, only S is calculated.

        overwrite_a   : if true, allows modification of A which may improve  performance. if false, A is not modified.

    output:
        U : an orthogonal or unitary matrix: U' U = 1. if full_matrices is true, U is of
            shape (m, m). ortherwise it is of shape (m, min(m, n)).

        S : an array of length min(m, n) containing the singular values of A sorted by
            decreasing magnitude.

        V : an orthogonal or unitary matrix: V V' = 1. if full_matrices is true, V is of
            shape (n, n). ortherwise it is of shape (min(m, n), n).

    return value:

    S          if compute_uv is false

    (U, S, V)      if compute_uv is true

    overview of the matrices:

        full_matrices true:
        A           : m*n
        U           : m*m     U' U  = 1
        S as matrix : m*n
        V           : n*n     V  V' = 1

        full_matrices false:
        A           : m*n
        U           : m*min(n,m)             U' U  = 1
        S as matrix : min(m,n)*min(m,n)
        V           : min(m,n)*n             V  V' = 1

    examples:

        >>> from mpmath import mp
        >>> A = mp.matrix([[2, -2, -1], [3, 4, -2], [-2, -2, 0]])
        >>> S = mp.svd(A, compute_uv = False)
        >>> print(S)
        [6.0]
        [3.0]
        [1.0]

        >>> U, S, V = mp.svd(A)
        >>> print(mp.chop(A - U * mp.diag(S) * V))
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    see also: svd_r, svd_c










.. _rst_mpm_eigsy: 

Eigenvalue problem for a real symmetric square matrix A
---------------------------------------------------------------------------------

.. method:: ctx.eigsy(d, e, z = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.



    Returns the eigendecomposition of the symmetric/hermitian matrix *matA* `=A`.


    See also Eigen :cite:p:`EigenMat110`, Wikipedia :cite:p:`WikipediaMat112`, Wikipedia :cite:p:`WikipediaMat112a`, Wikipedia :cite:p:`WikipediaMat130`.



    This routine solves the (ordinary) eigenvalue problem for a real symmetric
    square matrix `A`. Given `A`, an orthogonal matrix `Q` is calculated which
    diagonalizes `A: Q' A Q = \text{diag}(E)` and   `Q Q^T = Q^T Q = 1`

    Here diag(`E`) is a diagonal matrix whose diagonal is `E`.

    The columns of `Q` are the eigenvectors of `A` and `E` contains the eigenvalues:

            ``A * Q[:,i] = E[i] * Q[:,i]``


    input:

    A: real matrix of format (n,n) which is symmetric (i.e. A=A' or A[i,j]=A[j,i])

    eigvals_only: if true, calculates only the eigenvalues E. if false, calculates both eigenvectors and eigenvalues.

    overwrite_a: if true, allows modification of A which may improve  performance. if false, A is not modified.

    output:

    E: vector of format (n). contains the eigenvalues of A in ascending order.

    Q: orthogonal matrix of format (n,n). contains the eigenvectors of A as columns.

    return value:

    E          if eigvals_only is true

    (E, Q)      if eigvals_only is false

    example:

        >>> from mpmath import mp
        >>> A = mp.matrix([[3, 2], [2, 0]])
        >>> E = mp.eigsy(A, eigvals_only = True)
        >>> print(E)
        [-1.0]
        [ 4.0]

        >>> A = mp.matrix([[1, 2], [2, 3]])
        >>> E, Q = mp.eigsy(A)
        >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
        [0.0]
        [0.0]

    see also: eighe, eigh, eig





.. _rst_mpm_eighe: 

Eigenvalue problem for a complex hermitian square matrix A
---------------------------------------------------------------------------------

.. method:: ctx.eighe(A, eigvals_only = False, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.


    This routine solves the (ordinary) eigenvalue problem for a complex
    hermitian square matrix A. Given A, an unitary matrix Q is calculated which
    diagonalizes A:

        Q' A Q = diag(E)               and                Q Q' = Q' Q = 1

    Here diag(E) a is diagonal matrix whose diagonal is E.
    ' denotes the hermitian transpose (i.e. ordinary transposition and
    complex conjugation).

    The columns of Q are the eigenvectors of A and E contains the eigenvalues:

        A Q[:,i] = E[i] Q[:,i]


    input:

        A: complex matrix of format (n,n) which is hermitian
            (i.e. A=A' or A[i,j]=conj(A[j,i]))

        eigvals_only: if true, calculates only the eigenvalues E.
                    if false, calculates both eigenvectors and eigenvalues.

        overwrite_a: if true, allows modification of A which may improve
                    performance. if false, A is not modified.

    output:

        E: vector of format (n). contains the eigenvalues of A in ascending order.

        Q: unitary matrix of format (n,n). contains the eigenvectors
            of A as columns.

    return value:

            E         if eigvals_only is true

            (E, Q)     if eigvals_only is false

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[1, -3 - 1j], [-3 + 1j, -2]])
        >>> E = mp.eighe(A, eigvals_only = True)
        >>> print(E)
        [-4.0]
        [ 3.0]

        >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
        >>> E, Q = mp.eighe(A)
        >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
        [0.0]
        [0.0]

    see also: eigsy, eigh, eig







.. _rst_mpm_eigh: 

mpmath: Eigenvalue problem for a selfadjoint square matrix A
---------------------------------------------------------------------------------

.. method:: ctx.eigh(A, eigvals_only = False, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.


    "eigh" is a unified interface for "eigsy" and "eighe". Depending on
    whether A is real or complex the appropriate function is called.

    This routine solves the (ordinary) eigenvalue problem for a real symmetric
    or complex hermitian square matrix A. Given A, an orthogonal (A real) or
    unitary (A complex) matrix Q is calculated which diagonalizes A:

        Q' A Q = diag(E)               and                Q Q' = Q' Q = 1

    Here diag(E) a is diagonal matrix whose diagonal is E.
    ' denotes the hermitian transpose (i.e. ordinary transposition and
    complex conjugation).

    The columns of Q are the eigenvectors of A and E contains the eigenvalues:

        A Q[:,i] = E[i] Q[:,i]

    input:

        A: a real or complex square matrix of format (n,n) which is symmetric
            (i.e. A[i,j]=A[j,i]) or hermitian (i.e. A[i,j]=conj(A[j,i])).

        eigvals_only: if true, calculates only the eigenvalues E.
                    if false, calculates both eigenvectors and eigenvalues.

        overwrite_a: if true, allows modification of A which may improve
                    performance. if false, A is not modified.

    output:

        E: vector of format (n). contains the eigenvalues of A in ascending order.

        Q: an orthogonal or unitary matrix of format (n,n). contains the
            eigenvectors of A as columns.

    return value:

            E         if eigvals_only is true

            (E, Q)     if eigvals_only is false

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[3, 2], [2, 0]])
        >>> E = mp.eigh(A, eigvals_only = True)
        >>> print(E)
        [-1.0]
        [ 4.0]

        >>> A = mp.matrix([[1, 2], [2, 3]])
        >>> E, Q = mp.eigh(A)
        >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
        [0.0]
        [0.0]

        >>> A = mp.matrix([[1, 2 + 5j], [2 - 5j, 3]])
        >>> E, Q = mp.eigh(A)
        >>> print(mp.chop(A * Q[:,0] - E[0] * Q[:,0]))
        [0.0]
        [0.0]

    see also: eigsy, eighe, eig









mpmath: tridiag_sym
---------------------------------------------------------------------------------

.. method:: r_sy_tridiag(ctx, A, D, E, calc_ev = True)

    This routine transforms a real symmetric matrix A to a real symmetric
    tridiagonal matrix `S` using an orthogonal similarity transformation:

    .. math ::   Q^T  A  Q = S  


    Returns the tridiagonal decomposition of a selfadjoint matrix.
    See also Eigen :cite:p:`EigenMat111`, Wikipedia :cite:p:`WikipediaMat111`, Wikipedia :cite:p:`WikipediaMat111a`, Wikipedia :cite:p:`WikipediaMat112a`, Wikipedia :cite:p:`WikipediaMat130`.


    The orthogonal matrix `Q` is build up from Householder reflectors.

    parameters:

      A: On input, A contains the real symmetric matrix of dimension `(n,n)`. On output, if calc_ev is true, A contains the orthogonal matrix Q, otherwise A is destroyed.

      D: Returns a real array of length `n`, containing the diagonal elements of the tridiagonal matrix.

      E: Returns a real array of length `n`, contains the offdiagonal elements of the tridiagonal matrix in ''E[0:(n-1)]'' where  ''n'' is the dimension of the matrix A. ''E[n-1]'' is undefined.

      calc_ev: If calc_ev is true, this routine explicitly calculates the orthogonal matrix Q which is then returned in A. If calc_ev is false, Q is not explicitly calculated resulting in a shorter run time.

    This routine is a python translation of the fortran routine tred2.f in the
    software library EISPACK (see netlib.org) which itself is based on the algol
    procedure tred2 described in:

    Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson

    Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also Stoer, Bulirsch - Introduction to Numerical Analysis.



mpmath tridiag_her
---------------------------------------------------------------------------------

.. method:: c_he_tridiag_0(ctx, A, D, E, S)

    This routine transforms a complex hermitian matrix A to a real symmetric
    tridiagonal matrix `S` using an unitary similarity transformation:

    .. math :: Q^H  A  Q = S

    where `Q^H` denotes the hermitian matrix transpose, i.e. transposition und conjugation.The unitary matrix Q 
    is build up from Householder reflectors and an unitary diagonal matrix.

    parameters:

        A: (input/output) On input, A contains the complex hermitian matrix of dimension (n,n). On output, A contains the unitary matrix `Q` in compressed form.

        D:  Returns a real array of length n, contains the diagonal elements of the tridiagonal matrix.

        E: Returns a real array of length n, contains the offdiagonal elements of the tridiagonal matrix in E[0:(n-1)] where is the dimension of  the matrix A. E[n-1] is undefined.

        S: Returns a  complex array of length n, contains a unitary diagonal matrix.

    This routine is a python translation (in slightly modified form) of the fortran
    routine htridi.f in the software library EISPACK (see netlib.org) which itself
    is a complex version of the algol procedure tred1 described in:

    Num. Math. 11, p.181-195 (1968) by Martin, Reinsch and Wilkonson
    Handbook for auto. comp., Vol II, Linear Algebra, p.212-226 (1971)

    For a good introduction to Householder reflections, see also  Stoer, Bulirsch - Introduction to Numerical Analysis.



mpmath: tridiag_eigen_sym
---------------------------------------------------------------------------------

.. method:: tridiag_eigen(ctx, d, e, z = False)

    This subroutine find the eigenvalues and the first components of the
    eigenvectors of a real symmetric tridiagonal matrix using the implicit
    QL method.

    parameters:

        d: (input/output) real array of length n. on input, d contains the diagonal
        elements of the input matrix. on output, d contains the eigenvalues in
        ascending order.

        e: (input) real array of length n. on input, e contains the offdiagonal
        elements of the input matrix in e[0:(n-1)]. On output, e has been
        destroyed.

        z: (input/output) If z is equal to False, no eigenvectors will be computed.
        Otherwise on input z should have the format z[0:m,0:n] (i.e. a real or
        complex matrix of dimension (m,n) ). On output this matrix will be
        multiplied by the matrix of the eigenvectors (i.e. the columns of this
        matrix are the eigenvectors): z --> z*EV
        That means if z[i,j]={1 if j==j; 0 otherwise} on input, then on output
        z will contain the first m components of the eigenvectors. That means
        if m is equal to n, the i-th eigenvector will be z[:,i].

    This routine is a python translation (in slightly modified form) of the
    fortran routine imtql2.f in the software library EISPACK (see netlib.org)
    which itself is based on the algol procudure imtql2 desribed in:

    num. math. 12, p. 377-383(1968) by matrin and wilkinson
    modified in num. math. 15, p. 450(1970) by dubrulle
    handbook for auto. comp., vol. II-linear algebra, p. 241-248 (1971)

    See also the routine gaussq.f in netlog.org or acm algorithm 726.














.. _rst_mpm_eig: 

Eigensystem decomposition of a matrix A (real or complex)
---------------------------------------------------------------------------------




Returns the eigendecomposition of a general square matrix *matA* `=A`.
See also Eigen :cite:p:`EigenMat112`, Wikipedia :cite:p:`WikipediaMat112`, Wikipedia :cite:p:`WikipediaMat112a`, Wikipedia :cite:p:`WikipediaMat130`.




.. method:: ctx.eig(A, left = False, right = True, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.


    This routine computes the eigenvalues and optionally the left and right
    eigenvectors of a square matrix A. Given A, a vector E and matrices ER
    and EL are calculated such that

    A ER[:,i] =         E[i] ER[:,i]

    EL[i,:] A         = EL[i,:] E[i]

    E contains the eigenvalues of A. The columns of ER contain the right eigenvectors
    of A whereas the rows of EL contain the left eigenvectors.


    input:
        A           : a real or complex square matrix of shape (n, n)
        left        : if true, the left eigenvectors are calulated.
        right       : if true, the right eigenvectors are calculated.
        overwrite_a : if true, allows modification of A which may improve performance. if false, A is not modified.

    output:
        E    : a list of length n containing the eigenvalues of A.
        ER   : a matrix whose columns contain the right eigenvectors of A.
        EL   : a matrix whose rows contain the left eigenvectors of A.

    return values:
        E            if left and right are both false.
        (E, ER)       if right is true and left is false.
        (E, EL)       if left is true and right is false.
        (E, EL, ER)   if left and right are true.


    examples:
        >>> from mpmath import mp
        >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
        >>> E, ER = mp.eig(A)
        >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
        [0.0]
        [0.0]
        [0.0]

        >>> E, EL, ER = mp.eig(A,left = True, right = True)
        >>> E, EL, ER = mp.eig_sort(E, EL, ER)
        >>> mp.nprint(E)
        [2.0, 4.0, 9.0]
        >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
        [0.0]
        [0.0]
        [0.0]
        >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
        [0.0  0.0  0.0]

    warning:
        - If there are multiple eigenvalues, the eigenvectors do not necessarily span the whole vectorspace, i.e. ER and EL may have not full rank. Furthermore in that case the eigenvectors are numerical ill-conditioned.
        - In the general case the eigenvalues have no natural order.

    see also:
        - eigh (or eigsy, eighe) for the symmetric eigenvalue problem.
        - eig_sort for sorting of eigenvalues and eigenvectors







.. _rst_mpm_eig_sort: 

Sorting Eigenvalues
---------------------------------------------------------------------------------

.. method:: ctx.eig_sort(E, EL = False, ER = False, f = "real")

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.



    This routine sorts the eigenvalues and eigenvectors delivered by ``eig``.

    parameters:

    E  : the eigenvalues as delivered by eig

    EL : the left  eigenvectors as delivered by eig, or false

    ER : the right eigenvectors as delivered by eig, or false

    f  : either a string (``real`` sort by increasing real part, ``imag`` sort by increasing imag part, ``abs`` sort by absolute value) or a function  mapping complexs to the reals, i.e. ``f = lambda x: -mp.re(x)`` would sort the eigenvalues by decreasing real part.

    return values:

    E            if EL and ER are both false.

    (E, ER)       if ER is not false and left is false.

    (E, EL)       if EL is not false and right is false.

    (E, EL, ER)   if EL and ER are not false.

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
        >>> E, EL, ER = mp.eig(A,left = True, right = True)
        >>> E, EL, ER = mp.eig_sort(E, EL, ER)
        >>> mp.nprint(E)
        [2.0, 4.0, 9.0]
        >>> E, EL, ER = mp.eig_sort(E, EL, ER,f = lambda x: -mp.re(x))
        >>> mp.nprint(E)
        [9.0, 4.0, 2.0]
        >>> print(mp.chop(A * ER[:,0] - E[0] * ER[:,0]))
        [0.0]
        [0.0]
        [0.0]
        >>> print(mp.chop( EL[0,:] * A - EL[0,:] * E[0]))
        [0.0  0.0  0.0]







.. _rst_mpm_hessenberg: 

mpmath: Hessenberg decomposition of a matrix A (real or complex)
---------------------------------------------------------------------------------

.. method:: ctx.hessenberg(A, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.




    Reduces a square matrix to Hessenberg form by an orthogonal similarity transformation.
    See also Eigen :cite:p:`EigenMat113`, Wikipedia :cite:p:`WikipediaMat113`, Wikipedia :cite:p:`WikipediaMat130`.



    This routine computes the Hessenberg decomposition of a square matrix A.
    Given A, an unitary matrix Q is determined such that

            Q' A Q = H                and               Q' Q = Q Q' = 1

    where H is an upper right Hessenberg matrix. Here ' denotes the hermitian
    transpose (i.e. transposition and conjugation).

    input:
        A            : a real or complex square matrix
        overwrite_a  : if true, allows modification of A which may improve performance. if false, A is not modified.

    output:
        Q : an unitary matrix
        H : an upper right Hessenberg matrix

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
        >>> Q, H = mp.hessenberg(A)
        >>> mp.nprint(H, 3) # doctest:+SKIP
        [  3.15  2.23  4.44]
        [-0.769  4.85  3.05]
        [   0.0  3.61   7.0]
        >>> print(mp.chop(A - Q * H * Q.transpose_conj()))
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    return value:   (Q, H)










.. _rst_mpm_schur: 

Schur decomposition of a matrix A (real or complex)
---------------------------------------------------------------------------------

.. method:: ctx.schur(A, overwrite_a = False)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``or ``gmp``.



    Performs a Schur decomposition of a square matrix.

    See also Eigen :cite:p:`EigenMat114`, Eigen :cite:p:`EigenMat115`, Wikipedia :cite:p:`WikipediaMat115`, Wikipedia :cite:p:`WikipediaMat130`.



    This routine computes the Schur decomposition of a square matrix A.
    Given A, an unitary matrix Q is determined such that

            Q' A Q = R                and               Q' Q = Q Q' = 1

    where R is an upper right triangular matrix. Here ' denotes the
    hermitian transpose (i.e. transposition and conjugation).

    input:
        A            : a real or complex square matrix
        overwrite_a  : if true, allows modification of A which may improve performance. if false, A is not modified.

    output:
        Q : an unitary matrix
        R : an upper right triangular matrix

    return value:   (Q, R)

    example:
        >>> from mpmath import mp
        >>> A = mp.matrix([[3, -1, 2], [2, 5, -5], [-2, -3, 7]])
        >>> Q, R = mp.schur(A)
        >>> mp.nprint(R, 3) # doctest:+SKIP
        [2.0  0.417  -2.53]
        [0.0    4.0  -4.74]
        [0.0    0.0    9.0]
        >>> print(mp.chop(A - Q * R * Q.transpose_conj()))
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]

    warning: The Schur decomposition is not unique.





