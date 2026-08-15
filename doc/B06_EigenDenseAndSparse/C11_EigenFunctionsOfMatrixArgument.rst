

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}



.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|



Eigen: Functions of matrix argument
===============================================================================




Matrix Exponential
--------------------------------------------------------------------

.. method:: matA.Expm()


    Computes the matrix exponential of a square matrix `A`, which is defined by the power series  `\displaystyle  \exp(A) = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \ldots`


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat141`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat191`.



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



Matrix Sine
------------------------------------------------------------

.. method:: matA.Sinm(A)


    Calculates the sine function of the matrix.

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat192`.




    The cosine of a square matrix `A` is defined in analogy with the matrix exponential.


    .. math ::     \cos(A) =  \frac{e^{iA} + e^{-iA}}{2}


    .. math ::     \sin(A) =  \frac{e^{iA} - e^{-iA}}{2i}


    .. math ::     \cos^2(A) + \sin^2(A) =  I

    For real `A`, we can write `\cos(A) = \Re ( e^{iA} )` and `\sin(A) = \Im ( e^{iA} )`.


    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}


    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}


    Examples::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> X = eye(3)
        >>> cosm(X)
        [0.54030230586814               0.0               0.0]
        [             0.0  0.54030230586814               0.0]
        [             0.0               0.0  0.54030230586814]
        >>> X = hilbert(3)
        >>> cosm(X)
        [ 0.424403834569555  -0.316643413047167  -0.221474945949293]
        [-0.316643413047167   0.820646708837824  -0.127183694770039]
        [-0.221474945949293  -0.127183694770039   0.909236687217541]
        >>> X = matrix([[1+j,-2],[0,-j]])
        >>> cosm(X)
        [(0.833730025131149 - 0.988897705762865j)  (1.07485840848393 - 0.17192140544213j)]
        [                                     0.0               (1.54308063481524 + 0.0j)]








Matrix Cosine
-------------------------------------------------------------


.. method:: matA.Cosm()


    Calculates the cosine function of the matrix.

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat193`.



    The cosine of a square matrix `A` is defined in analogy with the matrix exponential.

    .. math ::     \cos(A) =  \frac{e^{iA} + e^{-iA}}{2}

    .. math ::     \sin(A) =  \frac{e^{iA} - e^{-iA}}{2i}

    .. math ::     \cos^2(A) + \sin^2(A) =  I


    For real `A`, we can write `\cos(A) = \Re ( e^{iA} )` and `\sin(A) = \Im ( e^{iA} )`.

    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}

    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}



    Examples::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> X = eye(3)
        >>> cosm(X)
        [0.54030230586814               0.0               0.0]
        [             0.0  0.54030230586814               0.0]
        [             0.0               0.0  0.54030230586814]
        >>> X = hilbert(3)
        >>> cosm(X)
        [ 0.424403834569555  -0.316643413047167  -0.221474945949293]
        [-0.316643413047167   0.820646708837824  -0.127183694770039]
        [-0.221474945949293  -0.127183694770039   0.909236687217541]
        >>> X = matrix([[1+j,-2],[0,-j]])
        >>> cosm(X)
        [(0.833730025131149 - 0.988897705762865j)  (1.07485840848393 - 0.17192140544213j)]
        [                                     0.0               (1.54308063481524 + 0.0j)]





|newpage|



Matrix Hyperbolic Sine
---------------------------------------------------------

