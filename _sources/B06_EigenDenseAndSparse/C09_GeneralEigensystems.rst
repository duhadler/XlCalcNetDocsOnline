

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Eigen decompositions of general square matrices
===============================================================================


Matrix balancing and eigenvalue/eigenvector computation
---------------------------------------------------------------

Diagonal scaling to improve eigenvalue accuracy

See also: :cite:t:`James2014`.


Example from Matlab: https://de.mathworks.com/help/matlab/ref/balance.html



Sample code for Eigen in C++ : https://stackoverflow.com/questions/43151853/eigen-balancing-matrix-for-eigenvalue



.. code-block:: cpp

    void balance_matrix(const Eigen::MatrixXd &A, Eigen::MatrixXd &Aprime, Eigen::MatrixXd &D) {
        // https://arxiv.org/pdf/1401.5766.pdf (Algorithm #3)
        const int p = 2;
        double beta = 2; // Radix base (2?)
        Aprime = A;
        D = Eigen::MatrixXd::Identity(A.rows(), A.cols());
        bool converged = false;
        do {
            converged = true;
            for (Eigen::Index i = 0; i < A.rows(); ++i) {
                double c = Aprime.col(i).lpNorm<p>();
                double r = Aprime.row(i).lpNorm<p>();
                double s = pow(c, p) + pow(r, p);
                double f = 1;
                while (c < r / beta) {
                    c *= beta;
                    r /= beta;
                    f *= beta;
                }
                while (c >= r*beta) {
                    c /= beta;
                    r *= beta;
                    f /= beta;
                }
                if (pow(c, p) + pow(r, p) < 0.95*s) {
                    converged = false;
                    D(i, i) *= f;
                    Aprime.col(i) *= f;
                    Aprime.row(i) /= f;
                }
            }
        } while (!converged);
    }








|newpage|


Hessenberg Decomposition
-----------------------------------


.. method:: mat.Hessenberg(Query)


    Reduces a square matrix to Hessenberg form by an orthogonal similarity transformation.

    See also Eigen :cite:p:`EigenMat113`,  Wikipedia :cite:p:`WikipediaMat113`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.



**Results:**


:H:     A square matrix of the same type and dimension as `A`, containing the matrix `H` in the decomposition `A = QHQ^T`.

:Q:     A square matrix of the same type and dimension as `A`, containing the matrix `Q` in the decomposition `A = QHQ^T`.

:packedMatrix:     A square matrix of the same type and dimension as `A`. Returns the internal representation of the decomposition. 

:hcoeff:     A square matrix of the same type and dimension as `A`. Returns the Householder coefficients of the decomposition. 


Reduces a square matrix to Hessenberg form by an orthogonal similarity transformation.

In the real case, the Hessenberg decomposition consists of an orthogonal matrix `Q` and a Hessenberg matrix `H`
such that `A = Q H Q^T =  Q^T H Q`. An orthogonal matrix is a matrix whose inverse equals its transpose: `Q^{-1} = Q^T.`, and `Q Q^T =  Q^T Q = I` 

The Hessenberg decomposition of a complex matrix is `A = Q H Q^*` with `Q` unitary, that is, `Q^{-1} = Q^*`, and `Q Q^* =  Q^* Q = I` .

A Hessenberg matrix has zeros below the subdiagonal, so it is almost upper triangular.





Example for a real matrix
.......................................


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

    >>> Query = "H, Q, Hcoeff, Packed"
    >>> Res = A.eigen_hessenberg2(Query)

    >>> Res["H"].show("H")
    H: 
       48, -59.6, -10.3,  10.5,  12.3, -5.09, 
    -59.7,  96.1,  35.2, -1.55, -7.54, -10.7, 
        0,  94.1,  26.9,  6.92, -19.6, -27.1, 
        0,     0, -24.9, -7.98,  45.0,  9.81, 
        0,     0,     0, -3.83,  2.49,  9.07, 
        0,     0,     0,     0, -1.38, -2.76, 

    >>> Res["Q"].show("Q")
    Q: 
    1,      0,      0,       0,      0,      0, 
    0, -0.770,  0.524, -0.0577,  0.320,  0.162, 
    0, -0.452, -0.161,   0.398, -0.417, -0.662, 
    0, -0.119, -0.490,  -0.337,  0.671, -0.426, 
    0, -0.385, -0.439,  -0.575, -0.473,  0.322, 
    0, -0.201, -0.516,   0.628,  0.220,  0.501, 

    >>> Res["Hcoeff"].show("Hcoeff")
    Hcoeff: 
    1.77, 
    1.29, 
    1.50, 
    1.75, 
       0, 

    >>> Res["Packed"].show("Packed")
    Packed: 
        48, -59.6,  -10.3,   10.5,  12.3, -5.09, 
     -59.7,  96.1,   35.2,  -1.55, -7.54, -10.7, 
     0.255,  94.1,   26.9,   6.92, -19.6, -27.1, 
    0.0671, 0.406,  -24.9,  -7.98,  45.0,  9.81, 
     0.218, 0.427,  0.492,  -3.83,  2.49,  9.07, 
     0.113, 0.444, -0.301, -0.378, -1.38, -2.76, 




