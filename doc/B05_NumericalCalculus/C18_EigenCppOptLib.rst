

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />




Eigen/CppOptLib: multidimensional optimization
===============================================================================




The Homepage  is https://github.com/PatWie/CppNumericalSolvers. 


To use another solver, simply replace BfgsSolver by another name. Supported solvers are:

gradient descent solver (GradientDescentSolver)

conjugate gradient descent solver (ConjugatedGradientDescentSolver)

BFGS solver (BfgsSolver)

L-BFGS solver (LbfgsSolver)
bfgsbSolver)

CMAes solver (CMAesSolver)

Nelder-Mead solver (NelderMeadSolver)

These solvers are tested on the Rosenbrock function from multiple difficult starting points by unit tests using the Google Testing Framework. And yes, you can use them directly in MATLAB. Additional benchmark functions are Beale, GoldsteinPrice, Booth, Matyas, Levi. Note, not all solvers are equivalently good at all problems.

For checking your gradient this library uses high-order central difference. Study the examples for more information about including box-constraints and gradient-information.





|newpage|

Nelder-Mead Solver
-------------------------------------------------------------------------

.. method:: ctxboost.NelderMead(f, fjac, matInput)

The Nelder-Mead method (or downhill simplex method) is a commonly applied numerical method used to find the minimum or maximum of an objective function in a multidimensional space. 

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat136`.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.





**Example:**


The routine in Python:

.. code-block:: pycon

    def demo_NelderMeadCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the NelderMead solver
        matRes = ctx.nelderMeadSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)


The same routine in Visual Basic:




.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoNelderMeadSolverDbl() 
        Console.WriteLine("Hello DemoNelderMeadSolverDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New NelderMeadSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) ' result is correct
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
    End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoNelderMeadSolverDbl() 
    matRes: 
     1.000014; 
     1.000029; 

    Y = F(matRes): 
     0.000000; 
     0.000000; 

    Norm: 2.96378497762668E-10














|newpage|

CMAes solver
------------------------------------------------------------

.. method:: ctxboost.CMAes(f, fjac, matInput)

CMA-ES stands for covariance matrix adaptation evolution strategy. Evolution strategies (ES) are stochastic, derivative-free methods for numerical optimization of non-linear or non-convex continuous optimization problems. 

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat135`.



**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.





**Example:**


The routine in Python:

.. code-block:: pycon

    def demo_CMAesCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the CMAes solver
        matRes = ctx.cMAesSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)


The same routine in Visual Basic:




.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoCMAesSolverDbl() 
        Console.WriteLine("Hello DemoCMAesSolverDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New CMAesSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
    End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoCMAesSolverDbl() 
    matRes: 
     0.999140; 
     0.998260; 

    Y = F(matRes): 
     0.000001; 
     0.000000; 

    Norm: 7.83903245823684E-07






|newpage|

BFGS Solver
------------------------------------------------------

.. method:: ctxboost.BFGS(f, fjac, matInput)

The Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm is an iterative method for solving unconstrained nonlinear optimization problems.

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat133`.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.




**Example:**

The routine in Python:

.. code-block:: pycon

    def demo_BfgsCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the Bfgs solver
        matRes = ctx.bfgsSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)


The same routine in Visual Basic:

.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoBfgsSolverClassDbl() 
        Console.WriteLine("Hello DemoBfgsSolverClassDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New BfgsSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
   End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoBfgsSolverClassDbl() 
    matRes: 
    0.999999951430365, 
    0.999999899650162, 

    Y = F(matRes): 
    3.38978598395966E-15, 
    0, 

    Norm: 3.38978598395966E-15








|newpage|

L-BFGS Solver
---------------------------------------------------------

.. method:: ctxboost.LBFGS(f, fjac, matInput)

Limited-memory BFGS (L-BFGS or LM-BFGS) is an optimization algorithm in the family of quasi-Newton methods that approximates the Broyden-Fletcher-Goldfarb-Shanno algorithm (BFGS) using a limited amount of computer memory.

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat134`.



**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.




**Example:**


The routine in Python:

.. code-block:: pycon

    def demo_LBfgsCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the LBfgs solver
        matRes = ctx.lbfgsBSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)


The same routine in Visual Basic:



