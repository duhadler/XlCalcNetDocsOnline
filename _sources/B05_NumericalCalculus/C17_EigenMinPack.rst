

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|




Eigen/MinPack: non linear optimization
===============================================================================





Multidimensional Rootfinding: Powell Hybrid
-----------------------------------------------------------------------------------------------

.. method:: ctxboost.PowellHybrid(f, fjac, guess)

This is a modified version of Powell's Hybrid method as implemented in the hybrj algorithm in minpack.  The Hybrid algorithm retains the fast convergence of Newton's method but will also reduce the residual when Newton's method is unreliable. The algorithm uses a generalized trust region to keep each step under control. 

See also: :cite:t:`Moré1980`, Eigen :cite:p:`EigenMat130`,  Wikipedia :cite:p:`WikipediaMat131`, :cite:t:`Powell1970`.



**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.





**Example:**

This is an example from the original manual of MINPACK (:cite:t:`Moré1980`).

The routine in Python:

.. code-block:: pycon

    def demo_PowellHybridCtx(ctx):

        # The function to optimize
        def XmatHybrd(x, fvec):
            n = x.size
            for k in range(n):
                temp = (3.0 - 2.0 * x[k]) * x[k]
                temp1 = ctx.zero()
                if (k!=0): temp1 = x[k-1]
                temp2 = ctx.zero()
                if (k != n-1): temp2 = x[k+1]
                fvec[k] = temp - temp1 - 2.0*temp2 + 1.0

        # The Jacobi function
        def XmatHybrdJ(x, fjac):
            n = x.size
            for k in range(n):
                for j in range(n):
                    fjac[k, j] = ctx.zero()
                fjac[k, k] = 3.0 - 4.0 * x[k]
                if (k != 0): fjac[k, k - 1] = -1
                if (k != n - 1): fjac[k, k + 1] = -2

        # This defines the start vector
        n = 9
        matInput = ctx.matZeros(n,1)
        matInput[0] = 1
        matInput[1] = 2  # entries 2 .. 8 are 0.
        print('matInput: \n', matInput)

        # This executes the PowellHybrd solver
        matRes = ctx.powellHybrd(XmatHybrd, XmatHybrdJ, matInput)

        # Check the result
        Y = ctx.matZeros(n,1)
        XmatHybrd(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)







The output of these routines:

.. code-block:: none

    Hello DemoPowellHybrdClassDbl() 

    X (solution):
    -0.570654511600659, 
    -0.681628342291231, 
    -0.701732452563471, 
    -0.704212940083752, 
    -0.701369047627289, 
    -0.691865643379914, 
    -0.665792012154689, 
    -0.596034201280817, 
    -0.416412062998472, 

    matEval =  F(X=solution):
    6.56011067690088E-09, 
    -4.17547307840493E-09, 
    -5.19316567526573E-09, 
    -2.39601338769546E-09, 
    2.02249372804886E-09, 
    4.81791939677123E-09, 
    2.57950016901987E-09, 
    -3.88373844195655E-09, 
    -1.35886191188206E-10, 




|newpage|

Nonlinear LeastSquares: Levenberg-Marquardt
------------------------------------------------------------------

.. method:: ctxboost.LevenbergMarquardt(f, fjac, matInput)

This is a robust and efficient version of the Levenberg-Marquardt algorithm as implemented
in the scaled lmder routine in minpack. The algorithm uses a generalized trust region to keep each step under control. 

See also: :cite:t:`Moré1980`, Eigen :cite:p:`EigenMat130`,  Wikipedia :cite:p:`WikipediaMat132`.


**Parameters:**

:f:   a callback matrix function  defining the system.

:fjac:   a callback matrix function defining the Jacobian of the system system.

:guess:   a matrix containing the initial guess for the solution


**Results:**

:x1:     a matrix containing the solution.




**Example:**


This is an example from the original manual of MINPACK (`Moré1980`).

The routine in Python:

.. code-block:: pycon

    def demo_LevenbergCtx(ctx):

        # The function to optimize
        def XmatLM(x, fvec):
            m = 15
            y = ctx.matZeros(m,1)
            y[0] = 1.4e-1
            y[1] = 1.8e-1
            y[2] = 2.2e-1
            y[3] = 2.5e-1
            y[4] = 2.9e-1
            y[5] = 3.2e-1
            y[6] = 3.5e-1
            y[7] = 3.9e-1
            y[8] = 3.7e-1
            y[9] = 5.8e-1
            y[10] = 7.3e-1
            y[11] = 9.6e-1
            y[12] = 1.34e0
            y[13] = 2.1e0
            y[14] = 4.39e0
            for i in range(m):
                tmp1 = i + 1
                tmp2 = m - i
                tmp3 = tmp1
                if (i >= 8): tmp3 = tmp2
                fvec[i] = y[i] - (x[0] + tmp1/(x[1]*tmp2 + x[2]*tmp3))

        # The Jacobi function
        def XmatLMJ(x, fjac):
            m = 15
            for i in range(m):
                tmp1 = i + 1
                tmp2 = m - i
                tmp3 = tmp1
                if (i >= 8): tmp3 = tmp2
                tmp4 = (x[1] * tmp2 + x[2] * tmp3)
                tmp4 = tmp4 * tmp4
                fjac[i, 0] = -1
                fjac[i, 1] = tmp1 * tmp2 / tmp4
                fjac[i, 2] = tmp1 * tmp3 / tmp4

        # This defines the start vector
        n = 3; m = 15
        matInput = ctx.matZeros(n,1)
        matInput[0] = 1
        matInput[1] = 2  # entries 2 .. 8 are 0.
        print('matInput: \n', matInput)
        # This executes the Levenberg solver
        matRes = ctx.levenberg(XmatLM, XmatLMJ, matInput)
        # Check the result
        Y = ctx.matZeros(m,1)
        XmatLM(matRes, Y)
        print('matRes: \n', matRes)
        print('Y: \n', Y)




This produces the following output:

.. code-block:: none

    Hello DemoLevenbergClassDbl() 

    X (solution):
    0.0824105765758334, 
    1.1330366534715, 
    2.34369463894115, 

    matEval =  F(X=solution):
    0.00588109515673704, 
    0.000265360346254795, 
    -0.000274673051589042, 
    -0.00654152299741256, 
    0.000823003778696318, 
    0.00129950005693674, 
    0.00446310734534455, 
    0.0199629386905548, 
    -0.0822160569476201, 
    0.0182119488681469, 
    0.0148111570102206, 
    0.0147099692233311, 
    0.0112079895785155, 
    0.00420403028888439, 
    -0.00680784758001085, 


