Example for a complex matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(5,5); A.show("A")
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 5.00 + 14.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 7.00 + 3.30j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 9.00 + 23.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 43.0 + 33.0j, 
    23.0 + 43.0j, 15.0 + 11.0j, 28.0 + 19.0j, 35.0 + 32.0j, 41.0 + 14.0j, 

    >>> Query = "H, Q, Hcoeff, Packed"
    >>> Res = A.eigen_hessenberg2(Query)

    >>> Res["H"].show("H")
    H: 
    45.0 + 7.50j, 18.1 - 51.3j, -17.5 + 4.87j, -25.8 + 10.1j,  18.1 + 13.2j, 
      -86.1 + 0j, 92.5 + 84.4j,  14.6 - 49.3j,  4.03 - 10.0j, -2.00 - 20.7j, 
          0 + 0j,   -64.4 + 0j,  34.6 + 3.78j,  18.8 - 10.4j,  15.2 - 24.8j, 
          0 + 0j,       0 + 0j,    -33.0 + 0j,  19.9 + 19.9j,  3.46 + 20.3j, 
          0 + 0j,       0 + 0j,        0 + 0j,     17.5 + 0j, 0.963 - 25.1j, 

    >>> Res["Q"].show("Q")
    Q: 
    1.00 + 0j,          0 + 0j,           0 + 0j,           0 + 0j,           0 + 0j, 
       0 + 0j, -0.151 - 0.337j,   0.179 + 0.305j,   0.728 + 0.398j,   0.129 + 0.183j, 
       0 + 0j, -0.372 - 0.105j,  -0.617 + 0.545j, -0.0540 - 0.336j,  -0.105 + 0.213j, 
       0 + 0j, -0.395 - 0.488j, -0.0150 - 0.157j,  -0.364 + 0.107j,   0.636 - 0.181j, 
       0 + 0j, -0.267 - 0.499j,  0.413 + 0.0291j, -0.213 - 0.0808j, -0.668 - 0.0986j, 

    >>> Res["Hcoeff"].show("Hcoeff")
    Hcoeff: 
    1.15 - 0.337j, 
    1.68 + 0.447j, 
    1.66 - 0.249j, 
    1.96 - 0.286j, 

    >>> Res["Packed"].show("Packed")
    Packed: 
        45.0 + 7.50j,      18.1 - 51.3j,  -17.5 + 4.87j, -25.8 + 10.1j,  18.1 + 13.2j, 
          -86.1 + 0j,      92.5 + 84.4j,   14.6 - 49.3j,  4.03 - 10.0j, -2.00 - 20.7j, 
    0.322 - 0.00339j,        -64.4 + 0j,   34.6 + 3.78j,  18.8 - 10.4j,  15.2 - 24.8j, 
      0.430 + 0.298j,  -0.0503 + 0.190j,     -33.0 + 0j,  19.9 + 19.9j,  3.46 + 20.3j, 
      0.331 + 0.337j, -0.274 + 0.00564j, 0.288 + 0.308j,     17.5 + 0j, 0.963 - 25.1j, 








|newpage|


Schur Decomposition
---------------------------------

.. method:: mat.Schur(Query)


    Performs a Schur decomposition of a square matrix.

    See also Eigen :cite:p:`EigenMat114`, Eigen :cite:p:`EigenMat115`,  Wikipedia :cite:p:`WikipediaMat115`,  Wikipedia :cite:p:`WikipediaMat130`.




**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**

:U:     A general matrix of the same type and dimension as `A`, containing the matrix `U` in the decomposition.

:T:     A general matrix of the same type and dimension as `A`, containing the matrix `T` in the decomposition.


REAL:

Given a real square matrix `A`, this class computes the real Schur decomposition: `A = UTU^T` where `U` is a real orthogonal matrix and `T` is a real quasi-triangular matrix. An orthogonal matrix is a matrix whose inverse is equal to its transpose, `U^{-1} = U^T.` A quasi-triangular matrix is a block-triangular matrix whose diagonal consists of 1-by-1 blocks and 2-by-2 blocks with complex eigenvalues. The eigenvalues of the blocks on the diagonal of T are the same as the eigenvalues of the matrix A, and thus the real Schur decomposition is used in EigenSolver to compute the eigendecomposition of a matrix.

COMPLEX:

Given a real or complex square matrix `A`, this class computes the Schur decomposition:  where `U` is a unitary complex matrix, and `T` is a complex upper triangular matrix. The diagonal of the matrix T corresponds to the eigenvalues of the matrix `A`.




Example for a real matrix
.......................................


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

    >>> Query = "U, T"
    >>> Res = A.eigen_schur2(Query)

    >>> Res["U"].show("U")
    U: 
    0.448, -0.245,   0.546,  -0.582, -0.317, 0.0355, 
    0.283,  0.578,   0.572,   0.481, 0.0718,  0.147, 
    0.442,  0.344,  -0.230,  -0.241,  0.328, -0.684, 
    0.312, -0.358, -0.0980,   0.565, -0.534, -0.400, 
    0.463, -0.512, -0.0393,   0.209,  0.631,  0.283, 
    0.460,  0.310,  -0.557, -0.0919, -0.323,  0.519, 

    >>> Res["T"].show("T")
    T: 
    158,  27.1,  34.3,   32.5, -0.516,  19.6, 
      0, -20.8, -3.79, -0.982,  -31.1,  2.71, 
      0,     0,  21.2,  -47.3,   1.06, -21.6, 
      0,     0,     0,  -5.80,   25.8,  6.25, 
      0,     0,     0,  -13.8,   12.4, -9.59, 
      0,     0,     0,      0,      0, -2.45, 





Example for a complex matrix
.......................................


.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", "")
    >>> A = A.top_left_corner(5,5); A.show("A")
    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 5.00 + 14.0j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 7.00 + 3.30j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 9.00 + 23.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 43.0 + 33.0j, 
    23.0 + 43.0j, 15.0 + 11.0j, 28.0 + 19.0j, 35.0 + 32.0j, 41.0 + 14.0j, 

    >>> Query = "U, T"
    >>> Res = A.eigen_schur2(Query)

    >>> Res["U"].show("U")
    U: 
     0.338 + 0.106j, -0.0858 - 0.301j,   0.235 - 0.292j, -0.271 - 0.686j, -0.0756 - 0.294j, 
     0.409 + 0.152j,  -0.572 + 0.142j,  -0.532 + 0.134j, 0.357 - 0.0924j,  0.0672 - 0.142j, 
    0.522 + 0.0826j, -0.0964 + 0.376j,   0.507 - 0.348j,  0.129 + 0.234j,  0.0787 + 0.338j, 
     0.443 + 0.121j,   0.286 - 0.234j,  -0.153 + 0.362j, -0.381 + 0.116j,   0.559 + 0.165j, 
    0.438 + 0.0389j,   0.464 - 0.229j, -0.149 + 0.0612j,  0.210 + 0.215j, -0.644 - 0.0920j, 

    >>> Res["T"].show("T")
    T: 
    125 + 131j, 6.55 - 27.8j, -1.71 - 17.5j,  4.81 - 19.6j,  14.2 + 15.8j, 
        0 + 0j, 43.0 + 29.8j, 0.609 + 17.6j,  13.8 - 10.4j, -5.47 - 18.4j, 
        0 + 0j,       0 + 0j,  10.5 - 45.0j, -11.8 - 20.4j, -5.32 + 18.9j, 
        0 + 0j,       0 + 0j,        0 + 0j,  21.7 - 13.7j,  4.33 + 21.6j, 
        0 + 0j,       0 + 0j,        0 + 0j,        0 + 0j, -7.36 - 11.2j, 






|newpage|


Eigensystem of a general square matrix: only eigenvalues
--------------------------------------------------------------------

.. method:: mat.Eigenvalues(Query)


    Returns the eigendecomposition of a general square matrix *matA* `=A`.

    See also Eigen :cite:p:`EigenMat112`,  Wikipedia :cite:p:`WikipediaMat112`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.



**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.