.. method:: matA.Sinhm()


    Calculates the hyperbolic sine function of the matrix.

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat194`.




    The hyperbolic sine of a square matrix `A` is defined in analogy with the matrix exponential.

    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}

    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}

    .. math ::     \cosh^2(A) + \sinh^2(A) =  I



    .. code-block:: vbnet
        
        Sub DemoCplxMatrixFunctions()        
            Console.WriteLine("Hello CplxMatrixFunctions!")
            Dim digits = 15        
            Dim n As Int32 = 4
            Dim A, B, C, D, E, F As New cplx_mat_t
            A.RandomSymmetric(n)
            A.Print("A: ")
        
            B = A.SinhMat()
            B.Print("B = Sinh(A): ")
            C = A.CoshMat()
            C.Print("C = Cosh(A): ")
            D = C * C - B * B
            D.Print("C * C - B * B: ")
        End Sub    


    .. code-block:: none

        Hello CplxMatrixFunctions!
        A: 
         0.254341-1.994995j,  1.110691+0.032289j, -0.311350-0.647176j,  0.547685-1.281594j; 
         1.110691+0.032289j,  1.435774-1.303568j, -0.641133-0.284371j, -0.827662-0.328684j; 
        -0.311350-0.647176j, -0.641133-0.284371j, -0.217231+1.954100j, -0.776330-0.558306j; 
         0.547685-1.281594j, -0.827662-0.328684j, -0.776330-0.558306j,  0.652181-1.335063j; 


        B = Sinh(A): 
        -0.344029-0.627502j,  0.956056-0.480516j, -0.134878-0.034162j, -0.590098+0.338244j; 
         0.956056-0.480516j,  1.739419-3.149695j, -0.793048-0.141610j, -1.597165+0.360539j; 
        -0.134878-0.034162j, -0.793048-0.141610j, -0.152880+1.211517j, -0.351965+0.026714j; 
        -0.590098+0.338244j, -1.597165+0.360539j, -0.351965+0.026714j,  0.171917-0.584919j; 

        C = Cosh(A): 
        -0.039723+0.009230j,  0.532073-1.170311j, -0.476465+0.181642j, -1.605643-0.168838j; 
         0.532073-1.170311j,  2.022858-2.326341j, -0.294411-0.149198j, -1.095355+1.019715j; 
        -0.476465+0.181642j, -0.294411-0.149198j, -0.216192+0.186437j,  0.187127+0.027892j; 
        -1.605643-0.168838j, -1.095355+1.019715j,  0.187127+0.027892j,  0.851060-0.052593j; 

        C * C - B * B: 
         1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j; 






|newpage|



Matrix Hyperbolic Cosine
-------------------------------------------


.. method:: matA.Coshm()


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat142`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat195`.



    Calculates the hyperbolic cosine function of the matrix.

    The hyperbolic cosine of a square matrix `A` is defined in analogy with the matrix exponential.

    .. math :: \cosh(A) =  \frac{e^{A} + e^{-A}}{2}

    .. math :: \sinh(A) =  \frac{e^{A} - e^{-A}}{2}

    .. math ::     \cosh^2(A) + \sinh^2(A) =  I



    .. code-block:: vbnet
        
        Sub DemoCplxMatrixFunctions()        
            Console.WriteLine("Hello CplxMatrixFunctions!")
            Dim digits = 15        
            Dim n As Int32 = 4
            Dim A, B, C, D, E, F As New cplx_mat_t
            A.RandomSymmetric(n)
            A.Print("A: ")
            B = A.ExpMat()
            B.Print("B = Exp(A): ")
            C = B.LogMat()
            C.Print("C = Log(B): ")
        
            D = B.SqrtMat()
            D.Print("D = Sqrt(B): ")
            E = D * D
            E.Print("E = D * D: ")
        
            B = A.SinMat()
            B.Print("B = Sin(A): ")
            C = A.CosMat()
            C.Print("C = Cos(A): ")
            D = B * B + C * C
            D.Print("B * B + C * C: ")
        
            B = A.SinhMat()
            B.Print("B = Sinh(A): ")
            C = A.CoshMat()
            C.Print("C = Cosh(A): ")
            D = C * C - B * B
            D.Print("C * C - B * B: ")
        End Sub    


    .. code-block:: none

        Hello CplxMatrixFunctions!
        A: 
         0.254341-1.994995j,  1.110691+0.032289j, -0.311350-0.647176j,  0.547685-1.281594j; 
         1.110691+0.032289j,  1.435774-1.303568j, -0.641133-0.284371j, -0.827662-0.328684j; 
        -0.311350-0.647176j, -0.641133-0.284371j, -0.217231+1.954100j, -0.776330-0.558306j; 
         0.547685-1.281594j, -0.827662-0.328684j, -0.776330-0.558306j,  0.652181-1.335063j; 

        B = Exp(A): 
        -0.383752-0.618272j,  1.488129-1.650828j, -0.611343+0.147480j, -2.195741+0.169406j; 
         1.488129-1.650828j,  3.762277-5.476036j, -1.087459-0.290808j, -2.692520+1.380254j; 
        -0.611343+0.147480j, -1.087459-0.290808j, -0.369072+1.397953j, -0.164837+0.054606j; 
        -2.195741+0.169406j, -2.692520+1.380254j, -0.164837+0.054606j,  1.022977-0.637512j; 

        C = Log(B): 
         0.254341-1.994995j,  1.110691+0.032289j, -0.311350-0.647176j,  0.547685-1.281594j; 
         1.110691+0.032289j,  1.435774-1.303568j, -0.641133-0.284371j, -0.827662-0.328684j; 
        -0.311350-0.647176j, -0.641133-0.284371j, -0.217231+1.954100j, -0.776330-0.558306j; 
         0.547685-1.281594j, -0.827662-0.328684j, -0.776330-0.558306j,  0.652181-1.335063j; 

        D = Sqrt(B): 
         0.508620-0.931943j,  0.661969-0.319593j, -0.337003-0.172068j, -0.485698-0.655636j; 
         0.661969-0.319593j,  2.077099-1.250104j, -0.401242-0.208424j, -0.746596+0.018077j; 
        -0.337003-0.172068j, -0.401242-0.208424j,  0.502520+0.963369j, -0.377613-0.193978j; 
        -0.485698-0.655636j, -0.746596+0.018077j, -0.377613-0.193978j,  1.013700-0.687531j; 

        E = D * D: 
        -0.383752-0.618272j,  1.488129-1.650828j, -0.611343+0.147480j, -2.195741+0.169406j; 
         1.488129-1.650828j,  3.762277-5.476036j, -1.087459-0.290808j, -2.692520+1.380254j; 
        -0.611343+0.147480j, -1.087459-0.290808j, -0.369072+1.397953j, -0.164837+0.054606j; 
        -2.195741+0.169406j, -2.692520+1.380254j, -0.164837+0.054606j,  1.022977-0.637512j; 

        B = Sin(A): 
         3.185996-4.423204j,  1.572018+0.576777j, -0.236161-2.007119j,  3.744383-3.392271j; 
         1.572018+0.576777j,  0.829215-0.073722j, -0.452703-0.362702j,  0.213357-0.343298j; 
        -0.236161-2.007119j, -0.452703-0.362702j, -0.274184+2.749772j, -0.899405-1.828027j; 
         3.744383-3.392271j,  0.213357-0.343298j, -0.899405-1.828027j,  3.157659-2.589512j; 

        C = Cos(A): 
         4.524926+3.229556j, -0.735268+1.275592j,  1.749846+0.069384j,  3.245352+3.579443j; 
        -0.735268+1.275592j, -0.328697+0.628146j,  0.172580+0.683175j,  0.290239+0.309901j; 
         1.749846+0.069384j,  0.172580+0.683175j,  3.469410-0.664084j,  0.996030+0.538410j; 
         3.245352+3.579443j,  0.290239+0.309901j,  0.996030+0.538410j,  2.603737+2.713445j; 

        B * B + C * C: 
         1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j; 

        B = Sinh(A): 
        -0.344029-0.627502j,  0.956056-0.480516j, -0.134878-0.034162j, -0.590098+0.338244j; 
         0.956056-0.480516j,  1.739419-3.149695j, -0.793048-0.141610j, -1.597165+0.360539j; 
        -0.134878-0.034162j, -0.793048-0.141610j, -0.152880+1.211517j, -0.351965+0.026714j; 
        -0.590098+0.338244j, -1.597165+0.360539j, -0.351965+0.026714j,  0.171917-0.584919j; 

        C = Cosh(A): 
        -0.039723+0.009230j,  0.532073-1.170311j, -0.476465+0.181642j, -1.605643-0.168838j; 
         0.532073-1.170311j,  2.022858-2.326341j, -0.294411-0.149198j, -1.095355+1.019715j; 
        -0.476465+0.181642j, -0.294411-0.149198j, -0.216192+0.186437j,  0.187127+0.027892j; 
        -1.605643-0.168838j, -1.095355+1.019715j,  0.187127+0.027892j,  0.851060-0.052593j; 

        C * C - B * B: 
         1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j,  0.000000+0.000000j; 
         0.000000+0.000000j,  0.000000+0.000000j,  0.000000+0.000000j,  1.000000+0.000000j; 






|newpage|



Matrix Square Root
-------------------------------------


.. method:: matA.Sqrtm()


    Computes a square root of the square matrix `A`, i.e. returns a matrix `B = A^{1/2}` such that `B^2 = A`. The square root of a matrix, if it exists, is not unique.


    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat144`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat196`.


    **Examples**

    Square roots of some simple matrices::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> sqrtm([[1,0], [0,1]])
        [1.0  0.0]
        [0.0  1.0]
        >>> sqrtm([[0,0], [0,0]])
        [0.0  0.0]
        [0.0  0.0]
        >>> sqrtm([[2,0],[0,1]])
        [1.4142135623731  0.0]
        [            0.0  1.0]
        >>> sqrtm([[1,1],[1,0]])
        [ (0.920442065259926 - 0.21728689675164j)  (0.568864481005783 + 0.351577584254143j)]
        [(0.568864481005783 + 0.351577584254143j)  (0.351577584254143 - 0.568864481005783j)]
        >>> sqrtm([[1,0],[0,1]])
        [1.0  0.0]
        [0.0  1.0]
        >>> sqrtm([[-1,0],[0,1]])
        [(0.0 - 1.0j)           0.0]
        [         0.0  (1.0 + 0.0j)]
        >>> sqrtm([[j,0],[0,j]])
        [(0.707106781186547 + 0.707106781186547j)                                       0.0]
        [                                     0.0  (0.707106781186547 + 0.707106781186547j)]

    A square root of a rotation matrix, giving the corresponding
    half-angle rotation matrix::

        >>> t1 = 0.75
        >>> t2 = t1 * 0.5
        >>> A1 = matrix([[cos(t1), -sin(t1)], [sin(t1), cos(t1)]])
        >>> A2 = matrix([[cos(t2), -sin(t2)], [sin(t2), cos(t2)]])
        >>> sqrtm(A1)
        [0.930507621912314  -0.366272529086048]
        [0.366272529086048   0.930507621912314]
        >>> A2
        [0.930507621912314  -0.366272529086048]
        [0.366272529086048   0.930507621912314]

    The identity `(A^2)^{1/2} = A` does not necessarily hold::

        >>> A = matrix([[4,1,4],[7,8,9],[10,2,11]])
        >>> sqrtm(A**2)
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]
        >>> sqrtm(A)**2
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]
        >>> A = matrix([[-4,1,4],[7,-8,9],[10,2,11]])
        >>> sqrtm(A**2)
        [  7.43715112194995  -0.324127569985474   1.8481718827526]
        [-0.251549715716942    9.32699765900402  2.48221180985147]
        [  4.11609388833616   0.775751877098258   13.017955697342]
        >>> chop(sqrtm(A)**2)
        [-4.0   1.0   4.0]
        [ 7.0  -8.0   9.0]
        [10.0   2.0  11.0]

    For some matrices, a square root does not exist::

        >>> sqrtm([[0,1], [0,0]])
        Traceback (most recent call last):
            ...
        ZeroDivisionError: matrix is numerically singular

    Two examples from the documentation for Matlab's ``sqrtm``::

        >>> mp.dps = 15; mp.pretty = True
        >>> sqrtm([[7,10],[15,22]])
        [1.56669890360128  1.74077655955698]
        [2.61116483933547  4.17786374293675]
        >>>
        >>> X = matrix(\
        ...   [[5,-4,1,0,0],
        ...   [-4,6,-4,1,0],
        ...   [1,-4,6,-4,1],
        ...   [0,1,-4,6,-4],
        ...   [0,0,1,-4,5]])
        >>> Y = matrix(\
        ...   [[2,-1,-0,-0,-0],
        ...   [-1,2,-1,0,-0],
        ...   [0,-1,2,-1,0],
        ...   [-0,0,-1,2,-1],
        ...   [-0,-0,-0,-1,2]])
        >>> mnorm(sqrtm(X) - Y)
        4.53155328326114e-19







|newpage|



Matrix Logarithm
--------------------------------------


.. method:: matA.Logm()


    Calculates the logarithm of the matrix.

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat143`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat197`.




    Computes a logarithm of the square matrix `A`, i.e. returns a matrix `B = \log(A)` such that `\exp(B) = A`. 
    The logarithm of a matrix, if it exists, is not unique.

    **Examples**

    Logarithms of some simple matrices::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> X = eye(3)
        >>> logm(X)
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        [0.0  0.0  0.0]
        >>> logm(2*X)
        [0.693147180559945                0.0                0.0]
        [              0.0  0.693147180559945                0.0]
        [              0.0                0.0  0.693147180559945]
        >>> logm(expm(X))
        [1.0  0.0  0.0]
        [0.0  1.0  0.0]
        [0.0  0.0  1.0]

    A logarithm of a complex matrix::

        >>> X = matrix([[2+j, 1, 3], [1-j, 1-2*j, 1], [-4, -5, j]])
        >>> B = logm(X)
        >>> nprint(B)
        [ (0.808757 + 0.107759j)    (2.20752 + 0.202762j)   (1.07376 - 0.773874j)]
        [ (0.905709 - 0.107795j)  (0.0287395 - 0.824993j)  (0.111619 + 0.514272j)]
        [(-0.930151 + 0.399512j)   (-2.06266 - 0.674397j)  (0.791552 + 0.519839j)]
        >>> chop(expm(B))
        [(2.0 + 1.0j)           1.0           3.0]
        [(1.0 - 1.0j)  (1.0 - 2.0j)           1.0]
        [        -4.0          -5.0  (0.0 + 1.0j)]

    A matrix `X` close to the identity matrix, for which
    `\log(\exp(X)) = \exp(\log(X)) = X` holds::

        >>> X = eye(3) + hilbert(3)/4
        >>> X
        [              1.25             0.125  0.0833333333333333]
        [             0.125  1.08333333333333              0.0625]
        [0.0833333333333333            0.0625                1.05]
        >>> logm(expm(X))
        [              1.25             0.125  0.0833333333333333]
        [             0.125  1.08333333333333              0.0625]
        [0.0833333333333333            0.0625                1.05]
        >>> expm(logm(X))
        [              1.25             0.125  0.0833333333333333]
        [             0.125  1.08333333333333              0.0625]
        [0.0833333333333333            0.0625                1.05]

    A logarithm of a rotation matrix, giving back the angle of
    the rotation::

        >>> t = 3.7
        >>> A = matrix([[cos(t),sin(t)],[-sin(t),cos(t)]])
        >>> chop(logm(A))
        [             0.0  -2.58318530717959]
        [2.58318530717959                0.0]
        >>> (2*pi-t)
        2.58318530717959

    For some matrices, a logarithm does not exist::

        >>> logm([[1,0], [0,0]])
        Traceback (most recent call last):
            ...
        ZeroDivisionError: matrix is numerically singular

    Logarithm of a matrix with large entries::

        >>> logm(hilbert(3) * 10**20).apply(re)
        [ 45.5597513593433  1.27721006042799  0.317662687717978]
        [ 1.27721006042799  42.5222778973542   2.24003708791604]
        [0.317662687717978  2.24003708791604    42.395212822267]




|newpage|



Matrix power
-------------------------------------------------

.. method:: mat.Powm(r)


    Computes `A^r = \exp(A \log r)` for a matrix `A` and complex number `r`.

    See also:   Wikipedia :cite:p:`WikipediaMat140`,  Wikipedia :cite:p:`WikipediaMat141`,  Wikipedia :cite:p:`WikipediaMat143`.

    See also: Eigen :cite:p:`EigenMat190`, Eigen :cite:p:`EigenMat198`.





    **Examples**

    Powers and inverse powers of a matrix::

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = True
        >>> A = matrix([[4,1,4],[7,8,9],[10,2,11]])
        >>> powm(A, 2)
        [ 63.0  20.0   69.0]
        [174.0  89.0  199.0]
        [164.0  48.0  179.0]
        >>> chop(powm(powm(A, 4), 1/4.))
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]
        >>> powm(extraprec(20)(powm)(A, -4), -1/4.)
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]
        >>> chop(powm(powm(A, 1+0.5j), 1/(1+0.5j)))
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]
        >>> powm(extraprec(5)(powm)(A, -1.5), -1/(1.5))
        [ 4.0  1.0   4.0]
        [ 7.0  8.0   9.0]
        [10.0  2.0  11.0]

    A Fibonacci-generating matrix::

        >>> powm([[1,1],[1,0]], 10)
        [89.0  55.0]
        [55.0  34.0]
        >>> fib(10)
        55.0
        >>> powm([[1,1],[1,0]], 6.5)
        [(16.5166626964253 - 0.0121089837381789j)  (10.2078589271083 + 0.0195927472575932j)]
        [(10.2078589271083 + 0.0195927472575932j)  (6.30880376931698 - 0.0317017309957721j)]
        >>> (phi**6.5 - (1-phi)**6.5)/sqrt(5)
        (10.2078589271083 - 0.0195927472575932j)
        >>> powm([[1,1],[1,0]], 6.2)
        [ (14.3076953002666 - 0.008222855781077j)  (8.81733464837593 + 0.0133048601383712j)]
        [(8.81733464837593 + 0.0133048601383712j)  (5.49036065189071 - 0.0215277159194482j)]
        >>> (phi**6.2 - (1-phi)**6.2)/sqrt(5)
        (8.81733464837593 - 0.0133048601383712j)