.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoLbfgsSolverDbl() 
        Console.WriteLine("Hello DemoLbfgsSolverDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New LbfgsSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
    End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoLbfgsSolverDbl() 
    matRes: 
     1.000000; 
     1.000000; 

    Y = F(matRes): 
     0.000000; 
     0.000000; 

    Norm: 7.41089272169439E-14




|newpage|

Gradient descent solver
-----------------------------------------------------------------

.. method:: ctxboost.GradientDescent(f, fjac, matInput)

Gradient descent is a first-order iterative optimization algorithm for finding a local minimum of a differentiable function. 

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat133`. and  https://en.wikipedia.org/wiki/Gradient_descent.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.



**Example:**

The routine in Python:

.. code-block:: pycon

    def demo_GradientDescentCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the GradientDescentSolver solver
        matRes = ctx.gradientDescentSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)


The same routine in Visual Basic:

.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoBfgsSolverClassDbl() 
        Console.WriteLine("Hello DemoBfgsSolverClassDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New BfgsSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
   End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoBfgsSolverClassDbl() 
    matRes: 
    0.999999951430365, 
    0.999999899650162, 

    Y = F(matRes): 
    3.38978598395966E-15, 
    0, 

    Norm: 3.38978598395966E-15




|newpage|

Conjugate gradient descent solver
-----------------------------------------------------------

.. method:: ctxboost.ConjugateGradientDescent(f, fjac, matInput)

The conjugate gradient method is an algorithm for the numerical solution of particular systems of linear equations, namely those whose matrix is symmetric and positive-definite. The conjugate gradient method can also be used to solve unconstrained optimization problems such as energy minimization.  

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat133`. and  https://en.wikipedia.org/wiki/Conjugate\_gradient\_method.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.



**Example:**

The routine in Python:

.. code-block:: pycon

    def demo_GradientDescentCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the GradientDescentSolver solver
        matRes = ctx.gradientDescentSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)




**Example:**

.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoConjugatedGradientDescentSolverDbl() 
        Console.WriteLine("Hello DemoConjugatedGradientDescentSolverDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New ConjugatedGradientDescentSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
   End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoConjugatedGradientDescentSolverDbl() 
    matRes: 
     0.999964; 
     0.999928; 

    Y = F(matRes): 
     0.000000; 
     0.000000; 

    Norm: 1.3055097726625E-09




|newpage|

Newton descent solver (description needs correction)
-----------------------------------------------------------

.. method:: ctxboost.NewtonDescent(f, fjac, matInput)

The conjugate gradient method is an algorithm for the numerical solution of particular systems of linear equations, namely those whose matrix is symmetric and positive-definite. The conjugate gradient method can also be used to solve unconstrained optimization problems such as energy minimization.  

See also: :cite:t:`Wieschollek2016`,  Wikipedia :cite:p:`WikipediaMat133`. and  https://en.wikipedia.org/wiki/Conjugate\_gradient\_method.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.



**Example:**

The routine in Python:

.. code-block:: pycon

    def demo_GradientDescentCtx(ctx):

        # The function to optimize
        def matF1(X, Y):
            t1 = 1 - X[0]
            t2 = X[1] - X[0] * X[0]
            Y[0] = t1 * t1 + 100 * t2 * t2

        # The Jacobi function
        def matF2(X, Y):
            Y[0] = -2 * (1 - X[0]) + 200 * (X[1] - X[0] * X[0]) * (-2 * X[0])
            Y[1] = 200 * (X[1] - X[0] * X[0])

        # This defines the start vector
        r = 2
        c = 1
        X = ctx.matZeros(r,c)
        X[0] = 1
        X[1] = 2
        print('X: \n', X)

        # This executes the GradientDescentSolver solver
        matRes = ctx.gradientDescentSolver(matF1, matF2, X)

        # Check the result
        Y = ctx.matZeros(r,c)
        matF1(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)
        nrm = ctx.sqrt( Y[0]*Y[0] + Y[1]*Y[1]) # result is correct
        print('Norm: \n', nrm)




**Example:**

.. code-block:: vbnet

    Public Sub matF1(x As dbl_mat_t, y As dbl_mat_t)        
        Dim t1 As Double = 1 - x(0)
        Dim t2 As Double = x(1) - x(0) * x(0)
        y(0) = t1 * t1 + 100 * t2 * t2
    End Sub

    Public Sub matF2(x As dbl_mat_t, y As dbl_mat_t)
        y(0) = -2 * (1 - x(0)) + 200 * (x(1) - x(0) * x(0)) * (-2 * x(0))
        y(1) = 200 * (x(1) - x(0) * x(0))
    End Sub

    Sub DemoConjugatedGradientDescentSolverDbl() 
        Console.WriteLine("Hello DemoConjugatedGradientDescentSolverDbl() ")
        Dim X, Y As New dbl_mat_t()
        X.resize(2, 1)
        Y.resize(X.rows, 1)
        X(0) = 1
        X(1) = 2
        
        Dim OptLib As New ConjugatedGradientDescentSolverDbl(AddressOf matF1, AddressOf matF2, X)
        Dim matRes = OptLib.Solve()
        matRes.print("matRes: ", 15)
        matF1(matRes, Y)
        Y.print("Y = F(matRes): ", 15)
        
        Dim nrm = Math.Sqrt( Y(0)*Y(0) + Y(1)*Y(1)) 
        Console.WriteLine("Norm: {0}", nrm)
        Console.WriteLine("")
   End Sub


This produces the following output: 

.. code-block:: none

    Hello DemoConjugatedGradientDescentSolverDbl() 
    matRes: 
     0.999964; 
     0.999928; 

    Y = F(matRes): 
     0.000000; 
     0.000000; 

    Norm: 1.3055097726625E-09