Computes eigenvalues and eigenvectors of general matrices.
The eigenvalues and eigenvectors of a matrix `A` are scalars `\lambda` and vectors `v` such that `Av = \lambda v`. If `D` is a diagonal matrix with the eigenvalues on the diagonal, and `V` is a matrix with the eigenvectors as its columns, then `AV = V D` . The matrix `V` is almost always invertible, in which case we have `A = V DV^{-1}`. This is called the eigendecomposition. The eigenvalues and eigenvectors of a matrix may be complex, even when the matrix is real. However, we can choose real matrices `V` and `D` satisfying `AV = V D`, just like the eigendecomposition, if the matrix `D` is not required to be diagonal, but if it is allowed to have blocks of the form


.. math::   \begin{bmatrix} 
                \mathbf{u} & \mathbf{v} \\ 
                \mathbf{-v} & \mathbf{u} 
            \end{bmatrix} 


(where `u` and `v` are real numbers) on the diagonal. These blocks correspond to complex eigenvalue pairs `u \pm iv`. We call this variant of the eigendecomposition the pseudo-eigendecomposition.

Call the function compute() to compute the eigenvalues and eigenvectors of a given matrix. Alternatively, you
can use the EigenSolver(const MatrixType, bool) constructor which computes the eigenvalues and eigenvectors at
construction time. Once the eigenvalue and eigenvectors are computed, they can be retrieved with the eigenvalues()
and eigenvectors() functions. The pseudoEigenvalueMatrix() and pseudoEigenvectors() methods allow the
construction of the pseudo-eigendecomposition.

The matrix is first reduced to real Schur form using the RealSchur (or Complex) class. The Schur decomposition is then used
to compute the eigenvalues and eigenvectors. The cost of the computation is dominated by the cost of the Schur
decomposition, which is very approximately 25n3 (where n is the size of the matrix) if computeEigenvectors is
true, and 10n3 if computeEigenvectors is false. This method reuses of the allocated data in the EigenSolver object.





Example for a real matrix: only eigenvalues
.....................................................


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

    >>> Query = "Eval"
    >>> Res = A.eigen_EigenValues2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i          L[i]  
    0:     158 + 0j, 
    1:   -20.8 + 0j, 
    2:    21.2 + 0j, 
    3: 3.32 + 16.6j, 
    4: 3.32 - 16.6j, 
    5:   -2.45 + 0j, 

    >>> X = A.cplx(); #X.show("X")
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
    i          L[i]      Det(A - I * L[i])  
    0:     158 + 0j,        -5.37E-23 + 0j, 
    1:   -20.8 + 0j,         7.82E-26 + 0j, 
    2:    21.2 + 0j,        -5.20E-26 + 0j, 
    3: 3.32 + 16.6j, -3.07E-26 - 3.37E-26j, 
    4: 3.32 - 16.6j, -3.07E-26 + 3.37E-26j, 
    5:   -2.45 + 0j,         2.78E-28 + 0j, 



Example for a complex matrix: only eigenvalues
.....................................................



.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.dcf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecCplxTableB6x6", ""); A.show("A")

    A: 
    45.0 + 7.50j, 2.90 + 36.0j, 11.0 + 13.0j, 37.0 + 37.0j, 5.00 + 14.0j, 13.0 + 5.00j, 
    13.0 + 29.0j, 38.0 + 41.0j, 22.0 + 44.0j, 28.0 + 20.0j, 7.00 + 3.30j, 35.0 + 25.0j, 
    32.0 + 9.00j, 42.0 + 49.0j, 47.0 + 11.0j, 32.0 + 49.0j, 9.00 + 23.0j, 5.50 + 35.0j, 
    34.0 + 42.0j, 6.00 + 16.0j, 20.0 + 38.0j, 22.0 + 17.0j, 43.0 + 33.0j, 24.0 + 19.0j, 
    23.0 + 43.0j, 15.0 + 11.0j, 28.0 + 19.0j, 35.0 + 32.0j, 41.0 + 14.0j, 5.00 + 48.0j, 
    33.0 + 49.0j, 42.0 + 48.0j, 47.0 + 32.0j, 34.0 + 25.0j, 46.0 + 31.0j, 4.70 + 23.0j, 

    >>> Query = "Eval"
    >>> Res = A.eigen_EigenSystem2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i            L[i]  
    0: -21.5 + 0.565j, 
    1:   28.1 + 2.54j, 
    2:  -11.3 - 39.2j, 
    3:   9.68 - 43.2j, 
    4:   42.2 + 28.5j, 
    5:     150 + 164j, 

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
    i            L[i]      Det(A - I * L[i])  
    0: -21.5 + 0.565j,  8.89E-26 - 9.48E-26j, 
    1:   28.1 + 2.54j, -4.38E-27 + 1.28E-25j, 
    2:  -11.3 - 39.2j,  1.02E-25 - 3.06E-25j, 
    3:   9.68 - 43.2j, -2.96E-25 - 6.70E-25j, 
    4:   42.2 + 28.5j,  1.62E-24 - 1.31E-24j, 
    5:     150 + 164j,  2.79E-21 - 1.17E-21j, 




|newpage|


Eigensystem of a general square matrix: eigenvalues and eigenvectors
----------------------------------------------------------------------------------

.. method:: mat.Eigensystem(Query)


    Returns the eigendecomposition of a general square matrix *matA* `=A`.

    See also Eigen :cite:p:`EigenMat112`,  Wikipedia :cite:p:`WikipediaMat112`,  Wikipedia :cite:p:`WikipediaMat112a`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.



**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.



Example for a real matrix: eigenvalues and eigenvectors
.................................................................


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

    >>> Query = "Eval, Evec"
    >>> Res = A.eigen_EigenSystem2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i          L[i]  
    0:     158 + 0j, 
    1:   -20.8 + 0j, 
    2:    21.2 + 0j, 
    3: 3.32 + 16.6j, 
    4: 3.32 - 16.6j, 
    5:   -2.45 + 0j, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
            V0           V1            V2                V3                V4            V5  
    0.448 + 0j, -0.309 + 0j,   0.450 + 0j, -0.0287 + 0.197j, -0.0287 - 0.197j, -0.0395 + 0j, 
    0.283 + 0j,  0.529 + 0j,   0.440 + 0j,   0.136 + 0.299j,   0.136 - 0.299j,  -0.192 + 0j, 
    0.442 + 0j,  0.274 + 0j,  -0.353 + 0j,  -0.260 - 0.288j,  -0.260 + 0.288j,  0.0958 + 0j, 
    0.312 + 0j, -0.401 + 0j,  -0.134 + 0j,  0.245 - 0.0527j,  0.245 + 0.0527j,  -0.451 + 0j, 
    0.463 + 0j, -0.576 + 0j, -0.0979 + 0j,   0.168 + 0.281j,   0.168 - 0.281j,  -0.274 + 0j, 
    0.460 + 0j,  0.238 + 0j,  -0.671 + 0j,  -0.282 - 0.672j,  -0.282 + 0.672j,   0.821 + 0j, 

    >>> AC = A.cplx()
    >>> CheckResult = (AC - V * L.D * V.eigen_inverse()).norm().real
    >>> print("||A - V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
        ||A - V * diag(L) * V^-1|| (should be zero):  4.22E-33

    >>> X = A.cplx(); #X.show("X")
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
    i          L[i]      Det(A - I * L[i])  
    0:     158 + 0j,        -5.37E-23 + 0j, 
    1:   -20.8 + 0j,         7.82E-26 + 0j, 
    2:    21.2 + 0j,        -5.20E-26 + 0j, 
    3: 3.32 + 16.6j, -3.07E-26 - 3.37E-26j, 
    4: 3.32 - 16.6j, -3.07E-26 + 3.37E-26j, 
    5:   -2.45 + 0j,         2.78E-28 + 0j, 


    >>> for i in range(V.rows):
    >>>     AV = AC * V.col(i); VL = V.col(i) * L[i]; X = AV - VL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(VL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - VL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "VL = " + Vi + " * " + Li, "AV - VL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  158 + 0j
    Checking the properties of eigenvector V0 (AV - VL should be a zero vector): 
    Eigenvector V0  AV = A * V0  VL = V0 * L[0]         AV - VL  
        0.448 + 0j,   70.8 + 0j,      70.8 + 0j,  1.60E-33 + 0j, 
        0.283 + 0j,   44.8 + 0j,      44.8 + 0j,         0 + 0j, 
        0.442 + 0j,   70.0 + 0j,      70.0 + 0j, -1.00E-34 + 0j, 
        0.312 + 0j,   49.4 + 0j,      49.4 + 0j,  2.00E-34 + 0j, 
        0.463 + 0j,   73.2 + 0j,      73.2 + 0j,  1.00E-34 + 0j, 
        0.460 + 0j,   72.7 + 0j,      72.7 + 0j, -5.00E-34 + 0j, 

    Eigenvalue L[1]:  -20.8 + 0j
    Checking the properties of eigenvector V1 (AV - VL should be a zero vector): 
    Eigenvector V1  AV = A * V1  VL = V1 * L[1]         AV - VL  
       -0.309 + 0j,   6.42 + 0j,      6.42 + 0j, -1.80E-34 + 0j, 
        0.529 + 0j,  -11.0 + 0j,     -11.0 + 0j,  6.00E-34 + 0j, 
        0.274 + 0j,  -5.69 + 0j,     -5.69 + 0j, -6.00E-35 + 0j, 
       -0.401 + 0j,   8.33 + 0j,      8.33 + 0j, -1.00E-34 + 0j, 
       -0.576 + 0j,   12.0 + 0j,      12.0 + 0j, -2.00E-34 + 0j, 
        0.238 + 0j,  -4.94 + 0j,     -4.94 + 0j, -5.70E-34 + 0j, 

    Eigenvalue L[2]:  21.2 + 0j
    Checking the properties of eigenvector V2 (AV - VL should be a zero vector): 
    Eigenvector V2  AV = A * V2  VL = V2 * L[2]         AV - VL  
        0.450 + 0j,   9.56 + 0j,      9.56 + 0j,  4.00E-35 + 0j, 
        0.440 + 0j,   9.35 + 0j,      9.35 + 0j, -7.00E-35 + 0j, 
       -0.353 + 0j,  -7.50 + 0j,     -7.50 + 0j,  4.70E-34 + 0j, 
       -0.134 + 0j,  -2.85 + 0j,     -2.85 + 0j,  1.90E-34 + 0j, 
      -0.0979 + 0j,  -2.08 + 0j,     -2.08 + 0j,  2.10E-34 + 0j, 
       -0.671 + 0j,  -14.3 + 0j,     -14.3 + 0j,  6.00E-34 + 0j, 

    Eigenvalue L[3]:  3.32 + 16.6j
    Checking the properties of eigenvector V3 (AV - VL should be a zero vector): 
      Eigenvector V3     AV = A * V3  VL = V3 * L[3]               AV - VL  
    -0.0287 + 0.197j, -3.35 + 0.178j, -3.35 + 0.178j, 5.10E-34 + 2.10E-34j, 
      0.136 + 0.299j,  -4.50 + 3.25j,  -4.50 + 3.25j, 5.40E-34 + 2.20E-34j, 
     -0.260 - 0.288j,   3.91 - 5.27j,   3.91 - 5.27j, 5.70E-34 + 3.60E-34j, 
     0.245 - 0.0527j,   1.69 + 3.88j,   1.69 + 3.88j, 5.00E-35 + 2.00E-34j, 
      0.168 + 0.281j,  -4.11 + 3.72j,  -4.11 + 3.72j, 3.30E-34 + 4.30E-34j, 
     -0.282 - 0.672j,   10.2 - 6.91j,   10.2 - 6.91j, 4.00E-34 + 5.10E-34j, 

    Eigenvalue L[4]:  3.32 - 16.6j
    Checking the properties of eigenvector V4 (AV - VL should be a zero vector): 
      Eigenvector V4     AV = A * V4  VL = V4 * L[4]               AV - VL  
    -0.0287 - 0.197j, -3.35 - 0.178j, -3.35 - 0.178j, 5.10E-34 - 2.10E-34j, 
      0.136 - 0.299j,  -4.50 - 3.25j,  -4.50 - 3.25j, 5.40E-34 - 2.20E-34j, 
     -0.260 + 0.288j,   3.91 + 5.27j,   3.91 + 5.27j, 5.70E-34 - 3.60E-34j, 
     0.245 + 0.0527j,   1.69 - 3.88j,   1.69 - 3.88j, 5.00E-35 - 2.00E-34j, 
      0.168 - 0.281j,  -4.11 - 3.72j,  -4.11 - 3.72j, 3.30E-34 - 4.30E-34j, 
     -0.282 + 0.672j,   10.2 + 6.91j,   10.2 + 6.91j, 4.00E-34 - 5.10E-34j, 

    Eigenvalue L[5]:  -2.45 + 0j
    Checking the properties of eigenvector V5 (AV - VL should be a zero vector): 
    Eigenvector V5  AV = A * V5  VL = V5 * L[5]         AV - VL  
      -0.0395 + 0j, 0.0969 + 0j,    0.0969 + 0j, -4.84E-34 + 0j, 
       -0.192 + 0j,  0.471 + 0j,     0.471 + 0j, -6.40E-34 + 0j, 
       0.0958 + 0j, -0.235 + 0j,    -0.235 + 0j, -6.15E-34 + 0j, 
       -0.451 + 0j,   1.10 + 0j,      1.10 + 0j, -2.00E-34 + 0j, 
       -0.274 + 0j,  0.671 + 0j,     0.671 + 0j, -2.59E-34 + 0j, 
        0.821 + 0j,  -2.01 + 0j,     -2.01 + 0j, -5.50E-34 + 0j, 





Example for a complex matrix: eigenvalues and eigenvectors
..................................................................



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

    >>> Query = "Eval, Evec"
    >>> Res = A.eigen_EigenSystem2(Query)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i           L[i]  
    0: 4.21 - 0.418j, 
    1:  39.6 + 8.06j, 
    2:  3.46 - 47.6j, 
    3:    105 + 116j, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
                  V0               V1                V2              V3  
    -0.0249 + 0.483j, -0.589 - 0.212j, -0.319 + 0.0888j, 0.165 + 0.359j, 
     0.0587 + 0.501j,  0.346 + 0.299j,   0.326 + 0.144j, 0.208 + 0.513j, 
    0.00311 - 0.567j, 0.484 + 0.0474j, -0.645 - 0.0595j, 0.358 + 0.473j, 
    -0.0210 - 0.435j, -0.148 - 0.374j,   0.534 - 0.242j, 0.154 + 0.402j, 

    >>> AC = +A
    >>> CheckResult = (AC - V * L.D * V.eigen_inverse()).norm().real
    >>> print("||A - V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - V * diag(L) * V^-1|| (should be zero):  2.59E-33

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
    i           L[i]     Det(A - I * L[i])  
    0: 4.21 - 0.418j, 6.96E-29 - 3.88E-29j, 
    1:  39.6 + 8.06j, 3.40E-28 - 3.72E-28j, 
    2:  3.46 - 47.6j, 3.35E-30 + 9.69E-29j, 
    3:    105 + 116j, 2.72E-27 - 2.05E-27j, 


    >>> for i in range(V.rows):
    >>>     AV = AC * V.col(i); VL = V.col(i) * L[i]; X = AV - VL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(VL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - VL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "VL = " + Vi + " * " + Li, "AV - VL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  4.21 - 0.418j
    Checking the properties of eigenvector V0 (AV - VL should be a zero vector): 
      Eigenvector V0     AV = A * V0  VL = V0 * L[0]                AV - VL  
    -0.0249 + 0.483j, 0.0971 + 2.04j, 0.0971 + 2.04j,  1.98E-34 + 2.00E-34j, 
     0.0587 + 0.501j,  0.457 + 2.09j,  0.457 + 2.09j, -2.01E-34 + 3.10E-34j, 
    0.00311 - 0.567j, -0.224 - 2.39j, -0.224 - 2.39j,  7.70E-35 + 4.10E-34j, 
    -0.0210 - 0.435j, -0.270 - 1.82j, -0.270 - 1.82j,  4.10E-35 + 8.00E-35j, 

    Eigenvalue L[1]:  39.6 + 8.06j
    Checking the properties of eigenvector V1 (AV - VL should be a zero vector): 
     Eigenvector V1    AV = A * V1  VL = V1 * L[1]                AV - VL  
    -0.589 - 0.212j, -21.6 - 13.1j,  -21.6 - 13.1j,  1.20E-33 + 4.00E-34j, 
     0.346 + 0.299j,  11.3 + 14.6j,   11.3 + 14.6j, -6.00E-34 - 6.00E-34j, 
    0.484 + 0.0474j,  18.8 + 5.78j,   18.8 + 5.78j, -6.00E-34 - 5.90E-34j, 
    -0.148 - 0.374j, -2.83 - 16.0j,  -2.83 - 16.0j,  1.60E-34 + 3.00E-34j, 

    Eigenvalue L[2]:  3.46 - 47.6j
    Checking the properties of eigenvector V2 (AV - VL should be a zero vector): 
      Eigenvector V2    AV = A * V2  VL = V2 * L[2]                AV - VL  
    -0.319 + 0.0888j,  3.13 + 15.5j,   3.13 + 15.5j,         4.00E-34 + 0j, 
      0.326 + 0.144j,  7.99 - 15.0j,   7.99 - 15.0j, -9.00E-35 - 4.00E-34j, 
    -0.645 - 0.0595j, -5.06 + 30.5j,  -5.06 + 30.5j, -2.70E-34 + 1.00E-34j, 
      0.534 - 0.242j, -9.70 - 26.3j,  -9.70 - 26.3j,  8.00E-35 + 3.00E-34j, 

    Eigenvalue L[3]:  105 + 116j
    Checking the properties of eigenvector V3 (AV - VL should be a zero vector): 
    Eigenvector V3    AV = A * V3  VL = V3 * L[3]               AV - VL  
    0.165 + 0.359j, -24.5 + 56.8j,  -24.5 + 56.8j, 1.00E-34 + 9.00E-34j, 
    0.208 + 0.513j, -38.1 + 78.0j,  -38.1 + 78.0j, 6.00E-34 + 2.00E-34j, 
    0.358 + 0.473j, -17.5 + 91.3j,  -17.5 + 91.3j, 6.00E-34 + 1.00E-34j, 
    0.154 + 0.402j, -30.7 + 60.1j,  -30.7 + 60.1j,        2.00E-34 + 0j, 









|newpage|


Real QZ Decomposition
-------------------------------

.. method:: mat.RealQZ(Query, matB)


    Performs a real QZ decomposition of a pair of square matrices maA `=A` and matB `=B`.
    See also Eigen :cite:p:`EigenMat124`,  Wikipedia :cite:p:`WikipediaMat124`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.

:B:   Optional. A square  matrix of the same type and dimensiion as `A`. 




**Results:**

:S:     Returns matrix S in the QZ decomposition.

:T:     Returns matrix T in the QZ decomposition.

:Q:     Returns matrix Q in the QZ decomposition.

:Z:     Returns matrix Z in the QZ decomposition.



Given a real square matrices `A` and `B`, this class computes the real QZ decomposition: `A = QSZ, B = QTZ`
where `Q` and `Z` are real orthogonal matrixes, `T` is upper-triangular matrix, and `S` is upper quasi-triangular matrix. An orthogonal matrix is a matrix whose inverse is equal to its transpose, `U^{-1} = U^T` . A quasi-triangular matrix is a block-triangular matrix whose diagonal consists of 1-by-1 blocks and 2-by-2 blocks where further reduction is impossible due to complex eigenvalues.

The eigenvalues of the pencil `A - zB` can be obtained from 1x1 and 2x2 blocks on the diagonals of `S` and `T`.
If computeQZ==false, some time is saved by not computing matrices `Q` and `Z`.





.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", "")
    >>> A.show("A")
    A: 
     48, 43,  31,   19, 14, 24, 
     46, 10,  20,  4.6, 14, 10, 
     27, 39,  13,   34, 29, 37, 
    7.1, 42,  15,  2.8, 35, 23, 
     23, 50,  42, 0.44, 42, 23, 
     12, 50, 1.2,   46, 36, 47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", "")
    >>> B.show("B")
    B: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> Query = "S, T, Q, Z"
    >>> Res = A.eigen_realQZ2(Query, B)

    >>> Res["S"].show("S"); Res["T"].show("T"); Res["Q"].show("Q"); Res["Z"].show("Z")
    S: 
      -63.4,    21.2,     2.29,   -7.98,  -109, -78.3, 
          0,    54.7,    -9.94,   -22.3, -41.7, -38.8, 
          0,       0,    -3.13,    35.8, 0.634,  44.2, 
          0,       0,     11.1,    10.1,  15.2,  21.9, 
          0,       0,        0,       0,  17.7,  16.6, 
          0,       0,        0,       0,     0, -1.85, 

    T: 
      -26.0,    97.8,     19.4,    16.6,  -218,  -121, 
          0,    56.9,     41.4,    31.4, -88.6, -49.7, 
          0,       0,    -17.9,       0,  28.2,  62.7, 
          0,       0,        0,    41.7,  40.0,  15.9, 
          0,       0,        0,       0, -72.4, -18.7, 
          0,       0,        0,       0,     0,  46.3, 

    Q: 
    0.0947,    0.603,  0.134, -0.760,   -0.174, 0.0338, 
    0.0315,    0.707, -0.256,  0.422,    0.464,  0.201, 
     0.444,    0.241,  0.167,  0.302,   -0.256, -0.748, 
     0.458,   -0.264, -0.374, -0.371,    0.614, -0.257, 
     0.292, -0.00167, -0.745, 0.0408,   -0.558,  0.214, 
     0.706,  -0.0920,  0.439,  0.117, -0.00351,  0.536, 

    Z: 
    -0.0354,     -0.278,   0.668,  0.0104,  -0.670,  -0.161, 
      0.896,     -0.282, -0.0310,   0.325,  0.0639, -0.0829, 
     -0.266,     -0.660,   0.323,   0.145,   0.553,   0.249, 
     -0.338, -0.0000580,  -0.211,   0.834, -0.0902,  -0.371, 
    -0.0542,     -0.365,  -0.211,  -0.415,   0.128,  -0.794, 
    -0.0913,     -0.523,  -0.599, -0.0741,  -0.465,   0.370, 

    >>> CheckResult = (A - Res["Q"] * Res["S"] *Res["Z"]).norm()
    >>> print("||A - Q * S * Z|| (should be zero): ", (CheckResult).s())
    ||A - Q * S * Z|| (should be zero):  1.11E-32

    >>>  CheckResult = (B - Res["Q"] * Res["T"] *Res["Z"]).norm()
    >>> print("||B - Q * T * Z|| (should be zero): ", (CheckResult).s())
    ||B - Q * T * Z|| (should be zero):  1.57E-32





|newpage|


PseudoEigenSystem
--------------------------

.. method:: mat.PseudoEigenValues(Query)


    Returns the eigenvalues of the general square matrix *matA* `=A`. 

    See also Eigen :cite:p:`EigenMat125`, Eigen :cite:p:`EigenMat126`.


**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**


:pseudoeval:   Returns the pseudo-eigenvalues of given matrix.

:pseudoevec:   Returns the pseudo-eigenvectors of given matrix.





Computes eigenvalues and eigenvectors of general matrices.
The eigenvalues and eigenvectors of a matrix `A` are scalars `\lambda` and vectors `v` such that `Av = \lambda v`. If `D` is a diagonal matrix with the eigenvalues on the diagonal, and `V` is a matrix with the eigenvectors as its columns, then `AV = V D` . The matrix `V` is almost always invertible, in which case we have `A = V DV^{-1}`. This is called the eigendecomposition. The eigenvalues and eigenvectors of a matrix may be complex, even when the matrix is real. However, we can choose real matrices `V` and `D` satisfying `AV = V D`, just like the eigendecomposition, if the matrix `D` is not required to be diagonal, but if it is allowed to have blocks of the form


.. math::   \begin{bmatrix} 
                \mathbf{u} & \mathbf{v} \\ 
                \mathbf{-v} & \mathbf{u} 
            \end{bmatrix} 


(where `u` and `v` are real numbers) on the diagonal. These blocks correspond to complex eigenvalue pairs `u \pm iv`. We call this variant of the eigendecomposition the pseudo-eigendecomposition.

Call the function compute() to compute the eigenvalues and eigenvectors of a given matrix. Alternatively, you
can use the EigenSolver(const MatrixType, bool) constructor which computes the eigenvalues and eigenvectors at
construction time. Once the eigenvalue and eigenvectors are computed, they can be retrieved with the eigenvalues()
and eigenvectors() functions. The pseudoEigenvalueMatrix() and pseudoEigenvectors() methods allow the
construction of the pseudo-eigendecomposition.

The matrix is first reduced to real Schur form using the RealSchur (or Complex) class. The Schur decomposition is then used
to compute the eigenvalues and eigenvectors. The cost of the computation is dominated by the cost of the Schur
decomposition, which is very approximately 25n3 (where n is the size of the matrix) if computeEigenvectors is
true, and 10n3 if computeEigenvectors is false. This method reuses of the allocated data in the EigenSolver object.





.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", "")
    >>> A.show("A")
    A: 
     48, 43,  31,   19, 14, 24, 
     46, 10,  20,  4.6, 14, 10, 
     27, 39,  13,   34, 29, 37, 
    7.1, 42,  15,  2.8, 35, 23, 
     23, 50,  42, 0.44, 42, 23, 
     12, 50, 1.2,   46, 36, 47, 

    >>> Query = "PseudoEval, PseudoEvec"
    >>> Res = A.eigen_PseudoEigenSystem2(Query)

    >>> D = Res["PseudoEval"]; D.show("D")
    D: 
    158,     0,    0,     0,    0,     0, 
      0, -20.8,    0,     0,    0,     0, 
      0,     0, 21.2,     0,    0,     0, 
      0,     0,    0,  3.32, 16.6,     0, 
      0,     0,    0, -16.6, 3.32,     0, 
      0,     0,    0,     0,    0, -2.45, 

    >>> V = Res["PseudoEvec"]; V.show("V")
    V: 
    0.448, -0.313,  0.464, -0.0997,  0.684, -0.0912, 
    0.283,  0.535,  0.454,   0.474,   1.04,  -0.443, 
    0.442,  0.277, -0.364,  -0.905,  -1.00,   0.221, 
    0.312, -0.406, -0.138,   0.852, -0.183,   -1.04, 
    0.463, -0.583, -0.101,   0.584,  0.979,  -0.632, 
    0.460,  0.240, -0.692,  -0.982,  -2.34,    1.89, 

    >>> Vinv = V.eigen_inverse(); Vinv.show(" V^-1")
     V^-1: 
     0.478,  0.587,  0.337,  0.273,  0.423,   0.412, 
    -0.731,  0.985,  0.336, -0.141, -0.150,  0.0289, 
      1.59, 0.0374, -0.514,  0.680,  -1.54, 0.00611, 
    -0.287,  0.467, -0.869,  0.481, 0.0293,   0.471, 
    -0.303,  0.129, 0.0641, -0.688,  0.740,  -0.123, 
    0.0355,  0.147, -0.684, -0.400,  0.283,   0.519, 

    >>> CheckResult = (A - V * D * Vinv).norm()
    >>> print("||A - V * D * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - V * D * V^-1|| (should be zero):  3.25E-33












|newpage|


Real Generalized Nonsymmetric Eigenvalues
-----------------------------------------------------

.. method:: mat.GenEigenValues(Query)



    Returns the Generalized Nonsymmetric Eigensystem; Eigenvalues only of the general matrix *matA* `=A`.
    See also Eigen :cite:p:`EigenMat123`,  Wikipedia :cite:p:`WikipediaMat123`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.




Computes the generalized eigenvalues and eigenvectors of a pair of general (nonsymmetric) matrices. Currently, only real matrices are supported.

The generalized eigenvalues and eigenvectors of a matrix pair `A` and `B` are scalars `\lambda` and vectors `v` such that `Av = \lambda Bv`. If `D` is a diagonal matrix with the eigenvalues on the diagonal, and `V` is a matrix with the eigenvectors as its columns, then `AV = BV D`. The matrix `V` is almost always invertible, in which case we have `A = BV DV^{-1}`. This is called the generalized eigen-decomposition.

The generalized eigenvalues and eigenvectors of a matrix pair may be complex, even when the matrices are real. Moreover, the generalized eigenvalue might be infinite if the matrix B is singular. To workaround this difficulty, the eigenvalues are provided as a pair of complex `\alpha` and real `\beta` such that: `\lambda_i = \alpha_i/\beta_i`. If `\beta_i` is (nearly) zero, then one can consider the well defined left eigenvalue `\mu_i = \beta_i/\alpha_i`    such that: `\mu_i Av_i = B v_i`, or even `\mu_i u_i^T Av_i = u_i^T B`, where
`u_i` is called the left eigenvector.





.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", "")
    >>> A.show("A")
    A: 
     48, 43,  31,   19, 14, 24, 
     46, 10,  20,  4.6, 14, 10, 
     27, 39,  13,   34, 29, 37, 
    7.1, 42,  15,  2.8, 35, 23, 
     23, 50,  42, 0.44, 42, 23, 
     12, 50, 1.2,   46, 36, 47, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", "")
    >>> B.show("B")
    B: 
    44.9, 25.5, 50.0, 47.9, 26.4, 62.0, 
    25.5, 24.3, 49.1, 95.0, 29.0, 46.6, 
    50.0, 49.1, 55.5, 84.0, 44.4, 26.7, 
    47.9, 95.0, 84.0, 64.5, 39.5, 87.5, 
    26.4, 29.0, 44.4, 39.5, 39.8, 12.3, 
    62.0, 46.6, 26.7, 87.5, 12.3, 85.0, 

    >>> Query = "Eval"
    >>> Res = A.eigen_GenEigenValues2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    i            L[i]  
    0:      2.44 + 0j, 
    1:     0.960 + 0j, 
    2: 0.209 - 0.729j, 
    3: 0.209 + 0.729j, 
    4:    -0.245 + 0j, 
    5:   -0.0398 + 0j, 

    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = A.cplx() - B.cplx() * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i            L[i]      Det(A - B * L[i])  
    0:      2.44 + 0j,         2.87E-23 + 0j, 
    1:     0.960 + 0j,         1.17E-25 + 0j, 
    2: 0.209 - 0.729j, -3.30E-26 + 3.44E-26j, 
    3: 0.209 + 0.729j, -3.30E-26 - 3.44E-26j, 
    4:    -0.245 + 0j,        -1.11E-27 + 0j, 
    5:   -0.0398 + 0j,         3.55E-27 + 0j, 




|newpage|


Real Generalized Nonsymmetric Eigensystem
-----------------------------------------------------

.. method:: mat.GenEigenSystem(Query)



    Returns the Generalized Nonsymmetric Eigensystem; Eigenvalues only of the general matrix *matA* `=A`.
    See also Eigen :cite:p:`EigenMat123`,  Wikipedia :cite:p:`WikipediaMat123`,  Wikipedia :cite:p:`WikipediaMat130`.



**Parameters:**

:Query:     Required. A string specifying which items of the result section should be computed.


**Results:**


:eval:   Returns the eigenvalues of given matrix.

:evec:   Returns the eigenvectors of given matrix.




.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf(); mp14.setdps(35); mp14.setshowdps(3)
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomA6x6", "")
    >>> A = A.top_left_corner(4,4); A.show("A ")
    A : 
     48, 43, 31,  19, 
     46, 10, 20, 4.6, 
     27, 39, 13,  34, 
    7.1, 42, 15, 2.8, 

    >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableRandomSAA6x6", "")
    >>> B = B.top_left_corner(4,4); B.show("B")
    B: 
    44.9, 25.5, 50.0, 47.9, 
    25.5, 24.3, 49.1, 95.0, 
    50.0, 49.1, 55.5, 84.0, 
    47.9, 95.0, 84.0, 64.5, 

    >>> Query = "Eval, Evec"
    >>> Res = A.eigen_GenEigenSystem2(Query, B)

    >>> L = Res["Eval"]; ct = ["L[i]"]; rt = ["i"] + [x for x in range(L.rows)]
    >>> L.show("Vector L of eigenvalues", coltitles = ct, rowtitles = rt)
    Vector L of eigenvalues: 
    i            L[i]  
    0: 0.431 - 0.989j, 
    1: 0.431 + 0.989j, 
    2:   -0.0862 + 0j, 
    3:     0.703 + 0j, 

    >>> V =  Res["Evec"]; mt = "Matrix V of eigenvectors (V0, ... , V" + str(V.cols-1) + ")"
    >>> V.show(mt, coltitles = ["V#"] * (V.cols))
    Matrix V of eigenvectors (V0, ... , V3): 
                  V0                V1           V2           V3  
      0.364 - 0.364j,   0.364 + 0.364j,  0.404 + 0j, -0.581 + 0j, 
     -0.281 - 0.488j,  -0.281 + 0.488j,  0.316 + 0j,  0.231 + 0j, 
      0.208 + 0.611j,   0.208 - 0.611j, -0.808 + 0j,  0.645 + 0j, 
    0.0202 + 0.0331j, 0.0202 - 0.0331j, -0.289 + 0j, -0.439 + 0j, 

    >>> AC = A.cplx(); BC = B.cplx()
    >>> # Vinv = V^-1 = V.H
    >>> Vinv = V.eigen_inverse(); Vinv.show(" V^-1")
    V^-1: 
         1.04 + 0.651j,    0.0367 + 1.33j,    0.669 + 0.592j,   -0.376 + 0.707j, 
         1.04 - 0.651j,    0.0367 - 1.33j,    0.669 - 0.592j,   -0.376 - 0.707j, 
    -0.295 + 9.42E-38j, -1.41 - 1.88E-36j, -1.19 - 3.62E-37j, -2.09 - 3.10E-36j, 
     0.192 + 1.76E-37j, 0.731 + 1.08E-36j, 0.754 + 8.75E-38j, -1.04 + 1.45E-36j, 

    >>> CheckResult = (AC - BC * V * L.D * Vinv).norm()
    >>> print("||A - B * V * diag(L) * V^-1|| (should be zero): ", (CheckResult).s())
    ||A - B * V * diag(L) * V^-1|| (should be zero):  2.54E-33 + 0j

    >>> Det = L * 0 # creates a zero vector of the same size and type as L

    >>> for i in range(A.rows):
    >>>     X = AC - BC * L[i]
    >>>     Det[i] = X.eigen_det()

    >>> Result = L.concat_horizontal(Det)
    >>> mt = "Checking the Eigenvalues (Det(A - B * L[i]) should be zero)"
    >>> ct = ["L[i]", "Det(A - B * L[i])"]
    >>> Result.show(mt, coltitles = ct, rowtitles = rt)
    Checking the Eigenvalues (Det(A - B * L[i]) should be zero): 
    i            L[i]     Det(A - B * L[i])  
    0: 0.431 - 0.989j, 1.41E-28 - 2.02E-28j, 
    1: 0.431 + 0.989j, 1.41E-28 + 2.02E-28j, 
    2:   -0.0862 + 0j,       -1.01E-29 + 0j, 
    3:     0.703 + 0j,       -8.72E-30 + 0j, 


    >>> for i in range(V.rows):
    >>>     AV = AC * V.col(i); BVL = (BC * L[i]) * V.col(i); X = AV - BVL
    >>>     Li = "L[" + str(i) + "]"; Vi = "V" + str(i)
    >>>     print("Eigenvalue " + Li + ": ", L[i].s())
    >>>     Result = V.col(i).concat_horizontal(AV).concat_horizontal(BVL).concat_horizontal(X)
    >>>     mt = "Checking the properties of eigenvector " + Vi + " (AV - BVL should be a zero vector)"
    >>>     ct = ["Eigenvector " + Vi, "AV = A * " + Vi, "BVL = B * " + Vi + " * " + Li, "   AV - BVL"]
    >>>     Result.show(mt, coltitles = ct)

    Eigenvalue L[0]:  0.431 - 0.989j
    Checking the properties of eigenvector V0 (AV - BVL should be a zero vector): 
      Eigenvector V0    AV = A * V0  BVL = B * V0 * L[0]               AV - BVL  
      0.364 - 0.364j,  12.2 - 18.8j,        12.2 - 18.8j,  1.00E-34 + 4.00E-34j, 
     -0.281 - 0.488j,  18.2 - 9.23j,        18.2 - 9.23j,         0 + 9.00E-35j, 
      0.208 + 0.611j,  2.24 - 19.8j,        2.24 - 19.8j,  1.60E-34 - 2.00E-34j, 
    0.0202 + 0.0331j, -6.06 - 13.8j,       -6.06 - 13.8j, -4.00E-35 - 4.00E-34j, 

    Eigenvalue L[1]:  0.431 + 0.989j
    Checking the properties of eigenvector V1 (AV - BVL should be a zero vector): 
      Eigenvector V1    AV = A * V1  BVL = B * V1 * L[1]               AV - BVL  
      0.364 + 0.364j,  12.2 + 18.8j,        12.2 + 18.8j,  1.00E-34 - 4.00E-34j, 
     -0.281 + 0.488j,  18.2 + 9.23j,        18.2 + 9.23j,         0 - 9.00E-35j, 
      0.208 - 0.611j,  2.24 + 19.8j,        2.24 + 19.8j,  1.60E-34 + 2.00E-34j, 
    0.0202 - 0.0331j, -6.06 + 13.8j,       -6.06 + 13.8j, -4.00E-35 + 4.00E-34j, 

    Eigenvalue L[2]:  -0.0862 + 0j
    Checking the properties of eigenvector V2 (AV - BVL should be a zero vector): 
    Eigenvector V2  AV = A * V2  BVL = B * V2 * L[2]        AV - BVL  
        0.404 + 0j,   2.42 + 0j,           2.42 + 0j, -1.00E-35 + 0j, 
        0.316 + 0j,   4.24 + 0j,           4.24 + 0j, -4.00E-35 + 0j, 
       -0.808 + 0j,   2.88 + 0j,           2.88 + 0j,  2.10E-34 + 0j, 
       -0.289 + 0j,   3.21 + 0j,           3.21 + 0j,  2.60E-34 + 0j, 

    Eigenvalue L[3]:  0.703 + 0j
    Checking the properties of eigenvector V3 (AV - BVL should be a zero vector): 
    Eigenvector V3  AV = A * V3  BVL = B * V3 * L[3]        AV - BVL  
       -0.581 + 0j,  -6.34 + 0j,          -6.34 + 0j,  1.40E-34 + 0j, 
        0.231 + 0j,  -13.6 + 0j,          -13.6 + 0j, -1.00E-34 + 0j, 
        0.645 + 0j,  -13.2 + 0j,          -13.2 + 0j,  5.00E-34 + 0j, 
       -0.439 + 0j,   14.0 + 0j,           14.0 + 0j,  5.00E-34 + 0j, 






